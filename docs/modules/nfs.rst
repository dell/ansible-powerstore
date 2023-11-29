.. _nfs_module:


nfs -- Manage NFS exports for PowerStore
========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing NFS exports on PowerStore Storage System includes creating new NFS Export, getting details of NFS export, modifying attributes of NFS export, and deleting NFS export.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.14 or later.
- PyPowerStore 2.1.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  nfs_export_name (optional, str, None)
    The name of the NFS export.

    Mandatory for create operation.

    Specify either \ :emphasis:`nfs\_export\_name`\  or \ :emphasis:`nfs\_export\_id`\  but not both for any operation.


  nfs_export_id (optional, str, None)
    The ID of the NFS export.


  filesystem (optional, str, None)
    The ID/Name of the filesystem for which the NFS export will be created.

    Either filesystem or snapshot is required for creation of the NFS Export.

    If filesystem name is specified, then \ :emphasis:`nas\_server`\  is required to uniquely identify the filesystem.

    If \ :emphasis:`filesystem`\  parameter is provided, then \ :emphasis:`snapshot`\  cannot be specified.


  snapshot (optional, str, None)
    The ID/Name of the Snapshot for which NFS export will be created.

    Either \ :emphasis:`filesystem`\  or \ :emphasis:`snapshot`\  is required for creation of the NFS Export.

    If snapshot name is specified, then \ :emphasis:`nas\_server`\  is required to uniquely identify the snapshot.

    If \ :emphasis:`snapshot`\  parameter is provided, then \ :emphasis:`filesystem`\  cannot be specified.

    NFS export can be created only if access type of snapshot is "protocol".


  nas_server (optional, str, None)
    The NAS server. This could be the name or ID of the NAS server.


  path (optional, str, None)
    Local path to export relative to the NAS server root.

    With NFS, each export of a file\_system or file\_snap must have a unique local path.

    Mandatory while creating NFS export.


  description (optional, str, None)
    The description for the NFS export.


  default_access (optional, str, None)
    Default access level for all hosts that can access the Export.

    For hosts that need different access than the default, they can be configured by adding to the list.

    If \ :emphasis:`default\_access`\  is not mentioned during creation, then NFS export will be created with \ :literal:`No\_Access`\ .


  no_access_hosts (optional, list, None)
    Hosts with no access to the NFS export.


  read_only_hosts (optional, list, None)
    Hosts with read-only access to the NFS export.


  read_only_root_hosts (optional, list, None)
    Hosts with read-only access for root user to the NFS export.


  read_write_hosts (optional, list, None)
    Hosts with read and write access to the NFS export.


  read_write_root_hosts (optional, list, None)
    Hosts with read and write access for root user to the NFS export.


  min_security (optional, str, None)
    NFS enforced security type for users accessing an NFS export.

    If not specified at the time of creation, it will be set to \ :literal:`SYS`\ .


  anonymous_uid (optional, int, None)
    Specifies the user ID of the anonymous account.

    If not specified at the time of creation, it will be set to -2.


  anonymous_gid (optional, int, None)
    Specifies the group ID of the anonymous account.

    If not specified at the time of creation, it will be set to -2.


  is_no_suid (optional, bool, None)
    If set, do not allow access to set SUID. Otherwise, allow access.

    If not specified at the time of creation, it will be set to \ :literal:`false`\ .


  host_state (optional, str, None)
    Define whether the hosts can access the NFS export.

    Required when adding or removing host access from the export.


  state (True, str, None)
    Define whether the NFS export should exist or not.


  array_ip (True, str, None)
    IP or FQDN of the PowerStore management system.


  validate_certs (optional, bool, True)
    Boolean variable to specify whether to validate SSL certificate or not.

    \ :literal:`true`\  - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS\_CA\_BUNDLE to the path of the SSL certificate.

    \ :literal:`false`\  - indicates that the SSL certificate should not be verified.


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
   - The \ :emphasis:`check\_mode`\  is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create NFS export (filesystem)
      dellemc.powerstore.nfs:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        nfs_export_name: "{{export_name1}}"
        filesystem: "{{filesystem}}"
        nas_server: "{{nas_server}}"
        path: "{{path1}}"
        description: "sample description"
        default_access: "NO_ACCESS"
        no_access_hosts:
          - "{{host5}}"
        read_only_hosts:
          - "{{host1}}"
        read_only_root_hosts:
          - "{{host2}}"
        read_write_hosts:
          - "{{host3}}"
        read_write_root_hosts:
          - "{{host4}}"
        min_security: "SYS"
        anonymous_uid: 1000
        anonymous_gid: 1000
        is_no_suid: true
        host_state: "present-in-export"
        state: "present"

    - name: Create NFS export Create NFS export for filesystem snapshot with mandatory parameters
      dellemc.powerstore.nfs:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        nfs_export_name: "{{export_name2}}"
        snapshot: "{{snapshot}}"
        nas_server: "{{nas_server}}"
        path: "{{path2}}"
        state: "present"

    - name: Get NFS export details using ID
      dellemc.powerstore.nfs:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        nfs_export_id: "{{export_id}}"
        state: "present"

    - name: Add Read-Only and Read-Write hosts to NFS export
      dellemc.powerstore.nfs:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        nfs_export_id: "{{export_id}}"
        read_only_hosts:
          - "{{host5}}"
        read_write_hosts:
          - "{{host6}}"
        host_state: "present-in-export"
        state: "present"

    - name: Remove Read-Only and Read-Write hosts from NFS export
      dellemc.powerstore.nfs:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        nfs_export_id: "{{export_id}}"
        read_only_hosts:
          - "{{host1}}"
        read_write_hosts:
          - "{{host3}}"
        host_state: "absent-in-export"
        state: "present"

    - name: Modify the attributes of NFS export
      dellemc.powerstore.nfs:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        nfs_export_id: "{{export_id}}"
        description: "modify description"
        default_access: "ROOT"
        state: "present"

    - name: Delete NFS export using name
      dellemc.powerstore.nfs:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        nfs_export_name: "{{export_name}}"
        nas_server: "{{nas_server}}"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


