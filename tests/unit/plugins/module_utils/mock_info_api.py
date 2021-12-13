# Copyright: (c) 2021, DellEMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Info module on PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }


class MockInfoApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.info.PowerstoreInfo'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.dellemc_ansible_powerstore_utils'

    INFO_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'filters': None,
        'all_pages': None
    }

    EMPTY_GATHERSUBSET_ERROR_MSG = "Please specify gather_subset"
    EMPTY_RESULT = {
        'SecurityConfig': [
        ],
        'Certificate': [
        ],
        'LDAP': [
        ],
        'ActiveDirectory': [
        ]
    }

    @staticmethod
    def get_security_config_response(response_type):
        if response_type == 'api':
            return {
                "securityconfig": [
                    {
                        "id": "1",
                        "idle_timeout": 3600,
                        "protocol_mode": "TLSv1_0",
                        "protocol_mode_l10n": "TLSv1_0"
                    }
                ]
            }
        elif response_type == 'module':
            return [
                {
                    "id": "1"
                }
            ]
        else:
            return "Getting list of security config for powerstore: %s failed with error: PyPowerStore Error message" % (
                   MockInfoApi.INFO_COMMON_ARGS['array_ip'])

    @staticmethod
    def get_certificate_response(response_type):
        if response_type == 'api':
            return {
                "certificate": [
                    {
                        "id": "e940144f-393f-4e9c-8f54-9a4d57b38c48",
                        "is_current": False,
                        "is_valid": False,
                        "members": [],
                        "scope": "Syslog_HTTP",
                        "service": "Syslog_HTTP",
                        "service_l10n": "Syslog_HTTP",
                        "type": "Client",
                        "type_l10n": "Client"
                    }
                ]
            }
        elif response_type == 'module':
            return [
                {
                    "id": "e940144f-393f-4e9c-8f54-9a4d57b38c48"
                },
                {
                    "id": "4b6a46bc-b22c-47d8-b094-9a4dc1c6877d"
                },
                {
                    "id": "37b76535-612b-456a-a694-1389f17632c7"
                },
                {
                    "id": "e00b93aa-3a11-4242-9576-e18c0052c069"
                },
                {
                    "id": "373dbe54-150f-47b9-8ce2-261307d05ebc"
                },
                {
                    "id": "cedeb3ed-0203-405b-b6c0-b3117a331704"
                }
            ]
        else:
            return "Getting list of certificate for powerstore: %s failed with error: PyPowerStore Error message" % (
                   MockInfoApi.INFO_COMMON_ARGS['array_ip'])

    @staticmethod
    def get_ad_response(response_type):
        if response_type == 'api':
            return {
                "ad": [
                    # fill response here
                ]
            }
        elif response_type == 'module':
            return [
                {
                    "id": "60c05c4a-a5aa-d547-d882-ee6f605dfe5a"
                }
            ]
        else:
            return "Getting list of active directory for powerstore: %s failed with error: PyPowerStore Error message" % (
                   MockInfoApi.INFO_COMMON_ARGS['array_ip'])

    @staticmethod
    def get_ldap_response(response_type):
        if response_type == 'api':
            return {
                "ldap": [
                    # fill response here
                ]
            }
        elif response_type == 'module':
            return [
                {
                    "id": "60c05ba8-362e-159a-0205-ee6f605dfe5a"
                }
            ]
        else:
            return "Getting list of ldap for powerstore: %s failed with error: PyPowerStore Error message" % (
                   MockInfoApi.INFO_COMMON_ARGS['array_ip'])
