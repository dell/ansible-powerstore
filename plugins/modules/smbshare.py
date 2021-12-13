#!/usr/bin/python
# Copyright: (c) 2020-2021, DellEMC
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: smbshare
version_added: '1.1.0'
short_description:  Manage SMB shares on a PowerStore storage system.
extends_documentation_fragment:
- dellemc.powerstore.dellemc_powerstore.powerstore
author:
- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>
description:
- Managing SMB Shares on PowerStore storage system includes create, get,
  modify, and delete the SMB shares.
options:
  share_name:
    description:
    - Name of the SMB share.
    - Required during creation of the SMB share.
    - For all other operations either share_name or share_id is required.
    type: str
  share_id:
    description:
    - ID of the SMB share.
    - Should not be specified during creation. ID is auto generated.
    - For all other operations either share_name or share_id is required.
    - If share_id is used then no need to pass nas_server/filesystem/snapshot/
      path.
    type: str
  path:
    description:
    - Local path to the file system/Snapshot or any existing sub-folder of
      the file system/Snapshot that is shared over the network.
    - Path is relative to the base of the NAS server and must start with the
      name of the filesystem.
    - Required for creation of the SMB share.
    type: str
  filesystem:
    description:
    - The ID/Name of the File System.
    - Either filesystem or snapshot is required for creation of the SMB share.
    - If filesystem name is specified, then nas_server is required to
      uniquely identify the filesystem.
    - If filesystem parameter is provided, then snapshot cannot be specified.
    type: str
  snapshot:
    description:
    - The ID/Name of the Snapshot.
    - Either filesystem or snapshot is required for creation of the SMB share.
    - If snapshot name is specified, then nas_server is required to
      uniquely identify the snapshot.
    - If snapshot parameter is provided, then filesystem cannot be specified.
    - SMB share can be created only if access type of snapshot is "protocol".
    type: str
  nas_server:
    description:
    - The ID/Name of the NAS Server.
    - It is not required if share_id is used.
    type: str
  description:
    description:
    - Description for the SMB share.
    - Optional parameter when creating a share.
    - To modify, pass the new value in description field.
    type: str
  is_abe_enabled:
    description:
    - Indicates whether Access-based Enumeration (ABE) for SMB share is
      enabled.
    - During creation, if not mentioned, then the default is False.
    type: bool
  is_branch_cache_enabled:
    description:
    - Indicates whether Branch Cache optimization for SMB share is enabled.
    - During creation, if not mentioned then default is False.
    type: bool
  is_continuous_availability_enabled:
    description:
    - Indicates whether continuous availability for SMB 3.0 is enabled.
    - During creation, if not mentioned, then the default is False.
    type: bool
  is_encryption_enabled:
    description:
    - Indicates whether encryption for SMB 3.0 is enabled at the shared folder
      level.
    - During creation, if not mentioned then default is False.
    type: bool
  offline_availability:
    description:
    - Defines valid states of Offline Availability.
    - MANUAL- Only specified files will be available offline.
    - DOCUMENTS- All files that users open will be available offline.
    - PROGRAMS- Program will preferably run from the offline cache even when
      connected to the network. All files that users open will be available
      offline.
    - NONE- Prevents clients from storing documents and programs in offline
      cache.
    type: str
    choices: ["MANUAL","DOCUMENTS","PROGRAMS","NONE"]
  umask:
    description:
    - The default UNIX umask for new files created on the SMB Share.
    - During creation, if not mentioned, then the default is "022".
    - For all other operations, the default is None.
    type: str
  state:
    description:
    - Define whether the SMB share should exist or not.
    - present  indicates that the share should exist on the system.
    - absent  indicates that the share should not exist on the system.
    type: str
    required: true
    choices: ['absent', 'present']

notes:
- When the ID of the filesystem/snapshot is passed then nas_server is not
  required. If passed, then the filesystem/snapshot should exist for the
  nas_server, else the task will fail.
- Multiple SMB shares can be created for the same local path.
'''

EXAMPLES = r'''

- name: Create SMB share for a filesystem
  smbshare:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    share_name: "sample_smb_share"
    filesystem: "sample_fs"
    nas_server: "{{nas_server_id}}"
    path: "{{path}}"
    description: "Sample SMB share created"
    is_abe_enabled: True
    is_branch_cache_enabled: True
    offline_availability: "DOCUMENTS"
    is_continuous_availability_enabled: True
    is_encryption_enabled: True
    state: "present"

