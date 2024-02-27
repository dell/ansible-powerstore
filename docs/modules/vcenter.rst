.. _vcenter_module:


vcenter -- Manage vCenter on a PowerStore storage system
========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing vCenter on a PowerStore Storage System includes adding a vCenter, getting details, modifying, and removing a vCenter.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.14 or later.
- PyPowerStore 3.1.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  vcenter_id (optional, str, None)
    Unique identifier of the vCenter instance.


  address (optional, str, None)
    IP address of vCenter, in IPv4, IPv6, hostname format.

    Mandatory while adding a vCenter.

    To modify the address, a new address of the same vCenter must be passed.


  vcenter_username (optional, str, None)
    User name to login to vcenter.

    Mandatory while adding a vCenter.

    *vcenter_password* needs to be provided to modify the user name.


  vcenter_password (optional, str, None)
    Password to login to vcenter.

    Mandatory while adding a vCenter.


  vasa_provider_credentials (optional, dict, None)
    Credentials required for registering VASA vendor provider.


    username (True, str, None)
      Username of the local user account which will be used by vSphere to register VASA provider.

      Mandatory while registering VASA provider.


    password (True, str, None)
      Password of the local user account which will be used by vSphere to register VASA provider.

      Mandatory while registering VASA provider.



  delete_vasa_provider (optional, bool, None)
    Whether to remove VASA provider.

    When ``true``, remove the VASA provider from vCenter. This will only happen if provider is not connected to any other PowerStore system.

    ``false`` is the API default.


  state (optional, str, present)
    The state of the vCenter instance after the task is performed.

    For get, create, and modify operations it should be set to ``present``.


  update_password (optional, str, always)
    This parameter controls the way the *vcenter_password* is updated during addition and modification of the vCenter.

    ``always`` will update password for each execution.

    ``on_create`` will only set while adding a vCenter or modifying the *vcenter_username.*

    For modifying *vcenter_password*, set the *update_password* to ``always``.


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
   - In unified+ deployment, the one vCenter instance residing in the PowerStore cluster will be prepopulated and cannot be deleted, nor may any other vCenter be added.
   - For unified deployment, one external vCenter may be configured if desired.
   - The *check_mode* is supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get details of vCenter
      dellemc.powerstore.vcenter:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        vcenter_id: "24d333-59f-423c-205-c6181ea81b"

    - name: Add a vcenter
      dellemc.powerstore.vcenter:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        address: "XX.XX.XX.XX"
        vcenter_username: "user-name"
        vcenter_password: "password"
        update_password: "on_create"
        vasa_provider_credentials:
          username: "admin"
          password: "pass"

    - name: Modify a vCenter attribute
      dellemc.powerstore.vcenter:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        vcenter_id: "24d333-59f-423c-205-c6181ea81b"
        address: "XX.XX.XX.YY"
        vcenter_username: "user-name"
        vcenter_password: "password"
        update_password: "always"

    - name: Remove a vcenter
      dellemc.powerstore.vcenter:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        vcenter_id: "24d333-59f-423c-205-c6181ea81b"
        delete_vasa_provider: true
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Shows whether or not the resource has changed.


vcenter_details (When vCenter exists., complex, {'id': '0d330d6c-3fe6-41c6-8023-5bd3fa7c61cd', 'instance_uuid': 'c4c14fbb-828b-40f3-99bb-5bd4db723516', 'address': '10.x.x.x', 'username': 'administrator', 'version': '7.0.3', 'vendor_provider_status': 'Online', 'vendor_provider_status_l10n': 'Online', 'virtual_machines': [], 'datastores': [], 'vsphere_host': []})
  Details of the vCenter instance.


  id (, str, )
    Unique identifier of vCenter instance.


  instance_uuid (, str, )
    UUID instance of vCenter.


  address (, str, )
    IP address of vCenter hosts, in IPv4, IPv6 or hostname format.


  username (, str, )
    User name to login to vCenter.


  version (, str, )
    Version of vCenter including its build number. Was added in PowerStore version 3.0.0.0.


  vendor_provider_status (, list, )
    General status of the VASA vendor provider in vCenter.


  vendor_provider_status_l10n (, str, )
    Localized message string corresponding to vendor_provider_status.


  virtual_machines (, list, )
    Virtual machines associated with vCenter.


  datastores (, list, )
    Data stores that exist on a specific vCenter. Was added in PowerStore version 3.0.0.0.


  vsphere_host (, list, )
    All the vSphere hosts that exist on a specific vCenter. Was added in PowerStore version 3.0.0.0.






Status
------





Authors
~~~~~~~

- Bhavneet Sharma (@sharmb5) <ansible.team@dell.com>

