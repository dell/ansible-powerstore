# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of QoS Policy module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockQosPolicyApi:
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    QOS_POLICY_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'qos_policy_name': None,
        'qos_policy_id': None,
        'new_name': None,
        'description': None,
        'policy_type': None,
        'io_limit_rule': None,
        'file_io_limit_rule': None,
        'state': None
    }

    QOS_POLICY_ID_1 = "8d7f64c2-3456-7890-cdef-012345678901"
    QOS_POLICY_NAME_1 = "gold_qos"

    IO_LIMIT_RULE_DETAILS = {
        "id": "6b5e42b0-1234-5678-abcd-ef0123456789",
        "name": "tenant_a_limits"
    }

    IO_LIMIT_RULE_DETAILS_2 = {
        "id": "7c6e53b1-aaaa-bbbb-cccc-dddddddddddd",
        "name": "tenant_b_limits"
    }

    FILE_IO_LIMIT_RULE_DETAILS = {
        "id": "7c6e53b1-2345-6789-bcde-f01234567890",
        "name": "file_bw_500mb"
    }

    QOS_POLICY_DETAILS_QOS = {
        "id": "8d7f64c2-3456-7890-cdef-012345678901",
        "name": "gold_qos",
        "type": "QoS",
        "description": "Gold tier QoS policy",
        "io_limit_rule_id": "6b5e42b0-1234-5678-abcd-ef0123456789",
        "io_limit_rule": {
            "id": "6b5e42b0-1234-5678-abcd-ef0123456789",
            "name": "tenant_a_limits"
        },
        "file_io_limit_rule": None,
        "qos_volumes": [],
        "qos_volume_groups": [],
        "nas_servers_with_qos": [],
        "file_systems_with_qos": []
    }

    QOS_POLICY_DETAILS_FILE_PERF = {
        "id": "9e8g75d3-4567-8901-defg-123456789012",
        "name": "file_gold_qos",
        "type": "File_Performance",
        "description": "File gold tier",
        "io_limit_rule": None,
        "file_io_limit_rule_id": "7c6e53b1-2345-6789-bcde-f01234567890",
        "file_io_limit_rule": {
            "id": "7c6e53b1-2345-6789-bcde-f01234567890",
            "name": "file_bw_500mb"
        },
        "qos_volumes": [],
        "qos_volume_groups": [],
        "nas_servers_with_qos": [],
        "file_systems_with_qos": []
    }

    QOS_POLICY_DETAILS_WITH_RESOURCES = {
        "id": "8d7f64c2-3456-7890-cdef-012345678901",
        "name": "gold_qos",
        "type": "QoS",
        "description": "Gold tier QoS policy",
        "io_limit_rule_id": "6b5e42b0-1234-5678-abcd-ef0123456789",
        "io_limit_rule": {
            "id": "6b5e42b0-1234-5678-abcd-ef0123456789",
            "name": "tenant_a_limits"
        },
        "qos_volumes": [
            {"id": "vol-1", "name": "test_vol"}
        ],
        "qos_volume_groups": [],
        "nas_servers_with_qos": [],
        "file_systems_with_qos": []
    }

    CREATE_RESPONSE = {"id": "8d7f64c2-3456-7890-cdef-012345678901"}

    @staticmethod
    def get_qos_policy_failed_msg():
        return "Get QoS policy failed with error"

    @staticmethod
    def create_qos_policy_failed_msg():
        return "Create QoS policy failed with error"

    @staticmethod
    def modify_qos_policy_failed_msg():
        return "Modify QoS policy failed with error"

    @staticmethod
    def delete_qos_policy_failed_msg():
        return "Delete QoS policy failed with error"

    @staticmethod
    def delete_policy_in_use_msg():
        return "Policy is assigned to"
