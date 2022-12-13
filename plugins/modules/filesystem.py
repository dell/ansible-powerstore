#!/usr/bin/python
# Copyright: (c) 2020-2021, Dell Technologies
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

extends_documentation_fragment:
  - dellemc.powerstore.powerstore
author:
- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
options:
 filesystem_name:
   description:
   - Name of the file system. Mutually exclusive with filesystem_id.
     Mandatory only for create operation.
   type: str
 filesystem_id:
   description:
   - Unique id of the file system. Mutually exclusive with filesystem_name.
   type: str
 description:
   description:
   - Description of the file system.
   type: str
 nas_server:
   description:
   - Name or ID of the NAS Server on which the file system is created.
     Mandatory parameter whenever filesystem_name is provided,
     since filesystem names are unique only within a NAS server.
   type: str
 size:
   description:
   - Size that the file system presents to the host or end user.
     Mandatory only for create operation.
   type: int
 cap_unit:
   description:
   - Capacity unit for the size.
   - It defaults to 'GB', if not specified.
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
     ADVISORY- No lock checking for NFS and honor SMB lock range only for SMB.
     MANDATORY- Honor SMB and NFS lock range.
   choices: [ADVISORY, MANDATORY]
   type: str
 folder_rename_policy:
   description:
   - File system folder rename policies for the file system with
     multi-protocol access enabled.
   - ALL_ALLOWED - All protocols are allowed to rename directories without
     any restrictions.
   - SMB_FORBIDDEN - A directory rename from the SMB protocol will be
     denied if at least one file is opened in the directory or in one of its
     child directories.
   - All_FORBIDDEN - Any directory rename request will be denied regardless
     of the protocol used, if at least one file is opened in the directory
     or in one of its child directories.
   choices: ['ALL_ALLOWED', 'SMB_FORBIDDEN', 'ALL_FORBIDDEN']
   type: str
 smb_properties:
   description:
   - Advance settings for SMB. It contains below optional candidate variables.
   type: dict
   suboptions:
     is_smb_sync_writes_enabled:
       description:
       - Indicates whether the synchronous writes option is enabled on the
        file system.
       type: bool
       required: False
     is_smb_no_notify_enabled:
       description:
       - Indicates whether notifications of changes to directory file
        structure are enabled.
       type: bool
       required: False
     is_smb_op_locks_enabled:
       description:
       - Indicates whether opportunistic file locking is enabled on the file
        system.
       type: bool
       required: False
     is_smb_notify_on_access_enabled:
       description:
       - Indicates whether file access notifications are enabled on the file
        system.
       type: bool
       required: False
     is_smb_notify_on_write_enabled:
       description:
       - Indicates whether file write notifications are enabled on the file
        system.
       type: bool
       required: False
     smb_notify_on_change_dir_depth:
       description:
       - Integer variable , determines the lowest directory level to which the
        enabled notifications apply. minimum value is 1.
       type: int
       required: False
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
       required: False
     grace_period_unit:
       description:
       - Unit of the grace period of soft limit.
       type: str
       choices: ['days', 'weeks', 'months']
       required: False
     default_hard_limit:
       description:
       - Default hard limit of user quotas and tree quotas.
       type: int
       required: False
     default_soft_limit:
       description:
       - Default soft limit of user quotas and tree quotas.
       type: int
       required: False
     cap_unit:
       description:
       - Capacity unit for default hard & soft limit.
       type: str
       choices: ['GB', 'TB']
       required: False
 state:
   description:
   - Define whether the filesystem should exist or not.
   choices: ['absent', 'present']
   required: True
   type: str
notes:
- It is recommended to remove the protection policy before deleting the
  filesystem.
- The check_mode is not supported.
'''

EXAMPLES = r'''

 - name: Create FileSystem by Name
   register: result_fs
   dellemc.powerstore.filesystem:
     array_ip: "{{array_ip}}"
     verifycert: "{{verifycert}}"
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
       is_smb_no_notify_enabled: True
       is_smb_notify_on_access_enabled: True
     quota_defaults:
       grace_period: 1
       grace_period_unit: 'days'
       default_hard_limit: 3
       default_soft_limit: 2
     protection_policy: "{{protection_policy_id}}"
     state: "present"

 - name: Modify File System by id
   dellemc.powerstore.filesystem:
     array_ip: "{{array_ip}}"
     verifycert: "{{verifycert}}"
     user: "{{user}}"
     password: "{{password}}"
     filesystem_id: "{{fs_id}}"
     folder_rename_policy: "ALL_ALLOWED"
     smb_properties:
       is_smb_op_locks_enabled: True
       smb_notify_on_change_dir_depth: 3
     quota_defaults:
       grace_period: 2
       grace_period_unit: 'weeks'
       default_hard_limit: 2
       default_soft_limit: 1
     state: "present"

 - name: Get File System details by id
   dellemc.powerstore.filesystem:
     array_ip: "{{array_ip}}"
     verifycert: "{{verifycert}}"
     user: "{{user}}"
     password: "{{password}}"
     filesystem_id: "{{result_fs.filesystem_details.id}}"
     state: "present"

 - name: Delete File System by id
   dellemc.powerstore.filesystem:
     array_ip: "{{array_ip}}"
     verifycert: "{{verifycert}}"
     user: "{{user}}"
     password: "{{password}}"
     filesystem_id: "{{result_fs.filesystem_details.id}}"
     state: "absent"


