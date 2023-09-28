# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of NAS server module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockNasServerApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.nasserver.PowerStoreNasServer'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'
    NAS_SERVER_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'nas_server_name': None,
        'nas_server_id': None,
        'description': None,
        'state': None,
        'nas_server_new_name': None,
        'current_node': None,
        'preferred_node': None,
        'current_unix_directory_service': None,
        'default_unix_user': None,
        'default_windows_user': None,
        'protection_policy': None
    }
    NAS_SERVER_NAME_1 = "Sample_nas_server_1"
    NAS_SERVER_ID = "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9"
    PROTECTION_POLICY_DETAILS = [{
        "description": None,
        "id": "bce845ea-78ba-4414-ada1-8130f3a49e74",
        "name": "Sample_protection_policy",
        "replication_rules": [{
            "id": "7ec83605-bed4-4e2b-8405-504a614db318",
            "name": "sample_replication_rule"
        }],
        "snapshot_rules": [],
        "type": "Protection"
    }]

    CLUSTERS = [{
        "id": "bce845ea-78ba-4414-ada1-8130f3a49e74",
        "name": "cluster_1",
    }]

    NAS_SERVER_DETAILS = [{
        "backup_IPv4_interface_id": None,
        "backup_IPv6_interface_id": None,
        "current_node": {
            "id": "N2",
            "name": "Appliance-XXXXXXX-node-B"
        },
        "current_node_id": "Appliance-XXXXXXX-node-B",
        "current_preferred_IPv4_interface_id": "60c02-b5d8-9d9b-7e6f-feb93c9",
        "current_preferred_IPv6_interface_id": None,
        "current_unix_directory_service": "LDAP",
        "current_unix_directory_service_l10n": "LDAP",
        "default_unix_user": None,
        "default_windows_user": None,
        "description": "",
        "file_interfaces":
        [
            {
                "id": "0c05652-b5d8-9d9b-7e6f-fe8be1eb93c9",
                "ip_address": "X.X.X.X",
                "name": "PROD001_xxxxxxxx08a9_6"
            }
        ],
        "file_ldaps":
        [
            {
                "id": "60c05ba8-362e-159a-0205-ee6f605dfe5a"
            }
        ],
        "file_nises": [],
        "file_systems": [
            {
                "id": "61c55b57-4a70-08dd-a240-96e8abdcbab0",
                "name": "sample_fs"
            }
        ],
        "id": "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
        "is_auto_user_mapping_enabled": True,
        "is_username_translation_enabled": False,
        "name": "Sample_nas_server_1",
        "nfs_servers": [
            {
                "id": "60c05653-4fd3-2033-2da0-ee6f605dfe5a"
            }
        ],
        "operational_status": "Started",
        "operational_status_l10n": "Started",
        "preferred_node": {
            "id": "N2",
            "name": "Appliance-XXXXXXX-node-B"
        },
        "preferred_node_id": "Appliance-XXXXXXX-node-B",
        "production_IPv4_interface_id": "60c05652-b5d8-9d9b-7e6f-fe8be1eb93c",
        "production_IPv6_interface_id": None,
        "protection_policy_id": None,
        "smb_servers": [
            {
                "id": "60c05c18-6806-26ae-3b0d-fe8be1eb93c"
            }
        ]
    }]

    NAS_SERVER_2_DETAILS = [{
        "backup_IPv4_interface_id": None,
        "backup_IPv6_interface_id": None,
        "current_node": {
            "id": "N2",
            "name": "Appliance-XXXXXXX-node-B"
        },
        "current_node_id": "Appliance-XXXXXXX-node-B",
        "current_preferred_IPv4_interface_id": "60c02-b5d8-9d9b-7e6f-feb93c9",
        "current_preferred_IPv6_interface_id": None,
        "current_unix_directory_service": "LDAP",
        "current_unix_directory_service_l10n": "LDAP",
        "default_unix_user": None,
        "default_windows_user": None,
        "description": "",
        "file_interfaces":
        [
            {
                "id": "0c05652-b5d8-9d9b-7e6f-fe8be1eb93c9",
                "ip_address": "X.X.X.X",
                "name": "PROD001_xxxxxxxx08a9_6"
            }
        ],
        "file_ldaps":
        [
            {
                "id": "60c05ba8-362e-159a-0205-ee6f605dfe5a"
            }
        ],
        "file_nises": [],
        "file_systems": [
            {
                "id": "61c55b57-4a70-08dd-a240-96e8abdcbab0",
                "name": "sample_fs"
            }
        ],
        "id": "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
        "is_auto_user_mapping_enabled": True,
        "is_username_translation_enabled": False,
        "name": "Sample_nas_server_2",
        "nfs_servers": [
            {
                "id": "60c05653-4fd3-2033-2da0-ee6f605dfe5a"
            }
        ],
        "operational_status": "Started",
        "operational_status_l10n": "Started",
        "preferred_node": {
            "id": "N2",
            "name": "Appliance-XXXXXXX-node-B"
        },
        "preferred_node_id": "Appliance-XXXXXXX-node-B",
        "production_IPv4_interface_id": "60c05652-b5d8-9d9b-7e6f-fe8be1eb93c",
        "production_IPv6_interface_id": None,
        "protection_policy_id": "bce845ea-78ba-4414-ada1-8130f3a49e74",
        "smb_servers": [
            {
                "id": "60c05c18-6806-26ae-3b0d-fe8be1eb93c"
            }
        ]
    }]

    NODE_DETAILS = [
        {
            'id': 'N1',
            'name': 'Appliance-XXXXXXX-node-A'},
        {
            'id': 'N2',
            'name': 'Appliance-XXXXXXX-node-B'}
    ]

    CLUSTER_DETAILS = [
        {
            "id": "0",
            "name": "WN-ABCD"},
        {
            "id": "1",
            "name": "WN-WXYZ"}
    ]

    @staticmethod
    def create_nas_server_failed_msg():
        return "Creating NAS server " + MockNasServerApi.NAS_SERVER_NAME_1 + " failed with error "

    @staticmethod
    def modify_nas_server_failed_msg():
        return "Failed to modify nasserver"

    @staticmethod
    def delete_nas_server_failed_msg():
        return "Deleting NAS server " + MockNasServerApi.NAS_SERVER_ID + " failed with error"
