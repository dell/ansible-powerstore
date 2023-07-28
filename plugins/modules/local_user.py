#!/usr/bin/python
# Copyright: (c) 2021, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

""" Ansible module for managing local users on PowerStore"""
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: local_user
version_added: '1.3.0'
short_description: Local user operations for PowerStore Storage System
description:
- Supports the provisioning operations on a Local user such as create, modify,
  delete and get the details of a local user.

extends_documentation_fragment:
  - dellemc.powerstore.powerstore

author:
- Arindam Datta (@dattaarindam) <ansible.team@dell.com>

options:
  user_name:
    description:
    - Name of the local user account. Mutually exclusive with I(user_id).
    - Mandatory only for create operation.
    type: str
  user_id:
    description:
    - Unique identifier of the local user account.
    - Mutually exclusive with I(user_name).
    type: str
  user_password:
    description:
    - Password for the new local user account to be created.
    - Mandatory only for create operation.
    type: str
  new_password:
    description:
    - New password for the existing local user account.
    type: str
  role_name:
    description:
    - The name of the role to which the local user account will be mapped.
    - It is mutually exclusive with I(role_id).
    type: str
  role_id:
    description:
    - The unique identifier of the role to which the local user account will
      be mapped.
    - It is mutually exclusive with I(role_name).
    type: int
  is_locked:
    description:
    - Whether the user account is locked or not.
    - Defaults to C(false) at creation time.
    type: bool
  state:
    description:
    - Define whether the local user should exist or not.
    choices: ['absent', 'present']
    required: true
    type: str

notes:
- The I(check_mode) is not supported.
'''

EXAMPLES = r'''
- name: Create local user
  dellemc.powerstore.local_user:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    user_name: "ansible_user_1"
    user_password: "Password123#"
    role_name: "role_1"
    is_locked: false
    state: "present"

- name: Get the details local user with user id
  dellemc.powerstore.local_user:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    user_id: "{{user_id}}"
    state: "present"

- name: Get the details local user with user name
  dellemc.powerstore.local_user:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    user_name: "ansible_user_1"
    state: "present"

- name: Modify attributes of local user
  dellemc.powerstore.local_user:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    user_name: "ansible_user_1"
    user_password: "Password123#"
    new_password: "Ansible123#"
    role_id: 4
    is_locked: true
    state: "present"

- name: Delete local user
  dellemc.powerstore.local_user:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    user_name: "ansible_user_1"
    state: "absent"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"
