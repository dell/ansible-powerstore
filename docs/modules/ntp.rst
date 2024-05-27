.. _ntp_module:


ntp -- NTP operations on a PowerStore storage system
====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Performs all NTP operations on a PowerStore Storage System. This module supports get details of an existing NTP instance. You can modify existing NTP instance with supported parameters.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- PyPowerStore 3.3.0.



Parameters
----------

  ntp_id (True, str, None)
    Unique identifier of the NTP instance.


  ntp_addresses (optional, list, None)
    NTP server addresses, may contain host names or IPv4 addresses.


  ntp_address_state (optional, str, None)
    State of the addresses mentioned in *ntp_addresses*.


  state (True, str, None)
    The state of the NTP instance after the task is performed.

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
   - Minimum 1 and maximum 3 addresses can be associated to a NTP instance.
   - Parameters *ntp_addresses* and *ntp_address_state* are required together.
   - Creation and deletion of NTP is not supported.
   - The *check_mode* is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get details of NTP instance
      dellemc.powerstore.ntp:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        ntp_id: "NTP1"
        state: "present"

    - name: Add addresses to NTP instance
      dellemc.powerstore.ntp:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        ntp_id: "NTP1"
        ntp_addresses:
          - "XX.XX.XX.XX"
          - "YY.YY.YY.YY"
        ntp_address_state: "present-in-ntp"
        state: "present"

    - name: Remove addresses from NTP instance
      dellemc.powerstore.ntp:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        ntp_id: "NTP1"
        ntp_addresses:
          - "YY.YY.YY.YY"
        ntp_address_state: "absent-in-ntp"
        state: "present"



Return Values
-------------

changed (always, bool, false)
  Shows whether or not the resource has changed.


ntp_details (When NTP exists., complex, {'addresses': ['1.2.3.4', '5.6.7.8'], 'id': 'NTP1'})
  Details of the NTP instance.


  id (, str, )
    Unique identifier of NTP instance.


  addresses (, str, )
    NTP server addresses, may contain host names or IPv4 addresses.






Status
------





Authors
~~~~~~~

- Bhavneet Sharma (@sharmb5) <ansible.team@dell.com>

