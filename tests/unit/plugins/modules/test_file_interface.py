# Copyright: (c) 2024, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)
"""Unit Tests for file interface module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import

from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_file_interface_api import MockFileInterfaceApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception import MockApiException

from ansible_collections.dellemc.powerstore.plugins.modules.file_interface import PowerStoreFileInterface, FileInterfaceHandler
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries.fail_json import FailJsonException, fail_json


class TestPowerStoreFileInterface():

    get_module_args = MockFileInterfaceApi.FILE_INTERFACE_COMMON_ARGS

    @pytest.fixture
    def file_interface_module_mock(self, mocker):
        mocker.patch(MockFileInterfaceApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        file_interface_module_mock = PowerStoreFileInterface()
        file_interface_module_mock.module = MagicMock()
        file_interface_module_mock.module.check_mode = False
        file_interface_module_mock.module.fail_json = fail_json
        return file_interface_module_mock

    def capture_fail_json_call(self, error_msg, file_interface_module_mock):
        try:
            FileInterfaceHandler().handle(
                file_interface_module_mock,
                file_interface_module_mock.module.params)
        except FailJsonException as fj_object:
            assert error_msg in fj_object.message

    def test_get_file_interface_response(self, file_interface_module_mock):
        self.get_module_args.update({
            'file_interface_id': "file_interface_id",
            'state': "present"
        })
        file_interface_module_mock.module.params = self.get_module_args
        FileInterfaceHandler().handle(file_interface_module_mock, file_interface_module_mock.module.params)
        file_interface_module_mock.file_interface.get_file_interface_details.assert_called()

    def test_get_file_interface_nas_ip_response(self, file_interface_module_mock):
        self.get_module_args.update({
            'nas_server_id': "nas_server_id",
            'ip_address': "10.10.10.11",
            'state': "present"
        })
        file_interface_module_mock.module.params = self.get_module_args
        FileInterfaceHandler().handle(file_interface_module_mock, file_interface_module_mock.module.params)
        file_interface_module_mock.file_interface.get_file_interface_by_nas_server_id.assert_called()

    def test_get_file_interface_exception(self, file_interface_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'file_interface_id': 'invalid_id',
            'state': "present"
        })
        file_interface_module_mock.module.params = self.get_module_args
        file_interface_module_mock.file_interface.get_file_interface_details = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockFileInterfaceApi.get_file_interface_exception_response(
                'get_file_interface_exception'), file_interface_module_mock)

    def test_create_file_interface_response(self, file_interface_module_mock):
        self.get_module_args.update({'nas_server_name': "sample_nas_server",
                                     'ip_address': "10.10.10.10",
                                     'prefix_length': 21,
                                     'vlan_id': 0,
                                     'gateway': "10.10.10.1",
                                     'role': "Production",
                                     'state': "present"})
        file_interface_module_mock.module.params = self.get_module_args
        file_interface_module_mock.file_interface.get_file_interface_details_by_nas_server_id = MagicMock(
            return_value=None)
        FileInterfaceHandler().handle(file_interface_module_mock, file_interface_module_mock.module.params)
        file_interface_module_mock.file_interface.create_file_interface.assert_called()

    def test_create_file_interface_exception(self, file_interface_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({'nas_server_name': "sample_nas_server",
                                     'ip_address': "10.10.10.10",
                                     'prefix_length': 21,
                                     'vlan_id': 0,
                                     'gateway': "10.10.10.1",
                                     'role': "Production",
                                     'state': "present"})
        file_interface_module_mock.module.params = self.get_module_args
        file_interface_module_mock.configuration.get_file_interface_details_by_nas_server_id = MagicMock(
            return_value=None)
        file_interface_module_mock.file_interface.create_file_interface = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockFileInterfaceApi.get_file_interface_exception_response(
                'create_file_interface_exception'), file_interface_module_mock)

    def test_modify_file_interface(self, file_interface_module_mock):
        self.get_module_args.update({'file_interface_id': MockFileInterfaceApi.FILE_INTERFACE_DETAILS['id'],
                                     'ip_address': "10.10.10.11",
                                     'state': "present"})
        file_interface_module_mock.module.params = self.get_module_args
        file_interface_module_mock.file_interface.get_file_interface_details = MagicMock(
            return_value=MockFileInterfaceApi.FILE_INTERFACE_DETAILS)
        FileInterfaceHandler().handle(file_interface_module_mock, file_interface_module_mock.module.params)
        file_interface_module_mock.file_interface.modify_file_interface.assert_called()

    def test_modify_file_interface_exception(self, file_interface_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({'file_interface_id': MockFileInterfaceApi.FILE_INTERFACE_DETAILS['id'],
                                     'ip_address': "10.10.10.11",
                                     'state': "present"})
        file_interface_module_mock.module.params = self.get_module_args
        file_interface_module_mock.file_interface.get_file_interface_details = MagicMock(
            return_value=MockFileInterfaceApi.FILE_INTERFACE_DETAILS)
        file_interface_module_mock.file_interface.modify_file_interface = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockFileInterfaceApi.get_file_interface_exception_response(
                'modify_file_interface_exception'), file_interface_module_mock)

    def test_delete_file_interface(self, file_interface_module_mock):
        self.get_module_args.update({
            'file_interface_id': MockFileInterfaceApi.FILE_INTERFACE_DETAILS['id'],
            'state': "absent"
        })
        file_interface_module_mock.module.params = self.get_module_args
        file_interface_module_mock.file_interface.get_file_interface_details = MagicMock(
            return_value=MockFileInterfaceApi.FILE_INTERFACE_DETAILS)
        FileInterfaceHandler().handle(file_interface_module_mock, file_interface_module_mock.module.params)
        file_interface_module_mock.file_interface.delete_file_interface.assert_called()

    def test_delete_file_interface_exception(self, file_interface_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'file_interface_id': MockFileInterfaceApi.FILE_INTERFACE_DETAILS['id'],
            'state': "absent"
        })
        file_interface_module_mock.module.params = self.get_module_args
        file_interface_module_mock.file_interface.get_file_interface_details = MagicMock(
            return_value=MockFileInterfaceApi.FILE_INTERFACE_DETAILS)
        file_interface_module_mock.file_interface.delete_file_interface = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockFileInterfaceApi.get_file_interface_exception_response(
                'delete_file_interface_exception'), file_interface_module_mock)
