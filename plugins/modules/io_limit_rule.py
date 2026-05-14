#!/usr/bin/python
# Copyright: (c) 2024, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: io_limit_rule
version_added: '3.9.0'
short_description: Manage IO limit rules on Dell PowerStore
description:
  - Managing IO limit rules on PowerStore storage system includes
    creating, modifying, getting details and deleting IO limit rules.
  - IO limit rules provide the ability to limit the bandwidth (KB/s)
    and/or IO operations per second for block storage resources.
  - This module requires PowerStoreOS 4.0 or later.
extends_documentation_fragment:
  - dellemc.powerstore.powerstore
author:
- Rounak Adhikary (@rounak) <ansible.team@dell.com>
options:
  io_limit_rule_name:
    description:
      - The name of the IO limit rule.
      - Specify either I(io_limit_rule_name) or I(io_limit_rule_id) for
        get/modify/delete operations.
    type: str
  io_limit_rule_id:
    description:
      - The unique identifier of the IO limit rule.
      - Specify either I(io_limit_rule_name) or I(io_limit_rule_id) for
        get/modify/delete operations.
    type: str
  new_name:
    description:
      - New name for the IO limit rule.
    type: str
  max_bw:
    description:
      - Maximum bandwidth limit.
      - Unit depends on I(max_bw_unit) parameter.
      - For Absolute type, API minimum is 2000 KB/s.
    type: int
  max_bw_unit:
    description:
      - Unit for the I(max_bw) value.
      - Converted to KB/s for the API call.
    type: str
    choices: ['KB/s', 'MB/s', 'GB/s']
    default: 'KB/s'
  max_iops:
    description:
      - Maximum IO operations per second limit.
      - Minimum value is 1, maximum is 2147483646.
    type: int
  burst_percentage:
    description:
      - Burst allowance percentage above the limit.
      - Valid range is 0 to 100.
    type: int
  limit_type:
    description:
      - Determines how max_iops and max_bw are applied.
      - C(absolute) means limits are absolute values.
      - C(density) means limits are per-GB of volume size.
    type: str
    choices: ['absolute', 'density']
  state:
    description:
      - Define whether the IO limit rule should exist or not.
    type: str
    required: true
    choices: ['present', 'absent']
notes:
  - Requires PowerStoreOS version 4.0 or later.
  - The I(check_mode) is supported.
'''

EXAMPLES = r'''
- name: Create an IO limit rule with IOPS and bandwidth limits
  dellemc.powerstore.io_limit_rule:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    io_limit_rule_name: "tenant_a_limits"
    limit_type: "absolute"
    max_iops: 5000
    max_bw: 102400
    max_bw_unit: "KB/s"
    burst_percentage: 20
    state: "present"

- name: Get IO limit rule details
  dellemc.powerstore.io_limit_rule:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    io_limit_rule_name: "tenant_a_limits"
    state: "present"

- name: Modify an IO limit rule
  dellemc.powerstore.io_limit_rule:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    io_limit_rule_name: "tenant_a_limits"
    max_iops: 10000
    state: "present"

- name: Create a density-based IO limit rule
  dellemc.powerstore.io_limit_rule:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    io_limit_rule_name: "density_rule"
    limit_type: "density"
    max_iops: 100
    max_bw: 10
    max_bw_unit: "MB/s"
    state: "present"

- name: Delete an IO limit rule
  dellemc.powerstore.io_limit_rule:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    io_limit_rule_name: "tenant_a_limits"
    state: "absent"
'''

RETURN = r'''
changed:
  description: Whether or not the resource has changed.
  returned: always
  type: bool
io_limit_rule_details:
  description: Details of the IO limit rule.
  returned: When IO limit rule exists.
  type: dict
  contains:
    id:
      description: The unique identifier of the IO limit rule.
      type: str
    name:
      description: The name of the IO limit rule.
      type: str
    max_bw:
      description: Maximum bandwidth in KB/s.
      type: int
    max_iops:
      description: Maximum IOPS.
      type: int
    burst_percentage:
      description: Burst percentage.
      type: int
    type:
      description: Limit type (Absolute or Density).
      type: str
    policies:
      description: Associated policies.
      type: list
  sample: {
    "id": "6b5e42b0-1234-5678-abcd-ef0123456789",
    "name": "tenant_a_limits",
    "max_bw": 102400,
    "max_iops": 5000,
    "burst_percentage": 20,
    "type": "Absolute",
    "policies": []
  }
