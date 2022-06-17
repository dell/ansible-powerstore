# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Cluster module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockClusterApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.cluster.PowerStoreCluster'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

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

    @staticmethod
    def get_cluster_failed_msg():
        return "Creation of cluster is currently not supported"

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
