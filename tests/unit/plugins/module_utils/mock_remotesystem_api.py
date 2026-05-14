# Copyright: (c) 2022, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of Remote System module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockRemoteSystemApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.remotesystem.PowerstoreRemoteSystem'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'
    sample_address = "xx.xx.xx.xx"
    sample_wwn_1 = "58:cc:f0:98:49:21:07:02"
    sample_wwn_2 = "58:cc:f0:98:49:21:07:01"
    REMOTE_SYSTEM_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'remote_id': None,
        'remote_name': None,
        'remote_user': None,
        'state': None,
        'remote_password': None,
        'remote_address': None,
        'new_remote_address': None,
        'remote_port': None,
        'network_latency': None,
        'data_connection_type': None,
        'fc_target_wwns': None,
        'wait_for_completion': None,
        'description': None
    }

    REMOTE_SYSTEM_DETAILS = [{
        "data_connection_state": "Initializing",
        "data_connection_state_l10n": "Initializing",
        "data_connection_type": "iSCSI",
        "data_connection_type_l10n": "iSCSI",
        "data_connections": None,
        "data_network_latency": "Low",
        "data_network_latency_l10n": "Low",
        "description": "Adding remote system",
        "discovery_chap_mode": "Disabled",
        "discovery_chap_mode_l10n": "Disabled",
        "fc_target_wwns": [],
        "id": "aaa3cc6b-455b-4bde-aa75-a1edf61bbe0b",
        "import_sessions": [],
        "iscsi_addresses": [
            sample_address,
            sample_address
        ],
        "management_address": sample_address,
        "name": "XX-1234",
        "replication_sessions": [],
        "serial_number": "PSeba1a5c63d46",
        "session_chap_mode": "Disabled",
        "session_chap_mode_l10n": "Disabled",
        "state": "Ok",
        "state_l10n": "Ok",
        "type": "PowerStore",
        "type_l10n": "PowerStore",
        "user_name": ""
    }]

    FC_REMOTE_SYSTEM_DETAILS = [{
        "data_connection_state": "OK",
        "data_connection_state_l10n": "OK",
        "data_connection_type": "FC",
        "data_connection_type_l10n": "FC",
        "data_connections": None,
        "data_network_latency": "Low",
        "data_network_latency_l10n": "Low",
        "description": "Adding FC remote system",
        "discovery_chap_mode": "Disabled",
        "discovery_chap_mode_l10n": "Disabled",
        "fc_target_wwns": [
            sample_wwn_1,
            sample_wwn_2
        ],
        "id": "bbb4dd7c-566c-5cef-99a6-b2feg72ccf1c",
        "import_sessions": [],
        "iscsi_addresses": [],
        "management_address": sample_address,
        "name": "FC-1234",
        "replication_sessions": [],
        "serial_number": "PSfca2b6d74e57",
        "session_chap_mode": "Disabled",
        "session_chap_mode_l10n": "Disabled",
        "state": "Ok",
        "state_l10n": "Ok",
        "type": "PowerStore",
        "type_l10n": "PowerStore",
        "user_name": ""
    }]

    CLUSTER_DETAILS = [
        {
            "id": "0",
            "name": "WN-ABCD"},
        {
            "id": "1",
            "name": "WN-WXYZ"}
    ]

    @staticmethod
    def create_remotesystem_with_remote_name_failed_msg():
        return "remote_id/remote_name cannot be passed"

    @staticmethod
    def fc_target_wwns_without_fc_type_failed_msg():
        return "fc_target_wwns can only be specified when" \
               " data_connection_type is set to 'FC'."
