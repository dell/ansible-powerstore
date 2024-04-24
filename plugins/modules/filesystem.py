#!/usr/bin/python
# Copyright: (c) 2024, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

""" Ansible module for managing filesystems for PowerStore"""
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: filesystem
version_added: '1.1.0'
short_description: Filesystem operations for PowerStore Storage system
description:
- Supports the provisioning operations on a filesystem such as create, modify,
  delete and get the details of a filesystem.
- Supports clone, refresh and restore operations on a filesystem.
extends_documentation_fragment:
  - dellemc.powerstore.powerstore
author:
- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>
- Pavan Mudunuri(@Pavan-Mudunuri) <ansible.team@dell.com>
options:
 filesystem_name:
   description:
   - Name of the file system. Mutually exclusive with I(filesystem_id).
     Mandatory only for create operation.
   type: str
 filesystem_id:
   description:
   - Unique id of the file system. Mutually exclusive with I(filesystem_name).
   type: str
 description:
   description:
   - Description of the file system.
   type: str
 nas_server:
   description:
   - Name or ID of the NAS Server on which the file system is created.
     Mandatory parameter whenever I(filesystem_name) is provided,
     since filesystem names are unique only within a NAS server.
   type: str
 size:
   description:
   - Size that the file system presents to the host or end user.
   - Mandatory only for create operation.
   type: int
 cap_unit:
   description:
   - Capacity unit for the size.
   - It defaults to C(GB), if not specified.
   choices: ['GB', 'TB']
   type: str
 access_policy:
   description:
   - File system security access policies.
   choices: [NATIVE, UNIX, WINDOWS]
   type: str
 locking_policy:
   description:
   - File system locking policies.
   - C(ADVISORY)- No lock checking for NFS and honor SMB lock range only for SMB.
   - C(MANDATORY)- Honor SMB and NFS lock range.
   choices: [ADVISORY, MANDATORY]
   type: str
 folder_rename_policy:
   description:
   - File system folder rename policies for the file system with
     multi-protocol access enabled.
   - C(ALL_ALLOWED) - All protocols are allowed to rename directories without
     any restrictions.
   - C(SMB_FORBIDDEN) - A directory rename from the SMB protocol will be
     denied if at least one file is opened in the directory or in one of its
     child directories.
   - C(All_FORBIDDEN) - Any directory rename request will be denied regardless
     of the protocol used, if at least one file is opened in the directory
     or in one of its child directories.
   choices: ['ALL_ALLOWED', 'SMB_FORBIDDEN', 'ALL_FORBIDDEN']
   type: str
 smb_properties:
   description:
   - Advance settings for SMB. It contains optional candidate variables listed below.
   type: dict
   suboptions:
     is_smb_sync_writes_enabled:
       description:
       - Indicates whether the synchronous writes option is enabled on the
         file system.
       type: bool
     is_smb_no_notify_enabled:
       description:
       - Indicates whether notifications of changes to directory file
         structure are enabled.
       type: bool
     is_smb_op_locks_enabled:
       description:
       - Indicates whether opportunistic file locking is enabled on the file
         system.
       type: bool
     is_smb_notify_on_access_enabled:
       description:
       - Indicates whether file access notifications are enabled on the file
         system.
       type: bool
     is_smb_notify_on_write_enabled:
       description:
       - Indicates whether file write notifications are enabled on the file
         system.
       type: bool
     smb_notify_on_change_dir_depth:
       description:
       - Determines the lowest directory level to which the
         enabled notifications apply. minimum value is C(1).
       type: int
 protection_policy:
   description:
   - Name or ID of the protection policy applied to the file system.
   - Specifying "" (empty string) removes the existing
     protection policy from file system.
   type: str
 quota_defaults:
   description:
   - Contains the default attributes for a filesystem quota.It contains
     below optional candidate variables.
   type: dict
   suboptions:
     grace_period:
       description:
       - Grace period of soft limit.
       type: int
     grace_period_unit:
       description:
       - Unit of the grace period of soft limit.
       type: str
       choices: ['days', 'weeks', 'months']
     default_hard_limit:
       description:
       - Default hard limit of user quotas and tree quotas.
       type: int
     default_soft_limit:
       description:
       - Default soft limit of user quotas and tree quotas.
       type: int
     cap_unit:
       description:
       - Capacity unit for default hard & soft limit.
       type: str
       choices: ['GB', 'TB']
 flr_attributes:
   description:
   - The attributes for file retention.
   - Can only be provided when the I(config_type) is C(GENERAL).
   type: dict
   suboptions:
     mode:
       description:
       - The FLR type of the file system.
       - It can only be provided during creation of a filesystem.
       type: str
       choices: ['Enterprise', 'Compliance']
     minimum_retention:
       description:
       - The shortest retention period for which files
         on an FLR-enabled file system can be locked
         and protected from deletion.
       type: str
     default_retention:
       description:
       - The default retention period that is used in an
         FLR-enabled file system when a file is locked and
         a retention period is not specified.
       type: str
     maximum_retention:
       description:
       - The longest retention period for which files on an
         FLR-enabled file system can be locked and protected
         from deletion.
       type: str
     auto_lock:
       description:
       - Indicates whether to automatically lock files
         in an FLR-enabled file system.
       type: bool
     auto_delete:
       description:
       - Indicates whether locked files will be automatically
         deleted from an FLR-enabled file system once their
         retention periods have expired.
       - This setting can only be applied to a mounted FLR
         enabled file systems.
       type: bool
     policy_interval:
       description:
       - Indicates how long to wait (in seconds) after files
         are modified before the files are automatically locked.
       - This setting can only be applied to mounted FLR enabled
         file systems.
       type: int
 config_type:
   description:
   - Indicates the file system type.
   - Cannot be modified.
   choices: ['GENERAL', 'VMWARE']
   type: str
 is_async_mtime_enabled:
   description:
   - Indicates whether asynchronous MTIME is
     enabled on the file system or protocol
     snaps that are mounted writeable.
   type: bool
 file_events_publishing_mode:
   description:
   - State of the event notification services
     for all file systems of the NAS server.
   - It can only be set to C(NFS_ONLY) when
     I(config_typ) is set to C(VMWARE).
   choices: ['DISABLE', 'SMB_ONLY', 'NFS_ONLY', 'ALL']
   type: str
 host_io_size:
   description:
   - Typical size of writes from the server or other
     computer using the VMware file system to the
     storage system.
   - Can only be set when the I(config_type) is C(VMWARE).
   - Cannot be modified.
   choices: ['VMWARE_8K', 'VMWARE_16K', 'VMWARE_32K', 'VMWARE_64K']
   type: str
 clone_filesystem:
   description:
   - The attributes for filesystem clone.
   type: dict
   suboptions:
     name:
       description:
       - Name of the clone.
       - It can only be provided during creation of a filesystem clone.
       type: str
     description:
       description:
       - Description of the clone.
       type: str
     access_policy:
       description:
       - File system security access policies.
       - C(Native) - Native Security.
       - C(UNIX) - UNIX Security.
       - C(Windows) - Windows Security.
       choices: ['Native', 'UNIX', 'Windows']
       type: str
     locking_policy:
       description:
       - File system locking policies.
       - C(Advisory)- No lock checking for NFS and honor SMB lock range only for SMB.
       - C(Mandatory)- Honor SMB and NFS lock range.
       choices: ['Advisory', 'Mandatory']
       type: str
     folder_rename_policy:
       description:
       - File system folder rename policies for the file system with
         multi-protocol access enabled.
       - C(All_Allowed) - All protocols are allowed to rename directories without
         any restrictions.
       - C(SMB_Forbidden) - A directory rename from the SMB protocol will be
         denied if at least one file is opened in the directory or in one of its
         child directories.
       - C(All_Forbidden) - Any directory rename request will be denied regardless
         of the protocol used, if at least one file is opened in the directory
         or in one of its child directories.
       choices: ['All_Allowed', 'SMB_Forbidden', 'All_Forbidden']
       type: str
     is_smb_sync_writes_enabled:
       description:
       - Indicates whether the synchronous writes option is enabled on the
         file system.
       type: bool
     is_smb_no_notify_enabled:
       description:
       - Indicates whether notifications of changes to directory file
         structure are enabled.
       type: bool
     is_smb_op_locks_enabled:
       description:
       - Indicates whether opportunistic file locking is enabled on the file
         system.
       type: bool
     is_smb_notify_on_access_enabled:
       description:
       - Indicates whether file access notifications are enabled on the file
         system.
       type: bool
     is_smb_notify_on_write_enabled:
       description:
       - Indicates whether file write notifications are enabled on the file
         system.
       type: bool
     smb_notify_on_change_dir_depth:
       description:
       - Determines the lowest directory level to which the
         enabled notifications apply. minimum value is C(1).
       type: int
     is_async_MTime_enabled:
       description:
       - Indicates whether asynchronous MTIME is enabled on the file system.
       type: bool
     file_events_publishing_mode:
       description:
       - State of the event notification services for all file systems of the NAS server.
       - C(None) - File event notifications are disabled for this file system.
       - C(SMB_Only) - SMB notifications are enabled for this file system.
       - C(NFS_Only) - NFS notifications are enabled for this file system.
       - C(All) - SMB and NFS notifications are enabled for this file system.
       choices: ['None', 'SMB_Only', 'NFS_Only', 'All']
       type: str
     flr_attributes:
       description:
       - The attributes for file retention.
       type: dict
       suboptions:
         force_clone:
           description:
            - Specifies whether an FLR-C file system should be cloned.
            - C(true) - means cloning an FLR-C file system is allowed.
            - C(false) - means cloning an FLR-C file system is not allowed.
              and any attempt to do so will return an error.
           type: bool
 snapshot_name:
   description:
   - The name of the filesystem snapshot.
   - Specify either snapshot name or ID (but not both) for restore and refresh operations.
   type: str
 snapshot_id:
   description:
   - The ID of the Snapshot.
   - Specify either snapshot name or ID (but not both) for restore and refresh operations.
   type: str
 refresh_filesystem:
   description:
   - Specifies to refresh filesystem.
   - Mandatory only for refresh filesystem.
   type: bool
 restore_filesystem:
   description:
   - Specifies to restore filesystem.
   - Mandatory only for restore filesystem.
   type: bool
 backup_snap_name:
   description:
   - Name of the backup snap to be created before the restore operation occurs.
   type: str
 state:
   description:
   - Define whether the filesystem should exist or not.
   choices: ['absent', 'present']
   required: true
   type: str