nfs_export_details (When NFS export exists., complex, {'anonymous_GID': -2, 'anonymous_UID': -2, 'default_access': 'No_Access', 'default_access_l10n': 'No_Access', 'description': None, 'export_path': '10.xx.xx.xx:/sample_nfs_export', 'file_system': {'filesystem_type': 'Primary', 'id': '61d68815-1ac2-fc68-7263-96e8abdcbab0', 'name': 'sample_file_system', 'nas_server': {'id': '60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9', 'name': 'ansible_nas_server_2'}}, 'id': '61d6888b-52ed-0d4b-2b35-96e8abdcbab0', 'is_no_SUID': False, 'min_security': 'Sys', 'min_security_l10n': 'Sys', 'name': 'sample_nfs_export', 'nfs_owner_username': 0, 'no_access_hosts': [], 'path': '/sample_file_system', 'read_only_hosts': [], 'read_only_root_hosts': [], 'read_write_hosts': [], 'read_write_root_hosts': []})
  The NFS export details.


  anonymous_GID (, int, )
    The group ID of the anonymous account.


  anonymous_UID (, int, )
    The user ID of the anonymous account.


  default_access (, str, )
    Default access level for all hosts that can access the export.


  description (, str, )
    The description for the NFS export.


  file_system (, complex, )
    Details of filesystem and NAS server on which NFS export is present.


    id (, str, )
      The ID of the filesystem.


    name (, str, )
      The name of the filesystem.


    filesystem_type (, str, )
      The type of the filesystem.


    nas_server (, complex, )
      Details of NAS server.


      id (, str, )
        The ID of the NAS server.


      name (, str, )
        The name of the NAS server.




  id (, str, )
    The ID of the NFS export.


  is_no_SUID (, bool, )
    If set, do not allow access to set SUID. Otherwise, allow access.


  min_security (, str, )
    NFS enforced security type for users accessing an NFS export.


  name (, str, )
    The name of the NFS export.


  no_access_hosts (, list, )
    Hosts with no access to the NFS export.


  path (, str, )
    Local path to a location within the file system.


  read_only_hosts (, list, )
    Hosts with read-only access to the NFS export.


  read_only_root_hosts (, list, )
    Hosts with read-only for root user access to the NFS export.


  read_write_hosts (, list, )
    Hosts with read and write access to the NFS export.


  read_write_root_hosts (, list, )
    Hosts with read and write for root user access to the NFS export.






Status
------





Authors
~~~~~~~

- Akash Shendge (@shenda1) <ansible.team@dell.com>

