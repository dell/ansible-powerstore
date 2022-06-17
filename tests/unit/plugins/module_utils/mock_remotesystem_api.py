# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Remote System module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockRemoteSystemApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.remotesystem.PowerstoreRemoteSystem'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'
    sample_address = "xx.xx.xx.xx"
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
        'wait_for_completion': None,
        'description': None
    }

    REMOTE_SYSTEM_DETAILS = [{
        "data_connection_state": "Initializing",
        "data_connection_state_l10n": "Initializing",
        "data_connections": None,
        "data_network_latency": "Low",
        "data_network_latency_l10n": "Low",
        "description": "Adding remote system",
        "discovery_chap_mode": "Disabled",
        "discovery_chap_mode_l10n": "Disabled",
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
