#!/usr/bin/python
# Copyright: (c) 2021, DellEMC
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

""" Ansible module for managing roles on PowerStore"""
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: role

version_added: '1.3.0'

short_description: Get details of the roles present on the PowerStore storage
                   system.

description:
- Manage role in PowerStore storage system includes getting the details of a
  role.

extends_documentation_fragment:
  - dellemc.powerstore.dellemc_powerstore.powerstore

author:
- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>
options:
  role_name:
    description:
    - Name of the role.
    type: str
  role_id:
    description:
    - Id of the role.
    type: str
  state:
    description:
    - Define whether the role should exist or not.
    - present, indicates that the role should exist on the system.
    - absent, indicates that the role should not exist on the system.
    type: str
    required: true
    choices: ['absent', 'present']

notes:
- Only getting the details of the role is supported by the ansible module.
- Creation, modification and deletion of roles is not supported by the ansible
  modules.

'''
EXAMPLES = r'''

- name: Get the details of role by name
  role:
    array_ip: "{{array_ip}}"
    verifycert: "{{verify_cert}}"
    user: "{{user}}"
    password: "{{password}}"
    role_name: "Administrator"
    state: "present"

- name: Get the details of role by id
  role:
    array_ip: "{{array_ip}}"
    verifycert: "{{verify_cert}}"
    user: "{{user}}"
    password: "{{password}}"
    role_id: "1"
    state: "present"
'''
RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: True

role_details:
    description: The role details.
    type: complex
    returned: When role exists.
    contains:
        id:
            description: The ID of the role.
            type: str
        name:
            description: The name of the role.
            type: str
        is_built_in:
            description: Indicates whether the role is built-in.
            type: bool
        description:
            description: Description of the role.
            type: str
'''

from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import dellemc_ansible_powerstore_utils as utils
from ansible.module_utils.basic import AnsibleModule

LOG = utils.get_logger('role')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.4.0'


class PowerStoreRole(object):
    """Class with role operations"""

    def __init__(self):
        """ Define all parameters required by this module"""

        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_role_parameters())

        # initialize the ansible module
        mut_ex_args = [
            ['role_id', 'role_name']
        ]

        required_one_of = [['role_id', 'role_name']]
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mut_ex_args,
            required_one_of=required_one_of
        )

        msg = 'HAS_PY4PS = {0} , IMPORT_ERROR = {1}'.format(HAS_PY4PS,
                                                            IMPORT_ERROR)
        LOG.info(msg)

        if not HAS_PY4PS:
            self.module.fail_json(msg=IMPORT_ERROR)
        msg = 'IS_SUPPORTED_PY4PS_VERSION = {0} , VERSION_ERROR = {1}' \
            .format(IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR)
        LOG.info(msg)

        if not IS_SUPPORTED_PY4PS_VERSION:
            self.module.fail_json(msg=VERSION_ERROR)

        # result is a dictionary that contains changed status and
        # role details
        self.result = {"changed": False, "role_details": {}}

        self.conn = utils.get_powerstore_connection(
            self.module.params, application_type=APPLICATION_TYPE)
        self.provisioning = self.conn.provisioning
        msg = 'Got Py4Ps instance for provisioning on' \
              ' PowerStore {0}'.format(self.conn)
        LOG.info(msg)
        self.configuration = self.conn.config_mgmt
        msg = 'Got Py4Ps instance for configuring cluster on' \
              ' PowerStore {0}'.format(self.conn)
        LOG.info(msg)

    def get_role_details(self, role_name, role_id):
        """
        Get the details of role
        :param role_name: Name of the role
        :param role_id: Id of the role
        :return: Details of role if exists else None.
        """
        name_or_id = role_name if role_name else role_id
        try:
            if role_name:
                role_details = self.configuration.get_role_by_name(role_name)
            else:
                role_details = self.configuration.get_role_details(role_id)
            return role_details
        except Exception as e:
            err_msg = "Get details for role: {0} failed with error: " \
                      "{1}".format(name_or_id, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(err_msg)
                return None
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg, **utils.failure_codes(e))

    def perform_module_operation(self):
        """
        Perform different actions on  role module based on parameters
        chosen in playbook
        """
        role_id = self.module.params['role_id']
        role_name = self.module.params['role_name']
        state = self.module.params['state']
        changed = False
        # Get the details of role
        role_details = self.get_role_details(role_name, role_id)

        # Create role
        if not role_details and state == 'present':
            name_or_id = role_name if role_name else role_id
            err_msg = "Role: {0} doesn't exist on the PowerStore storage " \
                      "system. Creation of a role is not supported by " \
                      "ansible module.".format(name_or_id)
            self.module.fail_json(msg=err_msg)

        # Delete role
        if state == "absent" and role_details:
            self.module.fail_json(
                msg="Deletion of role is not supported by ansible module. Only"
                    " get details of role is supported. Please enter a valid "
                    "operation.")

        self.result["changed"] = changed
        self.result["role_details"] = role_details
        self.module.exit_json(**self.result)


def get_powerstore_role_parameters():
    """This method provides parameters required for the ansible role
    module on PowerStore"""
    return dict(
        role_name=dict(), role_id=dict(),
        state=dict(required=True, choices=['present', 'absent'])
    )


def main():
    """ Create role object and perform actions on it
    based on user input from playbook"""

    obj = PowerStoreRole()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