- name: Modify Attributes of SMB share for a filesystem
  smbshare:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    share_name: "sample_smb_share"
    nas_server: "sample_nas_server"
    description: "Sample SMB share attributes updated"
    is_abe_enabled: False
    is_branch_cache_enabled: False
    offline_availability: "MANUAL"
    is_continuous_availability_enabled: False
    is_encryption_enabled: False
    umask: "022"
    state: "present"

- name: Create SMB share for a snapshot
  smbshare:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    share_name: "sample_snap_smb_share"
    snapshot: "sample_snapshot"
    nas_server: "{{nas_server_id}}"
    path: "{{path}}"
    description: "Sample SMB share created for snapshot"
    is_abe_enabled: True
    is_branch_cache_enabled: True
    is_continuous_availability_enabled: True
    state: "present"

- name: Modify Attributes of SMB share for a snapshot
  smbshare:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    share_name: "sample_snap_smb_share"
    nas_server: "sample_nas_server"
    description: "Sample SMB share attributes updated for snapshot"
    is_abe_enabled: False
    is_branch_cache_enabled: False
    offline_availability: "MANUAL"
    is_continuous_availability_enabled: False
    umask: "022"
    state: "present"

- name: Get details of SMB share
  smbshare:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    share_id: "{{smb_share_id}}"
    state: "present"

- name: Delete SMB share
  smbshare:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    share_id: "{{smb_share_id}}"
    state: "absent"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed
    returned: always
    type: bool
    sample: True

smb_share_details:
    description: The SMB share details.
    type: complex
    returned: When share exists.
    contains:
        id:
            description: The ID of the SMB share.
            type: str
            sample: "5efc4432-cd57-5dd0-2018-42079d64ae37"
        name:
            description: Name of the SMB share.
            type: str
            sample: "sample_smb_share"
        file_system:
            description: Includes ID and Name of filesystem and nas server for
                         which smb share exists.
            type: complex
            contains:
                filesystem_type:
                    description: Type of filesystem.
                    type: str
                    sample: "Primary"
                id:
                    description: ID of filesystem.
                    type: str
                    sample: "5f73f516-e67b-b179-8901-72114981c1f3"
                name:
                    description: Name of filesystem.
                    type: str
                    sample: "sample_filesystem"
                nas_server:
                    description: nas_server of filesystem.
                    type: dict
        description:
            description: Additional information about the share.
            type: str
            sample: "This share is created for demo purpose only."
        is_ABE_enabled:
            description: Whether Access Based enumeration is enforced or not
            type: bool
            sample: false
        is_branch_cache_enabled:
            description: Whether branch cache is enabled or not.
            type: bool
            sample: false
        is_continuous_availability_enabled:
            description: Whether the share will be available continuously or
                         not.
            type: bool
            sample: false
        is_encryption_enabled:
            description: Whether encryption is enabled or not.
            type: bool
            sample: false
