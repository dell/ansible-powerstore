#!/usr/bin/python
# Copyright: (c) 2023, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: vcenter
version_added: '1.9.0'
short_description: Manage vCenter on a PowerStore storage system
description:
- Managing vCenter on a PowerStore Storage System includes adding a vCenter,
  getting details, modifying, and removing a vCenter.
author:
- Bhavneet Sharma (@sharmb5) <ansible.team@dell.com>
extends_documentation_fragment:
  - dellemc.powerstore.powerstore
options:
  vcenter_id:
    description:
    - Unique identifier of the vCenter instance.
    type: str
  address:
    description:
    - IP address of vCenter, in IPv4, IPv6, hostname format.
    - Mandatory while adding a vCenter.
    - To modify the address, a new address of the same vCenter must be passed.
    type: str
  vcenter_username:
    description:
    - User name to login to vcenter.
    - Mandatory while adding a vCenter.
    - I(vcenter_password) needs to be provided to modify the user name.
    type: str
  vcenter_password:
    description:
    - Password to login to vcenter.
    - Mandatory while adding a vCenter.
    type: str
  vasa_provider_credentials:
    description:
    - Credentials required for registering VASA vendor provider.
    type: dict
    suboptions:
      username:
        description:
        - Username of the local user account which will be used by vSphere to
          register VASA provider.
        - Mandatory while registering VASA provider.
        type: str
        required: true
      password:
        description:
        - Password of the local user account which will be used by vSphere to
          register VASA provider.
        - Mandatory while registering VASA provider.
        type: str
        required: true
  delete_vasa_provider:
    description:
    - Whether to remove VASA provider.
    - When C(true), remove the VASA provider from vCenter. This will only
      happen if provider is not connected to any other PowerStore system.
    - C(false) is the API default.
    type: bool
  state:
    description:
    - The state of the vCenter instance after the task is performed.
    - For get, create, and modify operations it should be set to C(present).
    choices: [ 'present', 'absent']
    default: present
    type: str
  update_password:
    description:
    - This parameter controls the way the I(vcenter_password) is updated during
      addition and modification of the vCenter.
    - C(always) will update password for each execution.
    - C(on_create) will only set while adding a vCenter or modifying the
      I(vcenter_username.)
    - For modifying I(vcenter_password), set the I(update_password) to
      C(always).
    choices: ['always', 'on_create']
    default: always
    type: str

notes:
- In unified+ deployment, the one vCenter instance residing in the PowerStore
  cluster will be prepopulated and cannot be deleted, nor may any other vCenter
  be added.
- For unified deployment, one external vCenter may be configured if desired.
- The I(check_mode) is supported.
'''

EXAMPLES = r'''
- name: Get details of vCenter
  dellemc.powerstore.vcenter:
    array_ip: "{{array_ip}}"
    user: "{{user}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    vcenter_id: "24d333-59f-423c-205-c6181ea81b"

- name: Add a vcenter
  dellemc.powerstore.vcenter:
    array_ip: "{{array_ip}}"
    user: "{{user}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    address: "XX.XX.XX.XX"
    vcenter_username: "user-name"
    vcenter_password: "password"
    update_password: "on_create"
    vasa_provider_credentials:
      username: "admin"
      password: "pass"

- name: Modify a vCenter attribute
  dellemc.powerstore.vcenter:
    array_ip: "{{array_ip}}"
    user: "{{user}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    vcenter_id: "24d333-59f-423c-205-c6181ea81b"
    address: "XX.XX.XX.YY"
    vcenter_username: "user-name"
    vcenter_password: "password"
    update_password: "always"

- name: Remove a vcenter
  dellemc.powerstore.vcenter:
    array_ip: "{{array_ip}}"
    user: "{{user}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    vcenter_id: "24d333-59f-423c-205-c6181ea81b"
    delete_vasa_provider: true
    state: "absent"
'''

RETURN = r'''
changed:
  description: Shows whether or not the resource has changed.
  returned: always
  type: bool
  sample: "false"
