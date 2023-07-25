#!/usr/bin/python
# Copyright: (c) 2021, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)
""" Ansible module for managing cluster related operations for PowerStore"""
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: cluster

version_added: '1.3.0'

short_description: Manage cluster related operations on PowerStore

description:
- Managing cluster on PowerStore storage system includes creating cluster,
  validating create cluster attributes, getting details and modifying cluster
  configuration parameters.

extends_documentation_fragment:
  - dellemc.powerstore.powerstore

author:
- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>
- Bhavneet Sharma (@sharmb5) <ansible.team@dell.com>

options:
  cluster_name:
    description:
    - The Name of cluster.
    type: str
  chap_mode:
    description:
    - The mode that describes or sets the iSCSI CHAP mode for the cluster.
    type: str
    choices: ['Disabled', 'Single', 'Mutual']
  cluster_id:
    description:
    - Id of the cluster.
    type: str
  new_name:
    description:
    - The new name for the cluster.
    type: str
  service_password:
    description:
    - The password for the service user.
    type: str
  appliance_id:
    description:
    - ID of the appliance.
    - Parameters I(appliance_id) and I(appliance_name) are mutually exclusive.
    - Parameter I(is_ssh_enabled) has to be passed along with I(appliance_id).
    type: str
  appliance_name:
    description:
    - Name of the appliance.
    - Parameters I(appliance_id) and I(appliance_name) are mutually exclusive.
    - Parameter I(is_ssh_enabled) has to be passed along with I(appliance_name).
    type: str
  is_ssh_enabled:
    description:
    - Whether SSH access is enabled for the cluster.
    - Either I(appliance_id) or I(appliance_name) is to be passed along with
      I(is_ssh_enabled).
    type: bool
  physical_mtu:
    description:
    - MTU for ethernet ports in the cluster.
    - The MTU can be set between 1500 to 9000.
    type: int
  ignore_network_warnings:
    description:
    - Whether to ignore the network warning about unreachable external network.
    type: bool
  appliances:
    description:
    - Appliance configuration setting during cluster creation.
    - This is mandatory for create cluster operation.
    type: list
    elements: dict
    suboptions:
      link_local_address:
        description:
        - The unique IPv4 address of the appliance and is set by zeroconf.
        type: str
        required: true
      name:
        description:
        - Name of new appliance.
        type: str
      drive_failure_tolerance_level:
        description:
        - Specifies the possible drive failure tolerance levels.
        type: str
        choices: ['Single', 'Double']
  dns_servers:
    description:
    - DNS server addresses in IPv4 format. At least one DNS server should be
      provided.
    - This is mandatory for create cluster operation.
    type: list
    elements: str
  ntp_servers:
    description:
    - NTP server addresses in IPv4 or hostname format. At least one NTP server
      should be provided.
    - This is mandatory for create cluster operation.
    type: list
    elements: str
  physical_switches:
    description:
    - Physical switch setting for a new cluster.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Name of the physical switch.
        type: str
        required: true
      purpose:
        description:
        - Specifies the purpose of the physical switch.
        type: str
        required: true
        choices: ['Data_and_Management', 'Management_Only']
      connections:
        description:
        - specifies the supported connection for the physical switch.
        type: list
        required: true
        elements: dict
        suboptions:
          address:
            description:
            - Specifies the physical switch address in IPv4 or DNS hostname
              format.
            type: str
            required: true
          port:
            description:
            - Specifies the port used for connection to switch.
            type: int
          connect_method:
            description:
            - Specifies the connection method type for the physical Switch.
            type: str
            required: true
            choices: ['SSH', 'SNMPv2c']
          username:
            description:
            - Specifies username to connect a physical switch for SSH connection
              method.
            type: str
          ssh_password:
            description:
            - Specifies SSH password to connect a physical switch.
            type: str
          snmp_community_string:
            description:
            - Specifies C(SNMPv2) community string, if C(SNMPv2) connect method is
              selected.
            type: str
  networks:
    description:
    - Configuration of one or more network(s) based on network type.
    - This is mandatory for create cluster operation.
    type: list
    elements: dict
    suboptions:
      type:
        description:
        - Specifies the type of the network.
        type: str
        required: true
        choices: ['Management', 'Intra_Cluster_Management',
          'Intra_Cluster_Data', 'Storage', 'VMotion', 'File_Mobility']
      vlan_id:
        description:
        - The ID of the VLAN.
        type: int
      prefix_length:
        description:
        - Network prefix length.
        type: int
        required: true
      gateway:
        description:
        - Network gateway in IPv4 format.
        type: str
      cluster_mgmt_address:
        description:
        - New cluster management IP address in IPv4 format.
        type: str
      storage_discovery_address:
        description:
        - New storage discovery IP address in IPv4 format.
        - This can be specified only when configure the storage network type.
        type: str
      addresses:
        description:
        - IP addresses in IPv4 format.
        type: list
        elements: str
        required: true
      purposes:
        description:
        - Purpose of the network.
        - Only applicable for storage network.
        type: list
        elements: str
        choices: ['ISCSI', 'NVMe_TCP', 'File_Mobility']
  vcenters:
    description:
    - Configure vCenter settings when creating cluster.
    - Currently, for vcenters parameter API supports only single element.
    - This is required when creating PowerStore X cluster and optional for
      PowerStore T.
    type: list
    elements: dict
    suboptions:
      address:
        description:
        - IP address of vCenter in IPv4 or hostname format.
        type: str
        required: true
      username:
        description:
        - User name to login to vCenter.
        type: str
        required: true
      password:
        description:
        - Password to login to vCenter.
        type: str
        required: true
      is_verify_server_cert:
        description:
        - Whether or not the connection will be secured with the vcenter SSL
          certificate.
        type: bool
        required: true
      data_center_name:
        description:
        - Name of the data center.
        - This is used to join an existing datacenter in vcenter.
        - This should be specified when creating PowerStore X cluster.
        - Mutually exclusive with I(data_center_id).
        type: str
      data_center_id:
        description:
        - The VMWare ID of datacenter.
        - This is used to join an existing datacenter in vcenter.
        - This should be specified when creating PowerStore X cluster.
        - Mutually exclusive with I(data_center_name).
        type: str
      esx_cluster_name:
        description:
        - Name of the ESXi cluster.
        - This should be specified when creating PowerStore X cluster.
        type: str
      vasa_provider_credentials:
        description:
        - Storage system credentials for vCenter to use for communicating with
          the storage system using VASA.
        type: dict
        required: true
        suboptions:
          username:
            description:
            - Username of the local user account which will be used by vSphere
              to register VASA provider.
            type: str
            required: true
          password:
            description:
            - Password of the local user account which will be used by vSphere
              to register VASA provider.
            type: str
            required: true
  is_http_redirect_enabled:
    description:
    - Whether to redirect the HTTP requests to HTTPS.
    type: bool
  validate_create:
    description:
    - Whether to perform create cluster validate call.
    default: true
    type: bool
  wait_for_completion:
    description:
    - Flag to indicate if the operation should be run synchronously or
      asynchronously.
    - C(true) signifies synchronous execution. By default, create cluster
      operation will run asynchronously.
    default: false
    type: bool
  state:
    description:
    - Define whether the cluster should exist or not.
    - Value C(present) indicates that the cluster should exist on the system.
    - Value C(absent) indicates that the cluster should not exist on the system.
    type: str
    required: true
    choices: ['absent', 'present']

