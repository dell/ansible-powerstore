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

- A Dell PowerStore Storage System. Ansible 2.12, 2.13 or 2.14



Parameters
----------

  email_id (False, str, None)
    Unique identifier of the destination email address.

    Mutually exclusive with email_address.


  email_address (False, str, None)
    Email address to receive notifications.

    Mutually exclusive with email_id.


  new_address (False, str, None)
    New email address to receive notifications.


  send_test_email (False, bool, False)
    Whether to send the test email to the destination email address.


  notify (optional, dict, None)
    Whether to send different types of notifications. It contains below optional candidate variables.


    critical (False, bool, None)
      Whether to send notifications for critical alerts.


    major (False, bool, None)
      Whether to send notifications for major alerts.


    minor (False, bool, None)
      Whether to send notifications for minor alerts.


    info (False, bool, None)
      Whether to send notifications for informational alerts.



  state (True, str, None)
    The state of the destination email address after the task is performed.

    For Delete operation only, it should be set to "absent".

    For all Create, Modify, Test or Get details operations it should be set to "present".


  array_ip (True, str, None)
    IP or FQDN of the PowerStore management system.


  verifycert (True, bool, None)
    Boolean variable to specify whether to validate SSL certificate or not.

    True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.

    False - indicates that the SSL certificate should not be verified.


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
   - The check_mode is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
      - name: Get details of destination email with email_id
        dellemc.powerstore.email:
           array_ip: "{{array_ip}}"
           user: "{{user}}"
           password: "{{password}}"
           verifycert: "{{verifycert}}"
           email_id: "780b6220-2d0b-4b9f-a485-4ae7f673bd98"
           state: "present"

      - name: Get details of destination email with email_address
        dellemc.powerstore.email:
           array_ip: "{{array_ip}}"
           user: "{{user}}"
           password: "{{password}}"
           verifycert: "{{verifycert}}"
           email_address: "abc@dell.com"
           state: "present"

      - name: Create destination email
        dellemc.powerstore.email:
           array_ip: "{{array_ip}}"
           user: "{{user}}"
           password: "{{password}}"
           verifycert: "{{verifycert}}"
           email_address: "abc_xyz@dell.com"
           notify:
             info: True
             critical: True
             major: False
           state: "present"

      - name: Modify destination email
        dellemc.powerstore.email:
           array_ip: "{{array_ip}}"
           user: "{{user}}"
           password: "{{password}}"
           verifycert: "{{verifycert}}"
           email_address: "abc_xyz@dell.com"
           new_address: "def_pqr@dell.com"
           notify:
             info: False
             major: False
           state: "present"

      - name: Send a test mail to the destination email with email_id
        dellemc.powerstore.email:
           array_ip: "{{array_ip}}"
           user: "{{user}}"
           password: "{{password}}"
           verifycert: "{{verifycert}}"
           email_id: "780b6220-2d0b-4b9f-a485-4ae7f673bd98"
           send_test_email: True
           state: "present"

      - name: Delete destination email
        dellemc.powerstore.email:
           array_ip: "{{array_ip}}"
           user: "{{user}}"
           password: "{{password}}"
           verifycert: "{{verifycert}}"
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

