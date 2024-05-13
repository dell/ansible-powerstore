.. _smbshare_module:


smbshare -- Manage SMB shares on a PowerStore storage system
============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing SMB Shares on PowerStore storage system includes create, get, modify, and delete the SMB shares.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.14 or later.
- PyPowerStore 3.1.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  share_name (optional, str, None)
    Name of the SMB share.

    Required during creation of the SMB share.

    For all other operations either *share_name* or *share_id* is required.


  share_id (optional, str, None)
    ID of the SMB share.

    Should not be specified during creation. ID is auto generated.

    For all other operations either *share_name* or *share_id* is required.

    If *share_id* is used then no need to pass *nas_server*/*filesystem*/*snapshot*/ *path*.


  path (optional, str, None)
    Local path to the file system/Snapshot or any existing sub-folder of the file system/Snapshot that is shared over the network.

    Path is relative to the base of the NAS server and must start with the name of the filesystem.

    Required for creation of the SMB share.


  filesystem (optional, str, None)
    The ID/Name of the File System.

    Either filesystem or snapshot is required for creation of the SMB share.

    If filesystem name is specified, then *nas_server* is required to uniquely identify the filesystem.

    If filesystem parameter is provided, then snapshot cannot be specified.


  snapshot (optional, str, None)
    The ID/Name of the Snapshot.

    Either filesystem or snapshot is required for creation of the SMB share.

    If snapshot name is specified, then *nas_server* is required to uniquely identify the snapshot.

    If snapshot parameter is provided, then filesystem cannot be specified.

    SMB share can be created only if access type of snapshot is "protocol".


  nas_server (optional, str, None)
    The ID/Name of the NAS Server.

    It is not required if *share_id* is used.


  description (optional, str, None)
    Description for the SMB share.

    Optional parameter when creating a share.

    To modify, pass the new value in description field.


  is_abe_enabled (optional, bool, None)
    Indicates whether Access-based Enumeration (ABE) for SMB share is enabled.

    During creation, if not mentioned, then the default is ``false``.


  is_branch_cache_enabled (optional, bool, None)
    Indicates whether Branch Cache optimization for SMB share is enabled.

    During creation, if not mentioned then default is ``false``.


  is_continuous_availability_enabled (optional, bool, None)
    Indicates whether continuous availability for SMB 3.0 is enabled.

    During creation, if not mentioned, then the default is ``false``.


  is_encryption_enabled (optional, bool, None)
    Indicates whether encryption for SMB 3.0 is enabled at the shared folder level.

    During creation, if not mentioned then default is ``false``.


  offline_availability (optional, str, None)
    Defines valid states of Offline Availability.

    ``MANUAL``- Only specified files will be available offline.

    ``DOCUMENTS``- All files that users open will be available offline.

    ``PROGRAMS``- Program will preferably run from the offline cache even when connected to the network. All files that users open will be available offline.

    ``NONE``- Prevents clients from storing documents and programs in offline cache.


  umask (optional, str, None)
    The default UNIX umask for new files created on the SMB Share.

    During creation, if not mentioned, then the default is 022.

    For all other operations, the default is None.


  state (True, str, None)
    Define whether the SMB share should exist or not.

    Value ``present`` indicates that the share should exist on the system.

    Value ``absent`` indicates that the share should not exist on the system.


  acl (optional, list, None)
    To specify the ACL access options.


    state (True, str, None)
      Define whether the ACL should exist or not.

      ``present`` indicates that the ACL should exist on the system.

      ``absent`` indicates that the ACL should not exist on the system.


    trustee_name (True, str, None)
      The name of the trustee.

      The *trustee_name* can be ``SID``, ``User``, ``Group`` or ``WellKnown``.

      If *trustee_type* is ``WellKnown``, then *trustee_name* should be `Everyone`.


    trustee_type (True, str, None)
      The type of the trustee.


    access_level (True, str, None)
      The access level.


    access_type (True, str, None)
      The access type.



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
   - When the ID of the filesystem/snapshot is passed then *nas_server* is not required. If passed, then the filesystem/snapshot should exist for the *nas_server*, else the task will fail.
   - Multiple SMB shares can be created for the same local path.
   - The *check_mode* is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    

    - name: Create SMB share for a filesystem
      dellemc.powerstore.smbshare:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        share_name: "sample_smb_share"
        filesystem: "sample_fs"
        nas_server: "{{nas_server_id}}"
        path: "{{path}}"
        description: "Sample SMB share created"
        is_abe_enabled: true
        is_branch_cache_enabled: true
        offline_availability: "DOCUMENTS"
        is_continuous_availability_enabled: true
        is_encryption_enabled: true
        state: "present"

    - name: Modify Attributes of SMB share for a filesystem
      dellemc.powerstore.smbshare:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        share_name: "sample_smb_share"
        nas_server: "sample_nas_server"
        description: "Sample SMB share attributes updated"
        is_abe_enabled: false
        is_branch_cache_enabled: false
        offline_availability: "MANUAL"
        is_continuous_availability_enabled: false
        is_encryption_enabled: false
        umask: "022"
        state: "present"

    - name: Create SMB share for a snapshot
      dellemc.powerstore.smbshare:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        share_name: "sample_snap_smb_share"
        snapshot: "sample_snapshot"
        nas_server: "{{nas_server_id}}"
        path: "{{path}}"
        description: "Sample SMB share created for snapshot"
        is_abe_enabled: true
        is_branch_cache_enabled: true
        is_continuous_availability_enabled: true
        state: "present"

    - name: Modify Attributes of SMB share for a snapshot
      dellemc.powerstore.smbshare:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        share_name: "sample_snap_smb_share"
        nas_server: "sample_nas_server"
        description: "Sample SMB share attributes updated for snapshot"
        is_abe_enabled: false
        is_branch_cache_enabled: false
        offline_availability: "MANUAL"
        is_continuous_availability_enabled: false
        umask: "022"
        state: "present"

    - name: Create SMB share for a filesystem with ACL
      dellemc.powerstore.smbshare:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        share_name: "sample_smb_share"
        filesystem: "sample_fs"
        nas_server: "{{nas_server_id}}"
        path: "{{path}}"
        description: "Sample SMB share created"
        is_abe_enabled: true
        is_branch_cache_enabled: true
        offline_availability: "DOCUMENTS"
        is_continuous_availability_enabled: true
        is_encryption_enabled: true
        acl:
          - access_level: "Full"
            access_type: "Allow"
            trustee_name: "TEST-56\\Guest"
            trustee_type: "User"
            state: "present"
          - access_level: "Read"
            access_type: "Deny"
            trustee_name: "S-1-5-21-8-5-1-32"
            trustee_type: "SID"
            state: "present"
        state: "present"

    - name: Modify Attributes of SMB share for a filesystem with ACL
      dellemc.powerstore.smbshare:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        share_name: "sample_smb_share"
        nas_server: "sample_nas_server"
        description: "Sample SMB share attributes updated"
        is_abe_enabled: false
        is_branch_cache_enabled: false
        offline_availability: "MANUAL"
        is_continuous_availability_enabled: false
        is_encryption_enabled: false
        umask: "022"
        acl:
          - access_level: "Full"
            access_type: "Allow"
            trustee_name: "TEST-56\\Guest"
            trustee_type: "User"
            state: "absent"
          - access_level: "Read"
            access_type: "Deny"
            trustee_name: "S-1-5-21-8-5-1-32"
            trustee_type: "SID"
            state: "absent"
        state: "present"

    - name: Get details of SMB share
      dellemc.powerstore.smbshare:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        share_id: "{{smb_share_id}}"
        state: "present"

    - name: Delete SMB share
      dellemc.powerstore.smbshare:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        share_id: "{{smb_share_id}}"
        state: "absent"



