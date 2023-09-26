# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for role module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.shared_library import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_role_api import MockRoleApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.role import PowerStoreRole


class TestPowerstoreRole():

    get_module_args = MockRoleApi.ROLE_COMMON_ARGS

    @pytest.fixture
    def role_module_mock(self, mocker):
        mocker.patch(MockRoleApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        role_module_mock = PowerStoreRole()
        role_module_mock.module = MagicMock()
        return role_module_mock

    def test_get_role_response(self, role_module_mock):
        self.get_module_args.update({
            'role_id': "1",
            'state': "present"
        })
        role_module_mock.module.params = self.get_module_args
        role_module_mock.configuration.get_role_details = MagicMock(
            return_value=MockRoleApi.ROLE_DETAILS)
        role_module_mock.perform_module_operation()
        assert self.get_module_args['role_id'] == role_module_mock.module.exit_json.call_args[1]['role_details']['id']
        role_module_mock.configuration.get_role_details.assert_called()

    def test_get_role_response_role_name(self, role_module_mock):
        self.get_module_args.update({
            'role_name': "Administrator",
            'state': "present"
        })
        role_module_mock.module.params = self.get_module_args
        role_module_mock.configuration.get_role_by_name = MagicMock(
            return_value=MockRoleApi.ROLE_DETAILS)
        role_module_mock.perform_module_operation()
        assert self.get_module_args['role_name'] == role_module_mock.module.exit_json.call_args[1]['role_details']['name']
        role_module_mock.configuration.get_role_by_name.assert_called()

    def test_delete_role(self, role_module_mock):
        role_id = "1"
        self.get_module_args.update({'role_id': role_id,
                                     'state': "absent"})
        role_module_mock.module.params = self.get_module_args
        role_module_mock.configuration.get_role_details = MagicMock(
            return_value=MockRoleApi.ROLE_DETAILS)
        role_module_mock.perform_module_operation()
        assert MockRoleApi.delete_role_failed_msg() in \
            role_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_non_existing_role_details(self, role_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        invalid_role_id = "7"
        self.get_module_args.update({
            'role_id': invalid_role_id,
            'state': "present"
        })
        role_module_mock.module.params = self.get_module_args
        role_module_mock.configuration.get_role_details = MagicMock(
            side_effect=MockApiException)
        role_module_mock.perform_module_operation()
        print(role_module_mock.module.fail_json.call_args[1]['msg'])
        assert MockRoleApi.get_role_failed_msg() in \
            role_module_mock.module.fail_json.call_args[1]['msg']
