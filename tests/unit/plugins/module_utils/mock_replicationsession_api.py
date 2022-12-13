# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Replication session module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockReplicationSessionApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.replicationsession.PowerstoreReplicationSession'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'
    local_time = "2022-01-06T06:55:01.870946+00:00"
    vg = "Volume Group"
    ID = "b05b5108-26b6-4567-a1d8-1c7795b2e6bc"

    REPLICATION_SESSION_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'volume_group': None,
        'volume': None,
        'nas_server': None,
        'filesystem': None,
        'session_id': None,
        'session_state': None,
        'role': None
    }

    REPLICATION_SESSION_DETAILS = [
        {
            "estimated_completion_timestamp": None,
            "id": ID,
            "last_sync_timestamp": local_time,
            "local_resource_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "local_resource_name": "sample_volume",
            "migration_session": None,
            "progress_percentage": None,
            "remote_resource_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
            "remote_system": {
                "id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
                "name": "WN-D8989"
            },
            "remote_system_id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
            "replication_rule": {
                "id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
                "name": "sample_replication_rule"
            },
            "replication_rule_id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
            "resource_type": "volume",
            "resource_type_l10n": "volume",
            "role": "Destination",
            "role_l10n": "Destination",
            "state": "ok",
            "state_l10n": "ok",
            "storage_element_pairs": [
                {
                    "local_storage_element_id": "b0acb8de-446b-48e4-82ae-89ed05a35d01",
                    "remote_storage_element_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
                    "replication_shadow_id": None,
                    "storage_element_type": "volume"
                }
            ]
        },
        {
            "estimated_completion_timestamp": None,
            "id": "b05b5108-26b6-4567-a1d8-1c7795b2e6bd",
            "last_sync_timestamp": local_time,
            "local_resource_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "local_resource_name": "sample_volume_group",
            "migration_session": None,
            "progress_percentage": None,
            "remote_resource_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
            "remote_system": {
                "id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
                "name": "WN-D8989"
            },
            "remote_system_id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
            "replication_rule": {
                "id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
                "name": "sample_replication_rule"
            },
            "replication_rule_id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
            "resource_type": vg,
            "resource_type_l10n": vg,
            "role": "Destination",
            "role_l10n": "Destination",
            "state": "Paused",
            "state_l10n": "Paused",
            "storage_element_pairs": [
                {
                    "local_storage_element_id": "b0acb8de-446b-48e4-82ae-89ed05a35d01",
                    "remote_storage_element_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
                    "replication_shadow_id": None,
                    "storage_element_type": "volumegroup"
                }
            ]
        }
    ]

    REPLICATION_SESSION_DETAILS_SRC = [
        {
            "estimated_completion_timestamp": None,
            "id": ID,
            "last_sync_timestamp": local_time,
            "local_resource_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "local_resource_name": "sample_volume",
            "migration_session": None,
            "progress_percentage": None,
            "remote_resource_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
            "remote_system": {
                "id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
                "name": "WN-D8989"
            },
            "remote_system_id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
            "replication_rule": {
                "id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
                "name": "sample_replication_rule"
            },
            "replication_rule_id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
            "resource_type": "volume",
            "resource_type_l10n": "volume",
            "role": "Source",
            "role_l10n": "Source",
            "state": "ok",
            "state_l10n": "ok",
            "storage_element_pairs": [
                {
                    "local_storage_element_id": "b0acb8de-446b-48e4-82ae-89ed05a35d01",
                    "remote_storage_element_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
                    "replication_shadow_id": None,
                    "storage_element_type": "volume"
                }
            ]
        },
        {
            "estimated_completion_timestamp": None,
            "id": "b05b5108-26b6-4567-a1d8-1c7795b2e6bd",
            "last_sync_timestamp": local_time,
            "local_resource_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "local_resource_name": "sample_volume_group",
            "migration_session": None,
            "progress_percentage": None,
            "remote_resource_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
            "remote_system": {
                "id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
                "name": "WN-D8989"
            },
            "remote_system_id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
            "replication_rule": {
                "id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
                "name": "sample_replication_rule"
            },
            "replication_rule_id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
            "resource_type": vg,
            "resource_type_l10n": vg,
            "role": "Destination",
            "role_l10n": "Destination",
            "state": "Paused",
            "state_l10n": "Paused",
            "storage_element_pairs": [
                {
                    "local_storage_element_id": "b0acb8de-446b-48e4-82ae-89ed05a35d01",
                    "remote_storage_element_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
                    "replication_shadow_id": None,
                    "storage_element_type": "volumegroup"
                }
            ]
        }
    ]

    REPLICATION_SESSION_DETAILS_VG = [
        {
            "estimated_completion_timestamp": None,
            "id": ID,
            "last_sync_timestamp": local_time,
            "local_resource_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "local_resource_name": "sample_volume_group",
            "migration_session": None,
            "progress_percentage": None,
            "remote_resource_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
            "remote_system": {
                "id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
                "name": "WN-D8989"
            },
            "remote_system_id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
            "replication_rule": {
                "id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
                "name": "sample_replication_rule"
            },
            "replication_rule_id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
            "resource_type": "volume_group",
            "resource_type_l10n": "volume_group",
            "role": "Destination",
            "role_l10n": "Destination",
            "state": "ok",
            "state_l10n": "ok",
            "storage_element_pairs": [
                {
                    "local_storage_element_id": "b0acb8de-446b-48e4-82ae-89ed05a35d01",
                    "remote_storage_element_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
                    "replication_shadow_id": None,
                    "storage_element_type": "volume"
                }
            ]
        },
        {
            "estimated_completion_timestamp": None,
            "id": "b05b5108-26b6-4567-a1d8-1c7795b2e6bd",
            "last_sync_timestamp": local_time,
            "local_resource_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "local_resource_name": "sample_volume_group",
            "migration_session": None,
            "progress_percentage": None,
            "remote_resource_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
            "remote_system": {
                "id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
                "name": "WN-D8989"
            },
            "remote_system_id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
            "replication_rule": {
                "id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
                "name": "sample_replication_rule"
            },
            "replication_rule_id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
            "resource_type": vg,
            "resource_type_l10n": vg,
            "role": "Destination",
            "role_l10n": "Destination",
            "state": "Paused",
            "state_l10n": "Paused",
            "storage_element_pairs": [
                {
                    "local_storage_element_id": "b0acb8de-446b-48e4-82ae-89ed05a35d01",
                    "remote_storage_element_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
                    "replication_shadow_id": None,
                    "storage_element_type": "volumegroup"
                }
            ]
        }
    ]

    REPLICATION_SESSION_DETAILS_NAS_SERVER = [
        {
            "id": "62a9b5c4-f82e-5668-3ea4-4ad525462806",
            "state": "Partial_OK",
            "role": "Destination",
            "resource_type": "nas_server",
            "data_transfer_state": "Asynchronous",
            "type": "Asynchronous",
            "last_sync_timestamp": None,
            "local_resource_id": "629f413b-a583-9fac-a84b-4ad525462806",
            "remote_resource_id": "62a7875c-042d-1885-be35-4ad525462806",
            "remote_system_id": "57384c4e-0018-4464-829c-d567da38fac0",
            "progress_percentage": None,
            "estimated_completion_timestamp": None,
            "replication_rule_id": "ea57f751-d4ea-4f37-9fce-4345d4ac3fb6",
            "last_sync_duration": None,
            "next_sync_timestamp": None,
            "storage_element_pairs": None,
            "failover_test_in_progress": False,
            "error_code": None,
            "data_connection_state": "OK",
            "parent_replication_session_id": None,
            "local_resource_state": None,
            "state_l10n": "Partial OK",
            "role_l10n": "Destination",
            "resource_type_l10n": "NAS Server",
            "data_transfer_state_l10n": "Asynchronous",
            "type_l10n": "Asynchronous",
            "data_connection_state_l10n": "OK",
            "local_resource_state_l10n": None}
    ]

    REPLICATION_SESSION_DETAILS_FILESYSTEM = [
        {
            "id": "62a72cbf-36a0-c57a-04f0-da3630264434",
            "state": "OK",
            "role": "Source",
            "resource_type": "file_system",
            "data_transfer_state": None,
            "type": "Asynchronous",
            "last_sync_timestamp": "2022-07-06T10:25:40+00:00",
            "local_resource_id": "629f3441-b76e-41ca-3f37-4ad525462806",
            "remote_resource_id": "62a72ca3-a95b-4539-0641-da3630264434",
            "remote_system_id": "57384c4e-0018-4464-829c-d567da38fac0",
            "progress_percentage": None,
            "estimated_completion_timestamp": None,
            "replication_rule_id": "ea57f751-d4ea-4f37-9fce-4345d4ac3fb6",
            "last_sync_duration": 2000,
            "next_sync_timestamp": "2022-07-06T11:25:40+00:00",
            "storage_element_pairs": None,
            "failover_test_in_progress": False,
            "error_code": None,
            "data_connection_state": "OK",
            "parent_replication_session_id": "62a72ca3-9efe-ce10-a94f-4ad525462806",
            "local_resource_state": None,
            "state_l10n": "OK",
            "role_l10n": "Source",
            "resource_type_l10n": "File System",
            "data_transfer_state_l10n": None,
            "type_l10n": "Asynchronous",
            "data_connection_state_l10n": "OK",
            "local_resource_state_l10n": None}
    ]

    SESSION_IDS_VOLUME = [
        {'id': ID}
    ]

    SESSION_IDS_VOLUME_GROUP = [
        {'id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bd"}
    ]

    SESSION_IDS_NAS_SERVER = [
        {'id': "62a9b5c4-f82e-5668-3ea4-4ad525462806"}
    ]

    SESSION_IDS_FILESYSTEM = [
        {'id': "62a72cbf-36a0-c57a-04f0-da3630264434"}
    ]

    VOLUME_DETAILS = [{
        "appliance_id": "A1",
        "creation_timestamp": "2022-01-06T05:41:59.381459+00:00",
        "description": "Volume created",
        "hlu_details": [],
        "host": [],
        "host_group": [],
        "id": "634e4b95-e7bd-49e7-957b-6dc932642464",
        "is_replication_destination": False,
        "location_history": None,
        "mapped_volumes": [],
        "migration_session_id": None,
        "name": "sample_volume",
        "nguid": "nguid.ac8ab0e2506d99be8ccf096800e29e40",
        "node_affinity": "System_Select_At_Attach",
        "node_affinity_l10n": "System Select At Attach",
        "nsid": 54768,
        "performance_policy": {
            "id": "default_medium",
            "name": "Medium"
        },
        "performance_policy_id": "default_medium",
        "protection_data": {
            "copy_signature": None,
            "created_by_rule_id": None,
            "created_by_rule_name": None,
            "creator_type": "User",
            "creator_type_l10n": "User",
            "expiration_timestamp": None,
            "family_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "is_app_consistent": False,
            "parent_id": None,
            "source_id": None,
            "source_timestamp": None
        },
        "protection_policy": {
            "id": "4bbb6333-59e4-489c-9015-c618d3e8384b",
            "name": "sample_protection_policy"
        },
        "protection_policy_id": "4bbb6333-59e4-489c-9015-c618d3e8384b",
        "size": 1073741824,
        "state": "Ready",
        "state_l10n": "Ready",
        "type": "Primary",
        "type_l10n": "Primary",
        "volume_groups": [],
        "wwn": "naa.68ccf09800ac8ab0e2506d99bee29e40"
    }]

    VOLUME_GROUP_DETAILS = [
        {
            "creation_timestamp": "2022-01-06T05:41:59.381459+00:00",
            "description": "Volume group created",
            "id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "is_importing": False,
            "is_protectable": True,
            "is_replication_destination": False,
            "is_write_order_consistent": False,
            "location_history": None,
            "mapped_volumes": [],
            "migration_session_id": None,
            "name": "sample_volume_group",
            "placement_rule": "Same_Appliance",
            "protection_data": {
                "copy_signature": None,
                "created_by_rule_id": None,
                "created_by_rule_name": None,
                "creator_type": "User",
                "creator_type_l10n": "User",
                "expiration_timestamp": None,
                "family_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
                "is_app_consistent": False,
                "parent_id": None,
                "source_id": None,
                "source_timestamp": None
            },
            "protection_policy": {
                "id": "4bbb6333-59e4-489c-9015-c618d3e8384b",
                "name": "sample_protection_policy"
            },
            "protection_policy_id": "4bbb6333-59e4-489c-9015-c618d3e8384b",
            "type": "Primary",
            "type_l10n": "Primary",
            "volumes": []
        }
    ]

    NAS_SERVER_DETAILS = [
        {
            "id": "6299d83a-37dc-340b-788f-4ad525462806",
            "name": "sample_nas_server",
            "description": None,
            "operational_status": "Started",
            "current_node_id": "Appliance-RT-D0338-node-B",
            "preferred_node_id": "Appliance-RT-D0338-node-A",
            "default_unix_user": None,
            "default_windows_user": None,
            "current_unix_directory_service": "None",
            "is_username_translation_enabled": False,
            "is_auto_user_mapping_enabled": False,
            "production_IPv4_interface_id": None,
            "production_IPv6_interface_id": None,
            "backup_IPv4_interface_id": None,
            "backup_IPv6_interface_id": None,
            "current_preferred_IPv4_interface_id": "6299d84e-68e0-f4b2-c5e0-4ad525462806",
            "current_preferred_IPv6_interface_id": None,
            "protection_policy_id": "1df04c60-c098-40f2-929d-bb12ee3ea471",
            "file_events_publishing_mode": "None",
            "is_replication_destination": False,
            "is_production_mode_enabled": True,
            "operational_status_l10n": "Started",
            "current_unix_directory_service_l10n": "None",
            "file_events_publishing_mode_l10n": "None"}
    ]

    FILESYSTEM_DETAILS = [
        {
            "id": "629e34ae-2cf1-ca81-8ccd-4ad525462806",
            "name": "File_TEST",
            "description": None,
            "nas_server_id": "6299d83a-37dc-340b-788f-4ad525462806",
            "parent_id": None,
            "filesystem_type": "Primary",
            "size_total": 3221225472,
            "size_used": 1621098496,
            "config_type": "General",
            "protection_policy_id": None,
            "access_policy": "Native",
            "locking_policy": "Advisory",
            "folder_rename_policy": "All_Forbidden",
            "is_smb_sync_writes_enabled": False,
            "is_smb_op_locks_enabled": True,
            "is_smb_no_notify_enabled": False,
            "is_smb_notify_on_access_enabled": False,
            "is_smb_notify_on_write_enabled": False,
            "smb_notify_on_change_dir_depth": 512,
            "is_async_MTime_enabled": False,
            "is_quota_enabled": False,
            "grace_period": 604800,
            "default_hard_limit": 0,
            "default_soft_limit": 0,
            "creation_timestamp": None,
            "expiration_timestamp": None,
            "last_refresh_timestamp": None,
            "last_writable_timestamp": None,
            "is_modified": None,
            "access_type": None,
            "creator_type": None,
            "file_events_publishing_mode": "None",
            "flr_attributes": {
                "mode": "None",
                "minimum_retention": "0D",
                "default_retention": "0D",
                "maximum_retention": "0D",
                "auto_lock": False,
                "auto_delete": False,
                "policy_interval": 0,
                "has_protected_files": False,
                "clock_time": None,
                "maximum_retention_date": None
            },
            "host_io_size": None,
            "filesystem_type_l10n": "Primary File system",
            "config_type_l10n": "General",
            "access_policy_l10n": "Native",
            "locking_policy_l10n": "Advisory",
            "folder_rename_policy_l10n": "All Renames Forbidden",
            "access_type_l10n": None,
            "creator_type_l10n": None,
            "file_events_publishing_mode_l10n": "None",
            "host_io_size_l10n": None}
    ]

    REPLICATION_SESSION_DETAILS_SYNC = [
        {
            "estimated_completion_timestamp": None,
            "id": ID,
            "last_sync_timestamp": local_time,
            "local_resource_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "local_resource_name": "sample_volume",
            "migration_session": None,
            "progress_percentage": None,
            "remote_resource_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
            "remote_system": {
                "id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
                "name": "WN-D8989"
            },
            "remote_system_id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
            "replication_rule": {
                "id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
                "name": "sample_replication_rule"
            },
            "replication_rule_id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
            "resource_type": "Volume",
            "resource_type_l10n": "Volume",
            "role": "Destination",
            "role_l10n": "Destination",
            "state": "synchronizing",
            "state_l10n": "synchronizing",
            "storage_element_pairs": [
                {
                    "local_storage_element_id": "b0acb8de-446b-48e4-82ae-89ed05a35d01",
                    "remote_storage_element_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
                    "replication_shadow_id": None,
                    "storage_element_type": "volume"
                }
            ]
        }
    ]

    REPLICATION_SESSION_DETAILS_SYNC_SRC = [
        {
            "estimated_completion_timestamp": None,
            "id": ID,
            "last_sync_timestamp": local_time,
            "local_resource_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "local_resource_name": "sample_volume",
            "migration_session": None,
            "progress_percentage": None,
            "remote_resource_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
            "remote_system": {
                "id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
                "name": "WN-D8989"
            },
            "remote_system_id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
            "replication_rule": {
                "id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
                "name": "sample_replication_rule"
            },
            "replication_rule_id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
            "resource_type": "Volume",
            "resource_type_l10n": "Volume",
            "role": "Source",
            "role_l10n": "Source",
            "state": "synchronizing",
            "state_l10n": "synchronizing",
            "storage_element_pairs": [
                {
                    "local_storage_element_id": "b0acb8de-446b-48e4-82ae-89ed05a35d01",
                    "remote_storage_element_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
                    "replication_shadow_id": None,
                    "storage_element_type": "volume"
                }
            ]
        }
    ]

    REPLICATION_SESSION_DETAILS_PAUSED = [
        {
            "estimated_completion_timestamp": None,
            "id": ID,
            "last_sync_timestamp": local_time,
            "local_resource_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "local_resource_name": "sample_volume",
            "migration_session": None,
            "progress_percentage": None,
            "remote_resource_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
            "remote_system": {
                "id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
                "name": "WN-D8989"
            },
            "remote_system_id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
            "replication_rule": {
                "id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
                "name": "sample_replication_rule"
            },
            "replication_rule_id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
            "resource_type": "Volume",
            "resource_type_l10n": "Volume",
            "role": "Source",
            "role_l10n": "Source",
            "state": "paused",
            "state_l10n": "paused",
            "storage_element_pairs": [
                {
                    "local_storage_element_id": "b0acb8de-446b-48e4-82ae-89ed05a35d01",
                    "remote_storage_element_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
                    "replication_shadow_id": None,
                    "storage_element_type": "volume"
                }
            ],
            "type": "Asynchronous",
        }
    ]

    METRO_SESSION_DETAILS_PAUSED = [
        {
            "estimated_completion_timestamp": None,
            "id": ID,
            "last_sync_timestamp": local_time,
            "local_resource_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "local_resource_name": "sample_volume",
            "migration_session": None,
            "progress_percentage": None,
            "remote_resource_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
            "remote_system": {
                "id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
                "name": "WN-D8989"
            },
            "remote_system_id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
            "replication_rule": {
                "id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
                "name": "sample_replication_rule"
            },
            "replication_rule_id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
            "resource_type": "Volume",
            "resource_type_l10n": "Volume",
            "role": "Source",
            "role_l10n": "Source",
            "state": "paused",
            "state_l10n": "paused",
            "storage_element_pairs": [
                {
                    "local_storage_element_id": "b0acb8de-446b-48e4-82ae-89ed05a35d01",
                    "remote_storage_element_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
                    "replication_shadow_id": None,
                    "storage_element_type": "volume"
                }
            ],
            "type": "Metro_Active_Active",
        }
    ]

    REPLICATION_SESSION_DETAILS_PAUSED_DES = [
        {
            "estimated_completion_timestamp": None,
            "id": ID,
            "last_sync_timestamp": local_time,
            "local_resource_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "local_resource_name": "sample_volume",
            "migration_session": None,
            "progress_percentage": None,
            "remote_resource_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
            "remote_system": {
                "id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
                "name": "WN-D8989"
            },
            "remote_system_id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
            "replication_rule": {
                "id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
                "name": "sample_replication_rule"
            },
            "replication_rule_id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
            "resource_type": "Volume",
            "resource_type_l10n": "Volume",
            "role": "Destination",
            "role_l10n": "Destination",
            "state": "paused",
            "state_l10n": "paused",
            "storage_element_pairs": [
                {
                    "local_storage_element_id": "b0acb8de-446b-48e4-82ae-89ed05a35d01",
                    "remote_storage_element_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
                    "replication_shadow_id": None,
                    "storage_element_type": "volume"
                }
            ],
            "type": "Asynchronous",
        }
    ]

    REPLICATION_SESSION_DETAILS_FAILING_OVER = [
        {
            "estimated_completion_timestamp": None,
            "id": ID,
            "last_sync_timestamp": local_time,
            "local_resource_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "local_resource_name": "sample_volume",
            "migration_session": None,
            "progress_percentage": None,
            "remote_resource_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
            "remote_system": {
                "id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
                "name": "WN-D8989"
            },
            "remote_system_id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
            "replication_rule": {
                "id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
                "name": "sample_replication_rule"
            },
            "replication_rule_id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
            "resource_type": "Volume",
            "resource_type_l10n": "Volume",
            "role": "Source",
            "role_l10n": "Source",
            "state": "failing_over",
            "state_l10n": "failing_over",
            "storage_element_pairs": [
                {
                    "local_storage_element_id": "b0acb8de-446b-48e4-82ae-89ed05a35d01",
                    "remote_storage_element_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
                    "replication_shadow_id": None,
                    "storage_element_type": "volume"
                }
            ]
        }
    ]

    REPLICATION_SESSION_DETAILS_FAILED_OVER = [
        {
            "estimated_completion_timestamp": None,
            "id": ID,
            "last_sync_timestamp": local_time,
            "local_resource_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "local_resource_name": "sample_volume",
            "migration_session": None,
            "progress_percentage": None,
            "remote_resource_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
            "remote_system": {
                "id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
                "name": "WN-D8989"
            },
            "remote_system_id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
            "replication_rule": {
                "id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
                "name": "sample_replication_rule"
            },
            "replication_rule_id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
            "resource_type": "Volume",
            "resource_type_l10n": "Volume",
            "role": "Source",
            "role_l10n": "Source",
            "state": "failed_over",
            "state_l10n": "failed_over",
            "storage_element_pairs": [
                {
                    "local_storage_element_id": "b0acb8de-446b-48e4-82ae-89ed05a35d01",
                    "remote_storage_element_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
                    "replication_shadow_id": None,
                    "storage_element_type": "volume"
                }
            ]
        }
    ]

    REPLICATION_SESSION_DETAILS_FAILED_OVER_DES = [
        {
            "estimated_completion_timestamp": None,
            "id": ID,
            "last_sync_timestamp": local_time,
            "local_resource_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "local_resource_name": "sample_volume",
            "migration_session": None,
            "progress_percentage": None,
            "remote_resource_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
            "remote_system": {
                "id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
                "name": "WN-D8989"
            },
            "remote_system_id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
            "replication_rule": {
                "id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
                "name": "sample_replication_rule"
            },
            "replication_rule_id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
            "resource_type": "Volume",
            "resource_type_l10n": "Volume",
            "role": "Destination",
            "role_l10n": "Destination",
            "state": "failed_over",
            "state_l10n": "failed_over",
            "storage_element_pairs": [
                {
                    "local_storage_element_id": "b0acb8de-446b-48e4-82ae-89ed05a35d01",
                    "remote_storage_element_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
                    "replication_shadow_id": None,
                    "storage_element_type": "volume"
                }
            ]
        }
    ]

    REPLICATION_SESSION_DETAILS_RESUMING = [
        {
            "estimated_completion_timestamp": None,
            "id": ID,
            "last_sync_timestamp": local_time,
            "local_resource_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "local_resource_name": "sample_volume",
            "migration_session": None,
            "progress_percentage": None,
            "remote_resource_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
            "remote_system": {
                "id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
                "name": "WN-D8989"
            },
            "remote_system_id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
            "replication_rule": {
                "id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
                "name": "sample_replication_rule"
            },
            "replication_rule_id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
            "resource_type": "Volume",
            "resource_type_l10n": "Volume",
            "role": "Source",
            "role_l10n": "Source",
            "state": "resuming",
            "state_l10n": "resuming",
            "storage_element_pairs": [
                {
                    "local_storage_element_id": "b0acb8de-446b-48e4-82ae-89ed05a35d01",
                    "remote_storage_element_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
                    "replication_shadow_id": None,
                    "storage_element_type": "volume"
                }
            ]
        }
    ]

    REPLICATION_SESSION_DETAILS_SYSTEM_PAUSED = [
        {
            "estimated_completion_timestamp": None,
            "id": ID,
            "last_sync_timestamp": local_time,
            "local_resource_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "local_resource_name": "sample_volume",
            "migration_session": None,
            "progress_percentage": None,
            "remote_resource_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
            "remote_system": {
                "id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
                "name": "WN-D8989"
            },
            "remote_system_id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
            "replication_rule": {
                "id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
                "name": "sample_replication_rule"
            },
            "replication_rule_id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
            "resource_type": "Volume",
            "resource_type_l10n": "Volume",
            "role": "Source",
            "role_l10n": "Source",
            "state": "system_paused",
            "state_l10n": "system_paused",
            "storage_element_pairs": [
                {
                    "local_storage_element_id": "b0acb8de-446b-48e4-82ae-89ed05a35d01",
                    "remote_storage_element_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
                    "replication_shadow_id": None,
                    "storage_element_type": "volume"
                }
            ]
        }
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
    def failed_over_to_paused_failed_msg():
        return "replication session is in failed_over state, invalid transition to paused state."

    @staticmethod
    def failing_over_to_paused_failed_msg():
        return "replication session is in failing_over state, invalid transition to paused state."

    @staticmethod
    def change_state_from_transitioning_states_failed_msg():
        return "Replication Session is in resuming state. Please perform paused operation once this transition is completed."

    @staticmethod
    def failed_over_to_sync_destination_failed_msg():
        return "Sync call can not be made at the destination when the session is in failed_over state"

    @staticmethod
    def change_state_from_remaining_states_failed_msg():
        return "Any state change from this state is not supported by ansible module"

    @staticmethod
    def paused_to_sync_dest_error_failed_msg():
        return "Synchronization at destination is not supported."

    @staticmethod
    def volume_not_found_failed_msg():
        return "not found"

    @staticmethod
    def modify_role_failed_msg():
        return "Modifying the role Metro_Preferred of replication session b05b5108-26b6-4567-a1d8-1c7795b2e6bc failed with error"
