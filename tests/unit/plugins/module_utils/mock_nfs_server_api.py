# Copyright: (c) 2024, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of NFS server module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockNFSServerApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.storage_container.PowerStoreNFSServer'
    BASE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.storage_container.NFSServerHandler'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    NFS_SERVER_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'nfs_server_id': None,
        'nas_server': None,
        'host_name': None,
        'credentials_cache_TTL': None,
        'is_extended_credentials_enabled': None,
        'is_nfsv3_enabled': None,
        'is_nfsv4_enabled': None,
        'is_secure_enabled': None,
        'is_skip_unjoin': None,
        'is_use_smb_config_enabled': None,
        'state': "present"
    }

    NFS_SERVER_DETAILS = {
        "credentials_cache_TTL": 120,
        "host_name": "sample_host_name",
        "id": "65acf901-6a2f-f10b-1d10-62b767ad9845",
        "is_extended_credentials_enabled": True,
        "is_joined": False,
        "is_nfsv3_enabled": True,
        "is_nfsv4_enabled": False,
        "is_secure_enabled": False,
        "is_use_smb_config_enabled": None,
        "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
        "service_principal_name": None
    }

    @staticmethod
    def get_nfs_server_exception_response(response_type):
        if response_type == "delete_nfs_server_exception":
            return "Deletion of the NFS server"
        elif response_type == "modify_nfs_server_exception":
            return "Failed to modify the NFS server instance"
        elif response_type == "create_nfs_server_exception":
            return "Creation of NFS server on " \
                   "PowerStore array failed with error "
        elif response_type == "get_nfs_server_exception":
            return "Getting NFS server details failed with error"
