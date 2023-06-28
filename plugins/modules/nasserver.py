#!/usr/bin/python
# Copyright: (c) 2020-2021, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

""" Ansible module for managing NAS server on PowerStore"""
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: nasserver
version_added: '1.1.0'
short_description: NAS Server operations for PowerStore Storage system
description:
- Supports getting the details and modifying the attributes of a NAS server.
extends_documentation_fragment:
  - dellemc.powerstore.powerstore
author:
- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
options:
 nas_server_name:
   description:
   - Name of the NAS server. Mutually exclusive with I(nas_server_id).
   type: str
 nas_server_id:
   description:
   - Unique id of the NAS server. Mutually exclusive with I(nas_server_name).
   type: str
 description:
   description:
   - Description of the NAS server.
   type: str
 nas_server_new_name:
   description:
   - New name of the NAS server for a rename operation.
   type: str
 current_node:
   description:
   - Unique identifier or name of the node on which the NAS server is running.
   type: str
 preferred_node:
   description:
   - Unique identifier or name of the preferred node for the NAS server.
     The initial value (on NAS server create) is taken from the current node.
   type: str
 current_unix_directory_service:
   description:
   - Define the Unix directory service used for looking up identity
     information for Unix such as UIDs, GIDs, net groups, and so on.
   choices: ['NIS', 'LDAP', 'LOCAL_FILES','LOCAL_THEN_NIS',
   'LOCAL_THEN_LDAP']
   type: str
 default_unix_user:
   description:
   - Default Unix user name used for granting access in case of Windows to
     Unix user mapping failure. When empty, access in such case is denied.
   type: str
 default_windows_user:
   description:
   - Default Windows user name used for granting access in case of Unix
     to Windows user mapping failure. When empty, access in such case
     is denied.
   type: str
 protection_policy:
   description:
   - Name/ID of the protection policy applied to the nas server.
   - Policy can be removed by passing an empty string in the I(protection_policy) parameter.
   type: str
 state:
   description:
   - Define whether the nas server should exist or not.
   choices: ['absent', 'present']
   required: true
   type: str

notes:
- The I(check_mode) is not supported.
- Adding/Removing protection policy to/from a NAS server
  is supported for PowerStore version 3.0.0 and above.
'''

EXAMPLES = r'''

 - name: Get details of NAS Server by name
   dellemc.powerstore.nasserver:
     array_ip: "{{array_ip}}"
     validate_certs: "{{validate_certs}}"
     user: "{{user}}"
     password: "{{password}}"
     nas_server_name: "{{nas_server_name}}"
     state: "present"

 - name: Get Details of NAS Server by ID
   dellemc.powerstore.nasserver:
     array_ip: "{{array_ip}}"
     validate_certs: "{{validate_certs}}"
     user: "{{user}}"
     password: "{{password}}"
     nas_server_id: "{{nas_id}}"
     state: "present"

 - name: Rename NAS Server by Name
   dellemc.powerstore.nasserver:
     array_ip: "{{array_ip}}"
     validate_certs: "{{validate_certs}}"
     user: "{{user}}"
     password: "{{password}}"
     nas_server_name: "{{nas_server_name}}"
     nas_server_new_name : "{{nas_server_new_name}}"
     state: "present"

 - name: Modify NAS Server attributes by ID
   dellemc.powerstore.nasserver:
     array_ip: "{{array_ip}}"
     validate_certs: "{{validate_certs}}"
     user: "{{user}}"
     password: "{{password}}"
     nas_server_id: "{{nas_id}}"
     current_unix_directory_service: "LOCAL_FILES"
     current_node: "{{cur_node_n1}}"
     preferred_node: "{{prefered_node}}"
     protection_policy: "protection_policy_1"
     state: "present"

 - name: Remove protection policy
   dellemc.powerstore.nasserver:
     array_ip: "{{array_ip}}"
     validate_certs: "{{validate_certs}}"
     user: "{{user}}"
     password: "{{password}}"
     nas_server_id: "{{nas_id}}"
     protection_policy: ""
     state: "present"

'''

RETURN = r'''

changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"

