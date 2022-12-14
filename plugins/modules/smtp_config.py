#!/usr/bin/python
# Copyright: (c) 2022, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: smtp_config
version_added: '1.5.0'
short_description: SMTP configuration operations on a PowerStore storage
                   system
description:
- Performs all SMTP configuration operations on a PowerStore Storage System.
- This module supports get details of an existing SMTP configuration. You can modify
  an existing SMTP configuration with supported parameters. You can also send a test mail
  through configured SMTP server.
author:
- Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>
extends_documentation_fragment:
  - dellemc.powerstore.powerstore
options:
  smtp_id:
    description:
    - Unique identifier of the SMTP configuration.
    required: True
    type: int
  smtp_address:
    description:
    - IP address of the SMTP server.
    required: False
    type: str
  smtp_port:
    description:
    - Port used for sending SMTP messages.
    required: False
    type: int
  source_email:
    description:
    - Source email address used for sending SMTP messages.
    required: False
    type: str
  destination_email:
    description:
    - Destination email address for the test.
    required: False
    type: str
  state:
    description:
    - The state of the SMTP configuration after the task is performed.
    - For Delete operation only, it should be set to "absent".
    - For all operations it should be set to "present".
    required : True
    choices: [ 'present', 'absent']
    type: str

notes:
- Idempotency is not supported for test operation for smtp_config module.
- Creation and deletion of SMTP configuration is not supported.
- The check_mode is not supported.
'''
EXAMPLES = r'''

  - name: Get details of SMTP configuration
    dellemc.powerstore.smtp_config:
      array_ip: "{{array_ip}}"
      user: "{{user}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      smtp_id: "0"
      state: "present"

  - name: Modify SMTP config details
    dellemc.powerstore.smtp_config:
      array_ip: "{{array_ip}}"
      user: "{{user}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      smtp_id: "0"
      smtp_address: "sample.smtp.com"
      source_email: "def@dell.com"
      state: "present"

  - name: Send a test mail through the SMTP server
    dellemc.powerstore.smtp_config:
      array_ip: "{{array_ip}}"
      user: "{{user}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      smtp_id: "0"
      destination_email: "abc@dell.com"
      state: "present"
'''

RETURN = r'''

changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"

smtp_config_details:
    description: Details of the SMTP configuration.
    returned: When SMTP configuration exists.
    type: complex
    contains:
        id:
            description: Unique identifier of SMTP configuration.
            type: int
        address:
            description: IP address of the SMTP server.
            type: str
        port:
            description: Port used for sending SMTP messages.
            type: int
        source_email:
            description: Source email address used for sending SMTP messages.
            type: str
    sample: {
        "address": "sample.com",
        "id": "0",
        "port": 25,
        "source_email": "sample_source@dell.com"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import utils
import re

LOG = utils.get_logger('smtp_config')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.8.0'


class PowerstoreSmtpConfig(object):
    """SMTP config operations"""
    cluster_name = None
    cluster_global_id = None

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_smtp_config_parameters())
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

    def get_smtp_config_details(self, smtp_id):
        """Get SMTP configuration details by id"""
        try:
            LOG.info('Getting the details of SMTP configuration, '
                     'ID:%s', smtp_id)

            resp = self.configuration.get_smtp_config_details(smtp_id)
            LOG.info('Successfully got the details of SMTP configuration '
                     'with id: %s', smtp_id)
            return resp

        except Exception as e:
            msg = 'Get details of SMTP configuration: {0}' \
                  'failed with' \
                  ' error : {1} '.format(smtp_id,
                                         str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def test_smtp_config(self, smtp_id):
        """Send a test mail through the SMTP server"""
        try:
            LOG.info('Attempting to send a test mail through SMTP '
                     'configuration id %s', smtp_id)

            test_params = dict()
            test_params['email_address'] = \
                self.module.params['destination_email']
            self.configuration.test_smtp_config(smtp_id=smtp_id,
                                                test_parameters=test_params)
            return True
        except Exception as e:
            msg = 'Failed to send a test mail through SMTP configuration ' \
                  'id {0} with error {1}'.format(smtp_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def modify_smtp_required(self, smtp_details):
        """ To check if modification is required or not"""
        modify_smtp_config_dict = {
            'address': self.module.params['smtp_address'],
            'port': self.module.params['smtp_port'],
            'source_email': self.module.params['source_email']
        }
        regex = r'\b[A-Za-z0-9._%+-]+@[a-z0-9.-]+\.[a-z0-9]{2,}\b'
        to_modify = False
        keys = ['address', 'port', 'source_email']
        source_address = self.module.params['source_email']
        if source_address and source_address != " " and not re.fullmatch(regex, source_address):
            err_msg = "Invalid source email address: {0}".format(source_address)
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

        for key in keys:
            if modify_smtp_config_dict[key] is not None and\
                    smtp_details[key] != modify_smtp_config_dict[key]:
                LOG.debug("Key %s in smtp_details=%s,"
                          "modify_smtp_config_dict=%s", key,
                          smtp_details[key], modify_smtp_config_dict[key])
                to_modify = True
        if to_modify is True:
            for key in keys:
                if modify_smtp_config_dict[key] is None:
                    modify_smtp_config_dict[key] = smtp_details[key]
            return modify_smtp_config_dict
        return None

    def modify_smtp_config_details(self, smtp_id, modify_params):
        """Perform modify operations on a SMTP configuration"""

        try:
            LOG.info('Attempting to modify SMTP configuration with id %s',
                     smtp_id)
            self.configuration.modify_smtp_config_details(
                smtp_id=smtp_id, modify_parameters=modify_params)
            return True
        except Exception as e:
            msg = 'Failed to modify SMTP configuration instance ' \
                  'with error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def perform_module_operation(self):
        """Performing various module operations"""
        smtp_id = self.module.params['smtp_id']
        destination_email = self.module.params['destination_email']
        state = self.module.params['state']

        result = dict(
            smtp_config_details=None
        )
        changed = False
        modify_params = None

        smtp_details = self.get_smtp_config_details(smtp_id=smtp_id)
        LOG.info(smtp_details)
        if smtp_details:
            modify_params = self.modify_smtp_required(smtp_details=smtp_details)

        if not smtp_details and state == 'present':
            msg = "SMTP configuration with ID: {0} does not exist".format(smtp_id)
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        elif state == 'absent' and smtp_details:
            msg = " Deletion of SMTP configuration is not supported"
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        elif state == 'present' and smtp_details and modify_params:
            changed = self.modify_smtp_config_details(
                smtp_id=smtp_id,
                modify_params=modify_params)
            smtp_details = self.get_smtp_config_details(smtp_id=smtp_id)

        elif state == 'present' and smtp_details and destination_email:
            changed = self.test_smtp_config(smtp_id=smtp_id)

        result['smtp_config_details'] = smtp_details
        result['changed'] = changed
        self.module.exit_json(**result)


def get_powerstore_smtp_config_parameters():
    """This method provide the parameters required for the
      smtp_config operations for PowerStore"""

    return dict(
        smtp_id=dict(required=True, type='int'), smtp_address=dict(required=False, type='str'),
        smtp_port=dict(required=False, type='int'),
        source_email=dict(required=False, type='str'),
        destination_email=dict(required=False, type='str'),
        state=dict(required=True, type='str', choices=['present', 'absent'])
    )


def main():
    """ Create PowerStore smtp_config object and perform action on it
        based on user input from playbook """
    obj = PowerstoreSmtpConfig()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
