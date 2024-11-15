.. _filesystem_snapshot_module:


filesystem_snapshot -- Manage Filesystem Snapshots for PowerStore
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Supports the provisioning operations on a filesystem snapshot such as create, modify, delete and get the details of a filesystem snapshot.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- PyPowerStore 3.3.0.



Parameters
----------

  snapshot_name (optional, str, None)
    The name of the filesystem snapshot.

    Mandatory for create operation.

    Specify either snapshot name or ID (but not both) for any operation.


  snapshot_id (optional, str, None)
    The ID of the Snapshot.


  filesystem (optional, str, None)
    The ID/Name of the filesystem for which snapshot will be taken.

    If filesystem name is specified, then *nas_server* is required to uniquely identify the filesystem.

    Mandatory for create operation.


  nas_server (optional, str, None)
    The NAS server, this could be the name or ID of the NAS server.


  description (optional, str, None)
    The description for the filesystem snapshot.


  desired_retention (optional, int, None)
    The retention value for the Snapshot.

    If the *desired_retention*/*expiration_timestamp* is not mentioned during creation, snapshot will be created with unlimited retention.

    Maximum supported desired retention is 31 days.


  retention_unit (optional, str, hours)
    The unit for retention.


  expiration_timestamp (optional, str, None)
    The expiration timestamp of the snapshot. This should be provided in UTC format, e.g 2020-07-24T10:54:54Z.

    To remove the expiration timestamp, specify it as an empty string.


  access_type (optional, str, None)
    Specifies whether the snapshot directory or protocol access is granted to the filesystem snapshot.
    Value of access_type must be one of: ``SNAPSHOT``, ``PROTOCOL``

    For create operation, if *access_type* is not specified, snapshot will be created with ``SNAPSHOT`` access type.


  state (True, str, None)
    Define whether the filesystem snapshot should exist or not.


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
   - The *check_mode* is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create filesystem snapshot
      dellemc.powerstore.filesystem_snapshot:
          array_ip: "{{array_ip}}"
          validate_certs: "{{validate_certs}}"
          user: "{{user}}"
          password: "{{password}}"
          snapshot_name: "sample_filesystem_snapshot"
          nas_server: "ansible_nas_server"
          filesystem: "sample_filesystem"
          desired_retention: 20
          retention_unit: "days"
          state: "present"

    - name: Get the details of filesystem snapshot
      dellemc.powerstore.filesystem_snapshot:
          array_ip: "{{array_ip}}"
          validate_certs: "{{validate_certs}}"
          user: "{{user}}"
          password: "{{password}}"
          snapshot_id: "{{fs_snapshot_id}}"
          state: "present"

    - name: Modify the filesystem snapshot
      dellemc.powerstore.filesystem_snapshot:
          array_ip: "{{array_ip}}"
          validate_certs: "{{validate_certs}}"
          user: "{{user}}"
          password: "{{password}}"
          snapshot_name: "sample_filesystem_snapshot"
          nas_server: "ansible_nas_server"
          description: "modify description"
          expiration_timestamp: ""
          state: "present"

    - name: Delete filesystem snapshot
      dellemc.powerstore.filesystem_snapshot:
          array_ip: "{{array_ip}}"
          validate_certs: "{{validate_certs}}"
          user: "{{user}}"
          password: "{{password}}"
          snapshot_id: "{{fs_snapshot_id}}"
          state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


create_fs_snap (always, bool, false)
  Whether or not the resource has created.


delete_fs_snap (always, bool, false)
  Whether or not the resource has deleted.


modify_fs_snap (always, bool, false)
  Whether or not the resource has modified.


filesystem_snap_details (When snapshot exists., dict, {'access_policy': None, 'access_policy_l10n': None, 'access_type': 'Snapshot', 'access_type_l10n': 'Snapshot', 'creation_timestamp': '2022-01-16T21:58:02+00:00', 'creator_type': 'User', 'creator_type_l10n': 'User', 'default_hard_limit': None, 'default_soft_limit': None, 'description': None, 'expiration_timestamp': '2022-01-17T00:58:00+00:00', 'filesystem_type': 'Snapshot', 'filesystem_type_l10n': 'Snapshot', 'folder_rename_policy': None, 'folder_rename_policy_l10n': None, 'grace_period': None, 'id': '61e49f3f-9b57-e69b-1038-aa02b52a030f', 'is_async_MTime_enabled': False, 'is_modified': False, 'is_quota_enabled': None, 'is_smb_no_notify_enabled': None, 'is_smb_notify_on_access_enabled': None, 'is_smb_notify_on_write_enabled': None, 'is_smb_op_locks_enabled': None, 'is_smb_sync_writes_enabled': None, 'last_refresh_timestamp': None, 'last_writable_timestamp': None, 'locking_policy': None, 'locking_policy_l10n': None, 'name': 'sample-filesystem-snapshot', 'nas_server': {'id': '6026056b-5405-0e36-7697-c285b9fa42b7', 'name': 'ansible_nas_server_2'}, 'parent_id': '61e4947b-8992-3db7-2859-aa02b52a0308', 'parent_name': 'sample-filesystem', 'protection_policy': None, 'size_total': '214748364800', 'size_used': '1621098496', 'smb_notify_on_change_dir_depth': 0})
  Details of the snapshot.


  access_type (, str, )
    Displays the type of access allowed to the snapshot.


  creation_timestamp (, str, )
    The date and time the snapshot was created.


  description (, str, )
    Description of the filesystem snapshot.


  expiration_timestamp (, str, )
    The date and time the snapshot is due to be automatically deleted by the system.


  id (, str, )
    Unique identifier of the filesystem snapshot instance.


  name (, str, )
    The name of the snapshot.


  nas_server (, dict, )
    Details of NAS server on which snapshot is present.


    id (, str, )
      ID of the NAS server.


    name (, str, )
      Name of the NAS server



  parent_id (, str, )
    ID of the filesystem on which snapshot is taken.


  parent_name (, str, )
    Name of the filesystem on which snapshot is taken.






Status
------





Authors
~~~~~~~

- Akash Shendge (@shenda1) <ansible.team@dell.com>