notes:
- Deletion of a cluster is not supported by ansible module.
- The I(check_mode) is not supported.
- Before performing create operation, the default password for admin user and
  service user should be changed.
- For management type network during cluster creation,
  I(storage_discovery_address) and purposes should not be passed.
- The I(vcenters) parameter is mandatory for PowerStore X cluster creation.
- Minimum 3 and 5 addresses are required for management network for PowerStore
  T and X model respectively.
- The C(File_Mobility) purpose is supported only in FootHills Prime and above.
- Parameter I(is_http_redirect_enabled) is supported only in PowerStore FootHills
  Prime and above.
'''

EXAMPLES = r'''
- name: Get the details of cluster using id
  dellemc.powerstore.cluster:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    cluster_id: "0"
    state: "present"

- name: Modify details of cluster using the name
  dellemc.powerstore.cluster:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    cluster_name: "RT-D1320"
    appliance_id: "A1"
    is_ssh_enabled: true
    service_password: "S@mple_password"
    chap_mode: "Disabled"
    new_name: "new_RT-D1320"
    state: "present"

- name: Validate create cluster
  dellemc.powerstore.cluster:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    cluster_name: "RT-D1320"
    ignore_network_warnings: true
    appliances:
      - link_local_address: "1.2.x.x"
        name: "Ansible_cluster"
        derive_failure_tolerance_level: "Double"
    dns_servers:
      - "1.1.x.x"
    ntp_servers:
      - "1.3.x.x"
    networks:
      - type: "Management"
        vlan_id: 0
        prefix_length: 24
        gateway: "1.x.x.x"
        cluster_mgmt_address: "1.x.x.x"
        addresses:
          - "2.x.x.x"
          - "3.x.x.x"
      - type: "Storage"
        vlan_id: 0
        prefix_length: 42
        gateway: "1.x.x.x"
        storage_discovery_address: "1.x.x.x"
        addresses:
          - "2.x.x.x"
          - "3.x.x.x"
        purpose:
          - "ISCSI"
    is_http_redirect_enabled: true
    validate_create: true
    state: "present"

