# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of service config module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockServiceConfigApi:

    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    APP_ID_1 = "A1"
    APP_ID_2 = "A2"
    APP_NAME_1 = "APP1"
    APP_NAME_2 = "APP2"
    SSH_ENABLED = True
    SSH_DISABLED = False

    SERVICE_CONFIGS_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'service_config': None
    }

    SERVICE_CONFIGS_DETAILS = [
        {
            "appliance_name": APP_NAME_1,
            "appliance_id": APP_ID_1,
            "id": APP_ID_1,
            "is_ssh_enabled": SSH_DISABLED
        }
    ]

    APPLIANCE_DETAILS = {
        "id": APP_ID_1,
        "name": APP_NAME_1
    }

    @staticmethod
    def get_service_exception_response(response_type):
        if response_type == 'appliance_exception':
            return "Get Appliance with id A1 or name None failed with error"
        elif response_type == 'get_service_config_exception':
            return "Failed to get the service configs with error"
        elif response_type == "no_appliance_found":
            return "Appliance id: A3 or name: None not found. Specify valid " \
                   "appliance_id or appliance_name"
        elif response_type == "update_service_config_exception":
            return "Failed to update the service config with error"
        elif response_type == "mutually_exclusive_exception":
            return "parameters are mutually exclusive: appliance_name|appliance_id"
        elif response_type == "required_one_exception":
            return "one of the following is required: appliance_name, appliance_id"

    @staticmethod
    def empty_app_exception(response_type, empty_key):
        if response_type == "empty_appliance_exception":
            return f"Provide valid value of {empty_key}"
