#!/usr/bin/python
# Copyright: (c) 2024, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
module: nfs_server
version_added: '3.1.0'
short_description: Manage NFS server for PowerStore
description:
- Managing storage containers on PowerStore Storage System includes creating
  an NFS server, getting details of an NFS server, modifying an
  NFS server and deleting an NFS server.

author:
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerstore.powerstore

options:
  nfs_server_id:
    description:
    - The unique identifier of the NFS server.
    type: str
  nas_server:
    description:
    - Unique identifier/name of the NAS server to which the network interface belongs,
      as defined by the I(nas_server) resource type.
    type: str
  host_name:
    description:
    - The name that will be used by NFS clients to connect to this NFS server.
    type: str
  is_nfsv3_enabled:
    description:
    - Indicates whether NFSv3 is enabled on the NAS server.
    type: bool
  is_nfsv4_enabled:
    description:
    - Indicates whether NFSv4 is enabled on the NAS server.
    type: bool
  is_secure_enabled:
    description:
    - Indicates whether secure NFS is enabled on the NFS server.
    type: bool
  is_use_smb_config_enabled:
    description:
    - Indicates whether SMB authentication is used to authenticate to the KDC.
    type: bool
  is_extended_credentials_enabled:
    description:
    - Indicates whether the NFS server supports more than 16 Unix groups in a Unix credential.
    type: bool
  credentials_cache_TTL:
    description:
    - Sets the Time-To-Live (in minutes) expiration time in minutes for a
      Windows entry in the credentials cache.
    type: int
  is_skip_unjoin:
    description:
    - Allow to bypass NFS server unjoin.
    - If false modification will fail if secure is enabled and current kdc_type is MS Windows.
    - If secure is enabled either unjoin NFS server before deleting or set value to true.
    type: bool
  state:
    description:
    - Define whether the NFS server should be enabled or not.
    - For Delete operation only, it should be set to C(absent).
    choices: ['absent', 'present']
    type: str
    default: 'present'

notes:
- The I(check_mode) is supported.
- The details of an NFS server can be fetched using I(nfs_server_id) or
  I(nas_server).
- To set I(is_use_smb_config_enabled) as C(true), I(is_secure_enabled) should be
  set to C(true).
'''

EXAMPLES = r'''

- name: Enable NFS server
  register: result
  dellemc.powerstore.nfs_server:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    nas_server: "{{ nas_server_name }}"
    host_name: "sample.hostname"
    is_nfsv3_enabled: true
    is_nfsv4_enabled: true
    is_secure_enabled: false
    is_extended_credentials_enabled: false
    credentials_cache_TTL: 60
    state: "present"

- name: Get NFS server
  dellemc.powerstore.nfs_server:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    nfs_server_id: "{{ result.nfs_server_details.id }}"

- name: Get NFS server with NAS server
  dellemc.powerstore.nfs_server:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    nas_server: "{{ result.nfs_server_details.nas_server_id }}"

- name: Modify NFS server
  dellemc.powerstore.nfs_server:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    nfs_server_id: "{{ result.nfs_server_details.id }}"
    is_nfsv4_enabled: false
    is_extended_credentials_enabled: true
    credentials_cache_TTL: 120

- name: Delete NFS server
  dellemc.powerstore.nfs_server:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    nfs_server_id: "{{ result.nfs_server_details.id }}"
    state: "absent"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"

nfs_server_details:
    description: Details of the NFS server.
    returned: When NFS server is enabled.
    type: complex
    contains:
        credentials_cache_TTL:
            description: Sets the Time-To-Live (in minutes) expiration timestamp for a Windows entry in the credentials cache.
            type: int
        id:
            description: The unique identifier of the NFS server.
            type: str
        host_name:
            description: The name that will be used by NFS clients to connect to this NFS server.
            type: str
        is_extended_credentials_enabled:
            description: Indicates whether the NFS server supports more than 16 Unix groups in a Unix credential.
            type: bool
        is_joined:
            description: Indicates whether the NFS server is joined to Active Directory.
            type: bool
        is_nfsv3_enabled:
            description: Indicates whether NFSv3 is enabled on the NAS server.
            type: bool
        is_nfsv4_enabled:
            description: Indicates whether NFSv4 is enabled on the NAS server.
            type: bool
        nas_server_id:
            description: Unique identifier of the NAS server.
            type: str
        is_secure_enabled:
            description: Indicates whether secure NFS is enabled on the NFS server.
            type: bool
        is_use_smb_config_enabled:
            description: Indicates whether SMB authentication is used to authenticate to the KDC.
            type: bool
        service_principal_name:
            description: The Service Principal Name (SPN) for the NFS server.
            type: str

    sample: {
        "credentials_cache_TTL": 120,
        "host_name": "sample_host_name",
        "id": "65ad14fe-5f6e-beb3-424f-62b767ad9845",
        "is_extended_credentials_enabled": true,
        "is_joined": false,
        "is_nfsv3_enabled": true,
        "is_nfsv4_enabled": false,
        "is_secure_enabled": false,
        "is_use_smb_config_enabled": null,
        "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
        "service_principal_name": null
    }

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.libraries.powerstore_base \
    import PowerStoreBase
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.libraries.provisioning \
    import Provisioning

