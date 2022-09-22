#!/usr/bin/python
# Copyright: (c) 2022, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
module: ldap_domain
version_added: '1.6.0'
short_description: Manage LDAP domain for PowerStore
description:
- Managing LDAP domain on PowerStore Storage System includes creating
  LDAP domain, getting details of LDAP domain, modifying LDAP domain,
  verifying LDAP domain and deleting LDAP domain.

author:
- Akash Shendge (@shenda1) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerstore.powerstore

options:
  ldap_domain_name:
    description:
    - Name of the LDAP authority to construct the LDAP server configuration.
    - Mandatory for the create operation.
    type: str
  ldap_domain_id:
    description:
    - Unique identifier of the LDAP domain configuration.
    type: int
  ldap_servers:
    description:
    - List of IP addresses of the LDAP servers for the domain.
    type: list
    elements: str
  ldap_server_state:
    description:
    - State of the LDAP server.
    - The ldap_servers and ldap_server_state are required together.
    choices: ['present-in-domain', 'absent-in-domain']
    type: str
  ldap_server_port:
    description:
    - Port number used to connect to the LDAP Server.
    type: int
  protocol:
    description:
    - Types of directory service protocol.
    choices: ['LDAP', 'LDAPS']
    type: str
  ldap_server_type:
    description:
    - Types of the LDAP server.
    choices: ['AD', 'OpenLDAP']
    type: str
  bind_user:
    description:
    - Distinguished Name (DN) of the user to be used when binding; that is, authenticating and setting up
      the connection to the LDAP server.
    - Mandatory for the create operation.
    type: str
  bind_password:
    description:
    - Password to use when binding a new LDAP session.
    - Mandatory for the create operation.
    type: str
  ldap_timeout:
    description:
    - Timeout for establishing a connection to an LDAP server.
    type: int
  is_global_catalog:
    description:
    - Whether or not the catalog is global.
    type: bool
  ldap_domain_user_settings:
    description:
    - User settings of LDAP domain.
    type: dict
    suboptions:
      user_id_attribute:
        description:
        - Name of the LDAP attribute whose value indicates the unique identifier of the user.
        - Default value is sAMAccountName.
        type: str
      user_object_class:
        description:
        - LDAP object class for users.
        - Default value is user.
        type: str
      user_search_path:
        description:
        - Path used to search for users on the directory server.
        - Search path is empty, if global catalog is enabled.
        type: str
  ldap_domain_group_settings:
    description:
    - Group settings of LDAP domain.
    type: dict
    suboptions:
      group_name_attribute:
        description:
        - Name of the LDAP attribute whose value indicates the group name.
        - Default value is cn.
        type: str
      group_member_attribute:
        description:
        - Name of the LDAP attribute whose value contains the names of group members within a group.
        - Default value is member.
        type: str
      group_object_class:
        description:
        - LDAP object class for groups.
        - Default value is group.
        type: str
      group_search_path:
        description:
        - Path used to search for groups on the directory server.
        - Search path is empty, if global catalog is enabled.
        type: str
      group_search_level:
        description:
        - Nested search level for performing group search.
        - Default value is 0.
        type: int
  verify_configuration:
    description:
    - Indicates whether to perform the verify LDAP domain configuration or not.
    type: bool
    default: False
  state:
    description:
    - Define whether the LDAP domain configuration should exist or not.
    - For Delete operation only, it should be set to "absent".
    - For all other operations except delete, it should be set to "present".
    required: true
    choices: ['absent', 'present']
    type: str

notes:
- The 'is_global_catalog' option can be enabled only for AD server type.
- To use LDAPS protocol, the pre-requisite is to upload the certificate of
  LDAP server on PowerStore array.
- Verify operation does not support idempotency.
- The check_mode is supported.
'''

EXAMPLES = r'''
- name: Create LDAP domain
  dellemc.powerstore.ldap_domain:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    domain_name: "{{domain_name}}"
    ldap_servers: ["10.xxx.xx.xx"]
    protocol: "LDAP"
    ldap_server_type: "OpenLDAP"
    bind_user: "{{bind_user}}"
    bind_password: "{{bind_password}}"
    ldap_domain_user_settings:
      user_search_path: "cn=Users"
    ldap_domain_group_settings:
      group_search_path: "cn=Users"
    ldap_server_state: "present-in-domain"
    state: "present"

