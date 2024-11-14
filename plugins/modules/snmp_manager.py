#!/usr/bin/python
# Copyright: (c) 2024, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: snmp_manager
version_added: '3.6.0'
short_description: Manage SNMP Managers for PowerStore
description:
- Managing SNMP Managers on PowerStore Storage System includes creating
  SNMP Manager, modifying SNMP Manager and deleting SNMP Manager.

author:
- Meenakshi Dembi (@dembim) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerstore.powerstore

options:
  alert_severity:
    description:
    - Possible severities.
    choices: ['Info', 'Minor', 'Major', 'Critical']
    type: str
    default: 'Info'
  auth_privacy:
    description:
    - Supported SNMP privacy protocol.
    - C(Nil) - No encryption on the wire.
    - C(AES256) - means Encryption class for AES 256.
    - C(TDES) - Encryption class for Triple Data Encryption.
    type: str
    choices: ['Nil', 'AES256', 'TDES']
  auth_protocol:
    description:
    - Relevant only for SNMPv3. Supported SNMP authentication protocols.
    - C(Nil) - No authorization.
    - C(MD5) - The AuthMD5 class implements the MD5 authentication protocol.
    - C(SHA256) - The Secure Hash Authentication.
    choices: ['Nil', 'MD5', 'SHA256']
    type: str
  ip_address:
    description:
    - IP address or FQDN of the SNMP manager.
    - IPv4 and IPv6 are supported.
    type: str
    required: true
    aliases:
      - network_name
  new_ip_address:
    description:
    - IP address or FQDN of the SNMP manager to update.
    - IPv4 and IPv6 are supported.
    type: str
    aliases:
      - new_network_name
  snmp_password:
    description:
    - Passphrase, used for both Authentication and Privacy protocols.
    - I(snmp_password) is only applicable when I(version) is C(V3) and to set the security level to authentication only and authentication and privacy.
    type: str
    aliases:
      - auth_pass
  snmp_port:
    description:
    - Port number to use with the address of the SNMP manager.
    type: int
    default: 162
  snmp_username:
    description:
    -  User name for SNMP auth.
    - I(snmp_username) is required when I(version) is C(V3).
    type: str
  trap_community:
    description:
    - Trap Community string describes the security level.
    - I(trap_community) is required when I(version) is C(V2c).
    type: str
  update_password:
    description:
    - Update password applicable only to fir update case.
    choices: ['always', 'on_create']
    type: str
    default: 'always'
  version:
    description:
    - Supported SNMP protocol versions.
    - C(V2c) - SNMP version 2c.
    - C(V3) - SNMP version 3.
    choices: ['V3', 'V2c']
    type: str
    default: 'V3'
  state:
    description:
    - Define whether the file DNS should be enabled or not.
    - For Delete operation only, it should be set to C(absent).
    choices: ['absent', 'present']
    type: str
    default: 'present'

notes:
- The I(check_mode) is supported.
'''

EXAMPLES = r'''

- name: Create SNMP Manager with V2 SNMP protocol
  dellemc.powerstore.snmp_manager:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    network_name: 127.**.**.**
    snmp_port: 162
    version: "V2c"
    alert_severity: Critical
    trap_community: test
    state: present

- name: Create SNMP Manager with V3 SNMP protocol
  dellemc.powerstore.snmp_manager:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    network_name: 127.**.**.**
    snmp_port: 1024
    version: "V3"
    alert_severity: Critical
    trap_community: test
    snmp_username: test
    auth_protocol: MD5
    auth_privacy: TDES
    auth_pass: Password123!
    state: present

- name: Modify SNMP Manager
  dellemc.powerstore.snmp_manager:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    ip_address: 127.**.**.**
    new_ip_address: 192.**.**.**
    alert_severity: Info
    trap_community: test
    snmp_username: test
    auth_protocol: MD5
    auth_privacy: TDES
    auth_pass: Password123!
    state: present

- name: Delete SNMP Manager
  dellemc.powerstore.snmp_manager:
    array_ip: "{{ array_ip }}"
    validate_certs: "{{ validate_certs }}"
    user: "{{ user }}"
    password: "{{ password }}"
    ip_address: 127.**.**.**
    state: absent
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"

