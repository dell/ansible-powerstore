# Copyright: (c) 2024, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Security Config module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_security_config_api import MockSecurityConfigApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.security_config import PowerStoreSecurityConfig, main
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries.powerstore_unit_base \
    import PowerStoreUnitBase


class TestPowerstoreSecurityConfig(PowerStoreUnitBase):

    get_module_args = MockSecurityConfigApi.SECURITY_CONFIG_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerStoreSecurityConfig

    def test_get_security_config_response(self, powerstore_module_mock):
        MockSecurityConfigApi.get_security_config_response('api')
        self.get_module_args.update({
            'security_config_id': "1",
            'state': "present"
        })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.perform_module_operation()
        powerstore_module_mock.configuration.get_security_config_details.assert_called()

    def test_modify_security_config_response(self, powerstore_module_mock):
        MockSecurityConfigApi.modify_security_config_response('module')
        self.get_module_args.update({
            'security_config_id': "1",
            'protocol_mode': "TLSv1_1",
            'state': "present"
        })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.perform_module_operation()
        powerstore_module_mock.configuration.modify_security_config.assert_called()

    def test_modify_security_config_invalid_protocol_mode_response(self, powerstore_module_mock):
        MockSecurityConfigApi.modify_security_config_response('module')
        self.get_module_args.update({
            'security_config_id': "1",
            'protocol_mode': "TLSv1_3",
            'state': "present"
        })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.perform_module_operation()
        powerstore_module_mock.configuration.modify_security_config.assert_called()

    def test_get_security_config_details_exp(self, powerstore_module_mock):
        security_config_id = 1
        powerstore_module_mock.configuration.get_security_config_details = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockSecurityConfigApi.get_error_message("scd_exp"),
            powerstore_module_mock, "get_security_config_details",
            security_config_id
        )

    def test_modify_security_config_exp(self, powerstore_module_mock):
        security_config_id = 1
        protocol_mode = "TLSv1_1"
        powerstore_module_mock.configuration.modify_security_config = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockSecurityConfigApi.get_error_message("msc_exp"),
            powerstore_module_mock, "modify_security_config",
            security_config_id, protocol_mode
        )

    @pytest.mark.parametrize('params', [
        {"state": "present", "exp_key": "pm_exp1"},
        {"state": "absent", "scd": "scd1", "exp_key": "pm_exp2"}
    ])
    def test_perform_module_operation_exp(self, powerstore_module_mock, params):
        MockSecurityConfigApi.modify_security_config_response('module')
        self.get_module_args.update({
            'security_config_id': "1",
            'protocol_mode': "TLSv1_3",
            'state': params.get('state', None)
        })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.get_security_config_details = MagicMock(
            return_value=params.get('scd', None)
        )
        self.capture_fail_json_method(
            MockSecurityConfigApi.get_error_message(
                params.get('exp_key', None)),
            powerstore_module_mock, "perform_module_operation"
        )

    def test_main(self, mocker):
        mock_obj = mocker.patch(MockSecurityConfigApi.MODULE_PATH,
                                new=PowerStoreSecurityConfig)
        mock_obj.perform_module_operation = MagicMock(
            return_value=None)
        main()