vcenter_details:
  description: Details of the vCenter instance.
  returned: When vCenter exists.
  type: complex
  contains:
    id:
      description: Unique identifier of vCenter instance.
      type: str
    instance_uuid:
      description: UUID instance of vCenter.
      type: str
    address:
      description: IP address of vCenter hosts, in IPv4, IPv6 or hostname
                   format.
      type: str
    username:
      description: User name to login to vCenter.
      type: str
    version:
      description: Version of vCenter including its build number. Was added in
                   PowerStore version 3.0.0.0.
      type: str
    vendor_provider_status:
      description: General status of the VASA vendor provider in vCenter.
      type: list
    vendor_provider_status_l10n:
      description: Localized message string corresponding to
                   vendor_provider_status.
      type: str
    virtual_machines:
      description: Virtual machines associated with vCenter.
      type: list
    datastores:
      description: Data stores that exist on a specific vCenter. Was added
                   in PowerStore version 3.0.0.0.
      type: list
    vsphere_host:
      description: All the vSphere hosts that exist on a specific vCenter.
                   Was added in PowerStore version 3.0.0.0.
      type: list
  sample: {
    "id": "0d330d6c-3fe6-41c6-8023-5bd3fa7c61cd",
    "instance_uuid": "c4c14fbb-828b-40f3-99bb-5bd4db723516",
    "address": "10.x.x.x",
    "username": "administrator",
    "version": "7.0.3",
    "vendor_provider_status": "Online",
    "vendor_provider_status_l10n": "Online",
    "virtual_machines": [],
    "datastores": [],
    "vsphere_host": []
  }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.\
    dell import utils

LOG = utils.get_logger('vcenter')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/3.0.0'