'''

import copy
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

LOG = utils.get_logger('io_limit_rule')

BW_CONVERSION = {
    'KB/s': 1,
    'MB/s': 1024,
    'GB/s': 1048576
}

LIMIT_TYPE_MAP = {
    'absolute': 'Absolute',
    'density': 'Density'
}


class PowerStoreIoLimitRule(object):
    """Class with IO Limit Rule operations"""

    def __init__(self):
        """Define all parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_io_limit_rule_parameters())

        mutually_exclusive = [['io_limit_rule_name', 'io_limit_rule_id']]
        required_one_of = [['io_limit_rule_name', 'io_limit_rule_id']]

        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True,
            mutually_exclusive=mutually_exclusive,
            required_one_of=required_one_of
        )

        self.result = {"changed": False}
        self.conn = utils.get_powerstore_connection(
            self.module.params)
        self.provisioning = self.conn.provisioning
        self.protection = self.conn.protection
        self.configuration = self.conn.config_mgmt
        LOG.info('Got Py4Ps instance for provisioning and protection on '
                 'PowerStore %s', self.conn)

    def get_io_limit_rule(self, params):
        """Get IO limit rule by name or ID"""
        try:
            rule_id = params.get('io_limit_rule_id')
            rule_name = params.get('io_limit_rule_name')
            if rule_id:
                return self.provisioning.get_io_limit_rule_details(rule_id)
            elif rule_name:
                rules = self.provisioning.get_io_limit_rule_by_name(rule_name)
                if rules and len(rules) > 0:
                    return self.provisioning.get_io_limit_rule_details(rules[0]['id'])
            return None
        except Exception as e:
            msg = "Get IO limit rule failed with error: {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_io_limit_rule_details(self, rule_id):
        """Get IO limit rule details by ID"""
        try:
            return self.provisioning.get_io_limit_rule_details(rule_id)
        except Exception as e:
            msg = "Get IO limit rule details failed with error: {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def create_io_limit_rule(self, params):
        """Create a new IO limit rule"""
        try:
            payload = {
                'name': params['io_limit_rule_name'],
                'type': LIMIT_TYPE_MAP.get(params['limit_type'], params['limit_type'])
            }
            max_bw = params.get('max_bw')
            if max_bw is not None:
                unit = params.get('max_bw_unit') or 'KB/s'
                payload['max_bw'] = max_bw * BW_CONVERSION.get(unit, 1)
            if params.get('max_iops') is not None:
                payload['max_iops'] = params['max_iops']
            if params.get('burst_percentage') is not None:
                payload['burst_percentage'] = params['burst_percentage']
            return self.provisioning.create_io_limit_rule(payload)
        except Exception as e:
            msg = "Create IO limit rule failed with error: {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def modify_io_limit_rule(self, rule_id, modify_dict):
        """Modify an existing IO limit rule"""
        try:
            self.provisioning.modify_io_limit_rule(rule_id, modify_dict)
        except Exception as e:
            msg = "Modify IO limit rule failed with error: {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def delete_io_limit_rule(self, rule_id):
        """Delete an IO limit rule"""
        try:
            self.provisioning.delete_io_limit_rule(rule_id)
        except Exception as e:
            msg = "Delete IO limit rule failed with error: {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def is_modify_required(self, current, desired):
        """Check if modification is required"""
        modify_dict = {}
        if desired.get('new_name') and desired['new_name'] != current.get('name'):
            modify_dict['name'] = desired['new_name']
        max_bw = desired.get('max_bw')
        if max_bw is not None:
            unit = desired.get('max_bw_unit') or 'KB/s'
            converted_bw = max_bw * BW_CONVERSION.get(unit, 1)
            if converted_bw != current.get('max_bw'):
                modify_dict['max_bw'] = converted_bw
        if desired.get('max_iops') is not None and desired['max_iops'] != current.get('max_iops'):
            modify_dict['max_iops'] = desired['max_iops']
        if desired.get('burst_percentage') is not None and desired['burst_percentage'] != current.get('burst_percentage'):
            modify_dict['burst_percentage'] = desired['burst_percentage']
        return modify_dict if modify_dict else None

    def validate_input(self, params):
        """Validate input parameters"""
        name = params.get('io_limit_rule_name')
        rule_id = params.get('io_limit_rule_id')
        if not name and not rule_id:
            self.module.fail_json(msg="Specify either io_limit_rule_name or io_limit_rule_id.")

    def validate_create(self, params):
        """Validate parameters for create operation"""
        limit_type = params.get('limit_type')
        if not limit_type:
            self.module.fail_json(msg="limit_type is required when creating an IO limit rule.")
        if limit_type not in ('absolute', 'density'):
            self.module.fail_json(msg="Invalid limit_type: {0}. Must be 'absolute' or 'density'.".format(limit_type))
        max_bw = params.get('max_bw')
        max_iops = params.get('max_iops')
        if max_bw is None and max_iops is None:
            self.module.fail_json(msg="At least one of max_bw or max_iops is required when creating an IO limit rule.")
        self._validate_ranges(params)

    def _validate_ranges(self, params):
        """Validate numeric ranges"""
        max_bw = params.get('max_bw')
        max_iops = params.get('max_iops')
        burst = params.get('burst_percentage')
        limit_type = params.get('limit_type')
        if max_bw is not None:
            unit = params.get('max_bw_unit') or 'KB/s'
            converted_bw = max_bw * BW_CONVERSION.get(unit, 1)
            if limit_type == 'absolute' and converted_bw < 2000:
                self.module.fail_json(msg="max_bw must be at least 2000 KB/s for absolute type. Got {0} KB/s.".format(converted_bw))
        if max_iops is not None and max_iops < 1:
            self.module.fail_json(msg="max_iops must be at least 1. Got {0}.".format(max_iops))
        if burst is not None and (burst < 0 or burst > 100):
            self.module.fail_json(msg="burst_percentage must be between 0 and 100. Got {0}.".format(burst))


class IoLimitRuleExitHandler:
    def handle(self, rule_obj, rule_details, changed):
        rule_obj.result["changed"] = changed
        rule_obj.result["io_limit_rule_details"] = rule_details
        rule_obj.module.exit_json(**rule_obj.result)


class IoLimitRuleDeleteHandler:
    def handle(self, rule_obj, rule_params, rule_details, changed):
        if rule_details and rule_params['state'] == 'absent':
            if not rule_obj.module.check_mode:
                rule_obj.delete_io_limit_rule(rule_details['id'])
            changed = True
            rule_details = None
        IoLimitRuleExitHandler().handle(rule_obj, rule_details, changed)


class IoLimitRuleModifyHandler:
    def handle(self, rule_obj, rule_params, rule_details, changed):
        if rule_details and rule_params['state'] == 'present':
            modify_dict = rule_obj.is_modify_required(rule_details, rule_params)
            if modify_dict:
                before_dict = copy.deepcopy(rule_details)
                if not rule_obj.module.check_mode:
                    rule_obj.modify_io_limit_rule(rule_details['id'], modify_dict)
                    rule_details = rule_obj.get_io_limit_rule_details(rule_details['id'])
                changed = True
                if rule_obj.module._diff:
                    after_dict = copy.deepcopy(rule_details) if rule_details else {}
                    after_dict.update(modify_dict)
                    rule_obj.result['diff'] = dict(before=before_dict, after=after_dict)
        IoLimitRuleDeleteHandler().handle(rule_obj, rule_params, rule_details, changed)


class IoLimitRuleCreateHandler:
    def handle(self, rule_obj, rule_params, rule_details, changed):
        if not rule_details and rule_params['state'] == 'present':
            rule_obj.validate_create(rule_params)
            rule_obj._validate_ranges(rule_params)
            if not rule_obj.module.check_mode:
                result = rule_obj.create_io_limit_rule(rule_params)
                rule_details = rule_obj.get_io_limit_rule_details(result['id'])
            changed = True
        IoLimitRuleModifyHandler().handle(rule_obj, rule_params, rule_details, changed)


class IoLimitRuleHandler:
    def handle(self, rule_obj, rule_params):
        rule_obj.validate_input(rule_params)
        rule_details = rule_obj.get_io_limit_rule(rule_params)
        IoLimitRuleCreateHandler().handle(rule_obj, rule_params, rule_details, False)


def get_powerstore_io_limit_rule_parameters():
    return dict(
        io_limit_rule_name=dict(type='str'),
        io_limit_rule_id=dict(type='str'),
        new_name=dict(type='str'),
        max_bw=dict(type='int'),
        max_bw_unit=dict(type='str', choices=['KB/s', 'MB/s', 'GB/s'], default='KB/s'),
        max_iops=dict(type='int'),
        burst_percentage=dict(type='int'),
        limit_type=dict(type='str', choices=['absolute', 'density']),
        state=dict(type='str', required=True, choices=['present', 'absent'])
    )


def main():
    """ Create PowerStore IO limit rule object and perform action on it
        based on user input from playbook"""
    obj = PowerStoreIoLimitRule()
    IoLimitRuleHandler().handle(obj, obj.module.params)


if __name__ == '__main__':
    main()
