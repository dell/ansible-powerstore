# Copyright: (c) 2022, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of Volume Group module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockVolumeGroupApi:
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    VOLUME_GROUP_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'snapshot_id': None,
        'vg_name': None,
        'vg_id': None,
        'protection_policy': None,
        'is_write_order_consistent': None,
        'description': None,
        'new_vg_name': None,
        'volumes': None,
        'vol_state': None,
        'source_snap': None,
        'source_vg': None,
        'create_backup_snap': None,
        'backup_snap_profile': None,
        'vg_clone': None,
        'state': None
    }
    DESCRIPTION1 = 'Volume group created'
    DESCRIPTION2 = 'Volume group modified'
    VOL_DESC = 'Volume created'

    VG_DETAILS = [{
        "description": DESCRIPTION1,
        "id": "634e4b95-e7bd-49e7-957b-6dc932642464",
        "is_protectable": True,
        "is_replication_destination": False,
        "is_write_order_consistent": False,
        "name": "sample_volume_group",
        "protection_data": {
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
    }]

    CREATE_VG = [{
        "description": DESCRIPTION1,
        "id": "634e4b95-e7bd-49e7-957b-6dc932642464",
        "is_importing": False,
        "is_protectable": True,
        "is_replication_destination": False,
        "is_write_order_consistent": True,
        "location_history": None,
        "migration_session_id": None,
        "name": "sample_volume_group_1",
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
    }]

    MODIFY_VG = [{
        "description": DESCRIPTION2,
        "id": "634e4b95-e7bd-49e7-957b-6dc932642464",
        "is_importing": False,
        "is_protectable": True,
        "is_replication_destination": False,
        "is_write_order_consistent": False,
        "location_history": None,
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
        "protection_policy": None,
        "protection_policy_id": None,
        "type": "Primary",
        "type_l10n": "Primary",
        "volumes": [
            {
                'id': 'ae20eb9a-a482-416e-aaf7-2a3fe7203630',
                'name': 'sample_volume_1'
            },
            {
                'id': '6b730a66-494a-4aea-88d2-45552bb4adfc',
                'name': 'sample_volume_2'
            }
        ]
    }]

    PROTECTION_POLICY_DETAILS = [
        {
            'description': None,
            'id': '4bbb6333-59e4-489c-9015-c618d3e8384b',
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

    VOL_DETAILS1 = [
        {
            "appliance_id": "A1",
            "description": VOL_DESC,
            "hlu_details": [],
            "host": [],
            "host_group": [],
            "id": "ae20eb9a-a482-416e-aaf7-2a3fe7203630",
            "is_replication_destination": False,
            "location_history": None,
            "mapped_volumes": [],
            "migration_session_id": None,
            "name": "sample_volume_1",
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
        }
    ]

    VOL_DETAILS2 = [
        {
            "appliance_id": "A1",
            "description": VOL_DESC,
            "hlu_details": [],
            "host": [],
            "host_group": [],
            "id": "6b730a66-494a-4aea-88d2-45552bb4adfc",
            "is_replication_destination": False,
            "location_history": None,
            "mapped_volumes": [],
            "migration_session_id": None,
            "name": "sample_volume_2",
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
        }
    ]

    @staticmethod
    def get_non_existing_volume_failed_msg():
        return "Volume with id 6b730a66-494a-4aea-88d2-45552bb4adfc not found. Please enter a correct volume id"

    @staticmethod
    def refresh_vol_group_ex():
        return "Refreshing volume group 634e4b95-e7bd-49e7-957b-6dc932642464 failed with error"

    @staticmethod
    def restore_vol_group_ex():
        return "Restoring volume group 634e4b95-e7bd-49e7-957b-6dc932642464 failed with error"

    @staticmethod
    def clone_vol_group_ex():
        return "Cloning volume group 634e4b95-e7bd-49e7-957b-6dc932642464 failed with error"
