# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of LDAP Account module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockLDAPAccountApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.ldap_account.PowerStoreLDAPAccount'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    LDAP_ACCOUNT_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'ldap_account_id': None,
        'ldap_account_name': None,
        'ldap_domain_id': None,
        'ldap_domain_name': None,
        'role_id': None,
        'role_name': None,
        'ldap_account_type': None,
        'state': None,

    }
    LDAP_ACCOUNT_NAME_1 = "ldap_sample_user_1"
    LDAP_ACCOUNT_DETAILS = {
        "id": "6",
        "role_id": "1",
        "domain_id": "2",
        "name": "ldap_sample_user_1",
        "type": "User",
        "type_l10n": "User",
        "dn": "cn=ldap_sample_user_1,dc=sampleldap,dc=com"
    }

    CREATE_LDAP_ACCOUNT = {
        "id": "6",
        "role_id": "1",
        "domain_id": "2",
        "name": "ldap_sample_user_1",
        "type": "User",
        "type_l10n": "User",
        "dn": "cn=ldap_sample_user_1,dc=sampleldap,dc=com"
    }

    ROLE_DETAILS = {
        "description": "Can view status and performance information",
        "id": "1",
        "is_built_in": True,
        "name": "Administrator"
    }

    ROLE_DETAILS_2 = {
        "description": "Can view status and performance information",
        "id": "5",
        "is_built_in": True,
        "name": "Operator"
    }

    LDAP_DOMAIN_DETAILS = [{
        "id": "2",
        "domain_name": "domain.com",
        "port": 636,
        "protocol": "LDAPS",
        "protocol_l10n": "LDAPS",
        "bind_user": "cn=ldapadmin,dc=domain,dc=com",
        "ldap_timeout": 300000,
        "ldap_server_type": "OpenLDAP",
        "ldap_server_type_l10n": "OpenLDAP",
        "is_global_catalog": False,
        "user_id_attribute": "uid",
        "user_object_class": "inetOrgPerson",
        "user_search_path": "dc=domain,dc=com",
        "group_name_attribute": "cn",
        "group_member_attribute": "member",
        "group_object_class": "groupOfNames",
        "group_search_path": "dc=domain,dc=com",
        "group_search_level": 0,
        "ldap_servers": [
            "10.xxx.xx.xxx"
        ]
    }]
