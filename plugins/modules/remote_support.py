#!/usr/bin/python
# Copyright: (c) 2022, DellEMC
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: remote_support
version_added: '1.5.0'
short_description: Remote Support operations on a PowerStore storage system
description:
- Performs all Remote Support operations on a PowerStore Storage System.
  This module supports getting details of an existing Remote Support
  configuration.
- This module also supports modifying an existing Remote Support configuration.
  Verify a remote support configuration. You can send a test alert through the remote
  support configuration.
author:
- Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>
extends_documentation_fragment:
  - dellemc.powerstore.dellemc_powerstore.powerstore
options:
  remote_support_id:
    description:
    - Unique identifier of the remote support configuration.
    required: True
    type: int
  support_type:
    description:
    - The type of remote support that is configured.
    - Mandatory for modify and verify operation.
    - SRS_Gateway support_type is only supported for verify operation.
    required: False
    type: str
    choices: ['SRS_Gateway', 'SRS_Gateway_Tier2', 'SRS_Gateway_Tier3', 'SRS_Integrated_Tier2', 'SRS_Integrated_Tier3', 'Disabled']
  remote_support_servers:
    description:
    - One or two remote support servers.
    required: False
    type: list
    elements: dict
    suboptions:
        address:
          description:
          - Gateway server IP address (IPv4).
          - The address is a mandatory key.
          type: str
          required: true
        port:
          description:
          - Gateway server port.
          type: int
        is_primary:
          description:
          - Indicates whether the server is acting as the primary.
          - One server must be set to false when two servers are configured.
          type: bool
  server_state:
    description:
    - Indicates the state of the remote-support_servers.
    - Required with remote_support_servers.
    required: False
    type: str
    choices: ['present-in-server', 'absent-in-server']
  is_support_assist_license_accepted:
    description:
    - Indicates whether user has accepted remote support license agreement
      before enabling the Support Assist on the system for the first time.
    required: False
    type: bool
  is_cloudiq_enabled:
    description:
    - Indicates whether support for CloudIQ is enabled.
    required: False
    type: bool
  is_rsc_enabled:
    description:
    - Indicates whether support for Remote Service Credentials is enabled.
    required: False
    type: bool
  proxy_address:
    description:
    - Proxy server IP address (IPv4).
    required: False
    type: str
  proxy_port:
    description:
    - Proxy server port number.
    required: False
    type: int
  proxy_username:
    description:
    - User name for proxy server access.
    required: False
    type: str
  proxy_password:
    description:
    - Password for proxy server access.
    required: False
    type: str
  is_icw_configured:
    description:
    - Client already configured ICW.
    required: False
    type: bool
  verify_connection:
    description:
    - Indicates whether to perform the verify call or not.
    required: False
    type: bool
    default: False
  send_test_alert:
    description:
    - Indicates whether to send a test alert or not.
    required: False
    type: bool
    default: False
  wait_for_completion:
    description:
    - Flag to indicate if the operation should be run synchronously or
      asynchronously. True signifies synchronous execution. By default,
      modify operation will run asynchronously.
    default: False
    type: bool
  return_support_license_text:
    description:
    - Indicates whether to return support license agreement text or not.
    required: False
    type: bool
    default: False
  state:
    description:
    - The state of the remote support configuration after the task is performed.
    - For Delete operation only, it should be set to "absent".
    - For get/modify operation it should be set to "present".
    required : True
    choices: [ 'present', 'absent']
    type: str

