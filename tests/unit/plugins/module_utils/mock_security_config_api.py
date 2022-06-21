# Copyright: (c) 2021, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Security Config module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockSecurityConfigApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.security_config.PowerStoreSecurityConfig'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    SECURITY_CONFIG_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'security_config_id1': "1",
        'protocol_mode': None
    }

    @staticmethod
    def get_security_config_response(response_type):
        if response_type == 'module':
            return {
                "securityconfig": [
                    {
                        "id": "1",
                        "idle_timeout": 3600,
                        "protocol_mode": "TLSv1_1",
                        "protocol_mode_l10n": "TLSv1_1"
                    }
                ]
            }

        else:
            return "Getting security config details for powerstore: %s failed with error: PyPowerStore Error message" % (
                   MockSecurityConfigApi.SECURITY_CONFIG_COMMON_ARGS['array_ip'])

    @staticmethod
    def modify_security_config_response(response_type):
        if response_type == 'module':
            return {
                "securityconfig": [
                    {
                        "id": "1",
                        "idle_timeout": 3600,
                        "protocol_mode": "TLSv1_1",
                        "protocol_mode_l10n": "TLSv1_1"
                    }
                ]
            }

        else:
            return "Getting list of security config for powerstore: %s failed with error: PyPowerStore Error message" % (
                   MockSecurityConfigApi.SECURITY_CONFIG_COMMON_ARGS['array_ip'])
