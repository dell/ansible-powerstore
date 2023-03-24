.. _volumegroup_module:


volumegroup -- Manage volume groups on a PowerStore Storage System
==================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing volume group on PowerStore Storage System includes creating new volume group, adding volumes to volume group, removing volumes from volume group, clone of a volume group, refresh of a volume group and restore of volume group.

Module also include renaming volume group, modifying volume group, and deleting volume group.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore Storage System. Ansible 2.12, 2.13 or 2.14



Parameters
----------

  vg_name (False, str, None)
    The name of the volume group.


  vg_id (False, str, None)
    The id of the volume group.

    It can be used only for Modify, Add/Remove, or Delete operation.


  volumes (optional, list, None)
    This is a list of volumes.

    Either the volume ID or name must be provided for adding/removing existing volumes from a volume group.

    If volumes are given, then vol_state should also be specified.


  vol_state (optional, str, None)
    String variable. Describes the state of volumes inside a volume group.

    If volume is given, then vol_state should also be specified.


  new_vg_name (optional, str, None)
    The new name of the volume group.


  description (optional, str, None)
    Description about the volume group.


  protection_policy (False, str, None)
    String variable. Represents Protection policy id or name used for volume group.

    Specifying an empty string or "" removes the existing protection policy from volume group.


  is_write_order_consistent (False, bool, None)
    A boolean flag to indicate whether Snapshot sets of the volume group will be write-order consistent.

    If this parameter is not specified, the array by default sets it to true.


  source_vg (optional, str, None)
    ID or name of the volume group to refresh from.


  source_snap (optional, str, None)
    ID or name of the snapshot to restore from.


  create_backup_snap (optional, bool, None)
    Specifies whether a backup snapshot set of the target volume group needs to be created before attempting refresh or restore.

    If not specified it will be set to True.


  backup_snap_profile (optional, dict, None)
    Snapshot volume group request.


    name (optional, str, None)
      Name of snapshot set to be created.


    description (optional, str, None)
      Description of the snapshot set.


    expiration_timestamp (optional, str, None)
      Time after which the snapshot set can be auto-purged.



  vg_clone (optional, dict, None)
    Parameters to support clone of a volume group.


    name (True, str, None)
      Name for the clone volume group.


    description (optional, str, None)
      Description for the clone volume group.


    protection_policy (optional, str, None)
      ID or name of the protection policy to assign to the clone volume.



  state (True, str, None)
    Define whether the volume group should exist or not.


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
   - Parameter vol_state is mandatory if volumes are provided.
   - A protection policy can be specified either for an volume group, or for the individual volumes inside the volume group.
   - A volume can be a member of at most one volume group.
   - Specifying "protection_policy" as empty string or "" removes the existing protection policy from a volume group.
   - The check_mode is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create volume group without protection policy
      dellemc.powerstore.volumegroup:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        vg_name: "{{vg_name}}"
        description: "This volume group is for ansible"
        state: "present"

    - name: Get details of volume group
      dellemc.powerstore.volumegroup:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        vg_name: "{{vg_name}}"
        state: "present"

    - name: Add volumes to volume group
      dellemc.powerstore.volumegroup:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        vg_name: "{{vg_name}}"
        state: "present"
        volumes:
          - "7f879569-676c-4749-a06f-c2c30e09b295"
          - "68e4dad5-5de5-4644-a98f-6d4fb916e169"
          - "Ansible_Testing"
        vol_state: "present-in-group"

    - name: Remove volumes from volume group
      dellemc.powerstore.volumegroup:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        vg_name: "{{vg_name}}"
        state: "present"
        volumes:
          - "7f879569-676c-4749-a06f-c2c30e09b295"
          - "Ansible_Testing"
        vol_state: "absent-in-group"

    - name: Rename volume group and change is_write_order_consistent flag
      dellemc.powerstore.volumegroup:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        vg_name: "{{vg_name}}"
        new_vg_name: "{{new_vg_name}}"
        is_write_order_consistent: False
        state: "present"

    - name: Get details of volume group by ID
      dellemc.powerstore.volumegroup:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        vg_id: "{{vg_id}}"
        state: "present"

    - name: Delete volume group
      dellemc.powerstore.volumegroup:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        name: "{{new_vg_name}}"
        state: "absent"

    - name: Refresh a volume group
      dellemc.powerstore.volumegroup:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        vg_name: "ansible_vg"
        source_vg: "vg_source"
        create_backup_snap: True
        backup_snap_profile:
            name: "test_snap"
        state: "present"

    - name: Restore a volume group
      dellemc.powerstore.volumegroup:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        vg_name: "ansible_vg"
        source_snap: "snap_source"
        create_backup_snap: True
        backup_snap_profile:
            name: "test_snap_restore"
        state: "present"

    - name: Clone a volume group
      dellemc.powerstore.volumegroup:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        vg_name: "ansible_vg"
        vg_clone:
            name: "ansible_vg_clone"
            protection_policy: "policy1"
        state: "present"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


