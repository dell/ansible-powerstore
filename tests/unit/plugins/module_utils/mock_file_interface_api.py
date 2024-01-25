# Copyright: (c) 2024, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of File Interface module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockFileInterfaceApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.storage_container.PowerStoreFileInterface'
    BASE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.storage_container.FileInterfaceHandler'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    FILE_INTERFACE_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'file_interface_id': None,
        'nas_server': None,
        'ip_address': None,
        'gateway': None,
        'prefix_length': None,
        'vlan_id': None,
        'ip_port_id': None,
        'is_disabled': None,
        'role': None,
        'is_destination_override_enabled': None,
        'state': "present"
    }

    FILE_INTERFACE_DETAILS = [{
        "gateway": "10.10.10.1",
        "id": "65a50e0d-25f9-bd0a-8ca7-62b767ad9845",
        "ip_address": "10.**.**.**",
        "ip_port_id": "IP_PORT2",
        "is_destination_override_enabled": False,
        "is_disabled": False,
        "is_dr_test": False,
        "name": "PROD022_19c8adfb1d41_1d",
        "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
        "prefix_length": 21,
        "role": "Production",
        "source_parameters": None,
        "vlan_id": 0
    }]

    NAS_SERVER_DETAILS = {
        "id": "6581683c-61a3-76ab-f107-62b767ad9845"
    }

    @staticmethod
    def get_file_interface_exception_response(response_type):
        if response_type == "delete_file_interface_exception":
            return "Deletion of the file interface"
        elif response_type == "modify_file_interface_exception":
            return "Failed to modify the file interface instance"
        elif response_type == "create_file_interface_exception":
            return "Creation of file interface on " \
                   "PowerStore array name : None , global id : None failed " \
                   "with error "
        elif response_type == "get_file_interface_exception":
            return "Get file interface details for PowerStore " \
                   "array failed with error"
        elif response_type == "create_file_interface_wo_ip_exception":
            return "Provide nas_server, ip_address and prefix_length for creation."
        elif response_type == "get_file_interface_nas_ip_id_exception":
            return "file_interface_id is mutually exclusive with nas_server and ip_address."
