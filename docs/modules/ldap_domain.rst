.. _ldap_domain_module:


ldap_domain -- Manage LDAP domain for PowerStore
================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing LDAP domain on PowerStore Storage System includes creating LDAP domain, getting details of LDAP domain, modifying LDAP domain, verifying LDAP domain and deleting LDAP domain.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.14 or later.
- PyPowerStore 2.1.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  ldap_domain_name (optional, str, None)
    Name of the LDAP authority to construct the LDAP server configuration.

    Mandatory for the create operation.


  ldap_domain_id (optional, int, None)
    Unique identifier of the LDAP domain configuration.


  ldap_servers (optional, list, None)
    List of IP addresses of the LDAP servers for the domain.


  ldap_server_state (optional, str, None)
    State of the LDAP server.

    The \ :emphasis:`ldap\_servers`\  and \ :emphasis:`ldap\_server\_state`\  are required together.


  ldap_server_port (optional, int, None)
    Port number used to connect to the LDAP Server.


  protocol (optional, str, None)
    Types of directory service protocol.


  ldap_server_type (optional, str, None)
    Types of the LDAP server.


  bind_user (optional, str, None)
    Distinguished Name (DN) of the user to be used when binding; that is, authenticating and setting up the connection to the LDAP server.

    Mandatory for the create operation.


  bind_password (optional, str, None)
    Password to use when binding a new LDAP session.

    Mandatory for the create operation.


  ldap_timeout (optional, int, None)
    Timeout for establishing a connection to an LDAP server.


  is_global_catalog (optional, bool, None)
    Whether or not the catalog is global.


  ldap_domain_user_settings (optional, dict, None)
    User settings of LDAP domain.


    user_id_attribute (optional, str, None)
      Name of the LDAP attribute whose value indicates the unique identifier of the user.

      Default value is \ :literal:`sAMAccountName`\ .


    user_object_class (optional, str, None)
      LDAP object class for users.

      Default value is \ :literal:`user`\ .


    user_search_path (optional, str, None)
      Path used to search for users on the directory server.

      Search path is empty, if global catalog is enabled.



  ldap_domain_group_settings (optional, dict, None)
    Group settings of LDAP domain.


    group_name_attribute (optional, str, None)
      Name of the LDAP attribute whose value indicates the group name.

      Default value is \ :literal:`cn`\ .


    group_member_attribute (optional, str, None)
      Name of the LDAP attribute whose value contains the names of group members within a group.

      Default value is \ :literal:`member`\ .


    group_object_class (optional, str, None)
      LDAP object class for groups.

      Default value is \ :literal:`group`\ .


    group_search_path (optional, str, None)
      Path used to search for groups on the directory server.

      Search path is empty, if global catalog is enabled.


    group_search_level (optional, int, None)
      Nested search level for performing group search.

      Default value is 0.



  verify_configuration (optional, bool, False)
    Indicates whether to perform the verify LDAP domain configuration or not.


  state (True, str, None)
    Define whether the LDAP domain configuration should exist or not.

    For Delete operation only, it should be set to \ :literal:`absent`\ .

    For all other operations except delete, it should be set to \ :literal:`present`\ .


  array_ip (True, str, None)
    IP or FQDN of the PowerStore management system.


  validate_certs (optional, bool, True)
    Boolean variable to specify whether to validate SSL certificate or not.

    \ :literal:`true`\  - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS\_CA\_BUNDLE to the path of the SSL certificate.

    \ :literal:`false`\  - indicates that the SSL certificate should not be verified.


  user (True, str, None)
    The username of the PowerStore host.


  password (True, str, None)
    The password of the PowerStore host.


  timeout (optional, int, 120)
    Time after which the connection will get terminated.

    It is to be mentioned in seconds.


  port (optional, int, None)
    Port number for the PowerStore array.

    If not passed, it will take 443 as default.





Notes
-----

