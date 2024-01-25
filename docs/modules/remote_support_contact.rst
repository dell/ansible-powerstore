.. _remote_support_contact_module:


remote_support_contact -- Remote Support Contact operations on a PowerStore storage system
==========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Performs all Remote Support Contact operations on a PowerStore Storage system. This module supports get details and you can modify a Remote Support Contact with supported parameters.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.13 or later.
- PyPowerStore 3.0.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  contact_id (True, int, None)
    Unique identifier of the remote support contact.


  first_name (optional, str, None)
    The first name of the support contact for this system.


  last_name (optional, str, None)
    The last name of the support contact for this system.


  phone (optional, str, None)
    The phone number of this support contact for this system.


  email (optional, str, None)
    The email address of the support contact for this system.


  state (True, str, None)
    The state of the remote support contact after the task is performed.

    For Delete operation only, it should be set to ``absent``.

    For get/modify operation it should be set to ``present``.


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
   - Creation and deletion of remote support contact is not supported.
   - Parameters *first_name*, *last_name*, *email* and *phone* can be removed by passing empty string.
   - The *check_mode* is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get details of remote support contact
      dellemc.powerstore.remote_support_contact:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        contact_id: 0
        state: "present"

    - name: Modify remote support contact
      dellemc.powerstore.remote_support_contact:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        contact_id: 0
        first_name: "abc"
        last_name: "xyz"
        phone: "111-222-333-444"
        email: "abc_xyz@dell.com"
        state: "present"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


remote_support_contact_details (When remote support contact exists., complex, {'email': '', 'first_name': 'sample', 'id': '0', 'last_name': 'contact', 'phone': '0123213423'})
  Details of the remote support contact.


  id (, int, )
    Unique identifier of remote support contact.


  first_name (, str, )
    The first name of the support contact for this system.


  last_name (, str, )
    The last name of the support contact for this system.


  phone (, str, )
    The phone number of this support contact for this system.


  email (, str, )
    The email address of the support contact for this system.






Status
------





Authors
~~~~~~~

- Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>