class PowerstoreVCenter(object):
    """vCenter operations"""

    def __init__(self):
        """Define all the parameters required by this module"""

        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_vcenter_parameters())

        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True
        )

        LOG.info("HAS_PY4PS = %s , IMPORT_ERROR = %s", HAS_PY4PS, IMPORT_ERROR)
        # SDK version check
        if HAS_PY4PS is False:
            self.module.fail_json(msg=IMPORT_ERROR)

        LOG.info('IS_SUPPORTED_PY4PS_VERSION = %s, VERSION_ERROR'
                 ' = %s', IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR)
        if IS_SUPPORTED_PY4PS_VERSION is False:
            self.module.fail_json(msg=VERSION_ERROR)

        self.conn = utils.get_powerstore_connection(
            self.module.params,
            application_type=APPLICATION_TYPE)
        self.configuration = self.conn.config_mgmt

        LOG.info('Got Py4ps instance for configuration on PowerStore'
                 ' %s.', self.configuration)
        LOG.info('Check mode flag: %s.', self.module.check_mode)

    def is_vcenter_modify_required(self, vcenter_details):
        """ To check if modification is required or not"""
        address = self.module.params['address']
        username = self.module.params['vcenter_username']
        vasa_provider = self.module.params['vasa_provider_credentials']
        password = self.module.params['vcenter_password']
        update_password = self.module.params['update_password']

        modify_dict = dict()
        if address is not None and vcenter_details['address'] != address:
            modify_dict['address'] = address
        if username is not None and vcenter_details['username'] != username:
            modify_dict['username'] = username
            modify_dict['password'] = self.module.params['vcenter_password']
        if update_password == "always" and password is not None:
            modify_dict['password'] = self.module.params['vcenter_password']
        if vasa_provider is not None and \
                vcenter_details['vendor_provider_status'] != "Online":
            modify_dict['vasa_provider_credentials'] = vasa_provider
        return modify_dict

    def modify_vcenter(self, vcenter_id, modify_params):
        """Perform modify operations on a vCenter instance
        :param vcenter_id: ID of the vCenter
        :param modify_params: Dict containing params to modify for a vCenter
        """
        try:
            LOG.info('Modifying vCenter %s attributes.', vcenter_id)
            if not self.module.check_mode:
                self.configuration.modify_vcenter(
                    vcenter_id=vcenter_id, modify_param_dict=modify_params)
            return True
        except Exception as e:
            msg = f'Modification of vCenter {vcenter_id} failed with error {e}'
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def add_vcenter(self, address, username, password, vasa_provider):
        """Add a vCenter to Unified PowerStore system
        :param address: IP address of vCenter, in IPv4, IPv6 or host name
                        format
        :param username: Username to log in to vCenter
        :param password: Password to log in to vCenter
        :param vasa_provider: Dict contains credentials to register VASA
                              provider
        """
        LOG.info("Adding a vCenter.")
        if not all([address, username, password]):
            err_msg = 'address, vcenter_username and vcenter_password must' \
                      ' be passed to add a vCenter.'
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)
        try:
            add_dict = dict()
            add_dict['address'] = address
            add_dict['username'] = username
            add_dict['password'] = password
            if vasa_provider is not None:
                add_dict['vasa_provider_credentials'] = vasa_provider

            resp = dict()
            if not self.module.check_mode:
                resp = self.configuration.add_vcenter(add_params=add_dict)
            return resp, True

        except Exception as e:
            error_msg = f'Adding of vCenter failed with error {e}.'
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def delete_vcenter(self, vcenter_id, delete_vasa_provider):
        """Delete an vCenter instance from a unified PowerStore version
        :param vcenter_id: ID of a vCenter instance
        :param delete_vasa_provider: Whether to delete a VASA provider
        """
        try:
            LOG.info('Deleting vCenter %s', vcenter_id)
            if not self.module.check_mode:
                self.configuration.\
                    remove_vcenter(vcenter_id=vcenter_id,
                                   delete_vasa_provider=delete_vasa_provider)
            return True
        except Exception as e:
            err_msg = f'Deletion of vCenter {vcenter_id} failed with error {e}'
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg, **utils.failure_codes(e))

    def get_vcenter_details(self, vcenter_id):
        """Get vCenter details by id"""

        try:
            if vcenter_id:
                LOG.info('Getting the details of vCenter with ID: '
                         '%s', vcenter_id)
                resp = self.configuration.get_vcenter_details(
                    vcenter_id=vcenter_id)
                LOG.info('Successfully got the details of vCenter with id: '
                         '%s', vcenter_id)
                return resp
            if vcenter_id is None:
                vcenters = self.configuration.get_vcenters()
                if vcenters and vcenters[0]['address'] == \
                        self.module.params['address']:
                    LOG.info('Successfully got the details of '
                             'vCenter: %s', vcenters[0])
                    return vcenters[0]

        except Exception as e:
            msg = f'Get details of vCenter: {vcenter_id} failed with ' \
                  f'error : {e}'
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.error(msg)
                return None
            LOG.info(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def validate_input_params(self):
        """Validate the input parameters"""

        params = ['vcenter_id', 'address', 'vcenter_username',
                  'vcenter_password']

        for param in params:
            if utils.is_param_empty(self.module.params[param]):
                err_msg = f'Provide the valid {param}.'
                self.module.fail_json(msg=err_msg)

    def perform_module_operation(self):
        """Performing various module operations"""
        vcenter_id = self.module.params['vcenter_id']
        address = self.module.params['address']
        vcenter_username = self.module.params['vcenter_username']
        vcenter_password = self.module.params['vcenter_password']
        vasa_provider_credentials = self.module.params[
            'vasa_provider_credentials']
        delete_vasa_provider = self.module.params['delete_vasa_provider']
        state = self.module.params['state']

        result = dict(
            changed=False,
            vcenter_details=dict()
        )

        changed = False

        # Validate input parameters
        self.validate_input_params()

        vcenter_details = self.get_vcenter_details(vcenter_id=vcenter_id)
        LOG.info("vCenter details are %s", str(vcenter_details))
        if vcenter_details:
            vcenter_id = vcenter_details['id']
            result['vcenter_details'] = vcenter_details
            modify_params = self.\
                is_vcenter_modify_required(vcenter_details=vcenter_details)

        # create operation
        if state == 'present':
            if not vcenter_details:
                add_resp, changed = self.\
                    add_vcenter(address=address, username=vcenter_username,
                                password=vcenter_password,
                                vasa_provider=vasa_provider_credentials)
                if add_resp:
                    vcenter_id = add_resp['id']
            elif vcenter_details and modify_params:
                changed = self.modify_vcenter(vcenter_id, modify_params)

        elif state == 'absent' and vcenter_details:
            changed = self.delete_vcenter(vcenter_id, delete_vasa_provider)

        if changed:
            result['vcenter_details'] = self.\
                get_vcenter_details(vcenter_id=vcenter_id)
        result['changed'] = changed
        self.module.exit_json(**result)


def get_powerstore_vcenter_parameters():
    """This method provide the parameters required for the
      vCenter operations for PowerStore"""

    return dict(
        vcenter_id=dict(), address=dict(), vcenter_username=dict(),
        vcenter_password=dict(no_log=True),
        vasa_provider_credentials=dict(
            type='dict',
            options=dict(
                username=dict(type='str', required=True),
                password=dict(type='str', required=True, no_log=True))),
        delete_vasa_provider=dict(type='bool'),
        state=dict(type='str', choices=['present', 'absent'],
                   default='present'),
        update_password=dict(type='str', choices=['always', 'on_create'],
                             default='always')
    )


def main():
    """ Create PowerStore vCenter object and perform action on it
        based on user input from playbook """
    obj = PowerstoreVCenter()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
