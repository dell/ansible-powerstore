# Copyright: (c) 2021, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Email module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockEmailApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.email.PowerstoreEmail'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    EMAIL_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'email_id': None,
        'email_address': None,
        'send_test_email': None,
        'state': None,
        'new_address': None,
        'notify': {
            'critical': True,
            'major': True,
            'minor': True,
            'info': True
        }
    }
    EMAIL_ADDRESS_1 = "abc_xyz@dell.com"
    EMAIL_DETAILS = {'email': [{"email_address": "abc_xyz@dell.com",
                                "id": "780b6220-2d0b-4b9f-a485-4ae7f673bd98",
                                "notify": {
                                    "critical": True,
                                    "info": True,
                                    "major": True,
                                    "minor": False}
                                }]
                     }

    CREATE_EMAIL = {
        "email_address": "def_xyz@dell.com",
        "id": "780b6220-2d0b-4b9f-a485-4ae7f673bd98",
        "notify": {
            "critical": True,
            "info": False,
            "major": True,
            "minor": False
        }
    }

    MODIFY_EMAIL = None
    TEST_EMAIL = {}
    DELETE_EMAIL = None

    @staticmethod
    def create_email_address_failed_msg():
        return "new_address is not allowed during creation"

    @staticmethod
    def get_email_address_using_email_id_failed_msg():
        return "Please provide a valid email_id"

    @staticmethod
    def get_email_address_failed_msg():
        return "Please provide a valid email_address"
