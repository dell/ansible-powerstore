#!/usr/bin/python
# Copyright: (c) 2024, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
module: file_interface
version_added: '3.1.0'
short_description: Manage File interface for PowerStore
description:
- Managing file interfaces on PowerStore Storage System includes creating
  a file interface, getting details of a file interface, modifying a
  file interface and deleting a file interface.

author:
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerstore.powerstore

options:
  file_interface_id:
    description:
    - The unique identifier of the file interface.
    type: str
  nas_server:
    description:
    - Unique identifier/name of the NAS server to which the network interface belongs,
      as defined by the I(nas_server) resource type.
    type: str
  ip_address:
    description:
    - IP address of the network interface.
    - IPv4 and IPv6 are supported.
    type: str
  prefix_length:
    description:
    - Prefix length for the interface.
    - IPv4 and IPv6 are supported.
    type: int
  gateway:
    description:
    - Gateway address for the network interface.
    - IPv4 and IPv6 are supported.
    type: str
  vlan_id:
    description:
    - Virtual Local Area Network (VLAN) identifier for the interface.
    type: int
  role:
    description:
    - C(Production) type of network interface is used for all file protocols and services of a NAS server.
      This type of interface is inactive while a NAS server is in destination mode.
    - C(Backup) type of network interface is used only for NDMP/NFS backup or disaster recovery testing.
      This type of interface is always active in all NAS server modes.
    - C(System) type of interface are reserved for system traffic such as for NAS server migration, they can't be used for the production traffic.
    - C(System) type is not supported during create interface.
    choices: ['Production', 'Backup', 'System']
    type: str
  is_disabled:
    description:
    - Indicates whether the network interface is disabled.
    type: bool
  ip_port_id:
    description:
    - Unique Identifier of the IP Port that is associated with the file interface.
    type: str
  is_destination_override_enabled:
    description:
    - Used in replication context when the user wants to override the settings on the destination.
    type: bool
  state:
    description:
    - Define whether the file interface should exist or not.
    - For Delete operation only, it should be set to C(absent).
    choices: ['absent', 'present']
    type: str
    default: 'present'

notes:
- The I(check_mode) is supported.
- The details of a file interface can be fetched using I(file_interface_id) or
  I(nas_server) and I(ip_address)
'''

EXAMPLES = r'''

- name: Create File interface
  register: result
  dellemc.powerstore.file_interface:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    nas_server: "{{ nas_server_id }}"
    ip_address: "10.**.**.**"
    vlan_id: 0
    prefix_length: 21
    gateway: "10.**.**.1"
    state: "present"

- name: Get file interface with file_interface_id
  dellemc.powerstore.file_interface:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    file_interface_id: "{{ file_interface_id }}"

- name: Get file interface with nas_server_name and ip_addresss
  dellemc.powerstore.file_interface:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    nas_server: "sample_nas_server"
    ip_address: "10.**.**.**"

- name: Modify file interface
  dellemc.powerstore.file_interface:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    file_interface_id: "{{ file_interface_id }}"
    ip_address: "10.**.**.@@"
    vlan_id: 0
    prefix_length: 21
    gateway: "10.**.**.1"
    state: "present"

- name: Delete file interface
  dellemc.powerstore.file_interface:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    file_interface_id: "{{ file_interface_id }}"
    state: "absent"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"