- name: Get LDAP domain details using ID
  dellemc.powerstore.ldap_domain:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    ldap_domain_id: 4
    state: "present"

- name: Get LDAP domain details using name
  dellemc.powerstore.ldap_domain:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    ldap_domain_name: "{{ldap_domain_name}}"
    state: "present"

- name: Verify LDAP domain configuration
  dellemc.powerstore.ldap_domain:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    ldap_domain_id: 4
    verify_configuration: True
    state: "present"

- name: Delete LDAP domain configuration
  dellemc.powerstore.ldap_domain:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    ldap_domain_id: 4
    state: "absent"

- name: Create LDAP domain with AD server type
  dellemc.powerstore.ldap_domain:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    ldap_domain_name: "{{domain_name}}"
    ldap_servers:
    - "10.xxx.xx.xx"
    ldap_server_state: "present-in-domain"
    ldap_server_type: "AD"
    bind_user: "{{bind_user}}"
    bind_password: "{{bind_password}}"
    is_global_catalog: True
    ldap_server_port: 3268
    protocol: "LDAP"
    ldap_domain_user_settings:
      user_search_path: ""
    ldap_domain_group_settings:
      group_search_path: ""
    state: "present"

- name: Get LDAP domain details using domain name
  dellemc.powerstore.ldap_domain:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    ldap_domain_name: "{{domain_name}}"
    state: "present"

- name: Delete LDAP domain using domain name
  dellemc.powerstore.ldap_domain:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    ldap_domain_name: "{{domain_name}}"
    state: "absent"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"