notes:
- It is recommended to remove the protection policy before deleting the
  filesystem.
- The I(check_mode) is not supported.
- The pattern for I(minimum_retention), I(default_retention)
  and I(maximum_retention) is (^\d+[DMY])|(^infinite$).
- Filesystem snapshot can be created using filesystem_snapshot module.
'''

EXAMPLES = r'''
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
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"
is_filesystem_cloned:
    description: Whether or not the clone of filesystem is created.
    returned: always
    type: bool
    sample: "false"
is_filesystem_refreshed:
    description: Whether or not the filesystem is refreshed.
    returned: always
    type: bool
    sample: "false"
is_filesystem_restored:
    description: Whether or not the filesystem is restored.
    returned: always
    type: bool
    sample: "false"
filesystem_details:
    description: Details of the filesystem.
    returned: When filesystem exists
    type: complex
    contains:
        id:
            description: The system generated ID given to the filesystem.
            type: str
        name:
            description: Name of the filesystem.
            type: str
        description:
            description: The description about the filesystem.
            type: str
        protection_policy:
            description: Id and name of the protection policy associated with
                         the filesystem.
            type: dict
        nas_server:
            description: Id and name of the nas server to which the filesystem
                         belongs.
            type: dict
        size_total:
            description: Total size of the filesystem in bytes.
            type: int
        total_size_with_unit:
            description: Total size of the filesystem with appropriate unit.
            type: str
        size_used:
            description: Used size of the filesystem in bytes.
            type: int
        used_size_with_unit:
            description: Used size of the filesystem with appropriate unit.
            type: str
        access_policy:
            description: Access policy about the filesystem.
            type: str
        locking_policy:
            description: Locking policy about the filesystem.
            type: str
        is_smb_no_notify_enabled:
            description: Whether smb notify policy is enabled for a
                         filesystem.
            type: bool
        is_smb_notify_on_access_enabled:
            description: Whether smb on access notify policy is enabled.
            type: bool
        is_smb_op_locks_enabled:
            description: Whether smb op lock is enabled.
            type: bool
        grace_period:
            description: Default grace period for a filesystem quota in
                         second.
            type: int
        default_hard_limit:
            description: Default hard limit period for a filesystem quota in
                         byte.
            type: int
        default_soft_limit:
            description: Default soft limit period for a filesystem quota in
                         byte.
            type: int
        snapshots:
            description: Id and name of the snapshots of a filesystem.
            type: list
        is_async_MTime_enabled:
            description: Indicates whether asynchronous MTIME is enabled on the file system.
            type: bool
        file_events_publishing_mode:
            description: State of the event notification services for all file systems of the NAS server.
            type: str
        config_type:
            description: Indicates the file system type.
            type: str
        host_io_size:
            description: Typical size of writes from the server or other
                         computer using the VMware file system to the storage system.
            type: str
        flr_attributes:
            description: The file retention attributes.
            type: complex
            contains:
                mode:
                    description: The FLR type of the file system.
                    type: str
                minimum_retention:
                    description: The shortest retention period for which files on an
                                 FLR-enabled file system can be locked and protected
                                 from deletion.
                    type: str
                default_retention:
                    description: The default retention period that is used in an FLR-enabled
                                 file system when a file is locked and a retention period is
                                 not specified.
                    type: str
                maximum_retention:
                    description: The longest retention period for which files on an FLR-enabled
                                 file system can be locked and protected from deletion.
                    type: str
                auto_lock:
                    description: Indicates whether to automatically lock files in an FLR-enabled file system.
                    type: bool
                auto_delete:
                    description: Indicates whether locked files will be automatically deleted from an
                                 FLR-enabled file system once their retention periods have expired.
                    type: bool
                policy_interval:
                    description: Indicates how long to wait (in seconds) after files are
                                 modified before the files are automatically locked.
                    type: int
                has_protected_files:
                    description: Indicates whether FLR file system has protected files.
                    type: bool
                clock_time:
                    description: Per file system clock used to track the retention date.
                    type: str
                maximum_retention_date:
                    description: Maximum date and time that has been set on any locked file
                                 in an FLR-enabled file system, which means that the file
                                 system itself will be protected until this date and time.
                    type: str
        access_type:
            description: Indicates whether the snapshot directory or protocol
                         access is granted to the file system snapshot.
            type: str
        creation_timestamp:
            description: Time, in seconds, when the snapshot was created.
            type: str
        creator_type:
            description: Snapshot creator type.
            type: str
        expiration_timestamp:
            description: Time, in seconds, when the snapshot will expire.
            type: str
        filesystem_type:
            description: Indicates the type of a file system.
            type: str
        folder_rename_policy:
            description: File system folder rename policies for the file
                         system with multiprotocol access enabled.
            type: str
        is_modified:
            description: Indicates whether the snapshot may have
                         changed since it was created.
            type: bool
        is_quota_enabled:
            description: Indicates whether quota is enabled.
            type: bool
        is_smb_notify_on_write_enabled:
            description: Indicates whether file writes notifications
                         are enabled on the file system.
            type: bool
        is_smb_sync_writes_enabled:
            description: Indicates whether the synchronous writes
                         option is enabled on the file system.
            type: bool
        last_refresh_timestamp:
            description: Time, in seconds, when the snapshot was last refreshed.
            type: str
        last_writable_timestamp:
            description: If not mounted, and was previously mounted,
                         the time (in seconds) of last mount.
            type: str
        parent_id:
            description: Unique identifier of the object of the parent of this file system.
            type: str
        smb_notify_on_change_dir_depth:
            description: Lowest directory level to which the enabled notifications apply, if any.
            type: int
    sample: {
        "access_policy": "Native",
        "access_policy_l10n": "Native",
        "access_type": null,
        "access_type_l10n": null,
        "creation_timestamp": null,
        "creator_type": null,
        "creator_type_l10n": null,
        "default_hard_limit": 0,
        "default_soft_limit": 0,
        "description": null,
        "expiration_timestamp": null,
        "filesystem_type": "Primary",
        "filesystem_type_l10n": "Primary",
        "folder_rename_policy": "All_Forbidden",
        "folder_rename_policy_l10n": "All Renames Forbidden",
        "grace_period": 604800,
        "id": "61e49f3f-9b57-e69b-1038-aa02b52a030f",
        "is_async_MTime_enabled": false,
        "is_modified": false,
        "is_quota_enabled": false,
        "is_smb_no_notify_enabled": false,
        "is_smb_notify_on_access_enabled": false,
        "is_smb_notify_on_write_enabled": false,
        "is_smb_op_locks_enabled": true,
        "is_smb_sync_writes_enabled": true,
        "last_refresh_timestamp": null,
        "last_writable_timestamp": null,
        "locking_policy": "Advisory",
        "locking_policy_l10n": "Advisory",
        "name": "sample-filesystem",
        nas_server: {
            "id": "6026056b-5405-0e36-7697-c285b9fa42b7",
            "name": "ansible_nas_server_2"
        },
        "parent_id": null,
        "protection_policy": null,
        "size_total": "214748364800",
        "size_used": "1621098496",
        "smb_notify_on_change_dir_depth": 512,
        "snapshots": {},
        "total_size_with_unit": "200.0 GB",
        "used_size_with_unit": "1.51 GB"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils
import logging

LOG = utils.get_logger('filesystem',
                       log_devel=logging.INFO)

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/3.3.0'


class PowerStoreFileSystem(object):
    """File System operations"""
    cluster_name = None
    cluster_global_id = None
    IS_NAME = "NAME"
    protection_policy_id = None
    total_size = 0

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_filesystem_parameters())

        mutually_exclusive = [['filesystem_name', 'filesystem_id'], ['snapshot_name', 'snapshot_id']]
        required_one_of = [['filesystem_name', 'filesystem_id', 'snapshot_name', 'snapshot_id']]

        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mutually_exclusive,
            required_one_of=required_one_of
        )
        msg = 'HAS_PY4PS = {0} , IMPORT_ERROR = ' \
              '{1}'.format(HAS_PY4PS, IMPORT_ERROR)
        LOG.info(msg)
        if HAS_PY4PS is False:
            self.module.fail_json(msg=IMPORT_ERROR)
        msg = 'IS_SUPPORTED_PY4PS_VERSION = {0} , ' \
              'VERSION_ERROR = {1}'.format(IS_SUPPORTED_PY4PS_VERSION,
                                           VERSION_ERROR)
        LOG.info(msg)
        if IS_SUPPORTED_PY4PS_VERSION is False:
            self.module.fail_json(msg=VERSION_ERROR)

        self.conn = utils.get_powerstore_connection(
            self.module.params,
            application_type=APPLICATION_TYPE)
        self.provisioning = self.conn.provisioning
        msg = 'Got Py4ps instance for provisioning on ' \
              'PowerStore {0}'.format(self.conn)
        LOG.info(msg)
        self.protection = self.conn.protection
        msg = 'Got Py4ps instance for protection on' \
              ' PowerStore {0}'.format(self.protection)
        LOG.info(msg)

    def get_filesystem_details(self, filesystem_id=None,
                               filesystem_name=None,
                               nas_server_id=None):
        """Get the details of a File System on a PowerStore storage system"""

        try:
            fs_details = None
            msg = 'Getting File System Details with filesystem_id {0}, ' \
                  'filesystem_name {1} , nas_server_id ' \
                  '{2}'.format(filesystem_id, filesystem_name, nas_server_id)
            LOG.info(msg)

            if filesystem_id:
                fs_details = self.provisioning.get_filesystem_details(
                    filesystem_id=filesystem_id)
            elif filesystem_name and nas_server_id:
                fs_details = self.provisioning.get_filesystem_by_name(
                    filesystem_name=filesystem_name,
                    nas_server_id=nas_server_id)
                if fs_details:
                    # implement in sdk , workaround
                    fs_details = fs_details[0]
                else:
                    fs_details = None
            else:
                self.module.fail_json(msg="Invalid Option")
            msg = 'Successfully Got FileSystem Details' \
                  ' {0}'.format(fs_details)
            LOG.info(msg)
            return fs_details

        except Exception as e:
            msg = 'Get FileSystem Details for powerstore array name : ' \
                  '{0} , global id : {1} failed with error' \
                  ' {2} '.format(self.cluster_name, self.cluster_global_id,
                                 str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR \
                    and e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_nas_server(self, nas_server):
        """Get the details of NAS Server of a given Powerstore storage
        system"""

        try:
            msg = 'Getting NAS Server details {0}'.format(nas_server)
            LOG.info(msg)
            id_or_name = utils.name_or_id(val=nas_server)
            if id_or_name == self.IS_NAME:
                nas_details = self.provisioning.get_nas_server_by_name(
                    nas_server_name=nas_server)
                if nas_details:  # implement in sdk , workaround
                    nas_details = nas_details[0]['id']
            else:
                nas_details = self.provisioning.get_nas_server_details(
                    nas_server_id=nas_server)
                if nas_details:  # implement in sdk , workaround
                    nas_details = nas_details['id']

            if nas_details:
                msg = 'Successfully got NAS Server details {0} from ' \
                      'powerstore array name : {1} ,global id' \
                      ' : {2}'.format(nas_details, self.cluster_name,
                                      self.cluster_global_id)
                LOG.info(msg)

                return nas_details
            else:
                msg = 'Failed to get NAS Server with id or name {0} from ' \
                      'powerstore system'.format(nas_server)

            self.module.fail_json(msg=msg)

        except Exception as e:
            msg = 'Get NAS Server {0} for powerstore array name : {1} , ' \
                  'global id : {2} failed with error' \
                  ' {3} '.format(nas_server, self.cluster_name,
                                 self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_protection_policy(self, protection_policy):
        """Get protection policy"""
        try:
            msg = 'Getting the details of protection policy' \
                  ' {0}'.format(protection_policy)
            LOG.info(msg)
            id_or_name = utils.name_or_id(val=protection_policy)
            if id_or_name == self.IS_NAME:
                resp = self.protection.get_protection_policy_by_name(
                    name=protection_policy)
                if resp and len(resp) > 0:
                    pp_id = resp[0]['id']
                    msg = 'Successfully got the details of protection ' \
                          'policy name is {0} and id is ' \
                          '{1}'.format(protection_policy, pp_id)
                    LOG.info(msg)
                    return pp_id
            else:
                detail_resp = self.protection.get_protection_policy_details(
                    policy_id=protection_policy)
                if detail_resp:
                    pp_id = detail_resp['id']
                    msg = 'Successfully got the details of protection' \
                          ' policy name {0} and id is' \
                          ' {1}'.format(protection_policy, pp_id)
                    LOG.info(msg)
                    return pp_id

            msg = 'No protection policy present with name or id {0}'. \
                format(protection_policy)
            LOG.debug(msg)
            self.module.fail_json(msg=msg)

        except Exception as e:
            msg = 'Get details of protection policy name or ID : {0} ' \
                  'failed with error : {1} '.format(protection_policy,
                                                    str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def create_filesystem_dict_params(self, adv_parameters):
        """Create a filesystem."""
        smb_properties = self.module.params['smb_properties']
        if self.module.params['flr_attributes'] is not None:
            adv_parameters['flr_attributes'] = {}
            for key, value in self.module.params['flr_attributes'].items():
                if value is not None:
                    adv_parameters['flr_attributes'][key] = value

        if self.protection_policy_id:
            adv_parameters['protection_policy_id'] = \
                self.protection_policy_id

        if smb_properties:
            for key, value in smb_properties.items():
                if value is not None:
                    adv_parameters[key] = value

        return adv_parameters

    def create_filesystem(self, name, nas_server_id, size_total):
        """Create a filesystem."""
        try:
            LOG.info("Attempting to create filesystem name "
                     "%s", name)
            adv_parameters = dict()
            adv_param_list_enum = ['access_policy', 'locking_policy',
                                   'folder_rename_policy', 'config_type',
                                   'host_io_size', 'file_events_publishing_mode']

            if self.module.params['description'] is not None:
                adv_parameters['description'] = self.module.params['description']

            if self.module.params['is_async_mtime_enabled'] is not None:
                adv_parameters['is_async_MTime_enabled'] = self.module.params['is_async_mtime_enabled']

            for param in adv_param_list_enum:
                if self.module.params[param] is not None:
                    adv_parameters[param] = self.get_enum_keys(self.module.params[param])

            adv_parameters = self.create_filesystem_dict_params(adv_parameters)
            resp = self.provisioning.create_filesystem(
                name=name,
                nas_server_id=nas_server_id,
                size_total=size_total,
                advance_parameters=adv_parameters)

            LOG.info("Successfully Created FileSystem with "
                     "details : %s", str(resp))

            return resp.get("id")

        except Exception as e:
            msg = 'Create FileSystem with name {0} on powerstore array ' \
                  'name : {1} , global id : {2} failed with ' \
                  'error {3} '.format(name, self.cluster_name,
                                      self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def delete_filesystem(self, filesystem_id):
        """Deletes a filesystem"""
        try:
            LOG.info("Attempting to delete filesystem id "
                     "%s", str(filesystem_id))
            self.provisioning.delete_filesystem(filesystem_id=filesystem_id)
        except Exception as e:
            msg = 'Failed to delete filesystem id {0} with ' \
                  'error {1}'.format(filesystem_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def to_modify_quota_limits(self, quota_defaults, filesystem_details,
                               modify_parameters, enable_quota):
        """Check if modification of quota limits is needed"""
        default_hard_limit = quota_defaults['default_hard_limit']
        default_soft_limit = quota_defaults['default_soft_limit']
        cap_unit = quota_defaults['cap_unit']

        if (default_hard_limit is not None) or \
                (default_soft_limit is not None):
            if not cap_unit:
                cap_unit = 'GB'
            if default_hard_limit is not None:
                param_hard_limit = utils.get_size_bytes(
                    default_hard_limit, cap_unit)
                if param_hard_limit != \
                        filesystem_details['default_hard_limit']:
                    modify_parameters['default_hard_limit'] = \
                        param_hard_limit
                    enable_quota = True
            if default_soft_limit is not None:
                param_soft_limit = utils.get_size_bytes(
                    default_soft_limit, cap_unit)
                if param_soft_limit != \
                        filesystem_details['default_soft_limit']:
                    modify_parameters['default_soft_limit'] = \
                        param_soft_limit
                    enable_quota = True
        return enable_quota, modify_parameters

    def to_modify_filesystem_quota(self, filesystem_details, modify_parameters, quota_defaults):
        """Determines if any modification required on a specific
        filesystem instance."""

        LOG.info("Checking if modification is required for quota ")
        grace_period = quota_defaults['grace_period']
        grace_period_unit = quota_defaults['grace_period_unit']
        enable_quota = False
        is_quota_enabled = filesystem_details['is_quota_enabled']

        if grace_period is not None:
            if not grace_period_unit:
                grace_period_unit = 'days'
            param_grace_period = get_graceperiod_seconds(
                grace_period, grace_period_unit)
            if param_grace_period != \
                    filesystem_details['grace_period']:
                modify_parameters[
                    'grace_period'] = param_grace_period
                enable_quota = True

        enable_quota, modify_parameters = self.to_modify_quota_limits(quota_defaults, filesystem_details,
                                                                      modify_parameters, enable_quota)
        if enable_quota and (not is_quota_enabled):
            modify_parameters['is_quota_enabled'] = enable_quota

        LOG.debug("Modify Dict %s", str(modify_parameters))
        return modify_parameters

    def to_modify_protection_policy(self, modify_parameters, filesystem_details):
        """Check if modification of protection policy is needed"""

        if self.protection_policy_id and (
                (filesystem_details['protection_policy'] is None) or
                (filesystem_details['protection_policy'] is not None and
                 self.protection_policy_id !=
                 filesystem_details['protection_policy']['id'])):
            modify_parameters['protection_policy_id'] = \
                self.protection_policy_id

        # to handle the remove with "" case
        if self.protection_policy_id == "" and (
                filesystem_details['protection_policy'] is not None):
            modify_parameters['protection_policy_id'] = \
                self.protection_policy_id

        return modify_parameters

    def to_modify_flr_attributes(self, modify_parameters, filesystem_details):
        """Check if modification of file retention attributes is needed"""
        flr_attributes = self.module.params['flr_attributes']
        if flr_attributes is not None:
            modify_parameters['flr_attributes'] = {}
            for key, value in flr_attributes.items():
                if value is not None and \
                        filesystem_details['flr_attributes'][key] != value:
                    modify_parameters['flr_attributes'][key] = value
            if modify_parameters['flr_attributes'] == {}:
                del modify_parameters['flr_attributes']

        return modify_parameters

    def to_modify_smb_attributes(self, modify_parameters, filesystem_details):
        """Check if modification of SMB properties is needed"""
        smb_properties = self.module.params['smb_properties']
        if smb_properties:
            for key, value in smb_properties.items():
                if value is not None and \
                        filesystem_details[key] != value:
                    modify_parameters[key] = value

        return modify_parameters

    def to_modify_flr_smb_quota(self, modify_parameters, filesystem_details):
        """Check if modification of file retention, SMB or Quota attributes is needed"""
        modify_parameters = self.to_modify_flr_attributes(modify_parameters,
                                                          filesystem_details)

        # advance smb attributes
        modify_parameters = self.to_modify_smb_attributes(modify_parameters,
                                                          filesystem_details)
        quota_defaults = self.module.params['quota_defaults']
        if quota_defaults:
            modify_parameters = self.to_modify_filesystem_quota(filesystem_details,
                                                                modify_parameters,
                                                                quota_defaults)

        return modify_parameters

    def to_modify_filesystem(self, filesystem_details):
        """Determines if any modification required on a specific
        filesystem instance."""

        LOG.info("Checking if Modify required for filesystem ")
        modify_parameters = dict()

        description = self.module.params['description']
        if (description is not None) and description != \
                filesystem_details['description']:
            modify_parameters['description'] = description

        is_async_mtime_enabled = self.module.params['is_async_mtime_enabled']
        if (is_async_mtime_enabled is not None) and is_async_mtime_enabled != \
                filesystem_details['is_async_MTime_enabled']:
            modify_parameters['is_async_MTime_enabled'] = is_async_mtime_enabled

        if (self.total_size > 0) and \
                (filesystem_details['size_total'] != self.total_size):
            modify_parameters['size_total'] = self.total_size

        adv_param_list_enum = ['access_policy', 'locking_policy',
                               'folder_rename_policy', 'file_events_publishing_mode']

        for param in adv_param_list_enum:
            if self.module.params[param] is not None and (filesystem_details[param] is None or
                                                          self.module.params[param] !=
                                                          (filesystem_details[param]).upper()):
                modify_parameters[param] = \
                    self.get_enum_keys(self.module.params[param])

        modify_parameters = self.to_modify_protection_policy(modify_parameters, filesystem_details)

        modify_parameters = self.to_modify_flr_smb_quota(modify_parameters, filesystem_details)

        return modify_parameters

    def modify_filesystem(self, filesystem_id, modify_parameters):
        """Modify FileSystem attributes."""
        try:
            if modify_parameters:
                self.provisioning.modify_filesystem(
                    filesystem_id=filesystem_id,
                    modify_parameters=modify_parameters)
            return

        except Exception as e:
            msg = 'Failed to modify filesystem id {0} with ' \
                  'error {1}'.format(filesystem_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def display_filesystem_details(self, filesystem_id):
        """Display FileSystem details"""

        try:
            fs_details = self.provisioning.get_filesystem_details(
                filesystem_id=filesystem_id)
            snapshots = self.provisioning.get_snapshots_filesystem(
                filesystem_id=filesystem_id)
            if snapshots:
                fs_details['snapshots'] = snapshots
            else:
                fs_details['snapshots'] = {}

            if fs_details['size_total']:
                fs_details['total_size_with_unit'] = \
                    utils.convert_size_with_unit(
                        int(fs_details['size_total']))

            if fs_details['size_used']:
                fs_details['used_size_with_unit'] = \
                    utils.convert_size_with_unit(
                        int(fs_details['size_used']))

            return fs_details

        except Exception as e:
            msg = 'Failed to display filesystem id {0} with ' \
                  'error {1}'.format(filesystem_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_clusters(self):
        """Get the clusters"""
        try:
            clusters = self.provisioning.get_cluster_list()
            return clusters

        except Exception as e:
            msg = 'Failed to get the clusters with ' \
                  'error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_enum_keys(self, user_input):
        """Get the ENUM Keys for user input string"""
        try:
            enum_dict = {
                "NATIVE": "Native",
                "UNIX": "UNIX",
                "WINDOWS": "Windows",
                "ADVISORY": "Advisory",
                "MANDATORY": "Mandatory",
                "ALL_ALLOWED": "All_Allowed",
                "SMB_FORBIDDEN": "SMB_Forbidden",
                "ALL_FORBIDDEN": "All_Forbidden",
                "GENERAL": "General",
                "VMWARE": "VMware",
                "DISABLE": "None",
                "SMB_ONLY": "SMB_Only",
                "NFS_ONLY": "NFS_Only",
                "ALL": "All",
                "VMWARE_8K": "VMware_8K",
                "VMWARE_16K": "VMware_16K",
                "VMWARE_32K": "VMware_32K",
                "VMWARE_64K": "VMware_64K"
            }
            return enum_dict[user_input]

        except Exception as e:
            msg = 'Failed to get the enum value for user_ip : %s with ' \
                  'error %s' % (user_input, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def set_params(self, size, cap_unit, nas_server, protection_policy,
                   filesystem_name, filesystem_id):
        fs_details = None
        if size is not None:
            if cap_unit:
                self.total_size = utils.get_size_bytes(size, cap_unit)
            else:
                self.total_size = utils.get_size_bytes(size, 'GB')
            min_size = utils.get_size_bytes(3, 'GB')
            if self.total_size < min_size:
                err_msg = "Size must be minimum of 3GB"
                LOG.error(err_msg)
                self.module.fail_json(msg=err_msg)

        if (cap_unit is not None) and not size:
            self.module.fail_json(msg="cap_unit can be specified along "
                                      "with size")
        if protection_policy is not None:
            if protection_policy == "":
                self.protection_policy_id = protection_policy
            else:
                self.protection_policy_id = self.get_protection_policy(
                    protection_policy=protection_policy)
        if filesystem_name and nas_server:
            fs_details = self.get_filesystem_details(
                filesystem_name=filesystem_name, nas_server_id=nas_server)
        elif filesystem_id:
            fs_details = self.get_filesystem_details(
                filesystem_id=filesystem_id)
        return size, protection_policy, fs_details

    def validate_modify(self, fs_details):

        non_modify = ['config_type', 'host_io_size']
        for param in non_modify:
            if fs_details and self.module.params[param] is not None and \
                    fs_details[param] != self.get_enum_keys(self.module.params[param]):
                self.module.fail_json(msg=param + " cannot be modified.")

        if self.module.params['quota_defaults'] is not None:
            limit_types = ['default_hard_limit', 'default_soft_limit']
            for limit in limit_types:
                if self.module.params['quota_defaults'][limit] is not None and \
                        self.module.params['quota_defaults'][limit] < 0:
                    msg = limit + " cannot be less than '0'"
                    LOG.error(msg)
                    self.module.fail_json(msg=msg)

    def clone_filesystem_dict_params(self, clone_filesystem):
        adv_parameters = {}
        adv_param_list_enum = [
            'name', 'description', 'access_policy', 'locking_policy',
            'folder_rename_policy', 'is_smb_sync_writes_enabled',
            'is_smb_no_notify_enabled', 'is_smb_op_locks_enabled',
            'is_smb_notify_on_access_enabled', 'is_smb_notify_on_write_enabled',
            'smb_notify_on_change_dir_depth', 'is_async_MTime_enabled',
            'file_events_publishing_mode', 'flr_attributes'
        ]

        for param in adv_param_list_enum:
            if clone_filesystem[param] is not None:
                adv_parameters[param] = clone_filesystem[param]
        return adv_parameters

    def clone_filesystem(self, filesystem_id, clone_filesystem):
        """Clone filesystem"""
        try:
            LOG.info("Cloning filesystem")
            adv_parameters = self.clone_filesystem_dict_params(clone_filesystem)
            resp = self.provisioning.clone_filesystem(filesystem_id,
                                                      advance_parameters=adv_parameters)
            LOG.debug(resp)
            return resp["id"]
        except Exception as e:
            errormsg = f"Cloning filesystem failed with error {str(e)}"
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg, **utils.failure_codes(e))

    def verify_required_together_params(self, filesystem_name=None,
                                        snapshot_name=None,
                                        nas_server=None):
        if (filesystem_name or snapshot_name) and not nas_server:
            errormsg = "nas_server is required along with, filesystem_name or snapshot_name"
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)
        elif nas_server and not (filesystem_name or snapshot_name):
            errormsg = "filesystem_name or snapshot_name is required along with, nas_server"
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def get_snapshot_details_by_name(self, name, nas_server):
        try:
            snap_details = self.protection.get_filesystem_snapshot_details_by_name(snapshot_name=name,
                                                                                   nas_server_id=nas_server)
            return snap_details[0] if snap_details else None
        except Exception as e:
            LOG.error("Error getting snapshot details by name: %s", str(e))
            raise

    def get_snap_details(self, snapshot_id=None,
                         snapshot_name=None,
                         nas_server=None,
                         backup_snap_name=None):
        try:
            snap_details = None
            if snapshot_id:
                snap_details = self.protection.get_filesystem_snapshot_details(snapshot_id=snapshot_id)
            elif snapshot_name and nas_server:
                snap_details = self.get_snapshot_details_by_name(snapshot_name, nas_server)
                if not snap_details:
                    errormsg = f"Instance with name {str(snapshot_name)} was not found."
                    LOG.error(errormsg)
                    self.module.fail_json(msg=errormsg)
            elif backup_snap_name and nas_server:
                snap_details = self.get_snapshot_details_by_name(backup_snap_name, nas_server)
                if not snap_details:
                    return None
            return snap_details
        except Exception as e:
            errormsg = f"Failed to get filesystem snapshot {str(e)}"
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg, **utils.failure_codes(e))

    def refresh_filesystem(self, snapshot_id=None):
        """Refresh filesystem"""
        try:
            LOG.info("Refreshing filesystem")
            self.provisioning.refresh_filesystem(snapshot_id)
            return True
        except Exception as e:
            errormsg = f"Refreshing filesystem failed with error {str(e)}"
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg, **utils.failure_codes(e))

    def restore_filesystem(self, snapshot_id=None,
                           backup_snap_name=None):
        """Restore filesystem"""
        try:
            LOG.info("Restoring filesystem")
            self.provisioning.restore_filesystem(snapshot_id, backup_snap_name)
            return True
        except Exception as e:
            errormsg = f"Restoring filesystem failed with error {str(e)}"
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg, **utils.failure_codes(e))

    def get_clone(self, clone_name, nas_server_id):
        """Get Clone filesystem"""
        if clone_name:
            clone = self.get_filesystem_details(filesystem_name=clone_name,
                                                nas_server_id=nas_server_id)
            return clone
        else:
            errormsg = "'name' parameter is required in clone_filesystem"
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def perform_module_operation(self):
        clusters = self.get_clusters()
        if len(clusters) > 0:
            self.cluster_name = clusters[0]['name']
            self.cluster_global_id = clusters[0]['id']
        else:
            self.module.fail_json(
                msg="Unable to find any active cluster on this array ")

        filesystem_name = self.module.params['filesystem_name']
        filesystem_id = self.module.params['filesystem_id']
        nas_server = self.module.params['nas_server']
        size = self.module.params['size']
        cap_unit = self.module.params['cap_unit']
        protection_policy = self.module.params['protection_policy']
        clone_filesystem = self.module.params['clone_filesystem']
        refresh_filesystem = self.module.params['refresh_filesystem']
        restore_filesystem = self.module.params['restore_filesystem']
        snapshot_name = self.module.params['snapshot_name']
        snapshot_id = self.module.params['snapshot_id']
        backup_snap_name = self.module.params['backup_snap_name']
        state = self.module.params['state']

        # result is a dictionary to contain end state and filesystem details
        changed = False
        is_filesystem_restored = False
        is_filesystem_refreshed = False
        is_filesystem_cloned = False
        result = dict(
            changed=False,
            filesystem_details=None
        )
        self.verify_required_together_params(filesystem_name, snapshot_name, nas_server)
        fs_id = None
        to_modify = False
        to_modify_dict = None
        if nas_server:
            nas_server = self.get_nas_server(nas_server=nas_server)
        size, protection_policy, fs_details = \
            self.set_params(size, cap_unit, nas_server, protection_policy,
                            filesystem_name, filesystem_id)

        self.validate_modify(fs_details)

        if not fs_details and state == 'present' and not (snapshot_id or snapshot_name or clone_filesystem):
            fs_id = self.create_filesystem(
                name=filesystem_name,
                nas_server_id=nas_server,
                size_total=self.total_size)
            changed = True
            fs_details = self.get_filesystem_details(
                filesystem_id=fs_id)

        if fs_details:
            fs_id = fs_details['id']
            to_modify_dict = self.to_modify_filesystem(fs_details)
            if to_modify_dict:
                to_modify = True
            LOG.info("FileSystem Details: %s , To Modify %s", fs_details,
                     to_modify)
        if to_modify and state == 'present':
            self.modify_filesystem(
                filesystem_id=fs_id,
                modify_parameters=to_modify_dict)
            changed = True

        if state == 'present' and clone_filesystem:
            if filesystem_id:
                nas_server = fs_details['nas_server']['id']
            clone = self.get_clone(clone_name=clone_filesystem['name'],
                                   nas_server_id=nas_server)
            if not clone:
                if filesystem_name and nas_server:
                    fs_details = self.get_filesystem_details(filesystem_name=filesystem_name,
                                                             nas_server_id=nas_server)
                    filesystem_id = fs_details['id']
                self.clone_filesystem(filesystem_id, clone_filesystem)
                changed = True
                is_filesystem_cloned = True

        if (snapshot_id or snapshot_name) and \
                not (refresh_filesystem or restore_filesystem):
            errormsg = "Either refresh_filesystem or restore_filesystem is required"
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)
        elif (snapshot_id or snapshot_name) and \
                (refresh_filesystem or restore_filesystem):
            snap = self.get_snap_details(snapshot_id=snapshot_id,
                                         snapshot_name=snapshot_name,
                                         nas_server=nas_server)
            fs_id = snap['parent_id']
            snapshot_id = snap['id']
            nas_server = snap['nas_server']['id']

        if state == 'present' and refresh_filesystem and \
                (snapshot_id or snapshot_name):
            self.refresh_filesystem(snapshot_id=snapshot_id)
            fs_details = self.get_filesystem_details(filesystem_id=fs_id)
            changed = True
            is_filesystem_refreshed = True

        if state == 'present' and restore_filesystem and \
                (snapshot_id or snapshot_name):
            backup_snap = None
            if backup_snap_name:
                backup_snap = self.get_snap_details(nas_server=nas_server,
                                                    backup_snap_name=backup_snap_name)
            if not backup_snap:
                self.restore_filesystem(snapshot_id=snapshot_id,
                                        backup_snap_name=backup_snap_name)
                changed = True
                is_filesystem_restored = True
            fs_details = self.get_filesystem_details(filesystem_id=fs_id)

        if state == 'absent' and fs_details:
            self.delete_filesystem(filesystem_id=fs_id)
            fs_details = None
            changed = True

        if state == 'present' and fs_details:
            fs_details = self.display_filesystem_details(
                filesystem_id=fs_id)

        result['changed'] = changed
        result['is_filesystem_restored'] = is_filesystem_restored
        result['is_filesystem_refreshed'] = is_filesystem_refreshed
        result['is_filesystem_cloned'] = is_filesystem_cloned
        result['filesystem_details'] = fs_details
        self.module.exit_json(**result)


def get_graceperiod_seconds(grace_period, unit):
    """Get the second for Grace period"""

    day = 86400
    week = day * 7
    month = day * 30

    if unit == 'days':
        return grace_period * day
    if unit == 'weeks':
        return grace_period * week
    if unit == 'months':
        return grace_period * month


def get_powerstore_filesystem_parameters():
    """This method provides the parameters required for the ansible
    filesystem modules on PowerStore"""
    return dict(
        filesystem_name=dict(type='str'),
        filesystem_id=dict(type='str'),
        description=dict(type='str'),
        nas_server=dict(type='str'),
        size=dict(type='int'),
        cap_unit=dict(type='str', choices=['GB', 'TB']),
        access_policy=dict(type='str',
                           choices=['NATIVE', 'UNIX', 'WINDOWS']),
        locking_policy=dict(type='str',
                            choices=['ADVISORY', 'MANDATORY']),
        folder_rename_policy=dict(type='str',
                                  choices=['ALL_ALLOWED', 'SMB_FORBIDDEN',
                                           'ALL_FORBIDDEN']),
        config_type=dict(type='str', choices=['GENERAL', 'VMWARE']),
        is_async_mtime_enabled=dict(type='bool'),
        file_events_publishing_mode=dict(type='str',
                                         choices=['DISABLE', 'SMB_ONLY', 'NFS_ONLY', 'ALL']),
        host_io_size=dict(type='str',
                          choices=['VMWARE_8K', 'VMWARE_16K', 'VMWARE_32K', 'VMWARE_64K']),
        flr_attributes=dict(
            type='dict', options=dict(
                mode=dict(type='str', choices=['Enterprise', 'Compliance']),
                minimum_retention=dict(type='str'),
                default_retention=dict(type='str'),
                maximum_retention=dict(type='str'),
                auto_lock=dict(type='bool'),
                auto_delete=dict(type='bool'),
                policy_interval=dict(type='int')
            )
        ),
        clone_filesystem=dict(
            type='dict', options=dict(
                name=dict(type='str'),
                description=dict(type='str'),
                access_policy=dict(choices=['Native', 'UNIX', 'Windows'], type='str'),
                locking_policy=dict(choices=['Advisory', 'Mandatory'], type='str'),
                folder_rename_policy=dict(choices=['All_Allowed', 'SMB_Forbidden', 'All_Forbidden'], type='str'),
                is_smb_sync_writes_enabled=dict(type='bool'),
                is_smb_no_notify_enabled=dict(type='bool'),
                is_smb_op_locks_enabled=dict(type='bool'),
                is_smb_notify_on_access_enabled=dict(type='bool'),
                is_smb_notify_on_write_enabled=dict(type='bool'),
                smb_notify_on_change_dir_depth=dict(type='int'),
                is_async_MTime_enabled=dict(type='bool'),
                file_events_publishing_mode=dict(choices=['All', 'None', 'SMB_Only', 'NFS_Only'], type='str'),
                flr_attributes=dict(type='dict',
                                    options=dict(force_clone=dict(type='bool')))
            )
        ),
        snapshot_name=dict(type='str'),
        snapshot_id=dict(type='str'),
        refresh_filesystem=dict(type='bool'),
        restore_filesystem=dict(type='bool'),
        backup_snap_name=dict(type='str'),
        smb_properties=dict(
            type='dict', options=dict(
                is_smb_sync_writes_enabled=dict(type='bool'),
                is_smb_no_notify_enabled=dict(type='bool'),
                is_smb_op_locks_enabled=dict(type='bool'),
                is_smb_notify_on_access_enabled=dict(type='bool'),
                is_smb_notify_on_write_enabled=dict(type='bool'),
                smb_notify_on_change_dir_depth=dict(type='int')
            )
        ),
        protection_policy=dict(type='str'),
        quota_defaults=dict(
            type='dict', options=dict(
                grace_period=dict(type='int'),
                grace_period_unit=dict(type='str',
                                       choices=['days', 'weeks', 'months']),
                default_hard_limit=dict(type='int'),
                default_soft_limit=dict(type='int'),
                cap_unit=dict(type='str', choices=['GB', 'TB'])
            )
        ),
        state=dict(required=True, type='str', choices=['present', 'absent'])
    )


def main():
    """ Create PowerStore FileSystem object and perform action on it
        based on user input from playbook """
    obj = PowerStoreFileSystem()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
