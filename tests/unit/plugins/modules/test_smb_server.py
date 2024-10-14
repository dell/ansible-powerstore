# Copyright: (c) 2024, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""Unit Tests for SMB server module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
# pylint: disable=unused-import

from ansible_collections.dellemc.powerstore.plugins.modules.smb_server import \
    PowerStoreSMBServer
from ansible_collections.dellemc.powerstore.plugins.modules.smb_server import \
    SMBServerHandler
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_smb_server_api \
    import MockSMBServerApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception import \
    MockApiException
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries.powerstore_unit_base \
    import PowerStoreUnitBase


class TestPowerStoreSMBServer(PowerStoreUnitBase):

    get_module_args = MockSMBServerApi.SMB_SERVER_COMMON_ARGS
    nas_id = "6581683c-61a3-76ab-f107-62b767ad9845"

    @pytest.fixture
    def module_object(self):
        return PowerStoreSMBServer

    def test_get_smb_server_response(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'smb_server_id': MockSMBServerApi.SMB_SERVER_DETAILS[0]['id'],
                'state': "present"}
        )
        SMBServerHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.smb_server.get_smb_server_details.assert_called()

    def test_get_smb_server_nas_response(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nas_server': self.nas_id,
                'state': "present"
            })
        powerstore_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockSMBServerApi.NAS_SERVER_DETAILS)
        powerstore_module_mock.smb_server.get_smb_server_by_nas_server_id = MagicMock(
            return_value=MockSMBServerApi.SMB_SERVER_DETAILS)
        SMBServerHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.smb_server.get_smb_server_by_nas_server_id.assert_called()

    def test_get_smb_server_exception(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'smb_server_id': MockSMBServerApi.SMB_SERVER_DETAILS[0]['id'],
                'state': "present"
            })
        powerstore_module_mock.smb_server.get_smb_server_details = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockSMBServerApi.get_smb_server_exception_response(
                'get_smb_server_exception'), powerstore_module_mock, SMBServerHandler)

    def test_create_smb_server_response(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nas_server': "sample_nas_server",
                'is_standalone': True,
                'netbios_name': "string",
                'workgroup': "string",
                'description': "string",
                'local_admin_password': "string",
                'state': "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.smb_server.get_smb_server_details_by_nas_server_id = MagicMock(
            return_value=None)
        SMBServerHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.smb_server.create_smb_server.assert_called()

    def test_create_smb_server_without_is_standalone_exception(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nas_server': "sample_nas_server",
                'netbios_name': "string",
                'workgroup': "string",
                'description': "string",
                'local_admin_password': "string",
                'state': "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.smb_server.get_smb_server_details_by_nas_server_id = MagicMock(
            return_value=None)
        self.capture_fail_json_call(
            MockSMBServerApi.get_smb_server_exception_response(
                'create_smb_server_wo_is_standalone_exception'), powerstore_module_mock, SMBServerHandler)

    def test_create_smb_server_exception(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nas_server': "sample_nas_server",
                'is_standalone': True,
                'netbios_name': "string",
                'workgroup': "string",
                'description': "string",
                'local_admin_password': "string",
                'state': "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.smb_server.get_smb_server_details_by_nas_server_id = MagicMock(
            return_value=None)
        powerstore_module_mock.smb_server.create_smb_server = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockSMBServerApi.get_smb_server_exception_response(
                'create_smb_server_exception'), powerstore_module_mock, SMBServerHandler)

    def test_modify_smb_server(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'smb_server_id': MockSMBServerApi.SMB_SERVER_DETAILS[0]['id'],
                'description': "New description",
                'workgroup': "workgroupnew",
                'state': "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.smb_server.get_smb_server_details = MagicMock(
            return_value=MockSMBServerApi.SMB_SERVER_DETAILS[0])
        SMBServerHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.smb_server.modify_smb_server.assert_called()

    def test_modify_smb_server_exception(self, powerstore_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'smb_server_id': MockSMBServerApi.SMB_SERVER_DETAILS[0]['id'],
                'description': "New description",
                'workgroup': "workgroupnew",
                'state': "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.smb_server.get_smb_server_details = MagicMock(
            return_value=MockSMBServerApi.SMB_SERVER_DETAILS[0])
        powerstore_module_mock.smb_server.modify_smb_server = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockSMBServerApi.get_smb_server_exception_response(
                'modify_smb_server_exception'), powerstore_module_mock, SMBServerHandler)

    def test_delete_smb_server(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'smb_server_id': MockSMBServerApi.SMB_SERVER_DETAILS[0]['id'],
                'state': "absent"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.smb_server.get_smb_server_details = MagicMock(
            return_value=MockSMBServerApi.SMB_SERVER_DETAILS[0])
        SMBServerHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.smb_server.delete_smb_server.assert_called()

    def test_delete_smb_server_exception(self, powerstore_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'smb_server_id': MockSMBServerApi.SMB_SERVER_DETAILS[0]['id'],
                'state': "absent"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.smb_server.get_smb_server_details = MagicMock(
            return_value=MockSMBServerApi.SMB_SERVER_DETAILS[0])
        powerstore_module_mock.smb_server.delete_smb_server = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockSMBServerApi.get_smb_server_exception_response(
                'delete_smb_server_exception'), powerstore_module_mock, SMBServerHandler)