- name: Create cluster
  dellemc.powerstore.cluster:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    cluster_name: "RT-D1320"
    ignore_network_warnings: true
    appliances:
      - link_local_address: "1.2.x.x"
        name: "Ansible_cluster"
        derive_failure_tolerance_level: "Double"
    dns_servers:
      - "1.1.x.x"
    ntp_servers:
      - "1.3.x.x"
    physical_switch:
      - name: "Ansible_switch"
        purpose: "Management_Only"
        connections:
          - address: "1.x.x.x"
            port: 20
            connect_method: "SSH"
            username: "user"
            ssh_password: "password"
    networks:
      - type: "Management"
        vlan_id: 0
        prefix_length: 24
        gateway: "1.x.x.x"
        cluster_mgmt_address: "1.x.x.x"
        addresses:
          - "2.x.x.x"
          - "3.x.x.x"
      - type: "Storage"
        vlan_id: 0
        prefix_length: 42
        gateway: "1.x.x.x"
        storage_discovery_address: "1.x.x.x"
        addresses:
          - "2.x.x.x"
          - "3.x.x.x"
        purpose:
          - "ISCSI"
    vcenters:
      - address: "1.x.x.x"
        username: "user"
        password: "password"
        is_verify_server_cert: true
        vasa_provider_credentials:
          username: "user"
          password: "password"
    is_http_redirect_enabled: true
    wait_for_completion: false
    state: "present"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "true"

job_details:
    description: The job details.
    type: complex
    returned: When asynchronous task is performed.
    contains:
        id:
            description: The ID of the job.
            type: str
    sample: {
        "description_l10n": "Create Cluster.",
        "end_time": "2022-01-06T07:39:05.846+00:00",
        "estimated_completion_time": null,
        "id": "be0d099c-a6cf-44e8-88d7-9be80ccae369",
        "parent_id": null,
        "phase": "Completed",
        "phase_l10n": "Completed",
        "progress_percentage": 100,
        "resource_action": "create",
        "resource_action_l10n": "create",
        "resource_id": "0",
        "resource_name": null,
        "resource_type": "cluster",
        "resource_type_l10n": "cluster",
        "response_body": {
            "id": 0,
            "response_type": "job_create_response"
        },
        "response_status": null,
        "response_status_l10n": null,
        "root_id": "be0d099c-a6cf-44e8-88d7-9be80ccae369",
        "start_time": "2022-01-06T07:39:05.47+00:00",
        "state": "COMPLETED",
        "state_l10n": "Completed",
        "step_order": 23792565,
        "user": "admin"
    }

cluster_details:
    description: The cluster details.
    type: complex
    returned: When Cluster exists.
    contains:
        id:
            description: The ID of the cluster.
            type: str
        name:
            description: Name of the cluster.
            type: str
        is_ssh_enabled:
            description: Whether or not the ssh is enabled.
            type: bool
        physical_mtu:
            description: MTU for the cluster.
            type: int
        global_id:
            description: The global unique identifier of the cluster.
            type: str
        management_address:
            description: The floating management IP address for the cluster in
                         IPv4 or IPv6 format.
            type: str
        storage_discovery_address:
            description: The floating storage discovery IP address for the
                         cluster in IPv4 or IPv6 format.
            type: str
        master_appliance_id:
            description: The unique identifier of the appliance acting as
                         primary. This parameter is deprecated in version
                         2.0.0.0.
            type: str
        primary_appliance_id:
            description: The unique identifier of the appliance acting as
                         primary. This parameter was added in version 2.0.0.0.
            type: str
        appliance_count:
            description: Number of appliances configured in this cluster.
            type: int
        is_encryption_enabled:
            description: Whether or not Data at Rest Encryption is enabled on
                         the cluster.
            type: bool
        compatibility_level:
            description: The behavioral version of the software version API,
                         It is used to ensure the compatibility across
                         potentially different software versions.
            type: int
        state:
            description: Possible cluster states.
            type: str
        system_time:
            description: Current clock time for the system. System time and
                         all the system reported times are in UTC (GMT+0:00)
                         format.
            type: str
        service_config_details:
            description: Details of the service config for the entered
                         appliance.
            type: complex
            returned: When is_ssh_enabled is passed in the playbook task
            contains:
                id:
                    description: Id of the service configuration.
                    type: str
                appliance_id:
                    description: Id of the appliance for which the service
                                 configuration exists.
                    type: str
                is_ssh_enabled:
                    description: Whether the ssh is enabled for the appliance
                                 or not.
                    type: bool
        service_user_details:
            description: Details of the service user for which the password
                         can be updated.
            type: complex
            returned: when the cluster exists.
            contains:
                id:
                    description: Id of the service user.
                    type: str
                name:
                    description: Name of the service user.
                    type: str
                is_default_password:
                    description: Whether the service user has default password
                                 or not.
                    type: bool
                is_built_in:
                    description: Whether the service user is built in or not.
                    type: bool
        appliance_details:
            description: Name and Id of the appliance for which I(is_ssh_enabled)
                         parameter is used.
            type: complex
            returned: When appliance name or id is passed in the playbook
                      task.
            contains:
                id:
                    description: Id of the appliance.
                    type: str
                name:
                    description: Name of the appliance.
                    type: str
    sample: {
        "appliance_count": 1,
        "chap_mode": "Disabled",
        "compatibility_level": 10,
        "global_id": "PS00d01e1bb312",
        "id": 0,
        "is_encryption_enabled": true,
        "management_address": "1.2.3.4",
        "master_appliance_id": "A1",
        "name": "WN-D8977",
        "physical_mtu": 1500,
        "service_config_details": null,
        "state": "Configured",
        "state_l10n": "Configured",
        "storage_discovery_address": "10.230.42.228",
        "system_time": "2022-02-04T11:18:37.441Z"
    }
