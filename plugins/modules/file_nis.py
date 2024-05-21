#!/usr/bin/python
# Copyright: (c) 2024, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
module: file_nis
version_added: '3.1.0'
short_description: Manage File NIS for PowerStore
description:
- Managing file NIS on PowerStore Storage System includes enabling
  the file NIS, getting details of a file NIS, modifying a
  file NIS and disabling the file NIS.

author:
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerstore.powerstore

options:
  file_nis_id:
    description:
    - The unique identifier of the file NIS.
    type: str
  nas_server:
    description:
    - Unique identifier/name of the associated NAS Server instance
      that uses this NIS Service object.
    type: str
  domain:
    description:
    - Name of the NIS domain.
    type: str
  add_ip_addresses:
    description:
    - IP addresses to add to the current list.
    - IPv4 and IPv6 are supported.
    type: list
    elements: str
  remove_ip_addresses:
    description:
    - IP addresses to remove from the current list.
    - IPv4 and IPv6 are supported.
    type: list
    elements: str
  is_destination_override_enabled:
    description:
    - In order to modify any properties of this resource when the associated NAS server
      is a replication destination, the I(is_destination_override_enabled) flag must be set to C(true).
    type: bool
  state:
    description:
    - Define whether the file NIS should be enabled or not.
    - For Delete operation only, it should be set to C(absent).
    choices: ['absent', 'present']
    type: str
    default: 'present'

notes:
- The I(check_mode) is supported.
- The details of a file NIS can be fetched using I(file_nis_id) or
  I(nas_server).
'''

EXAMPLES = r'''

- name: Enable file NIS
  register: result
  dellemc.powerstore.file_nis:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    nas_server: "{{ nas_server_name }}"
    domain: "NAS_domain"
    add_ip_addresses:
      - "10.**.**.**"
    state: "present"

- name: Get File NIS
  dellemc.powerstore.file_nis:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    file_nis_id: "{{ result.file_nis_details.id }}"

- name: Get File NIS with NAS server
  dellemc.powerstore.file_nis:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    nas_server: "{{ result.file_nis_details.nas_server_id }}"

- name: Modify File NIS
  dellemc.powerstore.file_nis:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    file_nis_id: "{{ result.file_nis_details.id }}"
    domain: "NAS_domain"
    add_ip_addresses:
      - "10.**.**.@@"
    remove_ip_addresses:
      - "10.**.**.**"

- name: Delete file NIS
  dellemc.powerstore.file_nis:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    file_nis_id: "{{ result.file_nis_details.id }}"
    state: "absent"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"

