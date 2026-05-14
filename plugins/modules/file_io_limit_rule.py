#!/usr/bin/python
# Copyright: (c) 2024, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: file_io_limit_rule
version_added: '3.9.0'
short_description: Manage file IO limit rules on Dell PowerStore
description:
  - Managing file IO limit rules on PowerStore storage system includes
    creating, modifying, getting details and deleting file IO limit rules.
  - File IO limit rules provide the ability to set a bandwidth limit (MB/s)
    for a file_system or nas_server.
  - When applied to a nas_server, all file_systems share the maximum bandwidth.
  - This module requires PowerStoreOS 4.1 or later.
extends_documentation_fragment:
  - dellemc.powerstore.powerstore
author:
- Rounak Adhikary (@rounak) <ansible.team@dell.com>
options:
  file_io_limit_rule_name:
    description:
      - The name of the file IO limit rule.
      - Specify either I(file_io_limit_rule_name) or I(file_io_limit_rule_id).
    type: str
  file_io_limit_rule_id:
    description:
      - The unique identifier of the file IO limit rule.
    type: str
  new_name:
    description:
      - New name for the file IO limit rule.
    type: str
  max_bw:
    description:
      - Maximum bandwidth limit in MB/s.
      - Valid range is 1 to 1000000.
    type: int
  state:
    description:
      - Define whether the file IO limit rule should exist or not.
    type: str
    required: true
    choices: ['present', 'absent']
notes:
  - Requires PowerStoreOS version 4.1 or later.
  - The I(check_mode) is supported.
'''

EXAMPLES = r'''
- name: Create a file IO limit rule
  dellemc.powerstore.file_io_limit_rule:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    file_io_limit_rule_name: "file_bw_500mb"
    max_bw: 500
    state: "present"

- name: Get file IO limit rule details
  dellemc.powerstore.file_io_limit_rule:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    file_io_limit_rule_name: "file_bw_500mb"
    state: "present"

- name: Modify a file IO limit rule bandwidth
  dellemc.powerstore.file_io_limit_rule:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    file_io_limit_rule_name: "file_bw_500mb"
    max_bw: 1000
    state: "present"

- name: Rename a file IO limit rule
  dellemc.powerstore.file_io_limit_rule:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    file_io_limit_rule_name: "file_bw_500mb"
    new_name: "file_bw_1000mb"
    state: "present"

- name: Delete a file IO limit rule
  dellemc.powerstore.file_io_limit_rule:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    file_io_limit_rule_name: "file_bw_500mb"
    state: "absent"
'''

RETURN = r'''
changed:
  description: Whether or not the resource has changed.
  returned: always
  type: bool
file_io_limit_rule_details:
  description: Details of the file IO limit rule.
  returned: When file IO limit rule exists.
  type: dict
  contains:
    id:
      description: Unique identifier.
      type: str
    name:
      description: Name of the file IO limit rule.
      type: str
    max_bw:
      description: Maximum bandwidth in MB/s.
      type: int
    policies:
      description: Associated policies.
      type: list
  sample: {
    "id": "7c6e53b1-2345-6789-bcde-f01234567890",
    "name": "file_bw_500mb",
    "max_bw": 500,
    "policies": []
  }
