.. _role_module:


role -- Get details of the roles present on the PowerStore storage system
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Manage role in PowerStore storage system includes getting the details of a role.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- PyPowerStore 3.3.0.



Parameters
----------

  role_name (optional, str, None)
    Name of the role.


  role_id (optional, str, None)
    Id of the role.


  state (True, str, None)
    Define whether the role should exist or not.

    Value ``present``, indicates that the role should exist on the system.

    Value ``absent``, indicates that the role should not exist on the system.


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
   - Only getting the details of the role is supported by the ansible module.
   - Creation, modification and deletion of roles is not supported by the ansible modules.
   - The *check_mode* is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    

    - name: Get the details of role by name
      dellemc.powerstore.role:
        array_ip: "{{array_ip}}"
        validate_certs: "{{verify_cert}}"
        user: "{{user}}"
        password: "{{password}}"
        role_name: "Administrator"
        state: "present"

    - name: Get the details of role by id
      dellemc.powerstore.role:
        array_ip: "{{array_ip}}"
        validate_certs: "{{verify_cert}}"
        user: "{{user}}"
        password: "{{password}}"
        role_id: "1"
        state: "present"



Return Values
-------------

changed (always, bool, True)
  Whether or not the resource has changed.


role_details (When role exists., complex, {'description': 'Can view status and performance information', 'id': '1', 'is_built_in': True, 'name': 'Administrator'})
  The role details.


  id (, str, )
    The ID of the role.


  name (, str, )
    The name of the role.


  is_built_in (, bool, )
    Indicates whether the role is built-in.


  description (, str, )
    Description of the role.






Status
------





Authors
~~~~~~~

- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

