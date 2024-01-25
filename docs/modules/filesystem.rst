.. _filesystem_module:


filesystem -- Filesystem operations for PowerStore Storage system
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Supports the provisioning operations on a filesystem such as create, modify, delete and get the details of a filesystem.

Supports clone, refresh and restore operations on a filesystem.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.13 or later.
- PyPowerStore 3.0.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  filesystem_name (optional, str, None)
    Name of the file system. Mutually exclusive with *filesystem_id*. Mandatory only for create operation.


  filesystem_id (optional, str, None)
    Unique id of the file system. Mutually exclusive with *filesystem_name*.


  description (optional, str, None)
    Description of the file system.


  nas_server (optional, str, None)
    Name or ID of the NAS Server on which the file system is created. Mandatory parameter whenever *filesystem_name* is provided, since filesystem names are unique only within a NAS server.


  size (optional, int, None)
    Size that the file system presents to the host or end user.

    Mandatory only for create operation.


  cap_unit (optional, str, None)
    Capacity unit for the size.

    It defaults to ``GB``, if not specified.


  access_policy (optional, str, None)
    File system security access policies.


  locking_policy (optional, str, None)
    File system locking policies.

    ``ADVISORY``- No lock checking for NFS and honor SMB lock range only for SMB.

    ``MANDATORY``- Honor SMB and NFS lock range.


  folder_rename_policy (optional, str, None)
    File system folder rename policies for the file system with multi-protocol access enabled.

    ``ALL_ALLOWED`` - All protocols are allowed to rename directories without any restrictions.

    ``SMB_FORBIDDEN`` - A directory rename from the SMB protocol will be denied if at least one file is opened in the directory or in one of its child directories.

    ``All_FORBIDDEN`` - Any directory rename request will be denied regardless of the protocol used, if at least one file is opened in the directory or in one of its child directories.


  smb_properties (optional, dict, None)
    Advance settings for SMB. It contains optional candidate variables listed below.


    is_smb_sync_writes_enabled (optional, bool, None)
      Indicates whether the synchronous writes option is enabled on the file system.


    is_smb_no_notify_enabled (optional, bool, None)
      Indicates whether notifications of changes to directory file structure are enabled.


    is_smb_op_locks_enabled (optional, bool, None)
      Indicates whether opportunistic file locking is enabled on the file system.


    is_smb_notify_on_access_enabled (optional, bool, None)
      Indicates whether file access notifications are enabled on the file system.


    is_smb_notify_on_write_enabled (optional, bool, None)
      Indicates whether file write notifications are enabled on the file system.


    smb_notify_on_change_dir_depth (optional, int, None)
      Determines the lowest directory level to which the enabled notifications apply. minimum value is ``1``.



  protection_policy (optional, str, None)
    Name or ID of the protection policy applied to the file system.

    Specifying "" (empty string) removes the existing protection policy from file system.


  quota_defaults (optional, dict, None)
    Contains the default attributes for a filesystem quota.It contains below optional candidate variables.


    grace_period (optional, int, None)
      Grace period of soft limit.


    grace_period_unit (optional, str, None)
      Unit of the grace period of soft limit.


    default_hard_limit (optional, int, None)
      Default hard limit of user quotas and tree quotas.


    default_soft_limit (optional, int, None)
      Default soft limit of user quotas and tree quotas.


    cap_unit (optional, str, None)
      Capacity unit for default hard & soft limit.



  flr_attributes (optional, dict, None)
    The attributes for file retention.

    Can only be provided when the *config_type* is ``GENERAL``.


    mode (optional, str, None)
      The FLR type of the file system.

      It can only be provided during creation of a filesystem.


    minimum_retention (optional, str, None)
      The shortest retention period for which files on an FLR-enabled file system can be locked and protected from deletion.


    default_retention (optional, str, None)
      The default retention period that is used in an FLR-enabled file system when a file is locked and a retention period is not specified.


    maximum_retention (optional, str, None)
      The longest retention period for which files on an FLR-enabled file system can be locked and protected from deletion.


    auto_lock (optional, bool, None)
      Indicates whether to automatically lock files in an FLR-enabled file system.


    auto_delete (optional, bool, None)
      Indicates whether locked files will be automatically deleted from an FLR-enabled file system once their retention periods have expired.

      This setting can only be applied to a mounted FLR enabled file systems.


    policy_interval (optional, int, None)
      Indicates how long to wait (in seconds) after files are modified before the files are automatically locked.

      This setting can only be applied to mounted FLR enabled file systems.



  config_type (optional, str, None)
    Indicates the file system type.

    Cannot be modified.


  is_async_mtime_enabled (optional, bool, None)
    Indicates whether asynchronous MTIME is enabled on the file system or protocol snaps that are mounted writeable.


  file_events_publishing_mode (optional, str, None)
    State of the event notification services for all file systems of the NAS server.

    It can only be set to ``NFS_ONLY`` when *config_typ* is set to ``VMWARE``.


  host_io_size (optional, str, None)
    Typical size of writes from the server or other computer using the VMware file system to the storage system.

    Can only be set when the *config_type* is ``VMWARE``.

    Cannot be modified.


  clone_filesystem (optional, dict, None)
    The attributes for filesystem clone.


    name (optional, str, None)
      Name of the clone.

      It can only be provided during creation of a filesystem clone.


    description (optional, str, None)
      Description of the clone.


    access_policy (optional, str, None)
      File system security access policies.

      ``Native`` - Native Security.

      ``UNIX`` - UNIX Security.

      ``Windows`` - Windows Security.


    locking_policy (optional, str, None)
      File system locking policies.

      ``Advisory``- No lock checking for NFS and honor SMB lock range only for SMB.

      ``Mandatory``- Honor SMB and NFS lock range.


    folder_rename_policy (optional, str, None)
      File system folder rename policies for the file system with multi-protocol access enabled.

      ``All_Allowed`` - All protocols are allowed to rename directories without any restrictions.

      ``SMB_Forbidden`` - A directory rename from the SMB protocol will be denied if at least one file is opened in the directory or in one of its child directories.

      ``All_Forbidden`` - Any directory rename request will be denied regardless of the protocol used, if at least one file is opened in the directory or in one of its child directories.


    is_smb_sync_writes_enabled (optional, bool, None)
      Indicates whether the synchronous writes option is enabled on the file system.


    is_smb_no_notify_enabled (optional, bool, None)
      Indicates whether notifications of changes to directory file structure are enabled.


    is_smb_op_locks_enabled (optional, bool, None)
      Indicates whether opportunistic file locking is enabled on the file system.


    is_smb_notify_on_access_enabled (optional, bool, None)
      Indicates whether file access notifications are enabled on the file system.


    is_smb_notify_on_write_enabled (optional, bool, None)
      Indicates whether file write notifications are enabled on the file system.


    smb_notify_on_change_dir_depth (optional, int, None)
      Determines the lowest directory level to which the enabled notifications apply. minimum value is ``1``.


    is_async_MTime_enabled (optional, bool, None)
      Indicates whether asynchronous MTIME is enabled on the file system.


    file_events_publishing_mode (optional, str, None)
      State of the event notification services for all file systems of the NAS server.

      ``None`` - File event notifications are disabled for this file system.

      ``SMB_Only`` - SMB notifications are enabled for this file system.

      ``NFS_Only`` - NFS notifications are enabled for this file system.

      ``All`` - SMB and NFS notifications are enabled for this file system.


    flr_attributes (optional, dict, None)
      The attributes for file retention.


      force_clone (optional, bool, None)
        Specifies whether an FLR-C file system should be cloned.

        ``true`` - means cloning an FLR-C file system is allowed.

        ``false`` - means cloning an FLR-C file system is not allowed. and any attempt to do so will return an error.




  snapshot_name (optional, str, None)
    The name of the filesystem snapshot.

    Specify either snapshot name or ID (but not both) for restore and refresh operations.


  snapshot_id (optional, str, None)
    The ID of the Snapshot.

    Specify either snapshot name or ID (but not both) for restore and refresh operations.


  refresh_filesystem (optional, bool, None)
    Specifies to refresh filesystem.

    Mandatory only for refresh filesystem.


  restore_filesystem (optional, bool, None)
    Specifies to restore filesystem.

    Mandatory only for restore filesystem.


  backup_snap_name (optional, str, None)
    Name of the backup snap to be created before the restore operation occurs.


  state (True, str, None)
    Define whether the filesystem should exist or not.


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
   - It is recommended to remove the protection policy before deleting the filesystem.
   - The *check_mode* is not supported.
   - The pattern for *minimum_retention*, *default_retention* and *maximum_retention* is (^\d+[DMY])|(^infinite$).
   - Filesystem snapshot can be created using filesystem_snapshot module.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create FileSystem by Name
      register: result_fs
      dellemc.powerstore.filesystem:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        filesystem_name: "{{filesystem_name}}"
        description: "{{description}}"
        nas_server: "{{nas_server_id}}"
        size: "5"
        cap_unit: "GB"
        access_policy: "UNIX"
        locking_policy: "MANDATORY"
        smb_properties:
          is_smb_no_notify_enabled: true
          is_smb_notify_on_access_enabled: true
        quota_defaults:
          grace_period: 1
          grace_period_unit: 'days'
          default_hard_limit: 3
          default_soft_limit: 2
        protection_policy: "{{protection_policy_id}}"
        config_type: "VMWARE"
        is_async_mtime_enabled: true
        file_events_publishing_mode: "NFS_ONLY"
        host_io_size: "VMWARE_16K"
        state: "present"

    - name: Modify File System by id
      dellemc.powerstore.filesystem:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        filesystem_id: "{{fs_id}}"
        folder_rename_policy: "ALL_ALLOWED"
        smb_properties:
          is_smb_op_locks_enabled: true
          smb_notify_on_change_dir_depth: 3
        quota_defaults:
          grace_period: 2
          grace_period_unit: 'weeks'
          default_hard_limit: 2
          default_soft_limit: 1
        is_async_mtime_enabled: true
        file_events_publishing_mode: "ALL"
        flr_attributes:
          mode: "Enterprise"
          minimum_retention: "5D"
          default_retention: "1M"
          maximum_retention: "1Y"
        state: "present"

    - name: Get File System details by id
      dellemc.powerstore.filesystem:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        filesystem_id: "{{result_fs.filesystem_details.id}}"
        state: "present"

    - name: Delete File System by id
      dellemc.powerstore.filesystem:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        filesystem_id: "{{result_fs.filesystem_details.id}}"
        state: "absent"

    - name: Clone File System
      dellemc.powerstore.filesystem:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        filesystem_name: 'Atest'
        nas_server: 'Test_Nas'
        clone_filesystem:
          name: "Test_ansible"
          description: "Test"
          access_policy: "UNIX"
          locking_policy: "Advisory"
          folder_rename_policy: "All_Allowed"
          is_smb_sync_writes_enabled: true
          is_smb_no_notify_enabled: true
          is_smb_op_locks_enabled: true
          is_smb_notify_on_access_enabled: true
          is_smb_notify_on_write_enabled: true
          smb_notify_on_change_dir_depth: 32
          is_async_MTime_enabled: false
          file_events_publishing_mode: "All"
          flr_attributes:
            force_clone: false
        state: "present"

    - name: Refresh File System
      dellemc.powerstore.filesystem:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        snapshot_name: "Refresh_test"
        nas_server: 'Sample_NAS'
        refresh_filesystem: true
        state: "present"

    - name: Restore File System
      dellemc.powerstore.filesystem:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        snapshot_id: "xxx-xxx-xxx"
        restore_filesystem: true
        backup_snap_name: "Restore_test"
        state: "present"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


