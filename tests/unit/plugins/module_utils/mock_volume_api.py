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
        'clone_volume': None,
        'source_volume': None,
        'source_snap': None,
        'create_backup_snap': None,
        'backup_snap_profile': None,
        'remote_system': None,
        'remote_appliance_id': None,
        'end_metro_config': None,
        'delete_remote_volume': None,
        'state': None,
        'app_type': None,
        'app_type_other': None,
        'appliance_name': None,
        'appliance_id': None
    }

    DESCRIPTION1 = 'Volume created'
    NGUID1 = 'nguid.ac8ab0e2506d99be8ccf096800e29e40'
    NODE_AFFINITY1 = 'System_Select_At_Attach'
    WWN_1 = 'naa.68ccf09800ac8ab0e2506d99bee29e40'
    NODE_AFFINITY_2 = 'System Select At Attach'
    EXPIRATION_TIMESTAMP = '2022-12-23T01:20:00Z'
    PERFORMANCE_POLICY_LOW = 'default_low'
    SAMPLE_ADDRESS = "xx.xx.xx.xx"
    REMOTE_SYSTEM_ID = "5ccc6333-59f4-4239c-9215-c6181de8384b"
    REMOTE_SYSTEM_ID_1 = "24dc6333-59f4-4239c-9205-c6181ea8184b"
    REMOTE_SYSTEM_ID_2 = "87dc6677-59a4-4239d-9221-a2524ae9389c"
    ID_1 = "434f534e-7009-4e60-8e1e-5cf721ae40df"

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
            "app_type": "Relational_Databases_Other",
            "app_type_other": "Max_DB",
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
            "metro_replication_session_id": None,
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

    VOL1_SNAPSHOT_LIST = [
        {
            'id': 'fd44444-3333-2222-1111-0000000',
            'name': 'refresh_backup_snap_1'
        }
    ]

    MODIFY_VOL_DETAILS1 = [
        {
            "app_type": None,
            "app_type_other": None,
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
            "metro_replication_session_id": REMOTE_SYSTEM_ID,
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
            "app_type": "Business_Applications_CRM",
            "app_type_other": None,
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
            "metro_replication_session_id": REMOTE_SYSTEM_ID_1,
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
            "app_type": None,
            "app_type_other": None,
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
            "app_type": None,
            "app_type_other": None,
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

    REMOTE_SYSTEM_DETAILS = [{
        "id": REMOTE_SYSTEM_ID,
        "management_address": SAMPLE_ADDRESS,
        "appliance_details": [{
            "appliance_id": "A2"
        }],
        "name": "remote-system"
    }]

    REMOTE_SYSTEM_DETAILS_1 = [
        {
            "id": REMOTE_SYSTEM_ID,
            "management_address": SAMPLE_ADDRESS,
            "appliance_details": [{
                "appliance_id": "A2"
            }],
            "name": "remote-system"
        },
        {
            "id": REMOTE_SYSTEM_ID_2,
            "management_address": SAMPLE_ADDRESS,
            "appliance_details": [{
                "appliance_id": "A2"
            }],
            "name": "remote-system"
        }]

    REP_SESSION_DETAILS = [{
        "remote_system_id": REMOTE_SYSTEM_ID
    }]

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

    @staticmethod
    def get_fail_msg_for_clone_volume(msg_type=None):
        if msg_type == 'exception':
            return "Cloning volume %s failed with error " % (MockVolumeApi.VOL_DETAILS1[0]['id'])
        elif msg_type == 'log_unit_error':
            return "Either of host identifier or host group identifier is required along with logical_unit_number."

    @staticmethod
    def get_fail_msg_for_refresh_volume(msg_type=None):
        if msg_type == 'exception':
            return "Refreshing volume %s failed with error " % (MockVolumeApi.VOL_DETAILS1[0]['id'])
        elif msg_type == 'backup_snap_error':
            return "Specify create_back_snap as True to set backup_snap_profile."
        elif msg_type == 'expiration_timestamp_error':
            return 'Incorrect date format, should be YYYY-MM-DDTHH:MM:SSZ'

    @staticmethod
    def get_fail_msg_for_restore_volume(msg_type=None):
        if msg_type == 'exception':
            return "Restoring volume %s failed with error " % (MockVolumeApi.VOL_DETAILS1[0]['id'])
        elif msg_type == 'snap_exception':
            return "Restoring volume %s failed with error cannot unpack non-iterable NoneType object" % (MockVolumeApi.VOL_DETAILS1[0]['id'])

    @staticmethod
    def configure_metro_fail_msg():
        return "Failed to configure metro for volume sample_volume_1"

    @staticmethod
    def rep_session_fail_msg():
        return "Get metro replication session %s details failed with error:" % (MockVolumeApi.REMOTE_SYSTEM_ID)

    @staticmethod
    def exisiting_metro_session_fail_msg():
        return "Metro session is already configured for the volume"

    @staticmethod
    def no_appliance_fail_msg():
        return "No remote appliance A2 found in remote system"

    @staticmethod
    def remote_system_fail_msg():
        return "Fetching remote system %s failed with error" % (MockVolumeApi.ID_1)

    @staticmethod
    def remote_app_fail_msg():
        return "Fetching remote appliance None failed with error"

    @staticmethod
    def end_metro_fail_msg():
        return "Failed to remove the metro configuration for volume sample_volume_2 with error"
