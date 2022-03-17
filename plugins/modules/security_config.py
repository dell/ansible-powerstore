#!/usr/bin/python
# Copyright: (c) 2021, Dell EMC
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

""" Ansible module for managing security configs on PowerStore"""
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: security_config
version_added: '1.4.0'
short_description: Security configuration operations on PowerStore Storage
                   System
description:
- Managing security configuration on PowerStore storage system includes getting
  details and modifying security configuration parameters.

extends_documentation_fragment:
  - dellemc.powerstore.dellemc_powerstore.powerstore

author:
- Bhavneet Sharma (@sharmb5) <ansible.team@dell.com>

options:
  security_config_id:
    description:
    - ID of the security configuration.
    - Mandatory for all operations.
    type: int
    required: True
  protocol_mode:
    description:
    - Protocol mode of the security configuration.
    - Mandatory only for modify operation.
    type: str
    choices: ['TLSv1_0', 'TLSv1_1', 'TLSv1_2']
  state:
    description:
    - Define whether the security config should exist or not.
    choices: ['absent', 'present']
    required: True
    type: str
notes:
- Creation and deletion of security configs is not supported by Ansible
  modules.
- Modification of protocol mode is only supported for PowerStore v2.0.0.0 and
  above.
- The check_mode is not supported.
'''

EXAMPLES = r'''
- name: Get security config
  dellemc.powerstore.security_config:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    security_config_id: 1
    state: "present"

- name: Modify attribute of security config
  dellemc.powerstore.security_config:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    security_config_id: 1
    protocol_mode: "TLSv1_1"
    state: "present"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "true"
security_config_details:
    description: Details of the security configuration.
    returned: When security config exists
    type: complex
    contains:
        id:
            description: The system generated ID given to the security
                         configuration.
            type: str
        idle_timeout:
            description: Idle time (in seconds) after which login sessions
                         will expire and require re-authentication.
            type: int
        protocol_mode:
            description: The protocol mode of the security configuration.
            type: str
    sample: {
        "id": "1",
        "idle_timeout": 3600,
        "protocol_mode": "TLSv1_2",
        "protocol_mode_l10n": "TLSv1_2"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import dellemc_ansible_powerstore_utils as utils

LOG = utils.get_logger('security_config')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.5.0'


class PowerStoreSecurityConfig(object):
    """Security Config operations"""

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_security_config_parameters())

        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False
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

    def get_security_config_details(self, security_config_id):
        """ Get the details of a security config on a PowerStore storage
            system"""
        try:
            LOG.info("Getting the details of the security config, ID:%s",
                     security_config_id)
            if security_config_id:
                resp = self.configuration.get_security_config_details(
                    security_config_id=security_config_id)
                return resp

        except Exception as e:
            msg = "Failed to get the security config using ID {0} with " \
                  "error {1} ".format(security_config_id, str(e))

            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def modify_security_config(self, security_config_id, protocol_mode):
        """Perform modify operations for security config."""

        try:
            LOG.info("Modifying security config properties.")
            self.configuration.modify_security_config(
                security_config_id=security_config_id,
                protocol_mode=protocol_mode)
            return True
        except Exception as e:
            msg = 'Failed to modify security config instance with error ' \
                  '{0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def perform_module_operation(self):
        """ Perform different security configuration operations based on
            the parameters chosen in the playbook."""

        security_config_id = self.module.params['security_config_id']
        protocol_mode = self.module.params['protocol_mode']
        state = self.module.params['state']

        # result is a dictionary to contain end state and security config
        # details
        result = dict(
            changed=False,
            security_config_details=None
        )

        # Get security config details
        security_config_details = self.get_security_config_details(
            security_config_id)

        # create check if object not found.
        if state == 'present' and not security_config_details:
            error_message = 'Security config not found - Creation of ' \
                            'security config is not allowed through ' \
                            'Ansible module.'
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

        # Delete check
        if state == 'absent' and security_config_details:
            error_message = 'Deletion of security config is not allowed ' \
                            'through Ansible module.'
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

        # Check if modification is required for security config
        modify_flag = False
        if state == 'present' and security_config_details:
            modify_flag = check_security_config_modified(
                security_config_details, protocol_mode)

        # modify security config
        if state == 'present' and security_config_details and \
                modify_flag:
            result['changed'] = self.modify_security_config(
                security_config_id, protocol_mode)

        # Finally update the module result
        if state == 'present':
            result['security_config_details'] = self. \
                get_security_config_details(security_config_id)
        self.module.exit_json(**result)


def check_security_config_modified(security_config_details,
                                   protocol_mode=None):
    """ Check if modification required for security config."""

    LOG.info("Checking if modification required for security config.")

    if protocol_mode is not None and \
            security_config_details['protocol_mode'] != protocol_mode:
        LOG.info("new protocol_mode is: %s and current protocol_mode"
                 " is: %s", protocol_mode,
                 security_config_details['protocol_mode'])
        return True

    return False


def get_powerstore_security_config_parameters():
    """This method provides the parameters required for the security
       configurations on PowerStore"""
    return dict(
        security_config_id=dict(required=True, type='int'),
        protocol_mode=dict(required=False, type='str',
                           choices=['TLSv1_0', 'TLSv1_1', 'TLSv1_2']),
        state=dict(required=True, type='str', choices=['present', 'absent'])
    )


def main():
    """ Create PowerStore security config object and perform action on it
        based on user input from playbook """
    obj = PowerStoreSecurityConfig()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
