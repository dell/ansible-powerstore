# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for dns module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.shared_library import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_dns_api import MockDnsApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.dns import PowerstoreDns


class TestPowerstoreDns():

    get_module_args = MockDnsApi.DNS_COMMON_ARGS

    @pytest.fixture
    def dns_module_mock(self, mocker):
        mocker.patch(MockDnsApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        dns_module_mock = PowerstoreDns()
        dns_module_mock.module = MagicMock()
        return dns_module_mock

    def test_get_dns_response(self, dns_module_mock):
        self.get_module_args.update({
            'dns_id': "DNS1",
            'state': "present"
        })
        dns_module_mock.module.params = self.get_module_args
        dns_module_mock.configuration.get_dns_details = MagicMock(
            return_value=MockDnsApi.DNS_DETAILS)
        dns_module_mock.perform_module_operation()
        assert self.get_module_args['dns_id'] == dns_module_mock.module.exit_json.call_args[1]['dns_details']['id']
        dns_module_mock.configuration.get_dns_details.assert_called()

    def test_add_address(self, dns_module_mock):
        self.get_module_args.update({'dns_id': "DNS1",
                                     'dns_addresses': ["XX.XX.XX.YY"],
                                     'dns_address_state': "present-in-dns",
                                     'state': "present"})
        dns_module_mock.module.params = self.get_module_args
        dns_module_mock.perform_module_operation()
        dns_module_mock.configuration.modify_dns_details.assert_called()

    def test_remove_address(self, dns_module_mock):
        self.get_module_args.update({
            'dns_id': "DNS1",
            'dns_addresses': ["XX.XX.XX.XX"],
            'dns_address_state': "absent-in-dns",
            'state': "present"
        })
        dns_module_mock.module.params = self.get_module_args
        dns_module_mock.configuration.get_dns_details = MagicMock(
            return_value=MockDnsApi.DNS_DETAILS)
        dns_module_mock.perform_module_operation()
        assert self.get_module_args['dns_id'] == dns_module_mock.module.exit_json.call_args[1]['dns_details']['id']
        assert dns_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_get_non_existing_dns_details(self, dns_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        invalid_dns_id = "non_existing_dns"
        self.get_module_args.update({
            'dns_id': invalid_dns_id,
            'state': "present"
        })
        dns_module_mock.module.params = self.get_module_args
        dns_module_mock.configuration.get_dns_details = MagicMock(
            side_effect=MockApiException)
        dns_module_mock.perform_module_operation()
        assert MockDnsApi.get_dns_failed_msg(invalid_dns_id) in \
            dns_module_mock.module.fail_json.call_args[1]['msg']

    def test_add_more_than_3_addresses(self, dns_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        dns_id = "DNS1"
        self.get_module_args.update({'dns_id': dns_id,
                                     'dns_addresses': ["XX.XX.XX.YY",
                                                       "XX.XX.XX.ZZ",
                                                       "XX.XX.XX.WW",
                                                       "XX.XX.XX.VV"],
                                     'dns_address_state': "present-in-dns",
                                     'state': "present"})
        dns_module_mock.module.params = self.get_module_args
        dns_module_mock.configuration.get_dns_details = MagicMock(
            return_value=MockDnsApi.DNS_DETAILS)
        dns_module_mock.configuration.modify_dns_details = MagicMock(
            side_effect=MockApiException)
        dns_module_mock.perform_module_operation()
        assert MockDnsApi.modify_dns_failed_msg() in \
            dns_module_mock.module.fail_json.call_args[1]['msg']

    def test_delete_dns(self, dns_module_mock):
        dns_id = "DNS1"
        self.get_module_args.update({'dns_id': dns_id,
                                     'state': "absent"})
        dns_module_mock.module.params = self.get_module_args
        dns_module_mock.configuration.get_dns_details = MagicMock(
            return_value=MockDnsApi.DNS_DETAILS)
        dns_module_mock.perform_module_operation()
        assert MockDnsApi.delete_dns_failed_msg() in \
            dns_module_mock.module.fail_json.call_args[1]['msg']
