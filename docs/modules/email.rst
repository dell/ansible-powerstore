.. _email_module:


email -- Destination Email operations on a PowerStore storage system
====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Performs all destination email operations on a PowerStore Storage System.

This module supports get details of an existing destination email address. Create/Add new destination email address for all supported parameters.

This Module supports modify destination email address with supported parameters.

This Module supports delete/remove a specific destination email address. Send a test mail to a specific destination email address.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.6.0.0 or later.
- PyPowerStore.



Parameters
----------

  email_id (optional, str, None)
    Unique identifier of the destination email address.

    Mutually exclusive with :emphasis:`email\_address`.


  email_address (optional, str, None)
    Email address to receive notifications.

    Mutually exclusive with :emphasis:`email\_id`.


  new_address (optional, str, None)
    New email address to receive notifications.


  send_test_email (optional, bool, False)
    Whether to send the test email to the destination email address.


  notify (optional, dict, None)
    Whether to send different types of notifications. It contains below optional candidate variables.


    critical (optional, bool, None)
      Whether to send notifications for critical alerts.


    major (optional, bool, None)
      Whether to send notifications for major alerts.


    minor (optional, bool, None)
      Whether to send notifications for minor alerts.


    info (optional, bool, None)
      Whether to send notifications for informational alerts.



  state (True, str, None)
    The state of the destination email address after the task is performed.

    For Delete operation only, it should be set to :literal:`absent`.

    For all Create, Modify, Test or Get details operations it should be set to :literal:`present`.


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
   - Idempotency is not supported for Test operation of Email module.
   - The :emphasis:`check\_mode` is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get details of destination email with email_id
      dellemc.powerstore.email:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        email_id: "780b6220-2d0b-4b9f-a485-4ae7f673bd98"
        state: "present"

    - name: Get details of destination email with email_address
      dellemc.powerstore.email:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        email_address: "abc@dell.com"
        state: "present"

    - name: Create destination email
      dellemc.powerstore.email:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        email_address: "abc_xyz@dell.com"
        notify:
          info: true
          critical: true
          major: false
        state: "present"

    - name: Modify destination email
      dellemc.powerstore.email:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        email_address: "abc_xyz@dell.com"
        new_address: "def_pqr@dell.com"
        notify:
          info: false
          major: false
        state: "present"

    - name: Send a test mail to the destination email with email_id
      dellemc.powerstore.email:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        email_id: "780b6220-2d0b-4b9f-a485-4ae7f673bd98"
        send_test_email: true
        state: "present"

    - name: Delete destination email
      dellemc.powerstore.email:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        email_address: "def_pqr@dell.com"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


email_details (When destination email address exists, complex, {'email_address': 'abc@dell.com', 'id': 'e49c9469-a055-4207-898e-0c4150737722', 'notify': {'critical': True, 'info': True, 'major': True, 'minor': True}})
  Details of the destination email address.


  id (, str, )
    The system generated ID of the destination email instance.


  email_address (, str, )
    Email address to receive notifications.


  notify (, complex, )
    Whether to send different types of notifications.


    critical (, bool, )
      Whether to send notifications for critical alerts.


    info (, bool, )
      Whether to send notifications for informational alerts.


    major (, bool, )
      Whether to send notifications for major alerts.


    minor (, bool, )
      Whether to send notifications for minor alerts.







Status
------





Authors
~~~~~~~

- Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>