'''

import copy
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

LOG = utils.get_logger('file_io_limit_rule')


class PowerStoreFileIoLimitRule(object):
    """Class with File IO Limit Rule operations"""

    def __init__(self):
        """Define all parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_file_io_limit_rule_parameters())

        mutually_exclusive = [['file_io_limit_rule_name', 'file_io_limit_rule_id']]
        required_one_of = [['file_io_limit_rule_name', 'file_io_limit_rule_id']]

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
        LOG.info('Got Py4Ps instance for configuration on '
                 'PowerStore %s', self.conn)

    def get_file_io_limit_rule(self, params):
        """Get file IO limit rule by name or ID"""
        try:
            rule_id = params.get('file_io_limit_rule_id')
            rule_name = params.get('file_io_limit_rule_name')
            if rule_id:
                return self.configuration.get_file_io_limit_rule_details(rule_id)
            elif rule_name:
                rules = self.configuration.get_file_io_limit_rule_by_name(rule_name)
                if rules and len(rules) > 1:
                    self.module.fail_json(
                        msg="Multiple file IO limit rules found with name '{0}'.".format(rule_name))
                if rules and len(rules) == 1:
                    return self.configuration.get_file_io_limit_rule_details(rules[0]['id'])
            return None
        except Exception as e:
            msg = "Get file IO limit rule failed with error: {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_file_io_limit_rule_details(self, rule_id):
        try:
            return self.configuration.get_file_io_limit_rule_details(rule_id)
        except Exception as e:
            msg = "Get file IO limit rule details failed with error: {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def create_file_io_limit_rule(self, params):
        try:
            payload = {
                'name': params['file_io_limit_rule_name'],
                'max_bw': params['max_bw']
            }
            return self.configuration.create_file_io_limit_rule(payload)
        except Exception as e:
            msg = "Create file IO limit rule failed with error: {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def modify_file_io_limit_rule(self, rule_id, modify_dict):
        try:
            self.configuration.modify_file_io_limit_rule(rule_id, modify_dict)
        except Exception as e:
            msg = "Modify file IO limit rule failed with error: {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def delete_file_io_limit_rule(self, rule_id):
        try:
            self.configuration.delete_file_io_limit_rule(rule_id)
        except Exception as e:
            msg = "Delete file IO limit rule failed with error: {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def is_modify_required(self, current, desired):
        modify_dict = {}
        if desired.get('new_name') and desired['new_name'] != current.get('name'):
            modify_dict['name'] = desired['new_name']
        if desired.get('max_bw') is not None and desired['max_bw'] != current.get('max_bw'):
            modify_dict['max_bw'] = desired['max_bw']
        return modify_dict if modify_dict else None

    def validate_input(self, params):
        name = params.get('file_io_limit_rule_name')
        rule_id = params.get('file_io_limit_rule_id')
        if not name and not rule_id:
            self.module.fail_json(msg="Specify either file_io_limit_rule_name or file_io_limit_rule_id.")

    def validate_create(self, params):
        max_bw = params.get('max_bw')
        if max_bw is None:
            self.module.fail_json(msg="max_bw is required when creating a file IO limit rule.")
        self._validate_ranges(params)

    def _validate_ranges(self, params):
        max_bw = params.get('max_bw')
        if max_bw is not None:
            if max_bw < 1:
                self.module.fail_json(msg="max_bw must be at least 1 MB/s. Got {0}.".format(max_bw))
            if max_bw > 1000000:
                self.module.fail_json(msg="max_bw must not exceed 1000000 MB/s. Got {0}.".format(max_bw))


class FileIoLimitRuleExitHandler:
    def handle(self, rule_obj, rule_details, changed):
        rule_obj.result["changed"] = changed
        rule_obj.result["file_io_limit_rule_details"] = rule_details
        rule_obj.module.exit_json(**rule_obj.result)


class FileIoLimitRuleDeleteHandler:
    def handle(self, rule_obj, rule_params, rule_details, changed):
        if rule_details and rule_params['state'] == 'absent':
            if not rule_obj.module.check_mode:
                rule_obj.delete_file_io_limit_rule(rule_details['id'])
            changed = True
            rule_details = None
        FileIoLimitRuleExitHandler().handle(rule_obj, rule_details, changed)


class FileIoLimitRuleModifyHandler:
    def handle(self, rule_obj, rule_params, rule_details, changed):
        if rule_details and rule_params['state'] == 'present':
            modify_dict = rule_obj.is_modify_required(rule_details, rule_params)
            if modify_dict:
                before_dict = copy.deepcopy(rule_details)
                if not rule_obj.module.check_mode:
                    rule_obj.modify_file_io_limit_rule(rule_details['id'], modify_dict)
                    rule_details = rule_obj.get_file_io_limit_rule_details(rule_details['id'])
                changed = True
                if rule_obj.module._diff:
                    after_dict = copy.deepcopy(rule_details) if rule_details else {}
                    after_dict.update(modify_dict)
                    rule_obj.result['diff'] = dict(before=before_dict, after=after_dict)
        FileIoLimitRuleDeleteHandler().handle(rule_obj, rule_params, rule_details, changed)


class FileIoLimitRuleCreateHandler:
    def handle(self, rule_obj, rule_params, rule_details, changed):
        if not rule_details and rule_params['state'] == 'present':
            rule_obj.validate_create(rule_params)
            if not rule_obj.module.check_mode:
                result = rule_obj.create_file_io_limit_rule(rule_params)
                if result and result.get('id'):
                    rule_details = rule_obj.get_file_io_limit_rule_details(result['id'])
            changed = True
        FileIoLimitRuleModifyHandler().handle(rule_obj, rule_params, rule_details, changed)


class FileIoLimitRuleHandler:
    def handle(self, rule_obj, rule_params):
        rule_obj.validate_input(rule_params)
        rule_details = rule_obj.get_file_io_limit_rule(rule_params)
        FileIoLimitRuleCreateHandler().handle(rule_obj, rule_params, rule_details, False)


def get_powerstore_file_io_limit_rule_parameters():
    return dict(
        file_io_limit_rule_name=dict(type='str'),
        file_io_limit_rule_id=dict(type='str'),
        new_name=dict(type='str'),
        max_bw=dict(type='int'),
        state=dict(type='str', required=True, choices=['present', 'absent'])
    )


def main():
    obj = PowerStoreFileIoLimitRule()
    FileIoLimitRuleHandler().handle(obj, obj.module.params)


if __name__ == '__main__':
    main()
