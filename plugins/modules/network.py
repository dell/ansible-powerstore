#!/usr/bin/python
# Copyright: (c) 2021, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
module: network
version_added: '1.3.0'
short_description: Manage networks for PowerStore
description:
- Managing networks on PowerStore Storage System includes getting details of
  network, modifying attributes of network and adding/removing IP ports
  to/from storage network.

author:
- Akash Shendge (@shenda1) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerstore.powerstore

options:
  network_name:
    description:
    - The name of the network.
    - This parameter is added in 2.0.0.0.
    - Specify either I(network_name) or I(network_id) for any operation.
    type: str
  network_id:
    description:
    - The ID of the network.
    type: str
  vlan_id:
    description:
    - The ID of the VLAN.
    type: int
  gateway:
    description:
    - Network gateway in IPv4 format.
      IP version.
    - Specify empty string to remove the gateway.
    type: str
  prefix_length:
    description:
    - Network prefix length.
    type: int
  new_cluster_mgmt_address:
    description:
    - New cluster management IP address in IPv4 format.
    type: str
  storage_discovery_address:
    description:
    - New storage discovery IP address in IPv4 format.
    - Specify empty string to remove the storage discovery IP address.
    type: str
  mtu:
    description:
    - Maximum Transmission Unit (MTU) packet size set on network interfaces,
      in bytes.
    type: int
  new_name:
    description:
    - New name of the network.
    type: str
  addresses:
    description:
    - IP addresses to add/remove in IPv4 format.
    type: list
    elements: dict
    suboptions:
      current_address:
        description:
        - Existing IPv4 address.
        type: str
      new_address:
        description:
        - New IPv4 address.
        type: str
  ports:
    description:
    - Ports to be mapped/unmapped to/from the storage network.
    type: list
    elements: str
  port_state:
    description:
    - Specifies whether port should mapped/unmapped from the storage network.
    type: str
    choices: ['present-in-network', 'absent-in-network']
  vasa_provider_credentials:
    description:
    - Credentials required for re-registering the VASA vendor provider during
      the reconfiguration of the cluster management IP address.
    type: dict
    suboptions:
      username:
        description:
        - VASA vendor provider user name.
        type: str
        required: true
      password:
        description:
        - VASA vendor provider password.
        type: str
        required: true
  esxi_credentials:
    description:
    - Credentials required for re-registering the ESXi hosts in the vCenter.
    - It should be passed only when ESXi host addresses or management network
      VLAN / prefix / gateway are changed during the reconfiguration of the
      PowerStore X model appliances.
    - This parameter is applicable only for PowerStore X model.
    - This parameter will be ignored if passed for PowerStore T model.
    type: list
    elements: dict
    suboptions:
      node_id:
        description:
        - Node identifier corresponding to the ESXi host.
        type: str
        required: true
      password:
        description:
        - ESXi host root password.
        type: str
        required: true
  wait_for_completion:
    description:
    - Flag to indicate if the operation should be run synchronously or
      asynchronously. C(true) signifies synchronous execution. By default,
      modify operation will run C(asynchronously).
    default: false
    type: bool
  state:
    description:
    - Define whether the network exist or not.
    required: true
    choices: ['absent', 'present']
    type: str

notes:
- It is recommended to perform task asynchronously while changing cluster
  management address.
- Idempotency is not supported for I(vasa_provider_credentials) and
  I(esxi_credentials).
- For PowerStore X model, I(vasa_provider_credentials) has to be specified
  along with I(new_cluster_mgmt_address).
- The I(check_mode) is not supported.
'''

EXAMPLES = r'''
- name: Get network details using ID
  dellemc.powerstore.network:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    network_id: "NW1"
    state: "present"

- name: Get network details using name
  dellemc.powerstore.network:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    network_name: "Default Management Network"
    state: "present"

- name: Rename the storage network
  dellemc.powerstore.network:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    network_name: "Default Storage Network"
    new_name: "iSCSI Network"
    wait_for_completion: true
    state: "present"

- name: Replace the IP's in the management network and re-register VASA vendor provider
  dellemc.powerstore.network:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    network_id: "NW1"
    addresses:
      - current_address: "100.230.x.x"
        new_address: "100.230.x.x"
      - current_address: "100.230.x.x"
        new_address: "100.230.x.x"
      - current_address: "100.230.x.x"
        new_address: "100.230.x.x"
    new_cluster_mgmt_address: "100.230.x.x"
    vasa_provider_credentials:
      username: "vmadmin"
      password: "{{vm_password}}"
    state: "present"

