.. _service_config_module:


service_config -- Manage Service config on PowerStore storage systems
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Manage Service config on PowerStore storage systems includes retrieving, and updating Service config.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.13 or later.
- PyPowerStore 3.1.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  service_config (optional, list, None)
    Specifies the appliance details on which ssh will be enabled/disabled.


    appliance_name (optional, str, None)
      Specifies the name of the appliance.

      Mutually exclusive with appliance_id.


    appliance_id (optional, str, None)
      Specifies the appliance id.

      Mutually exclusive with appliance_name.


    is_ssh_enabled (True, bool, None)
      Whether ssh will be enabled/disabled on specified appliance.



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
   - The *check_mode* is supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get Service config
      dellemc.powerstore.service_config:
        array_ip: "{{ array_ip }}"
        user: "{{ user }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"

    - name: Update Service config
      dellemc.powerstore.service_config:
        array_ip: "{{ array_ip }}"
        user: "{{ user }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        service_config:
          - appliance_name: "{{ appliance_name }}"
            is_ssh_enabled: true
          - appliance_id: "A2"
            is_ssh_enabled: true



Return Values
-------------

changed (always, bool, true)
  A Boolean value indicating if task had to make changes.


service_configs_details (always, list, [{'id': 'A1', 'appliance_name': 'Appliance-1', 'appliance_id': 'A1', 'is_ssh_enabled': False}])
  The details of Service configurations.


  id (, str, )
    Unique identifier of the service configuration.


  appliance_name (, str, )
    Name of the appliance.


  appliance_id (, str, )
    Unique identifier of the appliance.


  is_ssh_enabled (, bool, )
    Whether the SSH will be enabled/disabled.






Status
------





Authors
~~~~~~~

- Bhavneet Sharma(@Bhavneet-Sharma) <ansible.team@dell.com>

