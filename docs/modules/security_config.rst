.. _security_config_module:


security_config -- Security configuration operations for PowerStore Storage System
==================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing security configuration on PowerStore storage system includes getting details and modifying security configuration parameters.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.14 or later.
- PyPowerStore 3.2.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  security_config_id (True, int, None)
    ID of the security configuration.

    Mandatory for all operations.


  protocol_mode (optional, str, None)
    Protocol mode of the security configuration.

    Mandatory only for modify operation.


  state (True, str, None)
    Define whether the security config should exist or not.


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
   - Creation and deletion of security configs is not supported by Ansible modules.
   - Modification of protocol mode is only supported for PowerStore v2.0.0.0 and above.
   - The *check_mode* is not supported.
   - Parameter TLSv1_1 is supported for protocol_mode for PowerStore v3.0.0.0 and above.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get security config
      dellemc.powerstore.security_config:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        security_config_id: 1
        state: "present"

    - name: Modify attribute of security config
      dellemc.powerstore.security_config:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        security_config_id: 1
        protocol_mode: "TLSv1_1"
        state: "present"



Return Values
-------------

changed (always, bool, true)
  Whether or not the resource has changed.


security_config_details (When security config exists, complex, {'id': '1', 'idle_timeout': 3600, 'protocol_mode': 'TLSv1_2', 'protocol_mode_l10n': 'TLSv1_2'})
  Details of the security configuration.


  id (, str, )
    The system generated ID given to the security configuration.


  idle_timeout (, int, )
    Idle time (in seconds) after which login sessions will expire and require re-authentication.


  protocol_mode (, str, )
    The protocol mode of the security configuration.






Status
------





Authors
~~~~~~~

- Bhavneet Sharma (@sharmb5) <ansible.team@dell.com>

