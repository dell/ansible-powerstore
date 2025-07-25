.. _storage_container_module:


storage_container -- Manage storage container for PowerStore
============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing storage containers on PowerStore Storage System includes creating a storage container, getting details of a storage container, modifying a storage container and deleting a storage container.

This module also supports creating and deleting storage container destinations.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.6.0.0 or later.
- PyPowerStore 3.4.1.
- Ansible-core 2.17 or later.
- Python 3.11, 3.12 or 3.13.



Parameters
----------

  storage_container_id (optional, str, None)
    The unique identifier of the storage container.


  storage_container_name (optional, str, None)
    Name for the storage container.

    This should be unique across all storage containers in the cluster.


  quota (optional, int, None)
    The total number of bytes that can be provisioned/reserved against this storage container.

    A value of :literal:`0` means there is no limit.

    It is possible to set the quota to a value that overprovisions the amount of space available in the system.


  quota_unit (optional, str, GB)
    Unit of the quota.


  storage_protocol (optional, str, None)
    The type of storage container.

    :literal:`SCSI` is set when a storage container is dedicated to :literal:`SCSI` usage.

    :literal:`NVMe` is set when a storage container is dedicated to :literal:`NVMe` usage.


  high_water_mark (optional, int, None)
    This is the percentage of the quota that can be consumed before an alert is raised.

    This is used only for creating a storage container.


  new_name (optional, str, None)
    The new name of the storage container.


  force_delete (optional, bool, False)
    This option overrides the error and allows the deletion to continue in case there are any vVols associated with the storage container.

    Use with great caution.


  state (False, str, present)
    Define whether the storage container should exist or not.

    For Delete operation only, it should be set to :literal:`absent`.


  storage_container_destination_state (optional, str, present)
    Define whether the storage container destination should exist in the storage container.

    To delete storage container destination, it should be :literal:`absent`.


  storage_container_destination (optional, dict, None)
    It contains details of remote system and remote storage container.

    It is required while creating and deleting storage container destinations.


    remote_system (True, str, None)
      Name or ID of the remote system.


    remote_address (True, str, None)
      The IP address of the remote storage system.


    user (True, str, None)
      Username of the remote PowerStore storage system.


    password (True, str, None)
      Password of the remote PowerStore storage system.


    port (optional, int, 443)
      Port number of the remote PowerStore storage system.


    timeout (optional, int, 120)
      Time after which connection will be terminated.

      It is mentioned in seconds.


    validate_certs (optional, bool, True)
      Boolean variable to specify whether to validate SSL certificate or not.

      :literal:`true` - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS\_CA\_BUNDLE to the path of the SSL certificate.

      :literal:`false` - indicates that the SSL certificate should not be verified.


    remote_storage_container (True, str, None)
      Name or ID of the remote storage container on the remote storage system.



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
   - Either storage container name or ID required while deleting the storage container destination.
   - The details of the storage container destination are embedded in the response of the storage container.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    

    - name: Create a storage_container
      dellemc.powerstore.storage_container:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        storage_container_name: "Ansible_storage_container_1"
        quota: 0
        storage_protocol: "SCSI"
        high_water_mark: 60

    - name: Get the details of the storage container using id
      dellemc.powerstore.storage_container:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        storage_container_id: "storage_container_id"
        state: "present"

    - name: Get the details of the storage container by name
      dellemc.powerstore.storage_container:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        storage_container_name: "Ansible_storage_container_1"

    - name: Modify a storage container
      dellemc.powerstore.storage_container:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        storage_container_name: "Ansible_storage_container_1"
        quota: 20
        quota_unit: "GB"
        storage_protocol: "NVMe"
        state: "present"

    - name: Rename a storage container
      dellemc.powerstore.storage_container:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        storage_container_name: "Ansible_storage_container_1"
        new_name: "Ansible_storage_container_1_new"

    - name: Delete a storage container containing vVols
      dellemc.powerstore.storage_container:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        storage_container_name: "Ansible_storage_container_1"
        force_delete: true
        state: "absent"

    - name: Delete a storage container using id
      dellemc.powerstore.storage_container:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        storage_container_id: "storage_container_id_1"
        state: "absent"

    - name: Create a storage container destination
      dellemc.powerstore.storage_container:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        storage_container_name: "local_storage_container"
        storage_container_destination:
          remote_address: "x.x.x.x"
          user: "{{user}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          remote_system: "remote_system_name"
          remote_storage_container: "remote_storage_container_name"

    - name: Delete a storage container destination
      dellemc.powerstore.storage_container:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        storage_container_id: "storage_container_id"
        storage_container_destination_state: "absent"
        storage_container_destination:
          remote_address: "x.x.x.x"
          user: "{{user}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          remote_system: "remote_system_name"
          remote_storage_container: "remote_storage_container_name"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


storage_container_details (When storage container exists., complex, {'datastores': [], 'destinations': [], 'id': 'e0ccd953-5650-41d8-9bce-f36d876d6a2a', 'name': 'Ansible_storage_container_1', 'quota': 21474836480, 'replication_groups': [], 'storage_protocol': 'NVMe', 'storage_protocol_l10n': 'NVMe', 'virtual_volumes': []})
  Details of the storage container.


  id (, str, )
    The unique identifier of the storage container.


  name (, str, )
    The name for the storage container.


  storage_protocol (, str, )
    The type of storage container.


  quota (, int, )
    The total number of bytes that can be provisioned/reserved against this storage container.


  replication_groups (, list, )
    Properties of a Replication Group.


    id (, str, )
      Unique identifier of the Replication Group instance.


    name (, str, )
      Name of the Replication Group.



  virtual_volumes (, list, )
    The virtual volumes associated to the storage container.


    id (, str, )
      The unique identifier of the virtual volume.


    name (, str, )
      The name of the virtual volume.



  destinations (, list, )
    A storage container destination defines replication destination for a local storage container on a remote system.


    id (, str, )
      The unique id of the storage container destination.


    remote_system_id (, str, )
      The unique id of the remote system.


    remote_system_name (, str, )
      The name of the remote system.


    remote_storage_container_id (, str, )
      The unique id of the destination storage container on the remote system.



  datastores (, list, )
    List of associated datstores.


    id (, str, )
      Unique identifier of the datastore instance.


    name (, str, )
      User-assigned name of the datastore in vCenter.







Status
------





Authors
~~~~~~~

- Trisha Datta (@trisha-dell) <ansible.team@dell.com>
- Bhavneet Sharma (@Bhavneet-Sharma) <ansible.team@dell.com>

