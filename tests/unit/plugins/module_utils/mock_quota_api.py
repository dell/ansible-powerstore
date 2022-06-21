# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Quota module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockQuotaApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.quota.PowerStoreQuota'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    QUOTA_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        "path": None,
        "quota_id": None,
        "nas_server": None,
        "filesystem": None,
        "quota_type": None,
        "description": None,
        "windows_name": None,
        "unix_name": None,
        "windows_sid": None,
        "uid": None,
        "quota": {
            'soft_limit': None,
            'hard_limit': None,
            'cap_unit': None
        },
        "state": None
    }

    QUOTA_DETAILS = [{
        "description": "Tree quota created on filesystem",
        "file_system": {
            "filesystem_type": "Primary",
            "id": "61d68a87-6000-3cc3-f816-96e8abdcbab0",
            "name": "sample_file_system",
            "nas_server": {
                "id": "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
                "name": "ansible_nas_server_2"
            }
        },
        "hard_limit(GB)": "90.0",
        "id": "00000006-08f2-0000-0200-000000000000",
        "is_user_quotas_enforced": False,
        "path": "/sample_file_system",
        "remaining_grace_period": -1,
        "size_used": 0,
        "soft_limit(GB)": "50.0",
        "state": "Ok"
    }]

    QUOTA_DETAILS2 = [{
        "description": "Tree quota created on filesystem",
        "file_system": {
            "filesystem_type": "Primary",
            "id": "61d68a87-6000-3cc3-f816-96e8abdcbab0",
            "name": "ansible_PS_SMB_quota_FS1",
            "nas_server": {
                "id": "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
                "name": "ansible_nas_server_2"
            }
        },
        "hard_limit(GB)": "90.0",
        "id": "00000006-08f2-0000-0200-000000000000",
        "is_user_quotas_enforced": False,
        "path": "/ansible_tree_quota_FS1_path2",
        "remaining_grace_period": -1,
        "size_used": 0,
        "soft_limit(GB)": "50.0",
        "state": "Ok"
    }]

    FILESYSTEM_DETAILS1 = [{
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
        "filesystem_type_l10n": "Primary File system",
        "folder_rename_policy": "All_Forbidden",
        "folder_rename_policy_l10n": "All Renames Forbidden",
        "grace_period": 604800,
        "id": "629494e2-f86e-63ef-3d95-827ee627f9b1",
        "is_async_MTime_enabled": False,
        "is_modified": None,
        "is_quota_enabled": True,
        "is_smb_no_notify_enabled": False,
        "is_smb_notify_on_access_enabled": False,
        "is_smb_notify_on_write_enabled": False,
        "is_smb_op_locks_enabled": True,
        "is_smb_sync_writes_enabled": False,
        "last_refresh_timestamp": None,
        "last_writable_timestamp": None,
        "locking_policy": "Advisory",
        "locking_policy_l10n": "Advisory",
        "name": "ansible_PS_SMB_quota_FS1",
        "nas_server": {
            "id": "628619c1-a1ad-b85d-37ae-b2dcd309270e",
            "name": "ansible_nas_server_2"
        },
        "parent_id": None,
        "protection_policy": None,
        "size_total": 107374182400,
        "size_used": 1621098496,
        "smb_notify_on_change_dir_depth": 512,
        "snapshots": {},
        "total_size_with_unit": "100.0 GB",
        "used_size_with_unit": "1.51 GB"
    }]

    NAS_SERVER_DETAILS1 = [{
        "backup_IPv4_interface_id": None,
        "backup_IPv6_interface_id": None,
        "current_node": {
            "id": "N2",
            "name": "Appliance-WND8977-node-B"
        },
        "current_node_id": "Appliance-WND8977-node-B",
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
                "id": "629494e2-f86e-63ef-3d95-827ee627f9b1",
                "name": "ansible_PS_SMB_quota_FS1"
            }
        ],
        "id": "628619c1-a1ad-b85d-37ae-b2dcd309270e",
        "is_auto_user_mapping_enabled": True,
        "is_username_translation_enabled": False,
        "name": "ansible_nas_server_2",
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
    }]