- name: Map port to the storage network
  dellemc.powerstore.network:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    network_id: "NW6"
    ports:
      - "IP1"
    port_state: "present-in-network"
    state: "present"

- name: Unmap port from the storage network
  dellemc.powerstore.network:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    network_id: "NW6"
    ports:
      - "IP1"
    port_state: "absent-in-network"
    state: "present"

- name: Replace the IP's in the management network and re-register VASA vendor
        provider for X model
  dellemc.powerstore.network:
    array_ip: "{{array_ip1}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    network_id: "NW1"
    vlan_id: 0
    gateway: "100.231.x.x"
    mtu: 1500
    prefix_length: 24
    addresses:
      - current_address: "100.230.x.x"
        new_address: "100.231.x.x"
      - current_address: "100.230.x.x"
        new_address: "100.231.x.x"
      - current_address: "100.230.x.x"
        new_address: "100.231.x.x"
      - current_address: "100.230.x.x"
        new_address: "100.231.x.x"
      - current_address: "100.230.x.x"
        new_address: "100.231.x.x"
    new_cluster_mgmt_address: "100.231.x.x"
    vasa_provider_credentials:
      username: "vmadmin"
      password: "{{vm_password}}"
    esxi_credentials:
      - "node_id": "N1"
        "password": "{{node_password}}"
      - "node_id": "N2"
        "password": "{{node_password}}"
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
        "description_l10n": "Modify network parameters.",
        "end_time": "2022-01-06T07:39:05.846+00:00",
        "estimated_completion_time": null,
        "id": "be0d099c-a6cf-44e8-88d7-9be80ccae369",
        "parent_id": null,
        "phase": "Completed",
        "phase_l10n": "Completed",
        "progress_percentage": 100,
        "resource_action": "modify",
        "resource_action_l10n": "modify",
        "resource_id": "nw6",
        "resource_name": null,
        "resource_type": "network",
        "resource_type_l10n": "network",
        "response_body": null,
        "response_status": null,
        "response_status_l10n": null,
        "root_id": "be0d099c-a6cf-44e8-88d7-9be80ccae369",
        "start_time": "2022-01-06T07:39:05.47+00:00",
        "state": "COMPLETED",
        "state_l10n": "Completed",
        "step_order": 23792565,
        "user": "admin"
    }

