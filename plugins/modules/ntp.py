#!/usr/bin/python
# Copyright: (c) 2022, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: ntp
version_added: '1.5.0'
short_description: NTP operations on a PowerStore storage system
description:
- Performs all NTP operations on a PowerStore Storage System.
  This module supports get details of an existing NTP instance. You can modify
  existing NTP instance with supported parameters.
author:
- Bhavneet Sharma (@sharmb5) <ansible.team@dell.com>
extends_documentation_fragment:
  - dellemc.powerstore.powerstore
options:
  ntp_id:
    description:
    - Unique identifier of the NTP instance.
    required: True
    type: str
  ntp_addresses:
    description:
    - NTP server addresses, may contain host names or IPv4 addresses.
    required: False
    type: list
    elements: str
  ntp_address_state:
    description:
    - State of the addresses mentioned in ntp_addresses.
    required: False
    choices: ['present-in-ntp', 'absent-in-ntp']
    type: str
  state:
    description:
    - The state of the NTP instance after the task is performed.
    - For get and modify operations it should be set to "present".
    required : True
    choices: [ 'present', 'absent']
    type: str

notes:
- Minimum 1 and maximum 3 addresses can be associated to a NTP instance.
- Parameters ntp_addresses and ntp_address_state are required together.
- Creation and deletion of NTP is not supported.
- The check_mode is not supported.
'''

EXAMPLES = r'''
  - name: Get details of NTP instance
    dellemc.powerstore.ntp:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       ntp_id: "NTP1"
       state: "present"

  - name: Add addresses to NTP instance
    dellemc.powerstore.ntp:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       ntp_id: "NTP1"
       ntp_addresses:
        - "XX.XX.XX.XX"
        - "YY.YY.YY.YY"
       ntp_address_state: "present-in-ntp"
       state: "present"

  - name: Remove addresses from NTP instance
    dellemc.powerstore.ntp:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       ntp_id: "NTP1"
       ntp_addresses:
        - "YY.YY.YY.YY"
       ntp_address_state: "absent-in-ntp"
       state: "present"
'''

RETURN = r'''
changed:
  description: Shows whether or not the resource has changed.
  returned: always
  type: bool
  sample: "false"
ntp_details:
  description: Details of the NTP instance.
  returned: When NTP exists.
  type: complex
  contains:
    id:
      description: Unique identifier of NTP instance.
      type: str
    addresses:
      description: NTP server addresses, may contain host names or IPv4
                   addresses.
      type: str
  sample: {
    "addresses": [
      "1.2.3.4",
      "5.6.7.8"
    ],
    "id": "NTP1"
  }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.\
    dell import utils

LOG = utils.get_logger('ntp')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.6.0'


class PowerstoreNtp(object):
    """NTP operations"""

    def __init__(self):
        """Define all the parameters required by this module"""

        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_ntp_parameters())

        required_together = [['ntp_addresses', 'ntp_address_state']]
        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            required_together=required_together
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

    def validate_input_params(self):
        """Validate the input parameters"""

        msg = "Please provide the valid {0}"
        if self.module.params['ntp_id'] is not None and \
                (len(self.module.params['ntp_id'].strip()) == 0 or
                 self.module.params['ntp_id'].count(" ") > 0):
            err_msg = msg.format('ntp_id')
            self.module.fail_json(msg=err_msg)

    def get_ntp_details(self, ntp_id):
        """Get NTP details by id"""

        try:
            LOG.info('Getting the details of NTP with ID: %s', ntp_id)

            resp = self.configuration.get_ntp_details(ntp_id)
            LOG.info('Successfully got the details of NTP with id: %s',
                     ntp_id)
            return resp

        except Exception as e:
            msg = 'Get details of NTP: {0} failed with error : ' \
                  '{1}'.format(ntp_id, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.error(msg)
                return None
            LOG.info(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def modify_ntp_required(self, ntp_details):
        """ To check if modification is required or not"""

        ntp_address_list = self.module.params['ntp_addresses']
        ntp_address_state = self.module.params['ntp_address_state']
        modify_list = []
        if ntp_address_state == "present-in-ntp":
            modify_list = \
                set(ntp_address_list).union(ntp_details['addresses'])
        elif ntp_address_state == "absent-in-ntp":
            modify_list = \
                set(ntp_details['addresses']) - \
                set(ntp_address_list).intersection(ntp_details['addresses'])
        if ntp_address_list and set(modify_list) != \
                set(ntp_details['addresses']):
            modify_dict = {'addresses': list(modify_list)}
            return modify_dict
        return None

    def modify_ntp_details(self, ntp_id, modify_params):
        """Perform modify operations on a NTP instance"""

        try:
            msg = "Attempting to modify NTP instance with id {0} to {1}". \
                format(ntp_id, str(modify_params))
            LOG.info(msg)
            self.configuration.modify_ntp_details(
                ntp_id=ntp_id, modify_parameters=modify_params)
            return True
        except Exception as e:
            msg = 'Failed to modify NTP instance with error' \
                  ' {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def perform_module_operation(self):
        """Performing various module operations"""
        ntp_id = self.module.params['ntp_id']
        state = self.module.params['state']

        result = dict(
            changed=False,
            ntp_details=None
        )
        changed = False
        modify_params = None

        # check for invalid value of ntp_id
        self.validate_input_params()

        ntp_details = self.get_ntp_details(ntp_id=ntp_id)
        LOG.info(ntp_details)
        if ntp_details:
            modify_params = self.modify_ntp_required(ntp_details=ntp_details)

        if not ntp_details and state == 'present':
            msg = "NTP ID: {0} not found. Creation of NTP is " \
                  "not allowed through Ansible module.".format(ntp_id)
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        elif state == 'present' and ntp_details and modify_params:
            changed = self.modify_ntp_details(ntp_id=ntp_id,
                                              modify_params=modify_params)
            ntp_details = self.get_ntp_details(ntp_id=ntp_id)

        elif state == 'absent' and ntp_details:
            msg = "Deletion of NTP is not supported through Ansible module."
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        result['ntp_details'] = ntp_details
        result['changed'] = changed
        self.module.exit_json(**result)


def get_powerstore_ntp_parameters():
    """This method provide the parameters required for the
      NTP operations for PowerStore"""

    return dict(
        ntp_id=dict(required=True, type='str'),
        ntp_addresses=dict(required=False, type='list', elements='str'),
        ntp_address_state=dict(required=False, type='str',
                               choices=['present-in-ntp', 'absent-in-ntp']),
        state=dict(required=True, type='str', choices=['present', 'absent'])
    )


def main():
    """ Create PowerStore NTP object and perform action on it
        based on user input from playbook """
    obj = PowerstoreNtp()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
