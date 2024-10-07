# Copyright: (c) 2022, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of SMB Share module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockSMBShareApi:
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    SMB_SHARE_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'share_id': None,
        'share_name': None,
        'nas_server': None,
        'filesystem': None,
        'path': None,
        'snapshot': None,
        'description': None,
        'is_abe_enabled': None,
        'is_branch_cache_enabled': None,
        'is_continuous_availability_enabled': None,
        'is_encryption_enabled': None,
        'offline_availability': None,
        'umask': None,
        'state': None,
        'aces': None,
    }

    SMB_NAME = "Sample_smb_share"
    SMB_ID = "61d68cf6-34d3-7b16-0370-96e8abdcbab0"
    FS_ID = "61e4947b-8992-3db7-2859-aa02b52a0308"
    NAS_ID = "6026056b-5405-0e36-7697-c285b9fa42b7"

    SMB_SHARE_DETAILS = [
        {
            "description": "SMB Share created",
            "file_system": {
                "filesystem_type": "Primary",
                "id": "61e4947b-8992-3db7-2859-aa02b52a0308",
                "name": "sample_file_system",
                "nas_server": {
                    "id": "6026056b-5405-0e36-7697-c285b9fa42b7",
                    "name": "ansible_nas_server_2"
                }
            },
            "id": "61d68cf6-34d3-7b16-0370-96e8abdcbab0",
            "is_ABE_enabled": True,
            "is_branch_cache_enabled": True,
            "is_continuous_availability_enabled": True,
            "is_encryption_enabled": True,
            "name": "Sample_smb_share",
            "offline_availability": "Documents",
            "path": "/sample_file_system",
            "umask": "007",
            "aces": [
                {
                    "trustee_name": "S-1-5-21-8-5-1-32",
                    "trustee_type": "SID",
                    "access_level": "Read",
                    "access_type": "Allow"
                }
            ]
        }
    ]

    MODIFY_SMB_SHARE = {
        "description": "SMB Share Modified",
        "file_system": {
            "filesystem_type": "Primary",
            "id": "61e4947b-8992-3db7-2859-aa02b52a0308",
            "name": "sample_file_system",
            "nas_server": {
                "id": "6026056b-5405-0e36-7697-c285b9fa42b7",
                "name": "ansible_nas_server_2"
            }
        },
        "id": "61d68cf6-34d3-7b16-0370-96e8abdcbab0",
        "is_ABE_enabled": True,
        "is_branch_cache_enabled": False,
        "is_continuous_availability_enabled": False,
        "is_encryption_enabled": True,
        "name": "Sample_smb_share",
        "offline_availability": "Programs",
        "path": "/sample_file_system",
        "umask": "177",
        "aces": [
            {
                "trustee_name": "S-1-5-21-8-5-1-32",
                "trustee_type": "SID",
                "access_level": "Read",
                "access_type": "Allow"
            }
        ]
    }

    @staticmethod
    def get_smbshare_without_nas_server_failed_msg():
        return "filesystem/snapshot/nas_server also required."

    @staticmethod
    def create_smb_share_without_path_failed_msg():
        return "Path is required for creation of a SMB share. Please provide path"

    @staticmethod
    def smb_error_messages():
        return {"umask_error": "not all arguments converted during string formatting"}
