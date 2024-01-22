#!/usr/bin/python
# Copyright: (c) 2024, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
module: file_dns
version_added: '3.1.0'
short_description: Manage File DNS for PowerStore
description:
- Managing storage containers on PowerStore Storage System includes creating
  a file DNS, getting details of a file DNS, modifying a
  file DNS and deleting a file DNS.

author:
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerstore.powerstore

options:
  file_dns_id:
    description:
    - The unique identifier of the file DNS.
    type: str
  nas_server:
    description:
    - Unique identifier/name of the associated NAS Server
      instance that uses this DNS Service object.
    type: str
  domain:
    description:
    - Name of the DNS domain, where the NAS Server does host
      names lookup when an FQDN is not specified in the request.
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
  transport:
    description:
    - Transport used when connecting to the DNS Server.
    - C(UDP) - DNS uses the UDP protocol.
    - C(TCP) - DNS uses the TCP protocol.
    choices: ['UDP', 'TCP']
    type: str
  is_destination_override_enabled:
    description:
    - In order to modify any properties of this resource when the associated NAS server
      is a replication destination, the is_destination_override_enabled flag must be set to true.
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
- The details of a file DNS can be fetched using I(file_dns_id) or
  I(nas_server)
'''

EXAMPLES = r'''

- name: Enable file DNS
  register: result
  dellemc.powerstore.file_dns:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    nas_server: "{{ nas_server_name }}"
    domain: "NAS_domain"
    add_ip_addresses:
      - "10.**.**.**"
    transport: "UDP"
    state: "present"

- name: Get File DNS
  dellemc.powerstore.file_dns:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    file_dns_id: "{{ result.file_dns_details.id }}"

- name: Get File DNS with NAS server
  dellemc.powerstore.file_dns:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    nas_server: "{{ result.file_dns_details.nas_server_id }}"

- name: Modify File DNS
  dellemc.powerstore.file_dns:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    file_dns_id: "{{ result.file_dns_details.id }}"
    domain: "NAS_domain"
    add_ip_addresses:
      - "10.**.**.@@"
    remove_ip_addresses:
      - "10.**.**.**"
    transport: "UDP"

- name: Delete file DNS
  dellemc.powerstore.file_dns:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    file_dns_id: "{{ result.file_dns_details.id }}"
    state: "absent"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"

