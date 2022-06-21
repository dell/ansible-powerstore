# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Volume module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockVolumeApi:
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    VOLUME_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'vol_id': None,
        'vol_name': None,
        'vg_name': None,
        'vg_id': None,
        'size': None,
        'cap_unit': None,
        'protection_policy': None,
        'performance_policy': None,
        'description': None,
        'new_name': None,
        'host': None,
        'hostgroup': None,
        'mapping_state': None,
        'hlu': None,
        'state': None
    }

    DESCRIPTION1 = 'Volume created'
    NGUID1 = 'nguid.ac8ab0e2506d99be8ccf096800e29e40'
    NODE_AFFINITY1 = 'System_Select_At_Attach'
    WWN_1 = 'naa.68ccf09800ac8ab0e2506d99bee29e40'
    NODE_AFFINITY_2 = 'System Select At Attach'

    VG_1 = [{
        "description": "Volume group created",
        "id": "fd156da5-d579-43b2-a377-e98af0c6962f",
        "is_protectable": True,
        "is_replication_destination": False,
        "is_write_order_consistent": False,
        "name": "sample_VG",
        "protection_data": {
            "expiration_timestamp": None,
            "family_id": "fd156da5-d579-43b2-a377-e98af0c6962f",
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

    HOST_DETAILS1 = [{
        "description": None,
        "host_group_id": None,
        "host_initiators": [
            {
                "active_sessions": [],
                "chap_mutual_username": "",
                "chap_single_username": "",
                "port_name": "iqn.2015-10.com.dell:dellemc-powerstore-apm0xxxxxxxxxx-a",
                "port_type": "iSCSI"
            }
        ],
        "id": "ced80318-b14a-461d-93a7-11b10afaf349",
        "mapped_hosts": [],
        "name": "sample_host",
        "os_type": "ESXi",
        "os_type_l10n": "ESXi"
    }]

    HG_DETAILS1 = [{
        "description": None,
        "hosts": [
            {
                "id": "ced80318-b14a-461d-93a7-11b10afaf349",
                "name": "sample_host"
            }
        ],
        "id": "d0a61806-0992-4e8b-9419-d47ac1ed563f",
        "name": "sample_host_group"
    }]

    VOL_DETAILS1 = [
        {
            "appliance_id": "A1",
            "description": DESCRIPTION1,
            "hlu_details": [],
            "host": [],
            "host_group": [],
            "id": "ae20eb9a-a482-416e-aaf7-2a3fe7203630",
            "is_replication_destination": False,
            "location_history": None,
            "mapped_volumes": [],
            "migration_session_id": None,
            "name": "sample_volume_1",
            "nguid": NGUID1,
            "node_affinity": NODE_AFFINITY1,
            "node_affinity_l10n": NODE_AFFINITY_2,
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
                "family_id": "fd156da5-d579-43b2-a377-e98af0c6962f",
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
            "volume_groups": [
                {
                    'id': 'fd156da5-d579-43b2-a377-e98af0c6962f',
                    'name': 'sample_VG',
                }
            ],
            "wwn": WWN_1
        }
    ]

    MODIFY_VOL_DETAILS1 = [
        {
            "appliance_id": "A1",
            "description": DESCRIPTION1,
            "hlu_details": [
                {
                    'host_group_id': None,
                    'host_id': 'ced80318-b14a-461d-93a7-11b10afaf349',
                    'id': '506983b8-e490-4bb4-8de7-75717948e93e',
                    'logical_unit_number': 123
                }
            ],
            "host": [
                {
                    'id': 'ced80318-b14a-461d-93a7-11b10afaf349',
                    'name': 'sample_host'
                }
            ],
            "host_group": [
                {
                    'id': 'd0a61806-0992-4e8b-9419-d47ac1ed563f',
                    'name': 'sample_host_group'
                }
            ],
            "id": "ae20eb9a-a482-416e-aaf7-2a3fe7203630",
            "is_replication_destination": False,
            "location_history": None,
            "mapped_volumes": [
                {
                    'id': '506983b8-e490-4bb4-8de7-75717948e93e',
                    'logical_unit_number': 123
                }
            ],
            "migration_session_id": None,
            "name": "sample_volume_1",
            "nguid": NGUID1,
            "node_affinity": NODE_AFFINITY1,
            "node_affinity_l10n": NODE_AFFINITY_2,
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
                "family_id": "fd156da5-d579-43b2-a377-e98af0c6962f",
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
            "volume_groups": [
                {
                    'id': 'fd156da5-d579-43b2-a377-e98af0c6962f',
                    'name': 'sample_VG',
                }
            ],
            "wwn": WWN_1
        }
    ]

    VOL_DETAILS2 = [
        {
            "appliance_id": "A1",
            "description": "Volume 2 created",
            "hlu_details": [],
            "host": [],
            "host_group": [],
            "id": "6b730a66-494a-4aea-88d2-45552bb4adfc",
            "is_replication_destination": False,
            "location_history": None,
            "mapped_volumes": [],
            "migration_session_id": None,
            "name": "sample_volume_2",
            "nguid": NGUID1,
            "node_affinity": NODE_AFFINITY1,
            "node_affinity_l10n": NODE_AFFINITY_2,
            "nsid": 54768,
            "performance_policy": {
                "id": "default_high",
                "name": "High"
            },
            "performance_policy_id": "default_high",
            "protection_data": {
                "copy_signature": None,
                "created_by_rule_id": None,
                "created_by_rule_name": None,
                "creator_type": "User",
                "creator_type_l10n": "User",
                "expiration_timestamp": None,
                "family_id": "fd156da5-d579-43b2-a377-e98af0c6962f",
                "is_app_consistent": False,
                "parent_id": None,
                "source_id": None,
                "source_timestamp": None
            },
            "protection_policy": None,
            "protection_policy_id": None,
            "size": 2147483648,
            "state": "Ready",
            "state_l10n": "Ready",
            "type": "Primary",
            "type_l10n": "Primary",
            "volume_groups": [],
            "wwn": WWN_1
        }
    ]

    TWO_VOL_LIST = [
        {
            "appliance_id": "A1",
            "description": DESCRIPTION1,
            "hlu_details": [],
            "host": [],
            "host_group": [],
            "id": "ae20eb9a-a482-416e-aaf7-2a3fe7203630",
            "is_replication_destination": False,
            "location_history": None,
            "mapped_volumes": [],
            "migration_session_id": None,
            "name": "sample_volume",
            "nguid": NGUID1,
            "node_affinity": NODE_AFFINITY1,
            "node_affinity_l10n": NODE_AFFINITY_2,
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
                "family_id": "fd156da5-d579-43b2-a377-e98af0c6962f",
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
            "wwn": WWN_1
        },
        {
            "appliance_id": "A1",
            "description": "Volume 2 created",
            "hlu_details": [],
            "host": [],
            "host_group": [],
            "id": "6b730a66-494a-4aea-88d2-45552bb4adfc",
            "is_replication_destination": False,
            "location_history": None,
            "mapped_volumes": [],
            "migration_session_id": None,
            "name": "sample_volume",
            "nguid": NGUID1,
            "node_affinity": NODE_AFFINITY1,
            "node_affinity_l10n": NODE_AFFINITY_2,
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
                "family_id": "fd156da5-d579-43b2-a377-e98af0c6962f",
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
            "wwn": WWN_1
        }
    ]

    @staticmethod
    def get_volume_more_than_one_failed_msg():
        return "Multiple volumes by the same name found"

    @staticmethod
    def create_volume_without_size_failed_msg():
        return "Size is a required parameter while creating volume"

    @staticmethod
    def create_volume_with_new_name_failed_msg():
        return "new_name specified for non-existing volume"

    @staticmethod
    def add_host_and_hg_volume_failed_msg():
        return "Only one of host or hostgroup can be mapped to a volume in one call"

    @staticmethod
    def modify_hlu_volume_failed_msg():
        return "Modification of HLU is not supported. Modification of HLU from 123 to 1213 for host ced80318-b14a-461d-93a7-11b10afaf349 was attempted"

    @staticmethod
    def shrink_volume_failed_msg():
        return "Current volume size 2147483648 B is greater than 1073741824 B specified. Only expansion of volume size is allowed"

    @staticmethod
    def map_without_mapping_state_failed_msg():
        return "Mapping state not provided, mandatory for mapping"
