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

    REPLICATION_SESSION_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'volume_group': None,
        'volume': None,
        'session_id': None,
        'session_state': None
    }

    REPLICATION_SESSION_DETAILS = [
        {
            "estimated_completion_timestamp": None,
            "id": "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
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
            "id": "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
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
            "id": "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
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

    SESSION_IDS_VOLUME = [
        {'id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc"}
    ]

    SESSION_IDS_VOLUME_GROUP = [
        {'id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bd"}
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

    REPLICATION_SESSION_DETAILS_SYNC = [
        {
            "estimated_completion_timestamp": None,
            "id": "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
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
            "id": "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
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
            "id": "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
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
            ]
        }
    ]

    REPLICATION_SESSION_DETAILS_PAUSED_DES = [
        {
            "estimated_completion_timestamp": None,
            "id": "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
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
            ]
        }
    ]

    REPLICATION_SESSION_DETAILS_FAILING_OVER = [
        {
            "estimated_completion_timestamp": None,
            "id": "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
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
            "id": "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
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
            "id": "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
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
            "id": "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
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
            "id": "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
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
