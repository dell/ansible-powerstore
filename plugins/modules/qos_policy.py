#!/usr/bin/python
# Copyright: (c) 2024, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: qos_policy
version_added: '3.9.0'
short_description: Manage QoS performance policies on Dell PowerStore
description:
  - Managing QoS performance policies on PowerStore storage system includes
    creating, modifying, getting details and deleting QoS policies.
  - QoS policies associate IO limit rules with block or file storage resources.
  - Policy type C(QoS) uses I(io_limit_rule) for block resources (volumes,
    volume groups). Requires PowerStoreOS 4.0+.
  - Policy type C(File_Performance) uses I(file_io_limit_rule) for file
    resources (NAS servers, file systems). Requires PowerStoreOS 4.1+.
extends_documentation_fragment:
  - dellemc.powerstore.powerstore
author:
- Rounak Adhikary (@rounak) <ansible.team@dell.com>
options:
  qos_policy_name:
    description:
      - The name of the QoS policy.
    type: str
  qos_policy_id:
    description:
      - The unique identifier of the QoS policy.
    type: str
  new_name:
    description:
      - New name for the QoS policy.
    type: str
  description:
    description:
      - Description for the QoS policy.
    type: str
  policy_type:
    description:
      - Type of QoS policy.
      - C(QoS) for block resources (requires io_limit_rule).
      - C(File_Performance) for file resources (requires file_io_limit_rule).
    type: str
    choices: ['QoS', 'File_Performance']
  io_limit_rule:
    description:
      - Name or ID of the IO limit rule to associate.
      - Only valid for C(QoS) policy type.
    type: str
  file_io_limit_rule:
    description:
      - Name or ID of the file IO limit rule to associate.
      - Only valid for C(File_Performance) policy type.
    type: str
  state:
    description:
      - Define whether the QoS policy should exist or not.
    type: str
    required: true
    choices: ['present', 'absent']
notes:
  - QoS policy type requires PowerStoreOS 4.0+.
  - File_Performance policy type requires PowerStoreOS 4.1+.
  - The I(check_mode) is supported.
  - Policies cannot be deleted if assigned to storage resources.
'''

EXAMPLES = r'''
- name: Create a QoS policy for block resources
  dellemc.powerstore.qos_policy:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    qos_policy_name: "gold_qos"
    description: "Gold tier QoS policy"
    policy_type: "QoS"
    io_limit_rule: "tenant_a_limits"
    state: "present"

- name: Create a File_Performance policy
  dellemc.powerstore.qos_policy:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    qos_policy_name: "file_gold_qos"
    policy_type: "File_Performance"
    file_io_limit_rule: "file_bw_500mb"
    state: "present"

- name: Get QoS policy details
  dellemc.powerstore.qos_policy:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    qos_policy_name: "gold_qos"
    state: "present"

- name: Modify QoS policy - change IO limit rule
  dellemc.powerstore.qos_policy:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    qos_policy_name: "gold_qos"
    io_limit_rule: "tenant_b_limits"
    state: "present"

- name: Delete a QoS policy
  dellemc.powerstore.qos_policy:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    qos_policy_name: "gold_qos"
    state: "absent"
'''

RETURN = r'''
changed:
  description: Whether or not the resource has changed.
  returned: always
  type: bool
qos_policy_details:
  description: Details of the QoS policy.
  returned: When QoS policy exists.
  type: dict
  contains:
    id:
      description: Unique identifier of the policy.
      type: str
    name:
      description: Name of the policy.
      type: str
    type:
      description: Policy type (QoS or File_Performance).
      type: str
    description:
      description: Policy description.
      type: str
    io_limit_rule:
      description: Associated IO limit rule (QoS type).
      type: dict
    file_io_limit_rule:
      description: Associated file IO limit rule (File_Performance type).
      type: dict
  sample: {
    "id": "8d7f64c2-3456-7890-cdef-012345678901",
    "name": "gold_qos",
    "type": "QoS",
    "description": "Gold tier QoS policy",
    "io_limit_rule": {"id": "rule_id", "name": "tenant_a_limits"}
  }
