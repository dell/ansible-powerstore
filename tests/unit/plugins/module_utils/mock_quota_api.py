# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of Quota module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockQuotaApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.quota.PowerStoreQuota'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'
    MODULE_OPERATION_ERROR1 = 'Unable to fetch the quota details, Invalid Quota ID passed.'
    MODULE_OPERATION_ERROR2 = 'Description parameter is not valid for User Quota.'
    MODULE_OPERATION_ERROR3 = 'uid/unix_name/windows_sid/windows_name are not valid parameters for Tree Quota type. Please enter correct quota_type'
    MODULE_OPERATION_ERROR4 = 'Please enter domain name and user name in the windows_name parameter.'
    MODULE_OPERATION_ERROR5 = 'Empty description or white spaced description is not allowed. Please enter a valid description'
    MODULE_OPERATION_ERROR6 = 'Description starting or ending with white spaces is not allowed. Please enter a valid description'
    MODULE_OPERATION_DESCRIPTION1 = "My Own Description"
    MODULE_OPERATION_DESCRIPTION2 = "Tree quota created on filesystem"
    MODULE_OPERATION_DESCRIPTION3 = "Test Quota description"

    UPDATE_QUOTA_ERROR1 = "Update quota for quota_id: 61d68a87-6000-3cc3-f816-96e8abdcbab0 failed with "

    CREATE_QUOTA_ERROR1 = "Path and filesystem are required for creation of tree quota."
    CREATE_QUOTA_ERROR2 = "Create quota for path = /ansible_tree_quota_FS1_path2 on filesystem = 629494e2-f86e-63ef-3d95-827ee627f9b1 failed with error =  "
    CREATE_QUOTA_ERROR3 = "UID/Windows SID/Windows Name/Unix Name and filesystem both are required to create User Quota"
    CREATE_QUOTA_ERROR4 = 'Create quota for uid: uid-123-unique-id failed with '
    CREATE_QUOTA_ERROR5 = 'Create quota for unix_name: unix_name failed with '
    CREATE_QUOTA_ERROR6 = 'Create quota for windows_name: windows_name failed with '
    CREATE_QUOTA_ERROR7 = 'Create quota for windows_sid: windows_sid failed with '

    DELETE_QUOTA_ERROR1 = "Delete Tree quota with quota_id: {0} failed with Deletion of User Quota is not supported."

    QUOTA_ERROR1 = "Unable to enforce user quotas on tree quotas, failed with error: "
    QUOTA_ERROR2 = "Unable to enable quota, failed with error: "
    QUOTA_ERROR3 = "Invalid soft_limit provided, must be greater than or equal to 0"

    QUOTA_EXPECTED1 = "No Tree Quota with path"
    QUOTA_EXPECTED2 = "UID/Windows SID/Windows Name/Unix Name and File"
    QUOTA_EXPECTED3 = 'Get quota details for user with uid: uid-123-unique-id failed with '
    QUOTA_EXPECTED4 = 'Get quota details for user with unix_name: unix_name failed with '
    QUOTA_EXPECTED5 = 'Get quota details for user with windows_name: windows_name failed with '
    QUOTA_EXPECTED6 = 'Get quota details for user with windows_sid: windows_sid failed with '
    QUOTA_EXPECTED7 = "Failed to get details of NAS server nas-server with error: "
    QUOTA_EXPECTED8 = "Failed to get details of NAS Server None with error: "
    QUOTA_EXPECTED9 = "NAS Server Name/ID is required along with File System Name. Please enter NAS Server Name/ID"
    QUOTA_EXPECTED10 = "Failed to get details of File System {0} with error: "
    QUOTA_EXPECTED11 = "Get details of Tree Quota failed"

    QUOTA_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        "path": None,
        "quota_id": None,
        "nas_server": None,
        "filesystem": None,
        "quota_type": None,
        "description": None,
        "windows_name": None,
        "unix_name": None,
        "windows_sid": None,
        "uid": None,
        "quota": None,
        "state": None
    }

    QUOTA_DETAILS = [{
        "description": "Tree quota created on filesystem",
        "file_system": {
            "filesystem_type": "Primary",
            "id": "61d68a87-6000-3cc3-f816-96e8abdcbab0",
            "name": "sample_file_system",
            "nas_server": {
                "id": "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
                "name": "ansible_nas_server_2"
            }
        },
        "hard_limit": 90,
        "id": "00000006-08f2-0000-0200-000000000000",
        "is_user_quotas_enforced": False,
        "path": "/sample_file_system",
        "remaining_grace_period": -1,
        "size_used": 0,
        "soft_limit": 50,
        "state": "Ok",
        "tree_quota_id": None,
        "tree_quota": {
            "soft_limit": 50,
            "hard_limit": 90,
        }
    }]
