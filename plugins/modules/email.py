#!/usr/bin/python
# Copyright: (c) 2022, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: email
version_added: '1.5.0'
short_description: Destination Email operations on a PowerStore storage system
description:
- Performs all destination email operations on a PowerStore Storage System.
- This module supports get details of an existing destination email address.
  Create/Add new destination email address for all supported parameters.
- This Module supports modify destination email address with supported parameters.
- This Module supports delete/remove a specific destination email
  address. Send a test mail to a specific destination email address.
extends_documentation_fragment:
  - dellemc.powerstore.powerstore
author:
- Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>
options:
  email_id:
    description:
    - Unique identifier of the destination email address.
    - Mutually exclusive with I(email_address).
    type: str
  email_address:
    description:
    - Email address to receive notifications.
    - Mutually exclusive with I(email_id).
    type: str
  new_address:
    description:
    - New email address to receive notifications.
    type: str
  send_test_email:
    description:
    - Whether to send the test email to the destination email address.
    type: bool
    default: false
  notify:
    description:
    - Whether to send different types of notifications. It contains below
      optional candidate variables.
    type: dict
    suboptions:
      critical:
        description:
        - Whether to send notifications for critical alerts.
        type: bool
      major:
        description:
        - Whether to send notifications for major alerts.
        type: bool
      minor:
        description:
        - Whether to send notifications for minor alerts.
        type: bool
      info:
        description:
        - Whether to send notifications for informational alerts.
        type: bool
  state:
    description:
    - The state of the destination email address after the task is performed.
    - For Delete operation only, it should be set to C(absent).
    - For all Create, Modify, Test or Get details operations it should be set
      to C(present).
    required : true
    choices: [ 'present', 'absent']
    type: str

notes:
- Idempotency is not supported for Test operation of Email module.
- The I(check_mode) is not supported.
'''

EXAMPLES = r'''
  - name: Get details of destination email with email_id
    dellemc.powerstore.email:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       validate_certs: "{{validate_certs}}"
       email_id: "780b6220-2d0b-4b9f-a485-4ae7f673bd98"
       state: "present"

  - name: Get details of destination email with email_address
    dellemc.powerstore.email:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       validate_certs: "{{validate_certs}}"
       email_address: "abc@dell.com"
       state: "present"

  - name: Create destination email
    dellemc.powerstore.email:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       validate_certs: "{{validate_certs}}"
       email_address: "abc_xyz@dell.com"
       notify:
         info: true
         critical: true
         major: false
       state: "present"

  - name: Modify destination email
    dellemc.powerstore.email:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       validate_certs: "{{validate_certs}}"
       email_address: "abc_xyz@dell.com"
       new_address: "def_pqr@dell.com"
       notify:
         info: false
         major: false
       state: "present"

  - name: Send a test mail to the destination email with email_id
    dellemc.powerstore.email:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       validate_certs: "{{validate_certs}}"
       email_id: "780b6220-2d0b-4b9f-a485-4ae7f673bd98"
       send_test_email: true
       state: "present"

  - name: Delete destination email
    dellemc.powerstore.email:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       validate_certs: "{{validate_certs}}"
       email_address: "def_pqr@dell.com"
       state: "absent"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"
