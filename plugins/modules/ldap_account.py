#!/usr/bin/python
# Copyright: (c) 2024, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
module: ldap_account
version_added: '1.6.0'
short_description: Manage LDAP Account for PowerStore
description:
- Managing LDAP accounts on PowerStore Storage System includes creating
  an LDAP account, getting details of LDAP accounts, modifying an LDAP account,
  and deleting an LDAP account.

author:
- Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerstore.powerstore

options:
  ldap_account_id:
    description:
    - Unique identifier of the LDAP account.
    type: int
  ldap_account_name:
    description:
    - Name of the new LDAP account to be created.
    - This has to match to the LDAP user or group
      in LDAP server to which the LDAP account is mapped.
    type: str
  ldap_domain_id:
    description:
    - Unique identifier of the LDAP domain to which LDAP user or group belongs.
    type: int
  ldap_domain_name:
    description:
    - Name of the LDAP domain to which LDAP user or group belongs.
    type: str
  role_id:
    description:
    - Unique identifier of the role to which the new LDAP account will be mapped.
    type: int
  role_name:
    description:
    - Name of the role to which the new LDAP account will be mapped.
    type: str
  ldap_account_type:
    description:
    - Type of LDAP account.
    choices: ['User', 'Group']
    type: str
  state:
    description:
    - Define whether the LDAP account should exist or not.
    - For Delete operation only, it should be set to C(absent).
    - For all other operations except delete, it should be set to C(present).
    required: true
    choices: ['absent', 'present']
    type: str

notes:
- The I(check_mode) is supported.
'''

EXAMPLES = r'''
- name: Create an LDAP account
  dellemc.powerstore.ldap_account:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    ldap_account_name: "ldap_user_account_1"
    ldap_domain_id: "1"
    role_name: "Administrator"
    ldap_account_type: "User"
    state: "present"

- name: Get the details of the LDAP account by name
  dellemc.powerstore.ldap_account:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    ldap_account_name: "ldap_user_account_1"
    state: "present"

- name: Get the details of the LDAP account by id
  dellemc.powerstore.ldap_account:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    ldap_account_id: "3"
    state: "present"

- name: Modify an LDAP account
  dellemc.powerstore.ldap_account:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    ldap_account_name: "ldap_user_account_1"
    role_name: "2"
    state: "present"

- name: Delete an LDAP account
  dellemc.powerstore.ldap_account:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    ldap_account_id: "3"
    state: "absent"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"