file_nis_details:
    description: Details of the file NIS.
    returned: When file NIS exists.
    type: complex
    contains:
        domain:
            description: Name of the NIS domain.
            type: str
        id:
            description: The unique identifier of the file NIS.
            type: str
        ip_addresses:
            description: The addresses may be IPv4 or IPv6.
            type: list
            elements: str
        is_destination_override_enabled:
            description: Used in replication context when the user wants to override the settings on the destination.
            type: bool
        nas_server_id:
            description: Unique identifier of the NAS server.
            type: str
    sample: {
        "domain": "NAS_domain",
        "id": "65ab7e44-7009-e3e5-907a-62b767ad9845",
        "ip_addresses": [
            "10.**.**.**"
        ],
        "is_destination_override_enabled": false,
        "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.libraries.powerstore_base \
    import PowerStoreBase
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.libraries.provisioning \
    import Provisioning

LOG = utils.get_logger('file_nis')


class PowerStoreFileNIS(PowerStoreBase):
    """Class with File NIS Operations"""

    def __init__(self):

        """Define all parameters for this module."""
        mutually_exclusive = [['nas_server', 'file_nis_id']]

        ansible_module_params = {
            'argument_spec': get_powerstore_file_nis_parameters(),
            'supports_check_mode': True,
            'mutually_exclusive': mutually_exclusive
        }
        super().__init__(AnsibleModule, ansible_module_params)

        self.result = dict(
            changed=False,
            file_nis_details={}
        )
        self.file_nis = self.conn.file_nis

    def get_nas_server(self, nas_server=None):
        """Get the details of NAS Server of a given Powerstore storage
        system"""
        return Provisioning(self.provisioning, self.module).get_nas_server(nas_server=nas_server)

    def prepare_ip_addresses(self, create_params):
        create_dict = dict()

        if create_params['add_ip_addresses'] is not None and create_params['remove_ip_addresses'] is not None:
            create_dict['ip_addresses'] = [ip for ip in create_params['add_ip_addresses'] if ip not in create_params['remove_ip_addresses']]
        elif create_params['add_ip_addresses'] is not None and create_params['remove_ip_addresses'] is None:
            create_dict['ip_addresses'] = create_params['add_ip_addresses']

        return create_dict

    def create_file_nis(self, create_params, nas_id):
        """Enable the File NIS"""
        try:
            self.validate_create(create_params)
            msg = 'Attempting to create a file NIS'
            LOG.info(msg)
            file_nis_details = {}
            if not self.module.check_mode:
                create_dict = dict()

                create_dict = self.prepare_ip_addresses(create_params)

                if create_params['domain'] is not None:
                    create_dict['domain'] = create_params['domain']
                if nas_id is not None:
                    create_dict['nas_server_id'] = nas_id
                resp = self.file_nis.create_file_nis(
                    payload=create_dict)

                if resp:
                    file_nis_details = self.get_file_nis_details(
                        file_nis_id=resp['id'])

                msg = f'Successfully created File NIS with details' \
                      f' {file_nis_details}'
                LOG.info(msg)

            return file_nis_details

        except Exception as e:
            msg = (f'Creation of File NIS on PowerStore array failed with error {str(e)} ')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def delete_file_nis(self, file_nis_id):
        """ Disable the File NIS """

        try:
            msg = f'Deleting File nis with identifier:' \
                  f' {file_nis_id}'
            LOG.info(msg)
            if not self.module.check_mode:
                self.file_nis.delete_file_nis(
                    file_nis_id=file_nis_id)
                return None
            return self.get_file_nis_details(
                file_nis_id=file_nis_id)

        except Exception as e:
            msg = (f'Deletion of the File NIS {file_nis_id}'
                   f' failed with error {str(e)}')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_file_nis_details(self, file_nis_id=None, nas_server_id=None):
        """ Get File nis details """

        try:
            msg = (f'Getting File nis details with '
                   f'file_nis_id {file_nis_id} '
                   f'nas_server_id {nas_server_id} ')
            LOG.info(msg)
            file_nis_details = None
            if file_nis_id is not None:
                file_nis_details = self.file_nis.get_file_nis_details(
                    file_nis_id=file_nis_id)
            elif nas_server_id is not None:
                file_niss = self.file_nis.get_file_nis_by_nas_server_id(
                    nas_server_id=nas_server_id)
                if len(file_niss) == 0:
                    return None
                else:
                    file_nis_details = file_niss[0]

            msg = f'Successfully got File NIS details {file_nis_details}'
            LOG.info(msg)
            return file_nis_details

        except Exception as e:
            msg = (f'Getting File NIS details failed with error {str(e)} ')
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR \
                    and e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def modify_ip_addresses(self, file_nis_details, file_nis_params):
        modify_dict = dict()

        if file_nis_params['add_ip_addresses'] is None and file_nis_params['remove_ip_addresses'] is not None:
            ip_addresses_list = [ip for ip in file_nis_details['ip_addresses'] if ip not in file_nis_params['remove_ip_addresses']]
            if set(ip_addresses_list) != set(file_nis_details['ip_addresses']):
                modify_dict['ip_addresses'] = ip_addresses_list

        elif file_nis_params['add_ip_addresses'] is not None and file_nis_params['remove_ip_addresses'] is not None:
            ip_addresses_list = list(set(file_nis_params['add_ip_addresses']) | set(file_nis_details['ip_addresses']))
            final_ip_addresses_list = [ip for ip in ip_addresses_list if ip not in file_nis_params['remove_ip_addresses']]
            if set(final_ip_addresses_list) != set(file_nis_details['ip_addresses']):
                modify_dict['ip_addresses'] = final_ip_addresses_list

        elif file_nis_params['add_ip_addresses'] is not None and file_nis_params['remove_ip_addresses'] is None:
            ip_addresses_list = list(set(file_nis_params['add_ip_addresses']) | set(file_nis_details['ip_addresses']))
            if set(ip_addresses_list) != set(file_nis_details['ip_addresses']):
                modify_dict['ip_addresses'] = ip_addresses_list

        return modify_dict

    def is_modify_required(self, file_nis_details, file_nis_params):
        """To get the details of the fields to be modified."""

        msg = f'File NIS details: {file_nis_details}'
        LOG.info(msg)
        modify_dict = dict()

        modify_dict = self.modify_ip_addresses(file_nis_details, file_nis_params)

        if file_nis_params['domain'] is not None and \
                file_nis_params['domain'] != file_nis_details['domain']:
            modify_dict['domain'] = file_nis_params['domain']

        if file_nis_params['is_destination_override_enabled'] is not None:
            modify_dict['is_destination_override_enabled'] = file_nis_params['is_destination_override_enabled']

        return modify_dict

    def modify_file_nis_details(self, file_nis_id,
                                modify_params):
        """Perform modify operations on a File NIS"""

        try:
            if not self.module.check_mode:
                self.file_nis.modify_file_nis(
                    file_nis_id=file_nis_id,
                    modify_parameters=modify_params)
            return self.get_file_nis_details(
                file_nis_id=file_nis_id)
        except Exception as e:
            msg = (f'Failed to modify the File NIS instance '
                   f'with error {str(e)}')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def validate_create(self, create_params):
        """Perform validation of create operations on a File NIS"""

        if create_params['nas_server'] is None or \
                create_params['add_ip_addresses'] is None or \
                create_params['domain'] is None:
            err_msg = "File NIS does not exist. Provide nas_server, add_ip_addresses and domain for creation."
            self.module.fail_json(msg=err_msg)


def get_powerstore_file_nis_parameters():
    """This method provides the parameters required for the ansible
    File NIS modules on PowerStore"""
    return dict(
        nas_server=dict(type='str'),
        file_nis_id=dict(type='str'),
        domain=dict(type='str'),
        add_ip_addresses=dict(type='list', elements='str'),
        remove_ip_addresses=dict(type='list', elements='str'),
        is_destination_override_enabled=dict(type='bool'),
        state=dict(default='present', type='str', choices=['present', 'absent'])
    )


class FileNISExitHandler():
    def handle(self, file_nis_obj, file_nis_details):
        file_nis_obj.result["file_nis_details"] = file_nis_details
        file_nis_obj.module.exit_json(**file_nis_obj.result)


class FileNISDeleteHandler():
    def handle(self, file_nis_obj, file_nis_params, file_nis_details):
        if file_nis_params['state'] == 'absent' and file_nis_details:
            file_nis_details = file_nis_obj.delete_file_nis(file_nis_params['file_nis_id'])
            file_nis_obj.result['changed'] = True

        FileNISExitHandler().handle(file_nis_obj, file_nis_details)


class FileNISModifyHandler():
    def handle(self, file_nis_obj, file_nis_params, file_nis_details):
        if file_nis_params['state'] == 'present' and file_nis_details:
            modify_dict = file_nis_obj.is_modify_required(file_nis_details, file_nis_params)
            if modify_dict:
                file_nis_details = file_nis_obj.modify_file_nis_details(file_nis_id=file_nis_details['id'],
                                                                        modify_params=modify_dict)
                file_nis_obj.result['changed'] = True

        FileNISDeleteHandler().handle(file_nis_obj, file_nis_params, file_nis_details)


class FileNISCreateHandler():
    def handle(self, file_nis_obj, file_nis_params, file_nis_details, nas_id):
        if file_nis_params['state'] == 'present' and not file_nis_details:
            file_nis_details = file_nis_obj.create_file_nis(create_params=file_nis_params,
                                                            nas_id=nas_id)
            file_nis_obj.result['changed'] = True

        FileNISModifyHandler().handle(file_nis_obj, file_nis_params, file_nis_details)


class FileNISHandler():
    def handle(self, file_nis_obj, file_nis_params):
        nas_id = None
        if file_nis_params['nas_server']:
            nas_id = file_nis_obj.get_nas_server(nas_server=file_nis_params['nas_server'])['id']
        file_nis_details = file_nis_obj.get_file_nis_details(file_nis_id=file_nis_params['file_nis_id'],
                                                             nas_server_id=nas_id)
        FileNISCreateHandler().handle(file_nis_obj, file_nis_params, file_nis_details, nas_id)


def main():
    """ Create PowerStore File NIS object and perform action on it
        based on user input from playbook."""
    obj = PowerStoreFileNIS()
    FileNISHandler().handle(obj, obj.module.params)


if __name__ == '__main__':
    main()
