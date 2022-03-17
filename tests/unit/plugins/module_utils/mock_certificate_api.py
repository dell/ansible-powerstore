# Copyright: (c) 2022, DellEMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Certificate module on PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }


class MockCertificateApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.certificate.PowerStoreCertificate.'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.dellemc_ansible_powerstore_utils'

    CERTIFICATE_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'certificate_id': None,
        'certificate_type': None,
        'service': None,
        'scope': None,
        'certificate': None,
        'is_current': None,
        'remote_address': None,
        'remote_user': None,
        'remote_password': None,
        'remote_port': None
    }

    CERTIFICATE_DETAILS = {"certificate": [
        {
            "id": "f19b38ac-4b8b-45b1-96eb-abe4faae51ca",
            "type": "CA_Server_Validation",
            "type_l10n": "CA_Server_Validation",
            "service": "Syslog_HTTP",
            "service_l10n": "Syslog_HTTP",
            "scope": "",
            "is_current": True,
            "is_valid": True,
            "members": []
        }]
    }

    MODIFY_CERTIFICATE_DETAILS = {
        "id": "f19b38ac-4b8b-45b1-96eb-abe4faae51ca",
        "type": "CA_Server_Validation",
        "type_l10n": "CA_Server_Validation",
        "service": "Syslog_HTTP",
        "service_l10n": "Syslog_HTTP",
        "scope": "",
        "is_current": True,
        "is_valid": True,
        "members": []
    }

    @staticmethod
    def create_certificates_wo_service_failed_msg():
        return "Please provide valid/existing certificate_id"

    @staticmethod
    def modify_certificate_with_certificate_failed_msg():
        return "Modification of certificate string is not supported through Ansible Module"

    @staticmethod
    def delete_certificate_failed_msg():
        return "Deletion of certificate is not supported through Ansible Module"

    @staticmethod
    def create_certificate_wo_certificate_failed_msg():
        return "certificate_type, service, and certificate are required to create a certificate"

    @staticmethod
    def exchange_certificate_failed_msg():
        return "Exchanging certificates with remote array Syslog_HTTP"

    @staticmethod
    def create_certificate_failed_msg():
        return "Create certificate on PowerStore array name"

    @staticmethod
    def reset_certificate_failed_msg():
        return "Resetting certificates with service Syslog_HTTP"
