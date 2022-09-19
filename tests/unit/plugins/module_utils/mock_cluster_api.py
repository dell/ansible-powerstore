# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Cluster module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockClusterApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.cluster.PowerStoreCluster'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    address_1 = "1.xx.xx.xx"
    invalid_address_1 = "1.x x.x x.xx"
    cluster_name = "test-cluster"
    invalid_name = ' '

    NET_DICT = {
        'type': 'Storage',
        'vlan_id': 0,
        'prefix_length': 21,
        'gateway': address_1,
        'storage_discovery_address': invalid_address_1,
        'addresses': [address_1]
    }

    MODIFIED_PARAMS = {
        'cluster_name': cluster_name,
        'ignore_network_warnings': True,
        'appliances': [
            {
                'link_local_address': address_1,
                'name': 'test-appliance',
                'drive_failure_tolerance_level': 'Single'
            }
        ],
        'dns_servers': [address_1],
        'ntp_servers': [address_1],
        'networks': [
            {
                'type': 'Management',
                'vlan_id': 0,
                'prefix_length': 21,
                'gateway': address_1,
                'cluster_mgmt_address': address_1,
                'addresses': [address_1]
            }
        ],
        'validate_create': True,
        'is_http_redirect_enabled': True,
        'state': "present"
    }

    CLUSTER_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'cluster_id': "0",
        'cluster_name': None,
        'appliance_name': None,
        'appliance_id': None,
        'service_password': None,
        'chap_mode': None,
        'is_ssh_enabled': None,
        'physical_mtu': None,
        'new_name': None,
        'appliances': None,
        'physical_switches': None,
        'dns_servers': None,
        'ntp_servers': None,
        'networks': None,
        'vcenters': None,
        'ignore_network_warnings': None,
        'is_http_redirect_enabled': None,
        'validate_create': None,
        'wait_for_completion': None,
        'state': None
    }

    CLUSTER_DETAILS = {
        "appliance_count": 1,
        "chap_mode": "Mutual",
        "compatibility_level": 15,
        "global_id": "PS71eb37fd6121",
        "id": "0",
        "is_encryption_enabled": True,
        "management_address": "10.XX.XX.XX",
        "master_appliance_id": "A1",
        "name": "WX-D9023",
        "physical_mtu": 1500,
        "service_config_details": {
            "appliance_id": "A1",
            "id": "A1",
            "is_ssh_enabled": True},
        "state": "Configured",
        "state_l10n": "Configured",
        "storage_discovery_address": None,
        "system_time": "2022-01-21T06:36:59.050Z"
    }

    APPLIANCE_DETAILS = {
        'id': 'A1',
        'name': 'test-appliance'
    }

    CLUSTER_LIST = [
        {
            "id": "0",
            "name": "WN-ABCD"},
        {
            "id": "0",
            "name": None}
    ]
    CLUSTER_LIST_1 = [
        {
            "id": "0",
            "name": None}
    ]

    @staticmethod
    def delete_cluster_failed_msg():
        return "Deletion of the existing cluster is currently not supported by the module."

    @staticmethod
    def modify_cluster_wo_appliance_failed_msg():
        return "Either appliance id or appliance name is needed"

    @staticmethod
    def modify_cluster_with_is_ssh_enabled_wo_appliance_failed_msg():
        return "is_ssh_enabled parameter is also needed along with appliance id/name"

    @staticmethod
    def modify_cluster_failed_msg():
        return "Modify operation failed with error"

    @staticmethod
    def get_cluster_list_failed_msg():
        return "Getting list of clusters failed with error"

    @staticmethod
    def cluster_addr_less_3_failed_msg():
        return "For Management network, minimum 3 addresses for PowerStore"

    @staticmethod
    def dns_ntp_more_than_3_failed_msg():
        return "Maximum three address should be provided"

    @staticmethod
    def link_local_address_failed_msg():
        return "Provide valid link_local_address"

    @staticmethod
    def appliance_name_failed_msg():
        return "Provide valid name of an appliance"

    @staticmethod
    def not_address_failed_msg():
        return "The address should be provided"

    @staticmethod
    def invalid_cluster_name_failed_msg():
        return "Provide valid "

    @staticmethod
    def invalid_vcenter_address_failed_msg():
        return "Provide valid address for new vcenter configuration"

    @staticmethod
    def invalid_switch_name_failed_msg():
        return "Provide valid physical switch name."

    @staticmethod
    def invalid_empty_connections_failed_msg():
        return "connections details should be present in physical_switches."

    @staticmethod
    def without_mgmt_cluster_address_failed_msg():
        return "The cluster_mgmt_address should be provided for Management"

    @staticmethod
    def invalid_cluster_address_failed_msg():
        return "Provide valid cluster_mgmt_address"

    @staticmethod
    def invalid_storage_address_failed_msg():
        return "Provide valid storage_discovery_address"

    @staticmethod
    def storage_address_in_mgmt_network_failed_msg():
        return "storage_discovery_address and purposes should not be " \
               "provided for management"

    @staticmethod
    def appliance_failed_msg():
        return "Unable to fetch the appliance details"

    @staticmethod
    def service_user_failed_msg():
        return "Get details of service user with id"

    @staticmethod
    def data_center_name_id_failed_msg():
        return "parameters are mutually " \
               "exclusive: data_center_name|data_center_id"