local_user_details:
    description: Details of the local user.
    returned: When local user exists
    type: complex
    contains:
        id:
            description: The system generated ID given to the local user.
            type: str
        name:
            description: Name of the local user.
            type: str
        is_built_in:
            description: Whether the user account is built-in or not.
            type: bool
        is_locked:
            description: Whether the user account is locked or not. Defaults
                         to false at creation time.
            type: bool
        is_default_password:
            description: Whether the user account has a default password or
                         not. Only applies to default user accounts
            type: bool
        role_id:
            description: Unique identifier of the role local user account is
                         mapped to.
            type: str
        role_name:
            description: Name of the role to which local user account is
                         mapped.
            type: str
    sample: {
        "id": "272",
        "is_built_in": false,
        "is_default_password": false,
        "is_locked": false,
        "name": "sampleuser",
        "role_id": "1",
        "role_name": "Administrator"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import utils

LOG = utils.get_logger('local_user')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/2.1.0'


class PowerStoreLocalUser(object):
    """Local user operations"""
    cluster_name = None
    cluster_global_id = None
    valid_role_id = None

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_local_user_parameters())

        mutually_exclusive = [['user_name', 'user_id'],
                              ['role_id', 'role_name']]
        required_one_of = [['user_name', 'user_id']]

        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mutually_exclusive,
            required_one_of=required_one_of
        )
        msg = 'HAS_PY4PS = {0} , IMPORT_ERROR = ' \
              '{1}'.format(HAS_PY4PS, IMPORT_ERROR)
        LOG.info(msg)
        if HAS_PY4PS is False:
            self.module.fail_json(msg=IMPORT_ERROR)
        msg = 'IS_SUPPORTED_PY4PS_VERSION = {0} , ' \
              'VERSION_ERROR = {1}'.format(IS_SUPPORTED_PY4PS_VERSION,
                                           VERSION_ERROR)
        LOG.info(msg)
        if IS_SUPPORTED_PY4PS_VERSION is False:
            self.module.fail_json(msg=VERSION_ERROR)

        self.conn = utils.get_powerstore_connection(
            self.module.params,
            application_type=APPLICATION_TYPE)
        self.provisioning = self.conn.provisioning
        msg = 'Got Py4ps instance for provisioning on ' \
              'PowerStore {0}'.format(self.conn)
        LOG.info(msg)
        self.configuration = self.conn.config_mgmt
        msg = 'Got Py4ps instance for configuration on' \
              ' PowerStore {0}'.format(self.configuration)
        LOG.info(msg)

    def get_role(self, role_id=None, role_name=None):
        """Get the details of a role on a PowerStore storage system"""
        try:
            role_details = dict()
            role_dtls = None

            if role_id:
                role_dtls = self.configuration.get_role_details(role_id)

            if role_name:
                role_dtls = self.configuration.get_role_by_name(role_name)

            if role_dtls:
                role_details['id'] = role_dtls['id']
                role_details['name'] = role_dtls['name']

            if not role_details:
                raise NameError("Specified role does not exist")

            return role_details
        except Exception as e:
            msg = "Failed to get the role with error {0} ".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_local_user_details(self, user_id=None, user_name=None):
        """Get the details of a local user on a PowerStore storage system"""

        try:
            msg = 'Getting Local User Details with user_id {0}, ' \
                  'user_name {1}'.format(user_id, user_name)
            LOG.info(msg)
            usr_details = None
            if user_id:
                usr_details = \
                    self.configuration.get_local_user_details(user_id)
            elif user_name:
                usr_details = \
                    self.configuration.get_local_user_by_name(user_name)
                if usr_details:
                    return usr_details

            msg = 'Successfully Got Local User Details' \
                  ' {0}'.format(usr_details)
            LOG.info(msg)
            return usr_details

        except Exception as e:
            msg = 'Get local user details for PowerStore array name : ' \
                  '{0} , global id : {1} failed with error' \
                  ' {2} '.format(self.cluster_name, self.cluster_global_id,
                                 str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR \
                    and e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def create_local_user(self, user_name):
        """Create a local user."""
        try:
            LOG.info("Attempting to create local user with name "
                     "%s", user_name)
            user_password = self.module.params['user_password']

            create_params = dict()
            if user_name:
                create_params['name'] = user_name
            if user_password:
                create_params['password'] = user_password
            if self.valid_role_id:
                create_params['role_id'] = self.valid_role_id
            resp = self.configuration.create_local_user(
                create_params=create_params)

            usr_details = None
            if resp:
                usr_details = self.get_local_user_details(user_id=resp['id'])

            LOG.info("Successfully Created Local User with "
                     "details : %s", usr_details)

            return usr_details

        except Exception as e:
            msg = 'Create local user with name {0} on PowerStore array ' \
                  'name : {1} , global id : {2} failed with ' \
                  'error {3} '.format(user_name, self.cluster_name,
                                      self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def delete_local_user(self, user_id):
        """Deletes a local_user"""
        try:
            LOG.info("Attempting to delete local_user id "
                     "%s", user_id)

            self.configuration.delete_local_user(user_id=user_id)
            return True
        except Exception as e:
            msg = 'Failed to delete local user id {0} with ' \
                  'error {1}'.format(user_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_clusters(self):
        """Get the clusters"""
        try:
            clusters = self.provisioning.get_cluster_list()
            return clusters

        except Exception as e:
            msg = 'Failed to get the clusters with ' \
                  'error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def is_modify_required(self, user_details):
        """To get the details of the field to be modified."""

        try:
            LOG.info("User details: %s", user_details)
            modify_dict = dict()
            user_password = self.module.params['user_password']
            new_password = self.module.params['new_password']
            is_locked = self.module.params['is_locked']

            if new_password:
                if not user_password:
                    msg = 'Please provide a valid user_password. ' \
                          'user_password along with new_password is required' \
                          ' to update password.'
                    LOG.error(msg)
                    self.module.fail_json(msg=msg)
                if new_password != user_password:
                    modify_dict['current_password'] = user_password
                    modify_dict['password'] = new_password
            if self.valid_role_id and \
                    user_details['role_id'] != self.valid_role_id:
                modify_dict['role_id'] = self.valid_role_id
            if is_locked is not None\
                    and user_details['is_locked'] != is_locked:
                modify_dict['is_locked'] = is_locked

            if modify_dict:
                return modify_dict
            else:
                return None

        except Exception as e:
            msg = 'Failed to determine if local user instance need ' \
                  'to modified with error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def modify_local_user(self, user_id, modify_params):
        """Perform modify operations on a local user"""

        try:
            self.configuration.modify_local_user(
                local_user_id=user_id, modify_parameters=modify_params)
            return True
        except Exception as e:
            msg = 'Failed to modify local user instance ' \
                  'with error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def perform_module_operation(self):
        """ Perform various module operations"""
        clusters = self.get_clusters()
        if len(clusters) > 0:
            self.cluster_name = clusters[0]['name']
            self.cluster_global_id = clusters[0]['id']
        else:
            self.module.fail_json(
                msg="Unable to find any active cluster on this array ")

        user_id = self.module.params['user_id']
        user_name = self.module.params['user_name']
        user_password = self.module.params['user_password']
        new_password = self.module.params['new_password']
        role_name = self.module.params['role_name']
        role_id = self.module.params['role_id']
        state = self.module.params['state']

        # result is a dictionary to contain end state and local user details
        changed = False
        result = dict(
            changed=False,
            local_user_details=None
        )

        modify_params = None

        if role_id or role_name:
            role_details = self.get_role(role_id=role_id, role_name=role_name)
            self.valid_role_id = role_details.get('id')

        usr_details = self.get_local_user_details(
            user_id=user_id, user_name=user_name)
        if usr_details:
            modify_params = self.is_modify_required(user_details=usr_details)

        if not usr_details and state == 'present':
            if not (user_name and user_password and self.valid_role_id):
                msg = "user_name and user_password and role " \
                      "details are required to create a local user"
                LOG.error(msg)
                self.module.fail_json(msg=msg)
            if new_password is not None:
                err_msg = "new_password is not allowed during creation."
                LOG.error(err_msg)
                self.module.fail_json(msg=err_msg)
            usr_details = self.create_local_user(user_name=user_name)
            changed = True
            modify_params = self.is_modify_required(user_details=usr_details)

        if state == 'present' and usr_details and modify_params:
            LOG.info('attempting to modify user with id %s',
                     usr_details.get("id"))
            changed = self.modify_local_user(
                user_id=usr_details.get("id"),
                modify_params=modify_params)
            usr_details = self.get_local_user_details(usr_details.get("id"))

        if state == 'absent' and usr_details:
            changed = self.delete_local_user(user_id=usr_details.get("id"))
            usr_details = None

        if state == 'present' and usr_details:
            role_details = self.get_role(role_id=usr_details['role_id'])
            usr_details['role_name'] = role_details.get('name')
            result['local_user_details'] = usr_details
        result['changed'] = changed
        self.module.exit_json(**result)


def get_powerstore_local_user_parameters():
    """This method provides the parameters required for the ansible
    local user modules on PowerStore"""
    return dict(
        user_name=dict(required=False, type='str'),
        user_id=dict(required=False, type='str'),
        user_password=dict(required=False, type='str', no_log=True),
        new_password=dict(required=False, type='str', no_log=True),
        role_name=dict(required=False, type='str'),
        role_id=dict(required=False, type='int'),
        is_locked=dict(required=False, type='bool'),
        state=dict(required=True, type='str', choices=['present', 'absent'])
    )


def main():
    """ Create PowerStore local_user object and perform action on it
        based on user input from playbook """
    obj = PowerStoreLocalUser()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
