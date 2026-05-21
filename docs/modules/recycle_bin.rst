.. _recycle_bin_module:


recycle_bin -- Manage Recycle Bin on PowerStore storage systems
==============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Manage Recycle Bin on PowerStore storage systems includes configuring the recycle bin expiration duration, recovering deleted volumes and volume groups from the recycle bin, permanently deleting items from the recycle bin, and emptying the entire recycle bin.

This module supports check mode and diff mode.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.5.0.0 or later.
- PyPowerStore 3.4.2 or later.



Parameters
----------

  recycle_bin_id (optional, str, None)
    The unique identifier of the recycle bin item.

    Required for recover and delete operations.

    Mutually exclusive with *resource_name*.


  resource_name (optional, str, None)
    The name of the deleted resource in the recycle bin.

    Used as an alternative to *recycle_bin_id* for identifying items.

    Mutually exclusive with *recycle_bin_id*.


  resource_type (optional, str, None)
    The type of resource to filter when using *resource_name*.

    Used to disambiguate when multiple items share the same name.


  expiration_duration (optional, int, None)
    Duration in days for items to remain in the recycle bin before automatic permanent deletion.

    Valid range is 0 to 30 days. A value of 0 means items expire immediately.

    Used only with *state=present* to configure the recycle bin retention policy.


  empty_recycle_bin (optional, bool, False)
    When set to :literal:`true` and *state=absent*, empties the entire recycle bin by permanently deleting all items.

    Cannot be used together with *recycle_bin_id* or *resource_name*.


  state (True, str, None)
    Define the operation to perform on the recycle bin.

    :literal:`present` with *expiration_duration* configures the retention policy.

    :literal:`present` with *recycle_bin_id* or *resource_name* recovers items from the recycle bin.

    :literal:`absent` with *recycle_bin_id* or *resource_name* permanently deletes items from the recycle bin.

    :literal:`absent` with *empty_recycle_bin=true* empties the entire recycle bin.


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
   - The :emphasis:`check\_mode` is supported.
   - The :emphasis:`diff` mode is supported.
   - Recycle Bin feature requires PowerStore version 3.5.0.0 or later.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get recycle bin configuration
      dellemc.powerstore.recycle_bin:
        array_ip: "{{ array_ip }}"
        user: "{{ user }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        state: "present"

    - name: Configure recycle bin expiration to 14 days
      dellemc.powerstore.recycle_bin:
        array_ip: "{{ array_ip }}"
        user: "{{ user }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        expiration_duration: 14
        state: "present"

    - name: Recover a volume from recycle bin by ID
      dellemc.powerstore.recycle_bin:
        array_ip: "{{ array_ip }}"
        user: "{{ user }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        recycle_bin_id: "e0684b39-0029-4be2-b5bf-67b8c145e1b8"
        state: "present"

    - name: Recover a volume from recycle bin by name
      dellemc.powerstore.recycle_bin:
        array_ip: "{{ array_ip }}"
        user: "{{ user }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        resource_name: "my_volume"
        resource_type: "volume"
        state: "present"

    - name: Permanently delete a specific item from recycle bin
      dellemc.powerstore.recycle_bin:
        array_ip: "{{ array_ip }}"
        user: "{{ user }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        recycle_bin_id: "e0684b39-0029-4be2-b5bf-67b8c145e1b8"
        state: "absent"

    - name: Empty the entire recycle bin
      dellemc.powerstore.recycle_bin:
        array_ip: "{{ array_ip }}"
        user: "{{ user }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        empty_recycle_bin: true
        state: "absent"



Return Values
-------------

changed (always, bool, true)
  Whether or not the resource has changed.


recycle_bin_config (When expiration_duration is provided or no item operation is performed, complex, {'id': '0', 'expiration_duration': 7})
  Details of the recycle bin configuration.


  id (, str, )
    Unique identifier for recycle bin configuration (always "0").


  expiration_duration (, int, )
    Duration in days for items to remain in the recycle bin.


recycle_bin_items (When getting recycle bin details without specific item operations, list, [{'id': 'e0684b39-0029-4be2-b5bf-67b8c145e1b8', 'name': 'test_volume', 'resource_type': 'volume', 'logical_provisioned': 1073741824, 'logical_used': 0, 'appliance_id': 'A1', 'deletion_timestamp': '2024-01-01T00:00:00.000+00:00', 'expiration_timestamp': '2024-01-08T00:00:00.000+00:00'}])
  List of items currently in the recycle bin.


  id (, str, )
    Unique identifier of the recycle bin item.


  name (, str, )
    Name of the deleted resource.


  resource_type (, str, )
    Type of resource (volume or volume_group).


  logical_provisioned (, int, )
    Provisioned size of the object in bytes.


  logical_used (, int, )
    Logical space used by the object in bytes.


  appliance_id (, str, )
    The appliance where the resource is located.


  deletion_timestamp (, str, )
    Time when the object was moved to the recycle bin.


  expiration_timestamp (, str, )
    Time when the object will be auto-purged.






Status
------





Authors
~~~~~~~

- Ansible Team <ansible.team@dell.com>
