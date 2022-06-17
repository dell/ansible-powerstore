# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of LDAP domain module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockLDAPDomainApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.ldap_domain.PowerStoreLDAPDomain'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    LDAPDOMAIN_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'ldap_domain_id': None,
        'ldap_domain_name': None,
        'ldap_servers': None,
        'ldap_server_state': None,
        'ldap_server_port': None,
        'ldap_server_type': None,
        'protocol': None,
        'bind_user': None,
        'bind_password': None,
        'ldap_timeout': None,
        'is_global_catalog': None,
        'ldap_domain_user_settings': None,
        'ldap_domain_group_settings': None,
        'verify_configuration': None,
        'state': None
    }

    LDAP_DOMAIN_DETAILS = {
        "id": "9",
        "domain_name": "domain.com",
        "port": 636,
        "protocol": "LDAPS",
        "protocol_l10n": "LDAPS",
        "bind_user": "cn=ldapadm,dc=domain,dc=com",
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
            "10.xxx.xx.xxx",
            "10.xxx.yy.yyy"
        ]
    }

    CREATE_RESPONSE = {
        'id': 9
    }
