#!/usr/bin/python
# Copyright: (c) 2024, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
module: smb_server
version_added: '3.1.0'
short_description: Manage SMB server for PowerStore
description:
- Managing storage containers on PowerStore Storage System includes creating
  an SMB server, getting details of an SMB server, modifying an
  SMB server and deleting an SMB server.

author:
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerstore.powerstore

options:
  smb_server_id:
    description:
    - The unique identifier of the SMB server.
    type: str
  nas_server:
    description:
    - Unique identifier/name of the NAS server to which the network interface belongs,
      as defined by the I(nas_server) resource type.
    type: str
  is_standalone:
    description:
    - Indicates whether the SMB server is standalone.
    - I(true) - SMB server is standalone.
    - I(false) - SMB server is joined to the Active Directory.
    type: bool
  computer_name:
    description:
    - DNS Name of the associated Computer Account when the SMB server is joined to an Active Directory domain.
    type: str
  domain:
    description:
    - Domain name where SMB server is registered in Active Directory, if applicable.
    type: str
  netbios_name:
    description:
    - NetBIOS name is the network name of the standalone SMB server.
    type: str
  workgroup:
    description:
    - Windows network workgroup for the SMB server.
    - Applies to standalone SMB servers only.
    type: str
  description:
    description:
    - Description of the SMB server in UTF-8 characters.
    type: str
  local_admin_password:
    description:
    - Password for the local administrator account of the SMB server.
    type: str
  state:
    description:
    - Define whether the SMB server should be enabled or not.
    - For Delete operation only, it should be set to C(absent).
    choices: ['absent', 'present']
    type: str
    default: 'present'

notes:
- The I(check_mode) is supported.
- The details of an SMB server can be fetched using I(smb_server_id) or
  I(nas_server).
'''

EXAMPLES = r'''

- name: Enable SMB server
  register: result
  dellemc.powerstore.smb_server:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    nas_server: "{{ nas_server_name }}"
    is_standalone: true
    netbios_name: "string"
    workgroup: "string"
    description: "string"
    local_admin_password: "string"
    state: "present"

- name: Get SMB server
  dellemc.powerstore.smb_server:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    smb_server_id: "{{ result.smb_server_details.id }}"

- name: Get SMB server with NAS server
  dellemc.powerstore.smb_server:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    nas_server: "{{ result.smb_server_details.nas_server_id }}"

- name: Modify SMB server
  dellemc.powerstore.smb_server:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    smb_server_id: "{{ result.smb_server_details.id }}"
    netbios_name: "string2"
    workgroup: "string2"
    description: "string2"
    local_admin_password: "string2"

- name: Delete SMB server
  dellemc.powerstore.smb_server:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    smb_server_id: "{{ result.smb_server_details.id }}"
    state: "absent"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"

