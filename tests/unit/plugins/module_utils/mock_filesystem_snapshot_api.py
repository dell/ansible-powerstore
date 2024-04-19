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

    ERROR_MAP = {
        "vet": "Incorrect date format, should be YYYY-MM-DDTHH:MM:SSZ",
        "vdr_err1": "Please provide a valid integer as the desired retention between 1 and 744.",
        "vdr_err2": "Please provide a valid integer as the desired retention between 1 and 31.",
        "nse_err1": "Failed to get details of NAS server nas_server_name with error Please provide valid NAS server details",
        "nse_err2": "Failed to get details of NAS server nas_server_name with error",
        "nfe_err1": "Failed to get the filesystem sample_filesystem by name with error Filesystem sample_filesystem not found on the array.",
        "nfe_err2": "Failed to get the filesystem sample_filesystem by name with error Please provide NAS Server details along with filesystem",
        "fs_name_exp": "Filesystem 61e4947b-8992-3db7-2859-aa02b52a0308 not found on the array",
        "fs_snap_exp1": "Please provide filesystem or NAS server details along with snapshot name.",
        "fs_snap_exp2": "Given filesystem 61e4947b-8992-3db7-2859-aa02b52a0318 \
            does not match with the filesystem of the snapshot. Please provide valid filesystem.",
        "fs_snap_exp3": "Failed to get the filesystem snapshot None with error",
        "create_exp1": "Please provide valid snapshot name.",
        "create_exp2": "Snapshot with name sample_snapshot is not found on nas_server nas_server. Please provide filesystem details to create a new snapshot.",
        "create_exp3": "Failed to create snapshot: sample_snapshot",
        "fs_snap_mod_exp1": "Modification of access type is not allowed.",
        "mod_fs_snapshot": "Modify operation of filesystem snapshot with name: Name, id: 61e4947b-8992-3db7-2859-aa02b52a0308 failed with error",
        "del_fs_snapshot": "Delete operation of filesystem snapshot with name: Name, id: 61e4947b-8992-3db7-2859-aa02b52a0308 failed with error",

    }

    MODULE_PATH = "ansible_collections.dellemc.powerstore.plugins.modules.filesystem_snapshot.PowerStoreFilesystemSnapshot"

    @staticmethod
    def get_error_message(key):
        return MockFilesystemSnapshotApi.ERROR_MAP.get(key)