file_nis_details:
    description: Details of the file DNS.
    returned: When file DNS exists.
    type: complex
    contains:
        domain:
            description: Name of the DNS domain.
            type: str
        id:
            description: The unique identifier of the file DNS.
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
        transport:
            description: Transport used when connecting to the DNS Server.
            type: str
    sample: {
        "domain": "NAS_domain",
        "id": "65ab7e44-7009-e3e5-907a-62b767ad9845",
        "ip_addresses": [
            "10.10.10.11"
        ],
        "is_destination_override_enabled": false,
        "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
        "transport": "UDP"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.libraries.powerstore_base \
    import PowerStoreBase
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.libraries.provisioning \
    import Provisioning

LOG = utils.get_logger('file_dns')

# Application type
APPLICATION_TYPE = 'Ansible/3.1.0'


class PowerStoreFileDNS(PowerStoreBase):
    """Class with File DNS Operations"""

    def __init__(self):

        """Define all parameters for this module."""

        mutually_exclusive = [['nas_server', 'file_dns_id']]

        ansible_module_params = {
            'argument_spec': get_powerstore_file_dns_parameters(),
            'supports_check_mode': True,
            'mutually_exclusive': mutually_exclusive
        }
        super().__init__(AnsibleModule, ansible_module_params)

        self.result = dict(
            changed=False,
            file_dns_details={}
        )
        self.file_dns = self.conn.file_dns

    def get_nas_server(self, nas_server=None):
        """Get the details of NAS Server of a given Powerstore storage
        system"""
        return Provisioning(self.provisioning, self.module).get_nas_server(nas_server=nas_server)

    def create_file_dns(self, create_params):
        """Enable the File DNS"""
        try:
            msg = 'Attempting to create a file DNS'
            LOG.info(msg)
            file_dns_details = {}
            if not self.module.check_mode:
                create_dict = dict()

                if create_params['add_ip_addresses'] is None:
                    create_dict['ip_addresses'] = []
                elif create_params['add_ip_addresses'] is not None and create_params['remove_ip_addresses'] is not None:
                    create_dict['ip_addresses'] = [ip for ip in create_params['add_ip_addresses'] if ip not in create_params['remove_ip_addresses']]
                elif create_params['add_ip_addresses'] is not None and create_params['remove_ip_addresses'] is None:
                    create_dict['ip_addresses'] = create_params['add_ip_addresses']

                create_keys = ['domain', 'transport']
                for key in create_keys:
                    if create_params[key] is not None:
                        create_dict[key] = create_params[key]
                if create_params['nas_server'] is not None:
                    create_dict['nas_server_id'] = create_params['nas_server']
                resp = self.file_dns.create_file_dns(
                    payload=create_dict)

                if resp:
                    file_dns_details = self.get_file_dns_details(
                        file_dns_id=resp['id'])

                msg = (f'Successfully created File DNS with details'
                       f' {file_dns_details}')
                LOG.info(msg)

            return file_dns_details

        except Exception as e:
            msg = (f'Creation of File DNS on PowerStore array failed with error {str(e)} ')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def delete_file_dns(self, file_dns_id):
        """ Disable the File DNS """

        try:
            msg = f'Deleting File DNS with identifier:' \
                  f' {file_dns_id}'
            LOG.info(msg)
            if not self.module.check_mode:
                self.file_dns.delete_file_dns(
                    file_dns_id=file_dns_id)
                return None
            return self.get_file_dns_details(
                file_dns_id=file_dns_id)

        except Exception as e:
            msg = (f'Deletion of the File DNS {file_dns_id}'
                   f' failed with error {str(e)}')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_file_dns_details(self, file_dns_id=None, nas_server_id=None):
        """ Get File DNS details """

        try:
            msg = (f'Getting File DNS details with '
                   f'file_dns_id {file_dns_id} '
                   f'nas_server_id {nas_server_id} ')
            LOG.info(msg)
            file_dns_details = None
            if file_dns_id is not None:
                file_dns_details = self.file_dns.get_file_dns_details(
                    file_dns_id=file_dns_id)
            elif nas_server_id is not None:
                file_dnss = self.file_dns.get_file_dns_by_nas_server_id(
                    nas_server_id=nas_server_id)
                if len(file_dnss) == 0:
                    return None
                else:
                    file_dns_details = file_dnss[0]

            msg = f'Successfully got File DNS details {file_dns_details}'
            LOG.info(msg)
            return file_dns_details

        except Exception as e:
            msg = (f'Getting File DNS details failed with error {str(e)} ')
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR \
                    and e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def is_modify_required(self, file_dns_details, file_dns_params):
        """To get the details of the fields to be modified."""

        msg = f'File DNS details: {file_dns_details}'
        LOG.info(msg)
        modify_dict = dict()

        modify_keys = ['domain', 'transport']

        if file_dns_params['add_ip_addresses'] is None and file_dns_params['remove_ip_addresses'] is not None:
            ip_addresses_list = [ip for ip in file_dns_details['ip_addresses'] if ip not in file_dns_params['remove_ip_addresses']]
            if set(ip_addresses_list) != set(file_dns_details['ip_addresses']):
                modify_dict['ip_addresses'] = ip_addresses_list

        elif file_dns_params['add_ip_addresses'] is not None and file_dns_params['remove_ip_addresses'] is not None:
            ip_addresses_list = list(set(file_dns_params['add_ip_addresses']) | set(file_dns_details['ip_addresses']))
            final_ip_addresses_list = [ip for ip in ip_addresses_list if ip not in file_dns_params['remove_ip_addresses']]
            if set(final_ip_addresses_list) != set(file_dns_details['ip_addresses']):
                modify_dict['ip_addresses'] = final_ip_addresses_list

        elif file_dns_params['add_ip_addresses'] is not None and file_dns_params['remove_ip_addresses'] is None:
            ip_addresses_list = list(set(file_dns_params['add_ip_addresses']) | set(file_dns_details['ip_addresses']))
            if set(ip_addresses_list) != set(file_dns_details['ip_addresses']):
                modify_dict['ip_addresses'] = ip_addresses_list

        for key in modify_keys:
            if file_dns_params[key] is not None and \
                    file_dns_params[key] != file_dns_details[key]:
                modify_dict[key] = file_dns_params[key]
        if file_dns_params['is_destination_override_enabled'] is not None:
            modify_dict['is_destination_override_enabled'] = file_dns_params['is_destination_override_enabled']

        if modify_dict:
            return modify_dict
        else:
            return None

    def modify_file_dns_details(self, file_dns_id,
                                modify_params):
        """Perform modify operations on a File DNS"""

        try:
            if not self.module.check_mode:
                self.file_dns.modify_file_dns(
                    file_dns_id=file_dns_id,
                    modify_parameters=modify_params)
            return self.get_file_dns_details(
                file_dns_id=file_dns_id)
        except Exception as e:
            msg = (f'Failed to modify the File DNS instance '
                   f'with error {str(e)}')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))