smb_server_details:
    description: Details of the SMB server.
    returned: When SMB server exists.
    type: complex
    contains:
        computer_name:
            description: DNS name of the associated computer account when the SMB server is joined to an Active Directory domain.
            type: str
        id:
            description: The unique identifier of the SMB server.
            type: str
        description:
            description: Description of the SMB server.
            type: str
        domain:
            description: Domain name where SMB server is registered in Active Directory, if applicable.
            type: str
        is_joined:
            description: Indicates whether the SMB server is joined to the Active Directory.
            type: bool
        is_standalone:
            description: Indicates whether the SMB server is standalone.
            type: bool
        netbios_name:
            description: NetBIOS name is the network name of the standalone SMB server.
            type: str
        nas_server_id:
            description: Unique identifier of the NAS server.
            type: str
        workgroup:
            description: Windows network workgroup for the SMB server.
            type: str

    sample: {
        "computer_name": null,
        "description": "string2",
        "domain": null,
        "id": "65ad211b-374b-5f77-2946-62b767ad9845",
        "is_joined": false,
        "is_standalone": true,
        "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
        "netbios_name": "STRING2",
        "workgroup": "STRING2"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.libraries.powerstore_base \
    import PowerStoreBase
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.libraries.provisioning \
    import Provisioning

LOG = utils.get_logger('smb_server')


class PowerStoreSMBServer(PowerStoreBase):
    """Class with SMB server Operations"""

    def __init__(self):

        """Define all parameters for this module."""

        mutually_exclusive = [['nas_server', 'smb_server_id']]
        ansible_module_params = {
            'argument_spec': get_powerstore_smb_server_parameters(),
            'supports_check_mode': True,
            'mutually_exclusive': mutually_exclusive
        }
        super().__init__(AnsibleModule, ansible_module_params)

        self.result = dict(
            changed=False,
            smb_server_details={}
        )
        self.smb_server = self.conn.smb_server

    def get_nas_server(self, nas_server=None):
        """Get the details of NAS Server of a given Powerstore storage
        system"""
        return Provisioning(self.provisioning, self.module).get_nas_server(nas_server=nas_server)

    def create_smb_server(self, create_params, nas_id):
        """Create an SMB server"""
        try:
            self.validate_create(create_params)
            msg = 'Attempting to create an SMB server'
            LOG.info(msg)
            smb_server_details = {}
            if not self.module.check_mode:
                create_dict = dict()
                create_keys = ['is_standalone', 'computer_name',
                               'domain', 'netbios_name', 'workgroup',
                               'description', 'local_admin_password']
                for key in create_keys:
                    if create_params[key] is not None:
                        create_dict[key] = create_params[key]

                if nas_id is not None:
                    create_dict['nas_server_id'] = nas_id
                resp = self.smb_server.create_smb_server(
                    payload=create_dict)

                if resp:
                    smb_server_details = self.get_smb_server_details(
                        smb_server_id=resp['id'])

                msg = f'Successfully created SMB server with details' \
                      f' {smb_server_details}'
                LOG.info(msg)

            return smb_server_details

        except Exception as e:
            msg = (f'Creation of SMB server on PowerStore array failed with error {str(e)} ')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def delete_smb_server(self, smb_server_id):
        """ Disable an SMB server """

        try:
            msg = f'Deleting SMB server with identifier:' \
                  f' {smb_server_id}'
            LOG.info(msg)
            if not self.module.check_mode:
                self.smb_server.delete_smb_server(
                    smb_server_id=smb_server_id)
                return None
            return self.get_smb_server_details(
                smb_server_id=smb_server_id)

        except Exception as e:
            msg = (f'Deletion of the SMB server {smb_server_id}'
                   f' failed with error {str(e)}')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_smb_server_details(self, smb_server_id=None, nas_server_id=None):
        """ Get SMB server details """

        try:
            msg = (f'Getting SMB server details with '
                   f'smb_server_id {smb_server_id} '
                   f'nas_server_id {nas_server_id} ')
            LOG.info(msg)
            smb_server_details = None
            if smb_server_id is not None:
                smb_server_details = self.smb_server.get_smb_server_details(
                    smb_server_id=smb_server_id)
            elif nas_server_id is not None:
                smb_servers = self.smb_server.get_smb_server_by_nas_server_id(
                    nas_server_id=nas_server_id)
                if len(smb_servers) == 0:
                    return None
                else:
                    smb_server_details = smb_servers[0]

            msg = f'Successfully got SMB server details {smb_server_details}'
            LOG.info(msg)
            return smb_server_details

        except Exception as e:
            msg = (f'Getting SMB server details failed with error {str(e)} ')
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR \
                    and e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def is_modify_required(self, smb_server_details, smb_server_params):
        """To get the details of the fields to be modified."""

        msg = f'SMB server details: {smb_server_details}'
        LOG.info(msg)
        modify_dict = dict()

        modify_keys = ['is_standalone', 'computer_name',
                       'domain', 'description']
        modify_keys_up = ['netbios_name', 'workgroup']

        for key in modify_keys:
            if smb_server_params[key] is not None and \
                    smb_server_params[key] != smb_server_details[key]:
                modify_dict[key] = smb_server_params[key]
        for key in modify_keys_up:
            if smb_server_params[key] is not None and \
                    smb_server_params[key].lower() != smb_server_details[key].lower():
                modify_dict[key] = smb_server_params[key]

        return modify_dict

    def modify_smb_server_details(self, smb_server_id,
                                  modify_params):
        """Perform modify operations on an SMB sever"""

        try:
            if not self.module.check_mode:
                self.smb_server.modify_smb_server(
                    smb_server_id=smb_server_id,
                    modify_parameters=modify_params)
            return self.get_smb_server_details(
                smb_server_id=smb_server_id)
        except Exception as e:
            msg = (f'Failed to modify the SMB server instance '
                   f'with error {str(e)}')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def validate_create(self, create_params):
        """Perform validation of create operations on an SMB server"""

        if create_params['nas_server'] is None or \
                create_params['is_standalone'] is None or \
                create_params['local_admin_password'] is None:
            err_msg = "SMB server does not exist. Provide nas_server, is_standalone and local_admin_password for creation"
            self.module.fail_json(msg=err_msg)


def get_powerstore_smb_server_parameters():
    """This method provides the parameters required for the ansible
    SMB server modules on PowerStore"""
    return dict(
        nas_server=dict(type='str'),
        smb_server_id=dict(type='str'),
        is_standalone=dict(type='bool'),
        computer_name=dict(type='str'),
        domain=dict(type='str'),
        netbios_name=dict(type='str'),
        workgroup=dict(type='str'),
        description=dict(type='str'),
        local_admin_password=dict(type='str', no_log=True),
        state=dict(default='present', type='str', choices=['present', 'absent'])
    )


class SMBServerExitHandler():
    def handle(self, smb_server_obj, smb_server_details):
        smb_server_obj.result["smb_server_details"] = smb_server_details
        smb_server_obj.module.exit_json(**smb_server_obj.result)


class SMBServerDeleteHandler():
    def handle(self, smb_server_obj, smb_server_params, smb_server_details):
        if smb_server_params['state'] == 'absent' and smb_server_details:
            smb_server_details = smb_server_obj.delete_smb_server(smb_server_params['smb_server_id'])
            smb_server_obj.result['changed'] = True

        SMBServerExitHandler().handle(smb_server_obj, smb_server_details)


class SMBServerModifyHandler():
    def handle(self, smb_server_obj, smb_server_params, smb_server_details):
        if smb_server_params['state'] == 'present' and smb_server_details:
            modify_dict = smb_server_obj.is_modify_required(smb_server_details, smb_server_params)
            if modify_dict:
                smb_server_details = smb_server_obj.modify_smb_server_details(smb_server_id=smb_server_details['id'],
                                                                              modify_params=modify_dict)
                smb_server_obj.result['changed'] = True

        SMBServerDeleteHandler().handle(smb_server_obj, smb_server_params, smb_server_details)


class SMBServerCreateHandler():
    def handle(self, smb_server_obj, smb_server_params, smb_server_details, nas_id):
        if smb_server_params['state'] == 'present' and not smb_server_details:
            smb_server_details = smb_server_obj.create_smb_server(create_params=smb_server_params,
                                                                  nas_id=nas_id)
            smb_server_obj.result['changed'] = True

        SMBServerModifyHandler().handle(smb_server_obj, smb_server_params, smb_server_details)


class SMBServerHandler():
    def handle(self, smb_server_obj, smb_server_params):
        nas_id = None
        if smb_server_params['nas_server']:
            nas_id = smb_server_obj.get_nas_server(nas_server=smb_server_params['nas_server'])['id']
        smb_server_details = smb_server_obj.get_smb_server_details(smb_server_id=smb_server_params['smb_server_id'],
                                                                   nas_server_id=nas_id)

        SMBServerCreateHandler().handle(smb_server_obj, smb_server_params, smb_server_details, nas_id)


def main():
    """ Create PowerStore SMB server object and perform action on it
        based on user input from playbook."""
    obj = PowerStoreSMBServer()
    SMBServerHandler().handle(obj, obj.module.params)


if __name__ == '__main__':
    main()
