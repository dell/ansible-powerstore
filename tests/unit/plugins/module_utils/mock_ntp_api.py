# Copyright: (c) 2022, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of NTP module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockNtpApi:
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    NTP_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'ntp_id': "NTP1",
        'ntp_addresses': None,
        'ntp_address_state': None,
        'state': None
    }

    NTP_DETAILS = {"id": "NTP1",
                   "addresses": [
                       "XX.XX.XX.XX",
                       "YY.YY.YY.YY"]
                   }

    @staticmethod
    def get_ntp_failed_msg(ntp_id):
        return "NTP ID: " + ntp_id + " not found. Creation of NTP is not allowed through Ansible module."

    @staticmethod
    def modify_ntp_failed_msg():
        return "Failed to modify NTP instance"

    @staticmethod
    def delete_ntp_failed_msg():
        return "Deletion of NTP is not supported through Ansible module."
