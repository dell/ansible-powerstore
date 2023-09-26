# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for LDAP Domain module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.shared_library import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_ldap_domain_api import MockLDAPDomainApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.ldap_domain import PowerStoreLDAPDomain


class TestPowerStoreLDAPDomain():
    get_module_args = MockLDAPDomainApi.LDAPDOMAIN_COMMON_ARGS

    @pytest.fixture
    def ldap_domain_module_mock(self, mocker):
        mocker.patch(MockLDAPDomainApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        ldap_domain_module_mock = PowerStoreLDAPDomain()
        ldap_domain_module_mock.module.check_mode = False
        ldap_domain_module_mock.module = MagicMock()
        return ldap_domain_module_mock

    def test_get_ldap_domain_response(self, ldap_domain_module_mock):
        self.get_module_args.update({
            'ldap_domain_id': 9,
            'state': "present"
        })
        ldap_domain_module_mock.module.params = self.get_module_args
        ldap_domain_module_mock.perform_module_operation()
        ldap_domain_module_mock.configuration.get_ldap_domain_configuration_details.assert_called()

    def test_get_ldap_domain_response_name(self, ldap_domain_module_mock):
        self.get_module_args.update({
            'ldap_domain_name': "domain.com",
            'state': "present"
        })
        ldap_domain_module_mock.module.params = self.get_module_args
        ldap_domain_module_mock.perform_module_operation()
        ldap_domain_module_mock.configuration.get_ldap_domain_configuration_details_by_name.assert_called()

    def test_create_ldap_domain(self, ldap_domain_module_mock):
        self.get_module_args.update({
            'ldap_domain_name': "domain.com",
            'bind_user': 'cn=ldapadm,dc=domain,dc=com',
            'bind_password': 'password',
            'protocol': 'LDAP',
            'ldap_server_type': 'OpenLDAP',
            'ldap_servers': ['10.xxx.xx.xxx'],
            'ldap_server_state': "present-in-domain",
            'ldap_domain_user_settings': {
                'user_search_path': MockLDAPDomainApi.LDAP_DOMAIN_DETAILS['user_search_path']
            },
            'ldap_domain_group_settings': {
                'group_search_path': MockLDAPDomainApi.LDAP_DOMAIN_DETAILS['user_search_path']
            },
            'state': "present"
        })
        ldap_domain_module_mock.module.params = self.get_module_args
        ldap_domain_module_mock.configuration.get_ldap_domain_configuration_details_by_name = \
            MagicMock(return_value=[])
        ldap_domain_module_mock.configuration.create_ldap_domain_configuration = MagicMock(
            return_value=MockLDAPDomainApi.CREATE_RESPONSE)
        ldap_domain_module_mock.perform_module_operation()
        assert ldap_domain_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_verify_ldap_domain(self, ldap_domain_module_mock):
        self.get_module_args.update({
            'ldap_domain_id': 9,
            'verify_configuration': True,
            'state': "present"
        })
        ldap_domain_module_mock.module.params = self.get_module_args
        ldap_domain_module_mock.module.get_ldap_domain_details = MagicMock(
            return_value=MockLDAPDomainApi.LDAP_DOMAIN_DETAILS
        )
        ldap_domain_module_mock.perform_module_operation()
        assert ldap_domain_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_delete_ldap_domain(self, ldap_domain_module_mock):
        self.get_module_args.update({
            'ldap_domain_id': 9,
            'state': "absent"
        })
        ldap_domain_module_mock.module.params = self.get_module_args
        ldap_domain_module_mock.module.get_ldap_domain_details = MagicMock(
            return_value=MockLDAPDomainApi.LDAP_DOMAIN_DETAILS
        )
        ldap_domain_module_mock.perform_module_operation()
        assert ldap_domain_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_ldap_domain(self, ldap_domain_module_mock):
        self.get_module_args.update({
            'ldap_domain_id': 9,
            'ldap_domain_user_settings': {
                'user_id_attribute': None,
                'user_object_class': None,
                'user_search_path': MockLDAPDomainApi.LDAP_DOMAIN_DETAILS['user_search_path']
            },
            'ldap_domain_group_settings': {
                'group_member_attribute': None,
                'group_name_attribute': None,
                'group_object_class': 'posixAccount',
                'group_search_level': 2,
                'group_search_path': None
            },
            'state': "present"
        })

        ldap_domain_module_mock.module.params = self.get_module_args
        ldap_domain_module_mock.configuration.get_ldap_domain_configuration_details = MagicMock(
            return_value=MockLDAPDomainApi.LDAP_DOMAIN_DETAILS
        )
        ldap_domain_module_mock.perform_module_operation()
        assert ldap_domain_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_add_ldap_servers(self, ldap_domain_module_mock):
        self.get_module_args.update({
            'ldap_domain_id': 9,
            'ldap_servers': ['10.xxx.xx.yyy'],
            'ldap_server_state': 'present-in-domain',
            'state': 'present'
        })
        ldap_domain_module_mock.module.params = self.get_module_args
        ldap_domain_module_mock.configuration.get_ldap_domain_configuration_details = MagicMock(
            return_value=MockLDAPDomainApi.LDAP_DOMAIN_DETAILS
        )
        ldap_domain_module_mock.perform_module_operation()
        assert ldap_domain_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_remove_ldap_servers(self, ldap_domain_module_mock):
        self.get_module_args.update({
            'ldap_domain_id': 9,
            'ldap_servers': ['10.xxx.yy.yyy'],
            'ldap_server_state': 'absent-in-domain',
            'state': 'present'
        })
        ldap_domain_module_mock.module.params = self.get_module_args
        ldap_domain_module_mock.configuration.get_ldap_domain_configuration_details = MagicMock(
            return_value=MockLDAPDomainApi.LDAP_DOMAIN_DETAILS
        )
        ldap_domain_module_mock.perform_module_operation()
        assert ldap_domain_module_mock.module.exit_json.call_args[1]['changed'] is True
