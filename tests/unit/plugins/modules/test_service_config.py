# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for service config module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
from mock.mock import MagicMock
# pylint: disable=unused-import

from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries.initial_mock \
    import utils
from ansible_collections.dellemc.powerstore.plugins.modules.service_config import \
    ServiceConfigs
from ansible_collections.dellemc.powerstore.plugins.modules.service_config import \
    ServiceConfigsHandler
from ansible_collections.dellemc.powerstore.plugins.modules.service_config import \
    main

from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_service_configs_api \
    import MockServiceConfigApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception import \
    MockApiException
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries.powerstore_unit_base \
    import PowerStoreUnitBase


class TestServiceConfigs(PowerStoreUnitBase):

    get_module_args = MockServiceConfigApi.SERVICE_CONFIGS_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return ServiceConfigs

    def test_get_service_response(self, powerstore_module_mock):
        self.set_module_params(powerstore_module_mock, self.get_module_args, {})
        ServiceConfigsHandler().handle(
            powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.configuration.get_service_configs.assert_called()

    def test_get_service_exception(self, powerstore_module_mock):
        self.set_module_params(powerstore_module_mock, self.get_module_args, {})
        powerstore_module_mock.configuration.get_service_configs = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockServiceConfigApi.get_service_exception_response('get_service_config_exception'),
            powerstore_module_mock, ServiceConfigsHandler)

    def test_empty_appliance_name_exception(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                "service_config": [
                    {
                        "appliance_name": " ",
                        "is_ssh_enabled": True
                    }
                ]
            })
        powerstore_module_mock.configuration.get_service_configs = MagicMock(
            return_value=MockServiceConfigApi.SERVICE_CONFIGS_DETAILS)
        powerstore_module_mock.configuration.get_appliance_details = MagicMock(
            return_value=MockServiceConfigApi.APPLIANCE_DETAILS)
        self.capture_fail_json_call(
            MockServiceConfigApi.empty_app_exception('empty_appliance_exception', 'appliance_name'),
            powerstore_module_mock, ServiceConfigsHandler)

    def test_empty_appliance_id_exception(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                "service_config": [
                    {
                        "appliance_id": " ",
                        "is_ssh_enabled": True
                    }
                ]
            })
        powerstore_module_mock.configuration.get_service_configs = MagicMock(
            return_value=MockServiceConfigApi.SERVICE_CONFIGS_DETAILS)
        powerstore_module_mock.configuration.get_appliance_details = MagicMock(
            return_value=MockServiceConfigApi.APPLIANCE_DETAILS)
        self.capture_fail_json_call(
            MockServiceConfigApi.empty_app_exception('empty_appliance_exception', 'appliance_id'),
            powerstore_module_mock, ServiceConfigsHandler)

    def test_mutually_exclusive_exception(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                "service_config": [
                    {
                        "appliance_id": MockServiceConfigApi.APP_ID_1,
                        "appliance_name": MockServiceConfigApi.APP_NAME_1,
                        "is_ssh_enabled": True
                    }
                ]
            })
        powerstore_module_mock.configuration.get_service_configs = MagicMock(
            return_value=MockServiceConfigApi.SERVICE_CONFIGS_DETAILS)
        powerstore_module_mock.configuration.get_appliance_details = MagicMock(
            return_value=MockServiceConfigApi.APPLIANCE_DETAILS)
        self.capture_fail_json_call(
            MockServiceConfigApi.get_service_exception_response('mutually_exclusive_exception'),
            powerstore_module_mock, ServiceConfigsHandler)

    def test_required_one_exception(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                "service_config": [
                    {
                        "is_ssh_enabled": True
                    }
                ]
            })
        powerstore_module_mock.configuration.get_service_configs = MagicMock(
            return_value=MockServiceConfigApi.SERVICE_CONFIGS_DETAILS)
        powerstore_module_mock.configuration.get_appliance_details = MagicMock(
            return_value=MockServiceConfigApi.APPLIANCE_DETAILS)
        self.capture_fail_json_call(
            MockServiceConfigApi.get_service_exception_response('required_one_exception'),
            powerstore_module_mock, ServiceConfigsHandler)

    def test_get_appliance_exception(self, powerstore_module_mock):
        self.set_module_params(powerstore_module_mock, self.get_module_args, {})
        powerstore_module_mock.configuration.get_service_configs = MagicMock(
            return_value=MockServiceConfigApi.SERVICE_CONFIGS_DETAILS)
        powerstore_module_mock.configuration.get_appliance_details = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockServiceConfigApi.get_service_exception_response('appliance_exception'),
            powerstore_module_mock, ServiceConfigsHandler)

    def test_update_service_config_response(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                "service_config": [
                    {
                        "appliance_name": MockServiceConfigApi.APP_NAME_1,
                        "is_ssh_enabled": True
                    }
                ]
            })
        powerstore_module_mock.configuration.get_service_configs = MagicMock(
            return_value=MockServiceConfigApi.SERVICE_CONFIGS_DETAILS)
        powerstore_module_mock.configuration.get_appliance_details = MagicMock(
            return_value=MockServiceConfigApi.APPLIANCE_DETAILS)
        ServiceConfigsHandler().handle(
            powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.configuration.modify_service_config.assert_called()
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_update_service_config_exception(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                "service_config": [
                    {
                        "appliance_name": MockServiceConfigApi.APP_NAME_1,
                        "is_ssh_enabled": True
                    }
                ]
            })
        powerstore_module_mock.configuration.get_service_configs = MagicMock(
            return_value=MockServiceConfigApi.SERVICE_CONFIGS_DETAILS)
        powerstore_module_mock.configuration.get_appliance_details = MagicMock(
            return_value=MockServiceConfigApi.APPLIANCE_DETAILS)
        powerstore_module_mock.configuration.modify_service_config = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockServiceConfigApi.get_service_exception_response('update_service_config_exception'),
            powerstore_module_mock, ServiceConfigsHandler)

    def test_non_exisiting_app_exception(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                "service_config": [
                    {
                        "appliance_id": "A3",
                        "is_ssh_enabled": True
                    }
                ]
            })
        powerstore_module_mock.configuration.get_service_configs = MagicMock(
            return_value=MockServiceConfigApi.SERVICE_CONFIGS_DETAILS)
        powerstore_module_mock.configuration.get_appliance_details = MagicMock(
            return_value=MockServiceConfigApi.APPLIANCE_DETAILS)
        self.capture_fail_json_call(
            MockServiceConfigApi.get_service_exception_response('no_appliance_found'),
            powerstore_module_mock, ServiceConfigsHandler)

    def test_main(self):
        main()
