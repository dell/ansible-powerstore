# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Snapshot module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockSnapshotApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.snapshot.PowerStoreSnapshot'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    SNAPSHOT_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'volume_group': None,
        'volume': None,
        'snapshot_name': None,
        'snapshot_id': None,
        'new_snapshot_name': None,
        'desired_retention': None,
        'retention_unit': None,
        'expiration_timestamp': None,
        'description': None,
        'state': None,
    }

    SOURCE_VOL_DETAILS = [{
        "appliance_id": "A1",
        "creation_timestamp": "2022-05-17T17:11:37.772532+00:00",
        "description": "",
        "hlu_details": [],
        "host": [],
        "host_group": [],
        "id": "3fa9cb4c-4943-4baf-a420-83019ed7f6dd",
        "is_replication_destination": False,
        "location_history": None,
        "mapped_volumes": [],
        "migration_session_id": None,
        "name": "ansible_vol",
        "nguid": "nguid.d817b2593ea140988ccf09680016ccff",
        "node_affinity": "System_Select_At_Attach",
        "node_affinity_l10n": "System Select At Attach",
        "nsid": 14,
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
            "family_id": "3fa9cb4c-4943-4baf-a420-83019ed7f6dd",
            "is_app_consistent": False,
            "parent_id": None,
            "source_id": None,
            "source_timestamp": None
        },
        "protection_policy": None,
        "protection_policy_id": None,
        "size": 1073741824,
        "state": "Ready",
        "state_l10n": "Ready",
        "type": "Primary",
        "type_l10n": "Primary",
        "volume_groups": [],
        "wwn": "naa.68ccf09800d817b2593ea1409816ccff"
    }]

    SOURCE_VG_DETAILS = [{
        "creation_timestamp": "2022-06-05T06:30:33.206+00:00",
        "description": None,
        "id": "1a18566b-31d4-4c00-bfce-30deeeb08acb",
        "is_importing": False,
        "is_protectable": True,
        "is_replication_destination": False,
        "is_write_order_consistent": False,
        "location_history": None,
        "migration_session_id": None,
        "name": "ansible_vg",
        "placement_rule": "Same_Appliance",
        "protection_data": {
            "copy_signature": None,
            "created_by_rule_id": None,
            "created_by_rule_name": None,
            "creator_type": "User",
            "creator_type_l10n": "User",
            "expiration_timestamp": None,
            "family_id": "1a18566b-31d4-4c00-bfce-30deeeb08acb",
            "is_app_consistent": False,
            "parent_id": None,
            "source_id": None,
            "source_timestamp": None
        },
        "protection_policy": None,
        "protection_policy_id": None,
        "type": "Primary",
        "type_l10n": "Primary",
        "volumes": [
            {
                "id": "75b98ed2-0cc9-4852-ac8a-008b5c9f1606",
                "name": "ansible_vg_vol"
            }
        ]
    }]

    VOL_SNAP_DETAILS = {
        "appliance_id": "A1",
        "creation_timestamp": "2022-06-05T06:37:35.88942+00:00",
        "description": "create_description",
        "hlu_details": [],
        "host": [],
        "host_group": [],
        "id": "83314020-31b7-4e2d-98d4-535a733f35e8",
        "is_replication_destination": False,
        "location_history": None,
        "mapped_volumes": [],
        "migration_session_id": None,
        "name": "ansible_vol_snap",
        "nguid": None,
        "node_affinity": "System_Select_At_Attach",
        "node_affinity_l10n": "System Select At Attach",
        "nsid": None,
        "performance_policy": {
            "id": "default_medium",
            "name": "Medium"
        },
        "performance_policy_id": "default_medium",
        "protection_data": {
            "copy_signature": "141c752b-da7b-4b4a-8a40-b25a95934905",
            "created_by_rule_id": None,
            "created_by_rule_name": None,
            "creator_type": "User",
            "creator_type_l10n": "User",
            "expiration_timestamp": "2022-06-12T06:37:22.628+00:00",
            "family_id": "3fa9cb4c-4943-4baf-a420-83019ed7f6dd",
            "is_app_consistent": False,
            "parent_id": "3fa9cb4c-4943-4baf-a420-83019ed7f6dd",
            "source_id": "3fa9cb4c-4943-4baf-a420-83019ed7f6dd",
            "source_timestamp": "2022-06-05T06:37:35.88942+00:00"
        },
        "protection_policy": None,
        "protection_policy_id": None,
        "size": 1073741824,
        "state": "Ready",
        "state_l10n": "Ready",
        "type": "Snapshot",
        "type_l10n": "Snapshot",
        "volume_groups": [],
        "wwn": None
    }

    VG_SNAP_DETAILS = {
        "creation_timestamp": "2022-06-05T06:43:33.588+00:00",
        "description": "",
        "id": "f3baa2c7-bdef-4b83-8f71-b67c904683ab",
        "is_importing": False,
        "is_protectable": True,
        "is_replication_destination": False,
        "is_write_order_consistent": False,
        "location_history": None,
        "migration_session_id": None,
        "name": "ansible_vg_snap",
        "placement_rule": "Same_Appliance",
        "protection_data": {
            "copy_signature": "f0d865f3-a4db-4f05-ad50-d8eba2b2af45",
            "created_by_rule_id": None,
            "created_by_rule_name": None,
            "creator_type": "User",
            "creator_type_l10n": "User",
            "expiration_timestamp": "2022-06-12T06:43:20.269+00:00",
            "family_id": "1a18566b-31d4-4c00-bfce-30deeeb08acb",
            "is_app_consistent": False,
            "parent_id": "1a18566b-31d4-4c00-bfce-30deeeb08acb",
            "source_id": "1a18566b-31d4-4c00-bfce-30deeeb08acb",
            "source_timestamp": "2022-06-05T06:43:33.588+00:00"
        },
        "protection_policy": None,
        "protection_policy_id": None,
        "type": "Snapshot",
        "type_l10n": "Snapshot",
        "volumes": [
            {
                "id": "5e8ad0c0-7b55-42fd-aa38-01524d42764a",
                "name": "ansible_vg_snap.ansible_vg_vol"
            }
        ]
    }

    VOL_SNAPS = [
        {'id': '83314020-31b7-4e2d-98d4-535a733f35e8', 'name': 'ansible_vol_snap'}
    ]

    VG_SNAPS = [
        {'id': 'f3baa2c7-bdef-4b83-8f71-b67c904683ab', 'name': 'ansible_vg_snap'}
    ]

    @staticmethod
    def get_invalid_desired_retention_days_failed_msg():
        return "Please provide a valid integer as the desired retention between 1 and 31."

    @staticmethod
    def get_invalid_desired_retention_hours_failed_msg():
        return "Please provide a valid integer as the desired retention between 1 and 744."

    @staticmethod
    def get_rename_create_failed_msg():
        return "Invalid param: new_name while creating a new snapshot."
