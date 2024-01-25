# Copyright: (c) 2024, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Local user module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_local_user_api import MockLocalUserApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.local_user import PowerStoreLocalUser


class TestPowerstoreLocalUser():

    get_module_args = MockLocalUserApi.LOCAL_USER_COMMON_ARGS

    @pytest.fixture
    def local_user_module_mock(self, mocker):
        mocker.patch(MockLocalUserApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        local_user_module_mock = PowerStoreLocalUser()
        local_user_module_mock.module = MagicMock()
        return local_user_module_mock

    def test_get_local_user_by_id(self, local_user_module_mock):
        self.get_module_args.update({
            'user_id': "272",
            'state': "present"
        })
        local_user_module_mock.module.params = self.get_module_args
        local_user_module_mock.configuration.get_local_user_details = MagicMock(
            return_value=MockLocalUserApi.LOCAL_USER_DETAILS)
        local_user_module_mock.perform_module_operation()
        assert self.get_module_args['user_id'] == local_user_module_mock.module.exit_json.call_args[1]['local_user_details']['id']

    def test_get_local_user_by_name(self, local_user_module_mock):
        self.get_module_args.update({
            'user_name': MockLocalUserApi.LOCAL_USER_1,
            'state': "present"
        })
        local_user_module_mock.module.params = self.get_module_args
        local_user_module_mock.configuration.get_local_user_by_name = MagicMock(
            return_value=MockLocalUserApi.LOCAL_USER_DETAILS)
        local_user_module_mock.perform_module_operation()
        assert self.get_module_args['user_name'] == local_user_module_mock.module.exit_json.call_args[1]['local_user_details']['name']

    def test_create_local_user(self, local_user_module_mock):
        self.get_module_args.update({
            'user_name': "Sample_user",
            'user_password': 'password',
            'role_name': 'Administrator',
            'is_locked': True,
            'state': 'present'
        })
        local_user_module_mock.module.params = self.get_module_args
        local_user_module_mock.configuration.get_local_user_by_name = MagicMock(
            return_value=None)
        local_user_module_mock.perform_module_operation()
        assert local_user_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_local_user_without_role(self, local_user_module_mock):
        self.get_module_args.update({
            'user_name': "Sample_user",
            'user_password': 'password',
            'is_locked': True,
            'state': 'present'
        })
        local_user_module_mock.module.params = self.get_module_args
        local_user_module_mock.configuration.get_local_user_by_name = MagicMock(
            return_value=None)
        local_user_module_mock.perform_module_operation()
        assert MockLocalUserApi.create_local_user_without_role_failed_msg() in \
               local_user_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_local_user_with_new_password(self, local_user_module_mock):
        self.get_module_args.update({
            'user_name': "Sample_user",
            'user_password': 'password',
            'role_name': 'Administrator',
            'new_password': 'xxx',
            'is_locked': True,
            'state': 'present'
        })
        local_user_module_mock.module.params = self.get_module_args
        local_user_module_mock.configuration.get_local_user_by_name = MagicMock(
            return_value=None)
        local_user_module_mock.perform_module_operation()
        assert MockLocalUserApi.create_local_user_with_new_password_failed_msg() in \
               local_user_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_local_user_role(self, local_user_module_mock):
        self.get_module_args.update({
            'user_id': "272",
            'role_id': '4',
            'is_locked': False,
            'state': 'present'
        })
        local_user_module_mock.module.params = self.get_module_args
        local_user_module_mock.configuration.get_local_user_details = MagicMock(
            return_value=MockLocalUserApi.MODIFY_LOCAL_USER)
        local_user_module_mock.perform_module_operation()
        assert self.get_module_args['role_id'] == local_user_module_mock.module.exit_json.call_args[1]['local_user_details']['role_id']
        assert local_user_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_local_user_without_user_password(self, local_user_module_mock):
        self.get_module_args.update({
            'user_name': "Sample_user",
            'new_password': 'xxx',
            'state': 'present'
        })
        local_user_module_mock.module.params = self.get_module_args
        local_user_module_mock.configuration.get_local_user_by_name = MagicMock(
            return_value=MockLocalUserApi.LOCAL_USER_DETAILS)
        local_user_module_mock.perform_module_operation()
        assert MockLocalUserApi.modify_new_pass_without_user_pass_failed_msg() in \
               local_user_module_mock.module.fail_json.call_args[1]['msg']

    def test_delete_local_user(self, local_user_module_mock):
        self.get_module_args.update({
            'user_name': MockLocalUserApi.LOCAL_USER_1,
            'state': "absent"
        })
        local_user_module_mock.module.params = self.get_module_args
        local_user_module_mock.configuration.get_local_user_by_name = MagicMock(
            return_value=MockLocalUserApi.LOCAL_USER_DETAILS)
        local_user_module_mock.perform_module_operation()
        local_user_module_mock.configuration.delete_local_user.assert_called()

    def test_get_local_user_with_exception(self, local_user_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'user_name': MockLocalUserApi.LOCAL_USER_1,
            'state': "present"
        })
        local_user_module_mock.module.params = self.get_module_args
        local_user_module_mock.configuration.get_local_user_by_name = MagicMock(
            return_value=None)
        local_user_module_mock.configuration.get_local_user_by_name = MagicMock(
            side_effect=MockApiException)
        local_user_module_mock.perform_module_operation()
        local_user_module_mock.configuration.get_local_user_by_name.assert_called()

    def test_create_local_user_with_exception(self, local_user_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'user_name': MockLocalUserApi.LOCAL_USER_1,
            'user_password': 'password',
            'role_name': 'Administrator',
            'is_locked': True,
            'state': "present"
        })
        local_user_module_mock.module.params = self.get_module_args
        local_user_module_mock.configuration.get_local_user_by_name = MagicMock(
            return_value=None)
        local_user_module_mock.configuration.create_local_user = MagicMock(
            side_effect=MockApiException)
        local_user_module_mock.perform_module_operation()
        local_user_module_mock.configuration.create_local_user.assert_called()

    def test_modify_local_user_with_exception(self, local_user_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'user_name': MockLocalUserApi.LOCAL_USER_1,
            'is_locked': True,
            'state': "present"
        })
        local_user_module_mock.module.params = self.get_module_args
        local_user_module_mock.configuration.get_local_user_by_name = MagicMock(
            return_value=MockLocalUserApi.LOCAL_USER_DETAILS)
        local_user_module_mock.configuration.modify_local_user = MagicMock(
            side_effect=MockApiException)
        local_user_module_mock.perform_module_operation()
        local_user_module_mock.configuration.modify_local_user.assert_called()

    def test_delete_local_user_with_exception(self, local_user_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'user_name': MockLocalUserApi.LOCAL_USER_1,
            'state': "absent"
        })
        local_user_module_mock.module.params = self.get_module_args
        local_user_module_mock.configuration.get_local_user_by_name = MagicMock(
            return_value=MockLocalUserApi.LOCAL_USER_DETAILS)
        local_user_module_mock.configuration.delete_local_user = MagicMock(
            side_effect=MockApiException)
        local_user_module_mock.perform_module_operation()
        local_user_module_mock.configuration.delete_local_user.assert_called()
