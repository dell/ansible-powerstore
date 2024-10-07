# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of SMB server module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockSMBServerApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.storage_container.PowerStoreSMBServer'
    BASE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.storage_container.SMBServerHandler'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    SMB_SERVER_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'smb_server_id': None,
        'nas_server': None,
        'computer_name': None,
        'description': None,
        'domain': None,
        'is_standalone': None,
        'local_admin_password': None,
        'netbios_name': None,
        'password': None,
        'workgroup': None,
        'state': "present"
    }

    SMB_SERVER_DETAILS = [{
        "computer_name": None,
        "description": "string2",
        "domain": None,
        "id": "65acede5-9ee6-c83f-ff39-62b767ad9845",
        "is_joined": False,
        "is_standalone": True,
        "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
        "netbios_name": "STRING2",
        "workgroup": "STRING2"
    }]

    NAS_SERVER_DETAILS = {
        "id": "6581683c-61a3-76ab-f107-62b767ad9845"
    }

    @staticmethod
    def get_smb_server_exception_response(response_type):
        if response_type == "delete_smb_server_exception":
            return "Deletion of the SMB server"
        elif response_type == "modify_smb_server_exception":
            return "Failed to modify the SMB server instance"
        elif response_type == "create_smb_server_exception":
            return "Creation of SMB server on " \
                   "PowerStore array failed with error "
        elif response_type == "get_smb_server_exception":
            return "Getting SMB server details failed with error"
        elif response_type == "create_smb_server_wo_is_standalone_exception":
            return "Provide nas_server, is_standalone and local_admin_password for creation"
