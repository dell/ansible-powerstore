# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for LDAP Account module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_ldap_account_api import MockLDAPAccountApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.ldap_account import PowerStoreLDAPAccount


class TestPowerStoreLDAPACcount():

    get_module_args = MockLDAPAccountApi.LDAP_ACCOUNT_COMMON_ARGS

    @pytest.fixture
    def ldap_account_module_mock(self, mocker):
        mocker.patch(MockLDAPAccountApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        ldap_account_module_mock = PowerStoreLDAPAccount()
        ldap_account_module_mock.module = MagicMock()
        ldap_account_module_mock.module.check_mode = False
        return ldap_account_module_mock

    def test_get_ldap_account_response(self, ldap_account_module_mock):
        self.get_module_args.update({
            'ldap_account_id': 6,
            'state': "present"
        })
        ldap_account_module_mock.module.params = self.get_module_args
        ldap_account_module_mock.perform_module_operation()
        ldap_account_module_mock.configuration.get_ldap_account_details.assert_called()

    def test_get_ldap_account_exception(self, ldap_account_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'ldap_account_id': 16,
            'state': "present"
        })
        ldap_account_module_mock.module.params = self.get_module_args
        ldap_account_module_mock.configuration.get_ldap_account_details = MagicMock(
            side_effect=MockApiException)
        ldap_account_module_mock.perform_module_operation()
        ldap_account_module_mock.configuration.get_ldap_account_details.assert_called()

    def test_get_ldap_account_response_with_name(self, ldap_account_module_mock):
        self.get_module_args.update({
            'ldap_account_name': MockLDAPAccountApi.LDAP_ACCOUNT_NAME_1,
            'state': "present"
        })
        ldap_account_module_mock.module.params = self.get_module_args
        ldap_account_module_mock.perform_module_operation()
        ldap_account_module_mock.configuration.get_ldap_account_details_by_name.assert_called()

    def test_create_ldap_account(self, ldap_account_module_mock):
        self.get_module_args.update({'ldap_account_name': MockLDAPAccountApi.LDAP_ACCOUNT_NAME_1,
                                     'ldap_account_type': "User",
                                     'ldap_domain_id': 2,
                                     'role_name': "Administrator",
                                     'state': "present"})
        ldap_account_module_mock.module.params = self.get_module_args
        ldap_account_module_mock.configuration.get_role_by_name = MagicMock(
            return_value=MockLDAPAccountApi.ROLE_DETAILS)
        ldap_account_module_mock.configuration.get_ldap_domain_configuration_details = MagicMock(
            return_value=MockLDAPAccountApi.LDAP_DOMAIN_DETAILS[0])
        ldap_account_module_mock.configuration.get_ldap_account_details_by_name = MagicMock(
            return_value=None)
        ldap_account_module_mock.perform_module_operation()
        ldap_account_module_mock.configuration.create_ldap_account.assert_called()
        assert ldap_account_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_ldap_account_invalid_role_exception(self, ldap_account_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({'ldap_account_name': MockLDAPAccountApi.LDAP_ACCOUNT_NAME_1,
                                     'ldap_account_type': "User",
                                     'ldap_domain_name': "domain.com",
                                     'role_name': "Admin",
                                     'state': "present"})
        ldap_account_module_mock.module.params = self.get_module_args
        ldap_account_module_mock.configuration.get_role_by_name = MagicMock(
            side_effect=MockApiException)
        ldap_account_module_mock.configuration.get_ldap_domain_configuration_details_by_name = MagicMock(
            return_value=MockLDAPAccountApi.LDAP_DOMAIN_DETAILS)
        ldap_account_module_mock.configuration.get_ldap_account_details_by_name = MagicMock(
            return_value=None)
        ldap_account_module_mock.perform_module_operation()
        ldap_account_module_mock.configuration.get_role_by_name.assert_called()

    def test_create_ldap_account_invalid_domain_exception(self, ldap_account_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({'ldap_account_name': MockLDAPAccountApi.LDAP_ACCOUNT_NAME_1,
                                     'ldap_account_type': "User",
                                     'ldap_domain_name': "sampledomain.com",
                                     'role_name': "Admin",
                                     'state': "present"})
        ldap_account_module_mock.module.params = self.get_module_args
        ldap_account_module_mock.configuration.get_role_by_name = MagicMock(
            return_value=MockLDAPAccountApi.ROLE_DETAILS)
        ldap_account_module_mock.configuration.get_ldap_domain_configuration_details_by_name = MagicMock(
            side_effect=MockApiException)
        ldap_account_module_mock.configuration.get_ldap_account_details_by_name = MagicMock(
            return_value=None)
        ldap_account_module_mock.perform_module_operation()
        ldap_account_module_mock.configuration.get_ldap_domain_configuration_details_by_name.assert_called()

    def test_modify_ldap_account(self, ldap_account_module_mock):
        self.get_module_args.update({'ldap_account_id': 6,
                                     'role_id': 5,
                                     'state': "present"})
        ldap_account_module_mock.module.params = self.get_module_args
        ldap_account_module_mock.configuration.get_role_details = MagicMock(
            return_value=MockLDAPAccountApi.ROLE_DETAILS_2)
        ldap_account_module_mock.configuration.get_ldap_account_details = MagicMock(
            return_value=MockLDAPAccountApi.LDAP_ACCOUNT_DETAILS)
        ldap_account_module_mock.perform_module_operation()
        assert ldap_account_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_ldap_account_exception(self, ldap_account_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({'ldap_account_id': 6,
                                     'role_id': 5,
                                     'state': "present"})
        ldap_account_module_mock.module.params = self.get_module_args
        ldap_account_module_mock.configuration.get_role_details = MagicMock(
            return_value=MockLDAPAccountApi.ROLE_DETAILS_2)
        ldap_account_module_mock.configuration.get_ldap_account_details = MagicMock(
            return_value=MockLDAPAccountApi.LDAP_ACCOUNT_DETAILS)
        ldap_account_module_mock.configuration.modify_ldap_account_details = MagicMock(
            side_effect=MockApiException)
        ldap_account_module_mock.perform_module_operation()
        ldap_account_module_mock.configuration.modify_ldap_account_details.assert_called()

    def test_delete_ldap_account(self, ldap_account_module_mock):
        self.get_module_args.update({
            'ldap_account_name': MockLDAPAccountApi.LDAP_ACCOUNT_NAME_1,
            'state': "absent"
        })
        ldap_account_module_mock.module.params = self.get_module_args
        ldap_account_module_mock.perform_module_operation()
        ldap_account_module_mock.configuration.delete_ldap_account.assert_called()

    def test_delete_ldap_account_exception(self, ldap_account_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'ldap_account_name': MockLDAPAccountApi.LDAP_ACCOUNT_NAME_1,
            'state': "absent"
        })
        ldap_account_module_mock.module.params = self.get_module_args
        ldap_account_module_mock.configuration.delete_ldap_account = MagicMock(
            side_effect=MockApiException)
        ldap_account_module_mock.perform_module_operation()
        ldap_account_module_mock.configuration.delete_ldap_account.assert_called()