LOG = utils.get_logger('nfs_server')

# Application type
APPLICATION_TYPE = 'Ansible/3.2.0'


class PowerStoreNFSServer(PowerStoreBase):
    """Class with NFS server Operations"""

    def __init__(self):

        """Define all parameters for this module."""

        mutually_exclusive = [['nas_server', 'nfs_server_id']]
        ansible_module_params = {
            'argument_spec': get_powerstore_nfs_server_parameters(),
            'supports_check_mode': True,
            'mutually_exclusive': mutually_exclusive
        }
        super().__init__(AnsibleModule, ansible_module_params)

        self.result = dict(
            changed=False,
            nfs_server_details={}
        )
        self.nfs_server = self.conn.nfs_server

    def get_nas_server(self, nas_server=None):
        """Get the details of NAS Server of a given Powerstore storage
        system"""
        return Provisioning(self.provisioning, self.module).get_nas_server(nas_server=nas_server)

    def create_nfs_server(self, create_params, nas_id):
        """Create an NFS server"""
        try:
            self.validate_create(create_params)
            msg = 'Attempting to create an NFS server'
            LOG.info(msg)
            nfs_server_details = {}
            if not self.module.check_mode:
                create_dict = dict()
                create_keys = ['host_name', 'is_nfsv3_enabled', 'is_nfsv4_enabled',
                               'is_secure_enabled', 'is_use_smb_config_enabled',
                               'is_extended_credentials_enabled', 'credentials_cache_TTL']
                for key in create_keys:
                    if create_params[key] is not None:
                        create_dict[key] = create_params[key]

                if nas_id is not None:
                    create_dict['nas_server_id'] = nas_id
                resp = self.nfs_server.create_nfs_server(
                    payload=create_dict)

                if resp:
                    nfs_server_details = self.get_nfs_server_details(
                        nfs_server_id=resp['id'])

                msg = f'Successfully created NFS server with details' \
                      f' {nfs_server_details}'
                LOG.info(msg)

            return nfs_server_details

        except Exception as e:
            msg = (f'Creation of NFS server on PowerStore array failed with error {str(e)} ')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def delete_nfs_server(self, nfs_server_id):
        """ Disable an nfs server """

        try:
            msg = f'Deleting NFS server with identifier:' \
                  f' {nfs_server_id}'
            LOG.info(msg)
            if not self.module.check_mode:
                self.nfs_server.delete_nfs_server(
                    nfs_server_id=nfs_server_id)
                return None
            return self.get_nfs_server_details(
                nfs_server_id=nfs_server_id)

        except Exception as e:
            msg = (f'Deletion of the NFS server {nfs_server_id}'
                   f' failed with error {str(e)}')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_nfs_server_details(self, nfs_server_id=None, nas_server_id=None):
        """ Get nfs server details """

        try:
            msg = (f'Getting nfs server details with '
                   f'nfs_server_id {nfs_server_id} '
                   f'nas_server_id {nas_server_id} ')
            LOG.info(msg)
            nfs_server_details = None
            if nfs_server_id is not None:
                nfs_server_details = self.nfs_server.get_nfs_server_details(
                    nfs_server_id=nfs_server_id)
            elif nas_server_id is not None:
                nfs_servers = self.nfs_server.get_nfs_server_by_nas_server_id(
                    nas_server_id=nas_server_id)
                if len(nfs_servers) == 0:
                    return None
                else:
                    nfs_server_details = nfs_servers[0]

            msg = f'Successfully got NFS server details {nfs_server_details}'
            LOG.info(msg)
            return nfs_server_details

        except Exception as e:
            msg = (f'Getting NFS server details failed with error {str(e)} ')
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR \
                    and e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def is_modify_required(self, nfs_server_details, nfs_server_params):
        """To get the details of the fields to be modified."""

        msg = f'NFS server details: {nfs_server_details}'
        LOG.info(msg)
        modify_dict = dict()

        modify_keys = ['host_name', 'is_nfsv3_enabled',
                       'is_nfsv4_enabled', 'is_secure_enabled',
                       'is_use_smb_config_enabled', 'is_extended_credentials_enabled',
                       'credentials_cache_TTL']

        for key in modify_keys:
            if nfs_server_params[key] is not None and \
                    nfs_server_params[key] != nfs_server_details[key]:
                modify_dict[key] = nfs_server_params[key]
        if nfs_server_params['is_skip_unjoin'] is not None and \
                nfs_server_params['is_skip_unjoin'] != nfs_server_details['is_joined']:
            modify_dict['is_skip_unjoin'] = nfs_server_params['is_skip_unjoin']

        return modify_dict

    def modify_nfs_server_details(self, nfs_server_id,
                                  modify_params):
        """Perform modify operations on an NFS sever"""

        try:
            if not self.module.check_mode:
                self.nfs_server.modify_nfs_server(
                    nfs_server_id=nfs_server_id,
                    modify_parameters=modify_params)
            return self.get_nfs_server_details(
                nfs_server_id=nfs_server_id)
        except Exception as e:
            msg = (f'Failed to modify the NFS server instance '
                   f'with error {str(e)}')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def validate_create(self, create_params):
        """Perform validation of create operations on an SMB server"""

        if create_params['nas_server'] is None:
            err_msg = "NFS server does not exist. Provide nas_server for creation"
            self.module.fail_json(msg=err_msg)


