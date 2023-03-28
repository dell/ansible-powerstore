#!/usr/bin/python
# Copyright: (c) 2022, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: remote_support_contact
version_added: '1.5.0'
short_description: Remote Support Contact operations on a PowerStore storage
                   system
description:
- Performs all Remote Support Contact operations on a PowerStore Storage
  system. This module supports get details and you can modify a Remote Support Contact
  with supported parameters.
author:
- Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>
extends_documentation_fragment:
  - dellemc.powerstore.powerstore
options:
  contact_id:
    description:
    - Unique identifier of the remote support contact.
    required: True
    type: int
  first_name:
    description:
    - The first name of the support contact for this system.
    required: False
    type: str
  last_name:
    description:
    - The last name of the support contact for this system.
    required: False
    type: str
  phone:
    description:
    - The phone number of this support contact for this system.
    required: False
    type: str
  email:
    description:
    - The email address of the support contact for this system.
    required: False
    type: str
  state:
    description:
    - The state of the remote support contact after the task is performed.
    - For Delete operation only, it should be set to "absent".
    - For get/modify operation it should be set to "present".
    required : True
    choices: [ 'present', 'absent']
    type: str

notes:
- Creation and deletion of remote support contact is not supported.
- Parameters first_name, last_name, email and phone can be removed by passing
  empty string.
- The check_mode is not supported.
'''
EXAMPLES = r'''

  - name: Get details of remote support contact
    dellemc.powerstore.remote_support_contact:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       contact_id: 0
       state: "present"

  - name: Modify remote support contact
    dellemc.powerstore.remote_support_contact:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       contact_id: 0
       first_name: "abc"
       last_name: "xyz"
       phone: "111-222-333-444"
       email: "abc_xyz@dell.com"
       state: "present"
'''

RETURN = r'''

changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"

remote_support_contact_details:
    description: Details of the remote support contact.
    returned: When remote support contact exists.
    type: complex
    contains:
        id:
            description: Unique identifier of remote support contact.
            type: int
        first_name:
            description: The first name of the support contact for this
                         system.
            type: str
        last_name:
            description: The last name of the support contact for this system.
            type: str
        phone:
            description: The phone number of this support contact for this
                         system.
            type: str
        email:
            description: The email address of the support contact for this
                         system.
            type: str
    sample: {
        "email": "",
        "first_name": "sample",
        "id": "0",
        "last_name": "contact",
        "phone": "0123213423"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import utils
import re
LOG = utils.get_logger('remote_support_contact')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.9.0'


class PowerstoreRemoteSupportContact(object):
    """remote support contact operations"""

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_remote_support_contact_parameters())
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

    def get_remote_support_contact_details(self, contact_id):
        """Get remote support contact details by id"""
        try:
            LOG.info('Getting the details of remote support contact, '
                     'ID:%s', contact_id)

            resp = self.configuration.get_remote_support_contact_details(contact_id)
            LOG.info('Successfully got the details of remote support contact '
                     'with id: %s', contact_id)
            return resp

        except Exception as e:
            msg = 'Get details of remote support contact: {0}' \
                  'failed with' \
                  ' error : {1} '.format(contact_id,
                                         str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def modify_remote_support_contact_required(self, contact_details):
        """ To check if modification is required or not"""
        modify_contact_dict = {
            'first_name': self.module.params['first_name'],
            'last_name': self.module.params['last_name'],
            'phone': self.module.params['phone'],
            'email': self.module.params['email']
        }

        to_modify = False
        keys = ['first_name', 'last_name', 'phone', 'email']

        for key in keys:
            if modify_contact_dict[key] is not None and\
                    contact_details[key] != modify_contact_dict[key]:
                modify_contact_dict[key] = self.module.params[key]
                to_modify = True
        if to_modify is True:
            return modify_contact_dict
        return None

    def modify_remote_support_contact_details(self, contact_id, modify_params):
        """Perform modify operations on a remote support contact"""

        try:
            LOG.info('Attempting to modify remote support contact with id %s',
                     contact_id)
            self.configuration.modify_remote_support_contact_details(
                remote_support_contact_id=contact_id, modify_parameters=modify_params)
            return True
        except Exception as e:
            msg = 'Failed to modify remote support contact instance ' \
                  'with error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def validate_input_params(self):
        """Validate the input parameters"""

        regex1 = r'\b[A-Za-z0-9._%+-]+@[a-z0-9.-]+\.[a-z0-9]{2,}\b'
        regex2 = r'[\d+-]+$'
        msg = "Please provide a valid {0}"
        email = self.module.params['email']
        if self.module.params['phone'] is not None and\
                self.module.params['phone'] != "" and \
                not re.match(regex2, self.module.params['phone']):
            err_msg = msg.format('phone')
            self.module.fail_json(msg=err_msg)
        if email and email != "" and not re.fullmatch(regex1, email):
            err_msg = "Invalid email address: {0}".format(email)
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

    def perform_module_operation(self):
        """Performing various module operations"""
        contact_id = self.module.params['contact_id']
        state = self.module.params['state']

        result = dict(
            remote_support_contact_details=None
        )
        changed = False
        modify_params = None

        # check for invalid value of parameters
        self.validate_input_params()

        if contact_id is None:
            msg = "Please provide valid contact_id"
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        contact_details = self.get_remote_support_contact_details(contact_id=contact_id)
        LOG.info(contact_details)
        if contact_details:
            modify_params = self.modify_remote_support_contact_required(contact_details=contact_details)

        if not contact_details and state == 'present':
            msg = "Remote Support Contact by ID: {0} does not exist." \
                  " Addition of Remote Support Contact is not supported "\
                  "through Ansible module.".format(contact_id)
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        elif state == 'absent' and contact_details:
            msg = " Deletion of Remote Support Contact is not supported "\
                  "through Ansible module."
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        elif state == 'present' and contact_details and modify_params:
            changed = self.modify_remote_support_contact_details(
                contact_id=contact_id,
                modify_params=modify_params)
            contact_details = self.get_remote_support_contact_details(contact_id=contact_id)

        result['remote_support_contact_details'] = contact_details
        result['changed'] = changed
        self.module.exit_json(**result)


def get_powerstore_remote_support_contact_parameters():
    """This method provide the parameters required for the
      remote support contact operations for PowerStore"""

    return dict(
        contact_id=dict(required=True, type='int'),
        first_name=dict(required=False, type='str'),
        last_name=dict(required=False, type='str'),
        email=dict(required=False, type='str'),
        phone=dict(required=False, type='str'),
        state=dict(required=True, type='str', choices=['present', 'absent'])
    )


def main():
    """ Create PowerStore remote support contact object and
        perform action on it based on user input from playbook """
    obj = PowerstoreRemoteSupportContact()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