Return Values
-------------

changed (always, bool, True)
  Whether or not the resource has changed.


smb_share_details (When share exists., complex, {'description': 'SMB Share created', 'file_system': {'filesystem_type': 'Primary', 'id': '61d68c36-7c59-f5d9-65f0-96e8abdcbab0', 'name': 'sample_file_system', 'nas_server': {'id': '60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9', 'name': 'ansible_nas_server'}}, 'id': '61d68cf6-34d3-7b16-0370-96e8abdcbab0', 'is_ABE_enabled': True, 'is_branch_cache_enabled': True, 'is_continuous_availability_enabled': True, 'is_encryption_enabled': True, 'name': 'sample_smb_share', 'offline_availability': 'Documents', 'path': '/sample_file_system', 'umask': '177', 'aces': [{'access_level': 'Read', 'access_type': 'Deny', 'trustee_name': 'S-1-5-21-843271493-548684746-1849754324-32', 'trustee_type': 'SID'}, {'access_level': 'Read', 'access_type': 'Allow', 'trustee_name': 'TEST-56\\Guest', 'trustee_type': 'User'}, {'access_level': 'Read', 'access_type': 'Allow', 'trustee_name': 'S-1-5-21-843271493-548684746-1849754324-33', 'trustee_type': 'SID'}, {'access_level': 'Full', 'access_type': 'Allow', 'trustee_name': 'Everyone', 'trustee_type': 'WellKnown'}]})
  The SMB share details.


  id (, str, 5efc4432-cd57-5dd0-2018-42079d64ae37)
    The ID of the SMB share.


  name (, str, sample_smb_share)
    Name of the SMB share.


  file_system (, complex, )
    Includes ID and Name of filesystem and nas server for which smb share exists.


    filesystem_type (, str, Primary)
      Type of filesystem.


    id (, str, 5f73f516-e67b-b179-8901-72114981c1f3)
      ID of filesystem.


    name (, str, sample_filesystem)
      Name of filesystem.


    nas_server (, dict, )
      nas_server of filesystem.



  description (, str, This share is created for demo purpose only.)
    Additional information about the share.


  is_ABE_enabled (, bool, False)
    Whether Access Based enumeration is enforced or not


  is_branch_cache_enabled (, bool, False)
    Whether branch cache is enabled or not.


  is_continuous_availability_enabled (, bool, False)
    Whether the share will be available continuously or not.


  is_encryption_enabled (, bool, False)
    Whether encryption is enabled or not.


  aces (, list, )
    access control list (ACL) of the smb share.


    access_level (, str, )
      access level of the smb share.


    access_type (, str, )
      access type of the smb share.


    trustee_name (, str, )
      trustee name of the smb share.


    trustee_type (, str, )
      trustee type of the smb share.







Status
------





Authors
~~~~~~~

- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

