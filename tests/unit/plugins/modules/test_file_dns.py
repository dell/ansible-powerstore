# Copyright: (c) 2024, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)
"""Unit Tests for File DNS module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
# pylint: disable=unused-import

from ansible_collections.dellemc.powerstore.plugins.modules.file_dns import \
    PowerStoreFileDNS
from ansible_collections.dellemc.powerstore.plugins.modules.file_dns import \
    FileDNSHandler

from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_file_dns_api \
    import MockFileDNSApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception import \
    MockApiException
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries.powerstore_unit_base \
    import PowerStoreUnitBase


class TestPowerStoreFileDNS(PowerStoreUnitBase):

    get_module_args = MockFileDNSApi.FILE_DNS_COMMON_ARGS
    nas_id = "6581683c-61a3-76ab-f107-62b767ad9845"

    @pytest.fixture
    def module_object(self):
        return PowerStoreFileDNS

    def test_get_file_dns_response(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'file_dns_id': MockFileDNSApi.FILE_DNS_DETAILS[0]['id'],
                'state': "present"}
        )
        FileDNSHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.file_dns.get_file_dns_details.assert_called()

    def test_get_file_dns_nas_response(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nas_server': self.nas_id,
                'state': "present"
            })
        powerstore_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockFileDNSApi.NAS_SERVER_DETAILS)
        powerstore_module_mock.file_dns.get_file_dns_by_nas_server_id = MagicMock(
            return_value=MockFileDNSApi.FILE_DNS_DETAILS)
        FileDNSHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.file_dns.get_file_dns_by_nas_server_id.assert_called()

    def test_get_file_dns_exception(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'file_dns_id': MockFileDNSApi.FILE_DNS_DETAILS[0]['id'],
                'state': "present"
            })
        powerstore_module_mock.file_dns.get_file_dns_details = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockFileDNSApi.get_file_dns_exception_response(
                'get_file_dns_exception'), powerstore_module_mock, FileDNSHandler)

    def test_create_file_dns_response(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nas_server': "sample_nas_server",
                'domain': "domain1",
                'add_ip_addresses': ['10.10.10.10'],
                'remove_ip_addresses': ['10.10.10.11'],
                'transport': "TCP",
                'state': "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.file_dns.get_file_dns_details_by_nas_server_id = MagicMock(
            return_value=None)
        FileDNSHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.file_dns.create_file_dns.assert_called()

    def test_create_file_dns_exception(self, powerstore_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nas_server': "sample_nas_server",
                'domain': "domain1",
                'add_ip_addresses': ['10.10.10.10'],
                'remove_ip_addresses': ['10.10.10.11'],
                'transport': "TCP",
                'state': "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.configuration.get_file_dns_details_by_nas_server_id = MagicMock(
            return_value=None)
        powerstore_module_mock.file_dns.create_file_dns = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockFileDNSApi.get_file_dns_exception_response(
                'create_file_dns_exception'), powerstore_module_mock, FileDNSHandler)

    def test_modify_file_dns(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'file_dns_id': MockFileDNSApi.FILE_DNS_DETAILS[0]['id'],
                'add_ip_addresses': ['10.10.10.11'],
                'remove_ip_addresses': ['10.10.10.10'],
                'transport': "TCP",
                'is_destination_override_enabled': True,
                'state': "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.file_dns.get_file_dns_details = MagicMock(
            return_value=MockFileDNSApi.FILE_DNS_DETAILS[0])
        FileDNSHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.file_dns.modify_file_dns.assert_called()

    def test_modify_file_dns_exception(self, powerstore_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'file_dns_id': MockFileDNSApi.FILE_DNS_DETAILS[0]['id'],
                'add_ip_addresses': ['10.10.10.11'],
                'remove_ip_addresses': ['10.10.10.10'],
                'transport': "UDP",
                'is_destination_override_enabled': True,
                'state': "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.file_dns.get_file_dns_details = MagicMock(
            return_value=MockFileDNSApi.FILE_DNS_DETAILS[0])
        powerstore_module_mock.file_dns.modify_file_dns = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockFileDNSApi.get_file_dns_exception_response(
                'modify_file_dns_exception'), powerstore_module_mock, FileDNSHandler)

    def test_delete_file_dns(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'file_dns_id': MockFileDNSApi.FILE_DNS_DETAILS[0]['id'],
                'state': "absent"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.file_dns.get_file_dns_details = MagicMock(
            return_value=MockFileDNSApi.FILE_DNS_DETAILS[0])
        FileDNSHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.file_dns.delete_file_dns.assert_called()

    def test_delete_file_dns_exception(self, powerstore_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'file_dns_id': MockFileDNSApi.FILE_DNS_DETAILS[0]['id'],
                'state': "absent"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.file_dns.get_file_dns_details = MagicMock(
            return_value=MockFileDNSApi.FILE_DNS_DETAILS[0])
        powerstore_module_mock.file_dns.delete_file_dns = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockFileDNSApi.get_file_dns_exception_response(
                'delete_file_dns_exception'), powerstore_module_mock, FileDNSHandler)
