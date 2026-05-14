# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of File IO Limit Rule module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockFileIoLimitRuleApi:
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    FILE_IO_LIMIT_RULE_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'file_io_limit_rule_name': None,
        'file_io_limit_rule_id': None,
        'new_name': None,
        'max_bw': None,
        'state': None
    }

    FILE_IO_LIMIT_RULE_ID_1 = "7c6e53b1-2345-6789-bcde-f01234567890"
    FILE_IO_LIMIT_RULE_NAME_1 = "file_bw_500mb"

    FILE_IO_LIMIT_RULE_DETAILS_1 = {
        "id": "7c6e53b1-2345-6789-bcde-f01234567890",
        "name": "file_bw_500mb",
        "max_bw": 500,
        "policies": []
    }

    FILE_IO_LIMIT_RULE_DETAILS_2 = {
        "id": "8d7f64c2-3456-7890-cdef-012345678901",
        "name": "file_bw_1000mb",
        "max_bw": 1000,
        "policies": []
    }

    FILE_IO_LIMIT_RULE_DETAILS_WITH_POLICY = {
        "id": "7c6e53b1-2345-6789-bcde-f01234567890",
        "name": "file_bw_500mb",
        "max_bw": 500,
        "policies": [
            {"id": "9e8g75d3-4567-8901-defg-123456789012", "name": "file_gold_qos"}
        ]
    }

    TWO_RULE_LIST = [
        {
            "id": "7c6e53b1-2345-6789-bcde-f01234567890",
            "name": "file_bw_500mb",
            "max_bw": 500
        },
        {
            "id": "8d7f64c2-3456-7890-cdef-012345678901",
            "name": "file_bw_500mb",
            "max_bw": 1000
        }
    ]

    CREATE_RESPONSE = {"id": "7c6e53b1-2345-6789-bcde-f01234567890"}

    @staticmethod
    def get_file_io_limit_rule_failed_msg():
        return "Get file IO limit rule failed with error"

    @staticmethod
    def create_file_io_limit_rule_failed_msg():
        return "Create file IO limit rule failed with error"

    @staticmethod
    def modify_file_io_limit_rule_failed_msg():
        return "Modify file IO limit rule failed with error"

    @staticmethod
    def delete_file_io_limit_rule_failed_msg():
        return "Delete file IO limit rule failed with error"

    @staticmethod
    def delete_rule_in_use_msg():
        return "Rule is used by policy"

    @staticmethod
    def get_multiple_rules_msg():
        return "Multiple file IO limit rules found"
