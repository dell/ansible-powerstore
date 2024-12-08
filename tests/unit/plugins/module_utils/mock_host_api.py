# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of Host module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockHostApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.host.PowerStoreHost'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'
    iscsi_initiator = "iqn.1998-01.com.vmware:losat106-0eab2afe"
    HOST_CONN_1 = "Metro_Optimize_Both"
    HOST_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'host_id': None,
        'host_name': None,
        'initiators': None,
        'state': None,
        'detailed_initiators': None,
        'initiator_state': None,
        'new_name': None,
        'os_type': None,
        'host_connectivity': None,
        'description': None
    }
    HOST_NAME_1 = "Sample_host_1"
    HOST_DETAILS = {
        "description": None,
        "host_group_id": None,
        "host_initiators": [
            {
                "active_sessions": [],
                "chap_mutual_username": "",
                "chap_single_username": "",
                "port_name": iscsi_initiator,
                "port_type": "iSCSI"
            }
        ],
        "id": "4d56e60-fc10-4f51-a698-84a664562f0d",
        "mapped_hosts": [],
        "name": "Sample_host_1",
        "os_type": "ESXi",
        "os_type_l10n": "ESXi",
        "host_connectivity": "Local_Only"
    }

    HOST_DETAILS_2 = {
        "description": None,
        "host_group_id": None,
        "host_initiators": [
            {
                "active_sessions": [],
                "chap_mutual_username": "",
                "chap_single_username": "",
                "port_name": iscsi_initiator,
                "port_type": "iSCSI"
            },
            {
                "active_sessions": [],
                "chap_mutual_username": "",
                "chap_single_username": "",
                "port_name": "iqn.1998-01.com.vmware:lgc198248-5b06fb38",
                "port_type": "iSCSI"
            }
        ],
        "id": "4d56e60-fc10-4f51-a698-84a664562f0d",
        "mapped_hosts": [],
        "name": "Sample_host_1",
        "os_type": "ESXi",
        "os_type_l10n": "ESXi"
    }

    HOST_DETAILS_3 = {
        "description": None,
        "host_group_id": None,
        "host_initiators": [],
        "id": "4d56e60-fc10-4f51-a698-84a664562f0d",
        "mapped_hosts": [],
        "name": "Sample_host_3",
        "os_type": "ESXi",
        "os_type_l10n": "ESXi"
    }

    HOST_DETAILS_4 = {
        "description": None,
        "host_group_id": None,
        "host_initiators": [
            {
                "active_sessions": [],
                "chap_mutual_username": "",
                "chap_single_username": "",
                "port_name": "nqn.2014-08.org.nvmexpress:uuid:7936206c-9c51-4bf4-86b6-f4e2803218f4",
                "port_type": "NVMe"
            }
        ],
        "id": "4d56e60-fc10-4f51-a698-84a664562f0g",
        "mapped_hosts": [],
        "name": "Sample_host_4",
        "os_type": "Windows",
        "os_type_l10n": "Windows"
    }

    HOST_DETAILS_5 = {
        "description": None,
        "host_group_id": None,
        "host_initiators": [
            {
                "active_sessions": [],
                "chap_mutual_username": "",
                "chap_single_username": "",
                "port_name": "21:00:00:XX:XX:XX:XX:XX",
                "port_type": "FC"
            }
        ],
        "id": "4d56e60-fc10-4f51-a698-84a664562f0f",
        "mapped_hosts": [],
        "name": "Sample_host_4",
        "os_type": "Windows",
        "os_type_l10n": "Windows"
    }

    HOST_DETAILS_TWO = [
        {
            "description": None,
            "host_group_id": None,
            "host_initiators": [
                {
                    "active_sessions": [],
                    "chap_mutual_username": "",
                    "chap_single_username": "",
                    "port_name": iscsi_initiator,
                    "port_type": "iSCSI"
                }
            ],
            "id": "4d56e60-fc10-4f51-a698-84a664562f0d",
            "mapped_hosts": [],
            "name": "Sample_host_1",
            "os_type": "ESXi",
            "os_type_l10n": "ESXi"
        },
        {
            "description": None,
            "host_group_id": None,
            "host_initiators": [
                {
                    "active_sessions": [],
                    "chap_mutual_username": "",
                    "chap_single_username": "",
                    "port_name": "iqn.1998-01.com.vmware:losat106-0eab2aff",
                    "port_type": "iSCSI"}
            ],
            "id": "4d56e60-fc10-4f51-a698-84a664562f0e",
            "mapped_hosts": [],
            "name": "Sample_host_1",
            "os_type": "ESXi",
            "os_type_l10n": "ESXi"
        }
    ]

    CREATE_HOST = {
        "description": None,
        "host_group_id": None,
        "host_initiators": [
            {
                "active_sessions": [],
                "chap_mutual_username": "",
                "chap_single_username": "chapuserSingle",
                "port_name": "iqn.1998-01.com.vmware:lgc198248-5b06fb37",
                "port_type": "iSCSI"
            }
        ],
        "id": "4d56e60-fc10-4f51-a698-84a664562f0e",
        "mapped_hosts": [],
        "name": "Sample_host_2",
        "os_type": "ESXi",
        "os_type_l10n": "ESXi"
    }

    @staticmethod
    def create_host_without_os_type_failed_msg():
        return "failed as os_type is not specified"

    @staticmethod
    def get_host_more_than_one_failed_msg():
        return "Multiple hosts by the same name found"

    @staticmethod
    def create_host_mixed_initiators_failed_msg():
        return "Connect either fiber channel or iSCSI or NVMe"

    @staticmethod
    def create_host_wo_initiator_state_failed_msg():
        return "Incorrect initiator_state specified for Create host functionality"

    @staticmethod
    def create_host_wo_initiator_failed_msg():
        return "failed with error"

    @staticmethod
    def create_host_with_new_name_failed_msg():
        return "Operation on host failed as new_name is given"

    @staticmethod
    def modify_os_type_failed_msg():
        return "os_type cannot be modified for an already existing host"
