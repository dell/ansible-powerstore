.. _smtp_config_module:


smtp_config -- SMTP configuration operations on a PowerStore storage system
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Performs all SMTP configuration operations on a PowerStore Storage System.

This module supports get details of an existing SMTP configuration. You can modify an existing SMTP configuration with supported parameters. You can also send a test mail through configured SMTP server.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.13 or later.
- PyPowerStore 3.1.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  smtp_id (optional, int, 0)
    Unique identifier of the SMTP configuration. This value is always '0'.


  smtp_address (optional, str, None)
    IP address of the SMTP server.


  smtp_port (optional, int, None)
    Port used for sending SMTP messages.


  source_email (optional, str, None)
    Source email address used for sending SMTP messages.


  destination_email (optional, str, None)
    Destination email address for the test.


  state (True, str, None)
    The state of the SMTP configuration after the task is performed.

    For Delete operation only, it should be set to ``absent``

    For all operations it should be set to ``present``.


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
   - Idempotency is not supported for test operation for smtp_config module.
   - Creation and deletion of SMTP configuration is not supported.
   - The *check_mode* is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get details of SMTP configuration
      dellemc.powerstore.smtp_config:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        smtp_id: "0"
        state: "present"

    - name: Modify SMTP config details
      dellemc.powerstore.smtp_config:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        smtp_id: "0"
        smtp_address: "sample.smtp.com"
        source_email: "def@dell.com"
        state: "present"

    - name: Send a test mail through the SMTP server
      dellemc.powerstore.smtp_config:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        smtp_id: "0"
        destination_email: "abc@dell.com"
        state: "present"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


smtp_config_details (When SMTP configuration exists., complex, {'address': 'sample.com', 'id': '0', 'port': 25, 'source_email': 'sample_source@dell.com'})
  Details of the SMTP configuration.


  id (, int, )
    Unique identifier of SMTP configuration.


  address (, str, )
    IP address of the SMTP server.


  port (, int, )
    Port used for sending SMTP messages.


  source_email (, str, )
    Source email address used for sending SMTP messages.






Status
------





Authors
~~~~~~~

- Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>

