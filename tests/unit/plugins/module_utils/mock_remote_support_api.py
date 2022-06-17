# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Remote Support module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockRemoteSupportApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.remote_support.PowerstoreRemoteSupport'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'
    gateway_type_1 = "SRS Gateway Tier3"
    support_type_1 = "SRS Integrated Tier3"
    REMOTE_SUPPORT_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'remote_support_id': 0,
        'support_type': None,
        'remote_support_servers': None,
        'proxy_address': None,
        'proxy_port': None,
        'proxy_username': None,
        'proxy_password': None,
        'is_support_assist_license_accepted': True,
        'is_cloudiq_enabled': False,
        'is_rsc_enabled': True,
        'is_icw_configured': True,
        'send_test_alert': False,
        'verify_connection': False,
        'server_state': None,
        'wait_for_completion': True,
        'return_support_license_text': False,
        'state': None
    }

    REMOTE_SUPPORT_DETAILS = {
        "id": "0",
        "type": "SRS_Integrated_Tier3",
        "is_cloudiq_enabled": True,
        "is_support_assist_license_accepted": True,
        "is_rsc_enabled": False,
        "connectivity_status": support_type_1,
        "last_update": "2022-02-01T10:47:41.345+00:00",
        "remote_support_servers": [
            {
                "id": "0",
                "remote_support_id": "0",
                "address": "localhost",
                "port": 9443,
                "is_primary": True,
                "connectivity_qos": None},
            {
                "id": "1",
                "remote_support_id": "0",
                "address": None,
                "port": None,
                "is_primary": False,
                "connectivity_qos": None}
        ],
        "proxy_address": None,
        "proxy_port": None,
        "proxy_username": None,
        "policy_manager_address": None,
        "policy_manager_port": None,
        "type_l10n": support_type_1,
        "connectivity_status_l10n": support_type_1
    }

    REMOTE_SUPPORT_DISABLED_DETAILS = {
        "id": "0",
        "type": "Disabled",
        "is_cloudiq_enabled": True,
        "is_support_assist_license_accepted": True,
        "is_rsc_enabled": False,
        "connectivity_status": "Disabled",
        "last_update": "2022-02-02T10:47:41.345+00:00",
        "remote_support_servers": [
            {
                "id": "0",
                "remote_support_id": "0",
                "address": "localhost",
                "port": 9443,
                "is_primary": True,
                "connectivity_qos": None
            },
            {
                "id": "1",
                "remote_support_id": "0",
                "address": None,
                "port": None,
                "is_primary": False,
                "connectivity_qos": None
            }
        ],
        "proxy_address": None,
        "proxy_port": None,
        "proxy_username": None,
        "policy_manager_address": None,
        "policy_manager_port": None,
        "type_l10n": "Disabled",
        "connectivity_status_l10n": "Disabled"
    }

    REMOTE_SUPPORT_GATEWAY1_DETAILS = {
        "id": "0",
        "type": "SRS_Gateway_Tier3",
        "is_cloudiq_enabled": True,
        "is_support_assist_license_accepted": True,
        "is_rsc_enabled": False,
        "connectivity_status": gateway_type_1,
        "last_update": "2022-02-03T10:47:41.345+00:00",
        "remote_support_servers": [
            {
                "id": "0",
                "remote_support_id": "0",
                "address": "10.X.X.X",
                "port": 9443,
                "is_primary": True,
                "connectivity_qos": None},
            {
                "id": "1",
                "remote_support_id": "0",
                "address": None,
                "port": None,
                "is_primary": False,
                "connectivity_qos": None
            }],
        "proxy_address": None,
        "proxy_port": None,
        "proxy_username": None,
        "policy_manager_address": None,
        "policy_manager_port": None,
        "type_l10n": gateway_type_1,
        "connectivity_status_l10n": gateway_type_1
    }

    REMOTE_SUPPORT_GATEWAY2_DETAILS = {
        "id": "0",
        "type": "SRS_Gateway_Tier3",
        "is_cloudiq_enabled": True,
        "is_support_assist_license_accepted": True,
        "is_rsc_enabled": False,
        "connectivity_status": gateway_type_1,
        "last_update": "2022-02-04T10:47:41.345+00:00",
        "remote_support_servers": [
            {
                "id": "0",
                "remote_support_id": "0",
                "address": "10.X.X.X",
                "port": 9443,
                "is_primary": True,
                "connectivity_qos": None},
            {
                "id": "1",
                "remote_support_id": "0",
                "address": "10.X.X.Y",
                "port": 9443,
                "is_primary": False,
                "connectivity_qos": None
            }],
        "proxy_address": None,
        "proxy_port": None,
        "proxy_username": None,
        "policy_manager_address": None,
        "policy_manager_port": None,
        "type_l10n": gateway_type_1,
        "connectivity_status_l10n": gateway_type_1
    }

    REMOTE_SUPPORT_GATEWAY2SAME_DETAILS = {
        "id": "0",
        "type": "SRS_Gateway_Tier3",
        "is_cloudiq_enabled": True,
        "is_support_assist_license_accepted": True,
        "is_rsc_enabled": False,
        "connectivity_status": gateway_type_1,
        "last_update": "2022-02-05T10:47:41.345+00:00",
        "remote_support_servers": [
            {
                "id": "0",
                "remote_support_id": "0",
                "address": "10.X.X.X",
                "port": 9443,
                "is_primary": True,
                "connectivity_qos": None},
            {
                "id": "1",
                "remote_support_id": "0",
                "address": "10.X.X.X",
                "port": 9442,
                "is_primary": False,
                "connectivity_qos": None
            }],
        "proxy_address": None,
        "proxy_port": None,
        "proxy_username": None,
        "policy_manager_address": None,
        "policy_manager_port": None,
        "type_l10n": gateway_type_1,
        "connectivity_status_l10n": gateway_type_1
    }

    REMOTE_SUPPORT_INTEGRATED_DETAILS = {
        "id": "0",
        "type": "SRS_Integrated_Tier3",
        "is_cloudiq_enabled": True,
        "is_support_assist_license_accepted": True,
        "is_rsc_enabled": False,
        "connectivity_status": support_type_1,
        "last_update": "2022-02-05T10:47:41.345+00:00",
        "remote_support_servers": [
            {
                "id": "0",
                "remote_support_id": "0",
                "address": "localhost",
                "port": None,
                "is_primary": True,
                "connectivity_qos": None},
            {
                "id": "1",
                "remote_support_id": "0",
                "address": None,
                "port": None,
                "is_primary": False,
                "connectivity_qos": None
            }],
        "proxy_address": None,
        "proxy_port": None,
        "proxy_username": None,
        "policy_manager_address": None,
        "policy_manager_port": None,
        "type_l10n": support_type_1,
        "connectivity_status_l10n": support_type_1
    }

    @staticmethod
    def get_remote_support_failed_msg():
        return "does not exist"

    @staticmethod
    def delete_remote_support_failed_msg():
        return "Deletion of Remote Support configuration is not supported"

    @staticmethod
    def modify_remote_support_failed_msg():
        return "Failed to modify remote support configuration instance"

    @staticmethod
    def verify_remote_support_failed_msg():
        return "Failed to verify Remote Support configuration instance"

    @staticmethod
    def send_test_remote_support_failed_msg():
        return "Failed to send a test mail for remote support"

    @staticmethod
    def send_test_alert_remote_support_failed_msg():
        return "Failed to send a test mail for remote support"

    @staticmethod
    def modify_remote_support_without_support_type_failed_msg():
        return "Please provide the support_type to modify the configuration"

    @staticmethod
    def verify_remote_support_without_support_type_failed_msg():
        return "remote_support_servers are required with type None"

    @staticmethod
    def modify_remote_support_without_remote_support_servers_failed_msg():
        return "remote_support_servers are required with type"
