#!/usr/bin/python
# Copyright: (c) 2022, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dns
version_added: '1.5.0'
short_description: DNS operations on a PowerStore storage system
description:
- Performs all DNS operations on a PowerStore Storage System.
  This module supports get details of an existing DNS instance. You can modify existing
  DNS instance with supported parameters.
author:
- Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>
extends_documentation_fragment:
  - dellemc.powerstore.powerstore
options:
  dns_id:
    description:
    - Unique identifier of the DNS instance.
    required: True
    type: str
  dns_addresses:
    description:
    - DNS server addresses in IPv4 format.
    required: False
    type: list
    elements: str
  dns_address_state:
    description:
    - State of the addresses mentioned in dns_addresses.
    required: False
    choices: ['present-in-dns', 'absent-in-dns']
    type: str
  state:
    description:
    - The state of the DNS instance after the task is performed.
    - For get and modify operations it should be set to "present".
    required : True
    choices: [ 'present', 'absent']
    type: str

notes:
- Minimum 1 and maximum 3 addresses can be associated to a DNS instance.
- Parameters dns_addresses and dns_address_state are required together.
- Creation and deletion of DNS is not supported.
- The check_mode is not supported.
'''

EXAMPLES = r'''
  - name: Get details of DNS instance
    dellemc.powerstore.dns:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       dns_id: "DNS1"
       state: "present"

  - name: Add addresses to DNS instance
    dellemc.powerstore.dns:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       dns_id: "DNS1"
       dns_addresses:
        - "XX.XX.XX.XX"
        - "YY.YY.YY.YY"
       dns_address_state: "present-in-dns"
       state: "present"

  - name: Remove addresses from DNS instance
    dellemc.powerstore.dns:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       dns_id: "DNS1"
       dns_addresses:
        - "YY.YY.YY.YY"
       dns_address_state: "absent-in-dns"
       state: "present"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"
dns_details:
    description: Details of the DNS instance.
    returned: When DNS exists.
    type: complex
    contains:
        id:
            description: Unique identifier of DNS instance.
            type: str
        addresses:
            description: DNS server addresses in IPv4 format.
            type: str
    sample: {
        "addresses": [
            "1.2.3.4",
            "5.6.7.8"
        ],
        "id": "DNS1"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import utils

LOG = utils.get_logger('dns')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.6.0'


class PowerstoreDns(object):
    """DNS operations"""
    cluster_name = None
    cluster_global_id = None

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_dns_parameters())

        required_together = [['dns_addresses', 'dns_address_state']]
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

    def get_dns_details(self, dns_id):
        """Get DNS details by id"""
        try:
            LOG.info('Getting the details of DNS, '
                     'ID:%s', dns_id)

            resp = self.configuration.get_dns_details(dns_id)
            LOG.info('Successfully got the details of DNS'
                     'with id: %s', dns_id)
            return resp

        except Exception as e:
            msg = 'Get details of DNS: {0}' \
                  'failed with' \
                  ' error : {1} '.format(dns_id,
                                         str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.error(msg)
                return None
            LOG.info(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def modify_dns_required(self, dns_details):
        """ To check if modification is required or not"""
        dns_address_list = self.module.params['dns_addresses']
        dns_address_state = self.module.params['dns_address_state']
        modify_list = []
        if dns_address_state == "present-in-dns":
            modify_list = set(dns_address_list).union(dns_details['addresses'])
        elif dns_address_state == "absent-in-dns":
            modify_list = set(dns_details['addresses']) - \
                set(dns_address_list).intersection(dns_details['addresses'])
        if dns_address_list and set(modify_list) != set(dns_details['addresses']):

            modify_dict = {'addresses': list(modify_list)}
            return modify_dict
        return None

    def modify_dns_details(self, dns_id, modify_params):
        """Perform modify operations on a DNS instance"""

        try:
            LOG.info('Attempting to modify DNS instance with id %s',
                     dns_id)
            self.configuration.modify_dns_details(
                dns_id=dns_id, modify_parameters=modify_params)
            return True
        except Exception as e:
            msg = 'Failed to modify DNS instance ' \
                  'with error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def validate_input_params(self):
        """Validate the input parameters"""

        msg = "Please provide a valid {0}"
        if self.module.params['dns_id'] is not None and \
                (len(self.module.params['dns_id'].strip()) == 0 or
                 self.module.params['dns_id'].count(" ") > 0):
            err_msg = msg.format('dns_id')
            self.module.fail_json(msg=err_msg)

    def perform_module_operation(self):
        """Performing various module operations"""
        dns_id = self.module.params['dns_id']
        state = self.module.params['state']

        result = dict(
            dns_details=None
        )
        changed = False
        modify_params = None

        # check for invalid value of dns_id
        self.validate_input_params()

        dns_details = self.get_dns_details(dns_id=dns_id)
        LOG.info(dns_details)
        if dns_details:
            modify_params = self.modify_dns_required(dns_details=dns_details)

        if not dns_details and state == 'present':
            msg = "DNS by ID: {0} does not exist. Creation of DNS is "\
                  "not supported through Ansible module.".format(dns_id)
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        elif state == 'present' and dns_details and modify_params:
            changed = self.modify_dns_details(
                dns_id=dns_id,
                modify_params=modify_params)
            dns_details = self.get_dns_details(dns_id=dns_id)

        elif state == 'absent' and dns_details:
            msg = "Deletion of DNS is not supported through Ansible module."
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        result['dns_details'] = dns_details
        result['changed'] = changed
        self.module.exit_json(**result)


def get_powerstore_dns_parameters():
    """This method provide the parameters required for the
      dns operations for PowerStore"""

    return dict(
        dns_id=dict(required=True, type='str'),
        dns_addresses=dict(required=False, type='list', elements='str'),
        dns_address_state=dict(required=False, type='str', choices=['present-in-dns', 'absent-in-dns']),
        state=dict(required=True, type='str', choices=['present', 'absent'])
    )


def main():
    """ Create PowerStore dns object and perform action on it
        based on user input from playbook """
    obj = PowerstoreDns()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