network_details:
    description: The network details.
    type: complex
    returned: When network exists.
    contains:
        name:
            description: The name of the network.
            type: str
        id:
            description: The ID of the network.
            type: str
        gateway:
            description: The gateway of the network.
            type: str
        vlan_id:
            description: VLAN identifier.
            type: int
        prefix_length:
            description: Network prefix length.
            type: int
        mtu:
            description: Maximum Transmission Unit (MTU) packet size set on
                         network interfaces, in bytes.
            type: int
        ip_version:
            description: IP protocol version
            type: str
        type:
            description: Network type
            type: str
        purposes:
            description: Purposes of the network.
            type: list
        cluster_details:
            description: The details of the cluster.
            type: complex
            contains:
                id:
                    description: The unique identifier of the cluster.
                    type: str
                name:
                    description: The name of the cluster.
                    type: str
                management_address:
                    description: The floating management IP address for the
                                 cluster in IPv4 or IPv6 format.
                    type: str
                storage_discovery_address:
                    description: The floating storage discovery IP address for
                                 the cluster in IPv4 or IPv6 format.
                    type: str
                appliance_count:
                    description: Number of appliances configured in this
                                 cluster.
                    type: int
        member_ips:
            description: Properties of the IP pool address.
            type: complex
            contains:
                id:
                    description: Unique identifier of the IP address.
                    type: str
                name:
                    description: Name of the IP address.
                    type: str
                network_id:
                    description: Unique identifier of the network to which the
                                 IP address belongs.
                    type: str
                ip_port_id:
                    description: Unique identifier of the port that uses this
                                 IP address to provide access to storage
                                 network services, such as iSCSI. This
                                 attribute can be set only for an IP address
                                 used by networks of type Storage.
                    type: str
                appliance_id:
                    description: Unique identifier of the appliance to which
                                 the IP address belongs.
                    type: str
                node_id:
                    description: Unique identifier of the cluster node to
                                 which the IP address belongs.
                    type: str
                address:
                    description: IP address value, in IPv4 or IPv6 format.
                    type: str
                purposes:
                    description: IP address purposes.
                    type: list
        vcenter_details:
            description: Details of the vcenter.
            type: complex
            contains:
                address:
                    description: IP address of vCenter host, in IPv4, IPv6,
                                 or hostname format.
                    type: str
                id:
                    description: Unique identifier of the vCenter instance.
                    type: str
                instance_uuid:
                    description: UUID instance of the vCenter.
                    type: str
                username:
                    description: User name to login to vCenter.
                    type: str
                vendor_provider_status:
                    description: General status of the VASA vendor provider
                                 in vCenter.
                    type: str
    sample: {
        "cluster_details": {
            "appliance_count": 1,
            "chap_mode": "Disabled",
            "compatibility_level": 10,
            "global_id": "PS00d01e1bb312",
            "id": 0,
            "is_encryption_enabled": true,
            "management_address": "10.xx.xx.xx",
            "master_appliance_id": "A1",
            "name": "WN-D8977",
            "physical_mtu": 1500,
            "service_config_details": null,
            "state": "Configured",
            "state_l10n": "Configured",
            "storage_discovery_address": "10.xx.xx.xx",
            "system_time": "2022-02-04T11:18:37.441Z"
        },
        "gateway": "10.xx.xx.xx",
        "id": "NW1",
        "ip_version": "IPv4",
        "ip_version_l10n": "IPv4",
        "member_ips": [
            {
                "address": "10.xx.xx.xx",
                "appliance_id": null,
                "id": "IP1",
                "ip_port_id": null,
                "name": "Default Management Network (10.xx.xx.xx)",
                "network_id": "NW1",
                "node_id": null,
                "purposes": [
                    "Mgmt_Cluster_Floating"
                ],
                "purposes_l10n": [
                    "Mgmt_Cluster_Floating"
                ]
            },
            {
                "address": "10.xx.xx.xx",
                "appliance_id": null,
                "id": "IP2",
                "ip_port_id": null,
                "name": "Default Management Network (10.xx.xx.xx)",
                "network_id": "NW1",
                "node_id": null,
                "purposes": [
                    "Mgmt_Appliance_Floating"
                ],
                "purposes_l10n": [
                    "Mgmt_Appliance_Floating"
                ]
            }
        ],
        "mtu": 1500,
        "name": "Default Management Network",
        "prefix_length": 24,
        "purposes": [],
        "purposes_l10n": null,
        "type": "Management",
        "type_l10n": "Management",
        "vcenter_details": {
            "address": "10.xx.xx.xx",
            "id": "0d330d6c-3fe6-41c6-8023-5bd3fa7c61cd",
            "instance_uuid": "c4c14fbb-828b-40f3-99bb-5bd4db723516",
            "username": "administrator@vsphere.local",
            "vendor_provider_status": "Online",
            "vendor_provider_status_l10n": "Online"
        },
        "vlan_id": 0
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import utils

LOG = utils.get_logger('network')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/3.0.0'


class PowerStoreNetwork(object):
    """Class with network operations"""

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_network_parameters())

        # initialize the Ansible module
        mut_ex_args = [['network_id', 'network_name']]
        required_one_of = [['network_id', 'network_name']]
        required_together = [['ports', 'port_state']]

        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mut_ex_args,
            required_one_of=required_one_of,
            required_together=required_together
        )

        LOG.info('HAS_PY4PS = %s , IMPORT_ERROR = %s', HAS_PY4PS,
                 IMPORT_ERROR)
        if HAS_PY4PS is False:
            self.module.fail_json(msg=IMPORT_ERROR)
        LOG.info('IS_SUPPORTED_PY4PS_VERSION = %s , VERSION_ERROR = '
                 '%s', IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR)
        if IS_SUPPORTED_PY4PS_VERSION is False:
            self.module.fail_json(msg=VERSION_ERROR)

        self.conn = utils.get_powerstore_connection(
            self.module.params, application_type=APPLICATION_TYPE)
        self.configuration = self.conn.config_mgmt
        self.provisioning = self.conn.provisioning
        LOG.info('Got Py4ps instance for configuration on PowerStore %s',
                 self.configuration)

    def get_member_ips(self, network_id):
        """ Get IP members of the network """

        try:
            filters = {'network_id': 'eq.' + network_id}
            return self.configuration.get_ip_pool_address(filters)
        except Exception as e:
            msg = 'Failed to get the member IPs of {0} with ' \
                  'error {1}'.format(network_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_cluster_details(self):
        """ Get cluster details """

        try:
            cluster_details = self.configuration.get_clusters()
            if cluster_details:
                return self.configuration.get_cluster_details(
                    cluster_details[0]['id'])
        except Exception as e:
            msg = 'Failed to get the cluster details with error {0}'.format(
                str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_vcenter_details(self):
        """ Get vcenter details """

        try:
            vcenter_details = self.configuration.get_vcenters()
            if vcenter_details:
                return self.configuration.get_vcenter_details(
                    vcenter_details[0]['id'])
        except Exception as e:
            msg = 'Failed to get the vcenter details with error {0}'.format(
                str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_network_details(self, network_name=None, network_id=None):
        """ Get network details by name or id"""

        try:
            LOG.info('Getting the details of network , Name:%s ,'
                     ' ID:%s', network_name, network_id)
            if network_id:
                resp = self.configuration.get_network_details(network_id)
            else:
                resp = self.configuration.get_network_by_name(
                    name=network_name)
                if resp and len(resp) > 0:
                    resp = resp[0]

            if resp:
                resp['member_ips'] = self.get_member_ips(resp['id'])
                resp['cluster_details'] = self.get_cluster_details()
                resp['vcenter_details'] = self.get_vcenter_details()
                return resp
            return None
        except Exception as e:
            name_or_id = network_name if network_name else network_id
            msg = "Get details of network {0} failed with error {1}".format(
                name_or_id, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def add_ports_to_network(self, network_details, ports):
        """ Add IP ports to the storage network """

        existing_ports = []

        if network_details['member_ips']:
            for ip in network_details['member_ips']:
                if ip['ip_port_id']:
                    existing_ports.append(ip['ip_port_id'])

        ports_to_add = list(set(ports) - set(existing_ports))

        if len(ports_to_add) == 0:
            return False

        try:
            LOG.info("Ports to add: %s", ports_to_add)
            self.configuration.add_remove_ports(network_details['id'],
                                                add_port_ids=ports_to_add)
            return True
        except Exception as e:
            errormsg = "Add existing IP ports to storage network {0} failed" \
                       " with error {1}".format(network_details['id'], str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg, **utils.failure_codes(e))

    def remove_ports_from_network(self, network_details, ports):
        """ Remove IP ports from the storage network """

        existing_ports = []

        if network_details['member_ips']:
            for ip in network_details['member_ips']:
                if ip['ip_port_id']:
                    existing_ports.append(ip['ip_port_id'])

        ports_to_remove = list(set(ports).intersection(set(existing_ports)))

        if len(ports_to_remove) == 0:
            return False

        try:
            LOG.info("Ports to remove: %s", ports_to_remove)
            self.configuration.add_remove_ports(
                network_details['id'], remove_port_ids=ports_to_remove)
            return True
        except Exception as e:
            errormsg = "Remove existing IP ports from storage network {0} " \
                       "failed with error {1}".format(network_details['id'],
                                                      str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg, **utils.failure_codes(e))

    def modify_network(self, network_id, wait_for_completion,
                       network_modify_dict):
        """Modify network properties"""

        if wait_for_completion:
            is_async = False
        else:
            is_async = True

        try:
            LOG.info("Modify network properties")
            job_dict = self.configuration.modify_network(
                network_id, network_modify_dict, is_async)
            return True, job_dict
        except Exception as e:
            errormsg = "Modify operation of network with id: {0}, failed " \
                       "with error {1}".format(network_id, str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg, **utils.failure_codes(e))

    def register_vasa_provider(self, vcenter_id, vasa_provider_credentials):
        """Register VASA provider"""

        try:
            LOG.info("Register VASA provider")
            modify_dict = dict()
            modify_dict['vasa_provider_credentials'] = \
                vasa_provider_credentials
            self.configuration.modify_vcenter(vcenter_id=vcenter_id,
                                              modify_param_dict=modify_dict)
            return True
        except Exception as e:
            errormsg = "VASA provider registration of vcenter with id: {0}," \
                       " failed with error {1}".format(vcenter_id, str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg, **utils.failure_codes(e))

    def check_array_version(self, network_name):
        """Verify PowerStore array version"""

        try:
            foot_hill_version = '2.0.0.0'
            release_version = self.provisioning.get_array_version()

            if release_version and network_name and (
                    utils.parse_version(release_version) <
                    utils.parse_version(foot_hill_version)):
                error_message = 'Please provide network_id. Network name ' \
                                'can be used with PowerStore ' \
                                'release >= 2.0.0.0.'
                LOG.error(error_message)
                self.module.fail_json(msg=error_message)
        except Exception as e:
            error_msg = "Failed to get the array version with error " \
                        "{0}".format(str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def validate_parameters(self):
        """Validate the input parameters"""

        param_list = ['network_name', 'new_name']
        param_list1 = ['network_id', 'gateway', 'storage_discovery_address']
        msg = "Please provide valid {0}"

        for param in param_list:
            if self.module.params[param] is not None and len(
                    self.module.params[param].strip()) == 0:
                error_msg = msg.format(param)
                self.module.fail_json(msg=error_msg)

        # Check for spaces
        for param in param_list1:
            if self.module.params[param] is not None and \
                    self.module.params[param].count(" ") > 0:
                error_msg = msg.format(param)
                self.module.fail_json(msg=error_msg)

        # Check for valid addresses
        addresses = self.module.params['addresses']
        if addresses:
            for address_dict in addresses:
                if 'current_address' in address_dict and \
                        address_dict['current_address'] is not None and \
                        len(address_dict['current_address'].strip()) == 0:
                    error_msg = "Please provide valid current address."
                    self.module.fail_json(msg=error_msg)

                if 'new_address' in address_dict and \
                        address_dict['new_address'] is not None and \
                        len(address_dict['new_address'].strip()) == 0:
                    error_msg = "Please provide valid new address."
                    self.module.fail_json(msg=error_msg)

    def perform_module_operation(self):
        """
        Perform different actions on network based on user parameters
        chosen in playbook
        """
        network_name = self.module.params['network_name']
        network_id = self.module.params['network_id']
        vlan_id = self.module.params['vlan_id']
        gateway = self.module.params['gateway']
        prefix_length = self.module.params['prefix_length']
        mtu = self.module.params['mtu']
        new_name = self.module.params['new_name']
        storage_discovery_address = self.module.params[
            'storage_discovery_address']
        addresses = self.module.params['addresses']
        ports = self.module.params['ports']
        port_state = self.module.params['port_state']
        new_cluster_mgmt_address = self.module.params['new_cluster_mgmt_address']
        vasa_provider_credentials = self.module.params[
            'vasa_provider_credentials']
        esxi_credentials = self.module.params['esxi_credentials']
        wait_for_completion = self.module.params['wait_for_completion']
        state = self.module.params['state']

        # result is a dictionary to contain end state and network details
        result = dict(
            changed=False,
            network_details=None
        )

        self.check_array_version(network_name)

        self.validate_parameters()

        # Get the details of Network
        network_details = self.get_network_details(network_name, network_id)
        if not network_id and network_details:
            network_id = network_details['id']

        if state == 'present' and not network_details:
            error_message = 'Network not found - Creation of network is ' \
                            'not allowed through Ansible module.'
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

        if state == 'absent' and network_details:
            error_message = 'Deletion of network is not allowed through ' \
                            'Ansible module.'
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

        if state == 'present' and not network_details['vcenter_details'] and \
                vasa_provider_credentials:
            error_message = "Please configure the vCenter server."
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

        # Check if modification to the network is required
        if state == 'present' and network_details:
            new_network_param_dict = {
                "vlan_id": vlan_id,
                "gateway": gateway,
                "prefix_length": prefix_length,
                "mtu": mtu,
                "name": new_name
            }

            network_modify_dict = check_network_modified(
                network_details, new_network_param_dict,
                new_cluster_mgmt_address, storage_discovery_address,
                addresses, vasa_provider_credentials, esxi_credentials)

        # Check if IP ports can be added to storage network
        if state == 'present' and port_state == 'present-in-network' \
                and network_details and ports:
            result['changed'] = self.add_ports_to_network(network_details,
                                                          ports)
        # Check if IP ports can be removed from storage network
        elif state == 'present' and port_state == 'absent-in-network' \
                and network_details and ports:
            result['changed'] = self.remove_ports_from_network(
                network_details, ports)

        # Register VASA provider
        if state == 'present' and network_details['vcenter_details'] and \
                'vendor_provider_status' in \
                network_details['vcenter_details'] and \
                network_details['vcenter_details']['vendor_provider_status'] \
                == 'Not_Registered':
            result['changed'] = self.register_vasa_provider(
                network_details['vcenter_details']['id'],
                vasa_provider_credentials)

        # Modify Network Properties
        if state == 'present' and network_details and network_modify_dict:
            result['changed'], job_dict = self.modify_network(
                network_id, wait_for_completion, network_modify_dict)

        # Finally update the module result!
        if state == 'present' and result['changed'] and network_modify_dict \
                and not wait_for_completion:
            result['job_details'] = job_dict
        else:
            result['network_details'] = self.get_network_details(
                network_name, network_id)
        self.module.exit_json(**result)


def check_network_modified(network_details, new_network_param_dict=None,
                           new_cluster_mgmt_address=None,
                           storage_discovery_address=None,
                           addresses=None, vasa_provider_credentials=None,
                           esxi_credentials=None):
    """Check if modification is required for network"""

    LOG.info("Checking if modification is required for network")
    modify_param = dict()

    for key in new_network_param_dict.keys():
        if key in network_details and \
                new_network_param_dict[key] is not None and \
                new_network_param_dict[key] != network_details[key]:
            modify_param[key] = new_network_param_dict[key]

    existing_address = network_details['cluster_details'][
        'storage_discovery_address']
    if (storage_discovery_address is not None and
        existing_address != storage_discovery_address) and \
            ((existing_address is None and storage_discovery_address != "")
             or (existing_address is not None)):
        modify_param['storage_discovery_address'] = storage_discovery_address

    if new_cluster_mgmt_address is not None and \
            network_details['cluster_details']['management_address'] != \
            new_cluster_mgmt_address:
        modify_param['cluster_mgmt_address'] = new_cluster_mgmt_address

    if addresses is not None:
        existing_addresses = [ip['address'] for ip in
                              network_details['member_ips']]
        addresses_to_add = []
        addresses_to_remove = []
        for address_dict in addresses:
            if address_dict['current_address'] and address_dict['new_address']:
                if address_dict['current_address'] in existing_addresses:
                    addresses_to_add.append(address_dict['new_address'])
                    addresses_to_remove.append(address_dict['current_address']
                                               )
            elif address_dict['current_address'] and \
                    address_dict['current_address'] in existing_addresses:
                addresses_to_remove.append(address_dict['current_address'])
            elif address_dict['new_address'] and \
                    address_dict['new_address'] not in existing_addresses:
                addresses_to_add.append(address_dict['new_address'])

        if addresses_to_add:
            modify_param['add_addresses'] = addresses_to_add
        if addresses_to_remove:
            modify_param['remove_addresses'] = addresses_to_remove

    if vasa_provider_credentials is not None:
        modify_param['vasa_provider_credentials'] = vasa_provider_credentials

    if esxi_credentials is not None:
        modify_param['esxi_credentials'] = esxi_credentials

    return modify_param


def get_powerstore_network_parameters():
    """This method provide the parameters required for the network operations
     on PowerStore"""

    return dict(
        network_name=dict(), network_id=dict(), vlan_id=dict(type='int'),
        gateway=dict(), prefix_length=dict(type='int'), new_name=dict(),
        mtu=dict(type='int'), new_cluster_mgmt_address=dict(),
        addresses=dict(type='list', elements='dict',
                       options=dict(current_address=dict(type='str'),
                                    new_address=dict(type='str'))),
        vasa_provider_credentials=dict(
            type='dict', options=dict(
                username=dict(type='str', required=True),
                password=dict(type='str', required=True, no_log=True))),
        esxi_credentials=dict(type='list', elements='dict',
                              options=dict(node_id=dict(type='str',
                                                        required=True),
                                           password=dict(type='str',
                                                         required=True,
                                                         no_log=True))),
        storage_discovery_address=dict(),
        ports=dict(type='list', elements='str'),
        port_state=dict(choices=['present-in-network',
                                 'absent-in-network']),
        wait_for_completion=dict(type='bool', default=False),
        state=dict(required=True, type='str', choices=['present', 'absent'])
    )


def main():
    """ Create PowerStore network object and perform action on it based on
    user input from playbook """
    obj = PowerStoreNetwork()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