snmp_details:
    description: Details of the SNMP manager.
    returned: When SNMP exists.
    type: dict
    contains:
        id:
            description: Unique identifier of the SNMP manager.
            type: str
        ip_addresses:
            description: IPv4 address, IPv6 address, or FQDN of the SNMP manager.
            type: str
        port:
            description: Port number to use with the address of the SNMP manager.
            type: int
        version:
            description: Supported SNMP protocol versions.
            type: str
        trap_community:
            description: Trap Community string. Usually describes the security level.
            type: str
        alert_severity:
            description: Possible severities.
            type: str
        user_name:
            description: User name relevant only for SNMPv3.
            type: str
        auth_protocol:
            description: Relevant only for SNMPv3. Supported SNMP authentication protocols.
            type: str
        privacy_protocol:
            description: Relevant only for SNMPv3. Supported SNMP privacy protocols.
            type: str
    sample: {
        "id": "967ffb5d-5059-43a6-8377-1b83b99e6470",
        "ip_address": "127.0.0.1",
        "port": 162,
        "version": "V3",
        "trap_community": null,
        "alert_severity": "Info",
        "user_name": "admin",
        "auth_protocol": "MD5",
        "privacy_protocol": "AES256"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.libraries.powerstore_base \
    import PowerStoreBase


LOG = utils.get_logger('snmp_manager')


class PowerStoreSNMPManager(PowerStoreBase):
    """Class with SNMP Manager Operations"""

    def __init__(self):

        """Define all parameters for this module."""

        ansible_module_params = {
            'argument_spec': get_powerstore_snmp_manager_parameters(),
            'supports_check_mode': True
        }
        super().__init__(AnsibleModule, ansible_module_params)

        self.result = {
            "changed": False,
            "snmp_manager_details": {},
            "diff": {}
        }
        self.snmp_manager = self.conn.snmp_server

    def get_snmp_manager(self, snmp_manager_id):
        """Get the details of SNMP Manager of a given Powerstore storage
        system"""
        try:
            return self.snmp_manager.get_snmp_server_details(snmp_server_id=snmp_manager_id)
        except Exception as err:
            msg = (f'Got error while trying to get SNMP Manager details error: {str(err)} ')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(err))

    def getting_snmp_manager_id(self, ip_address):
        """Get the id of the SNMP manager"""
        try:
            all_snmp_managers = self.snmp_manager.get_snmp_server_list()
            for items in all_snmp_managers:
                if items['ip_address'] == ip_address:
                    return items['id']
        except Exception as err:
            msg = (f'Got error while trying to get SNMP Manager id error: {str(err)} ')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(err))

    def prepare_snmp_manager_create_payload(self, create_params):
        """Prepare payload for SNMP manager creation"""
        version = create_params['version']
        trap_community = create_params.get('trap_community')
        auth_protocol = create_params.get('auth_protocol')
        privacy_protocol = create_params.get('auth_privacy')
        payload = {
            'port': create_params['snmp_port'],
            'version': version,
            'trap_community': trap_community if version != 'V3' else None,
            'alert_severity': create_params['alert_severity'],
            'ip_address': create_params['ip_address'],
        }
        if version == 'V3':
            payload['user_name'] = create_params.get('snmp_username')
            if auth_protocol == "Nil" or auth_protocol is None:
                payload['auth_protocol'] = "None"
            else:
                payload['auth_protocol'] = auth_protocol

            if privacy_protocol == "Nil" or privacy_protocol is None:
                payload['privacy_protocol'] = "None"
            else:
                payload['privacy_protocol'] = privacy_protocol

        if auth_protocol != "None" and version == 'V3':
            payload['authpass'] = create_params.get('snmp_password')

        return payload

    def create_snmp_manager(self, create_params):
        """Create SNMP Manager"""
        try:
            changed = False
            self.validate_create(create_params)
            self.common_validations(create_params)
            snmp_manager_details = {}
            if not self.module.check_mode:
                create_dict = dict()
                create_dict = self.prepare_snmp_manager_create_payload(create_params)
                resp = self.snmp_manager.create_snmp_server(payload=create_dict)
                if resp:
                    snmp_manager_details = self.get_snmp_manager(resp['id'])
                    changed = True
                msg = (f'Successfully created SNMP Manager with details'
                       f' {snmp_manager_details}')
                LOG.info(msg)

            if self.module._diff:
                self.result.update({"diff": {"before": {}, "after": snmp_manager_details}})

            if self.module.check_mode:
                changed, snmp_manager_details = True, {}

            return changed, snmp_manager_details

        except Exception as e:
            msg = (f'Creation of SNMP Manager on PowerStore array failed with error {str(e)} ')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def delete_snmp_manager(self, snmp_manager_details):
        """ Delete SNMP Manager """
        try:
            msg = f'Deleting SNMP Manager:' \
                  f' {snmp_manager_details}'
            LOG.info(msg)
            changed = False

            if self.module.check_mode and snmp_manager_details:
                changed = True

            if self.module._diff:
                self.result.update({"diff": {"before": snmp_manager_details, "after": {}}})

            if not self.module.check_mode and snmp_manager_details:
                self.snmp_manager.delete_snmp_server(snmp_server_id=snmp_manager_details['id'])
                snmp_manager_details = {}
                changed = True

            return changed, snmp_manager_details
        except Exception as e:
            msg = (f'Deletion of the SNMP Manager {snmp_manager_details}'
                   f' failed with error {str(e)}')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def validate_version_change(self, snmp_manager_params, snmp_manager_details):
        if snmp_manager_params.get('version') != snmp_manager_details.get('version'):
            msg = (f"Version cannot be changed from {snmp_manager_details.get('version')} to {snmp_manager_params.get('version')}")
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def is_modify_required(self, snmp_manager_params, snmp_manager_details):
        param_dict = dict()

        self.validate_version_change(snmp_manager_params, snmp_manager_details)
        self.common_validations(snmp_manager_params)

        params_to_check = {
            'ip_address': 'new_ip_address',
            'port': 'snmp_port',
            'alert_severity': 'alert_severity'
        }
        for key, value in params_to_check.items():
            if snmp_manager_params.get(value) and snmp_manager_params.get(value) != snmp_manager_details.get(key):
                param_dict[key] = snmp_manager_params.get(value)

        if snmp_manager_details['version'] == 'V3':
            if snmp_manager_params.get('snmp_username') != snmp_manager_details.get('user_name'):
                param_dict['user_name'] = snmp_manager_params.get('snmp_username')

            auth_protocol = snmp_manager_params.get('auth_protocol')
            if auth_protocol is None or auth_protocol == "Nil":
                auth_protocol = "None"

            privacy_protocol = snmp_manager_params.get('auth_privacy')
            if privacy_protocol is None or privacy_protocol == "Nil":
                privacy_protocol = "None"

            if auth_protocol != snmp_manager_details['auth_protocol'] or privacy_protocol != snmp_manager_details['privacy_protocol']:
                param_dict['auth_protocol'] = auth_protocol
                param_dict['privacy_protocol'] = privacy_protocol

        if snmp_manager_details['version'] == 'V2c':
            trap_community = snmp_manager_params.get('trap_community')
            if trap_community and trap_community != snmp_manager_details.get('trap_community'):
                param_dict['trap_community'] = snmp_manager_params.get('trap_community')

        if snmp_manager_params.get('snmp_password') and snmp_manager_params.get('update_password') == "always":
            param_dict['authpass'] = snmp_manager_params.get('snmp_password')

        return param_dict

    def modify_snmp_manager_details(self, modify_dict, snmp_manager_details):
        """Modify SNMP Manager details"""
        try:
            changed = False
            existing_details = snmp_manager_details
            modified_details = snmp_manager_details.copy()
            modified_details.update(modify_dict)
            if not self.module.check_mode:
                if modify_dict:
                    self.snmp_manager.modify_snmp_server(snmp_server_id=snmp_manager_details["id"], modify_parameters=modify_dict)
                    snmp_manager_details = self.get_snmp_manager(snmp_manager_details["id"])
                    changed = True
                    msg = (f'Successfully modified SNMP Manager with details {snmp_manager_details}')
                    LOG.info(msg)

            if self.module.check_mode:
                changed = True

            if self.module._diff:
                self.result.update({"diff": {"before": existing_details, "after": modified_details}})

            return changed, snmp_manager_details
        except Exception as e:
            msg = (f'Updation of the SNMP Manager {snmp_manager_details["id"]}'
                   f' failed with error {str(e)}')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def validate_create(self, create_params):
        """Perform validation of create SNMP Manager parameters"""
        if not create_params['ip_address']:
            errormsg = "Provide valid value for ip_address/network_name."
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)
        if create_params['version'] == 'V2c' and not (create_params['trap_community'] and len(create_params['trap_community'].strip()) > 0):
            errormsg = "Trap community is required parameter for creating SNMP Manager with version V2c."
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)
        if create_params['version'] == 'V3' and not (create_params['snmp_username'] and len(create_params['snmp_username'].strip()) > 0):
            errormsg = "snmp_username is required parameter for creating SNMP Manager with version V3."
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)
        if (create_params['version'] == 'V3' and create_params['auth_protocol']) and \
                not (create_params['snmp_password'] and len(create_params['snmp_password'].strip()) > 0):
            errormsg = "snmp_password/auth_pass required parameter for creating or modifying SNMP Manager with version V3 and auth_protocol."
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def common_validations(self, create_params):
        if create_params['version'] == 'V3' and (create_params['auth_privacy'] and create_params['auth_privacy'] != "Nil") \
                and (not create_params['auth_protocol'] or create_params['auth_protocol'] == "Nil"):
            errormsg = "For V3 SNMP auth_protocol with None value must have privacy_protocol with None value."
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)
        if create_params['version'] == 'V3' and (not create_params['auth_protocol'] or create_params['auth_protocol'] == "Nil") \
                and (not create_params['auth_privacy'] or create_params['auth_privacy'] == "Nil") and create_params['snmp_password']:
            errormsg = "V3 with no authenticaton should not use snmp_password/authpass."
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)


