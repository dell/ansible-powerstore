# Copyright: (c) 2022, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of DNS module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockDnsApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.email.PowerstoreDns'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    DNS_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'dns_id': "DNS1",
        'dns_addresses': None,
        'dns_address_state': None,
        'state': None
    }

    DNS_DETAILS = {"id": "DNS1",
                   "addresses": [
                       "XX.XX.XX.XX",
                       "YY.YY.YY.YY"]
                   }

    @staticmethod
    def get_dns_failed_msg(dns_id):
        return "DNS by ID: " + dns_id + " does not exist."

    @staticmethod
    def modify_dns_failed_msg():
        return "Failed to modify DNS instance"

    @staticmethod
    def delete_dns_failed_msg():
        return "Deletion of DNS is not supported through Ansible module"