ldap_account_details:
    description: Details of the LDAP account.
    returned: When LDAP account exists.
    type: complex
    contains:
        id:
            description: Unique identifier of the LDAP account.
            type: int
        role_id:
            description: Unique identifier of the role to which the LDAP account is mapped.
            type: int
        domain_id:
            description: Unique identifier of the LDAP domain to which LDAP user or group belongs.
            type: int
        name:
            description: Name of the LDAP account.
            type: str
        type:
            description: Type of LDAP account.
            type: str
        dn:
            description: Types of directory service protocol.
            type: str
    sample: {
        "id": "5",
        "role_id": "1",
        "domain_id": "2",
        "name": "sample_ldap_user",
        "type": "User",
        "type_l10n": "User",
        "dn": "cn=sample_ldap_user,dc=ldap,dc=com"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import utils

LOG = utils.get_logger('ldap_account')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']


class PowerStoreLDAPAccount(object):
    """Class with LDAP Account Operations"""
    cluster_name = None
    cluster_global_id = None
    valid_role_id = None
    valid_ldap_domain_id = None

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_ldap_account_parameters())

        # initialize the Ansible module
        mut_ex_args = [['ldap_domain_id', 'ldap_domain_name'],
                       ['role_id', 'role_name'],
                       ['ldap_account_id', 'ldap_account_name']]
        required_one_of = [['ldap_account_id', 'ldap_account_name']]

        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True,
            mutually_exclusive=mut_ex_args,
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

        self.conn = utils.get_powerstore_connection(self.module.params)
        self.configuration = self.conn.config_mgmt
        msg = 'Got Py4ps instance for configuration on' \
              ' PowerStore {0}'.format(self.configuration)
        LOG.info(msg)
        LOG.info('Check Mode Flag: %s', self.module.check_mode)

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

    def get_ldap_domain(self, ldap_domain_id=None, ldap_domain_name=None):
        """Get the details of the LDAP domain configuration on a PowerStore storage system"""
        try:
            ldap_domain_details = dict()
            ldap_domain_dtls = None

            if ldap_domain_id:
                ldap_domain_dtls = self.configuration.get_ldap_domain_configuration_details(ldap_domain_id)

            if ldap_domain_name:
                ldap_domain_dtls = self.configuration.get_ldap_domain_configuration_details_by_name(ldap_domain_name)

            if ldap_domain_dtls:
                ldap_domain_details['id'] = ldap_domain_dtls['id']
                ldap_domain_details['name'] = ldap_domain_dtls['domain_name']

            if not ldap_domain_details:
                raise NameError("Specified LDAP domain configuration does not exist")

            return ldap_domain_details
        except Exception as e:
            msg = "Failed to get the LDAP domain configuration with error {0} ".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def create_ldap_account(self, ldap_account_type, ldap_account_name):
        """Create an LDAP Account."""
        try:
            LOG.info("Attempting to create an LDAP Account with name "
                     "%s", ldap_account_name)
            acc_details = {}
            if not self.module.check_mode:
                create_params = dict()
                create_params['name'] = ldap_account_name
                create_params['type'] = ldap_account_type
                if self.valid_ldap_domain_id:
                    create_params['domain_id'] = self.valid_ldap_domain_id
                if self.valid_role_id:
                    create_params['role_id'] = self.valid_role_id

                resp = self.configuration.create_ldap_account(
                    create_parameters=create_params)

                if resp:
                    acc_details = self.get_ldap_account_details(ldap_account_id=resp['id'])

                LOG.info("Successfully created LDAP account with "
                         "details : %s", acc_details)

            return acc_details, True

        except Exception as e:
            msg = 'Create LDAP account with name {0} on PowerStore array ' \
                  'name : {1} , global id : {2} failed with ' \
                  'error {3} '.format(ldap_account_name, self.cluster_name,
                                      self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def delete_ldap_account(self, ldap_account_id):
        """ Delete LDAP account """

        try:
            LOG.info('Deleting LDAP account with identifier: %s', ldap_account_id)
            if not self.module.check_mode:
                self.configuration.delete_ldap_account(ldap_account_id=ldap_account_id)
            return True

        except Exception as e:
            msg = 'Deletion of LDAP account {0} failed with error ' \
                  '{1}'.format(ldap_account_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_ldap_account_details(self, ldap_account_id=None, ldap_account_name=None):
        """ Get LDAP account details by name or id """

        try:
            msg = 'Getting LDAP account details with ldap_account_id {0}, ' \
                  'ldap_account_name {1}'.format(ldap_account_id, ldap_account_name)
            LOG.info(msg)
            acc_details = None
            if ldap_account_id:
                acc_details = \
                    self.configuration.get_ldap_account_details(ldap_account_id)
            elif ldap_account_name:
                acc_details = \
                    self.configuration.get_ldap_account_details_by_name(ldap_account_name)
                if acc_details:
                    return acc_details

            msg = 'Successfully got LDAP account Details' \
                  ' {0}'.format(acc_details)
            LOG.info(msg)
            return acc_details

        except Exception as e:
            msg = 'Get LDAP account details for PowerStore array name : ' \
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

    def is_modify_required(self, ldap_account_details):
        """To get the details of the fields to be modified."""

        try:
            LOG.info("LDAP account details: %s", ldap_account_details)
            modify_dict = dict()

            if self.valid_role_id and \
                    ldap_account_details['role_id'] != self.valid_role_id:
                modify_dict['role_id'] = self.valid_role_id

            if modify_dict:
                return modify_dict
            else:
                return None

        except Exception as e:
            msg = 'Failed to determine if LDAP account instance needs ' \
                  'to modified with error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def modify_ldap_account_details(self, ldap_account_id, modify_params):
        """Perform modify operations on an LDAP account"""

        try:
            if not self.module.check_mode:
                self.configuration.modify_ldap_account_details(
                    ldap_account_id=ldap_account_id, modify_parameters=modify_params)
            return True
        except Exception as e:
            msg = 'Failed to modify the LDAP account instance ' \
                  'with error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_role_and_ldap_domain(self, ldap_domain_id, ldap_domain_name, role_id, role_name):
        """Get role and LDAP domain """

        if ldap_domain_id or ldap_domain_name:
            ldap_domain_details = self.get_ldap_domain(ldap_domain_id=ldap_domain_id,
                                                       ldap_domain_name=ldap_domain_name)
            if ldap_domain_details:
                self.valid_ldap_domain_id = ldap_domain_details.get('id')

        if role_id or role_name:
            role_details = self.get_role(role_id=role_id, role_name=role_name)
            if role_details:
                self.valid_role_id = role_details.get('id')

        return self.valid_ldap_domain_id, self.valid_role_id

    def perform_module_operation(self):
        """
        Perform different actions on LDAP account based on user parameters
        chosen in playbook
        """
        ldap_domain_id = self.module.params['ldap_domain_id']
        ldap_domain_name = self.module.params['ldap_domain_name']
        ldap_account_id = self.module.params['ldap_account_id']
        ldap_account_name = self.module.params['ldap_account_name']
        role_id = self.module.params['role_id']
        role_name = self.module.params['role_name']
        ldap_account_type = self.module.params['ldap_account_type']
        state = self.module.params['state']

        # result is a dictionary to contain end state and LDAP account details
        changed = False
        result = dict(
            changed=False,
            ldap_account_details={}
        )
        modify_params = None

        self.valid_ldap_domain_id, self.valid_role_id = self.get_role_and_ldap_domain(ldap_domain_id=ldap_domain_id,
                                                                                      ldap_domain_name=ldap_domain_name,
                                                                                      role_id=role_id,
                                                                                      role_name=role_name)

        acc_details = self.get_ldap_account_details(
            ldap_account_id=ldap_account_id, ldap_account_name=ldap_account_name)
        if acc_details:
            modify_params = self.is_modify_required(ldap_account_details=acc_details)

        if not acc_details and state == 'present':
            if not (ldap_account_name and self.valid_ldap_domain_id and self.valid_role_id):
                msg = "ldap_account_name, ldap domain and role " \
                      "details are required to create an LDAP Account"
                LOG.error(msg)
                self.module.fail_json(msg=msg)
            acc_details, changed = self.create_ldap_account(ldap_account_type=ldap_account_type,
                                                            ldap_account_name=ldap_account_name)

        if state == 'present' and acc_details and modify_params:
            LOG.info('attempting to modify the LDAP account with id %s',
                     acc_details.get("id"))
            changed = self.modify_ldap_account_details(
                ldap_account_id=acc_details.get("id"),
                modify_params=modify_params)
            acc_details = self.get_ldap_account_details(acc_details.get("id"))

        if state == 'absent' and acc_details:
            changed = self.delete_ldap_account(ldap_account_id=acc_details.get("id"))
            acc_details = None

        if state == 'present' and acc_details:
            role_details = self.get_role(role_id=acc_details['role_id'])
            domain_details = self.get_ldap_domain(ldap_domain_id=acc_details['domain_id'])
            acc_details['role_name'] = role_details.get('name')
            acc_details['domain_name'] = domain_details.get('name')
            result['ldap_account_details'] = acc_details
        result['changed'] = changed
        self.module.exit_json(**result)


def get_powerstore_ldap_account_parameters():
    """This method provide the parameters required for the ldap_account
       operations for PowerStore"""
    return dict(
        ldap_domain_id=dict(type='int'), ldap_domain_name=dict(),
        ldap_account_id=dict(type='int'), ldap_account_name=dict(),
        role_id=dict(type='int'), role_name=dict(),
        ldap_account_type=dict(choices=['User', 'Group']),
        state=dict(required=True, type='str', choices=['present', 'absent'])
    )


def main():
    """ Create PowerStore LDAP account object and perform action on it
        based on user input from playbook """
    obj = PowerStoreLDAPAccount()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
