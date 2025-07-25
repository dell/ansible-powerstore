.. _snapshot_module:


snapshot -- Manage Snapshots for PowerStore
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing Snapshots on PowerStore storage system, Create a new Volume Group Snapshot, Get details of Volume Group Snapshot, Modify Volume Group Snapshot, Delete an existing Volume Group Snapshot.

Module also supports Create a new Volume Snapshot, Get details of Volume Snapshot, Modify Volume Snapshot, Delete an existing Volume Snapshot.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.6.0.0 or later.
- PyPowerStore 3.4.1.
- Ansible-core 2.17 or later.
- Python 3.11, 3.12 or 3.13.



Parameters
----------

  snapshot_name (optional, str, None)
    The name of the Snapshot. Either snapshot name or ID is required.


  snapshot_id (optional, str, None)
    The ID of the Snapshot. Either snapshot ID or Snapshot name is required.


  volume (optional, str, None)
    The volume. This could be the volume name or ID.


  volume_group (optional, str, None)
    The volume group. This could be the volume group name or ID.


  new_snapshot_name (optional, str, None)
    The new name of the Snapshot.


  desired_retention (optional, str, None)
    The retention value for the Snapshot.

    If the retention value is not specified, the Snapshot details would be returned.

    To create a Snapshot, either a retention or expiration timestamp must be given.

    If the Snapshot does not have any retention value - specify it as 'None'.


  retention_unit (optional, str, None)
    The unit for retention.

    If this unit is not specified, :literal:`hours` is taken as default :emphasis:`retention\_unit`.

    If :emphasis:`desired\_retention` is specified, :emphasis:`expiration\_timestamp` cannot be specified.


  expiration_timestamp (optional, str, None)
    The expiration timestamp of the Snapshot. This should be provided in UTC format, e.g 2019-07-24T10:54:54Z.


  description (optional, str, None)
    The description for the Snapshot.


  state (True, str, None)
    Defines whether the Snapshot should exist or not.


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
   - The :emphasis:`check\_mode` is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create a volume snapshot on PowerStore
      dellemc.powerstore.snapshot:
        array_ip: "{{mgmt_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        volume: "{{volume}}"
        description: "{{description}}"
        desired_retention: "{{desired_retention}}"
        retention_unit: "{{retention_unit_days}}"
        state: "{{state_present}}"

    - name: Get details of a volume snapshot
      dellemc.powerstore.snapshot:
        array_ip: "{{mgmt_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        volume: "{{volume}}"
        state: "{{state_present}}"

    - name: Rename volume snapshot
      dellemc.powerstore.snapshot:
        array_ip: "{{mgmt_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        new_snapshot_name: "{{new_snapshot_name}}"
        volume: "{{volume}}"
        state: "{{state_present}}"

    - name: Delete volume snapshot
      dellemc.powerstore.snapshot:
        array_ip: "{{mgmt_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{new_snapshot_name}}"
        volume: "{{volume}}"
        state: "{{state_absent}}"

    - name: Create a volume group snapshot on PowerStore
      dellemc.powerstore.snapshot:
        array_ip: "{{mgmt_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        volume_group: "{{volume_group}}"
        description: "{{description}}"
        expiration_timestamp: "{{expiration_timestamp}}"
        state: "{{state_present}}"

    - name: Get details of a volume group snapshot
      dellemc.powerstore.snapshot:
        array_ip: "{{mgmt_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        volume_group: "{{volume_group}}"
        state: "{{state_present}}"

    - name: Modify volume group snapshot expiration timestamp
      dellemc.powerstore.snapshot:
        array_ip: "{{mgmt_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        volume_group: "{{volume_group}}"
        description: "{{description}}"
        expiration_timestamp: "{{expiration_timestamp_new}}"
        state: "{{state_present}}"

    - name: Rename volume group snapshot
      dellemc.powerstore.snapshot:
        array_ip: "{{mgmt_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        new_snapshot_name: "{{new_snapshot_name}}"
        volume_group: "{{volume_group}}"
        state: "{{state_present}}"

    - name: Delete volume group snapshot
      dellemc.powerstore.snapshot:
        array_ip: "{{mgmt_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{new_snapshot_name}}"
        volume_group: "{{volume_group}}"
        state: "{{state_absent}}"



Return Values
-------------

changed (always, bool, true)
  Whether or not the resource has changed.


create_vg_snap (When value exists, bool, true)
  A boolean flag to indicate whether volume group snapshot got created.


create_vol_snap (When value exists, bool, true)
  A boolean flag to indicate whether volume snapshot got created.


delete_vg_snap (When value exists, bool, true)
  A boolean flag to indicate whether volume group snapshot got deleted.


delete_vol_snap (When value exists, bool, true)
  A boolean flag to indicate whether volume snapshot got deleted.


modify_vg_snap (When value exists, bool, true)
  A boolean flag to indicate whether volume group snapshot got modified.


modify_vol_snap (When value exists, bool, true)
  A boolean flag to indicate whether volume snapshot got modified.


snap_details (When snapshot exists, complex, {'appliance_id': 'A1', 'creation_timestamp': '2022-01-06T05:41:59.381459+00:00', 'description': 'Snapshot created', 'hlu_details': [], 'host': [], 'host_group': [], 'id': '634e4b95-e7bd-49e7-957b-6dc932642464', 'is_replication_destination': False, 'location_history': None, 'mapped_volumes': [], 'migration_session_id': None, 'name': 'sample_snapshot', 'nguid': None, 'node_affinity': 'System_Select_At_Attach', 'node_affinity_l10n': 'System Select At Attach', 'nsid': None, 'performance_policy': {'id': 'default_medium', 'name': 'Medium'}, 'performance_policy_id': 'default_medium', 'protection_data': {'copy_signature': 'b9978b85-4a73-4abb-a25a-634e36f3e3d1', 'created_by_rule_id': None, 'created_by_rule_name': None, 'creator_type': 'User', 'creator_type_l10n': 'User', 'expiration_timestamp': '2022-01-06T08:41:00+00:00', 'family_id': 'dc15650a-2af5-4398-8ae3-63fc7ae25f63', 'is_app_consistent': False, 'parent_id': 'dc15650a-2af5-4398-8ae3-63fc7ae25f63', 'source_id': 'dc15650a-2af5-4398-8ae3-63fc7ae25f63', 'source_timestamp': '2022-01-06T05:41:59.381459+00:00'}, 'protection_policy': None, 'protection_policy_id': None, 'size': 1073741824, 'state': 'Ready', 'state_l10n': 'Ready', 'type': 'Snapshot', 'type_l10n': 'Snapshot', 'volume_groups': [], 'wwn': None})
  Details of the snapshot.


  id (, str, )
    The system generated ID given to the snapshot.


  name (, str, )
    Name of the snapshot.


  size (, int, )
    Size of the snapshot.


  description (, str, )
    Description about the snapshot.


  creation_timestamp (, str, )
    The creation timestamp of the snapshot.


  performance_policy_id (, str, )
    The performance policy for the snapshot.


  protection_policy_id (, str, )
    The protection policy of the snapshot.


  state (, str, )
    The state of the snapshot.


  type (, str, )
    The type of the snapshot.


  protection_data (, complex, )
    The protection data of the snapshot.


    expiration_timestamp (, str, )
      The expiration timestamp of the snapshot.



  volumes (, complex, )
    The volumes details of the volume group snapshot.


    id (, str, )
      The system generated ID given to the volume associated with the volume group.







Status
------





Authors
~~~~~~~

- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>
- Prashant Rakheja (@prashant-dell) <ansible.team@dell.com>