add_vols_to_vg (When value exists, bool, false)
  A boolean flag to indicate whether volume/s got added to volume group.


create_vg (When value exists, bool, false)
  A boolean flag to indicate whether volume group got created.


delete_vg (When value exists, bool, false)
  A boolean flag to indicate whether volume group got deleted.


modify_vg (When value exists, bool, false)
  A boolean flag to indicate whether volume group got modified.


remove_vols_from_vg (When value exists, bool, false)
  A boolean flag to indicate whether volume/s got removed from volume group.


volume_group_details (When volume group exists, complex, {'creation_timestamp': '2022-01-06T05:41:59.381459+00:00', 'description': 'Volume group created', 'id': '634e4b95-e7bd-49e7-957b-6dc932642464', 'is_importing': False, 'is_protectable': True, 'is_replication_destination': False, 'is_write_order_consistent': False, 'location_history': None, 'mapped_volumes': [], 'migration_session_id': None, 'name': 'sample_volume_group', 'placement_rule': 'Same_Appliance', 'protection_data': {'copy_signature': None, 'created_by_rule_id': None, 'created_by_rule_name': None, 'creator_type': 'User', 'creator_type_l10n': 'User', 'expiration_timestamp': None, 'family_id': '634e4b95-e7bd-49e7-957b-6dc932642464', 'is_app_consistent': False, 'parent_id': None, 'source_id': None, 'source_timestamp': None}, 'protection_policy': {'id': '4bbb6333-59e4-489c-9015-c618d3e8384b', 'name': 'sample_protection_policy'}, 'protection_policy_id': '4bbb6333-59e4-489c-9015-c618d3e8384b', 'type': 'Primary', 'type_l10n': 'Primary', 'volumes': [], 'snapshots': [{'id': '2179802f-f975-434a-b317-9e55460e3e08', 'name': 'test_snapshot'}, {'id': '33d8990b-a468-4708-ba42-8b41af545939', 'name': 'backup.2022-08-04T10:57:41Z 001113180'}]})
  Details of the volume group.


  id (, str, )
    The system generated ID given to the volume group.


  name (, str, )
    Name of the volume group.


  description (, str, )
    description about the volume group.


  protection_policy_id (, str, )
    The protection policy of the volume group.


  is_write_order_consistent (, bool, )
    A boolean flag to indicate whether snapshot sets of the volume group will be write-order consistent.


  type (, str, )
    The type of the volume group.


  snapshots (, complex, )
    The snapshots associated with the volume group.


    id (, str, )
      ID of the snapshot.


    name (, str, )
      Name of the snapshot.



  volumes (, complex, )
    The volumes details of the volume group.


    id (, str, )
      The system generated ID given to the volume associated with the volume group.


    name (, str, )
      The name of the volume associated with the volume group.







Status
------





Authors
~~~~~~~

- Akash Shendge (@shenda1) <ansible.team@dell.com>
- Arindam Datta (@dattaarindam) <ansible.team@dell.com>