ldap_domain_details:
    description: Details of the LDAP domain configuration.
    returned: When LDAP domain configuration exists.
    type: complex
    contains:
        id:
            description: Unique identifier of the new LDAP server configuration.
            type: str
        domain_name:
            description: Name of the LDAP authority to construct the LDAP server configuration.
            type: str
        ldap_servers:
            description: List of IP addresses of the LDAP servers for the domain. IP addresses are in IPv4 format.
            type: list
        port:
            description: Port number used to connect to the LDAP server(s).
            type: int
        ldap_server_type:
            description: Types of LDAP server.
            type: str
        protocol:
            description: Types of directory service protocol.
            type: str
        bind_user:
            description: Distinguished Name (DN) of the user to be used when binding.
            type: str
        ldap_timeout:
            description: Timeout for establishing a connection to an LDAP server. Default value is 30000 (30 seconds).
            type: int
        is_global_catalog:
            description: Whether or not the catalog is global. Default value is false.
            type: bool
        user_id_attribute:
            description: Name of the LDAP attribute whose value indicates the unique identifier of the user.
            type: str
        user_object_class:
            description: LDAP object class for users.
            type: str
        user_search_path:
            description: Path used to search for users on the directory server.
            type: str
        group_name_attribute:
            description: Name of the LDAP attribute whose value indicates the group name.
            type: str
        group_member_attribute:
            description: Name of the LDAP attribute whose value contains the names of group members within a group.
            type: str
        group_object_class:
            description: LDAP object class for groups.
            type: str
        group_search_path:
            description: Path used to search for groups on the directory server.
            type: str
        group_search_level:
            description: Nested search level for performing group search.
            type: int
        ldap_server_type_l10n:
            description: Localized message string corresponding to ldap_server_type.
            type: str
        protocol_l10n:
            description: Localized message string corresponding to protocol.
            type: str
    sample: {
        "id": "9",
        "domain_name": "domain.com",
        "port": 636,
        "protocol": "LDAPS",
        "protocol_l10n": "LDAPS",
        "bind_user": "cn=ldapadmin,dc=domain,dc=com",
        "ldap_timeout": 300000,
        "ldap_server_type": "OpenLDAP",
        "ldap_server_type_l10n": "OpenLDAP",
        "is_global_catalog": false,
        "user_id_attribute": "uid",
        "user_object_class": "inetOrgPerson",
        "user_search_path": "dc=domain,dc=com",
        "group_name_attribute": "cn",
        "group_member_attribute": "member",
        "group_object_class": "groupOfNames",
        "group_search_path": "dc=domain,dc=com",
        "group_search_level": 0,
        "ldap_servers": [
            "10.xxx.xx.xxx"
        ]
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import utils

LOG = utils.get_logger('ldap_domain')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.7.0'


class PowerStoreLDAPDomain(object):
    """Class with LDAP Domain Operations"""

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_ldap_domain_parameters())

        # initialize the Ansible module
        mut_ex_args = [['ldap_domain_id', 'ldap_domain_name']]
        required_one_of = [['ldap_domain_id', 'ldap_domain_name']]
        required_together = [['ldap_servers', 'ldap_server_state'],
                             ['bind_user', 'bind_password']]

        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True,
            mutually_exclusive=mut_ex_args,
            required_one_of=required_one_of,
            required_together=required_together
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
        self.configuration = self.conn.config_mgmt
        msg = 'Got Py4ps instance for configuration on' \
              ' PowerStore {0}'.format(self.configuration)
        LOG.info(msg)
        LOG.info('Check Mode Flag: %s', self.module.check_mode)

    def create_ldap_domain(self, create_ldap_domain_dict):
        """ Create LDAP domain configuration """

        try:
            LOG.info('Creating LDAP domain')
            resp = {}
            if not self.module.check_mode:
                resp = self.configuration.create_ldap_domain_configuration(
                    create_parameters=create_ldap_domain_dict)
            return resp, True

        except Exception as e:
            msg = 'Creation of LDAP domain failed with error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def delete_ldap_domain(self, ldap_domain_id):
        """ Delete LDAP domain configuration """

        try:
            LOG.info('Deleting LDAP domain with identifier: %s', ldap_domain_id)
            if not self.module.check_mode:
                self.configuration.delete_ldap_domain_configuration(ldap_domain_id=ldap_domain_id)
            return True

        except Exception as e:
            msg = 'Deletion of LDAP domain {0} failed with error ' \
                  '{1}'.format(ldap_domain_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def verify_ldap_domain(self, ldap_domain_id):
        """ Verify LDAP domain configuration """

        try:
            LOG.info('Verifying LDAP domain with identifier: %s', ldap_domain_id)
            if not self.module.check_mode:
                self.configuration.verify_ldap_domain_configuration(ldap_domain_id=ldap_domain_id)
            return True

        except Exception as e:
            msg = 'Verification of LDAP domain {0} failed with error ' \
                  '{1}'.format(ldap_domain_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def check_modification_ldap_servers(self, modify_dict, ldap_domain_details):
        """ Check if modification is required for LDAP servers """

        if self.module.params['ldap_servers'] is not None:
            final_server_list = []
            if self.module.params['ldap_server_state'] == 'present-in-domain':
                add_ldap_servers = set(
                    self.module.params['ldap_servers']) - set(ldap_domain_details['ldap_servers'])
                if len(add_ldap_servers) > 0:
                    final_server_list = list(set(
                        ldap_domain_details['ldap_servers']) | set(add_ldap_servers))
            else:
                remove_ldap_servers = set(
                    self.module.params['ldap_servers']) & set(ldap_domain_details['ldap_servers'])
                if len(remove_ldap_servers) > 0:
                    final_server_list = list(set(
                        ldap_domain_details['ldap_servers']) - set(remove_ldap_servers))
            if len(final_server_list) > 0:
                modify_dict['ldap_servers'] = final_server_list

    def is_modification_required(self, ldap_domain_details):
        """ Check if modification is required for LDAP domain configuration """

        LOG.info("Checking if modification is required for LDAP domain")
        modify_dict = {}

        new_ldap_domain_dict = {
            "bind_user": self.module.params['bind_user'],
            "is_global_catalog": self.module.params['is_global_catalog'],
            "ldap_server_type": self.module.params['ldap_server_type'],
            "ldap_timeout": self.module.params['ldap_timeout'],
            "port": self.module.params['ldap_server_port'],
            "protocol": self.module.params['protocol']
        }

        if self.module.params['ldap_domain_group_settings'] is not None:
            new_ldap_domain_dict["group_member_attribute"] = \
                self.module.params['ldap_domain_group_settings']['group_member_attribute']
            new_ldap_domain_dict["group_name_attribute"] = \
                self.module.params['ldap_domain_group_settings']['group_name_attribute']
            new_ldap_domain_dict['group_object_class'] = \
                self.module.params['ldap_domain_group_settings']['group_object_class']
            new_ldap_domain_dict['group_search_level'] = \
                self.module.params['ldap_domain_group_settings']['group_search_level']
            new_ldap_domain_dict['group_search_path'] = \
                self.module.params['ldap_domain_group_settings']['group_search_path']

        if self.module.params['ldap_domain_user_settings'] is not None:
            new_ldap_domain_dict["user_id_attribute"] = \
                self.module.params['ldap_domain_user_settings']['user_id_attribute']
            new_ldap_domain_dict["user_object_class"] = \
                self.module.params['ldap_domain_user_settings']['user_object_class']
            new_ldap_domain_dict['user_search_path'] = \
                self.module.params['ldap_domain_user_settings']['user_search_path']

        self.check_modification_ldap_servers(modify_dict, ldap_domain_details)

        for key in new_ldap_domain_dict.keys():
            if key in ldap_domain_details and new_ldap_domain_dict[key] is not None and \
                    new_ldap_domain_dict[key] != ldap_domain_details[key]:
                if key == 'is_global_catalog' and new_ldap_domain_dict[key]:
                    modify_dict['user_search_path'] = ""
                    modify_dict['group_search_path'] = ""
                modify_dict[key] = new_ldap_domain_dict[key]
        return modify_dict

    def modify_ldap_domain(self, ldap_domain_id, modify_dict):
        """ Modify LDAP domain configuration """

        try:
            LOG.info('Modifying LDAP domain with identifier: %s', ldap_domain_id)
            if not self.module.check_mode:
                self.configuration.modify_ldap_domain_configuration(
                    ldap_domain_id=ldap_domain_id, modify_parameters=modify_dict)
            return True

        except Exception as e:
            msg = 'Modification of LDAP domain {0} failed with error ' \
                  '{1}'.format(ldap_domain_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_ldap_domain_details(self, ldap_domain_id=None, ldap_domain_name=None):
        """ Get LDAP domain configuration details by name or id """

        try:
            name_or_id = ldap_domain_name if ldap_domain_name else ldap_domain_id
            LOG.info('Getting the details of LDAP domain with identifier: %s', name_or_id)

            if ldap_domain_id:
                return self.configuration.get_ldap_domain_configuration_details(ldap_domain_id)
            else:
                return self.configuration.get_ldap_domain_configuration_details_by_name(ldap_domain_name)
        except Exception as e:
            msg = "Get details of LDAP domain {0} failed with error {1}".format(
                name_or_id, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def validate_parameters(self):
        """Validate the input parameters"""

        params = ['ldap_domain_name', 'bind_user', 'bind_password']
        msg = "Please provide a valid {0}"

        for param in params:
            if self.module.params[param] is not None and \
                    (len(self.module.params[param].strip()) == 0 or
                     self.module.params[param].count(" ") > 0):
                err_msg = msg.format(param)
                self.module.fail_json(msg=err_msg)

    def perform_module_operation(self):
        """
        Perform different actions on LDAP domain based on user parameters
        chosen in playbook
        """
        ldap_domain_id = self.module.params['ldap_domain_id']
        ldap_domain_name = self.module.params['ldap_domain_name']
        ldap_servers = self.module.params['ldap_servers']
        ldap_server_port = self.module.params['ldap_server_port']
        protocol = self.module.params['protocol']
        ldap_server_type = self.module.params['ldap_server_type']
        bind_user = self.module.params['bind_user']
        bind_password = self.module.params['bind_password']
        ldap_timeout = self.module.params['ldap_timeout']
        is_global_catalog = self.module.params['is_global_catalog']
        ldap_domain_user_settings = self.module.params['ldap_domain_user_settings']
        ldap_domain_group_settings = self.module.params['ldap_domain_group_settings']
        verify_configuration = self.module.params['verify_configuration']
        state = self.module.params['state']

        # result is a dictionary to contain end state and LDAP domain details
        result = dict(
            changed=False,
            ldap_domain_details={}
        )

        # Validate parameters
        self.validate_parameters()

        # Get the details of LDAP domain
        ldap_domain_details = self.get_ldap_domain_details(ldap_domain_id, ldap_domain_name)
        if ldap_domain_details:
            if ldap_domain_id is None:
                ldap_domain_id = ldap_domain_details['id']
            modify_dict = self.is_modification_required(ldap_domain_details)

        # Create LDAP domain configuration
        if state == 'present' and not ldap_domain_details:
            create_ldap_domain_dict = {
                'domain_name': ldap_domain_name,
                'ldap_servers': ldap_servers,
                'port': ldap_server_port,
                'protocol': protocol,
                'ldap_server_type': ldap_server_type,
                'bind_user': bind_user,
                'bind_password': bind_password,
                'ldap_timeout': ldap_timeout,
                'is_global_catalog': is_global_catalog
            }

            # Update create dict
            update_create_dict(create_ldap_domain_dict, is_global_catalog, ldap_server_type,
                               ldap_domain_user_settings, ldap_domain_group_settings)
            resp, result['changed'] = self.create_ldap_domain(create_ldap_domain_dict)
            if resp:
                ldap_domain_id = resp['id']

        # Delete LDAP domain configuration
        if state == 'absent' and ldap_domain_details:
            result['changed'] = self.delete_ldap_domain(ldap_domain_id)

        # Verify LDAP domain configuration
        if state == 'present' and ldap_domain_details and verify_configuration:
            result['changed'] = self.verify_ldap_domain(ldap_domain_id)

        # Modify LDAP domain configuration
        if state == 'present' and ldap_domain_details and modify_dict:
            result['changed'] = self.modify_ldap_domain(ldap_domain_id, modify_dict)

        # Finally update the module result!
        if state == 'present':
            result['ldap_domain_details'] = self.get_ldap_domain_details(ldap_domain_id, ldap_domain_name)
        self.module.exit_json(**result)


def update_create_dict(create_ldap_domain_dict, is_global_catalog, ldap_server_type, ldap_domain_user_settings, ldap_domain_group_settings):
    """ Update dictionary for create operation """

    if ldap_server_type and is_global_catalog and ldap_server_type == 'AD':
        if ldap_domain_user_settings is None:
            create_ldap_domain_dict['user_search_path'] = ""
        elif ldap_domain_user_settings:
            create_ldap_domain_dict.update(ldap_domain_user_settings)
            if ldap_domain_user_settings['user_search_path'] is None:
                create_ldap_domain_dict['user_search_path'] = ""

        if ldap_domain_group_settings is None:
            create_ldap_domain_dict['group_search_path'] = ""
        elif ldap_domain_group_settings:
            create_ldap_domain_dict.update(ldap_domain_group_settings)
            if ldap_domain_group_settings['group_search_path'] is None:
                create_ldap_domain_dict['group_search_path'] = ""
    else:
        update_create_dict_openldap(create_ldap_domain_dict, ldap_domain_user_settings, ldap_domain_group_settings)


def update_create_dict_openldap(create_ldap_domain_dict, ldap_domain_user_settings, ldap_domain_group_settings):
    """ Update dictionary for create operation for OpenLDAP server type"""

    if ldap_domain_user_settings:
        create_ldap_domain_dict.update(ldap_domain_user_settings)
    if ldap_domain_group_settings:
        create_ldap_domain_dict.update(ldap_domain_group_settings)


def get_powerstore_ldap_domain_parameters():
    """This method provide the parameters required for the ldap_domain
       operations for PowerStore"""
    return dict(
        ldap_domain_id=dict(type='int'), ldap_domain_name=dict(),
        ldap_servers=dict(type='list', elements='str'),
        ldap_server_state=dict(choices=['present-in-domain', 'absent-in-domain']),
        ldap_server_port=dict(type='int'), protocol=dict(choices=['LDAP', 'LDAPS']),
        ldap_server_type=dict(choices=['AD', 'OpenLDAP']),
        bind_user=dict(), bind_password=dict(no_log=True),
        ldap_timeout=dict(type='int'), is_global_catalog=dict(type='bool'),
        ldap_domain_user_settings=dict(type='dict', options=dict(
            user_id_attribute=dict(), user_object_class=dict(),
            user_search_path=dict()
        )),
        ldap_domain_group_settings=dict(type='dict', options=dict(
            group_name_attribute=dict(),
            group_member_attribute=dict(), group_object_class=dict(),
            group_search_path=dict(), group_search_level=dict(type='int'),
        )),
        verify_configuration=dict(type='bool', default=False),
        state=dict(required=True, type='str', choices=['present', 'absent'])
    )


def main():
    """ Create PowerStore LDAP domain object and perform action on it
        based on user input from playbook """
    obj = PowerStoreLDAPDomain()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
