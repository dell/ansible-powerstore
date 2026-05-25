# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of recycle bin module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockRecycleBinApi:

    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    RECYCLE_BIN_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'recycle_bin_id': None,
        'resource_name': None,
        'resource_type': None,
        'expiration_duration': None,
        'empty_recycle_bin': False,
        'state': 'present'
    }

    RECYCLE_BIN_CONFIG = {
        "id": "0",
        "expiration_duration": 7
    }

    RECYCLE_BIN_CONFIG_MODIFIED = {
        "id": "0",
        "expiration_duration": 14
    }

    RECYCLE_BIN_ITEM_VOLUME = {
        "id": "e0684b39-0029-4be2-b5bf-67b8c145e1b8",
        "name": "test_volume",
        "resource_type": "volume",
        "logical_provisioned": 1073741824,
        "logical_used": 0,
        "appliance_id": "A1",
        "deletion_timestamp": "2024-01-01T00:00:00.000+00:00",
        "expiration_timestamp": "2024-01-08T00:00:00.000+00:00",
        "resource_type_l10n": "volume"
    }

    RECYCLE_BIN_ITEM_VG = {
        "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "name": "test_vg",
        "resource_type": "volume_group",
        "logical_provisioned": 2147483648,
        "logical_used": 1073741824,
        "appliance_id": "A1",
        "deletion_timestamp": "2024-01-02T00:00:00.000+00:00",
        "expiration_timestamp": "2024-01-09T00:00:00.000+00:00",
        "resource_type_l10n": "volume group"
    }

    RECYCLE_BIN_ITEMS = [RECYCLE_BIN_ITEM_VOLUME, RECYCLE_BIN_ITEM_VG]

    RECYCLE_BIN_EMPTY = []

    DUPLICATE_NAME_ITEMS = [
        {
            "id": "id-1",
            "name": "dup_name",
            "resource_type": "volume",
            "logical_provisioned": 1073741824,
            "logical_used": 0,
            "appliance_id": "A1",
            "deletion_timestamp": "2024-01-01T00:00:00.000+00:00",
            "expiration_timestamp": "2024-01-08T00:00:00.000+00:00"
        },
        {
            "id": "id-2",
            "name": "dup_name",
            "resource_type": "volume",
            "logical_provisioned": 2147483648,
            "logical_used": 0,
            "appliance_id": "A1",
            "deletion_timestamp": "2024-01-02T00:00:00.000+00:00",
            "expiration_timestamp": "2024-01-09T00:00:00.000+00:00"
        }
    ]

    @staticmethod
    def get_recycle_bin_exception_response(response_type):
        if response_type == 'get_config_exception':
            return "Failed to get recycle bin configuration with error"
        elif response_type == 'modify_config_exception':
            return "Failed to modify recycle bin configuration with error"
        elif response_type == 'get_items_exception':
            return "Failed to get recycle bin items with error"
        elif response_type == 'get_item_exception':
            return "Failed to get recycle bin item"
        elif response_type == 'recover_exception':
            return "Failed to recover recycle bin item"
        elif response_type == 'delete_exception':
            return "Failed to delete recycle bin item"
        elif response_type == 'empty_exception':
            return "Failed to empty recycle bin with error"
        elif response_type == 'invalid_expiration':
            return "expiration_duration must be between 0 and 30 days"
        elif response_type == 'absent_no_params':
            return "state is absent but none of the following are set"
        elif response_type == 'duplicate_name':
            return "Multiple recycle bin items found with name"
