# Copyright: (c) 2023, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of storage container module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockStorageContainerApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.storage_container.PowerStoreStorageContainer'
    BASE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.storage_container.StorageContainerHandler'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    SC_ID = "e0ccd953-5650-41d8-9bce-f36d876d6a2a"
    SC_ID_1 = "e0ccd953-5650-41d8-9bce-f36d876d6a2b"
    REMOTE_SC_ID = "666deaed-c378-42dd-a649-14ee89101520"
    REMOTE_SC_ID_1 = "666deaed-c378-42dd-a649-14ee89101521"
    QUOTA = 21474836480
    REMOTE_SYS_NAME = "AB-D8337"
    REMOTE_SYS_ID = "504b6fd2-0a41-4fe6-863d-2f04b2718804"
    MASKED_VALUE = "x.x.x.x"
    MASKED_VALUE1 = "y.y.y.y"
    STORAGE_CONTAINER_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'storage_container_id': None,
        'storage_container_name': None,
        'quota': 0,
        'quota_unit': "GB",
        'storage_protocol': "SCSI",
        'high_water_mark': 50,
        'force_delete': False,
        'new_name': None,
        'state': "present",
        'storage_container_destination': None,
        'storage_container_destination_state': "present"
    }
    STORAGE_CONTAINER_NAME_1 = "Ansible_storage_container_1"
    STORAGE_CONTAINER_DETAILS = {
        "datastores": [],
        "destinations": [],
        "id": SC_ID,
        "name": STORAGE_CONTAINER_NAME_1,
        "quota": QUOTA,
        "replication_groups": [],
        "storage_protocol": "NVMe",
        "storage_protocol_l10n": "NVMe",
        "virtual_volumes": []
    }

    CREATE_STORAGE_CONTAINER = {
        "datastores": [],
        "destinations": [],
        "id": SC_ID,
        "name": STORAGE_CONTAINER_NAME_1,
        "quota": QUOTA,
        "replication_groups": [],
        "storage_protocol": "NVMe",
        "storage_protocol_l10n": "NVMe",
        "virtual_volumes": []
    }

    CREATE_STORAGE_CONTAINER_DESTINATION = {
        "datastores": [],
        "destinations": [{
            "id": "64f26e3f-6fb5-4acc-a39c-3fa2e7917716",
            "remote_storage_container_id": REMOTE_SC_ID,
            "remote_system_id": REMOTE_SYS_ID,
            "remote_system_name": REMOTE_SYS_NAME
        }],
        "id": SC_ID,
        "name": STORAGE_CONTAINER_NAME_1,
        "quota": QUOTA,
        "replication_groups": [],
        "storage_protocol": "NVMe",
        "storage_protocol_l10n": "NVMe",
        "virtual_volumes": []
    }

    STORAGE_CONTAINER_EMPTY_DESTINATION = {
        "datastores": [],
        "destinations": [],
        "id": SC_ID,
        "name": STORAGE_CONTAINER_NAME_1,
        "quota": QUOTA,
        "replication_groups": [],
        "storage_protocol": "NVMe",
        "storage_protocol_l10n": "NVMe",
        "virtual_volumes": []
    }

    REMOTE_SYSTEM_DETAILS = [
        {
            "id": REMOTE_SYS_ID,
            "name": REMOTE_SYS_NAME
        },
        {
            "id": "504b6fd2-0a41-4fe6-863d-2f04b2718855",
            "name": "AB-D8338"
        }
    ]

    REMOTE_SYSTEM_DETAILS1 = [
        {
            "id": REMOTE_SYS_ID,
            "name": REMOTE_SYS_NAME,
            "management_address": MASKED_VALUE
        }
    ]

    REMOTE_STORAGE_CONTAINER = {
        "datastores": [],
        "destinations": [],
        "id": REMOTE_SC_ID_1,
        "name": STORAGE_CONTAINER_NAME_1,
        "quota": 0,
        "replication_groups": [],
        "storage_protocol": "NVMe",
        "storage_protocol_l10n": "NVMe",
        "virtual_volumes": []
    }

    REMOTE_STORAGE_CONTAINER_1 = {
        "datastores": [],
        "destinations": [{
            "id": "64f26e3f-6fb5-4acc-a39c-3fa2e7917716",
            "remote_storage_container_id": REMOTE_SC_ID,
            "remote_system_id": REMOTE_SYS_ID,
            "remote_system_name": REMOTE_SYS_NAME
        }],
        "id": REMOTE_SC_ID,
        "name": STORAGE_CONTAINER_NAME_1,
        "quota": 0,
        "replication_groups": [],
        "storage_protocol": "SCSI",
        "storage_protocol_l10n": "SCSI",
        "virtual_volumes": []
    }

    @staticmethod
    def get_storage_container_exception_response(response_type):
        if response_type == 'remote_dict_exception':
            return "The storage_container_destination dict is required to " \
                   "delete the storage container destination"
        elif response_type == 'delete_destination_exp':
            return "Failed to delete a storage container destination with error"
        elif response_type == "create_destination_exp":
            return "Failed to create a storage container destination with error"
        elif response_type == "delete_container_exp":
            return "Deletion of storage container"
        elif response_type == "modify_container_exception":
            return "Failed to modify the storage container instance with error"
        elif response_type == "create_container_exception":
            return "Creation of storage container with name {0} on " \
                   "PowerStore array name : None , global id : None failed " \
                   "with error".format(MockStorageContainerApi.STORAGE_CONTAINER_NAME_1)
        elif response_type == "get_container_exception":
            return "Get remote storage container details for PowerStore " \
                   "array failed with error"
        elif response_type == "remote_system_exception":
            return "Failed to get the remote system"

    @staticmethod
    def get_sc_exception(resp_type):
        if resp_type == 'remote_none_sc':
            return "Unable to find the remote storage container"
        elif resp_type == "remote_sys_none":
            return "Unable to find the remote system"
        elif resp_type == "invalid_remote_addr":
            return "Enter the valid remote_address for remote_system"