def get_powerstore_file_dns_parameters():
    """This method provides the parameters required for the ansible
    File DNS modules on PowerStore"""
    return dict(
        nas_server=dict(type='str'),
        file_dns_id=dict(type='str'),
        domain=dict(type='str'),
        add_ip_addresses=dict(type='list', elements='str'),
        remove_ip_addresses=dict(type='list', elements='str'),
        transport=dict(type='str', choices=['TCP', 'UDP']),
        is_destination_override_enabled=dict(type='bool'),
        state=dict(default='present', type='str', choices=['present', 'absent'])
    )


class FileDNSExitHandler():
    def handle(self, file_dns_obj, file_dns_details):
        file_dns_obj.result["file_dns_details"] = file_dns_details
        file_dns_obj.module.exit_json(**file_dns_obj.result)


class FileDNSDeleteHandler():
    def handle(self, file_dns_obj, file_dns_params, file_dns_details):
        if file_dns_params['state'] == 'absent' and file_dns_details:
            changed = file_dns_obj.delete_file_dns(file_dns_params['file_dns_id'])
            file_dns_obj.result['changed'] = True
            file_dns_details = {}

        FileDNSExitHandler().handle(file_dns_obj, file_dns_details)


class FileDNSModifyHandler():
    def handle(self, file_dns_obj, file_dns_params, file_dns_details):
        if file_dns_params['state'] == 'present' and file_dns_details:
            modify_dict = file_dns_obj.is_modify_required(file_dns_details, file_dns_params)
            if modify_dict:
                file_dns_details = file_dns_obj.modify_file_dns_details(file_dns_id=file_dns_details['id'],
                                                                        modify_params=modify_dict)
                file_dns_obj.result['changed'] = True

        FileDNSDeleteHandler().handle(file_dns_obj, file_dns_params, file_dns_details)


class FileDNSCreateHandler():
    def handle(self, file_dns_obj, file_dns_params, file_dns_details):
        if file_dns_params['state'] == 'present' and not file_dns_details:
            file_dns_details = file_dns_obj.create_file_dns(file_dns_params)
            file_dns_obj.result['changed'] = True

        FileDNSModifyHandler().handle(file_dns_obj, file_dns_params, file_dns_details)


class FileDNSHandler():
    def handle(self, file_dns_obj, file_dns_params):
        nas_id = None
        if file_dns_params['nas_server']:
            nas_id = file_dns_obj.get_nas_server(nas_server=file_dns_params['nas_server'])
        if nas_id:
            file_dns_params['nas_server'] = nas_id
        file_dns_details = file_dns_obj.get_file_dns_details(file_dns_id=file_dns_params['file_dns_id'],
                                                             nas_server_id=file_dns_params['nas_server'])
        FileDNSCreateHandler().handle(file_dns_obj, file_dns_params, file_dns_details)


def main():
    """ Create PowerStore File DNS object and perform action on it
        based on user input from playbook."""
    obj = PowerStoreFileDNS()
    FileDNSHandler().handle(obj, obj.module.params)


if __name__ == '__main__':
    main()