'''
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import dellemc_ansible_powerstore_utils as utils
import logging

LOG = utils.get_logger('smbshare', log_devel=logging.INFO)

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.4.0'


class PowerStoreSMBShare(object):
    """Class with SMB Share operations"""

    def __init__(self):
        """ Define all parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_smb_share_parameters())

        # initialize the ansible module
        mut_ex_args = [['share_name', 'share_id'],
                       ['filesystem', 'snapshot'],
                       ['share_id', 'nas_server'],
                       ['share_id', 'filesystem'],
                       ['share_id', 'path'],
                       ['share_id', 'snapshot']]
        required_one_of = [['share_id', 'share_name']]

        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mut_ex_args,
            required_one_of=required_one_of
        )

        msg = 'HAS_PY4PS = {0} , IMPORT_ERROR = {1}'.format(HAS_PY4PS,
                                                            IMPORT_ERROR)
        LOG.info(msg)

        if not HAS_PY4PS:
            self.module.fail_json(msg=IMPORT_ERROR)
        msg = 'IS_SUPPORTED_PY4PS_VERSION = {0} , VERSION_ERROR = {1}' \
            .format(IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR)
        LOG.info(msg)

        if not IS_SUPPORTED_PY4PS_VERSION:
            self.module.fail_json(msg=VERSION_ERROR)

        # result is a dictionary that contains changed status and
        # SMB share details
        self.result = {"changed": False, "smb_share_details": {}}

        self.conn = utils.get_powerstore_connection(
            self.module.params, application_type=APPLICATION_TYPE)

        self.provisioning = self.conn.provisioning
        msg = 'Got Py4Ps instance for provisioning on' \
              ' PowerStore {0}'.format(self.conn)
        LOG.info(msg)

    def get_smb_share(self, share_id, share_name,
                      smb_parent, nas_server, path):
        """Get SMB share details"""
        err_msg = "Entered filesystem/snapshot/nas_server/path do not match" \
                  " with the corresponding parameters in smb share details." \
                  " Please enter valid parameters."
        try:
            if share_id:
                return self.provisioning.get_smb_share(share_id)
            else:
                share_details = self.provisioning.get_smb_share_by_name(
                    share_name)
                # Matching NAS Server, Filesystem, Snapshot and Path is
                # required when share_name is passed.
                share_obj = match_smb_share(share_details, smb_parent,
                                            nas_server, path)
                if share_details and not share_obj:
                    self.module.fail_json(msg=err_msg)
                return share_obj

        except Exception as e:
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                return None
            msg = 'Get details for SMB Share with id = {0} and name = {1} ' \
                  'failed with error: {2}'.format(share_id,
                                                  share_name, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def create_smb_share(self, share_name, smb_parent_id, path, description,
                         is_branch_cache_enabled, offline_availability,
                         is_abe_enabled, continuous_available,
                         is_encryption_enabled, umask):
        """Create PowerStore SMB share"""

        try:
            msg = "Creating SMB Share with name {0} ".format(share_name)
            LOG.info(msg)
            if not path:
                self.module.fail_json(
                    msg="Path is required for creation of a SMB share."
                        " Please provide path")
            self.provisioning.create_smb_share(
                name=share_name,
                path=path,
                file_system_id=smb_parent_id,
                description=description,
                is_ABE_enabled=is_abe_enabled,
                is_branch_cache_enabled=is_branch_cache_enabled,
                is_continuous_availability_enabled=continuous_available,
                is_encryption_enabled=is_encryption_enabled,
                offline_availability=offline_availability,
                umask=umask
            )
            return True
        except Exception as e:
            msg = 'Create SMB share {0} failed with error {1}'.format(
                share_name, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def delete_smb_share(self, smb_share_details):

        share_id = smb_share_details['id']
        share_name = smb_share_details['name']
        try:
            self.provisioning.delete_smb_share(share_id)
            return True
        except Exception as e:
            msg = 'Deletion of SMB share with name = {0}, id = {1} failed' \
                  ' with error: {2}'.format(share_name, share_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_nas_server_id(self, nas_server):
        """
        Get the NAS Server ID
        :param nas_server: Name/ID of the NAS Server
        :return: ID of the NAS Server
        """
        nas_server_id = nas_server
        if nas_server and utils.name_or_id(nas_server) == "NAME":
            try:
                nas_server_id = self.provisioning.get_nas_server_by_name(
                    nas_server)[0]['id']
            except Exception as e:
                error_msg = "Failed to get details of NAS server {0} with" \
                            " error: {1}".format(nas_server, str(e))
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg, **utils.failure_codes(e))
        return nas_server_id

    def get_filesystem_id(self, smb_parent, snapshot, nas_server):
        """
        Get the filesystem/snapshot ID.
        :param smb_parent: Name/ID of the filesystem/snapshot.
        :param snapshot: Name/ID of the Snapshot.
        :param nas_server: Name/ID of the NAS Server
        :return: ID of the filesystem/snapshot .
        """
        file_system_id = smb_parent
        nas_server_id = self.get_nas_server_id(nas_server)
        fs_details = None
        if smb_parent and utils.name_or_id(smb_parent) == "NAME":
            try:
                fs_details = self.provisioning.get_filesystem_by_name(
                    smb_parent, nas_server_id)
                if not fs_details:
                    self.module.fail_json(
                        msg="No File System/Snapshot found with "
                            "Name {0}".format(smb_parent))
                file_system_id = fs_details[0]['id']
            except Exception as e:
                error_msg = "Failed to get details of File System/Snapshot" \
                            " {0} with error: {1}".format(smb_parent, str(e))
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

        if snapshot and fs_details[0]['filesystem_type'] == 'Primary':
            self.module.fail_json(msg="Please enter a valid snapshot,"
                                      " filesystem passed")

        if not snapshot and fs_details[0]['filesystem_type'] == 'Snapshot':
            self.module.fail_json(msg="Please enter a valid Filesystem,"
                                      " snapshot passed")
        return file_system_id

    def to_update_smb_share(self, share_details):

        parameters_list = ['is_ABE_enabled', 'is_branch_cache_enabled',
                           'is_continuous_availability_enabled',
                           'is_encryption_enabled', 'umask',
                           'offline_availability']
        update_flag = False
        # Handled separately because if description is passed ""
        # then it gets updated as None. So added condition to address
        # Idempotency case where description is None on the SMB Share and
        # entered value is "".
        if self.module.params['description'] is not None:
            if self.module.params['description'] == "" and \
                    share_details['description'] is not None:
                update_flag = True
            if self.module.params['description'] and \
                    share_details['description'] != \
                    self.module.params['description']:
                update_flag = True

        for parameter in parameters_list:
            if self.module.params[parameter] is not None \
                    and share_details[parameter] != \
                    self.module.params[parameter]:
                update_flag = True
        return update_flag

    def update_smb_share(self, share_id, share_name, description, umask,
                         is_branch_cache_enabled, offline_availability,
                         is_abe_enabled, continuous_available,
                         is_encryption_enabled):
        """Update PowerStore SMB share"""
        try:
            self.provisioning.update_smb_share(
                id=share_id,
                description=description,
                is_ABE_enabled=is_abe_enabled,
                is_branch_cache_enabled=is_branch_cache_enabled,
                is_continuous_availability_enabled=continuous_available,
                is_encryption_enabled=is_encryption_enabled,
                offline_availability=offline_availability,
                umask=umask
            )
            return True
        except Exception as e:
            msg = 'Update SMB share with name = {0}, id = {1} failed' \
                  ' with error: {2}'.format(share_name, share_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def validate_umask(self, umask):
        err_msg = "umask should be a 3 digit octal number. " \
                  "Please enter a valid umask string."
        if len(umask) != 3:
            self.module.fail_json(msg=err_msg)

        try:
            umask = int(umask)
        except ValueError as val_err:
            self.module.fail_json(
                msg="Please enter a valid umask string. "
                    "Failed with error: {0}".format(str(val_err)))

        while umask:
            if (umask % 10) > 7:
                self.module.fail_json(msg=err_msg)
            else:
                umask = int(umask / 10)

    def perform_module_operation(self):
        """
        Perform different actions on SMB share based on user parameters
        chosen in playbook
        """
        state = self.module.params['state']
        share_id = self.module.params['share_id']
        share_name = self.module.params['share_name']
        path = self.module.params['path']
        filesystem = self.module.params['filesystem']
        snapshot = self.module.params['snapshot']
        nas_server = self.module.params['nas_server']
        description = self.module.params['description']
        is_branch_cache_enabled = \
            self.module.params['is_branch_cache_enabled']
        is_continuous_availability_enabled = \
            self.module.params['is_continuous_availability_enabled']
        is_encryption_enabled = self.module.params['is_encryption_enabled']

        umask = self.module.params['umask']
        if umask:
            self.validate_umask(umask)

        is_abe_enabled = self.module.params['is_ABE_enabled'] = \
            self.module.params['is_abe_enabled']
        del self.module.params['is_abe_enabled']

        offline_availability = self.module.params['offline_availability']
        if offline_availability:
            offline_availability = \
                self.module.params['offline_availability'] = \
                offline_availability.title()

        changed = False

        smb_parent = filesystem if filesystem else snapshot

        if share_name:
            if smb_parent and not (utils.name_or_id(smb_parent) == "ID"
                                   or nas_server):
                self.module.fail_json(
                    msg="share_name, filesystem/snapshot name given. Please"
                        " enter nas_server to uniquely identify SMB Share")
            if not smb_parent and not nas_server:
                self.module.fail_json(
                    msg="share_name provided,"
                        " filesystem/snapshot/nas_server also required.")

        '''
        Get the Details of the SMB Share
        '''
        smb_share_details = self.get_smb_share(share_id, share_name,
                                               smb_parent, nas_server, path)

        '''
        Creation of SMB Share
        '''
        if state == 'present' and not smb_share_details:
            LOG.info("Creating a SMB share")
            if share_id:
                err_msg = "SMB share with share_id {0} not found" \
                    .format(share_id)
                self.module.fail_json(msg=err_msg)

            if share_name and not smb_parent:
                self.module.fail_json(msg="Creation Failed,"
                                          " filesystem/snapshot required.")

            # If Filesystem/Snapshot Name is passed
            # and NAS Server is not passed.
            smb_parent_id = smb_parent
            if utils.name_or_id(smb_parent) == "NAME":
                if not nas_server:
                    self.module.fail_json(msg="File System/Snapshot name is "
                                              "passed, nas_server required "
                                              "for creation of SMB share.")
                smb_parent_id = self.get_filesystem_id(smb_parent, snapshot,
                                                       nas_server)

            changed = self.create_smb_share(
                share_name, smb_parent_id, path, description,
                is_branch_cache_enabled, offline_availability,
                is_abe_enabled, is_continuous_availability_enabled,
                is_encryption_enabled, umask)

        '''
        Update the SMB share details
        '''
        if state == 'present' and smb_share_details:
            share_id = share_id if share_id else smb_share_details['id']
            update_flag = self.to_update_smb_share(smb_share_details)
            if update_flag:
                LOG.info("Updating attributes of SMB share")
                changed = self.update_smb_share(
                    share_id, share_name, description, umask,
                    is_branch_cache_enabled, offline_availability,
                    is_abe_enabled, is_continuous_availability_enabled,
                    is_encryption_enabled)

        '''
        Delete the SMB share details
        '''
        if state == 'absent' and smb_share_details:
            LOG.info("Deleting SMB share")
            changed = self.delete_smb_share(smb_share_details)

        '''
        Update the changed state and SMB share details
        '''

        self.result["changed"] = changed
        if state == 'present':
            self.result["smb_share_details"] = \
                self.get_smb_share(share_id, share_name,
                                   smb_parent, nas_server, path)
        self.module.exit_json(**self.result)


def match_smb_share(share_details, smb_parent, nas_server, path):
    """

    :param share_details: SMB share details.
    :param smb_parent: Entered Filesystem/Snapshot for SMB share.
    :param nas_server: Entered Name/ID of the NAS Server.
    :param path: Entered local Path of the SMB share.
    :return:
    """
    if not share_details:
        return share_details

    for share in share_details:
        match_flag = True
        if (nas_server and not is_match_nas(nas_server, share)) or\
                (smb_parent and not is_match_smb_parent(smb_parent, share)) or\
                (path and not is_match_path(path, share)):
            match_flag = False
        if match_flag:
            return share
    return False


def is_match_nas(nas_server, smb_share_details):
    """
    Whether the entered nas_server and nas_server in the
    smb_share_details is same or not
    :param nas_server: ID/Name of NAS Server
    :param smb_share_details: The details of the SMB share.
    """
    nas_id_from_details = \
        smb_share_details['file_system']['nas_server']['id']
    nas_name_from_details = \
        smb_share_details['file_system']['nas_server']['name']

    if smb_share_details and nas_server:
        if (utils.name_or_id(nas_server) == "ID" and
                nas_id_from_details != nas_server):
            return False
        if utils.name_or_id(nas_server) == "NAME" and \
                nas_name_from_details != nas_server:
            return False
    return True


def is_match_path(input_path, smb_share_details):
    """
    Whether the entered path and path in the
    smb_share_details is same or not.
    :param input_path: The path parameter entered by user.
    :param smb_share_details: Details of the SMB share.
    """
    input_path = input_path[:-1] if input_path[-1] == "/" else input_path
    if smb_share_details['path'] != input_path:
        return False
    return True


def is_match_smb_parent(smb_parent, smb_share_details):
    """
    Whether the entered Filesystem/Snapshot and Filesystem/Snapshot in
    the smb_share_details is same or not.
    :param smb_parent: Filesystem/Snapshot for which smb share exists.
    :param smb_share_details: Details of the SMB share.
    """

    fs_id_from_details = smb_share_details['file_system']['id']
    fs_name_from_details = smb_share_details['file_system']['name']

    if smb_share_details and smb_parent:
        if (utils.name_or_id(smb_parent) == 'ID' and
                fs_id_from_details != smb_parent):
            return False
        if utils.name_or_id(smb_parent) == 'NAME' and \
                fs_name_from_details != smb_parent:
            return False
    return True


def get_powerstore_smb_share_parameters():
    """
    This method provides parameters required for the ansible smb share
    modules on PowerStore
    """
    return dict(
        path=dict(), share_name=dict(), share_id=dict(),
        filesystem=dict(), snapshot=dict(), nas_server=dict(),
        umask=dict(), description=dict(),
        offline_availability=dict(
            choices=["MANUAL", "DOCUMENTS", "PROGRAMS", "NONE"]),
        is_abe_enabled=dict(type='bool'),
        is_branch_cache_enabled=dict(type='bool'),
        is_continuous_availability_enabled=dict(type='bool'),
        is_encryption_enabled=dict(type='bool'),
        state=dict(required=True, choices=['present', 'absent'],
                   type='str'),
    )


def main():
    """ Create PowerStore SMB share object and perform action on it
        based on user input from playbook"""
    obj = PowerStoreSMBShare()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
