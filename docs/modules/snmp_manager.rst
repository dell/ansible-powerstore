.. _snmp_manager_module:


snmp_manager -- Manage SNMP Managers for PowerStore
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing SNMP Managers on PowerStore Storage System includes creating SNMP Manager, modifying SNMP Manager and deleting SNMP Manager.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.6.0.0 or later.
- PyPowerStore.



Parameters
----------

  alert_severity (optional, str, Info)
    Possible severities.


  auth_privacy (optional, str, None)
    Supported SNMP privacy protocol.

    :literal:`Nil` - No encryption on the wire.

    :literal:`AES256` - means Encryption class for AES 256.

    :literal:`TDES` - Encryption class for Triple Data Encryption.


  auth_protocol (optional, str, None)
    Relevant only for SNMPv3. Supported SNMP authentication protocols.

    :literal:`Nil` - No authorization.

    :literal:`MD5` - The AuthMD5 class implements the MD5 authentication protocol.

    :literal:`SHA256` - The Secure Hash Authentication.


  ip_address (True, str, None)
    IP address or FQDN of the SNMP manager.

    IPv4 and IPv6 are supported.


  new_ip_address (optional, str, None)
    IP address or FQDN of the SNMP manager to update.

    IPv4 and IPv6 are supported.


  snmp_password (optional, str, None)
    Passphrase, used for both Authentication and Privacy protocols.

    :emphasis:`snmp\_password` is only applicable when :emphasis:`version` is :literal:`V3` and to set the security level to authentication only and authentication and privacy.


  snmp_port (optional, int, 162)
    Port number to use with the address of the SNMP manager.


  snmp_username (optional, str, None)
    User name for SNMP auth.

    :emphasis:`snmp\_username` is required when :emphasis:`version` is :literal:`V3`.


  trap_community (optional, str, None)
    Trap Community string describes the security level.

    :emphasis:`trap\_community` is required when :emphasis:`version` is :literal:`V2c`.


  update_password (optional, str, always)
    Update password applicable only to fir update case.


  version (optional, str, V3)
    Supported SNMP protocol versions.

    :literal:`V2c` - SNMP version 2c.

    :literal:`V3` - SNMP version 3.


  state (optional, str, present)
    Define whether the file DNS should be enabled or not.

    For Delete operation only, it should be set to :literal:`absent`.


  array_ip (True, str, None)
    IP or FQDN of the PowerStore management system.


  validate_certs (optional, bool, True)
    Boolean variable to specify whether to validate SSL certificate or not.

    :literal:`true` - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS\_CA\_BUNDLE to the path of the SSL certificate.

    :literal:`false` - indicates that the SSL certificate should not be verified.


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
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    

    - name: Create SNMP Manager with V2 SNMP protocol
      dellemc.powerstore.snmp_manager:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        network_name: 127.**.**.**
        snmp_port: 162
        version: "V2c"
        alert_severity: Critical
        trap_community: test
        state: present

    - name: Create SNMP Manager with V3 SNMP protocol
      dellemc.powerstore.snmp_manager:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        network_name: 127.**.**.**
        snmp_port: 1024
        version: "V3"
        alert_severity: Critical
        trap_community: test
        snmp_username: test
        auth_protocol: MD5
        auth_privacy: TDES
        auth_pass: Password123!
        state: present

    - name: Modify SNMP Manager
      dellemc.powerstore.snmp_manager:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        ip_address: 127.**.**.**
        new_ip_address: 192.**.**.**
        alert_severity: Info
        trap_community: test
        snmp_username: test
        auth_protocol: MD5
        auth_privacy: TDES
        auth_pass: Password123!
        state: present

    - name: Delete SNMP Manager
      dellemc.powerstore.snmp_manager:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        ip_address: 127.**.**.**
        state: absent



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


snmp_details (When SNMP exists., dict, {'alert_severity': 'Info', 'auth_protocol': 'MD5', 'id': '967ffb5d-5059-43a6-8377-1b83b99e6470', 'ip_address': '127.0.0.1', 'port': 162, 'privacy_protocol': 'AES256', 'trap_community': None, 'user_name': 'admin', 'version': 'V3'})
  Details of the SNMP manager.


  alert_severity (, str, )
    Possible severities.


  auth_protocol (, str, )
    Relevant only for SNMPv3. Supported SNMP authentication protocols.


  id (, str, )
    Unique identifier of the SNMP manager.


  ip_addresses (, str, )
    IPv4 address, IPv6 address, or FQDN of the SNMP manager.


  port (, int, )
    Port number to use with the address of the SNMP manager.


  privacy_protocol (, str, )
    Relevant only for SNMPv3. Supported SNMP privacy protocols.


  trap_community (, str, )
    Trap Community string. Usually describes the security level.


  user_name (, str, )
    User name relevant only for SNMPv3.


  version (, str, )
    Supported SNMP protocol versions.






Status
------





Authors
~~~~~~~

- Meenakshi Dembi (@dembim) <ansible.team@dell.com>