nasserver_details:
    description: Details about the nas server.
    returned: When nas server exists
    type: complex
    contains:
        id:
            description: The system generated ID given to the nas server.
            type: str
        name:
            description: Name of the nas server.
            type: str
        description:
            description: Additional information about the nas server.
            type: str
        operational_status:
            description: NAS server operational status.
            type: str
        current_node:
            description: Unique identifier and name of the node on which the
                         NAS server is running.
            type: dict
        preferred_node:
            description: Unique identifier and name of the preferred node for
                         the NAS server.
            type: dict
        default_unix_user:
            description: Default Unix user name used for granting access in
                         case of Windows to Unix user mapping failure.
            type: str
        current_unix_directory_service:
            description: Define the Unix directory service used for looking up
                         identity information for Unix such as UIDs, GIDs, net
                         groups, and so on.
            type: str
        is_username_translation_enabled:
            description: Enable the possibility to match a windows account to
                         a Unix account with different names.
            type: bool
        production_IPv4_interface_id:
            description: Unique identifier of the preferred IPv4 production
                         interface.
            type: str
        production_IPv6_interface_id:
            description: Unique identifier of the preferred IPv6 production
                         interface.
            type: str
        backup_IPv4_interface_id:
            description: Unique identifier of the preferred IPv4 backup
                         interface.
            type: str
        backup_IPv6_interface_id:
            description: Unique identifier of the preferred IPv6 backup
                         interface.
            type: str
        file_interfaces:
            description: This is the inverse of the resource type
                         file_interface association. Will return the id,name &
                         ip_address of the associated file interface.
            type: dict
        nfs_servers:
            description: This is the inverse of the resource type nfs_server
                         association.
            type: str
        smb_servers:
            description: This is the inverse of the resource type smb_server
                         association.
            type: str
        file_ldaps:
            description: This is the inverse of the resource type file_ldap
                         association.
            type: str
        file_systems:
            description: This is the inverse of the resource type file_system
                         association.
            type: dict
        protection_policy_id:
            description: Id of the protection policy applied to the nas server.
            type: str
    sample: {
        "backup_IPv4_interface_id": null,
        "backup_IPv6_interface_id": null,
        "current_node": {
            "id": "N2",
            "name": "Appliance-WND8977-node-B"
        },
        "current_node_id": "Appliance-WND8977-node-B",
        "current_preferred_IPv4_interface_id": "60c02-b5d8-9d9b-7e6f-feb93c9",
        "current_preferred_IPv6_interface_id": null,
        "current_unix_directory_service": "LDAP",
        "current_unix_directory_service_l10n": "LDAP",
        "default_unix_user": null,
        "default_windows_user": null,
        "description": "",
        "file_interfaces": [
            {
                "id": "0c05652-b5d8-9d9b-7e6f-fe8be1eb93c9",
                "ip_address": "1.2.3.4",
                "name": "PROD001_827ee18708a9_6"
            }
        ],
        file_ldaps: [
            {
                "id": "60c05ba8-362e-159a-0205-ee6f605dfe5a"
            }
        ],
        "file_nises": [],
        "file_systems": [
            {
                "id": "61c55b57-4a70-08dd-a240-96e8abdcbab0",
                "name": "sample_fs"
            }
        ],
        "id": "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
        "is_auto_user_mapping_enabled": true,
        "is_username_translation_enabled": false,
        "name": "ansible_nas_server_2",
        "nfs_servers": [
            {
                "id": "60c05653-4fd3-2033-2da0-ee6f605dfe5a"
            }
        ],
        "operational_status": "Started",
        "operational_status_l10n": "Started",
        "preferred_node": {
            "id": "N2",
            "name": "Appliance-WND8977-node-B"
        },
        "preferred_node_id": "Appliance-WND8977-node-B",
        "production_IPv4_interface_id": "60c05652-b5d8-9d9b-7e6f-fe8be1eb93c",
        "production_IPv6_interface_id": null,
        "protection_policy_id": null,
        "smb_servers": [
            {
                "id": "60c05c18-6806-26ae-3b0d-fe8be1eb93c"
            }
        ]
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import utils
import logging

LOG = utils.get_logger('nasserver',
                       log_devel=logging.INFO)

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/2.0.0'


class PowerStoreNasServer(object):
    """NAS Server System operations"""
    cluster_name = None
    cluster_global_id = None
    IS_NAME = "NAME"
    protection_policy_id = None

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_nasserver_parameters())

        mutually_exclusive = [['nas_server_name', 'nas_server_id']]
        required_one_of = [['nas_server_name', 'nas_server_id']]

        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mutually_exclusive,
            required_one_of=required_one_of
        )
        msg = 'HAS_PY4PS = {0} , IMPORT_ERROR = {1}'.format(
            HAS_PY4PS, IMPORT_ERROR)
        LOG.info(msg)
        if HAS_PY4PS is False:
            self.module.fail_json(msg=IMPORT_ERROR)
        msg = 'IS_SUPPORTED_PY4PS_VERSION = {0}, VERSION_ERROR = {1}' \
              ''.format(IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR)
        LOG.info(msg)
        if IS_SUPPORTED_PY4PS_VERSION is False:
            self.module.fail_json(msg=VERSION_ERROR)

        self.conn = utils.get_powerstore_connection(
            self.module.params, application_type=APPLICATION_TYPE)
        self.provisioning = self.conn.provisioning
        msg = 'Got Py4ps instance for provisioning on' \
              ' PowerStore {0}'.format(self.conn)
        LOG.info(msg)
        self.protection = self.conn.protection
        msg = 'Got Py4ps instance for protection on' \
              ' PowerStore {0}'.format(self.protection)
        LOG.info(msg)

    def get_node_id(self, node):
        """Get respective node id from either node name or node id"""
        try:
            msg = "Getting Node {0} id ".format(node)
            LOG.info(msg)
            nodes = self.provisioning.get_nodes()
            for item in nodes:
                if node in item.values():
                    # verify with other array
                    # if correction required for ID & Name
                    res_node = {'name': item['name'], 'id': item['id']}
                    msg = "Got Node {0} id as {1} ".format(node, res_node)
                    LOG.info(msg)
                    return res_node

            msg = "Failed to get any Node with either name or " \
                  "id {0}".format(node)

        except Exception as e:
            msg = 'Get Node {0} for powerstore array name : ' \
                  '{1} , global id : {2} failed with' \
                  ' error {3} '.format(node, self.cluster_name,
                                       self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))
        LOG.error(msg)
        self.module.fail_json(msg=msg)

    def get_protection_policy(self, protection_policy):
        """Get protection policy"""
        try:
            msg = 'Getting the details of protection policy' \
                  ' {0}'.format(protection_policy)

            LOG.info(msg)
            id_or_name = utils.name_or_id(val=protection_policy)
            if id_or_name == self.IS_NAME:
                resp = self.protection.get_protection_policy_by_name(
                    name=protection_policy)
                if len(resp) == 0:
                    msg = 'No protection policy present with name {0}'. \
                          format(protection_policy)
                    LOG.debug(msg)
                    self.module.fail_json(msg=msg)
                elif resp and len(resp) > 0:
                    pp_id = resp[0]['id']
            else:
                resp = self.protection.get_protection_policy_details(
                    policy_id=protection_policy)
                if resp:
                    pp_id = resp['id']
            if pp_id:
                msg = 'Successfully got the details of protection ' \
                    'policy name is {0} and id is ' \
                    '{1}'.format(protection_policy, pp_id)
                LOG.info(msg)
                return pp_id
            else:
                msg = 'No protection policy present with name or id {0}'. \
                      format(protection_policy)
                LOG.debug(msg)
                self.module.fail_json(msg=msg)

        except Exception as e:
            msg = 'Get details of protection policy name or ID : {0} ' \
                  'failed with error : {1} '.format(protection_policy,
                                                    str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_nas_server(self, nas_server_id=None, nas_server_name=None):
        """Get the details of NAS Server of a given Powerstore storage
        system"""
        msg = None

        try:
            log_msg = "Getting NAS Server details id: {0} name " \
                      "{1}".format(nas_server_id, nas_server_name)
            LOG.info(log_msg)
            if nas_server_name:
                nas_details = self.provisioning.get_nas_server_by_name(
                    nas_server_name=nas_server_name)
                if nas_details:
                    nas_details = nas_details[0]
            else:
                nas_details = self.provisioning.get_nas_server_details(
                    nas_server_id=nas_server_id)

            if nas_details:
                log_msg = 'Successfully got NAS Server details {0} from' \
                          ' powerstore array name : {1} ,global id : ' \
                          '{2}'.format(nas_details, self.cluster_name,
                                       self.cluster_global_id)
                LOG.info(log_msg)
            else:
                msg = 'Failed to get NAS Server with id {0} or name {1}' \
                      ' from powerstore system'.format(nas_server_id,
                                                       nas_server_name)
            LOG.error(msg)
            return nas_details

        except Exception as e:
            msg = 'Get NAS Server with id {0} or name {1} failed with ' \
                  'error {2} '.format(nas_server_id, nas_server_name, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
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

    def to_modify_nasserver(self, nasserver_details):
        """Determines if any modification required on a specific
        nas server instance."""

        try:
            LOG.info("Checking if Modify required for nas server ")
            modify_parameters = dict()

            description = self.module.params['description']

            if description is not None and description != "" and \
                    description != nasserver_details['description']:
                modify_parameters['description'] = description

            if description == "" and \
                    nasserver_details['description'] is not None:
                modify_parameters['description'] = description

            if self.protection_policy_id is not None and self.protection_policy_id != "" and \
                    self.protection_policy_id != nasserver_details['protection_policy_id']:
                modify_parameters['protection_policy_id'] = self.protection_policy_id

            if self.protection_policy_id == "" and (
                    nasserver_details['protection_policy_id'] is not None):
                modify_parameters['protection_policy_id'] = \
                    self.protection_policy_id

            nas_server_new_name = self.module.params['nas_server_new_name']
            if nas_server_new_name and nas_server_new_name != \
                    nasserver_details['name']:
                modify_parameters['name'] = nas_server_new_name

            # Node Name appears as ID in NAS Server
            node_types = ['current_node', 'preferred_node']
            for node_type in node_types:
                node_type_val = self.module.params[node_type]
                if node_type_val:
                    node_id = (self.get_node_id(
                        node=node_type_val))['name']
                    if node_id != nasserver_details[node_type + '_id']:
                        modify_parameters[node_type + '_id'] = node_id

            cur_unix_dir_ser = \
                self.module.params['current_unix_directory_service']
            if cur_unix_dir_ser and cur_unix_dir_ser != (
                    nasserver_details['current_unix_directory_service']) \
                    .upper():
                modify_parameters['current_unix_directory_service'] = \
                    self.get_enum_keys(cur_unix_dir_ser)

            users = ['unix', 'windows']

            for user in users:
                def_user = self.module.params['default_' + user + '_user']

                nas_details_user = ""
                if nasserver_details['default_' + user + '_user']:
                    nas_details_user = \
                        nasserver_details['default_' + user + '_user']

                if def_user is not None and \
                        def_user != nas_details_user:
                    modify_parameters['default_' + user + '_user'] = def_user

            log_msg = "Modify Dict {0}".format(str(modify_parameters))
            LOG.info(log_msg)
            return modify_parameters

        except Exception as e:
            msg = 'Failed to determine if modify nas server required with ' \
                  'error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def modify_nasserver(self, nasserver_id, modify_parameters):
        """Modify NAS Server attributes."""
        try:
            if modify_parameters:
                self.provisioning.modify_nasserver(
                    nasserver_id=nasserver_id,
                    modify_parameters=modify_parameters)
            return

        except Exception as e:
            msg = 'Failed to modify nasserver id {0} with ' \
                  'error {1}'.format(nasserver_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_enum_keys(self, user_input):
        """Get the ENUM Keys for user input string"""
        try:
            enum_dict = {
                "NIS": "NIS",
                "LDAP": "LDAP",
                "LOCAL_FILES": "Local_Files",
                "LOCAL_THEN_NIS": "Local_Then_NIS",
                "LOCAL_THEN_LDAP": "Local_Then_LDAP"
            }
            return enum_dict[user_input]

        except Exception as e:
            msg = 'Failed to get the enum value for user_ip : {0} with ' \
                  'error {1}'.format(user_input, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def perform_module_operation(self):
        clusters = self.get_clusters()
        if len(clusters) > 0:
            self.cluster_name = clusters[0]['name']
            self.cluster_global_id = clusters[0]['id']
        else:
            self.module.fail_json(msg="Unable to find any active cluster "
                                      "on this array ")

        nas_server_name = self.module.params['nas_server_name']
        nas_server_id = self.module.params['nas_server_id']
        state = self.module.params['state']
        protection_policy = self.module.params['protection_policy']

        # result is a dictionary to contain end state and nasserver details
        changed = False
        result = dict(
            changed=False,
            nasserver_details=None
        )

        nasserver_details = None
        nas_id = None
        to_modify = False
        to_modify_dict = None

        if protection_policy is not None:
            if protection_policy == "":
                self.protection_policy_id = protection_policy
            else:
                self.protection_policy_id = self.get_protection_policy(
                    protection_policy=protection_policy)

        if nas_server_name:
            nasserver_details = self.get_nas_server(
                nas_server_name=nas_server_name)
        if nas_server_id:
            nasserver_details = self.get_nas_server(
                nas_server_id=nas_server_id)

        if nasserver_details:
            nas_id = nasserver_details['id']
            if self.module.params['protection_policy'] is not None and \
                    'protection_policy_id' not in nasserver_details.keys():
                msg = "Protection policy can be handled only for PowerStore " \
                      "FootHills Prime or above."
                LOG.error(msg)
                self.module.fail_json(msg=msg)
            else:
                to_modify_dict = self.to_modify_nasserver(
                    nasserver_details=nasserver_details)
            if to_modify_dict:
                to_modify = True
        log_msg = "NAS Server Details: {0} , To Modify {1}".format(
            nasserver_details, to_modify)
        LOG.debug(log_msg)

        if not nasserver_details and state == 'present':
            msg = "Creation of NAS Server is not currently supported " \
                  "through Ansible Module "

            LOG.error(msg)
            self.module.fail_json(msg=msg)

        if to_modify and state == 'present':
            self.modify_nasserver(nasserver_id=nas_id,
                                  modify_parameters=to_modify_dict)
            changed = True

        if state == 'absent' and nasserver_details:
            msg = "Deletion of NAS Server is not currently supported " \
                  "through Ansible Module"
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        if state == 'present' and nasserver_details:
            nasserver_details = self.get_nas_server(
                nas_server_id=nas_id)
            nasserver_details['current_node'] = self.get_node_id(
                nasserver_details['current_node_id'])
            nasserver_details['preferred_node'] = self.get_node_id(
                nasserver_details['preferred_node_id'])

        result['changed'] = changed
        result['nasserver_details'] = nasserver_details
        self.module.exit_json(**result)


def get_powerstore_nasserver_parameters():
    """This method provides the parameters required for the ansible
    nas server modules on PowerStore"""
    return dict(
        nas_server_name=dict(required=False, type='str'),
        nas_server_id=dict(required=False, type='str'),
        description=dict(required=False, type='str'),
        nas_server_new_name=dict(required=False, type='str'),
        current_node=dict(required=False, type='str'),
        preferred_node=dict(required=False, type='str'),
        protection_policy=dict(required=False, type='str'),
        current_unix_directory_service=dict(required=False, type='str',
                                            choices=['NIS',
                                                     'LDAP',
                                                     'LOCAL_FILES',
                                                     'LOCAL_THEN_NIS',
                                                     'LOCAL_THEN_LDAP']),
        default_unix_user=dict(required=False, type='str'),
        default_windows_user=dict(required=False, type='str'),
        state=dict(required=True, type='str', choices=['present', 'absent'])
    )


def main():
    """ Create PowerStore NAS Server object and perform action on it
        based on user input from playbook """
    obj = PowerStoreNasServer()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
