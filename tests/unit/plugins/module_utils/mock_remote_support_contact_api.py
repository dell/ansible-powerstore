# Copyright: (c) 2022, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of Remote Support Contact module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockRemoteSupportContactApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.remote_support_contact.PowerstoreRemoteSupportContact'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    REMOTE_SUPPORT_CONTACT_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'contact_id': 0,
        'first_name': None,
        'last_name': None,
        'phone': None,
        'email': "def@dell.com",
        'state': None
    }

    REMOTE_SUPPORT_CONTACT_DETAILS = {
        "email": "abc_xyz@dell.com",
        "first_name": "abc",
        "id": "0",
        "last_name": "xyz",
        "phone": "617-555-1212"
    }

    @staticmethod
    def get_remote_support_contact_failed_msg():
        return "does not exist"

    @staticmethod
    def delete_remote_support_contact_failed_msg():
        return "Deletion of Remote Support Contact is not supported"

    @staticmethod
    def modify_remote_support_contact_failed_msg():
        return "Failed to modify remote support contact instance"
