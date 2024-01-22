# Copyright: (c) 2024, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)
"""Unit Tests for file interface module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
# pylint: disable=unused-import

from ansible_collections.dellemc.powerstore.plugins.modules.file_interface import \
    PowerStoreFileInterface
from ansible_collections.dellemc.powerstore.plugins.modules.file_interface import \
    FileInterfaceHandler
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_file_interface_api \
    import MockFileInterfaceApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception import \
    MockApiException
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries.powerstore_unit_base \
    import PowerStoreUnitBase


class TestPowerStoreFileInterface(PowerStoreUnitBase):

    get_module_args = MockFileInterfaceApi.FILE_INTERFACE_COMMON_ARGS
    IP_ADDRESS_1 = "10.**.**.**"
    IP_ADDRESS_2 = "10.**.**.@@"
    GATEWAY = "10.**.**.1"

    @pytest.fixture
    def module_object(self):
        return PowerStoreFileInterface

    def test_get_file_interface_response(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'file_interface_id': MockFileInterfaceApi.FILE_INTERFACE_DETAILS['id'],
                'state': "present"}
        )
        FileInterfaceHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.file_interface.get_file_interface_details.assert_called()

    def test_get_file_interface_nas_ip_response(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nas_server': "nas_server_id",
                'ip_address': self.IP_ADDRESS_2,
                'state': "present"
            })
        FileInterfaceHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.file_interface.get_file_interface_by_nas_server_id.assert_called()

    def test_get_file_interface_exception(self, powerstore_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'file_interface_id': MockFileInterfaceApi.FILE_INTERFACE_DETAILS['id'],
                'state': "present"
            })
        powerstore_module_mock.file_interface.get_file_interface_details = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockFileInterfaceApi.get_file_interface_exception_response(
                'get_file_interface_exception'), powerstore_module_mock, FileInterfaceHandler)

    def test_create_file_interface_response(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nas_server': "sample_nas_server",
                'ip_address': self.IP_ADDRESS_1,
                'prefix_length': 21,
                'vlan_id': 0,
                'gateway': self.GATEWAY,
                'role': "Production",
                'state': "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.file_interface.get_file_interface_details_by_nas_server_id = MagicMock(
            return_value=None)
        FileInterfaceHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.file_interface.create_file_interface.assert_called()

    def test_create_file_interface_exception(self, powerstore_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nas_server': "sample_nas_server",
                'ip_address': self.IP_ADDRESS_1,
                'prefix_length': 21,
                'vlan_id': 0,
                'gateway': self.GATEWAY,
                'role': "Production",
                'state': "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.configuration.get_file_interface_details_by_nas_server_id = MagicMock(
            return_value=None)
        powerstore_module_mock.file_interface.create_file_interface = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockFileInterfaceApi.get_file_interface_exception_response(
                'create_file_interface_exception'), powerstore_module_mock, FileInterfaceHandler)

    def test_modify_file_interface(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'file_interface_id': MockFileInterfaceApi.FILE_INTERFACE_DETAILS['id'],
                'ip_address': self.IP_ADDRESS_2,
                'state': "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.file_interface.get_file_interface_details = MagicMock(
            return_value=MockFileInterfaceApi.FILE_INTERFACE_DETAILS)
        FileInterfaceHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.file_interface.modify_file_interface.assert_called()

    def test_modify_file_interface_exception(self, powerstore_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'file_interface_id': MockFileInterfaceApi.FILE_INTERFACE_DETAILS['id'],
                'ip_address': self.IP_ADDRESS_2,
                'state': "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.file_interface.get_file_interface_details = MagicMock(
            return_value=MockFileInterfaceApi.FILE_INTERFACE_DETAILS)
        powerstore_module_mock.file_interface.modify_file_interface = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockFileInterfaceApi.get_file_interface_exception_response(
                'modify_file_interface_exception'), powerstore_module_mock, FileInterfaceHandler)

    def test_delete_file_interface(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'file_interface_id': MockFileInterfaceApi.FILE_INTERFACE_DETAILS['id'],
                'state': "absent"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.file_interface.get_file_interface_details = MagicMock(
            return_value=MockFileInterfaceApi.FILE_INTERFACE_DETAILS)
        FileInterfaceHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.file_interface.delete_file_interface.assert_called()

    def test_delete_file_interface_exception(self, powerstore_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'file_interface_id': MockFileInterfaceApi.FILE_INTERFACE_DETAILS['id'],
                'state': "absent"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.file_interface.get_file_interface_details = MagicMock(
            return_value=MockFileInterfaceApi.FILE_INTERFACE_DETAILS)
        powerstore_module_mock.file_interface.delete_file_interface = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockFileInterfaceApi.get_file_interface_exception_response(
                'delete_file_interface_exception'), powerstore_module_mock, FileInterfaceHandler)
