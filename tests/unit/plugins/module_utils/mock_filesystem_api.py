# Copyright: (c) 2022, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of Filesystem module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockFilesystemApi:

    FILESYSTEM_COMMON_ARGS = {
        "array_ip": '**.***.**.***',
        "filesystem_id": None,
        "filesystem_name": None,
        "nas_server": None,
        "access_policy": None,
        "size": None,
        "cap_unit": None,
        "protection_policy": None,
        "locking_policy": None,
        "description": None,
        "folder_rename_policy": None,
        "smb_properties": None,
        "quota_defaults": None,
        "state": None,
        "config_type": None,
        "is_async_mtime_enabled": None,
        "file_events_publishing_mode": None,
        "flr_attributes": None,
        "host_io_size": None,
        "clone_filesystem": None,
        "snapshot_name": None,
        "snapshot_id": None,
        "refresh_filesystem": None,
        "restore_filesystem": None,
        "backup_snap_name": None
    }

    FS_NAME = "sample_filesystem"
    FS_ID = "621fb793-5e18-b998-462d-a6cb1f6ffcd6"
    NAS_NAME = "ansible_nas_server_2"
    NAS_ID = "6026056b-5405-0e36-7697-c285b9fa42b7"
    DESCRIPTION1 = "FS Testing"
    FILESYSTEM_TYPE = "Primary File system"
    SNAP_ID = "6026056b-5405-0e36-7697-c4523fa42b7"

    FS_DETAILS_1 = [{
        "access_policy": "UNIX",
        "access_policy_l10n": "UNIX",
        "access_type": None,
        "access_type_l10n": None,
        "config_type": "General",
        "config_type_l10n": "General",
        "creation_timestamp": None,
        "creator_type": None,
        "creator_type_l10n": None,
        "default_hard_limit": 10737418240,
        "default_soft_limit": 8589934592,
        "description": DESCRIPTION1,
        "expiration_timestamp": None,
        "file_events_publishing_mode": None,
        "file_events_publishing_mode_l10n": None,
        "filesystem_type": "Primary",
        "filesystem_type_l10n": FILESYSTEM_TYPE,
        "flr_attributes": {
            "auto_delete": False,
            "auto_lock": False,
            "clock_time": None,
            "default_retention": "0D",
            "has_protected_files": False,
            "maximum_retention": "0D",
            "maximum_retention_date": None,
            "minimum_retention": "0D",
            "mode": "None",
            "policy_interval": 0
        },
        "folder_rename_policy": "All_Forbidden",
        "folder_rename_policy_l10n": "All Renames Forbidden",
        "grace_period": 2592000,
        "host_io_size": None,
        "host_io_size_l10n": None,
        "id": "621fb793-5e18-b998-462d-a6cb1f6ffcd6",
        "is_async_MTime_enabled": False,
        "is_modified": None,
        "is_quota_enabled": True,
        "is_smb_no_notify_enabled": True,
        "is_smb_notify_on_access_enabled": True,
        "is_smb_notify_on_write_enabled": True,
        "is_smb_op_locks_enabled": True,
        "is_smb_sync_writes_enabled": True,
        "last_refresh_timestamp": None,
        "last_writable_timestamp": None,
        "locking_policy": "Advisory",
        "locking_policy_l10n": "Advisory",
        "name": "sample_filesystem",
        "nas_server": {
            "id": "6026056b-5405-0e36-7697-c285b9fa42b7",
            "name": "ansible_nas_server_2"
        },
        "parent_id": None,
        "protection_policy": {
            "id": "ebba2048-5ec5-4c5d-9632-e4e4d80c43d6",
            "name": "sample_protection_policy"
        },
        "size_total": 10737418240,
        "size_used": 1621098496,
        "smb_notify_on_change_dir_depth": 1,
        "snapshots": {},
        "total_size_with_unit": "10.0 GB",
        "used_size_with_unit": "1.51 GB"
    }]

    FILESYSTEM_SNAP_DETAILS = [
        {
            "access_policy": None,
            "access_policy_l10n": None,
            "access_type": "Snapshot",
            "access_type_l10n": "Snapshot",
            "creation_timestamp": "2022-01-17T00:58:00+00:00",
            "creator_type": "User",
            "creator_type_l10n": "User",
            "default_hard_limit": None,
            "default_soft_limit": None,
            "description": None,
            "expiration_timestamp": "2022-01-17T00:58:00+00:00",
            "filesystem_type": "Snapshot",
            "filesystem_type_l10n": "Snapshot",
            "folder_rename_policy": None,
            "folder_rename_policy_l10n": None,
            "grace_period": None,
            "id": "61e49f3f-9b57-e69b-1038-aa02b52a030f",
            "is_async_MTime_enabled": False,
            "is_modified": False,
            "is_quota_enabled": None,
            "is_smb_no_notify_enabled": None,
            "is_smb_notify_on_access_enabled": None,
            "is_smb_notify_on_write_enabled": None,
            "is_smb_op_locks_enabled": None,
            "is_smb_sync_writes_enabled": None,
            "last_refresh_timestamp": None,
            "last_writable_timestamp": None,
            "locking_policy": None,
            "locking_policy_l10n": None,
            "name": "Sample_FS_Snapshot",
            "nas_server": {
                "id": "6026056b-5405-0e36-7697-c285b9fa42b7",
                "name": "ansible_nas_server_2"
            },
            "parent_id": "61e4947b-8992-3db7-2859-aa02b52a0308",
            "parent_name": "sample-filesystem",
            "protection_policy": None,
            "size_total": "214748364800",
            "size_used": "1621098496",
            "smb_notify_on_change_dir_depth": 0
        }
    ]

    MODIFY_FS_DETAILS = [{
        "access_policy": "Native",
        "access_policy_l10n": "Native",
        "access_type": None,
        "access_type_l10n": None,
        "config_type": "General",
        "config_type_l10n": "General",
        "creation_timestamp": None,
        "creator_type": None,
        "creator_type_l10n": None,
        "default_hard_limit": 3298534883328,
        "default_soft_limit": 2199023255552,
        "description": None,
        "expiration_timestamp": None,
        "file_events_publishing_mode": True,
        "file_events_publishing_mode_l10n": True,
        "filesystem_type": "Primary",
        "filesystem_type_l10n": FILESYSTEM_TYPE,
        "flr_attributes": {
            "auto_delete": False,
            "auto_lock": False,
            "clock_time": None,
            "default_retention": "15D",
            "has_protected_files": False,
            "maximum_retention": "30D",
            "maximum_retention_date": None,
            "minimum_retention": "10D",
            "mode": "Enterprise",
            "policy_interval": 0
        },
        "folder_rename_policy": "SMB_Forbidden",
        "folder_rename_policy_l10n": "Renames via SMB Forbidden",
        "grace_period": 1209600,
        "host_io_size": None,
        "host_io_size_l10n": None,
        "id": "621fb793-5e18-b998-462d-a6cb1f6ffcd6",
        "is_async_MTime_enabled": True,
        "is_modified": None,
        "is_quota_enabled": True,
        "is_smb_no_notify_enabled": False,
        "is_smb_notify_on_access_enabled": False,
        "is_smb_notify_on_write_enabled": False,
        "is_smb_op_locks_enabled": False,
        "is_smb_sync_writes_enabled": False,
        "last_refresh_timestamp": None,
        "last_writable_timestamp": None,
        "locking_policy": "Mandatory",
        "locking_policy_l10n": "Mandatory",
        "name": "sample_filesystem",
        "nas_server": {
            "id": "6026056b-5405-0e36-7697-c285b9fa42b7",
            "name": "ansible_nas_server_2"
        },
        "parent_id": None,
        "protection_policy": None,
        "size_total": 4398046511104,
        "size_used": 1621098496,
        "smb_notify_on_change_dir_depth": 3,
        "snapshots": {},
        "total_size_with_unit": "4.0 TB",
        "used_size_with_unit": "1.51 GB"
    }]

    CLUSTER_DETAILS = [
        {
            "id": "0",
            "name": "WN-ABCD"},
        {
            "id": "1",
            "name": "WN-WXYZ"}

    ]

    NAS_SERVER_DETAILS = [
        {
            "backup_IPv4_interface_id": None,
            "backup_IPv6_interface_id": None,
            "current_node": {
                "id": "N2",
                "name": "WN-D8978-appliance-1-node-B"
            },
            "current_node_id": "WN-D8978-appliance-1-node-B",
            "current_preferred_IPv4_interface_id": "60260575-67fb-d21a-f0db-c285b9fa42b7",
            "current_preferred_IPv6_interface_id": None,
            "current_unix_directory_service": "LDAP",
            "current_unix_directory_service_l10n": "LDAP",
            "default_unix_user": None,
            "default_windows_user": None,
            "description": "",
            "file_interfaces": [
                {
                    "id": "60260575-67fb-d21a-f0db-c285b9fa42b7",
                    "ip_address": "10.2x.4x.5x",
                    "name": "PROD001_ceffdd03ff93_3"
                }
            ],
            "file_ldaps": [
                {
                    "id": "621c89df-3a51-aef5-63c0-a6cb1f6ffcd6"
                }
            ],
            "file_nises": [],
            "file_systems": [],
            "id": "6026056b-5405-0e36-7697-c285b9fa42b7",
            "is_auto_user_mapping_enabled": True,
            "is_username_translation_enabled": False,
            "name": "ansible_nas_server_2",
            "nfs_servers": [
                {
                    "id": "6026059a-b80b-cc44-ebc3-c214cc45e61c"
                }
            ],
            "operational_status": "Started",
            "operational_status_l10n": "Started",
            "preferred_node": {
                "id": "N1",
                "name": "WN-D8978-appliance-1-node-A"
            },
            "preferred_node_id": "WN-D8978-appliance-1-node-A",
            "production_IPv4_interface_id": None,
            "production_IPv6_interface_id": None,
            "smb_servers": [
                {
                    "id": "6088df61-c32e-429e-bc69-dadf01876de0"
                }
            ]
        }
    ]

    PROTECTION_POLICY_DETAILS = [
        {
            'description': None,
            'id': 'ebba2048-5ec5-4c5d-9632-e4e4d80c43d6',
            'name': 'sample_protection_policy',
            'replication_rules': [],
            'snapshot_rules': [
                {
                    'id': '4db27abe-08cf-427d-a95b-e7a51216b0cf',
                    'name': 'sample_snapshot_rule'
                }
            ]
        }
    ]

    @staticmethod
    def create_filesystem_with_size_less_than_3_failed_msg():
        return "Size must be minimum of 3GB"

    @staticmethod
    def create_filesystem_without_size_failed_msg():
        return "cap_unit can be specified along with size"

    @staticmethod
    def filesystem_with_invalid_default_hard_limit():
        return "default_hard_limit cannot be less than '0'"

    @staticmethod
    def exception_messages(action_type):
        if action_type == "modify_filesystem":
            return 'Failed to modify filesystem id 621fb793-5e18-b998-462d-a6cb1f6ffcd6 with error '
        elif action_type == "delete_filesystem":
            return 'Failed to delete filesystem id 621fb793-5e18-b998-462d-a6cb1f6ffcd6 with error '
        elif action_type == "create_filesystem":
            return 'Create FileSystem with name sample_filesystem on powerstore array name : WN-ABCD , global id : 0 failed with error  '
        elif action_type == "get_nas_server":
            return 'Get NAS Server 6026056b-5405-0e36-7697-c285b9fa42b7 for powerstore array name : WN-ABCD , global id : 0 failed with error  '
        elif action_type == "get_protection_policy":
            return 'Get details of protection policy name or ID : 4db27abe-08cf-427d-a95b-e7a51216b0cf failed with error :  '
        elif action_type == "get_filesystem_no_nas":
            return "Get NAS Server 6026056b-5405-0e36-7697-c285b9fa42b7 for powerstore array name : WN-ABCD , global id : 0 failed with error" \
                   " Failed to get NAS Server with id or name 6026056b-5405-0e36-7697-c285b9fa42b7 from powerstore system "
        elif action_type == "fs_snapshot":
            return "Failed to get filesystem snapshot"
        elif action_type == "clone_filesystem":
            return "Cloning filesystem failed with error"
        elif action_type == "refresh_filesystem":
            return "Refreshing filesystem failed with error"
        elif action_type == "restore_filesystem":
            return "Restoring filesystem failed with error"
