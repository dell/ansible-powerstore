# Copyright: (c) 2023, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for storage container module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_storage_container_api import MockStorageContainerApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

remote_config = MagicMock()
remote_config.config_mgmt.get_storage_container_details = MagicMock(return_value=MockStorageContainerApi.REMOTE_STORAGE_CONTAINER_1)
utils.get_powerstore_connection = MagicMock(side_effect=[
    MagicMock(),
    remote_config
])
from ansible_collections.dellemc.powerstore.plugins.modules.storage_container import PowerStoreStorageContainer, StorageContainerHandler
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries.\
    fail_json import FailJsonException, fail_json


class TestPowerStoreStorageContainer():

    get_module_args = MockStorageContainerApi.STORAGE_CONTAINER_COMMON_ARGS

    @pytest.fixture
    def storage_container_module_mock(self, mocker):
        mocker.patch(MockStorageContainerApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        storage_container_module_mock = PowerStoreStorageContainer()
        storage_container_module_mock.module = MagicMock()
        storage_container_module_mock.module.check_mode = False
        storage_container_module_mock.module.fail_json = fail_json
        return storage_container_module_mock

    def capture_fail_json_call(self, error_msg, storage_container_module_mock):
        try:
            StorageContainerHandler().handle(
                storage_container_module_mock,
                storage_container_module_mock.module.params)
        except FailJsonException as fj_object:
            assert error_msg in fj_object.message

    def test_get_storage_container_response(self, storage_container_module_mock):
        self.get_module_args.update({
            'storage_container_id': "storage_container_id",
            'state': "present"
        })
        storage_container_module_mock.module.params = self.get_module_args
        StorageContainerHandler().handle(storage_container_module_mock, storage_container_module_mock.module.params)
        storage_container_module_mock.configuration.get_storage_container_details.assert_called()

    def test_get_storage_container_exception(self, storage_container_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'storage_container_id': 16,
            'state': "present"
        })
        storage_container_module_mock.module.params = self.get_module_args
        storage_container_module_mock.configuration.get_storage_container_details = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockStorageContainerApi.get_storage_container_exception_response(
                'get_container_exception'), storage_container_module_mock)

    def test_get_storage_container_response_with_name(self, storage_container_module_mock):
        self.get_module_args.update({
            'storage_container_name': MockStorageContainerApi.STORAGE_CONTAINER_NAME_1,
            'state': "present"
        })
        storage_container_module_mock.module.params = self.get_module_args
        StorageContainerHandler().handle(storage_container_module_mock, storage_container_module_mock.module.params)
        storage_container_module_mock.configuration.get_storage_container_details_by_name.assert_called()

    def test_create_storage_container(self, storage_container_module_mock):
        self.get_module_args.update({'storage_container_name': MockStorageContainerApi.STORAGE_CONTAINER_NAME_1,
                                     'quota': 0,
                                     'storage_protocol': "SCSI",
                                     'high_water_mark': 60,
                                     'state': "present"})
        storage_container_module_mock.module.params = self.get_module_args
        storage_container_module_mock.configuration.get_storage_container_details_by_name = MagicMock(
            return_value=None)
        StorageContainerHandler().handle(storage_container_module_mock, storage_container_module_mock.module.params)
        storage_container_module_mock.configuration.create_storage_container.assert_called()

    def test_create_storage_container_exception(self, storage_container_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({'storage_container_name': MockStorageContainerApi.STORAGE_CONTAINER_NAME_1,
                                     'quota': 10,
                                     'storage_protocol': "SCSI",
                                     'high_water_mark': 60,
                                     'state': "present"})
        storage_container_module_mock.module.params = self.get_module_args
        storage_container_module_mock.configuration.get_storage_container_details_by_name = MagicMock(
            return_value=None)
        storage_container_module_mock.configuration.create_storage_container = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockStorageContainerApi.get_storage_container_exception_response(
                'create_container_exception'), storage_container_module_mock)

    def test_modify_storage_container(self, storage_container_module_mock):
        self.get_module_args.update({'storage_container_id': "storage_container_id_1",
                                     'quota': 0,
                                     'storage_protocol': "NVMe",
                                     'new_name': "New_storage_container_name",
                                     'state': "present"})
        storage_container_module_mock.module.params = self.get_module_args
        storage_container_module_mock.configuration.get_storage_container_details = MagicMock(
            return_value=MockStorageContainerApi.STORAGE_CONTAINER_DETAILS)
        StorageContainerHandler().handle(storage_container_module_mock, storage_container_module_mock.module.params)

    def test_modify_storage_container_exception(self, storage_container_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({'storage_container_id': "storage_container_id_1",
                                     'quota': 0,
                                     'storage_protocol': "NVMe",
                                     'new_name': "New_storage_container_name",
                                     'state': "present"})
        storage_container_module_mock.module.params = self.get_module_args
        storage_container_module_mock.configuration.get_storage_container_details = MagicMock(
            return_value=MockStorageContainerApi.STORAGE_CONTAINER_DETAILS)
        storage_container_module_mock.configuration.modify_storage_container_details = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockStorageContainerApi.get_storage_container_exception_response(
                'modify_container_exception'), storage_container_module_mock)

    def test_delete_storage_container(self, storage_container_module_mock):
        self.get_module_args.update({
            'storage_container_name': MockStorageContainerApi.STORAGE_CONTAINER_NAME_1,
            'state': "absent"
        })
        storage_container_module_mock.module.params = self.get_module_args
        StorageContainerHandler().handle(storage_container_module_mock, storage_container_module_mock.module.params)
        storage_container_module_mock.configuration.delete_storage_container.assert_called()

    def test_delete_storage_container_exception(self, storage_container_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'storage_container_name': MockStorageContainerApi.STORAGE_CONTAINER_NAME_1,
            'state': "absent"
        })
        storage_container_module_mock.module.params = self.get_module_args
        storage_container_module_mock.configuration.delete_storage_container = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockStorageContainerApi.get_storage_container_exception_response(
                'delete_container_exp'), storage_container_module_mock)

    def before_destinations_operation(self, storage_container_module_mock):
        self.get_module_args.update({
            'storage_container_name': MockStorageContainerApi.STORAGE_CONTAINER_NAME_1,
            'storage_container_destination': {
                "remote_address": MockStorageContainerApi.MASKED_VALUE,
                "user": "user",
                "password": MockStorageContainerApi.MASKED_VALUE,
                "verifycert": False,
                "port": 443,
                "timeout": 120,
                "remote_system": MockStorageContainerApi.REMOTE_SYS_NAME,
                "remote_storage_container": MockStorageContainerApi.STORAGE_CONTAINER_NAME_1
            },
            'state': "present"})
        storage_container_module_mock.module.params = self.get_module_args
        storage_container_module_mock.configuration.get_storage_container_details = MagicMock(
            return_value=MockStorageContainerApi.CREATE_STORAGE_CONTAINER_DESTINATION)

    def test_create_storage_container_destination(self, storage_container_module_mock):
        self.before_destinations_operation(storage_container_module_mock)
        storage_container_module_mock.protection.get_remote_system_by_name = MagicMock(
            return_value=MockStorageContainerApi.REMOTE_SYSTEM_DETAILS)
        storage_container_module_mock.get_remote_storage_container = MagicMock(
            return_value=MockStorageContainerApi.REMOTE_STORAGE_CONTAINER)
        StorageContainerHandler().handle(storage_container_module_mock, storage_container_module_mock.module.params)
        storage_container_module_mock.configuration.create_storage_container_destination.assert_called()

    def test_create_sc_destination_exception(self, storage_container_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.before_destinations_operation(storage_container_module_mock)
        storage_container_module_mock.protection.get_remote_system_by_name = MagicMock(
            return_value=MockStorageContainerApi.REMOTE_SYSTEM_DETAILS1)
        storage_container_module_mock.configuration.create_storage_container_destination = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockStorageContainerApi.get_storage_container_exception_response(
                'create_destination_exp'), storage_container_module_mock)

    def before_sc_destination_delete(self, storage_container_module_mock):
        self.get_module_args.update({
            'storage_container_name': MockStorageContainerApi.STORAGE_CONTAINER_NAME_1,
            'storage_container_destination_state': 'absent',
            'storage_container_destination': {
                "remote_address": MockStorageContainerApi.MASKED_VALUE,
                "user": "user",
                "password": MockStorageContainerApi.MASKED_VALUE,
                "validate_certs": False,
                "port": 443,
                "timeout": 120,
                "remote_system": MockStorageContainerApi.REMOTE_SYS_ID,
                "remote_storage_container": MockStorageContainerApi.REMOTE_SC_ID
            },
            'state': "present"})
        storage_container_module_mock.module.params = self.get_module_args

    def test_delete_storage_container_destination(self, storage_container_module_mock):
        self.before_sc_destination_delete(storage_container_module_mock)
        storage_container_module_mock.configuration.get_storage_container_details = MagicMock(
            return_value=MockStorageContainerApi.REMOTE_STORAGE_CONTAINER_1)
        storage_container_module_mock.protection.get_remote_system_details = MagicMock(
            return_value=MockStorageContainerApi.REMOTE_SYSTEM_DETAILS[0])
        StorageContainerHandler().handle(storage_container_module_mock, storage_container_module_mock.module.params)
        storage_container_module_mock.configuration.delete_storage_container_destination.assert_called()

    def test_delete_storage_container_destination_exp(self, storage_container_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.before_sc_destination_delete(storage_container_module_mock)
        storage_container_module_mock.configuration.get_storage_container_details = MagicMock(
            return_value=MockStorageContainerApi.CREATE_STORAGE_CONTAINER_DESTINATION)
        storage_container_module_mock.protection.get_remote_system_details = MagicMock(
            return_value=MockStorageContainerApi.REMOTE_SYSTEM_DETAILS[0])
        storage_container_module_mock.get_remote_storage_container = MagicMock(
            return_value=MockStorageContainerApi.REMOTE_STORAGE_CONTAINER_1)
        storage_container_module_mock.configuration.delete_storage_container_destination = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockStorageContainerApi.get_storage_container_exception_response(
            'delete_destination_exp'), storage_container_module_mock)

    def test_delete_storage_container_destination_empty_remote_container(self, storage_container_module_mock):
        self.get_module_args.update({
            'storage_container_name': MockStorageContainerApi.STORAGE_CONTAINER_NAME_1,
            'storage_container_destination_state': 'absent',
            'state': "present"})
        storage_container_module_mock.module.params = self.get_module_args
        storage_container_module_mock.configuration.get_storage_container_details = MagicMock(
            return_value=MockStorageContainerApi.CREATE_STORAGE_CONTAINER_DESTINATION)
        self.capture_fail_json_call(MockStorageContainerApi.get_storage_container_exception_response(
            'remote_dict_exception'), storage_container_module_mock)

    def test_get_remote_system_exception(self, storage_container_module_mock):
        self.before_destinations_operation(storage_container_module_mock)
        storage_container_module_mock.protection.get_remote_system_by_name = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockStorageContainerApi.get_storage_container_exception_response(
            'remote_system_exception'), storage_container_module_mock)

    def test_get_remote_storage_container_exception(self, storage_container_module_mock):
        self.before_destinations_operation(storage_container_module_mock)
        storage_container_module_mock.configuration.get_storage_container_details = MagicMock(
            return_value=MockStorageContainerApi.CREATE_STORAGE_CONTAINER_DESTINATION)
        storage_container_module_mock.protection.get_remote_system_by_name = MagicMock(
            return_value=MockStorageContainerApi.REMOTE_SYSTEM_DETAILS)
        storage_container_module_mock.get_remote_storage_container = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockStorageContainerApi.get_sc_exception(
            'remote_none_sc'), storage_container_module_mock)

    def test_get_remote_system_none_exception(self, storage_container_module_mock):
        self.before_destinations_operation(storage_container_module_mock)
        storage_container_module_mock.get_storage_container_details = MagicMock(
            return_value=MockStorageContainerApi.CREATE_STORAGE_CONTAINER_DESTINATION)
        storage_container_module_mock.get_remote_system = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockStorageContainerApi.get_sc_exception(
            'remote_sys_none'), storage_container_module_mock)

    def test_delete_storage_container_destination_get_remote_sc_exp(self, storage_container_module_mock):
        self.before_sc_destination_delete(storage_container_module_mock)
        storage_container_module_mock.configuration.get_storage_container_details = MagicMock(
            return_value=MockStorageContainerApi.CREATE_STORAGE_CONTAINER_DESTINATION)
        storage_container_module_mock.protection.get_remote_system_details = MagicMock(
            return_value=MockStorageContainerApi.REMOTE_SYSTEM_DETAILS[0])
        storage_container_module_mock.get_remote_storage_container = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockStorageContainerApi.get_sc_exception(
            'remote_none_sc'), storage_container_module_mock)

    def test_delete_storage_container_destination_get_remote_sys_exp(self, storage_container_module_mock):
        self.before_sc_destination_delete(storage_container_module_mock)
        storage_container_module_mock.get_storage_container_details = MagicMock(
            return_value=MockStorageContainerApi.CREATE_STORAGE_CONTAINER_DESTINATION)
        storage_container_module_mock.get_remote_system = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockStorageContainerApi.get_sc_exception(
            'remote_sys_none'), storage_container_module_mock)

    def test_get_remote_system_invalid_addr_exception(self, storage_container_module_mock):
        self.get_module_args.update({
            'storage_container_name': MockStorageContainerApi.STORAGE_CONTAINER_NAME_1,
            'storage_container_destination': {
                "remote_address": MockStorageContainerApi.MASKED_VALUE1,
                "user": "user",
                "password": MockStorageContainerApi.MASKED_VALUE,
                "verifycert": False,
                "port": 443,
                "timeout": 120,
                "remote_system": MockStorageContainerApi.REMOTE_SYS_NAME,
                "remote_storage_container": MockStorageContainerApi.STORAGE_CONTAINER_NAME_1
            },
            'state': "present"})
        storage_container_module_mock.module.params = self.get_module_args
        storage_container_module_mock.configuration.get_storage_container_details = MagicMock(
            return_value=MockStorageContainerApi.CREATE_STORAGE_CONTAINER_DESTINATION)
        storage_container_module_mock.protection.get_remote_system_by_name = MagicMock(
            return_value=MockStorageContainerApi.REMOTE_SYSTEM_DETAILS1)
        self.capture_fail_json_call(MockStorageContainerApi.get_sc_exception(
            'invalid_remote_addr'), storage_container_module_mock)
