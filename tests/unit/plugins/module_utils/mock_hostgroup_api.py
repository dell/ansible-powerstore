# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Host Group module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockHostGroupApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.hostgroup.PowerStoreHostgroup'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'
    iscsi_initiator = "iqn.1998-01.com.vmware:losatxxx-0xxxxxfe"
    HOSTGROUP_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'hostgroup_id': None,
        'hostgroup_name': None,
        'hosts': None,
        'state': None,
        'host_state': None,
        'new_name': None,
    }
    HOSTGROUP_NAME_1 = "Sample_hostgroup_1"

    HOSTGROUP_DETAILS_NO_HOSTS = {
        "description": None,
        "hosts": [],
        "id": "d21beab9-15fa-4cee-9651-e3b740ceaa7e",
        "name": "Sample_hostgroup_3"
    }

    HOSTGROUP_DETAILS = {
        "description": None,
        "hosts": [
            {
                "id": "bdd5e201-153c-4b86-b35e-394db0c4851e",
                "name": "Host2"
            },
            {
                "id": "bdd5e201-153c-4b86-b35e-394db0c4851f",
                "name": "Host1"
            }
        ],
        "id": "d21beab9-15fa-4cee-9651-e3b740ceaa7c",
        "name": "Sample_hostgroup_1"
    }

    HOSTGROUP_DETAILS_BY_NAME = [{
        "description": None,
        "hosts": [
            {
                "id": "bdd5e201-153c-4b86-b35e-394db0c4851e",
                "name": "Host2"
            },
            {
                "id": "bdd5e201-153c-4b86-b35e-394db0c4851f",
                "name": "Host1"
            }
        ],
        "id": "d21beab9-15fa-4cee-9651-e3b740ceaa7c",
        "name": "Sample_hostgroup_1"
    }]

    HOSTGROUP_DETAILS_2 = {
        "description": None,
        "hosts": [
            {
                "id": "bdd5e201-153c-4b86-b35e-394db0c4851f",
                "name": "Host1"
            }
        ],
        "id": "d21beab9-15fa-4cee-9651-e3b740ceaa7c",
        "name": "Sample_hostgroup_2"
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
            }
        ],
        "id": "bdd5e201-153c-4b86-b35e-394db0c4851e",
        "mapped_hosts": [],
        "name": "Host2",
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
                "port_name": "nqn.2014-08.org.nvmexpress:uuid:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx18f4",
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

    HOSTGROUP_DETAILS_TWO = [
        {
            "description": None,
            "hosts": [
                {
                    "id": "9d875b91-3214-4ed5-947b-8b9acabaf3c8",
                    "name": "iSCSI_Host_Ansible_Test2"
                },
                {
                    "id": "bdd5e201-153c-4b86-b35e-394db0c4851e",
                    "name": "iSCSI_Host_Ansible_Test1"
                }
            ],
            "id": "d21beab9-15fa-4cee-9651-e3b740ceaa7c",
            "name": "Sample_hostgroup_1"
        },
        {
            "description": None,
            "hosts": [
                {
                    "id": "9d875b91-3214-4ed5-947b-8b9acabaf3c8",
                    "name": "iSCSI_Host_Ansible_Test2"
                },
                {
                    "id": "bdd5e201-153c-4b86-b35e-394db0c4851e",
                    "name": "iSCSI_Host_Ansible_Test1"
                }
            ],
            "id": "d21beab9-15fa-4cee-9651-e3b740ceaa7c",
            "name": "Sample_hostgroup_1"
        }
    ]

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
                    "port_name": "iqn.1998-01.com.vmware:xxxxxxxx-xxxx2aff",
                    "port_type": "iSCSI"}
            ],
            "id": "4d56e60-fc10-4f51-a698-84a664562f0e",
            "mapped_hosts": [],
            "name": "Sample_host_1",
            "os_type": "ESXi",
            "os_type_l10n": "ESXi"
        }
    ]

    @staticmethod
    def get_hostgroup_more_than_one_failed_msg():
        return "Multiple host groups by the same name found"

    @staticmethod
    def create_hostgroup_absent_host_failed_msg():
        return "Please provide correct host_state"

    @staticmethod
    def create_hostgroup_wo_host_failed_msg():
        return "no hosts or invalid hosts specified"

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
