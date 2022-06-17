# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Certificate module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_certificate_api import MockCertificateApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKResponse
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_powerstore_connection = MagicMock()
utils.PowerStoreException = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerstore.plugins.modules.certificate import PowerStoreCertificate


class TestPowerstoreCertificate():

    get_module_args = MockCertificateApi.CERTIFICATE_COMMON_ARGS
    remote_address_1 = "10.XX.XX.XX"

    @pytest.fixture
    def certificate_module_mock(self, mocker):
        mocker.patch(MockCertificateApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        certificate_module_mock = PowerStoreCertificate()
        certificate_module_mock.module = MagicMock()
        return certificate_module_mock

    def test_get_certificate_response(self, certificate_module_mock):
        self.get_module_args.update({
            'certificate_id': "f19b38ac-4b8b-45b1-96eb-abe4faae51ca",
            'state': "present"
        })
        certificate_module_mock.module.params = self.get_module_args
        certificate_module_mock.perform_module_operation()
        certificate_module_mock.configuration.get_certificate_details.assert_called()

    def test_reset_certificate(self, certificate_module_mock):
        self.get_module_args.update({
            'certificate_id': "f19b38ac-4b8b-45b1-96eb-abe4faae51ca",
            'service': "VASA_HTTP",
            'state': "present"
        })
        certificate_module_mock.module.params = self.get_module_args
        certificate_module_mock.get_certificate_details = MagicMock(return_value=None)
        certificate_module_mock.perform_module_operation()
        certificate_module_mock.configuration.reset_certificates.assert_called()

    def test_exchange_certificates(self, certificate_module_mock):
        self.get_module_args.update({
            'service': "Replication_HTTP",
            'remote_address': self.remote_address_1,
            'remote_port': 443,
            'remote_user': "remote_user",
            'remote_password': "remote_password",
            'state': "present"
        })
        certificate_module_mock.module.params = self.get_module_args
        certificate_module_mock.get_certificate_details = MagicMock(return_value=None)
        certificate_module_mock.perform_module_operation()
        certificate_module_mock.configuration.exchange_certificate.assert_called()

    def test_create_certificate(self, certificate_module_mock):
        self.get_module_args.update({'certificate_type': "CA_Server_Validation",
                                     'service': "Syslog_HTTP",
                                     'certificate': "certificate_string",
                                     'is_current': True,
                                     'state': "present"})
        certificate_module_mock.module.params = self.get_module_args
        certificate_module_mock.get_certificate_details = MagicMock(return_value=None)
        certificate_module_mock.configuration.get_certificate_details = MagicMock(
            return_value=MockSDKResponse(MockCertificateApi.CERTIFICATE_DETAILS))
        certificate_module_mock.perform_module_operation()
        assert certificate_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_certificate_certificate_id(self, certificate_module_mock):
        self.get_module_args.update({'certificate_type': "CA_Server_Validation",
                                     'service': "Syslog_HTTP",
                                     'certificate_id': "f19b38ac-4b8b-45b1-96eb-abe4faae51ca",
                                     'certificate': "certificate_string",
                                     'is_current': True,
                                     'state': "present"})
        certificate_module_mock.module.params = self.get_module_args
        certificate_module_mock.get_certificate_details = MagicMock(return_value=None)
        certificate_module_mock.perform_module_operation()
        assert MockCertificateApi.create_certificate_certificate_id_failed_msg() in \
            certificate_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_certificate(self, certificate_module_mock):
        self.get_module_args.update({'certificate_id': "f19b38ac-4b8b-45b1-96eb-abe4faae51ca",
                                     'is_current': False,
                                     'state': "present"})
        certificate_module_mock.module.params = self.get_module_args
        certificate_module_mock.configuration.get_certificate_details = MagicMock(
            return_value=MockCertificateApi.MODIFY_CERTIFICATE_DETAILS)
        certificate_module_mock.perform_module_operation()
        assert certificate_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_delete_certificate(self, certificate_module_mock):
        certificate_id = "f19b38ac-4b8b-45b1-96eb-abe4faae51ca"
        self.get_module_args.update({'certificate_id': certificate_id,
                                     'state': "absent"})
        certificate_module_mock.module.params = self.get_module_args
        certificate_module_mock.configuration.get_certificate_details = MagicMock(
            return_value=MockCertificateApi.CERTIFICATE_DETAILS)
        certificate_module_mock.perform_module_operation()
        assert MockCertificateApi.delete_certificate_failed_msg() in \
            certificate_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_certificate_wo_certificate(self, certificate_module_mock):
        self.get_module_args.update({'certificate_type': "CA_Server_Validation",
                                     'service': "Syslog_HTTP",
                                     'is_current': True,
                                     'state': "present"})
        certificate_module_mock.module.params = self.get_module_args
        certificate_module_mock.get_certificate_details = MagicMock(return_value=None)
        certificate_module_mock.perform_module_operation()
        assert MockCertificateApi.create_certificate_wo_certificate_failed_msg() in \
            certificate_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_certificates_wo_service(self, certificate_module_mock):
        self.get_module_args.update({
            'certificate': "certificate_string",
            'certificate_type': "CA_Server_Validation",
            'state': "present"
        })
        certificate_module_mock.module.params = self.get_module_args
        certificate_module_mock.get_certificate_details = MagicMock(return_value=None)
        certificate_module_mock.perform_module_operation()
        print(certificate_module_mock.module.fail_json.call_args[1]['msg'])
        assert MockCertificateApi.create_certificates_wo_service_failed_msg() in \
            certificate_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_certificate_with_certificate(self, certificate_module_mock):
        self.get_module_args.update({'certificate_id': "f19b38ac-4b8b-45b1-96eb-abe4faae51ca",
                                     'certificate': "new_certificate_string",
                                     'is_current': False,
                                     'state': "present"})
        certificate_module_mock.module.params = self.get_module_args
        certificate_module_mock.get_certificate_details = MagicMock(
            return_value=MockCertificateApi.CERTIFICATE_DETAILS)
        certificate_module_mock.perform_module_operation()
        assert MockCertificateApi.modify_certificate_with_certificate_failed_msg() in \
            certificate_module_mock.module.fail_json.call_args[1]['msg']

    def test_exchange_certificate_syslog_http(self, certificate_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'service': "Syslog_HTTP",
            'remote_address': self.remote_address_1,
            'remote_port': 443,
            'remote_user': "remote_user",
            'remote_password': "remote_password",
            'state': "present"
        })
        certificate_module_mock.module.params = self.get_module_args
        certificate_module_mock.configuration.get_certificate_details = MagicMock(
            return_value=None)
        certificate_module_mock.configuration.exchange_certificate = MagicMock(
            side_effect=MockApiException)
        certificate_module_mock.perform_module_operation()
        assert MockCertificateApi.exchange_certificate_failed_msg() in \
            certificate_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_certificate_client_certificate_type(self, certificate_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'certificate_type': "Client",
            'service': "Syslog_HTTP",
            'certificate': "certificate_string",
            'is_current': True,
            'state': "present"
        })
        certificate_module_mock.module.params = self.get_module_args
        certificate_module_mock.configuration.get_certificate_details = MagicMock(
            return_value=None)
        certificate_module_mock.configuration.create_certificate = MagicMock(
            side_effect=MockApiException)
        certificate_module_mock.perform_module_operation()
        assert MockCertificateApi.create_certificate_failed_msg() in \
            certificate_module_mock.module.fail_json.call_args[1]['msg']

    def test_reset_certificate_syslog_http(self, certificate_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'service': "Syslog_HTTP",
            'state': "present"
        })
        certificate_module_mock.module.params = self.get_module_args
        certificate_module_mock.configuration.get_certificate_details = MagicMock(
            return_value=None)
        certificate_module_mock.configuration.reset_certificates = MagicMock(
            side_effect=MockApiException)
        certificate_module_mock.perform_module_operation()
        certificate_module_mock.configuration.reset_certificates.assert_called()