'''

import copy
import re
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

LOG = utils.get_logger('qos_policy')

UUID_RE = re.compile(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')


class PowerStoreQosPolicy(object):
    """Class with QoS Policy operations"""

    def __init__(self):
        """ Define all parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_qos_policy_parameters())

        mutually_exclusive = [['qos_policy_name', 'qos_policy_id']]
        required_one_of = [['qos_policy_name', 'qos_policy_id']]

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
        LOG.info('Got Py4Ps instance for provisioning, protection and configuration on '
                 'PowerStore %s', self.conn)

    def get_qos_policy(self, params):
        try:
            policy_id = params.get('qos_policy_id')
            policy_name = params.get('qos_policy_name')
            if policy_id:
                return self.protection.get_policy_details(policy_id)
            elif policy_name:
                policies = self.protection.get_policy_by_name(policy_name)
                if policies and len(policies) > 0:
                    return self.protection.get_policy_details(policies[0]['id'])
            return None
        except Exception as e:
            msg = "Get QoS policy failed with error: {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_qos_policy_details(self, policy_id):
        try:
            return self.protection.get_policy_details(policy_id)
        except Exception as e:
            msg = "Get QoS policy details failed with error: {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def create_qos_policy(self, params, resolved):
        try:
            payload = {'name': params['qos_policy_name']}
            if params.get('description'):
                payload['description'] = params['description']
            if resolved.get('io_limit_rule_id'):
                payload['io_limit_rule_id'] = resolved['io_limit_rule_id']
            if resolved.get('file_io_limit_rule_id'):
                payload['file_io_limit_rule_id'] = resolved['file_io_limit_rule_id']
            return self.protection.create_policy(payload)
        except Exception as e:
            msg = "Create QoS policy failed with error: {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def modify_qos_policy(self, policy_id, modify_dict):
        try:
            self.protection.modify_policy(policy_id, modify_dict)
        except Exception as e:
            msg = "Modify QoS policy failed with error: {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def delete_qos_policy(self, policy_id):
        try:
            self.protection.delete_policy(policy_id)
        except Exception as e:
            msg = "Delete QoS policy failed with error: {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def resolve_io_limit_rule(self, rule_name_or_id):
        if not rule_name_or_id:
            return None
        if UUID_RE.match(rule_name_or_id):
            return rule_name_or_id
        try:
            rules = self.provisioning.get_io_limit_rule_by_name(rule_name_or_id)
            if rules and len(rules) > 0:
                return rules[0]['id']
            self.module.fail_json(msg="IO limit rule '{0}' not found.".format(rule_name_or_id))
        except Exception as e:
            msg = "Failed to resolve IO limit rule: {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def resolve_file_io_limit_rule(self, rule_name_or_id):
        if not rule_name_or_id:
            return None
        if UUID_RE.match(rule_name_or_id):
            return rule_name_or_id
        try:
            rules = self.configuration.get_file_io_limit_rule_by_name(rule_name_or_id)
            if rules and len(rules) > 0:
                return rules[0]['id']
            self.module.fail_json(msg="File IO limit rule '{0}' not found.".format(rule_name_or_id))
        except Exception as e:
            msg = "Failed to resolve file IO limit rule: {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def is_modify_required(self, current, desired, resolved):
        modify_dict = {}
        if desired.get('new_name') and desired['new_name'] != current.get('name'):
            modify_dict['name'] = desired['new_name']
        if desired.get('description') is not None and desired['description'] != current.get('description'):
            modify_dict['description'] = desired['description']
        if resolved.get('io_limit_rule_id') and resolved['io_limit_rule_id'] != current.get('io_limit_rule_id'):
            modify_dict['io_limit_rule_id'] = resolved['io_limit_rule_id']
        if resolved.get('file_io_limit_rule_id') and \
                resolved['file_io_limit_rule_id'] != current.get('file_io_limit_rule_id'):
            modify_dict['file_io_limit_rule_id'] = resolved['file_io_limit_rule_id']
        return modify_dict if modify_dict else None

    def validate_input(self, params):
        name = params.get('qos_policy_name')
        policy_id = params.get('qos_policy_id')
        if not name and not policy_id:
            self.module.fail_json(msg="Specify either qos_policy_name or qos_policy_id.")

    def validate_create(self, params):
        policy_type = params.get('policy_type')
        if not policy_type:
            self.module.fail_json(msg="policy_type is required when creating a QoS policy.")
        if policy_type == 'QoS':
            if not params.get('io_limit_rule'):
                self.module.fail_json(msg="io_limit_rule is required for QoS policy type.")
            if params.get('file_io_limit_rule'):
                self.module.fail_json(msg="file_io_limit_rule is not valid for QoS policy type. Use io_limit_rule.")
        elif policy_type == 'File_Performance':
            if not params.get('file_io_limit_rule'):
                self.module.fail_json(msg="file_io_limit_rule is required for File_Performance policy type.")


class QosPolicyExitHandler:
    def handle(self, policy_obj, policy_details, changed):
        policy_obj.result["changed"] = changed
        policy_obj.result["qos_policy_details"] = policy_details
        policy_obj.module.exit_json(**policy_obj.result)


class QosPolicyDeleteHandler:
    def handle(self, policy_obj, policy_params, policy_details, changed):
        if policy_details and policy_params['state'] == 'absent':
            if not policy_obj.module.check_mode:
                policy_obj.delete_qos_policy(policy_details['id'])
            changed = True
            policy_details = None
        QosPolicyExitHandler().handle(policy_obj, policy_details, changed)


class QosPolicyModifyHandler:
    def handle(self, policy_obj, policy_params, policy_details, resolved, changed):
        if policy_details and policy_params['state'] == 'present':
            modify_dict = policy_obj.is_modify_required(policy_details, policy_params, resolved)
            if modify_dict:
                before_dict = copy.deepcopy(policy_details)
                if not policy_obj.module.check_mode:
                    policy_obj.modify_qos_policy(policy_details['id'], modify_dict)
                    policy_details = policy_obj.get_qos_policy_details(policy_details['id'])
                changed = True
                if policy_obj.module._diff:
                    after_dict = copy.deepcopy(policy_details) if policy_details else {}
                    after_dict.update(modify_dict)
                    policy_obj.result['diff'] = dict(before=before_dict, after=after_dict)
        QosPolicyDeleteHandler().handle(policy_obj, policy_params, policy_details, changed)


class QosPolicyCreateHandler:
    def handle(self, policy_obj, policy_params, policy_details, resolved, changed):
        if not policy_details and policy_params['state'] == 'present':
            policy_obj.validate_create(policy_params)
            if not policy_obj.module.check_mode:
                result = policy_obj.create_qos_policy(policy_params, resolved)
                if result and result.get('id'):
                    policy_details = policy_obj.get_qos_policy_details(result['id'])
            changed = True
        QosPolicyModifyHandler().handle(policy_obj, policy_params, policy_details, resolved, changed)


class QosPolicyHandler:
    def handle(self, policy_obj, policy_params):
        policy_obj.validate_input(policy_params)
        resolved = {}
        if policy_params.get('io_limit_rule'):
            resolved['io_limit_rule_id'] = policy_obj.resolve_io_limit_rule(policy_params['io_limit_rule'])
        if policy_params.get('file_io_limit_rule'):
            resolved['file_io_limit_rule_id'] = policy_obj.resolve_file_io_limit_rule(
                policy_params['file_io_limit_rule'])
        policy_details = policy_obj.get_qos_policy(policy_params)
        QosPolicyCreateHandler().handle(policy_obj, policy_params, policy_details, resolved, False)


def get_powerstore_qos_policy_parameters():
    return dict(
        qos_policy_name=dict(type='str'),
        qos_policy_id=dict(type='str'),
        new_name=dict(type='str'),
        description=dict(type='str'),
        policy_type=dict(type='str', choices=['QoS', 'File_Performance']),
        io_limit_rule=dict(type='str'),
        file_io_limit_rule=dict(type='str'),
        state=dict(type='str', required=True, choices=['present', 'absent'])
    )


def main():
    obj = PowerStoreQosPolicy()
    QosPolicyHandler().handle(obj, obj.module.params)


if __name__ == '__main__':
    main()