notes:
- Creation and deletion of remote support configuration is not supported.
- Support for check_mode is not available for this module.
- Verify and send test alert operations do not support idempotency.
'''

EXAMPLES = r'''

  - name: Get details of remote support configuration
    dellemc.powerstore.remote_support:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       remote_support_id: 0
       state: "present"

  - name: Modify remote support configuration - SRS_Gateway_Tier2
    dellemc.powerstore.remote_support:
      array_ip: "{{array_ip}}"
      user: "{{user}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      remote_support_id: 0
      support_type: "SRS_Gateway_Tier2"
      remote_support_servers:
      - address: "10.XX.XX.XX"
        port: 9443
        is_primary: True
      - address: "10.XX.XX.YY"
        port: 9443
        is_primary: False
      server_state: "present-in-server"
      is_rsc_enabled: True
      is_cloudiq_enabled: False
      timeout: 300
      state: "present"

  - name: Modify remote support configuration - SRS_Integrated_Tier2
    dellemc.powerstore.remote_support:
      array_ip: "{{array_ip}}"
      user: "{{user}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      remote_support_id: 0
      support_type: "SRS_Integrated_Tier2"
      proxy_address: "10.XX.XX.ZZ"
      proxy_port: 3128
      proxy_username: "user"
      proxy_password: "password"
      timeout: 300
      state: "present"

  - name: Verify remote support configuration
    dellemc.powerstore.remote_support:
      array_ip: "{{array_ip}}"
      user: "{{user}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      remote_support_id: 0
      support_type: "SRS_Integrated_Tier3"
      timeout: 300
      verify_connection: True
      state: "present"

  - name: Send a test alert
    dellemc.powerstore.remote_support:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       remote_support_id: 0
       send_test_alert: True
       state: "present"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"
job_details:
    description: The job details.
    type: complex
    returned: When asynchronous task is performed.
    contains:
        id:
            description: The ID of the job.
            type: str
    sample: {
        "description_l10n": "Modify SupportAssist configuration.",
        "end_time": "2022-02-24T04:41:56.852+00:00",
        "estimated_completion_time": null,
        "id": "24e3f881-87f1-49f6-8764-13df4906eb2f",
        "parent_id": null,
        "phase": "Completed",
        "phase_l10n": "Completed",
        "progress_percentage": 100,
        "resource_action": "modify",
        "resource_action_l10n": "modify",
        "resource_id": "0",
        "resource_name": null,
        "resource_type": "remote_support",
        "resource_type_l10n": "remote support",
        "response_body": null,
        "response_status": "204",
        "response_status_l10n": "204",
        "root_id": "24e3f881-87f1-49f6-8764-13df4906eb2f",
        "start_time": "2022-02-24T04:41:38.146+00:00",
        "state": "COMPLETED",
        "state_l10n": "Completed",
        "step_order": 64871764,
        "user": "admin"
    }
