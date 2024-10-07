# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of File DNS module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockFileDNSApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.storage_container.PowerStoreFileDNS'
    BASE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.storage_container.FileDNSHandler'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    FILE_DNS_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'file_dns_id': None,
        'nas_server': None,
        'domain': None,
        'add_ip_addresses': None,
        'remove_ip_addresses': None,
        'transport': None,
        'is_destination_override_enabled': None,
        'state': "present"
    }

    FILE_DNS_DETAILS = [{
        "domain": "NAS_domain",
        "id": "65ad05aa-01bc-11d5-c30e-62b767ad9845",
        "ip_addresses": [
            "10.10.10.10"
        ],
        "is_destination_override_enabled": False,
        "nas_server_id": "6581683c-61a3-76ab-f107-62b767ad9845",
        "transport": "UDP"
    }]

    NAS_SERVER_DETAILS = {
        "id": "6581683c-61a3-76ab-f107-62b767ad9845"
    }

    @staticmethod
    def get_file_dns_exception_response(response_type):
        if response_type == "delete_file_dns_exception":
            return "Deletion of the File DNS"
        elif response_type == "modify_file_dns_exception":
            return "Failed to modify the File DNS instance"
        elif response_type == "create_file_dns_exception":
            return "Creation of File DNS on " \
                   "PowerStore array failed with error "
        elif response_type == "get_file_dns_exception":
            return "Getting File DNS details failed with error"
        elif response_type == "create_without_ip_exception":
            return "Provide nas_server, add_ip_addresses and domain for creation"
