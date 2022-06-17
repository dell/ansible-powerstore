# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Filesystem Snapshot module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockFilesystemSnapshotApi:
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    FILESYSTEM_SNAPSHOT_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'snapshot_id': None,
        'snapshot_name': None,
        'nas_server': None,
        'filesystem': None,
        'desired_retention': None,
        'retention_unit': None,
        'description': None,
        'expiration_timestamp': None,
        'access_type': None,
        'state': None
    }

    FS_SNAP_1 = "Sample_FS_Snapshot_1"
    FS_ID = "61e4947b-8992-3db7-2859-aa02b52a0308"
    NAS_ID = "6026056b-5405-0e36-7697-c285b9fa42b7"
    create_time = "2022-01-16T21:58:02+00:00"
    expire_time = "2022-01-17T00:58:00+00:00"

    FILESYSTEM_SNAP_DETAILS = [
        {
            "access_policy": None,
            "access_policy_l10n": None,
            "access_type": "Snapshot",
            "access_type_l10n": "Snapshot",
            "creation_timestamp": create_time,
            "creator_type": "User",
            "creator_type_l10n": "User",
            "default_hard_limit": None,
            "default_soft_limit": None,
            "description": None,
            "expiration_timestamp": expire_time,
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

    CREATE_FS_SNAPSHOT = [
        {
            "access_policy": None,
            "access_policy_l10n": None,
            "access_type": "Protocol",
            "access_type_l10n": "Protocol",
            "creation_timestamp": create_time,
            "creator_type": "User",
            "creator_type_l10n": "User",
            "default_hard_limit": None,
            "default_soft_limit": None,
            "description": None,
            "expiration_timestamp": expire_time,
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
            "name": "Sample_FS_Snapshot_1",
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

    MODIFY_FS_SNAPSHOT = [
        {
            "access_policy": None,
            "access_policy_l10n": None,
            "access_type": "Snapshot",
            "access_type_l10n": "Snapshot",
            "creation_timestamp": create_time,
            "creator_type": "User",
            "creator_type_l10n": "User",
            "default_hard_limit": None,
            "default_soft_limit": None,
            "description": 'Description',
            "expiration_timestamp": expire_time,
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

    @staticmethod
    def get_fs_snapshot_without_nas_failed_msg():
        return "Please provide filesystem or NAS server details along with snapshot name"