email_details:
    description: Details of the destination email address.
    returned: When destination email address exists
    type: complex
    contains:
        id:
            description: The system generated ID of the destination email instance.
            type: str
        email_address:
            description: Email address to receive notifications.
            type: str
        notify:
            description:
                - Whether to send different types of notifications.
            type: complex
            contains:
                critical:
                    description: Whether to send notifications for critical alerts.
                    type: bool
                info:
                    description: Whether to send notifications for informational alerts.
                    type: bool
                major:
                    description: Whether to send notifications for major alerts.
                    type: bool
                minor:
                    description: Whether to send notifications for minor alerts.
                    type: bool
    sample: {
        "email_address": "abc@dell.com",
        "id": "e49c9469-a055-4207-898e-0c4150737722",
        "notify": {
            "critical": true,
            "info": true,
            "major": true,
            "minor": true
        }
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import utils
import re

LOG = utils.get_logger('email')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/2.2.0'


class PowerstoreEmail(object):
    """Email operations"""
    cluster_name = None
    cluster_global_id = None

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_email_parameters())
        mut_ex_args = [['email_id', 'email_address']]
        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mut_ex_args
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

    def get_destination_email_details(self, email_address=None, email_id=None):
        """Get email details by address or id"""
        try:
            LOG.info('Getting the details of destination email addrress, '
                     'address:%s, ID:%s', email_address, email_id)
            if email_address:
                resp = \
                    self.configuration.\
                    get_destination_email_by_address(
                        email_address=email_address)
                if resp:
                    LOG.info('Successfully got the details of destination email '
                             'with address: %s', email_address)
                    LOG.info(resp)
                    return modify_result(email_details=resp[0])

            else:
                resp = self.configuration.get_destination_email_details(email_id=email_id)
                if resp:
                    LOG.info('Successfully got the details of destination email '
                             'with id: %s', email_id)
                    return modify_result(email_details=resp)

            msg = 'No destination email present with address {0} or ID {1}'.format(
                email_address, email_id)
            LOG.info(msg)
            return resp

        except Exception as e:
            msg = 'Get details of destination email address: {0} or ID {1}' \
                  'failed with' \
                  ' error : {2} '.format(email_address, email_id,
                                         str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def create_destination_email(self, email_address):
        """Create a destination email."""
        try:
            LOG.info("Attempting to create a destination email with address "
                     "%s", email_address)
            email_address = self.module.params['email_address']

            create_params = dict()
            create_params['email_address'] = email_address
            notification_levels = ['critical', 'major', 'minor', 'info']
            if self.module.params['notify'] is not None:
                for level in notification_levels:
                    if self.module.params['notify'][level] is not None:
                        create_params['notify_' + level] = self.module.params['notify'][level]
            resp = self.configuration.create_destination_email(
                create_params=create_params)

            if resp:
                email_details = self.get_destination_email_details(email_id=resp['id'])

            LOG.info("Successfully Created destination email with "
                     "details : %s", email_details)

            return email_details

        except Exception as e:
            msg = 'Create destination email with address {0} on PowerStore array ' \
                  'name : {1} , global id : {2} failed with ' \
                  'error {3} '.format(email_address, self.cluster_name,
                                      self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def delete_destination_email(self, email_id):
        """Delete a destination email"""
        try:
            LOG.info("Attempting to delete destination email id "
                     "%s", email_id)

            self.configuration.delete_destination_email(email_id=email_id)
            return True
        except Exception as e:
            msg = 'Failed to delete destination email id {0} with ' \
                  'error {1}'.format(email_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def test_destination_email(self, email_id):
        """Send a test mail to a destination email"""
        try:
            LOG.info('Attempting to send a test mail to a destination '
                     'email id %s', email_id)

            self.configuration.test_destination_email(email_id=email_id)
            return True
        except Exception as e:
            msg = 'Failed to send a test mail to a destination email' \
                  'id {0} with error {1}'.format(email_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def is_modify_required(self, email_details):
        """To get the details of the field to be modified."""

        try:
            LOG.info("Email details: %s", email_details)
            modify_dict = dict()
            notify_params = dict()
            keys_notify = ['critical', 'major', 'minor', 'info']

            for key in keys_notify:
                notify_params[key] = None

            new_address = self.module.params['new_address']
            if self.module.params['notify'] is not None:
                for key in self.module.params['notify']:
                    notify_params[key] = self.module.params['notify'][key]

            if new_address and new_address != email_details['email_address']:
                modify_dict['email_address'] = new_address

            if notify_params:
                for key in keys_notify:
                    if notify_params[key] is not None and\
                            email_details['notify'][key] != notify_params[key]:
                        modify_dict['notify_' + key] = notify_params[key]
            if modify_dict:
                return modify_dict
            return None

        except Exception as e:
            msg = 'Failed to determine if destination email instance need ' \
                  'to modified with error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def modify_destination_email(self, email_id, modify_params):
        """Perform modify operations on a destination email"""

        try:
            LOG.info('Attempting to modify destination email with id %s',
                     email_id)
            self.configuration.modify_destination_email_details(
                email_id=email_id, modify_parameters=modify_params)
            return True
        except Exception as e:
            msg = 'Failed to modify destination email instance ' \
                  'with error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def validate_input_params(self):
        """Validate the input parameters"""

        regex = r'\b[A-Za-z0-9._%+-]+@[a-z0-9.-]+\.[a-z0-9]{2,}\b'
        param_list = ['email_address', 'new_address']
        msg = "Please provide a valid {0}"

        if self.module.params['email_id'] is not None and \
                (len(self.module.params['email_id'].strip()) == 0 or
                 self.module.params['email_id'].count(" ") > 0):
            err_msg = msg.format('email_id')
            self.module.fail_json(msg=err_msg)
        for param in param_list:
            if self.module.params[param] is not None and \
                    not re.fullmatch(regex, self.module.params[param]):
                err_msg = msg.format(param)
                self.module.fail_json(msg=err_msg)

    def perform_module_operation(self):
        """Performing various module operations"""
        email_id = self.module.params['email_id']
        email_address = self.module.params['email_address']
        new_address = self.module.params['new_address']
        send_test_email = self.module.params['send_test_email']
        state = self.module.params['state']

        result = dict(
            email_details=None
        )
        changed = False

        modify_params = None

        # check for invalid value of email_id
        self.validate_input_params()

        email_details = self.get_destination_email_details(
            email_id=email_id, email_address=email_address)
        if email_details:
            modify_params = self.is_modify_required(email_details=email_details)
        if not email_details and state == 'present':
            if not email_address:
                msg = "email address is required to create a destination email"
                LOG.error(msg)
                self.module.fail_json(msg=msg)
            if new_address is not None:
                err_msg = "new_address is not allowed during creation."
                LOG.error(err_msg)
                self.module.fail_json(msg=err_msg)
            email_details = self.create_destination_email(email_address=email_address)
            changed = True

        if state == 'present' and email_details and modify_params:
            changed = self.modify_destination_email(
                email_id=email_details.get("id"),
                modify_params=modify_params)
            email_details = self.get_destination_email_details(email_id=email_details.get("id"))

        if state == 'absent' and email_details:
            changed = self.delete_destination_email(email_id=email_details.get("id"))
            email_details = None
        if state == 'present' and email_details and send_test_email is True:
            changed = self.test_destination_email(email_id=email_details.get("id"))
        result['email_details'] = email_details
        result['changed'] = changed
        self.module.exit_json(**result)


def modify_result(email_details):
    result_dict = dict()
    notify_dict = dict()
    notify_dict['critical'] = email_details['notify_critical']
    notify_dict['major'] = email_details['notify_major']
    notify_dict['minor'] = email_details['notify_minor']
    notify_dict['info'] = email_details['notify_info']
    result_dict['id'] = email_details['id']
    result_dict['email_address'] = email_details['email_address']
    result_dict['notify'] = notify_dict
    return result_dict


def get_powerstore_email_parameters():
    """This method provide the parameters required for the destination email
     operations for PowerStore"""

    return dict(
        email_id=dict(), email_address=dict(),
        new_address=dict(),
        notify=dict(
            type='dict', options=dict(
                critical=dict(type='bool', required=False),
                major=dict(type='bool', required=False),
                minor=dict(type='bool', required=False),
                info=dict(type='bool', required=False)
            ),
            required=False
        ),
        send_test_email=dict(type='bool', required=False, default=False),
        state=dict(required=True, type='str', choices=['present', 'absent'])
    )


def main():
    """ Create PowerStore email object and perform action on it
        based on user input from playbook """
    obj = PowerstoreEmail()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