is_filesystem_cloned (always, bool, false)
  Whether or not the clone of filesystem is created.


is_filesystem_refreshed (always, bool, false)
  Whether or not the filesystem is refreshed.


is_filesystem_restored (always, bool, false)
  Whether or not the filesystem is restored.


filesystem_details (When filesystem exists, complex, {'access_policy': 'Native', 'access_policy_l10n': 'Native', 'access_type': None, 'access_type_l10n': None, 'creation_timestamp': None, 'creator_type': None, 'creator_type_l10n': None, 'default_hard_limit': 0, 'default_soft_limit': 0, 'description': None, 'expiration_timestamp': None, 'filesystem_type': 'Primary', 'filesystem_type_l10n': 'Primary', 'folder_rename_policy': 'All_Forbidden', 'folder_rename_policy_l10n': 'All Renames Forbidden', 'grace_period': 604800, 'id': '61e49f3f-9b57-e69b-1038-aa02b52a030f', 'is_async_MTime_enabled': False, 'is_modified': False, 'is_quota_enabled': False, 'is_smb_no_notify_enabled': False, 'is_smb_notify_on_access_enabled': False, 'is_smb_notify_on_write_enabled': False, 'is_smb_op_locks_enabled': True, 'is_smb_sync_writes_enabled': True, 'last_refresh_timestamp': None, 'last_writable_timestamp': None, 'locking_policy': 'Advisory', 'locking_policy_l10n': 'Advisory', 'name': 'sample-filesystem', 'nas_server': {'id': '6026056b-5405-0e36-7697-c285b9fa42b7', 'name': 'ansible_nas_server_2'}, 'parent_id': None, 'protection_policy': None, 'size_total': '214748364800', 'size_used': '1621098496', 'smb_notify_on_change_dir_depth': 512, 'snapshots': {}, 'total_size_with_unit': '200.0 GB', 'used_size_with_unit': '1.51 GB'})
  Details of the filesystem.


  id (, str, )
    The system generated ID given to the filesystem.


  name (, str, )
    Name of the filesystem.


  description (, str, )
    The description about the filesystem.


  protection_policy (, dict, )
    Id and name of the protection policy associated with the filesystem.


  nas_server (, dict, )
    Id and name of the nas server to which the filesystem belongs.


  size_total (, int, )
    Total size of the filesystem in bytes.


  total_size_with_unit (, str, )
    Total size of the filesystem with appropriate unit.


  size_used (, int, )
    Used size of the filesystem in bytes.


  used_size_with_unit (, str, )
    Used size of the filesystem with appropriate unit.


  access_policy (, str, )
    Access policy about the filesystem.


  locking_policy (, str, )
    Locking policy about the filesystem.


  is_smb_no_notify_enabled (, bool, )
    Whether smb notify policy is enabled for a filesystem.


  is_smb_notify_on_access_enabled (, bool, )
    Whether smb on access notify policy is enabled.


  is_smb_op_locks_enabled (, bool, )
    Whether smb op lock is enabled.


  grace_period (, int, )
    Default grace period for a filesystem quota in second.


  default_hard_limit (, int, )
    Default hard limit period for a filesystem quota in byte.


  default_soft_limit (, int, )
    Default soft limit period for a filesystem quota in byte.


  snapshots (, list, )
    Id and name of the snapshots of a filesystem.


  is_async_MTime_enabled (, bool, )
    Indicates whether asynchronous MTIME is enabled on the file system.


  file_events_publishing_mode (, str, )
    State of the event notification services for all file systems of the NAS server.


  config_type (, str, )
    Indicates the file system type.


  host_io_size (, str, )
    Typical size of writes from the server or other computer using the VMware file system to the storage system.


  flr_attributes (, complex, )
    The file retention attributes.


    mode (, str, )
      The FLR type of the file system.


    minimum_retention (, str, )
      The shortest retention period for which files on an FLR-enabled file system can be locked and protected from deletion.


    default_retention (, str, )
      The default retention period that is used in an FLR-enabled file system when a file is locked and a retention period is not specified.


    maximum_retention (, str, )
      The longest retention period for which files on an FLR-enabled file system can be locked and protected from deletion.


    auto_lock (, bool, )
      Indicates whether to automatically lock files in an FLR-enabled file system.


    auto_delete (, bool, )
      Indicates whether locked files will be automatically deleted from an FLR-enabled file system once their retention periods have expired.


    policy_interval (, int, )
      Indicates how long to wait (in seconds) after files are modified before the files are automatically locked.


    has_protected_files (, bool, )
      Indicates whether FLR file system has protected files.


    clock_time (, str, )
      Per file system clock used to track the retention date.


    maximum_retention_date (, str, )
      Maximum date and time that has been set on any locked file in an FLR-enabled file system, which means that the file system itself will be protected until this date and time.



  access_type (, str, )
    Indicates whether the snapshot directory or protocol access is granted to the file system snapshot.


  creation_timestamp (, str, )
    Time, in seconds, when the snapshot was created.


  creator_type (, str, )
    Snapshot creator type.


  expiration_timestamp (, str, )
    Time, in seconds, when the snapshot will expire.


  filesystem_type (, str, )
    Indicates the type of a file system.


  folder_rename_policy (, str, )
    File system folder rename policies for the file system with multiprotocol access enabled.


  is_modified (, bool, )
    Indicates whether the snapshot may have changed since it was created.


  is_quota_enabled (, bool, )
    Indicates whether quota is enabled.


  is_smb_notify_on_write_enabled (, bool, )
    Indicates whether file writes notifications are enabled on the file system.


  is_smb_sync_writes_enabled (, bool, )
    Indicates whether the synchronous writes option is enabled on the file system.


  last_refresh_timestamp (, str, )
    Time, in seconds, when the snapshot was last refreshed.


  last_writable_timestamp (, str, )
    If not mounted, and was previously mounted, the time (in seconds) of last mount.


  parent_id (, str, )
    Unique identifier of the object of the parent of this file system.


  smb_notify_on_change_dir_depth (, int, )
    Lowest directory level to which the enabled notifications apply, if any.






Status
------





Authors
~~~~~~~

- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>
- Pavan Mudunuri(@Pavan-Mudunuri) <ansible.team@dell.com>