'''

from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import utils
from ansible.module_utils.basic import AnsibleModule
import copy

LOG = utils.get_logger('cluster')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/2.1.0'


class PowerStoreCluster(object):
    """Class with cluster configuration operations"""

    def __init__(self):
        """ Define all parameters required by this module"""

        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_cluster_parameters())

        # initialize the ansible module
        mut_ex_args = [
            ['cluster_name', 'cluster_id'],
            ['appliance_name', 'appliance_id']
        ]
        required_together = [['appliances', 'networks', 'dns_servers',
                              'ntp_servers']]
        required_one_of = [['cluster_name', 'cluster_id']]
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mut_ex_args,
            required_together=required_together,
            required_one_of=required_one_of
        )

        msg = 'HAS_PY4PS = {0} , IMPORT_ERROR = {1}'.format(HAS_PY4PS,
                                                            IMPORT_ERROR)
        LOG.info(msg)

        if not HAS_PY4PS:
            self.module.fail_json(msg=IMPORT_ERROR)
        msg = 'IS_SUPPORTED_PY4PS_VERSION = {0} , VERSION_ERROR = {1}' \
            .format(IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR)
        LOG.info(msg)

        if not IS_SUPPORTED_PY4PS_VERSION:
            self.module.fail_json(msg=VERSION_ERROR)

        # result is a dictionary that contains changed status and
        # cluster details
        self.result = {"changed": False, "cluster_details": {}}

        self.conn = utils.get_powerstore_connection(
            self.module.params, application_type=APPLICATION_TYPE)
        self.configuration = self.conn.config_mgmt
        self.provisioning = self.conn.provisioning
        msg = 'Got Py4Ps instance for configuring cluster on' \
              ' PowerStore {0}'.format(self.conn)
        LOG.info(msg)

    def get_cluster_details(self, cluster_name=None, cluster_id=None):
        """
        Get the cluster details
        """
        try:
            cluster_details = None
            if cluster_name:
                cluster_details = \
                    self.configuration.get_cluster_by_name(cluster_name)
                if cluster_details:
                    cluster_details = cluster_details[0]

            if cluster_id:
                cluster_details =\
                    self.configuration.get_cluster_details(
                        cluster_id=cluster_id)
            return cluster_details
        except Exception as e:
            name_or_id = cluster_name if cluster_name else cluster_id
            msg = 'Get details of cluster {0} failed' \
                  ' with error: {1}'.format(name_or_id, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def show_cluster_details(self, cluster_id, appliance_id):
        """
        Show the details of the cluster.
        """
        cluster_details = self.get_cluster_details(
            cluster_id=cluster_id)
        chap_config_details = self.get_chap_config_details()
        if cluster_details:
            cluster_details['chap_mode'] = chap_config_details['mode']
            cluster_details['service_config_details'] = None
            if appliance_id:
                cluster_details['service_config_details'] = \
                    self.configuration.get_service_config_details(appliance_id)
                cluster_details['service_user_details'] = \
                    self.get_service_user_details()
                appliance_details = self.get_appliance_details(
                    appliance_id, None)
                cluster_details['appliance_details'] = {}
                cluster_details['appliance_details']['id'] =\
                    appliance_details['id']
                cluster_details['appliance_details']['name'] =\
                    appliance_details['name']

        return cluster_details

    def modify_cluster(self, cluster_id, service_config_id,
                       modify_dict=None):
        """
        Update the parameters for clusters.
        """
        try:
            if 'name' in modify_dict.keys():
                self.configuration.modify_cluster(cluster_id,
                                                  name=modify_dict['name'])
            if 'physical_mtu' in modify_dict.keys():
                self.configuration.modify_cluster(
                    cluster_id, physical_mtu=modify_dict['physical_mtu'])
            if 'service_password' in modify_dict.keys():
                self.configuration.modify_service_user(
                    '1', password=modify_dict['service_password'])
            if 'is_ssh_enabled' in modify_dict.keys() and service_config_id:
                self.configuration.modify_service_config(
                    service_config_id,
                    is_ssh_enabled=modify_dict['is_ssh_enabled'])
            if 'chap_mode' in modify_dict.keys():
                self.configuration.modify_chap_config(
                    '0', mode=modify_dict['chap_mode'])
        except Exception as e:
            msg = 'Modify operation failed' \
                  ' with error: {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_chap_config_details(self):
        """
        Get the details of chap config.
        """
        try:
            # The ID of the CHAP config will always be 0
            return \
                self.configuration.get_chap_config_details(chap_config_id='0')

        except Exception as e:
            msg = 'Get details of chap config with id = 0 failed' \
                  ' with error: {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_service_user_details(self):
        """
        Get the details of the service user
        """
        try:
            # There can be only one service user with name as
            # 'service' and id as '1'. This can not be changed or updated.
            return self.configuration.get_service_user_details(
                service_user_id='1')
        except Exception as e:
            msg = 'Get details of service user with id: 1 and name: service' \
                  ' failed with error: {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_service_config_details(self, appliance_id):
        """
        Get the service config details
        """
        try:
            return self.configuration.get_service_config_by_appliance_id(
                appliance_id)[0]
        except Exception as e:
            msg = 'Get details of service config for appliance with id: {0}' \
                  ' failed with error: {1}'.format(appliance_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_appliance_details(self, appliance_id, appliance_name):
        """
        Get the appliance details
        """
        try:
            if appliance_name:
                appliance_details = self.configuration.get_appliance_by_name(
                    appliance_name)
                if appliance_details:
                    return appliance_details[0]
            if appliance_id:
                return self.configuration.get_appliance_details(appliance_id)
            return None

        except Exception as e:
            msg = 'Get appliance details failed with error: {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def prepare_network_payload(self, networks):
        """
        To remove storage_discovery_address and purposes key form management type
        network
        :param networks: List of dict of networks for cluster
        """
        for net_dict in networks:
            if net_dict['type'] == 'Management' and \
                    ('storage_discovery_address' in net_dict
                     or 'purposes' in net_dict):
                if net_dict['storage_discovery_address'] is not None or \
                        net_dict['purposes'] is not None:
                    error_msg = "storage_discovery_address and purposes " \
                                "should not be provided for management " \
                                "type network."
                    self.module.fail_json(msg=error_msg)
                else:
                    del net_dict['storage_discovery_address']
                    del net_dict['purposes']
                    break
            elif net_dict['type'] == 'Storage' and \
                    'cluster_mgmt_address' in net_dict:
                del net_dict['cluster_mgmt_address']
                break
            elif net_dict['type'] == 'VMotion' and \
                    ('cluster_mgmt_address' in net_dict or
                     'storage_discovery_address' in net_dict or
                     'purpose' in net_dict):
                del net_dict['cluster_mgmt_address']
                del net_dict['storage_discovery_address']
                del net_dict['purposes']
                break

    def create_cluster_validate(self, cluster_name):
        """Create cluster validation operation"""

        ignore_network_warnings = self.module.params['ignore_network_warnings']
        dns_servers = self.module.params['dns_servers']
        ntp_servers = self.module.params['ntp_servers']
        is_http_redirect_enabled = self.module.params['is_http_redirect_enabled']

        clusters = dict()
        clusters['name'] = cluster_name
        clusters['ignore_network_warnings'] = ignore_network_warnings
        appliances = copy.deepcopy(self.module.params['appliances'])
        physical_switches = copy.deepcopy(self.module.params['physical_switches'])
        networks = copy.deepcopy(self.module.params['networks'])
        vcenters = self.module.params['vcenters']

        if networks is not None:
            self.prepare_network_payload(networks)

        try:
            # cluster create validate operation
            LOG.info("Validating the new cluster configurations.")
            resp = self.configuration.cluster_create_validate(
                cluster=clusters, appliances=appliances,
                dns_servers=dns_servers, ntp_servers=ntp_servers,
                networks=networks,
                is_http_redirect_enabled=is_http_redirect_enabled,
                physical_switches=physical_switches, vcenters=vcenters)
            LOG.info("response of validate create %s ", str(resp))
            return True, resp
        except Exception as e:
            msg = "Validation of create cluster {0} failed with " \
                  "{1}".format(cluster_name, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def create_cluster(self, cluster_name, wait_for_completion):
        """ Create the new cluster"""

        ignore_network_warnings = self.module.params['ignore_network_warnings']
        dns_servers = self.module.params['dns_servers']
        ntp_servers = self.module.params['ntp_servers']
        is_http_redirect_enabled = self.module.params['is_http_redirect_enabled']

        clusters = dict()
        clusters['name'] = cluster_name
        clusters['ignore_network_warnings'] = ignore_network_warnings
        appliances = copy.deepcopy(self.module.params['appliances'])
        physical_switches = copy.deepcopy(
            self.module.params['physical_switches'])
        networks = copy.deepcopy(self.module.params['networks'])
        vcenters = self.module.params['vcenters']

        if networks is not None:
            self.prepare_network_payload(networks)

        if wait_for_completion:
            is_async = False
        else:
            is_async = True

        try:
            # cluster create operation
            LOG.info("Creating new cluster configurations.")
            job_dict = self.configuration.cluster_create(
                cluster=clusters, appliances=appliances,
                dns_servers=dns_servers, ntp_servers=ntp_servers,
                networks=networks,
                is_http_redirect_enabled=is_http_redirect_enabled,
                physical_switches=physical_switches, vcenters=vcenters,
                is_async=is_async)
            LOG.info("response is: %s", str(job_dict))
            return True, job_dict
        except Exception as e:
            err_msg = "Cluster {0} creation failed with " \
                      "{1}".format(cluster_name, str(e))
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg, **utils.failure_codes(e))

    def validate_vcenters_params(self):
        """Validate vCenters parameters"""

        vcenters = self.module.params['vcenters']

        if vcenters:
            for vcenter in vcenters:
                if 'address' in vcenter and vcenter['address'] is not None and \
                        len(vcenter['address'].strip()) == 0:
                    err_msg = "Provide valid address for new " \
                              "vcenter configuration."
                    self.module.fail_json(msg=err_msg)
                if 'data_center_name' in vcenter and \
                        'data_center_id' in vcenter and \
                        vcenter['data_center_name'] is not None and \
                        vcenter['data_center_id'] is not None:
                    err_msg = "parameters are mutually exclusive: " \
                              "data_center_name|data_center_id"
                    self.module.fail_json(msg=err_msg)

    def validate_addresses_params(self, net_dict):
        """
        Validate the addresses related params
        """
        param_list = ['cluster_mgmt_address', 'storage_discovery_address']
        for param in param_list:
            if param in net_dict and net_dict[param] is not None and \
                    (len(net_dict[param].strip()) == 0 or
                     " " in net_dict[param]):
                err_msg = "Provide valid {0}.".format(param)
                self.module.fail_json(msg=err_msg)

    def validate_networks_params(self):
        """Validate Networks parameters"""

        networks = self.module.params['networks']
        if networks:
            for net_dict in networks:
                if 'addresses' in net_dict and \
                        net_dict['type'] == 'Management' and \
                        len(net_dict['addresses']) < 3:
                    err_msg = "For Management network, minimum 3 addresses " \
                              "for PowerStore T and minimum 5 addresses for" \
                              " PowerStore X should be provided."
                    self.module.fail_json(msg=err_msg)
                if net_dict['type'] == 'Management' and \
                        ('cluster_mgmt_address' not in net_dict or
                         net_dict['cluster_mgmt_address'] is None):
                    err_msg = "The cluster_mgmt_address should be provided" \
                              " for Management type network."
                    self.module.fail_json(msg=err_msg)
                self.validate_addresses_params(net_dict)

    def validate_connections_dict(self, connections):
        """Validate connections dict parameters"""

        for connect_dict in connections:
            if 'address' in connect_dict and connect_dict['address'] is not None and \
                    len(connect_dict['address'].strip()) == 0:
                error_msg = "The address should be provided" \
                            " in connections."
                self.module.fail_json(msg=error_msg)
            if connect_dict['connect_method'] == "SSH" and \
                    (connect_dict['username'] is None or
                     connect_dict['ssh_password'] is None):
                error_msg = "username/ssh_password should be provided with " \
                            "SSH connect_method"
                self.module.fail_json(msg=error_msg)
            if connect_dict['connect_method'] == "SNMPv2c" and \
                    not connect_dict['snmp_community_string']:
                error_msg = "snmp_community_string should be provided with " \
                            "SNMPv2c connect_method"
                self.module.fail_json(msg=error_msg)

    def validate_physical_switch_params(self):
        """ Validate physical switch parameters"""

        physical_switches = self.module.params['physical_switches']
        if physical_switches:
            for switch_list in physical_switches:
                if 'name' in switch_list and \
                        utils.is_param_empty(switch_list['name']):
                    err_msg = "Provide valid physical switch name."
                    self.module.fail_json(msg=err_msg)
                connections = switch_list['connections']
                if len(connections) == 0:
                    error_msg = "connections details should be present in " \
                                "physical_switches."
                    self.module.fail_json(msg=error_msg)
                self.validate_connections_dict(connections)

    def validate_ntp_or_dns(self):
        """validate the NTP and DNS server addresses"""

        dns_servers = self.module.params['dns_servers']
        ntp_servers = self.module.params['ntp_servers']

        if dns_servers is not None and len(dns_servers) > 3:
            err_msg = "Maximum three address should be provided for" \
                      " dns_servers."
            self.module.fail_json(msg=err_msg)

        if ntp_servers is not None and len(ntp_servers) > 3:
            err_msg = "Maximum three address should be provided for" \
                      " ntp_servers."
            self.module.fail_json(msg=err_msg)

    def validate_create_parameters(self):
        """Validate the input parameters"""

        # Check for space
        if utils.is_param_empty(self.module.params['cluster_name']):
            error_msg = "Provide valid {0}".format('cluster_name')
            self.module.fail_json(msg=error_msg)

        self.validate_ntp_or_dns()

        appliances = self.module.params['appliances']
        if appliances:
            for app_dict in appliances:
                if 'link_local_address' in app_dict and \
                        (len(app_dict['link_local_address'].strip()) == 0 or
                         " " in app_dict['link_local_address']):
                    error_msg = "Provide valid link_local_address for " \
                                "an appliance."
                    self.module.fail_json(msg=error_msg)

                if 'name' in app_dict and \
                        utils.is_param_empty(app_dict['name']):
                    error_msg = "Provide valid name of an appliance."
                    self.module.fail_json(msg=error_msg)
        self.validate_physical_switch_params()
        self.validate_networks_params()
        self.validate_vcenters_params()

    def get_cluster_list(self):
        """
        Getting list of cluster to filter create and create validate operation
        """
        try:
            LOG.info("Getting list of clusters.")
            clusters = self.provisioning.get_cluster_list()
            return clusters
        except Exception as e:
            error_msg = "Getting list of clusters failed with error: " \
                        "{0}".format(str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def perform_module_operation(self):
        """
        Perform different actions on cluster module based on parameters
        chosen in playbook
        """

        cluster_id = self.module.params['cluster_id']
        cluster_name = self.module.params['cluster_name']
        is_ssh_enabled = self.module.params['is_ssh_enabled']
        chap_mode = self.module.params['chap_mode']
        service_password = self.module.params['service_password']
        physical_mtu = self.module.params['physical_mtu']
        new_name = self.module.params['new_name']
        state = self.module.params['state']
        appliance_name = self.module.params['appliance_name']
        appliance_id = self.module.params['appliance_id']
        validate_create = self.module.params['validate_create']
        wait_for_completion = self.module.params['wait_for_completion']

        changed = False
        create_changed = False
        cluster_details = {}
        validate_resp = {}
        job_dict = {}

        clusters = self.get_cluster_list()
        self.validate_create_parameters()

        # if is_ssh_enabled is passed and appliance name/id is not passed.
        if not (appliance_id or appliance_name) and is_ssh_enabled is not None:
            self.module.fail_json(
                msg='Either appliance id or appliance name is needed along'
                    ' with is_ssh_enabled parameter. Please enter a valid'
                    ' appliance id/name')
        # if appliance name/id is passed and is_ssh_enabled is not passed.
        if is_ssh_enabled is None and (appliance_id or appliance_name):
            self.module.fail_json(
                msg='is_ssh_enabled parameter is also needed along with '
                    'appliance id/name. Please enter a valid is_ssh_enabled '
                    'value.')
        # Getting the service_config_id from the appliance details
        # for updating is_ssh_enabled.
        service_config_id = None
        if appliance_id or appliance_name:
            appliance_details = self.get_appliance_details(
                appliance_id, appliance_name)
            if not appliance_details:
                self.module.fail_json(
                    msg="Unable to fetch the appliance details. Please provide"
                        " a valid appliance_name.")
            elif appliance_details:
                service_config_id = appliance_details['id']
                appliance_id = appliance_details['id']

        if clusters is not None and clusters[0]['name'] is not None:
            cluster_details = self.get_cluster_details(cluster_name, cluster_id)
        if cluster_details and 'id' in cluster_details and cluster_name:
            cluster_id = cluster_details['id']

        # Validate create cluster operation
        if state == 'present' and not cluster_details:
            if validate_create:
                changed, validate_resp = self.\
                    create_cluster_validate(cluster_name)
            else:
                # Create cluster operation
                create_changed, job_dict = self.\
                    create_cluster(cluster_name, wait_for_completion)

        if state == 'absent' and cluster_details:
            self.module.fail_json(
                msg="Invalid operation. Deletion of the existing cluster is "
                    "currently not supported by the module.")

        # cluster details with all the parameters needed for modify
        if clusters is not None and clusters[0]['name'] is not None:
            cluster_details = self.show_cluster_details(cluster_id, appliance_id)

        if state == 'present' and cluster_details:
            update_params_dict = modify_payload(
                cluster_details, new_name, physical_mtu, service_password,
                chap_mode, is_ssh_enabled)
            if update_params_dict:
                self.modify_cluster(cluster_id, service_config_id,
                                    update_params_dict)
                changed = True

        if state == 'present' and not wait_for_completion and create_changed \
                and not validate_create:
            self.result["changed"] = create_changed
            self.result["job_details"] = job_dict
        elif state == 'present' and changed and validate_create and \
                clusters[0]['name'] is None:
            self.result["changed"] = changed
            self.result["cluster_details"] = {}
            self.result['validate_response'] = validate_resp
        else:
            self.result["changed"] = changed
            self.result["cluster_details"] = self.\
                show_cluster_details(cluster_id, appliance_id)
        self.module.exit_json(**self.result)


def modify_payload(cluster_details, new_name=None, physical_mtu=None,
                   service_password=None, chap_mode=None, is_ssh_enabled=None):
    """
    Dictionary containing all the parameters which are to be updated
    :param cluster_details: The details of the cluster
    :param physical_mtu: MTU for the cluster
    :param new_name: New name for the cluster
    :param service_password: new password for the service user
    :param chap_mode: CHAP mode
    :param is_ssh_enabled: To enable ssh for the service users or not
    :return: Returns payload_dict, includes parameters which are to be updated
    """
    payload = {}
    if service_password is not None:
        payload['service_password'] = service_password
    if physical_mtu is not None and\
            physical_mtu != int(cluster_details['physical_mtu']):
        payload['physical_mtu'] = physical_mtu
    if new_name is not None and new_name != "" and\
            cluster_details['name'].lower() != new_name.lower():
        payload['name'] = new_name
    if chap_mode and \
            (not cluster_details['chap_mode'] or
             (chap_mode.lower() != cluster_details['chap_mode'].lower())):
        payload['chap_mode'] = chap_mode
    if cluster_details['service_config_details'] is not None:
        service_config_ssh = \
            cluster_details['service_config_details']['is_ssh_enabled']
        if is_ssh_enabled is not None and service_config_ssh != is_ssh_enabled:
            payload['is_ssh_enabled'] = is_ssh_enabled

    return payload


def get_powerstore_cluster_parameters():
    """This method provides parameters required for the ansible cluster
    module on PowerStore"""
    return dict(
        cluster_name=dict(), cluster_id=dict(),
        appliance_name=dict(), appliance_id=dict(),
        service_password=dict(no_log=True),
        chap_mode=dict(choices=['Disabled', 'Single', 'Mutual']),
        is_ssh_enabled=dict(type='bool'), new_name=dict(),
        physical_mtu=dict(type='int'),
        ignore_network_warnings=dict(type='bool'),
        appliances=dict(
            type='list', elements='dict',
            options=dict(
                link_local_address=dict(
                    type='str', required=True),
                name=dict(type='str'),
                drive_failure_tolerance_level=dict(
                    type='str', choices=['Single', 'Double']))),
        dns_servers=dict(type='list', elements='str'),
        ntp_servers=dict(type='list', elements='str'),
        physical_switches=dict(
            type='list', elements='dict', options=dict(
                name=dict(type='str', required=True), purpose=dict(
                    type='str', required=True,
                    choices=['Data_and_Management', 'Management_Only']),
                connections=dict(
                    type='list', elements='dict', required=True, options=dict(
                        address=dict(type='str', required=True),
                        port=dict(type='int'),
                        connect_method=dict(
                            type='str', choices=['SSH', 'SNMPv2c'],
                            required=True), username=dict(type='str'),
                        ssh_password=dict(type='str', no_log=True),
                        snmp_community_string=dict(type='str', no_log=True))))),
        networks=dict(type='list', elements='dict',
                      options=dict(
                          type=dict(
                              type='str', required=True,
                              choices=['Management',
                                       'Intra_Cluster_Management',
                                       'Intra_Cluster_Data', 'Storage',
                                       'VMotion', 'File_Mobility']),
                          vlan_id=dict(type='int'),
                          prefix_length=dict(type='int', required=True),
                          gateway=dict(type='str'),
                          cluster_mgmt_address=dict(type='str'),
                          storage_discovery_address=dict(type='str'),
                          addresses=dict(type='list', elements='str',
                                         required=True),
                          purposes=dict(
                              type='list', elements='str',
                              choices=['ISCSI', 'NVMe_TCP',
                                       'File_Mobility']))),
        vcenters=dict(
            type='list', elements='dict',
            options=dict(
                address=dict(type='str', required=True),
                username=dict(type='str', required=True),
                password=dict(type='str', required=True, no_log=True),
                is_verify_server_cert=dict(type='bool', required=True),
                data_center_name=dict(type='str'),
                data_center_id=dict(type='str'),
                esx_cluster_name=dict(type='str'),
                vasa_provider_credentials=dict(
                    type='dict', required=True, options=dict(
                        username=dict(type='str', required=True),
                        password=dict(type='str', required=True,
                                      no_log=True))))),
        is_http_redirect_enabled=dict(type='bool'),
        validate_create=dict(type='bool', default=True),
        wait_for_completion=dict(type='bool', default=False),
        state=dict(required=True, choices=['present', 'absent'])
    )


def main():
    """ Create cluster config object and perform actions on it
    based on user input from playbook"""

    obj = PowerStoreCluster()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
