# Copyright: (c) 2022, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of Certificate module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockCertificateApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.certificate.PowerStoreCertificate.'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

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
    def get_modify_certificate_details(service="Syslog_HTTP"):
        cert_detail = MockCertificateApi.MODIFY_CERTIFICATE_DETAILS.copy()
        cert_detail['service'] = service
        return cert_detail

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
    def create_certificate_certificate_id_failed_msg():
        return "certificate_id is not accepted while adding a certificate"

    @staticmethod
    def modify_management_certificate_failed_msg():
        return "cannot disable `is_current` for Management_HTTP service"
