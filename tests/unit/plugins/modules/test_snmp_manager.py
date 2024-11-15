# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for storage container module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_snmp_manager_api import MockSNMPManagerApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries.powerstore_unit_base \
    import PowerStoreUnitBase
from ansible_collections.dellemc.powerstore.plugins.modules.snmp_manager import PowerStoreSNMPManager, SNMPManagerHandler


class TestPowerStoreSNMPManager(PowerStoreUnitBase):

    get_module_args = MockSNMPManagerApi.SNMP_MANAGER_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerStoreSNMPManager

    def test_get_snmp_manager(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock, self.get_module_args,
            {
                "ip_address": "127.0.0.1"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.snmp_manager.get_snmp_server_list = MagicMock(return_value=MockSNMPManagerApi.GET_SNMP_MANAGER_LIST)
        powerstore_module_mock.snmp_manager.get_snmp_server_details = MagicMock(
            return_value=MockSNMPManagerApi.GET_SNMP_MANAGER_DETAILS)
        SNMPManagerHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.snmp_manager.get_snmp_server_details.assert_called()
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_get_snmp_manager_list_exception(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock, self.get_module_args,
            {
                "ip_address": "127.0.0.1"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.snmp_manager.get_snmp_server_list = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_call(
            MockSNMPManagerApi.get_snmp_manager_exception_response('get_snmp_manager_list_exception'),
            powerstore_module_mock, SNMPManagerHandler)

    def test_get_snmp_manager_id_exception(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock, self.get_module_args,
            {
                "ip_address": "127.0.0.1"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.snmp_manager.get_snmp_server_list = MagicMock(return_value=MockSNMPManagerApi.GET_SNMP_MANAGER_LIST)
        powerstore_module_mock.snmp_manager.get_snmp_server_details = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_call(
            MockSNMPManagerApi.get_snmp_manager_exception_response('get_snmp_manager_id_exception'),
            powerstore_module_mock, SNMPManagerHandler)

    def test_create_snmp_manager(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock, self.get_module_args,
            {
                "ip_address": "127.0.0.1"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.get_snmp_manager = MagicMock(return_value=None)
        powerstore_module_mock.snmp_manager.create_snmp_server = MagicMock(return_value=MockSNMPManagerApi.CREATE_SNMP_MANAGER_DETAILS)
        SNMPManagerHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_snmp_manager_check_mode(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock, self.get_module_args,
            {
                "ip_address": "127.0.0.1"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.module.check_mode = True
        powerstore_module_mock.get_snmp_manager = MagicMock(return_value=None)
        powerstore_module_mock.snmp_manager.create_snmp_server = MagicMock(return_value=MockSNMPManagerApi.CREATE_SNMP_MANAGER_DETAILS)
        SNMPManagerHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_snmp_manager_exception(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock, self.get_module_args,
            {
                "ip_address": "127.0.0.1"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.get_snmp_manager = MagicMock(return_value=None)
        powerstore_module_mock.snmp_manager.create_snmp_server = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_call(
            MockSNMPManagerApi.get_snmp_manager_exception_response('create_snmp_manager_exception'),
            powerstore_module_mock, SNMPManagerHandler)

    def test_delete_snmp_manager(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock, self.get_module_args,
            {
                "ip_address": "127.0.0.1",
                "state": "absent"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.getting_snmp_manager_id = MagicMock(return_value=MockSNMPManagerApi.GET_SNMP_MANAGER_DETAILS['id'])
        powerstore_module_mock.get_snmp_manager = MagicMock(return_value=MockSNMPManagerApi.GET_SNMP_MANAGER_DETAILS)
        powerstore_module_mock.snmp_manager.delete_snmp_server = MagicMock(return_value=True)
        SNMPManagerHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_delete_snmp_manager_exception(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock, self.get_module_args,
            {
                "ip_address": "127.0.0.1",
                "state": "absent"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.getting_snmp_manager_id = MagicMock(return_value=MockSNMPManagerApi.GET_SNMP_MANAGER_DETAILS['id'])
        powerstore_module_mock.get_snmp_manager = MagicMock(return_value=MockSNMPManagerApi.GET_SNMP_MANAGER_DETAILS)
        powerstore_module_mock.snmp_manager.delete_snmp_server = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_call(
            MockSNMPManagerApi.get_snmp_manager_exception_response('delete_snmp_manager_exception'),
            powerstore_module_mock, SNMPManagerHandler)

    def test_modify_snmp_manager(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock, self.get_module_args,
            {
                "ip_address": "127.0.0.1",
                "new_ip_address": "127.0.0.2",
                "snmp_username": "new_user",
                "auth_protocol": "SHA256",
                "auth_privacy": "TDES",
                "state": "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.getting_snmp_manager_id = MagicMock(return_value=MockSNMPManagerApi.GET_SNMP_MANAGER_DETAILS['id'])
        powerstore_module_mock.get_snmp_manager = MagicMock(return_value=MockSNMPManagerApi.GET_SNMP_MANAGER_DETAILS)
        powerstore_module_mock.snmp_manager.modify_snmp_server = MagicMock(return_value=True)
        SNMPManagerHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_snmp_manager_v2c(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock, self.get_module_args,
            {
                'version': 'V2c',
                "trap_community": "new_community",
                "auth_protocol": "Nil",
                "auth_privacy": "Nil",
                "state": "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.getting_snmp_manager_id = MagicMock(return_value=MockSNMPManagerApi.GET_SNMP_MANAGER_DETAILS_V2c['id'])
        powerstore_module_mock.get_snmp_manager = MagicMock(return_value=MockSNMPManagerApi.GET_SNMP_MANAGER_DETAILS_V2c)
        powerstore_module_mock.snmp_manager.modify_snmp_server = MagicMock(return_value=True)
        SNMPManagerHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_snmp_manager_exception(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock, self.get_module_args,
            {
                "ip_address": "127.0.0.1",
                "new_ip_address": "127.0.0.2",
                "state": "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.getting_snmp_manager_id = MagicMock(return_value=MockSNMPManagerApi.GET_SNMP_MANAGER_DETAILS['id'])
        powerstore_module_mock.get_snmp_manager = MagicMock(return_value=MockSNMPManagerApi.GET_SNMP_MANAGER_DETAILS)
        powerstore_module_mock.snmp_manager.modify_snmp_server = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_call(
            MockSNMPManagerApi.get_snmp_manager_exception_response('modify_snmp_manager_exception'),
            powerstore_module_mock, SNMPManagerHandler)

    def test_create_snmp_manager_error_msg_validation_1(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock, self.get_module_args,
            {
                "ip_address": ""
            })
        powerstore_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(
            MockSNMPManagerApi.get_snmp_validation_error_response('create_without_ip_exception'),
            powerstore_module_mock, SNMPManagerHandler)

    def test_create_snmp_manager_error_msg_validation_4(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock, self.get_module_args,
            {
                "ip_address": "127.0.0.1",
                "version": "V2c",
                "trap_community": ""
            })
        powerstore_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(
            MockSNMPManagerApi.get_snmp_validation_error_response('trap_community_error'),
            powerstore_module_mock, SNMPManagerHandler)

    def test_create_snmp_manager_error_msg_validation_6(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock, self.get_module_args,
            {
                "ip_address": "127.0.0.1",
                "version": "V3",
                "snmp_username": ""
            })
        powerstore_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(
            MockSNMPManagerApi.get_snmp_validation_error_response('create_without_snmp_username'),
            powerstore_module_mock, SNMPManagerHandler)

    def test_create_snmp_manager_error_msg_validation_7(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock, self.get_module_args,
            {
                "ip_address": "127.0.0.1",
                "version": "V3",
                "auth_protocol": "MD5",
                "snmp_password": ""
            })
        powerstore_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(
            MockSNMPManagerApi.get_snmp_validation_error_response('create_without_snmp_password'),
            powerstore_module_mock, SNMPManagerHandler)

    def test_create_snmp_manager_error_msg_validation_8(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock, self.get_module_args,
            {
                "ip_address": "127.0.0.1",
                "version": "V3",
                "auth_protocol": "Nil",
                "auth_privacy": "AES256",
                "snmp_password": MockSNMPManagerApi.PASSWORD
            })
        powerstore_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(
            MockSNMPManagerApi.get_snmp_validation_error_response('create_without_auth_protocol'),
            powerstore_module_mock, SNMPManagerHandler)

    def test_create_snmp_manager_error_msg_validation_9(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock, self.get_module_args,
            {
                "ip_address": "127.0.0.1",
                "version": "V3",
                "auth_protocol": "Nil",
                "auth_privacy": "Nil",
                "snmp_password": MockSNMPManagerApi.PASSWORD
            })
        powerstore_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(
            MockSNMPManagerApi.get_snmp_validation_error_response('create_without_protocol'),
            powerstore_module_mock, SNMPManagerHandler)

    def test_modify_snmp_manager_error_msg_validation(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock, self.get_module_args,
            {
                'version': 'V2c',
                "trap_community": "new_community",
                "auth_protocol": "Nil",
                "auth_privacy": "Nil",
                "state": "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(
            MockSNMPManagerApi.get_snmp_validation_error_response('modify_version_error_message'),
            powerstore_module_mock, SNMPManagerHandler)
