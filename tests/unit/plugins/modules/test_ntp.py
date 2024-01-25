# Copyright: (c) 2024, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for NTP module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_ntp_api \
    import MockNtpApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.ntp import PowerstoreNtp


class TestPowerstoreNtp():

    get_module_args = MockNtpApi.NTP_COMMON_ARGS

    @pytest.fixture
    def ntp_module_mock(self, mocker):
        mocker.patch(MockNtpApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        ntp_module_mock = PowerstoreNtp()
        ntp_module_mock.module = MagicMock()
        return ntp_module_mock

    def test_get_ntp_response(self, ntp_module_mock):
        self.get_module_args.update({
            'ntp_id': "NTP1",
            'state': "present"
        })
        ntp_module_mock.module.params = self.get_module_args
        ntp_module_mock.configuration.get_ntp_details = MagicMock(
            return_value=MockNtpApi.NTP_DETAILS)
        ntp_module_mock.perform_module_operation()
        assert self.get_module_args['ntp_id'] == ntp_module_mock.module.exit_json.call_args[1]['ntp_details']['id']
        ntp_module_mock.configuration.get_ntp_details.assert_called()

    def test_add_address(self, ntp_module_mock):
        self.get_module_args.update({'ntp_id': "NTP1",
                                     'ntp_addresses': ["XX.XX.XX.YY"],
                                     'ntp_address_state': "present-in-ntp",
                                     'state': "present"})
        ntp_module_mock.module.params = self.get_module_args
        ntp_module_mock.perform_module_operation()
        ntp_module_mock.configuration.modify_ntp_details.assert_called()

    def test_remove_address(self, ntp_module_mock):
        self.get_module_args.update({
            'ntp_id': "NTP1",
            'ntp_addresses': ["XX.XX.XX.XX"],
            'ntp_address_state': "absent-in-ntp",
            'state': "present"
        })
        ntp_module_mock.module.params = self.get_module_args
        ntp_module_mock.configuration.get_ntp_details = MagicMock(
            return_value=MockNtpApi.NTP_DETAILS)
        ntp_module_mock.perform_module_operation()
        assert self.get_module_args['ntp_id'] == ntp_module_mock.module.exit_json.call_args[1]['ntp_details']['id']
        assert ntp_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_get_non_existing_ntp_details(self, ntp_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        invalid_ntp_id = "non_existing_ntp"
        self.get_module_args.update({
            'ntp_id': invalid_ntp_id,
            'state': "present"
        })
        ntp_module_mock.module.params = self.get_module_args
        ntp_module_mock.configuration.get_ntp_details = MagicMock(
            side_effect=MockApiException)
        ntp_module_mock.perform_module_operation()
        assert MockNtpApi.get_ntp_failed_msg(invalid_ntp_id) in \
               ntp_module_mock.module.fail_json.call_args[1]['msg']

    def test_add_more_than_3_addresses(self, ntp_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        ntp_id = "NTP1"
        self.get_module_args.update({'ntp_id': ntp_id,
                                     'ntp_addresses': ["XX.XX.XX.YY",
                                                       "XX.XX.XX.ZZ",
                                                       "XX.XX.XX.WW",
                                                       "XX.XX.XX.VV"],
                                     'ntp_address_state': "present-in-ntp",
                                     'state': "present"})
        ntp_module_mock.module.params = self.get_module_args
        ntp_module_mock.configuration.get_ntp_details = MagicMock(
            return_value=MockNtpApi.NTP_DETAILS)
        ntp_module_mock.configuration.modify_ntp_details = MagicMock(
            side_effect=MockApiException)
        ntp_module_mock.perform_module_operation()
        assert MockNtpApi.modify_ntp_failed_msg() in \
               ntp_module_mock.module.fail_json.call_args[1]['msg']

    def test_delete_ntp(self, ntp_module_mock):
        ntp_id = "NTP1"
        self.get_module_args.update({'ntp_id': ntp_id,
                                     'state': "absent"})
        ntp_module_mock.module.params = self.get_module_args
        ntp_module_mock.configuration.get_ntp_details = MagicMock(
            return_value=MockNtpApi.NTP_DETAILS)
        ntp_module_mock.perform_module_operation()
        assert MockNtpApi.delete_ntp_failed_msg() in \
               ntp_module_mock.module.fail_json.call_args[1]['msg']
