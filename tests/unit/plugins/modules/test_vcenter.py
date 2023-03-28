# Copyright: (c) 2023, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for vCenter module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_vcenter_api import MockVCenterApi
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
from ansible_collections.dellemc.powerstore.plugins.modules.vcenter import PowerstoreVCenter


class TestPowerstoreVolume():
    get_module_args = MockVCenterApi.VCENTER_COMMON_ARGS

    @pytest.fixture
    def vcenter_module_mock(self, mocker):
        mocker.patch(MockVCenterApi.MODULE_UTILS_PATH + '.PowerStoreException',
                     new=MockApiException)
        vcenter_module_mock = PowerstoreVCenter()
        vcenter_module_mock.module = MagicMock()
        vcenter_module_mock.module.check_mode = False
        return vcenter_module_mock

    def test_get_vcenter_by_id(self, vcenter_module_mock):
        self.get_module_args.update({
            'vcenter_id': MockVCenterApi.ID_1
        })
        vcenter_module_mock.module.params = self.get_module_args
        vcenter_module_mock.configuration.get_vcenter_details = MagicMock(
            return_value=MockVCenterApi.VCENTER_DETAILS_1)
        vcenter_module_mock.perform_module_operation()
        vcenter_module_mock.configuration.get_vcenter_details.assert_called()
        assert self.get_module_args['vcenter_id'] == \
               vcenter_module_mock.module.exit_json.call_args[
                   1]['vcenter_details']['id']

    def before_modify_vcenter(self, vcenter_module_mock):
        self.get_module_args.update({
            "vcenter_id": MockVCenterApi.ID_1,
            "address": MockVCenterApi.SAMPLE_ADDRESS1,
            "vcenter_username": MockVCenterApi.USERNAME_2,
            "vcenter_password": MockVCenterApi.PASS_STR,
            "update_password": "always",
            "vasa_provider_credentials": {
                "username": MockVCenterApi.USERNAME_1,
                "password": MockVCenterApi.PASS_STR
            },
            "state": "present"
        })
        vcenter_module_mock.module.params = self.get_module_args
        vcenter_module_mock.configuration.get_vcenter_details = MagicMock(
            return_value=MockVCenterApi.VCENTER_DETAILS_1)

    def test_add_vcenter(self, vcenter_module_mock):
        self.get_module_args.update({
            "address": MockVCenterApi.SAMPLE_ADDRESS,
            "vcenter_username": MockVCenterApi.USERNAME_1,
            "vcenter_password": MockVCenterApi.PASS_STR,
            "vasa_provider_credentials": {
                "username": MockVCenterApi.USERNAME_1,
                "password": MockVCenterApi.PASS_STR
            },
            "state": "present"
        })
        vcenter_module_mock.module.params = self.get_module_args
        vcenter_module_mock.configuration.get_vcenter_details = MagicMock(
            return_value=None)
        vcenter_module_mock.perform_module_operation()
        vcenter_module_mock.configuration.add_vcenter.assert_called()
        assert vcenter_module_mock.module.exit_json.call_args[1]['changed'] \
               is True

    def test_modify_vcenter(self, vcenter_module_mock):
        self.before_modify_vcenter(vcenter_module_mock)
        vcenter_module_mock.perform_module_operation()
        vcenter_module_mock.configuration.modify_vcenter.assert_called()
        assert vcenter_module_mock.module.exit_json.call_args[1]['changed'] \
               is True

    def test_modify_vcenter_exception(self, vcenter_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.before_modify_vcenter(vcenter_module_mock)
        vcenter_module_mock.configuration.modify_vcenter = MagicMock(
            side_effect=MockApiException)
        vcenter_module_mock.perform_module_operation()
        vcenter_module_mock.configuration.modify_vcenter.assert_called()
        assert MockVCenterApi.modify_vcenter_exception_failed_msg() in \
               vcenter_module_mock.module.fail_json.call_args[1]['msg']

    def test_remove_vcenter(self, vcenter_module_mock):
        self.get_module_args.update({
            "vcenter_id": MockVCenterApi.ID_1,
            "delete_vasa_provider": True,
            "state": "absent"
        })
        vcenter_module_mock.module.params = self.get_module_args
        vcenter_module_mock.configuration.get_vcenter_details = MagicMock(
            return_value=MockVCenterApi.VCENTER_DETAILS_2[0])
        vcenter_module_mock.perform_module_operation()
        vcenter_module_mock.configuration.remove_vcenter.assert_called()
        assert vcenter_module_mock.module.exit_json.call_args[1]['changed'] \
               is True

    def test_remove_vcenter_exception(self, vcenter_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            "vcenter_id": MockVCenterApi.ID_1,
            "delete_vasa_provider": True,
            "state": "absent"
        })
        vcenter_module_mock.module.params = self.get_module_args
        vcenter_module_mock.configuration.get_vcenter_details = MagicMock(
            return_value=MockVCenterApi.VCENTER_DETAILS_2[0])
        vcenter_module_mock.configuration.remove_vcenter = MagicMock(
            side_effect=MockApiException)
        vcenter_module_mock.perform_module_operation()
        vcenter_module_mock.configuration.remove_vcenter.assert_called()
        assert MockVCenterApi.remove_vcenter_exception_failed_msg() in \
               vcenter_module_mock.module.fail_json.call_args[1]['msg']

    def test_add_vcenter_with_empty_param(self, vcenter_module_mock):
        self.get_module_args.update({
            "address": " x . y",
            "vcenter_username": MockVCenterApi.USERNAME_2,
            "vcenter_password": MockVCenterApi.PASS_STR,
            "state": "present"
        })
        vcenter_module_mock.module.params = self.get_module_args
        vcenter_module_mock.perform_module_operation()
        assert MockVCenterApi.invalid_param_failed_msg() in \
               vcenter_module_mock.module.fail_json.call_args[1]['msg']

    def test_add_vcenter_without_param(self, vcenter_module_mock):
        self.get_module_args.update({
            "address": MockVCenterApi.SAMPLE_ADDRESS1,
            "state": "present"
        })
        vcenter_module_mock.module.params = self.get_module_args
        vcenter_module_mock.perform_module_operation()
        assert MockVCenterApi.add_vcenter_without_param_failed_msg() in \
               vcenter_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_vcenter_by_id_exception(self, vcenter_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vcenter_id': MockVCenterApi.ID_1
        })
        vcenter_module_mock.module.params = self.get_module_args
        vcenter_module_mock.configuration.get_vcenter_details = MagicMock(
            side_effect=MockApiException)
        vcenter_module_mock.perform_module_operation()
        vcenter_module_mock.configuration.get_vcenter_details.assert_called()
        assert MockVCenterApi.get_vcenter_exception_failed_msg() in \
               vcenter_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_vcenter_by_id_not_found_exception(self, vcenter_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'vcenter_id': MockVCenterApi.ID_1
        })
        vcenter_module_mock.module.params = self.get_module_args
        vcenter_module_mock.configuration.get_vcenter_details = MagicMock(
            side_effect=MockApiException)
        vcenter_module_mock.perform_module_operation()
        vcenter_module_mock.configuration.get_vcenter_details.assert_called()

    def test_add_vcenter_idempotency(self, vcenter_module_mock):
        self.get_module_args.update({
            "address": MockVCenterApi.SAMPLE_ADDRESS1,
            "vcenter_username": MockVCenterApi.USERNAME_2,
            "vcenter_password": MockVCenterApi.PASS_STR,
            "update_password": "on_create",
            "vasa_provider_credentials": {
                "username": MockVCenterApi.USERNAME_1,
                "password": MockVCenterApi.PASS_STR
            },
            "state": "present"
        })
        vcenter_module_mock.module.params = self.get_module_args
        vcenter_module_mock.configuration.get_vcenters = MagicMock(
            return_value=MockVCenterApi.VCENTER_DETAILS_2)
        vcenter_module_mock.perform_module_operation()
        vcenter_module_mock.configuration.get_vcenters.assert_called()
        assert vcenter_module_mock.module.exit_json.call_args[1]['changed'] \
               is False