.. note::
   - The \ :emphasis:`is\_global\_catalog`\  option can be enabled only for AD server type.
   - To use LDAPS protocol, the pre-requisite is to upload the certificate of LDAP server on PowerStore array.
   - Verify operation does not support idempotency.
   - The \ :emphasis:`check\_mode`\  is supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create LDAP domain
      dellemc.powerstore.ldap_domain:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        domain_name: "{{domain_name}}"
        ldap_servers: ["10.xxx.xx.xx"]
        protocol: "LDAP"
        ldap_server_type: "OpenLDAP"
        bind_user: "{{bind_user}}"
        bind_password: "{{bind_password}}"
        ldap_domain_user_settings:
          user_search_path: "cn=Users"
        ldap_domain_group_settings:
          group_search_path: "cn=Users"
        ldap_server_state: "present-in-domain"
        state: "present"

    - name: Get LDAP domain details using ID
      dellemc.powerstore.ldap_domain:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        ldap_domain_id: 4
        state: "present"

    - name: Get LDAP domain details using name
      dellemc.powerstore.ldap_domain:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        ldap_domain_name: "{{ldap_domain_name}}"
        state: "present"

    - name: Verify LDAP domain configuration
      dellemc.powerstore.ldap_domain:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        ldap_domain_id: 4
        verify_configuration: true
        state: "present"

    - name: Delete LDAP domain configuration
      dellemc.powerstore.ldap_domain:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        ldap_domain_id: 4
        state: "absent"

    - name: Create LDAP domain with AD server type
      dellemc.powerstore.ldap_domain:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        ldap_domain_name: "{{domain_name}}"
        ldap_servers:
          - "10.xxx.xx.xx"
        ldap_server_state: "present-in-domain"
        ldap_server_type: "AD"
        bind_user: "{{bind_user}}"
        bind_password: "{{bind_password}}"
        is_global_catalog: true
        ldap_server_port: 3268
        protocol: "LDAP"
        ldap_domain_user_settings:
          user_search_path: ""
        ldap_domain_group_settings:
          group_search_path: ""
        state: "present"

    - name: Get LDAP domain details using domain name
      dellemc.powerstore.ldap_domain:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        ldap_domain_name: "{{domain_name}}"
        state: "present"

    - name: Delete LDAP domain using domain name
      dellemc.powerstore.ldap_domain:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        ldap_domain_name: "{{domain_name}}"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


ldap_domain_details (When LDAP domain configuration exists., complex, {'id': '9', 'domain_name': 'domain.com', 'port': 636, 'protocol': 'LDAPS', 'protocol_l10n': 'LDAPS', 'bind_user': 'cn=ldapadmin,dc=domain,dc=com', 'ldap_timeout': 300000, 'ldap_server_type': 'OpenLDAP', 'ldap_server_type_l10n': 'OpenLDAP', 'is_global_catalog': False, 'user_id_attribute': 'uid', 'user_object_class': 'inetOrgPerson', 'user_search_path': 'dc=domain,dc=com', 'group_name_attribute': 'cn', 'group_member_attribute': 'member', 'group_object_class': 'groupOfNames', 'group_search_path': 'dc=domain,dc=com', 'group_search_level': 0, 'ldap_servers': ['10.xxx.xx.xxx']})
  Details of the LDAP domain configuration.


  id (, str, )
    Unique identifier of the new LDAP server configuration.


  domain_name (, str, )
    Name of the LDAP authority to construct the LDAP server configuration.


  ldap_servers (, list, )
    List of IP addresses of the LDAP servers for the domain. IP addresses are in IPv4 format.


  port (, int, )
    Port number used to connect to the LDAP server(s).


  ldap_server_type (, str, )
    Types of LDAP server.


  protocol (, str, )
    Types of directory service protocol.


  bind_user (, str, )
    Distinguished Name (DN) of the user to be used when binding.


  ldap_timeout (, int, )
    Timeout for establishing a connection to an LDAP server. Default value is 30000 (30 seconds).


  is_global_catalog (, bool, )
    Whether or not the catalog is global. Default value is false.


  user_id_attribute (, str, )
    Name of the LDAP attribute whose value indicates the unique identifier of the user.


  user_object_class (, str, )
    LDAP object class for users.


  user_search_path (, str, )
    Path used to search for users on the directory server.


  group_name_attribute (, str, )
    Name of the LDAP attribute whose value indicates the group name.


  group_member_attribute (, str, )
    Name of the LDAP attribute whose value contains the names of group members within a group.


  group_object_class (, str, )
    LDAP object class for groups.


  group_search_path (, str, )
    Path used to search for groups on the directory server.


  group_search_level (, int, )
    Nested search level for performing group search.


  ldap_server_type_l10n (, str, )
    Localized message string corresponding to ldap\_server\_type.


  protocol_l10n (, str, )
    Localized message string corresponding to protocol.






Status
------





Authors
~~~~~~~

- Akash Shendge (@shenda1) <ansible.team@dell.com>

