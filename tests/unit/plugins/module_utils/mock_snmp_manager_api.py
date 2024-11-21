# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of SMNP Manager module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockSNMPManagerApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.snmp_manager.PowerStoreSNMPManager'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    IP_ADDRESS = '1.1.1.1'
    DANGEROUS_STR = "D@ngerous1"

    SNMP_MANAGER_COMMON_ARGS = {
        "array_ip": IP_ADDRESS,
        "state": "present",
        "ip_address": "127.0.0.1",
        "snmp_port": 162,
        "version": "V3",
        "alert_severity": "Info",
        "trap_community": "public",
        "snmp_username": "test123",
        "auth_protocol": "MD5",
        "auth_privacy": "AES256",
        "snmp_password": DANGEROUS_STR,
        "update_password": "on_create"
    }

    GET_SNMP_MANAGER_DETAILS = {
        "id": "967ffb5d-5059-43a6-8377-1b83b99e6470",
        "ip_address": "127.0.0.1",
        "port": 162,
        "version": "V3",
        "trap_community": None,
        "alert_severity": "Info",
        "user_name": "test123",
        "auth_protocol": "MD5",
        "privacy_protocol": "AES256"
    }

    CREATE_SNMP_MANAGER_DETAILS = {
        "id": "967ffb5d-5059-43a6-8377-1b83b99e6470",
        "ip_address": "127.0.0.1",
        "port": 162,
        "version": "V3",
        "trap_community": None,
        "alert_severity": "Critical",
        "user_name": "test123",
        "auth_protocol": "MD5",
        "privacy_protocol": "AES256"
    }

    GET_SNMP_MANAGER_DETAILS_V2 = {
        "id": "967ffb5d-5059-43a6-8377-1b83553e6470",
        "ip_address": "127.0.0.6",
        "port": 162,
        "version": "V2c",
        "trap_community": "Test_community",
        "alert_severity": "Info",
    }

    GET_SNMP_MANAGER_LIST = [
        {
            "alert_severity": "Info",
            "auth_protocol": "MD5",
            "id": "27221b71-7ee9-4759-8308-77e6c8ca4f05",
            "ip_address": "127.0.0.7",
            "port": 162,
            "privacy_protocol": "TDES",
            "trap_community": None,
            "user_name": "admin",
            "version": "V3"
        },
        {
            "id": "967ffb5d-5059-43a6-8377-1b83b99e6470",
            "ip_address": "127.0.0.1",
            "port": 162,
            "version": "V3",
            "trap_community": None,
            "alert_severity": "Info",
            "user_name": "test123",
            "auth_protocol": "MD5",
            "privacy_protocol": "AES256"
        },
        {
            "alert_severity": "Info",
            "auth_protocol": "None",
            "id": "face90f4-aa4d-469f-8844-0930442f71c8",
            "ip_address": "127.0.0.5",
            "port": 162,
            "privacy_protocol": "None",
            "trap_community": None,
            "user_name": "admin",
            "version": "V3"
        }
    ]

    @staticmethod
    def get_snmp_manager_exception_response(response_type):
        if response_type == "create_snmp_manager_exception":
            return "Creation of SNMP Manager on PowerStore array failed with error"
        elif response_type == "delete_snmp_manager_exception":
            return "Deletion of the SNMP Manager"
        elif response_type == "modify_snmp_manager_exception":
            return "Updation of the SNMP Manager"
        elif response_type == "get_snmp_manager_list_exception":
            return "Got error while trying to get SNMP Manager id error:"
        elif response_type == "get_snmp_manager_id_exception":
            return "Got error while trying to get SNMP Manager details error:"

    @staticmethod
    def get_snmp_validation_error_response(response_type):
        if response_type == "create_without_ip_exception":
            return "Provide valid value for ip_address or network_name."
        if response_type == "create_without_snmp_port":
            return "snmp_port is required parameter for creating SNMP Manager."
        if response_type == "create_without_alert_severity":
            return "alert_severity is required parameter for creating/modifying SNMP Manager."
        if response_type == "trap_community_error":
            return "Trap community is required parameter for creating SNMP Manager with version V2c."
        if response_type == "create_without_snmp_username":
            return "snmp_username is required parameter for creating SNMP Manager with version V3."
        if response_type == "create_without_snmp_password":
            return "snmp_password/auth_pass required parameter for creating or modifying SNMP Manager with version V3 and auth_protocol."
        if response_type == "create_without_auth_protocol":
            return "For V3 SNMP auth_protocol with None value must have privacy_protocol with None value."
        if response_type == "create_without_protocol":
            return "V3 with no authenticaton should not use snmp_password/authpass."
        if response_type == "modify_version_error_message":
            return "Version cannot be changed from"
        if response_type == "modify_without_trap_community":
            return "Trap community is required parameter for updating SNMP Manager with version V2c."
