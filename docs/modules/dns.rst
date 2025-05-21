.. _dns_module:


dns -- DNS operations on a PowerStore storage system
====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Performs all DNS operations on a PowerStore Storage System. This module supports get details of an existing DNS instance. You can modify existing DNS instance with supported parameters.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- PyPowerStore 3.4.1.



Parameters
----------

  dns_id (True, str, None)
    Unique identifier of the DNS instance.


  dns_addresses (optional, list, None)
    DNS server addresses in IPv4 format.


  dns_address_state (optional, str, None)
    State of the addresses mentioned in *dns_addresses*.


  state (True, str, None)
    The state of the DNS instance after the task is performed.

    For get and modify operations it should be set to ``present``.


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
   - Minimum 1 and maximum 3 addresses can be associated to a DNS instance.
   - Parameters *dns_addresses* and *dns_address_state* are required together.
   - Creation and deletion of DNS is not supported.
   - The *check_mode* is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get details of DNS instance
      dellemc.powerstore.dns:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        dns_id: "DNS1"
        state: "present"

    - name: Add addresses to DNS instance
      dellemc.powerstore.dns:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        dns_id: "DNS1"
        dns_addresses:
          - "XX.XX.XX.XX"
          - "YY.YY.YY.YY"
        dns_address_state: "present-in-dns"
        state: "present"

    - name: Remove addresses from DNS instance
      dellemc.powerstore.dns:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        dns_id: "DNS1"
        dns_addresses:
          - "YY.YY.YY.YY"
        dns_address_state: "absent-in-dns"
        state: "present"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


dns_details (When DNS exists., complex, {'addresses': ['1.2.3.4', '5.6.7.8'], 'id': 'DNS1'})
  Details of the DNS instance.


  id (, str, )
    Unique identifier of DNS instance.


  addresses (, str, )
    DNS server addresses in IPv4 format.






Status
------





Authors
~~~~~~~

- Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>