def get_powerstore_snmp_manager_parameters():
    """This method provides the parameters required for the ansible
    SNMP modules on PowerStore"""
    return dict(
        alert_severity=dict(default='Info', type='str', choices=['Info', 'Minor', 'Major', 'Critical']),
        auth_privacy=dict(type='str', choices=['Nil', 'AES256', 'TDES']),
        auth_protocol=dict(type='str', choices=['Nil', 'MD5', 'SHA256']),
        ip_address=dict(type='str', aliases=['network_name'], required=True),
        new_ip_address=dict(type='str', aliases=['new_network_name']),
        snmp_port=dict(default=162, type='int'),
        snmp_password=dict(type='str', aliases=['auth_pass'], no_log=True),
        snmp_username=dict(type='str'),
        trap_community=dict(type='str'),
        update_password=dict(default='always', type='str', choices=['always', 'on_create']),
        version=dict(default='V3', type='str', choices=['V2c', 'V3']),
        state=dict(default='present', type='str', choices=['present', 'absent'])
    )


class SNMPManagerExitHandler():
    def handle(self, snmp_obj, snmp_manager_details):
        snmp_obj.result["snmp_manager_details"] = snmp_manager_details
        snmp_obj.module.exit_json(**snmp_obj.result)


class SNMPManagerDeleteHandler():
    def handle(self, snmp_obj, snmp_manager_params, snmp_manager_details):
        if snmp_manager_params['state'] == 'absent':
            changed, snmp_manager_details = snmp_obj.delete_snmp_manager(snmp_manager_details)
            snmp_obj.result['changed'] = changed

        SNMPManagerExitHandler().handle(snmp_obj, snmp_manager_details)


