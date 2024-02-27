.. _ldap_account_module:


ldap_account -- Manage LDAP Account for PowerStore
==================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing LDAP accounts on PowerStore Storage System includes creating an LDAP account, getting details of LDAP accounts, modifying an LDAP account, and deleting an LDAP account.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.14 or later.
- PyPowerStore 3.1.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  ldap_account_id (optional, int, None)
    Unique identifier of the LDAP account.


  ldap_account_name (optional, str, None)
    Name of the new LDAP account to be created.

    This has to match to the LDAP user or group in LDAP server to which the LDAP account is mapped.


  ldap_domain_id (optional, int, None)
    Unique identifier of the LDAP domain to which LDAP user or group belongs.


  ldap_domain_name (optional, str, None)
    Name of the LDAP domain to which LDAP user or group belongs.


  role_id (optional, int, None)
    Unique identifier of the role to which the new LDAP account will be mapped.


  role_name (optional, str, None)
    Name of the role to which the new LDAP account will be mapped.


  ldap_account_type (optional, str, None)
    Type of LDAP account.


  state (True, str, None)
    Define whether the LDAP account should exist or not.

    For Delete operation only, it should be set to ``absent``.

    For all other operations except delete, it should be set to ``present``.


  array_ip (True, str, None)
    IP or FQDN of the PowerStore management system.


  validate_certs (optional, bool, True)
    Boolean variable to specify whether to validate SSL certificate or not.

    ``true`` - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.

    ``false`` - indicates that the SSL certificate should not be verified.


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
   - The *check_mode* is supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create an LDAP account
      dellemc.powerstore.ldap_account:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        ldap_account_name: "ldap_user_account_1"
        ldap_domain_id: "1"
        role_name: "Administrator"
        ldap_account_type: "User"
        state: "present"

    - name: Get the details of the LDAP account by name
      dellemc.powerstore.ldap_account:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        ldap_account_name: "ldap_user_account_1"
        state: "present"

    - name: Get the details of the LDAP account by id
      dellemc.powerstore.ldap_account:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        ldap_account_id: "3"
        state: "present"

    - name: Modify an LDAP account
      dellemc.powerstore.ldap_account:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        ldap_account_name: "ldap_user_account_1"
        role_name: "2"
        state: "present"

    - name: Delete an LDAP account
      dellemc.powerstore.ldap_account:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        ldap_account_id: "3"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


ldap_account_details (When LDAP account exists., complex, {'id': '5', 'role_id': '1', 'domain_id': '2', 'name': 'sample_ldap_user', 'type': 'User', 'type_l10n': 'User', 'dn': 'cn=sample_ldap_user,dc=ldap,dc=com'})
  Details of the LDAP account.


  id (, int, )
    Unique identifier of the LDAP account.


  role_id (, int, )
    Unique identifier of the role to which the LDAP account is mapped.


  domain_id (, int, )
    Unique identifier of the LDAP domain to which LDAP user or group belongs.


  name (, str, )
    Name of the LDAP account.


  type (, str, )
    Type of LDAP account.


  dn (, str, )
    Types of directory service protocol.






Status
------





Authors
~~~~~~~

- Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>

