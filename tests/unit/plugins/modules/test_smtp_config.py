# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for smtp_config module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.shared_library import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_smtp_config_api import MockSmtpConfigApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.smtp_config import PowerstoreSmtpConfig


class TestPowerstoreSmtpConfig():

    get_module_args = MockSmtpConfigApi.SMTP_CONFIG_COMMON_ARGS

    @pytest.fixture
    def smtp_config_module_mock(self, mocker):
        mocker.patch(MockSmtpConfigApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        smtp_config_module_mock = PowerstoreSmtpConfig()
        smtp_config_module_mock.module = MagicMock()
        return smtp_config_module_mock

    def test_get_smtp_config_response(self, smtp_config_module_mock):
        self.get_module_args.update({
            'smtp_id': 0,
            'state': "present"
        })
        smtp_config_module_mock.module.params = self.get_module_args
        smtp_config_module_mock.configuration.get_smtp_config_details = MagicMock(
            return_value=MockSmtpConfigApi.SMTP_CONFIG_DETAILS)
        smtp_config_module_mock.perform_module_operation()
        assert self.get_module_args['smtp_id'] == smtp_config_module_mock.module.exit_json.call_args[1]['smtp_config_details']['id']
        smtp_config_module_mock.configuration.get_smtp_config_details.assert_called()

    def test_modify_smtp_config_details(self, smtp_config_module_mock):
        self.get_module_args.update({'smtp_id': 0,
                                     'smtp_address': "newsmtp.smtp.com",
                                     'source_email': "new_source@dell.com",
                                     'state': "present"})
        smtp_config_module_mock.module.params = self.get_module_args
        smtp_config_module_mock.configuration.get_smtp_config_details = MagicMock(
            return_value=MockSmtpConfigApi.SMTP_CONFIG_DETAILS)
        smtp_config_module_mock.perform_module_operation()
        assert self.get_module_args['smtp_id'] == smtp_config_module_mock.module.exit_json.call_args[1]['smtp_config_details']['id']
        smtp_config_module_mock.configuration.modify_smtp_config_details.assert_called()

    def test_send_test_email(self, smtp_config_module_mock):
        self.get_module_args.update({
            'smtp_id': 0,
            'destination_email': "abc_xyz@dell.com",
            'state': "present"
        })
        smtp_config_module_mock.module.params = self.get_module_args
        smtp_config_module_mock.perform_module_operation()
        smtp_config_module_mock.configuration.test_smtp_config.assert_called()

    def test_get_non_existing_smtp_config_details(self, smtp_config_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        invalid_smtp_id = 1
        self.get_module_args.update({
            'smtp_id': invalid_smtp_id,
            'state': "present"
        })
        smtp_config_module_mock.module.params = self.get_module_args
        smtp_config_module_mock.configuration.get_smtp_config_details = MagicMock(
            side_effect=MockApiException)
        smtp_config_module_mock.perform_module_operation()
        assert MockSmtpConfigApi.get_smtp_config_failed_msg() in \
            smtp_config_module_mock.module.fail_json.call_args[1]['msg']

    def test_delete_smtp(self, smtp_config_module_mock):
        smtp_id = 0
        self.get_module_args.update({'smtp_id': smtp_id,
                                     'state': "absent"})
        smtp_config_module_mock.module.params = self.get_module_args
        smtp_config_module_mock.configuration.get_smtp_config_details = MagicMock(
            return_value=MockSmtpConfigApi.SMTP_CONFIG_DETAILS)
        smtp_config_module_mock.perform_module_operation()
        assert MockSmtpConfigApi.delete_smtp_config_failed_msg() in \
            smtp_config_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_invalid_port(self, smtp_config_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        smtp_id = 0
        self.get_module_args.update({'smtp_id': smtp_id,
                                     'smtp_port': 28,
                                     'state': "present"})
        smtp_config_module_mock.module.params = self.get_module_args
        smtp_config_module_mock.configuration.get_smtp_config_details = MagicMock(
            return_value=MockSmtpConfigApi.SMTP_CONFIG_DETAILS)
        smtp_config_module_mock.configuration.modify_smtp_config_details = MagicMock(
            side_effect=MockApiException)
        smtp_config_module_mock.perform_module_operation()
        assert MockSmtpConfigApi.modify_smtp_config_failed_msg() in \
            smtp_config_module_mock.module.fail_json.call_args[1]['msg']