'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
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
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
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
APPLICATION_TYPE = 'Ansible/1.8.0'


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

        mutually_exclusive = [['filesystem_name', 'filesystem_id']]
        required_one_of = [['filesystem_name', 'filesystem_id']]
        required_together = [['filesystem_name', 'nas_server']]

        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mutually_exclusive,
            required_one_of=required_one_of,
            required_together=required_together
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

    def create_filesystem(self, name, nas_server_id, size_total):
        """Create a filesystem."""
        try:
            LOG.info("Attempting to create filesystem name "
                     "%s", name)
            adv_parameters = dict()
            description = self.module.params['description']
            if description:
                adv_parameters['description'] = description

            access_policy = self.module.params['access_policy']
            if access_policy:
                adv_parameters['access_policy'] = \
                    self.get_enum_keys(access_policy)

            locking_policy = self.module.params['locking_policy']
            if locking_policy:
                adv_parameters['locking_policy'] = \
                    self.get_enum_keys(locking_policy)

            folder_rename_policy = self.module.params['folder_rename_policy']
            if folder_rename_policy:
                adv_parameters['folder_rename_policy'] = \
                    self.get_enum_keys(folder_rename_policy)

            if self.protection_policy_id:
                adv_parameters['protection_policy_id'] = \
                    self.protection_policy_id

            smb_properties = self.module.params['smb_properties']
            if smb_properties:
                for key, value in smb_properties.items():
                    if value is not None:
                        adv_parameters[key] = value

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

    def to_modify_filesystem(self, filesystem_details):
        """Determines if any modification required on a specific
        filesystem instance."""

        try:
            LOG.info("Checking if Modify required for filesystem ")
            modify_parameters = dict()

            description = self.module.params['description']
            if (description is not None) and description != \
                    filesystem_details['description']:
                modify_parameters['description'] = description

            if (self.total_size > 0) and \
                    (filesystem_details['size_total'] != self.total_size):
                modify_parameters['size_total'] = self.total_size

            access_policy = self.module.params['access_policy']
            if access_policy and access_policy !=\
                    (filesystem_details['access_policy']).upper():
                modify_parameters['access_policy'] = \
                    self.get_enum_keys(access_policy)

            locking_policy = self.module.params['locking_policy']
            if locking_policy and locking_policy != (
                    filesystem_details['locking_policy']).upper():
                modify_parameters['locking_policy'] = \
                    self.get_enum_keys(locking_policy)

            folder_rename_policy = self.module.params['folder_rename_policy']
            if folder_rename_policy and folder_rename_policy != (
                    filesystem_details['folder_rename_policy']).upper():
                modify_parameters['folder_rename_policy'] = \
                    self.get_enum_keys(folder_rename_policy)

            if self.protection_policy_id and (
                    (filesystem_details['protection_policy'] is None) or
                    (filesystem_details['protection_policy'] is not None) and
                    self.protection_policy_id !=
                    filesystem_details['protection_policy']['id']):
                modify_parameters['protection_policy_id'] = \
                    self.protection_policy_id

            # to handle the remove with "" case
            if self.protection_policy_id == "" and (
                    filesystem_details['protection_policy'] is not None):
                modify_parameters['protection_policy_id'] = \
                    self.protection_policy_id

            # advance smb attributes
            smb_properties = self.module.params['smb_properties']
            if smb_properties:
                for key, value in smb_properties.items():
                    if value is not None and \
                            filesystem_details[key] != value:
                        modify_parameters[key] = value

            # quota defaults
            quota_defaults = self.module.params['quota_defaults']
            if quota_defaults:
                grace_period = quota_defaults['grace_period']
                grace_period_unit = quota_defaults['grace_period_unit']
                default_hard_limit = quota_defaults['default_hard_limit']
                default_soft_limit = quota_defaults['default_soft_limit']
                cap_unit = quota_defaults['cap_unit']
                enable_quota = False
                is_quota_enabled = filesystem_details['is_quota_enabled']

                if grace_period is not None:
                    if not grace_period_unit:
                        grace_period_unit = 'days'
                    param_grace_period = get_graceperiod_seconds(
                        grace_period, grace_period_unit)
                    if param_grace_period !=\
                            filesystem_details['grace_period']:
                        modify_parameters[
                            'grace_period'] = param_grace_period
                        enable_quota = True

                if default_hard_limit < 0 or default_soft_limit < 0:
                    msg = "hard or soft limit cannot be less than '0'"
                    LOG.error(msg)
                    self.module.fail_json(msg=msg)

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

                if enable_quota and (not is_quota_enabled):
                    modify_parameters['is_quota_enabled'] = enable_quota

            LOG.info("Modify Dict %s", str(modify_parameters))
            return modify_parameters

        except Exception as e:
            msg = 'Failed to determine if modify filesystem required with ' \
                  'error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

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
                "ALL_FORBIDDEN": "All_Forbidden"
            }
            return enum_dict[user_input]

        except Exception as e:
            msg = 'Failed to get the enum value for user_ip : %s with ' \
                  'error %s' % (user_input, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

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
        state = self.module.params['state']

        # result is a dictionary to contain end state and filesystem details
        changed = False
        result = dict(
            changed=False,
            filesystem_details=None
        )

        fs_details = None
        fs_id = None
        to_modify = False
        to_modify_dict = None

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

        if nas_server:
            nas_server = self.get_nas_server(nas_server=nas_server)
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
        if fs_details:
            fs_id = fs_details['id']
            to_modify_dict = self.to_modify_filesystem(fs_details)
            if to_modify_dict:
                to_modify = True
        LOG.info("FileSystem Details: %s , To Modify %s", fs_details,
                 to_modify)

        if not fs_details and state == 'present':
            fs_id = self.create_filesystem(
                name=filesystem_name,
                nas_server_id=nas_server,
                size_total=self.total_size)
            fs_details = self.get_filesystem_details(
                filesystem_id=fs_id)
            to_modify_dict = self.to_modify_filesystem(fs_details)
            to_modify = True if to_modify_dict else to_modify
            changed = True

        if to_modify and state == 'present':
            self.modify_filesystem(
                filesystem_id=fs_id,
                modify_parameters=to_modify_dict)
            changed = True

        if state == 'absent' and fs_details:
            self.delete_filesystem(filesystem_id=fs_id)
            fs_details = None
            changed = True

        if state == 'present' and fs_details:
            fs_details = self.display_filesystem_details(
                filesystem_id=fs_id)

        result['changed'] = changed
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
        filesystem_name=dict(required=False, type='str'),
        filesystem_id=dict(required=False, type='str'),
        description=dict(required=False, type='str'),
        nas_server=dict(required=False, type='str'),
        size=dict(required=False, type='int'),
        cap_unit=dict(required=False, type='str', choices=['GB', 'TB']),
        access_policy=dict(required=False, type='str',
                           choices=['NATIVE', 'UNIX', 'WINDOWS']),
        locking_policy=dict(required=False, type='str',
                            choices=['ADVISORY', 'MANDATORY']),
        folder_rename_policy=dict(required=False, type='str',
                                  choices=['ALL_ALLOWED', 'SMB_FORBIDDEN',
                                           'ALL_FORBIDDEN']),
        smb_properties=dict(
            type='dict', options=dict(
                is_smb_sync_writes_enabled=dict(type='bool', required=False),
                is_smb_no_notify_enabled=dict(type='bool', required=False),
                is_smb_op_locks_enabled=dict(type='bool', required=False),
                is_smb_notify_on_access_enabled=dict(type='bool',
                                                     required=False),
                is_smb_notify_on_write_enabled=dict(type='bool',
                                                    required=False),
                smb_notify_on_change_dir_depth=dict(type='int',
                                                    required=False)
            ),
            required=False
        ),
        protection_policy=dict(required=False, type='str'),
        quota_defaults=dict(
            type='dict', options=dict(
                grace_period=dict(type='int', required=False),
                grace_period_unit=dict(type='str', required=False,
                                       choices=['days', 'weeks', 'months']),
                default_hard_limit=dict(type='int', required=False),
                default_soft_limit=dict(type='int', required=False),
                cap_unit=dict(type='str', required=False,
                              choices=['GB', 'TB'])
            ),
            required=False
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
