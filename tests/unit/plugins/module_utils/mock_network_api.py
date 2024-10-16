# Copyright: (c) 2022-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of Network module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockNetworkApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.network.PowerStoreNetwork'
    mg_address = "10.xx.xx.xx"
    network_name = "Default Management Network"
    system_time = "2022-02-04T11:18:37.441Z"
    STATE_P = "present"
    NW_1 = "NW_1"
    VASA_ID = "0d330"
    CURRENT_ADDR_ERR = "Please provide valid current address."
    NEW_ADDR_ERR = "Please provide valid new address."
    CURRENT_ADDR_1 = "10.xx.xx.xy"
    CURRENT_ADDR_2 = "10.xx.xx.yy"

    NETWORK_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'network_name': None,
        'network_id': None,
        'vlan_id': None,
        'state': None,
        'gateway': None,
        'prefix_length': None,
        'new_name': None,
        'mtu': None,
        'new_cluster_mgmt_address': None,
        'addresses': None,
        'vasa_provider_credentials': None,
        'esxi_credentials': None,
        'storage_discovery_address': None,
        'ports': None,
        'port_state': None,
        'wait_for_completion': None
    }

    VCENTER_DETAILS = {
        "id": NW_1,
        "vcenter_details": None
    }

    NETWORK_DETAILS = {
        "cluster_details": {
            "appliance_count": 1,
            "chap_mode": "Disabled",
            "compatibility_level": 10,
            "global_id": "PS00d01e1bb312",
            "id": 0,
            "is_encryption_enabled": True,
            "management_address": mg_address,
            "master_appliance_id": "A1",
            "name": "WN-XXXX",
            "physical_mtu": 1500,
            "service_config_details": None,
            "state": "Configured",
            "state_l10n": "Configured",
            "storage_discovery_address": mg_address,
            "system_time": system_time
        },
        "gateway": mg_address,
        "id": NW_1,
        "ip_version": "IPv4",
        "ip_version_l10n": "IPv4",
        "member_ips": [
            {
                "address": CURRENT_ADDR_1,
                "appliance_id": None,
                "id": "IP1",
                "ip_port_id": "0",
                "name": network_name,
                "network_id": NW_1,
                "node_id": None,
                "purposes": [
                    "Mgmt_Cluster_Floating"
                ],
                "purposes_l10n": [
                    "Mgmt_Cluster_Floating"
                ]
            },
            {
                "address": CURRENT_ADDR_2,
                "appliance_id": None,
                "id": "IP2",
                "ip_port_id": "1",
                "name": network_name,
                "network_id": NW_1,
                "node_id": None,
                "purposes": [
                    "Mgmt_Appliance_Floating"
                ],
                "purposes_l10n": [
                    "Mgmt_Appliance_Floating"
                ]
            }
        ],
        "mtu": 1500,
        "name": network_name,
        "prefix_length": 24,
        "purposes": [],
        "purposes_l10n": None,
        "type": "Management",
        "type_l10n": "Management",
        "vcenter_details": {
            "address": mg_address,
            "id": "0d330d6c-3fe6-41c6-8023-5bd3fa7c61cd",
            "instance_uuid": "c4c14fbb-828b-40f3-99bb-5bd4db723516",
            "username": "administrator@vsphere.local",
            "vendor_provider_status": "Online",
            "vendor_provider_status_l10n": "Online"
        },
        "vlan_id": 0
    }

    VASA_DETAILS = {
        "username": "username",
        "password": "password"
    }

    CLUSTER_DETAILS = [
        {
            "id": "0",
            "name": "WN-ABCD"},
        {
            "id": "1",
            "name": "WN-WXYZ"}
    ]
