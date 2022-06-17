# Copyright: (c) 2021, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Info module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockInfoApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.info.PowerstoreInfo'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    INFO_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'filters': None,
        'all_pages': None,
        'gather_subset': None
    }

    EMPTY_GATHERSUBSET_ERROR_MSG = "Please specify gather_subset"
    EMPTY_RESULT = {
        'SecurityConfig': [],
        'Certificate': [],
        'LDAP': [],
        'ActiveDirectory': [],
        'DNS': [],
        'EmailNotification': [],
        'NTP': [],
        'RemoteSupport': [],
        'RemoteSupportContact': [],
        'SMTPConfig': []
    }

    CLUSTER_DETAILS_TWO = [
        {
            "id": "0",
            "name": "WN-ABCD"},
        {
            "id": "1",
            "name": "WN-WXYZ"}

    ]

    @staticmethod
    def get_security_config_response(response_type):
        if response_type == 'api':
            return [
                {
                    "id": "1"
                }
            ]

    @staticmethod
    def get_certificate_response(response_type):
        if response_type == 'api':
            return [
                {
                    "id": "e940144f-393f-4e9c-8f54-9a4d57b38c48"
                },
                {
                    "id": "4b6a46bc-b22c-47d8-b094-9a4dc1c6877d"
                },
                {
                    "id": "37b76535-612b-456a-a694-1389f17632c7"
                },
                {
                    "id": "e00b93aa-3a11-4242-9576-e18c0052c069"
                },
                {
                    "id": "373dbe54-150f-47b9-8ce2-261307d05ebc"
                },
                {
                    "id": "cedeb3ed-0203-405b-b6c0-b3117a331704"
                }
            ]

    @staticmethod
    def get_dns_response(response_type):
        if response_type == 'api':
            return [
                {
                    "id": "DNS1"
                }
            ]

    @staticmethod
    def get_ntp_response(response_type):
        if response_type == 'api':
            return [
                {
                    "id": "NTP1"
                }
            ]

    @staticmethod
    def get_one_id_response(response_type):
        if response_type == 'api':
            return [
                {
                    "id": "0"
                }
            ]

    @staticmethod
    def get_email_destination_response(response_type):
        if response_type == 'api':
            return [
                {
                    "id": "9c3e5cba-17d5-4d64-b97c-350f91e2b714"
                }
            ]

    @staticmethod
    def get_remote_support_contact_response(response_type):
        if response_type == 'api':
            return [
                {
                    "id": "0"
                },
                {
                    "id": "1"
                }
            ]

    @staticmethod
    def get_remote_support_response(response_type):
        if response_type == 'api':
            return [
                {
                    "id": "0"
                }
            ]

    @staticmethod
    def get_volumes_failed_msg():
        return "Given filter operator 'None' is not supported"

    @staticmethod
    def get_invalid_gather_subset_failed_msg():
        return "subset_mapping do not have details"

    @staticmethod
    def get_no_gather_subset_failed_msg():
        return "No subset specified in gather_subset"

    @staticmethod
    def get_subset_invalid_filter():
        return "Filter should have all keys: 'filter_key, filter_operator, filter_value'"
