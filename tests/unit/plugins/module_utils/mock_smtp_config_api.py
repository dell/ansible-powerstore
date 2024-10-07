# Copyright: (c) 2022, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of Email module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockSmtpConfigApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.email.PowerstoreSmtpConfig'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    SMTP_CONFIG_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'smtp_id': 0,
        'smtp_address': None,
        'smtp_port': None,
        'state': None,
        'source_email': None,
        'destination_email': "def@dell.com"
    }

    SMTP_CONFIG_DETAILS = {
        "id": 0,
        "address": "sample.smtp.com",
        "port": 25,
        "source_email": "abc@dell.com"
    }

    @staticmethod
    def get_smtp_config_failed_msg():
        return "does not exist"

    @staticmethod
    def delete_smtp_config_failed_msg():
        return "Deletion of SMTP configuration is not supported"

    @staticmethod
    def modify_smtp_config_failed_msg():
        return "Failed to modify SMTP configuration instance"
