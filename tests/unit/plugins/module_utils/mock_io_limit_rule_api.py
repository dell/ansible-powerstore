# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of IO Limit Rule module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockIoLimitRuleApi:
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    IO_LIMIT_RULE_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'io_limit_rule_name': None,
        'io_limit_rule_id': None,
        'new_name': None,
        'max_bw': None,
        'max_bw_unit': None,
        'max_iops': None,
        'burst_percentage': None,
        'limit_type': None,
        'state': None
    }

    IO_LIMIT_RULE_ID_1 = "6b5e42b0-1234-5678-abcd-ef0123456789"
    IO_LIMIT_RULE_NAME_1 = "tenant_a_limits"

    IO_LIMIT_RULE_DETAILS_1 = {
        "id": "6b5e42b0-1234-5678-abcd-ef0123456789",
        "name": "tenant_a_limits",
        "max_bw": 102400,
        "max_iops": 5000,
        "burst_percentage": 20,
        "type": "Absolute",
        "policies": []
    }

    IO_LIMIT_RULE_DETAILS_2 = {
        "id": "7c6e53b1-2345-6789-bcde-f01234567890",
        "name": "tenant_b_limits",
        "max_bw": 204800,
        "max_iops": 10000,
        "burst_percentage": 50,
        "type": "Density",
        "policies": []
    }

    IO_LIMIT_RULE_DETAILS_WITH_POLICY = {
        "id": "6b5e42b0-1234-5678-abcd-ef0123456789",
        "name": "tenant_a_limits",
        "max_bw": 102400,
        "max_iops": 5000,
        "burst_percentage": 20,
        "type": "Absolute",
        "policies": [
            {"id": "8d7f64c2-3456-7890-cdef-012345678901", "name": "gold_qos"}
        ]
    }

    CREATE_RESPONSE = {"id": "6b5e42b0-1234-5678-abcd-ef0123456789"}

    @staticmethod
    def get_io_limit_rule_failed_msg():
        return "Get IO limit rule failed with error"

    @staticmethod
    def create_io_limit_rule_failed_msg():
        return "Create IO limit rule failed with error"

    @staticmethod
    def modify_io_limit_rule_failed_msg():
        return "Modify IO limit rule failed with error"

    @staticmethod
    def delete_io_limit_rule_failed_msg():
        return "Delete IO limit rule failed with error"

    @staticmethod
    def delete_rule_in_use_msg():
        return "Rule is used by policy"