remote_support_details:
    description: Details of the remote support configuration.
    returned: When remote support configuration exists.
    type: complex
    contains:
        id:
            description: Unique identifier of remote support configuration.
            type: int
        type:
            description: The type of remote support that is configured.
            type: str
        is_cloudiq_enabled:
            description: Indicates whether support for CloudIQ is enabled.
            type: bool
        is_support_assist_license_accepted:
            description: Indicates whether user has accepted remote support license agreement
             before enabling the Support Assist on the system for the first time.
            type: bool
        support_assist_license_agreement_text:
            description: The support assist license agreement text.
            type: str
        is_rsc_enabled:
            description: Indicates whether support for Remote Service Credentials is enabled.
            type: bool
        proxy_address:
            description: Proxy server IP address (IPv4).
            type: str
        proxy_port:
            description: Proxy server port number.
            type: int
        proxy_username:
            description: User name for proxy server access.
            type: str
        proxy_password:
            description: Password for proxy server access.
            type: str
        remote_support_servers:
            description:
                - Details of two remote support servers.
            type: complex
            contains:
                id:
                    description: Unique identifier of the remote support server.
                    type: str
                address:
                    description: Gateway server IP address (IPv4).
                    type: str
                port:
                    description: Gateway server port.
                    type: int
                is_primary:
                    description: Indicates whether the server is acting as the primary.
                    type: bool
    sample: {
        "connectivity_status": "Unavailable",
        "connectivity_status_l10n": "Unavailable",
        "id": "0",
        "is_cloudiq_enabled": true,
        "is_rsc_enabled": false,
        "is_support_assist_license_accepted": true,
        "last_update": "2022-02-11T11:16:39.134+00:00",
        "policy_manager_address": null,
        "policy_manager_port": null,
        "proxy_address": null,
        "proxy_port": null,
        "proxy_username": null,
        "remote_support_servers": [
            {
                "address": "localhost",
                "connectivity_qos": [
                    {
                        "appliance_id": "A1",
                        "connectivity_qos": "connectivity_qos",
                        "connectivity_qos_priority": 2,
                        "connectivity_qos_value": -1.0,
                        "id": "dc326198-2d92-4ff4-a774-324b00ca8818",
                        "last_update": "2022-02-11T11:16:39.888+00:00",
                        "remote_support_servers_id": "0"
                    }
                ],
                "id": "0",
                "is_primary": true,
                "port": "9443",
                "remote_support_id": "0"
            },
            {
                "address": "localhost",
                "connectivity_qos": [],
                "id": "1",
                "is_primary": false,
                "port": "null",
                "remote_support_id": "0"
            }
        ],
        "support_assist_license_agreement_text": "license string",
        "type": "SRS_Integrated_Tier3",
        "type_l10n": "SRS Integrated with Remote Access"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import dellemc_ansible_powerstore_utils as utils
import copy

LOG = utils.get_logger('remote_support')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.5.0'


class PowerstoreRemoteSupport(object):
    """Remote Support operations"""

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_remote_support_parameters())
        required_together = [['proxy_address', 'proxy_port'],
                             ['remote_support_servers', 'server_state']]
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

    def get_remote_support_details(self, remote_support_id, return_support_license_text):
        """Get Remote Support details by id"""
        try:
            LOG.info('Getting the details of Remote Support, '
                     'ID:%s', remote_support_id)

            resp = self.configuration.get_remote_support_details(remote_support_id=remote_support_id,
                                                                 return_support_license_text=return_support_license_text)
            LOG.info('Successfully got the details of Remote Support '
                     'with id: %s', remote_support_id)
            return resp

        except Exception as e:
            msg = 'Get details of Remote Support: {0}' \
                  'failed with' \
                  ' error : {1} '.format(remote_support_id,
                                         str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def test_remote_support_config(self, remote_support_id):
        """Send a test alert for remote support configuration"""
        try:
            LOG.info('Attempting to send a test mail for remote support '
                     'configuration id %s', remote_support_id)
            self.configuration.test_remote_support_config(
                remote_support_id=remote_support_id)
            return True
        except Exception as e:
            msg = 'Failed to send a test mail for remote support ' \
                  'id {0} with error {1}'.format(remote_support_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def add_remote_support_servers_two_unique_servers_exist(self, remote_support_details,
                                                            remote_support_servers, existing_gateway):

        # checking if user mentioned address is same as primary gateway
        if remote_support_servers[0]['address'] == existing_gateway[0]['address']:
            existing_gateway[0]['port'] = remote_support_servers[0]['port']
            existing_gateway[0]['is_primary'] = remote_support_servers[0]['is_primary']
            existing_gateway[1]['is_primary'] = not remote_support_servers[0]['is_primary']
        # checking if user mentioned address is same as backup gateway
        elif remote_support_servers[0]['address'] == existing_gateway[1]['address']:
            existing_gateway[1]['port'] = remote_support_servers[0]['port']
            existing_gateway[1]['is_primary'] = remote_support_servers[0]['is_primary']
            existing_gateway[0]['is_primary'] = not remote_support_servers[0]['is_primary']

        return existing_gateway

    def add_remote_support_servers_same_primary_and_backup_address(self, remote_support_details,
                                                                   remote_support_servers, existing_gateway):

        # check if user has mentioned the primary gateway.
        if remote_support_servers[0] in existing_gateway:
            return existing_gateway
        if remote_support_servers[0]['is_primary'] == existing_gateway[0]['is_primary'] and \
                existing_gateway[1]['port'] != remote_support_servers[0]['port']:
            existing_gateway[0]['port'] = remote_support_servers[0]['port']
        # check if user has mentioned the backup gateway.
        elif remote_support_servers[0]['is_primary'] == existing_gateway[0]['is_primary'] and \
                existing_gateway[0]['port'] != remote_support_servers[0]['port']:
            existing_gateway[1]['port'] = remote_support_servers[0]['port']

        return existing_gateway

    def add_remote_support_servers_none_exists(self, remote_support_details,
                                               remote_support_servers, existing_gateway):
        # Checking if user provided 0 or more than 1 server details.
        if len(remote_support_servers) != 1:
            existing_gateway = remote_support_servers
        # Checking if user provided backup server details only.
        elif len(remote_support_servers) == 1 and not \
                remote_support_servers[0]['is_primary']:
            existing_gateway = [{'is_primary': True}]
            existing_gateway = \
                existing_gateway + [i for i in remote_support_servers
                                    if i not in existing_gateway]
        # Checking if user provided primary server details only.
        elif len(remote_support_servers) == 1 and \
                remote_support_servers[0]['is_primary']:
            existing_gateway = [{'is_primary': False}]
            existing_gateway = \
                existing_gateway + [i for i in remote_support_servers
                                    if i not in existing_gateway]
        return existing_gateway

    def add_one_remote_support_server_primary_exists(self, remote_support_details,
                                                     remote_support_servers, existing_gateway):

        # if user provided backup server with different port and/or different address
        # as that of the existing primary server.
        if not remote_support_servers[0]['is_primary']:
            existing_gateway[1]['address'] = remote_support_servers[0]['address']
            existing_gateway[1]['port'] = remote_support_servers[0]['port']

        # if user provided a primary server.
        elif remote_support_servers[0]['is_primary']:
            existing_gateway[1]['address'] = existing_gateway[0]['address']
            existing_gateway[1]['port'] = existing_gateway[0]['port']
            existing_gateway[0]['address'] = remote_support_servers[0]['address']
            existing_gateway[0]['port'] = remote_support_servers[0]['port']
        return existing_gateway

    def add_two_remote_support_server_primary_exists(self, remote_support_details,
                                                     remote_support_servers, existing_gateway):
        # if none of the address mentioned addresses match with existing address.
        if remote_support_servers[0]["address"] != existing_gateway[0]["address"] and \
                remote_support_servers[1]["address"] != existing_gateway[0]["address"]:
            existing_gateway = \
                remote_support_servers + [i for i in existing_gateway
                                          if i not in remote_support_servers]
        # if one address matches with the existing primary address.
        else:
            existing_gateway = remote_support_servers

        return existing_gateway

    def add_remote_support_servers_primary_exists(self, remote_support_details,
                                                  remote_support_servers, existing_gateway):

        # Checking if user provided only 1 server details.
        if len(remote_support_servers) == 1:

            existing_gateway = self.add_one_remote_support_server_primary_exists(remote_support_details=remote_support_details,
                                                                                 remote_support_servers=remote_support_servers,
                                                                                 existing_gateway=existing_gateway)
        # Checking if user provided 2 server details.
        elif len(remote_support_servers) == 2:

            existing_gateway = self.add_two_remote_support_server_primary_exists(remote_support_details=remote_support_details,
                                                                                 remote_support_servers=remote_support_servers,
                                                                                 existing_gateway=existing_gateway)

        return existing_gateway

    def add_remote_support_servers_primary_and_backup_exists(self, remote_support_details,
                                                             remote_support_servers,
                                                             existing_gateway):

        # checking if any address mentioned by user is different from the existing server addresses.
        different_address = 0
        for i in range(len(remote_support_servers)):
            if remote_support_servers[i]['address'] != existing_gateway[0]["address"] and \
                    remote_support_servers[i]['address'] != existing_gateway[1]["address"]:
                existing_gateway = \
                    remote_support_servers + [i for i in existing_gateway
                                              if i not in remote_support_servers]
                different_address = 1
        if different_address != 1:
            # checking if user mentioned 2 server details.
            if len(remote_support_servers) != 1:
                existing_gateway = remote_support_servers
                return existing_gateway
            # checking if user mentioned only 1 server details
            elif len(remote_support_servers) == 1:
                # checking if primary and backup adddresses are different.
                if existing_gateway[0]['address'] != existing_gateway[1]['address']:
                    existing_gateway = self.add_remote_support_servers_two_unique_servers_exist(remote_support_details=remote_support_details,
                                                                                                remote_support_servers=remote_support_servers,
                                                                                                existing_gateway=existing_gateway)

                # checking if same address exists as primary and backup.
                elif existing_gateway[0]['address'] == existing_gateway[1]['address']:
                    existing_gateway = self.add_remote_support_servers_same_primary_and_backup_address(remote_support_details=remote_support_details,
                                                                                                       remote_support_servers=remote_support_servers,
                                                                                                       existing_gateway=existing_gateway)

        return existing_gateway

    def add_remote_support_servers(self, remote_support_details, remote_support_servers,
                                   existing_gateway):
        # Checking if currently no server is associated to remote support configuration.
        if existing_gateway[1]['address'] is None and existing_gateway[0]['address'] == "localhost":

            existing_gateway = self.add_remote_support_servers_none_exists(remote_support_details=remote_support_details,
                                                                           remote_support_servers=remote_support_servers,
                                                                           existing_gateway=existing_gateway)

        # Checking if only one gateway server is associated to the remote support configuration.
        elif existing_gateway[1]['address'] is None and existing_gateway[0]['address'] != "localhost":

            existing_gateway = self.add_remote_support_servers_primary_exists(remote_support_details=remote_support_details,
                                                                              remote_support_servers=remote_support_servers,
                                                                              existing_gateway=existing_gateway)

        # if both primary and backup addresses are associated to remote support configuration
        elif existing_gateway[1]['address'] is not None and existing_gateway[0]['address'] is not None:

            existing_gateway = self.add_remote_support_servers_primary_and_backup_exists(remote_support_details=remote_support_details,
                                                                                         remote_support_servers=remote_support_servers,
                                                                                         existing_gateway=existing_gateway)
        return existing_gateway

    def remove_remote_support_servers_address_only(self, remote_support_details, remote_support_servers,
                                                   existing_gateway, position, rem_address):

        # if existing addresses are different from each other.
        if existing_gateway[0]['address'] != existing_gateway[1]['address']:
            existing_gateway[position]['address'] = None
            existing_gateway[position]['port'] = None
        # if existing addresses are same
        else:
            msg = "Two gateway servers with address: {0} exist. Please " \
                "provide port or is_primary value as well.".format(rem_address['address'])
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        return existing_gateway

    def remove_remote_support_servers_with_port_or_is_primary(self, remote_support_details, remote_support_servers,
                                                              existing_gateway, position, rem_address):

        # if port and/or is_primary is mentioned.
        if (rem_address['port'] is not None and rem_address['is_primary'] is not None and
                rem_address['port'] == existing_gateway[position]['port'] and
                rem_address['is_primary'] == existing_gateway[position]['is_primary']) or \
                (rem_address['port'] is not None and rem_address['is_primary'] is None and
                 rem_address['port'] == existing_gateway[position]['port']) or \
                (rem_address['port'] is None and rem_address['is_primary'] is not None and
                 rem_address['is_primary'] == existing_gateway[position]['is_primary']):
            existing_gateway[position]['address'] = None
            existing_gateway[position]['port'] = None

        # if both port and is_primary are absent.
        elif rem_address['port'] is None and rem_address['is_primary'] is None:
            existing_gateway = self.remove_remote_support_servers_address_only(remote_support_details=remote_support_details,
                                                                               remote_support_servers=remote_support_servers,
                                                                               existing_gateway=existing_gateway,
                                                                               position=position,
                                                                               rem_address=rem_address)
        return existing_gateway

    def remove_remote_support_servers(self, remote_support_details, remote_support_servers,
                                      existing_gateway):
        # checking for each server detail mentioned by user with each existing server.
        for position in range(len(existing_gateway)):
            for rem_address in remote_support_servers:
                if rem_address['address'] == existing_gateway[position]['address']:
                    existing_gateway = self.remove_remote_support_servers_with_port_or_is_primary(remote_support_details=remote_support_details,
                                                                                                  remote_support_servers=remote_support_servers,
                                                                                                  existing_gateway=existing_gateway,
                                                                                                  position=position,
                                                                                                  rem_address=rem_address)

        # if primary is removed but backup still exists, making the backup as the primary.
        if existing_gateway[0]['address'] is None and existing_gateway[1]['address'] is not None:
            existing_gateway[0]['is_primary'] = False
            existing_gateway[1]['is_primary'] = True

        return existing_gateway

    def parameter_modify_check(self, modify_remote_support_dict, existing_gateway, current_gateway, remote_support_details, to_modify):
        """ To check if modification is needed as per the support_type"""

        if self.module.params['support_type'] is None and \
                (self.module.params['proxy_address'] is not None or
                 self.module.params['remote_support_servers'] is not None) and \
                self.module.params['verify_connection'] is False:
            msg = "Please provide the support_type to modify the configuration."
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        for gateway_server in existing_gateway:
            if gateway_server not in current_gateway:
                to_modify = True
                modify_remote_support_dict['remote_support_servers'] = existing_gateway
                break

        if modify_remote_support_dict['type'] == "SRS_Gateway_Tier2" or \
                modify_remote_support_dict['type'] == "SRS_Gateway_Tier3":
            if self.module.params['remote_support_servers'] is None and \
                    remote_support_details['type'] != "SRS_Gateway_Tier2" and \
                    remote_support_details['type'] != "SRS_Gateway_Tier3":
                msg = "remote_support_servers are required with type {0}".format(modify_remote_support_dict['type'])
                LOG.error(msg)
                self.module.fail_json(msg=msg)

            modify_remote_support_dict['remote_support_servers'] = existing_gateway

        if modify_remote_support_dict['type'] is not None and \
                modify_remote_support_dict['type'] != remote_support_details['type']:
            to_modify = True

        if modify_remote_support_dict['proxy_address'] != remote_support_details["proxy_address"]:
            to_modify = True
        return modify_remote_support_dict, to_modify

    def modify_remote_support_servers(self, server_state, remote_support_details, remote_support_servers,
                                      existing_gateway):
        """ Modifying the remote_support_server_list """

        # checking if the existing servers are same as the servers provided by the user
        # when server_state is present-in-server.
        if server_state == "present-in-server" and remote_support_servers is not None \
                and remote_support_servers != existing_gateway:
            existing_gateway = self.add_remote_support_servers(remote_support_details=remote_support_details,
                                                               remote_support_servers=remote_support_servers,
                                                               existing_gateway=existing_gateway)

        # check if server_state is absent-in-server
        elif server_state == "absent-in-server" and \
                (remote_support_details['type'] == "SRS_Gateway_Tier2" or
                 remote_support_details['type'] == "SRS_Gateway_Tier3"):
            existing_gateway = self.remove_remote_support_servers(remote_support_details=remote_support_details,
                                                                  remote_support_servers=remote_support_servers,
                                                                  existing_gateway=existing_gateway)
        return existing_gateway

    def modify_remote_support_required(self, remote_support_details):
        """ To check if modification is required or not"""
        remote_support_servers = self.module.params['remote_support_servers']
        server_state = self.module.params['server_state']
        modify_remote_support_dict = {
            'type': self.module.params['support_type'],
            'proxy_address': self.module.params['proxy_address'],
            'proxy_port': self.module.params['proxy_port'],
            'proxy_username': self.module.params['proxy_username'],
            'proxy_password': self.module.params['proxy_password'],
            'is_cloudiq_enabled': self.module.params['is_cloudiq_enabled'],
            'is_rsc_enabled': self.module.params['is_rsc_enabled']
        }

        if self.module.params['is_support_assist_license_accepted'] is False and \
                remote_support_details['is_support_assist_license_accepted'] is True:
            msg = "Once the Support Assist license is accepted, it can not be unaccepted."
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        to_modify = False
        keys = ['is_cloudiq_enabled', 'is_rsc_enabled'
                ]
        if remote_support_details['type'] != "Disabled":
            existing_gateway = [{
                'address': remote_support_details['remote_support_servers'][0]['address'],
                'port': remote_support_details['remote_support_servers'][0]['port'],
                'is_primary': remote_support_details['remote_support_servers'][0]['is_primary']},
                {
                'address': remote_support_details['remote_support_servers'][1]['address'],
                'port': remote_support_details['remote_support_servers'][1]['port'],
                'is_primary': remote_support_details['remote_support_servers'][1]['is_primary']
            }]

        if remote_support_details['type'] == "Disabled":
            existing_gateway = [{
                'address': "localhost",
                'port': None,
                'is_primary': None},
                {
                'address': None,
                'port': None,
                'is_primary': None
            }]

        if modify_remote_support_dict['type'] == "Disabled":
            if remote_support_details['type'] == "Disabled":
                return None
            modify_param = {'type': 'Disabled'}
            return modify_param
        current_gateway = copy.deepcopy(existing_gateway)
        existing_gateway = self.modify_remote_support_servers(server_state=server_state,
                                                              remote_support_details=remote_support_details,
                                                              remote_support_servers=remote_support_servers,
                                                              existing_gateway=existing_gateway)

        modify_remote_support_dict, to_modify = self.parameter_modify_check(modify_remote_support_dict=modify_remote_support_dict,
                                                                            existing_gateway=existing_gateway,
                                                                            current_gateway=current_gateway,
                                                                            remote_support_details=remote_support_details,
                                                                            to_modify=to_modify)

        for key in keys:
            if modify_remote_support_dict[key] is not None and\
                    remote_support_details[key] != modify_remote_support_dict[key]:
                LOG.debug("Key %s in remote_support_details=%s,"
                          "modify_remote_support_dict=%s", key,
                          remote_support_details[key], modify_remote_support_dict[key])
                to_modify = True

        if to_modify is True:
            return modify_remote_support_dict
        return None

    def modify_remote_support_details(self, remote_support_id,
                                      wait_for_completion, modify_params):
        """Perform modify operations on a Remote Support configuration"""

        if wait_for_completion:
            is_async = False
        else:
            is_async = True

        try:
            LOG.info('Attempting to modify Remote Support configuration with id %s',
                     remote_support_id)
            modify_params = {param: value for param, value in modify_params.items() if value is not None}

            job_dict = self.configuration.modify_remote_support_details(
                remote_support_id=remote_support_id, modify_parameters=modify_params, is_async=is_async)
            return True, job_dict
        except Exception as e:
            msg = 'Failed to modify Remote Support configuration instance ' \
                  'with error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def verify_remote_support_config(self, remote_support_id):
        """Perform verify operation on a Remote Support configuration"""

        try:
            LOG.info('Attempting to verify Remote Support configuration with id %s',
                     remote_support_id)
            support_type = self.module.params['support_type']
            if support_type is None:
                msg = "Please provide the support_type to verify the configuration."
                LOG.error(msg)
                self.module.fail_json(msg=msg)
            verify_params = dict()
            if support_type == "SRS_Integrated_Tier2" or support_type == "SRS_Integrated_Tier3":
                verify_params = {'type': support_type}
            elif support_type != "Disabled":
                if self.module.params['remote_support_servers'] is None:
                    msg = "remote_support_servers are required with type {0}".format(support_type)
                    LOG.error(msg)
                    self.module.fail_json(msg=msg)
                elif len(self.module.params['remote_support_servers']) == 1:
                    verify_params = {
                        'type': support_type,
                        'address': self.module.params['remote_support_servers'][0]['address'],
                        'port': self.module.params['remote_support_servers'][0]['port']
                    }
                else:
                    msg = "Please provide only one server for connection verification."
                    LOG.error(msg)
                    self.module.fail_json(msg=msg)

            self.configuration.verify_remote_support_config(
                remote_support_id=remote_support_id, verify_parameters=verify_params)
            return True
        except Exception as e:
            msg = 'Failed to verify Remote Support configuration instance ' \
                  'with error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def perform_module_operation(self):
        """Performing various module operations"""

        remote_support_id = self.module.params['remote_support_id']
        send_test_alert = self.module.params['send_test_alert']
        verify_connection = self.module.params['verify_connection']
        state = self.module.params['state']
        support_type = self.module.params['support_type']
        wait_for_completion = self.module.params['wait_for_completion']
        return_support_license_text = self.module.params['return_support_license_text']
        result = dict(
            remote_support_details=None
        )

        changed = False
        modify_params = None

        remote_support_details = self.get_remote_support_details(remote_support_id=remote_support_id,
                                                                 return_support_license_text=return_support_license_text)
        if remote_support_details and verify_connection is False and send_test_alert is False:
            modify_params = self.modify_remote_support_required(remote_support_details=remote_support_details)

        if not remote_support_details and state == 'present':
            msg = "Remote Support configuration by ID: {0} does not exist. Creation " \
                  "of Remote Support is not supported.".format(remote_support_id)
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        if state == 'absent' and remote_support_details:
            msg = " Deletion of Remote Support configuration is not supported."
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        if state == 'present' and remote_support_details and verify_connection is True:
            changed = self.verify_remote_support_config(remote_support_id=remote_support_id)

        if state == 'present' and remote_support_details and send_test_alert is True:
            changed = self.test_remote_support_config(remote_support_id=remote_support_id)

        if state == 'present' and remote_support_details and modify_params and support_type \
                and verify_connection is not True:
            changed, job_dict = self.modify_remote_support_details(
                remote_support_id=remote_support_id,
                wait_for_completion=wait_for_completion,
                modify_params=modify_params)

        if state == 'present' and changed and modify_params \
                and not wait_for_completion:
            result['job_details'] = job_dict
        else:
            result['remote_support_details'] = self.get_remote_support_details(remote_support_id=remote_support_id,
                                                                               return_support_license_text=return_support_license_text)
        result['changed'] = changed
        self.module.exit_json(**result)


def get_powerstore_remote_support_parameters():
    """This method provide the parameters required for the
      remote_support operations on PowerStore"""

    return dict(
        remote_support_id=dict(required=True, type='int'),
        support_type=dict(required=False, type='str', choices=['SRS_Gateway', 'SRS_Gateway_Tier2',
                                                               'SRS_Gateway_Tier3', 'SRS_Integrated_Tier2',
                                                               'SRS_Integrated_Tier3', 'Disabled']),
        proxy_port=dict(required=False, type='int'),
        proxy_address=dict(required=False, type='str'),
        proxy_username=dict(required=False, type='str'),
        proxy_password=dict(required=False, type='str', no_log=True),
        remote_support_servers=dict(
            type='list', required=False, elements='dict',
            options=dict(address=dict(type='str', required=True),
                         port=dict(type='int', required=False),
                         is_primary=dict(type='bool', required=False))
        ),
        server_state=dict(required=False, type='str', choices=['present-in-server', 'absent-in-server']),
        is_support_assist_license_accepted=dict(required=False, type='bool'),
        is_cloudiq_enabled=dict(required=False, type='bool'),
        is_rsc_enabled=dict(required=False, type='bool'),
        is_icw_configured=dict(required=False, type='bool'),
        verify_connection=dict(required=False, type='bool', default=False),
        send_test_alert=dict(required=False, type='bool', default=False),
        wait_for_completion=dict(required=False, type='bool', default=False),
        return_support_license_text=dict(required=False, type='bool', default=False),
        state=dict(required=True, type='str', choices=['present', 'absent'])
    )


def main():
    """ Create PowerStore Remote Support object and perform action on it
        based on user input from playbook """
    obj = PowerstoreRemoteSupport()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
