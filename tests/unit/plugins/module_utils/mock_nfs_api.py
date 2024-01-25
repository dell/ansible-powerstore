# Copyright: (c) 2024, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of NFS module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockNfsApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.nfs.PowerStoreNfsExport'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'
    filesystem_path = "/sample_file_system"
    export_path = "10.xx.xx.xx:/sample_nfs_export"
    NFS_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'nfs_export_name': None,
        'nfs_export_id': None,
        'filesystem': None,
        'state': None,
        'snapshot': None,
        'nas_server': None,
        'path': None,
        'description': None,
        'default_access': None,
        'read_only_root_hosts': None,
        'read_only_hosts': None,
        'read_write_hosts': None,
        'read_write_root_hosts': None,
        'min_security': None,
        'anonymous_uid': None,
        'anonymous_gid': None,
        'is_no_suid': None,
        'host_state': None,
        'no_access_hosts': None
    }
    NAS_SERVER_NAME_1 = "Sample_nas_server_1"

    NAS_SERVER_DETAILS = {
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
                "id": "61d68815-1ac2-fc68-7263-96e8abdcbab0",
                "name": "sample_file_system"
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
        "smb_servers": [
            {
                "id": "60c05c18-6806-26ae-3b0d-fe8be1eb93c"
            }
        ]
    }

    NAS_SERVER_DETAILS_2 = {
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
                "id": "61c55b57-4a70-08dd-a240-96e8abdcbab1",
                "name": "sample_fs_2"
            }
        ],
        "id": "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c8",
        "is_auto_user_mapping_enabled": True,
        "is_username_translation_enabled": False,
        "name": "Sample_nas_server_2",
        "nfs_servers": [
            {
                "id": "60c05653-4fd3-2033-2da0-ee6f605dfe5b"
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
        "smb_servers": [
            {
                "id": "60c05c18-6806-26ae-3b0d-fe8be1eb93c"
            }
        ]
    }

    NFS_DETAILS_BY_NAME = [
        {
            "anonymous_GID": -2,
            "anonymous_UID": -2,
            "default_access": "No_Access",
            "default_access_l10n": "No_Access",
            "description": None,
            "export_path": export_path,
            "file_system": {
                "filesystem_type": "Primary",
                "id": "61d68815-1ac2-fc68-7263-96e8abdcbab0",
                "name": "sample_file_system",
                "nas_server": {
                    "id": "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
                    "name": "Sample_nas_server_1"
                }
            },
            "id": "61d6888b-52ed-0d4b-2b35-96e8abdcbab0",
            "is_no_SUID": False,
            "min_security": "Sys",
            "min_security_l10n": "Sys",
            "name": "sample_nfs_export",
            "nfs_owner_username": 0,
            "no_access_hosts": [],
            "path": filesystem_path,
            "read_only_hosts": [],
            "read_only_root_hosts": [],
            "read_write_hosts": [],
            "read_write_root_hosts": []
        }
    ]

    NFS_DETAILS = {
        "anonymous_GID": -2,
        "anonymous_UID": -2,
        "default_access": "No_Access",
        "default_access_l10n": "No_Access",
        "description": None,
        "export_path": export_path,
        "file_system": {
            "filesystem_type": "Primary",
            "id": "61d68815-1ac2-fc68-7263-96e8abdcbab0",
            "name": "sample_file_system",
            "nas_server": {
                "id": "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
                "name": "Sample_nas_server_1"
            }
        },
        "id": "61d6888b-52ed-0d4b-2b35-96e8abdcbab0",
        "is_no_SUID": False,
        "min_security": "Sys",
        "min_security_l10n": "Sys",
        "name": "sample_nfs_export",
        "nfs_owner_username": 0,
        "no_access_hosts": [],
        "path": filesystem_path,
        "read_only_hosts": [],
        "read_only_root_hosts": [],
        "read_write_hosts": [],
        "read_write_root_hosts": []
    }

    NFS_DETAILS_2 = [{
        "anonymous_GID": -2,
        "anonymous_UID": -2,
        "default_access": "No_Access",
        "default_access_l10n": "No_Access",
        "description": None,
        "export_path": export_path,
        "file_system": {
            "filesystem_type": "Primary",
            "id": "61d68815-1ac2-fc68-7263-96e8abdcbab0",
            "name": "sample_file_system",
            "nas_server": {
                "id": "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
                "name": "Sample_nas_server_1"
            }
        },
        "id": "61d6888b-52ed-0d4b-2b35-96e8abdcbab1",
        "is_no_SUID": False,
        "min_security": "Sys",
        "min_security_l10n": "Sys",
        "name": "sample_nfs_export_2",
        "nfs_owner_username": 0,
        "no_access_hosts": ["10.10.10.10"],
        "path": filesystem_path,
        "read_only_hosts": ["10.10.10.11"],
        "read_only_root_hosts": ["10.10.10.12"],
        "read_write_hosts": [],
        "read_write_root_hosts": ["10.10.10.13"]
    }]

    NFS_DETAILS_3 = [{
        "anonymous_GID": -2,
        "anonymous_UID": -2,
        "default_access": "No_Access",
        "default_access_l10n": "No_Access",
        "description": None,
        "export_path": export_path,
        "file_system": {
            "filesystem_type": "Primary",
            "id": "61d68815-1ac2-fc68-7263-96e8abdcbab0",
            "name": "sample_file_system",
            "nas_server": {
                "id": "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
                "name": "Sample_nas_server_1"
            }
        },
        "id": "61d6888b-52ed-0d4b-2b35-96e8abdcbab1",
        "is_no_SUID": False,
        "min_security": "Sys",
        "min_security_l10n": "Sys",
        "name": "sample_nfs_export_3",
        "nfs_owner_username": 0,
        "no_access_hosts": ["2620:0:170:2858:250:12aa:34aa:aaa3"],
        "path": filesystem_path,
        "read_only_hosts": ["2620:0:170:2858:250:12aa:34aa:aaa4"],
        "read_only_root_hosts": ["2620:0:170:2858:250:12aa:34aa:aaa5"],
        "read_write_hosts": [],
        "read_write_root_hosts": ["2620:0:170:2858:250:12aa:34aa:aaa6"]
    }]

    FILESYSTEM_DETAILS_BY_NAME = [{
        "access_policy": "Native",
        "access_policy_l10n": "Native",
        "access_type": None,
        "access_type_l10n": None,
        "creation_timestamp": None,
        "creator_type": None,
        "creator_type_l10n": None,
        "default_hard_limit": 0,
        "default_soft_limit": 0,
        "description": None,
        "expiration_timestamp": None,
        "filesystem_type": "Primary",
        "filesystem_type_l10n": "Primary",
        "folder_rename_policy": "All_Forbidden",
        "folder_rename_policy_l10n": "All Renames Forbidden",
        "grace_period": 604800,
        "id": "61d68815-1ac2-fc68-7263-96e8abdcbab0",
        "is_async_MTime_enabled": False,
        "is_modified": False,
        "is_quota_enabled": False,
        "is_smb_no_notify_enabled": False,
        "is_smb_notify_on_access_enabled": False,
        "is_smb_notify_on_write_enabled": False,
        "is_smb_op_locks_enabled": True,
        "is_smb_sync_writes_enabled": True,
        "last_refresh_timestamp": None,
        "last_writable_timestamp": None,
        "locking_policy": "Advisory",
        "locking_policy_l10n": "Advisory",
        "name": "sample_file_system",
        "nas_server": {
            "id": "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
            "name": "Sample_nas_server_1"
        },
        "parent_id": None,
        "protection_policy": None,
        "size_total": "214748364800",
        "size_used": "1621098496",
        "smb_notify_on_change_dir_depth": 512,
        "snapshots": {},
        "total_size_with_unit": "200.0 GB",
        "used_size_with_unit": "1.51 GB"}
    ]

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
    def get_nfs_export_wo_nas_failed_msg():
        return "Please provide NAS Server details along with filesystem"

    @staticmethod
    def modify_nfs_export_invalid_description_failed_msg():
        return "Please enter a valid description"

    @staticmethod
    def remove_nfs_export_hosts_without_hosts_failed_msg():
        return "Host state is given but hosts are not specified."

    @staticmethod
    def remove_nfs_export_hosts_without_host_state_failed_msg():
        return "Hosts are given but host state is not specified."

    @staticmethod
    def add_invalid_ipv6_hosts_failed_msg():
        return "Along with alphanumeric characters, only special characters allowed are"