file_interface_details:
    description: Details of the file interface.
    returned: When file interface exists.
    type: complex
    contains:
        gateway:
            description: Gateway address for the network interface.
            type: str
        id:
            description: The unique identifier of the file interface.
            type: str
        ip_address:
            description: IP address of the network interface.
            type: str
        ip_port_id:
            description: Unique Identifier of the IP Port that is associated with the file interface.
            type: str
        is_destination_override_enabled:
            description: Used in replication context when the user wants to override the settings on the destination.
            type: bool
        is_disabled:
            description: Indicates whether the network interface is disabled.
            type: bool
        name:
            description: Name of the network interface.
                         This property supports case-insensitive filtering.
            type: str
        nas_server_id:
            description: Unique identifier of the NAS server.
            type: str
        prefix_length:
            description: Prefix length for the interface.
            type: int
        role:
            description: Role of the interface
            type: str
        vlan_id:
            description: Virtual Local Area Network (VLAN) identifier for the interface.
            type: int

    sample: {
        "gateway": "10.**.**.1",
        "id": "65a50e0d-25f9-bd0a-8ca7-62b767ad9845",
        "ip_address": "10.**.**.**",
        "ip_port_id": "IP_PORT2",
        "is_destination_override_enabled": False,
        "is_disabled": False,
        "is_dr_test": False,
        "name": "PROD022_19c8adfb1d41_1d",
        "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
        "prefix_length": 21,
        "role": "Production",
        "source_parameters": None,
        "vlan_id": 0
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.libraries.powerstore_base \
    import PowerStoreBase
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.libraries.provisioning \
    import Provisioning

LOG = utils.get_logger('file_interface')

# Application type
APPLICATION_TYPE = 'Ansible/3.1.0'


class PowerStoreFileInterface(PowerStoreBase):
    """Class with File Interface Operations"""
    cluster_name = None
    cluster_global_id = None

    def __init__(self):

        """Define all parameters for this module."""

        ansible_module_params = {
            'argument_spec': get_powerstore_file_interface_parameters(),
            'supports_check_mode': True
        }
        super().__init__(AnsibleModule, ansible_module_params)

        self.result = dict(
            changed=False,
            file_interface_details={}
        )
        self.file_interface = self.conn.file_interface

    def get_nas_server(self, nas_server=None):
        """Get the details of NAS Server of a given Powerstore storage
        system"""
        return Provisioning(self.provisioning, self.module).get_nas_server(nas_server=nas_server)

    def create_file_interface(self, create_params):
        """Create a file interface"""
        try:
            self.validate_create(create_params)
            msg = 'Attempting to create a file interface'
            LOG.info(msg)
            file_interface_details = {}
            if not self.module.check_mode:
                create_dict = dict()
                create_keys = ['ip_address', 'vlan_id', 'gateway',
                               'prefix_length', 'role',
                               'is_disabled', 'ip_port_id']
                for key in create_keys:
                    if create_params[key] is not None:
                        create_dict[key] = create_params[key]

                if create_params['nas_server'] is not None:
                    create_dict['nas_server_id'] = create_params['nas_server']
                resp = self.file_interface.create_file_interface(
                    payload=create_dict)

                if resp:
                    file_interface_details = self.get_file_interface_details(
                        file_interface_id=resp['id'])

                msg = (f'Successfully created file interface with details'
                       f' {file_interface_details}')
                LOG.info(msg)

            return file_interface_details

        except Exception as e:
            msg = (f'Creation of file interface on PowerStore array name : '
                   f'{self.cluster_name} , global id : '
                   f'{self.cluster_global_id} failed with error {str(e)} ')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def delete_file_interface(self, file_interface_id):
        """ Delete a file interface """

        try:
            msg = f'Deleting file interface with identifier:' \
                  f' {file_interface_id}'
            LOG.info(msg)
            if not self.module.check_mode:
                self.file_interface.delete_file_interface(
                    file_interface_id=file_interface_id)
                return None
            return self.get_file_interface_details(
                file_interface_id=file_interface_id)

        except Exception as e:
            msg = (f'Deletion of the file interface {file_interface_id}'
                   f' failed with error {str(e)}')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_file_interface_details(self, file_interface_id=None, nas_server_id=None, ip_address=None):
        """ Get file interface details by id """

        try:
            msg = (f'Getting file interface details with '
                   f'file_interface_id {file_interface_id} '
                   f'nas_server_id {nas_server_id} '
                   f'ip_address {ip_address}')
            LOG.info(msg)
            file_interface_details = None
            if file_interface_id is not None:
                file_interface_details = self.file_interface.get_file_interface_details(
                    file_interface_id=file_interface_id)
            elif nas_server_id is not None and ip_address is not None:
                file_interfaces = self.file_interface.get_file_interface_by_nas_server_id(
                    nas_server_id=nas_server_id,
                    ip_address=ip_address)
                if len(file_interfaces) == 0:
                    return None
                else:
                    file_interface_details = file_interfaces[0]

            msg = f'Successfully got file interface details {file_interface_details}'
            LOG.info(msg)
            return file_interface_details

        except Exception as e:
            msg = (f'Get file interface details for PowerStore array failed with error {str(e)} ')
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR \
                    and e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def is_modify_required(self, file_interface_details, file_interface_params):
        """To get the details of the fields to be modified."""

        msg = f'File interface details: {file_interface_details}'
        LOG.info(msg)
        modify_dict = dict()

        modify_keys = ["ip_address", "prefix_length", "gateway",
                       "vlan_id", "is_disabled", "ip_port_id",
                       "is_destination_override_enabled"]
        for key in modify_keys:
            if file_interface_params[key] is not None and \
                    file_interface_params[key] != file_interface_details[key]:
                modify_dict[key] = file_interface_params[key]
 
        return modify_dict

    def modify_file_interface_details(self, file_interface_id,
                                      modify_params):
        """Perform modify operations on a file interface"""

        try:
            if not self.module.check_mode:
                self.file_interface.modify_file_interface(
                    file_interface_id=file_interface_id,
                    modify_parameters=modify_params)
            return self.get_file_interface_details(
                file_interface_id=file_interface_id)
        except Exception as e:
            msg = (f'Failed to modify the file interface instance '
                   f'with error {str(e)}')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def validate_create(self, create_params):
        """Perform validation of create operations on a File interface"""

        if create_params['nas_server'] is None or \
                create_params['ip_address'] is None or \
                create_params['prefix_length'] is None:
            err_msg = "File interface does not exist. Provide nas_server, ip_address and prefix_length for creation."
            self.module.fail_json(msg=err_msg)

    def validate_params(self, file_interface_params):
        """Perform validation of parameters of a File interface"""

        if file_interface_params['nas_server'] is not None and \
                file_interface_params['ip_address'] is not None and \
                file_interface_params['file_interface_id'] is not None:
            err_msg = "file_interface_id is mutually exclusive with nas_server and ip_address."
            self.module.fail_json(msg=err_msg)


def get_powerstore_file_interface_parameters():
    """This method provides the parameters required for the ansible
    file interface module on PowerStore"""
    return dict(
        nas_server=dict(type='str'),
        file_interface_id=dict(type='str'),
        ip_address=dict(type='str'),
        gateway=dict(type='str'),
        prefix_length=dict(type='int'),
        vlan_id=dict(type='int'),
        ip_port_id=dict(type='str'),
        is_disabled=dict(type='bool'),
        role=dict(type='str',
                  choices=['Production', 'Backup', 'System']),
        is_destination_override_enabled=dict(type='bool'),
        state=dict(default='present', type='str', choices=['present', 'absent'])
    )


class FileInterfaceExitHandler():
    def handle(self, file_interface_obj, file_interface_details):
        file_interface_obj.result["file_interface_details"] = file_interface_details
        file_interface_obj.module.exit_json(**file_interface_obj.result)


class FileInterfaceDeleteHandler():
    def handle(self, file_interface_obj, file_interface_params, file_interface_details):
        if file_interface_params['state'] == 'absent' and file_interface_details:
            file_interface_details = file_interface_obj.delete_file_interface(file_interface_params['file_interface_id'])
            file_interface_obj.result['changed'] = True

        FileInterfaceExitHandler().handle(file_interface_obj, file_interface_details)


class FileInterfaceModifyHandler():
    def handle(self, file_interface_obj, file_interface_params, file_interface_details):
        if file_interface_params['state'] == 'present' and file_interface_details:
            modify_dict = file_interface_obj.is_modify_required(file_interface_details, file_interface_params)
            if modify_dict:
                file_interface_details = file_interface_obj.modify_file_interface_details(file_interface_id=file_interface_params['file_interface_id'],
                                                                                          modify_params=modify_dict)
                file_interface_obj.result['changed'] = True

        FileInterfaceDeleteHandler().handle(file_interface_obj, file_interface_params, file_interface_details)


class FileInterfaceCreateHandler():
    def handle(self, file_interface_obj, file_interface_params, file_interface_details):
        if file_interface_params['state'] == 'present' and not file_interface_details:
            file_interface_details = file_interface_obj.create_file_interface(file_interface_params)
            file_interface_obj.result['changed'] = True

        FileInterfaceModifyHandler().handle(file_interface_obj, file_interface_params, file_interface_details)


class FileInterfaceHandler():
    def handle(self, file_interface_obj, file_interface_params):
        file_interface_obj.validate_params(file_interface_params=file_interface_params)
        nas_id = None
        if file_interface_params['nas_server']:
            nas_id = file_interface_obj.get_nas_server(nas_server=file_interface_params['nas_server'])['id']
        if nas_id:
            file_interface_params['nas_server'] = nas_id
        file_interface_details = file_interface_obj.get_file_interface_details(file_interface_id=file_interface_params['file_interface_id'],
                                                                               nas_server_id=file_interface_params['nas_server'],
                                                                               ip_address=file_interface_params['ip_address'])
        FileInterfaceCreateHandler().handle(file_interface_obj, file_interface_params, file_interface_details)


def main():
    """ Create PowerStore File Interface object and perform action on it
        based on user input from playbook."""
    obj = PowerStoreFileInterface()
    FileInterfaceHandler().handle(obj, obj.module.params)


if __name__ == '__main__':
    main()