def get_powerstore_nfs_server_parameters():
    """This method provides the parameters required for the ansible
    nfs server modules on PowerStore"""
    return dict(
        nas_server=dict(type='str'),
        nfs_server_id=dict(type='str'),
        host_name=dict(type='str'),
        is_nfsv3_enabled=dict(type='bool'),
        is_nfsv4_enabled=dict(type='bool'),
        is_secure_enabled=dict(type='bool'),
        is_use_smb_config_enabled=dict(type='bool'),
        is_extended_credentials_enabled=dict(type='bool'),
        is_skip_unjoin=dict(type='bool'),
        credentials_cache_TTL=dict(type='int'),
        state=dict(default='present', type='str', choices=['present', 'absent'])
    )


class NFSServerExitHandler():
    def handle(self, nfs_server_obj, nfs_server_details):
        nfs_server_obj.result["nfs_server_details"] = nfs_server_details
        nfs_server_obj.module.exit_json(**nfs_server_obj.result)


class NFSServerDeleteHandler():
    def handle(self, nfs_server_obj, nfs_server_params, nfs_server_details):
        if nfs_server_params['state'] == 'absent' and nfs_server_details:
            nfs_server_details = nfs_server_obj.delete_nfs_server(nfs_server_params['nfs_server_id'])
            nfs_server_obj.result['changed'] = True

        NFSServerExitHandler().handle(nfs_server_obj, nfs_server_details)


class NFSServerModifyHandler():
    def handle(self, nfs_server_obj, nfs_server_params, nfs_server_details):
        if nfs_server_params['state'] == 'present' and nfs_server_details:
            modify_dict = nfs_server_obj.is_modify_required(nfs_server_details, nfs_server_params)
            if modify_dict:
                nfs_server_details = nfs_server_obj.modify_nfs_server_details(nfs_server_id=nfs_server_details['id'],
                                                                              modify_params=modify_dict)
                nfs_server_obj.result['changed'] = True

        NFSServerDeleteHandler().handle(nfs_server_obj, nfs_server_params, nfs_server_details)


class NFSServerCreateHandler():
    def handle(self, nfs_server_obj, nfs_server_params, nfs_server_details, nas_id):
        if nfs_server_params['state'] == 'present' and not nfs_server_details:
            nfs_server_details = nfs_server_obj.create_nfs_server(create_params=nfs_server_params,
                                                                  nas_id=nas_id)
            nfs_server_obj.result['changed'] = True

        NFSServerModifyHandler().handle(nfs_server_obj, nfs_server_params, nfs_server_details)


class NFSServerHandler():
    def handle(self, nfs_server_obj, nfs_server_params):
        nas_id = None
        if nfs_server_params['nas_server']:
            nas_id = nfs_server_obj.get_nas_server(nas_server=nfs_server_params['nas_server'])['id']
        nfs_server_details = nfs_server_obj.get_nfs_server_details(nfs_server_id=nfs_server_params['nfs_server_id'],
                                                                   nas_server_id=nas_id)
        NFSServerCreateHandler().handle(nfs_server_obj, nfs_server_params, nfs_server_details, nas_id)


def main():
    """ Create PowerStore NFS server object and perform action on it
        based on user input from playbook."""
    obj = PowerStoreNFSServer()
    NFSServerHandler().handle(obj, obj.module.params)


if __name__ == '__main__':
    main()