class SNMPManagerModifyHandler():
    def handle(self, snmp_obj, snmp_manager_params, snmp_manager_details):
        if snmp_manager_params['state'] == 'present' and snmp_manager_details:
            modify_dict = snmp_obj.is_modify_required(snmp_manager_params, snmp_manager_details)
            changed, snmp_manager_details = snmp_obj.modify_snmp_manager_details(modify_dict, snmp_manager_details)
            snmp_obj.result['changed'] = changed

        SNMPManagerDeleteHandler().handle(snmp_obj, snmp_manager_params, snmp_manager_details)


class SNMPManagerCreateHandler():
    def handle(self, snmp_obj, snmp_manager_params, snmp_manager_details):
        if snmp_manager_params['state'] == 'present' and not snmp_manager_details:
            changed, snmp_manager_details = snmp_obj.create_snmp_manager(create_params=snmp_manager_params)
            snmp_obj.result['changed'] = changed
            SNMPManagerExitHandler().handle(snmp_obj, snmp_manager_details)

        SNMPManagerModifyHandler().handle(snmp_obj, snmp_manager_params, snmp_manager_details)


class SNMPManagerHandler():
    def handle(self, snmp_obj, snmp_manager_params):
        snmp_manager_details = dict()
        snmp_manager_id = snmp_obj.getting_snmp_manager_id(snmp_manager_params['ip_address'])
        if snmp_manager_id:
            snmp_manager_details = snmp_obj.get_snmp_manager(snmp_manager_id)
        SNMPManagerCreateHandler().handle(snmp_obj, snmp_manager_params, snmp_manager_details)


def main():
    """ Create PowerStore SNMP object and perform action on it
        based on user input from playbook."""
    obj = PowerStoreSNMPManager()
    SNMPManagerHandler().handle(obj, obj.module.params)


if __name__ == '__main__':
    main()
