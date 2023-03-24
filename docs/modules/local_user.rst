.. _local_user_module:


local_user -- Local user operations for PowerStore Storage System
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Supports the provisioning operations on a Local user such as create, modify, delete and get the details of a local user.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore Storage System. Ansible 2.12, 2.13 or 2.14



Parameters
----------

  user_name (optional, str, None)
    Name of the local user account. Mutually exclusive with user_id.

    Mandatory only for create operation.


  user_id (optional, str, None)
    Unique identifier of the local user account.

    Mutually exclusive with user_name.


  user_password (optional, str, None)
    Password for the new local user account to be created.

    Mandatory only for create operation.


  new_password (optional, str, None)
    New password for the existing local user account.


  role_name (optional, str, None)
    The name of the role to which the local user account will be mapped.

    It is mutually exclusive with role_id.


  role_id (optional, int, None)
    The unique identifier of the role to which the local user account will be mapped.

    It is mutually exclusive with role_name.


  is_locked (optional, bool, None)
    Whether the user account is locked or not.

    Defaults to false at creation time.


  state (True, str, None)
    Define whether the local user should exist or not.


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
   - The check_mode is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create local user
      dellemc.powerstore.local_user:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        user_name: "ansible_user_1"
        user_password: "Password123#"
        role_name: "role_1"
        is_locked: False
        state: "present"

    - name: Get the details local user with user id
      dellemc.powerstore.local_user:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        user_id: "{{user_id}}"
        state: "present"

    - name: Get the details local user with user name
      dellemc.powerstore.local_user:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        user_name: "ansible_user_1"
        state: "present"

    - name: Modify attributes of local user
      dellemc.powerstore.local_user:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        user_name: "ansible_user_1"
        user_password: "Password123#"
        new_password: "Ansible123#"
        role_id: 4
        is_locked: True
        state: "present"

    - name: Delete local user
      dellemc.powerstore.local_user:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        user_name: "ansible_user_1"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


local_user_details (When local user exists, complex, {'id': '272', 'is_built_in': False, 'is_default_password': False, 'is_locked': False, 'name': 'sampleuser', 'role_id': '1', 'role_name': 'Administrator'})
  Details of the local user.


  id (, str, )
    The system generated ID given to the local user.


  name (, str, )
    Name of the local user.


  is_built_in (, bool, )
    Whether the user account is built-in or not.


  is_locked (, bool, )
    Whether the user account is locked or not. Defaults to false at creation time.


  is_default_password (, bool, )
    Whether the user account has a default password or not. Only applies to default user accounts


  role_id (, str, )
    Unique identifier of the role local user account is mapped to.


  role_name (, str, )
    Name of the role to which local user account is mapped.






Status
------





Authors
~~~~~~~

- Arindam Datta (@dattaarindam) <ansible.team@dell.com>

