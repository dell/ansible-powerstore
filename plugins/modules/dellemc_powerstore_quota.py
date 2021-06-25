#!/usr/bin/python
# Copyright: (c) 2020-2021, DellEMC
""" Ansible module for managing Tree Quotas and User Quotas on PowerStore"""
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: dellemc_powerstore_quota

version_added: '1.1.0'

short_description: Manage Tree Quotas and User Quotas on PowerStore.

description:
- Managing  Quotas on Powerstore storage system includes getting details,
  modifying, creating and deleting  Quotas.

extends_documentation_fragment:
  - dellemc.powerstore.dellemc_powerstore.powerstore

author:
- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

options:
  path:
    description:
    - The path on which the quota will be imposed.
    - Path is relative to the root of the filesystem.
    - For user quota, if path is not specified, quota will be created at the
      root of the filesystem.
    type: str
  quota_type:
    description:
    - The type of quota which will be imposed.
    type: str
    choices: ['user', 'tree']
  quota_id:
    description:
    - Id of the user/tree quota.
    - If quota_id is mentioned, then path/nas_server/file_system/quota_type is
      not required.
    type: str
  filesystem:
    description:
    - The ID/Name of the filesystem for which the Tree/User Quota  will be
      created.
    - If filesystem name is specified, then nas_server is required to uniquely
      identify the filesystem.
    type: str
  nas_server:
    description:
    - The NAS server. This could be the name or ID of the NAS server.
    type: str
  description:
    description:
    - Additional information that can be mentioned for a Tree Quota.
    - Description parameter can only be used when quota_type is 'tree'
    type: str
  unix_name:
    description:
    - The name of the unix user account for which
      quota operations will be performed.
    - Any one among uid/unix_name/windows_name/windows_sid is required when
      quota_type is 'user'.
    type: str
  windows_name:
    description:
    - The name of the Windows User for which quota operations will be
      performed.
    - The name should be mentioned along with Domain Name as
      'DOMAIN_NAME\user_name' or as "DOMAIN_NAME\\user_name".
    - Any one among uid/unix_name/windows_name/windows_sid is required when
      quota_type is 'user'.
    type: str
  uid:
    description:
    - The ID of the unix user account for which quota operations will be
      performed.
    - Any one among uid/unix_name/windows_name/windows_sid is required when
      quota_type is 'user'.
    type: int
  windows_sid:
    description:
    - The SID of the Windows User account for which quota operations will be
      performed.
    - Any one among uid/unix_name/windows_name/windows_sid is required when
      quota_type is 'user'.
    type: str
  quota:
    description:
    - Specifies Quota parameters.
    type: dict
    suboptions:
      soft_limit:
        description:
        - Soft limit of the User/Tree quota.
        - No Soft limit when set to 0.
        type: int
      hard_limit:
        description:
        - Hard limit of the user quota.
        - No hard limit when set to 0.
        type: int
      cap_unit:
        description:
        - Unit of storage for the hard and soft limits.
        - This parameter is required if limit is specified.
        type: str
        default: 'GB'
        choices: ['GB', 'TB']
  state:
    description:
    - Define whether the Quota should exist or not.
    - present  indicates that the Quota should exist on the system.
    - absent  indicates that the Quota should not exist on the system.
    type: str
    required: true
    choices: ['absent', 'present']

notes:
- Tree quota can not be created at the root of the filesystem.
- When the ID of the filesystem is passed then nas_server is not required.
  If passed, then filesystem should exist for the nas_server, else the task
  will fail.
- If a primary directory of the current directory or a subordinate directory of the
  path is having a Tree Quota configured, then the quota for that path can't be
  created. Hierarchical tree quotas are not allowed.
- When the first quota is created for a directory/user in a filesystem then the
  quotas will be enabled for that filesystem automatically.
- If a user quota is to be created on a tree quota, then the user quotas will be
  enabled automatically in a tree quota.
- Delete User Quota operation is not supported.

'''
EXAMPLES = r'''

    - name: Create a Quota for a User using unix name
      dellemc_powerstore_quota:
        array_ip: "{{array_ip}}"
        verifycert: "{{verify_cert}}"
        user: "{{user}}"
        password: "{{password}}"
        quota_type: "user"
        unix_name: "{{unix_name}}"
        filesystem: "sample_fs"
        nas_server: "{{nas_server_id}}"
        quota:
          soft_limit: 5
          hard_limit: 10
          cap_unit: "TB"
        state: "present"

    - name: Create a Tree Quota
      dellemc_powerstore_quota:
        array_ip: "{{array_ip}}"
        verifycert: "{{verify_cert}}"
        user: "{{user}}"
        password: "{{password}}"
        quota_type: "tree"
        path: "/home"
        filesystem: "sample_fs"
        nas_server: "sample_nas_server"
        quota:
          soft_limit: 5
          hard_limit: 10
          cap_unit: "TB"
        state: "present"

    - name: Modify attributes for Tree Quota
      dellemc_powerstore_quota:
        array_ip: "{{array_ip}}"
        verifycert: "{{verify_cert}}"
        user: "{{user}}"
        password: "{{password}}"
        quota_id: "{{quota_id}}"
        quota:
          soft_limit: 10
          hard_limit: 15
          cap_unit: "TB"
        state: "present"

    - name: Get details of User Quota
      dellemc_powerstore_quota:
        array_ip: "{{array_ip}}"
        verifycert: "{{verify_cert}}"
        user: "{{user}}"
        password: "{{password}}"
        quota_type: "user"
        uid: 100
        path: "/home"
        filesystem: "{{filesystem_id}}"
        state: "present"

    - name: Get details of Tree Quota
      dellemc_powerstore_quota:
        array_ip: "{{array_ip}}"
        verifycert: "{{verify_cert}}"
        user: "{{user}}"
        password: "{{password}}"
        quota_id: "{{quota_id}}"
        state: "present"

    - name: Delete a Tree Quota
      dellemc_powerstore_quota:
        array_ip: "{{array_ip}}"
        verifycert: "{{verify_cert}}"
        user: "{{user}}"
        password: "{{password}}"
        quota_type: "tree"
        path: "/home"
        filesystem: "sample_fs"
        nas_server: "sample_nas_server"
        state: "absent"

'''
RETURN = r'''
changed:
    description: Whether or not the resource has changed
    returned: always
    type: bool
    sample: True

quota_details:
    description: The quota details.
    type: complex
    returned: When Quota exists.
    contains:
        id:
            description: The ID of the Quota.
            type: str
            sample: "2nQKAAEAAAAAAAAAAAAAQIMCAAAAAAAA"
        file_system:
            description: Includes ID and Name of filesystem and nas server for which
                smb share exists.
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
        hard_limit(cap_unit):
            description: Value of the Hard Limit imposed on the quota.
            type: int
            sample: "4.0"
        soft_limit(cap_unit):
            description: Value of the Soft Limit imposed on the quota.
            type: int
            sample: "2.0"
        remaining_grace_period:
            description: The time period remaining after which the grace period will
                expire.
            type: int
            sample: 86400
        description:
            description:
                - Additional information about the tree quota.
                - Only applicable for Tree Quotas.
            type: str
            sample: "Sample Tree quota's description"
        uid:
            description:
                - The ID of the unix host for which user quota exists.
                - Only applicable for user quotas.
            type: int
        unix_name:
            description:
                - The Name of the unix host for which user quota exists.
                - Only applicable for user quotas.
            type: str
        windows_name:
            description:
                - The Name of the Windows host for which user quota exists.
                - Only applicable for user quotas.
            type: str
        windows_sid:
            description:
                - The SID of the windows host for which user quota exists.
                - Only applicable for user quotas.
            type: str
        tree_quota_id:
            description:
                - ID of the Tree Quota on which the specific User Quota exists.
                - Only applicable for user quotas.
            type: str
        tree_quota_for_user_quota:
            description:
                - Additional Information of Tree Quota limits on which user
                  quota exists.
                - Only applicable for User Quotas
            type: complex
            contains:
                description:
                    description: Description of Tree Quota for user quota.
                    type: str
                    sample: "Primary"
                hard_limit(cap_unit):
                    description: Value of the Hard Limit imposed on the quota.
                    type: int
                    sample: "2.0"
                path:
                    description: The path on which the quota will be imposed.
                    type: str
                    sample: "/sample_path"
        size_used:
            description: Size currently consumed by Tree/User on the filesystem.
            type: int
        state:
            description:
                - State of the user quota or tree quota record period.
                - OK means No quota limits are exceeded.
                - Soft_Exceeded means Soft limit is exceeded, and grace period
                  is not expired.
                - Soft_Exceeded_And_Expired means Soft limit is exceeded, and
                  grace period is expired.
                - Hard_Reached means Hard limit is reached.
            type: str
            sample: "Ok"
        state_l10n:
            description: Localized message string corresponding to state.
            type: str
            sample: "Ok"
'''

import logging
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import dellemc_ansible_powerstore_utils as utils
from ansible.module_utils.basic import AnsibleModule

LOG = utils.get_logger('dellemc_powerstore_quota', log_devel=logging.INFO)

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.2.0'


class PowerStoreQuota(object):
    """Class with Quota operations"""

    def __init__(self):
        """ Define all parameters required by this module"""

        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_quota_parameters())

        # initialize the ansible module
        mut_ex_args = [
            ['quota_id', 'quota_type'],
            ['quota_id', 'nas_server'],
            ['quota_id', 'filesystem'],
            ['quota_id', 'path'],
            ['uid', 'windows_name', 'windows_sid', 'unix_name',
             'quota_id']
        ]

        required_one_of = [['quota_id', 'quota_type']]
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
        # Quota details
        self.result = {"changed": False, "quota_details": {}}

        self.conn = utils.get_powerstore_connection(
            self.module.params, application_type=APPLICATION_TYPE)
        self.provisioning = self.conn.provisioning
        msg = 'Got Py4Ps instance for provisioning on' \
              ' PowerStore {0}'.format(self.conn)
        LOG.info(msg)

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
                return nas_server_id
            except Exception as e:
                error_msg = "Failed to get details of NAS server {0} with" \
                            " error: {1}".format(nas_server, str(e))
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)
        else:
            try:
                nas_details = self.provisioning.get_nas_server_details(
                    nas_server_id)
                return nas_details['id']
            except Exception as e:
                error_msg = "Failed to get details of NAS Server" \
                            " {0} with error: {1}".format(nas_server_id,
                                                          str(e))
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)

    def get_filesystem_id(self, filesystem, nas_server):
        """
        Get the filesystem ID.
        :param filesystem: Name/ID of the filesystem.
        :param nas_server: Name/ID of the NAS Server
        :return: ID of the filesystem.
        """
        file_system_id = filesystem
        if filesystem and utils.name_or_id(filesystem) == "NAME":
            if not nas_server:
                self.module.fail_json(
                    msg="NAS Server Name/ID is required"
                        " along with File System Name."
                        " Please enter NAS Server Name/ID")
            nas_server_id = self.get_nas_server_id(nas_server)
            try:
                fs_details = self.provisioning.get_filesystem_by_name(
                    filesystem, nas_server_id)
                if not fs_details:
                    self.module.fail_json(
                        msg="No File System found with "
                            "Name {0}".format(filesystem))
                return fs_details[0]['id']
            except Exception as e:
                error_msg = "Failed to get details of File System" \
                            " {0} with error: {1}".format(filesystem, str(e))
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)
        else:
            try:
                fs_details = self.provisioning.get_filesystem_details(
                    file_system_id)
                return fs_details['id']
            except Exception as e:
                error_msg = "Failed to get details of File System" \
                            " {0} with error: {1}".format(file_system_id,
                                                          str(e))
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)

    def get_tree_quota_details(self, quota_id=None, path=None,
                               filesystem_id=None):
        """
        Get the details of Tree Quota
        :param quota_id: ID of the tree quota
        :param path: Path for which the quota exists.
        :param filesystem_id: ID of the filesystem.
        :return:if exists then Tree quota details, else None
        """
        try:
            if quota_id:
                return self.provisioning.get_tree_quota(quota_id)

            # If filesystem or path is not passed then error is
            # thrown as both are required to fetch a unique tree quota.
            if not path or not filesystem_id:
                self.module.fail_json(
                    msg="Get details of Tree Quota failed. Please enter "
                        "valid filesystem and Path.")
            # Get Tree Quota details using filesystem ID, Path.
            tree_quota_details = self.provisioning.get_tree_quota(
                tree_quota_id=None, path=path,
                file_system_id=filesystem_id)
            if tree_quota_details:
                return tree_quota_details[0]
            return None

        except Exception as e:
            msg = 'Get details for Tree Quota with id = {0}, path = {1}' \
                  'and filesystem = {2} failed with error: {3}' \
                  ''.format(quota_id, path, self.module.params['filesystem'],
                            str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_user_quota_details(self, quota_id, path=None,
                               filesystem_id=None, uid=None, unix_name=None,
                               win_name=None, win_sid=None):
        """
        Get the details of User Quota
        :param quota_id: Id of the quota
        :param path: Path for which the quota exists.
        :param filesystem_id: ID of the filesystem.
        :param uid: ID of the Unix Host
        :param unix_name: Name of the Unix host.
        :param win_name: Name of the windows host.
        :param win_sid: SID of the windows host.
        :return: if exists then User quota details, else None
        """
        try:
            # Get User Quota details using Quota ID
            if quota_id:
                return self.provisioning.get_user_quota(quota_id)
            tree_quota_id = None
            if path and filesystem_id:
                tree_quota_id = self.get_tree_quota_id(path, filesystem_id)
            uid = str(uid) if uid is not None else None
            query_params_dict = create_params_dict(
                uid=uid, unix_name=unix_name, windows_sid=win_sid,
                windows_name=win_name, tree_quota_id=tree_quota_id,
                file_system_id=filesystem_id)
            # If filesystem or User is not passed then error is
            # thrown as both are required to fetch a unique user quota.
            if not filesystem_id or not (uid or win_sid or win_name or
                                         unix_name):
                self.module.fail_json(
                    msg="UID/Windows SID/Windows Name/Unix Name and File "
                        "System both are required to get unique User Quota")
            # Get User Quota details using filesystem,
            # Tree Quota ID and User.
            user_quota_details = self.provisioning.get_user_quota(
                user_quota_id=None,
                query_params=query_params_dict)

            # When path is not entered and filesystem is entered then the GET
            # SDK Call returns list of quotas which exists for filesystem.
            # This list of user quotas will also include user quota on a Tree
            # Quota for a filesystem.
            # So below if condition returns user quota for a filesystem.
            if user_quota_details and filesystem_id and not path:
                for user_quota in user_quota_details:
                    if user_quota['tree_quota_id'] is None:
                        return user_quota
            # When path and file System both are entered then query param
            # will fetch unique user quota for entered path.
            if user_quota_details and filesystem_id and path:
                return user_quota_details[0]

            return None

        except Exception as e:
            user_name = None
            user_type = None
            if uid is not None:
                user_name = str(uid)
                user_type = 'uid'
            elif unix_name:
                user_name = unix_name
                user_type = "unix_name"
            elif win_name:
                user_name = win_name
                user_type = "windows_name"
            elif win_sid:
                user_name = win_sid
                user_type = "windows_sid"

            error_message = "Get quota details for user with {0}: {1} " \
                            "failed with {2}".format(user_type, user_name,
                                                     str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(error_message)
                return None
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def get_tree_quota_id(self, path, filesystem_id):
        """
        Get the ID of the Tree Quota
        :param path: Path for which the quota exists.
        :param filesystem_id: ID of the filesystem.
        :return: Id of the Tree Quota
        """
        try:
            tree_quota_details = self.get_tree_quota_details(
                None, path, filesystem_id)
            if not tree_quota_details:
                err_msg = "No Tree Quota with path = {0} in " \
                          "filesystem = {1} exists, cannot get " \
                          "details of user quota on a tree quota." \
                          "".format(path, self.module.params['filesystem'])
                LOG.error(err_msg)
                self.module.fail_json(msg=err_msg)

            return tree_quota_details['id']
        except Exception as e:
            msg = "Get Tree Quota ID for path = {0} and filesystem = {1}" \
                  " failed with error: {2}" \
                  "".format(path, self.module.params['filesystem'], str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_quota_details(self, quota_id, quota_type=None, path=None,
                          filesystem_id=None, uid=None, unix_name=None,
                          win_name=None, win_sid=None):
        """
        Get the details of the Quota
        :param quota_id: ID of the quota
        :param quota_type: Type of the Quota.
        :param path: Path for which the quota exists.
        :param filesystem_id: ID of the filesystem.
        :param uid: ID of the Unix Host
        :param unix_name: Name of the Unix host.
        :param win_name: Name of the windows host.
        :param win_sid: SID of the windows host.
        :return: If exists then returns the details and type of the quota
        else None
        """
        if quota_id or quota_type == 'tree':
            tree_quota_details = self.get_tree_quota_details(
                quota_id, path, filesystem_id)
            if tree_quota_details:
                return tree_quota_details, 'tree'
        if quota_id or quota_type == "user":
            user_quota_details = self.get_user_quota_details(
                quota_id, path, filesystem_id, uid, unix_name, win_name,
                win_sid)
            if user_quota_details:
                return user_quota_details, 'user'
        return None, None

    def convert_quota_thresholds(self, quota):
        """
        Convert the threshold limits to appropriate units.
        :param quota: Threshold limits dictionary containing all limits.
        :return: Converted Threshold limits dictionary.
        """
        limit_params = ['soft_limit', 'hard_limit']
        for limit in quota.keys():
            if limit in limit_params:
                if quota[limit] is not None and quota[limit] < 0:
                    self.module.fail_json(
                        msg="Invalid %s provided, must be greater"
                            " than or equal to 0" % limit)
                if quota[limit] is not None and quota[limit] > 0:
                    quota[limit] = utils.get_size_bytes(
                        quota[limit], quota['cap_unit'])
        return quota

    def enable_quotas(self, filesystem):
        """
        Enable quotas on filesystem
        :param filesystem: Id of the filesystem
        """
        filesystem_details = self.provisioning.get_filesystem_details(
            filesystem)
        try:
            if not filesystem_details['is_quota_enabled']:
                self.provisioning.modify_filesystem(
                    filesystem, {'is_quota_enabled': True})
        except Exception as e:
            error_message = "Unable to enable quota, " \
                            "failed with error: {0}".format(str(e))
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def enforce_user_quota_on_tree_quota(self, path, filesystem):
        """
        Enforce user quotas on Tree Quota
        :param path: The path of the tree relative to the root of the
         filesystem.
        :param filesystem: ID of the filesystem
        """
        try:
            tree_quota_details = self.get_tree_quota_details(
                None, path, filesystem)
            if tree_quota_details and \
                    not tree_quota_details['is_user_quotas_enforced']:
                self.provisioning.update_tree_quota(
                    tree_quota_details['id'],
                    {'is_user_quotas_enforced': True})
        except Exception as e:
            error_message = "Unable to enforce user quotas on tree quotas," \
                            " failed with error: {0}".format(str(e))
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def create_quota(self, quota_type, path=None, filesystem=None,
                     description=None, windows_name=None, windows_sid=None,
                     unix_name=None, uid=None, hard_limit=None,
                     soft_limit=None):
        """
        Create a User/Tree Quota
        :param quota_type: Type of the Quota.
        :param path: Path for which the quota exists.
        :param filesystem: ID of the filesystem.
        :param description: Additional Info about the Tree Quota.
        :param windows_name: Name of the windows host.
        :param windows_sid: SID of the windows host.
        :param unix_name: Name of the Unix host.
        :param uid: ID of the Unix Host
        :param hard_limit: Hard limit imposed on the Quota
        :param soft_limit: Soft limit imposed on the Quota
        :return: ID of the Created Quota.
        """
        if quota_type == "tree":
            if not filesystem or not path:
                self.module.fail_json(msg="Path and filesystem are required"
                                          " for creation of tree quota.")
            self.enable_quotas(filesystem)
            try:
                tree_quota_params = create_params_dict(
                    description=description,
                    hard_limit=hard_limit,
                    soft_limit=soft_limit)
                quota_id = self.provisioning.create_tree_quota(
                    filesystem, path, tree_quota_params=tree_quota_params)
                return quota_id['id']
            except Exception as e:
                err_msg = "Create quota for path = {0} on filesystem = {1}" \
                          " failed with error =  {2}" \
                          "".format(path, self.module.params['filesystem'],
                                    str(e))
                LOG.error(err_msg)
                self.module.fail_json(msg=err_msg)

        if quota_type == "user":
            if not filesystem or not (uid or windows_sid or
                                      windows_name or unix_name):
                self.module.fail_json(
                    msg="UID/Windows SID/Windows Name/Unix Name and "
                        "filesystem both are required to create User Quota")
            tree_quota_id = None
            self.enable_quotas(filesystem)
            try:
                # If path is given and quota type is user then the
                # user quota will be created on tree quota.
                # Hence enforcing user quotas on tree quotas.
                if path and path != '/':
                    tree_quota_id = self.get_tree_quota_id(path, filesystem)
                    self.enforce_user_quota_on_tree_quota(path, filesystem)

                user_quota_params_dict = create_params_dict(
                    uid=uid, unix_name=unix_name,
                    windows_name=windows_name, windows_sid=windows_sid,
                    hard_limit=hard_limit, soft_limit=soft_limit,
                    tree_quota_id=tree_quota_id)
                quota_id = self.provisioning.create_user_quota(
                    file_system_id=filesystem,
                    user_quota_params=user_quota_params_dict)
                return quota_id['id']

            except Exception as e:
                user_name = None
                user_type = None
                if uid is not None:
                    user_name = str(uid)
                    user_type = 'uid'
                elif unix_name:
                    user_name = unix_name
                    user_type = "unix_name"
                elif windows_name:
                    user_name = windows_name
                    user_type = "windows_name"
                elif windows_sid:
                    user_name = windows_sid
                    user_type = "windows_sid"

                error_message = "Create quota for {0}: {1} failed" \
                                " with {2}".format(user_type, user_name,
                                                   str(e))
                LOG.error(error_message)
                self.module.fail_json(msg=error_message)

    def update_quota(self, quota_type, quota_details=None,
                     description=None, hard_limit=None,
                     soft_limit=None):
        """
        Update the Quota details
        :param quota_type: Type of the Quota.
        :param quota_details: Details of the Quota.
        :param description: Additional Info about the Tree Quota.
        :param hard_limit: Hard limit imposed on the Quota
        :param soft_limit: Soft limit imposed on the Quota
        :return: True if the operation is successful.
        """
        filesystem = quota_details['file_system']['id']
        quota_id = quota_details['id']
        # Set 'is_quotas_enabled' parameter to True for the filesystem,
        # in case if quota is created through UI and modification is done
        # by ansible quota module

        try:
            self.enable_quotas(filesystem)
            if quota_type == "tree":
                tree_quota_params = create_params_dict(
                    description=description, hard_limit=hard_limit,
                    soft_limit=soft_limit)
                self.provisioning.update_tree_quota(
                    quota_id, tree_quota_params=tree_quota_params)
                LOG.info("Tree Quota attributes updated successfully.")
                return True

            if quota_type == "user":
                user_quota_params = create_params_dict(
                    hard_limit=hard_limit, soft_limit=soft_limit)
                self.provisioning.update_user_quota(
                    user_quota_id=quota_id,
                    user_quota_params=user_quota_params)
                return True

        except Exception as e:
            error_message = "Update quota for quota_id: {0} failed" \
                            " with {1}".format(quota_id, str(e))
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def delete_quota(self, quota_type, quota_id):
        """
        Delete Tree Quota
        :param quota_type: Type of the quota
        :param quota_id: ID of the Quota.
        :return: True, else error
        """
        try:
            if quota_type == "tree":
                self.provisioning.delete_tree_quota(quota_id)
                return True
            else:
                self.module.fail_json(msg="Deletion of User Quota"
                                          " is not supported.")
        except Exception as e:
            error_message = "Delete Tree quota with quota_id: {0} failed" \
                            " with {1}".format(quota_id, str(e))
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def show_quota_details(self, quota_id, quota_type, path, filesystem_id,
                           uid, unix_name,
                           windows_name, windows_sid, state):
        """
        Show the details of the Tree/User Quota.
        """
        quota_details = {}
        if state == "present":
            quota_details, type = self.get_quota_details(
                quota_id, quota_type, path, filesystem_id, uid, unix_name,
                windows_name, windows_sid)
        if state == "present" and quota_type == "user" and \
                quota_details and quota_details['tree_quota']:
            tree_quota = add_limits_with_unit(quota_details['tree_quota'])
            quota_details['tree_quota_for_user_quota'] = tree_quota
            quota_details.pop('tree_quota')
        if quota_details:
            quota_details = add_limits_with_unit(quota_details)
        return quota_details

    def validate_description(self, description):
        """
        Check if entered description is valid or not.
        """
        if description is not None:
            if description.strip() == "":
                self.module.fail_json(msg="Empty description or white spaced"
                                          " description is not allowed. "
                                          "Please enter a valid description")
            if description != description.strip():
                self.module.fail_json(
                    msg="Description starting or ending with"
                        " white spaces is not allowed. "
                        "Please enter a valid description")

    def perform_module_operation(self):
        """
        Perform different actions on  Quota module based on parameters
        chosen in playbook
        """

        quota_id = self.module.params['quota_id']
        path = self.module.params['path']
        nas_server = self.module.params['nas_server']
        quota_type = self.module.params['quota_type']

        description = self.module.params['description']
        self.validate_description(description)

        windows_name = self.module.params['windows_name']
        # Converting Domain Name to upper case as
        # REST API accepts it in Upper case only.
        try:
            if windows_name:
                windows_name = \
                    windows_name.split('\\')[0].upper() + \
                    "\\" + windows_name.split('\\')[1]
        except Exception:
            error_message = "Please enter domain name and user name" \
                            " in the windows_name parameter."
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)
        unix_name = self.module.params['unix_name']
        uid = self.module.params['uid']
        windows_sid = self.module.params['windows_sid']
        state = self.module.params['state']

        quota = self.module.params['quota']
        hard_limit = soft_limit = None
        if quota:
            quota = self.convert_quota_thresholds(quota)
            hard_limit = quota['hard_limit']
            soft_limit = quota['soft_limit']

        filesystem_id = None
        changed = False
        filesystem = self.module.params['filesystem']
        if filesystem:
            filesystem_id = self.get_filesystem_id(filesystem, nas_server)

        # Get Details of Tree/User Quota
        quota_details, q_type = self.get_quota_details(
            quota_id, quota_type, path, filesystem_id, uid, unix_name,
            windows_name, windows_sid)
        if quota_id and state == 'present' and not quota_details:
            self.module.fail_json(msg="Unable to fetch the quota details, "
                                      "Invalid Quota ID passed. ")
        if quota_id or q_type:
            quota_type = q_type
        # Check if valid combination of parameters are entered or not.
        if quota_type == "user" and description:
            self.module.fail_json(
                msg="Description parameter is not valid for User Quota.")

        # Check if valid combination of parameters are entered or not.
        if quota_type == "tree":
            if uid or unix_name or windows_sid or windows_name:
                self.module.fail_json(
                    msg="uid/unix_name/windows_sid/windows_name are not "
                        "valid parameters for Tree Quota type. "
                        "Please enter correct quota_type")

        # Update TREE/USER Quota details
        if state == "present" and quota_details:
            update_flag = to_modify(description, hard_limit, soft_limit,
                                    quota_details)
            if update_flag:
                changed = self.update_quota(quota_type, quota_details,
                                            description, hard_limit,
                                            soft_limit)

        # Create a TREE/USER Quota.
        if state == "present" and not quota_details:
            LOG.info("Creating a Tree/User Quota")
            quota_id = self.create_quota(quota_type, path, filesystem_id,
                                         description, windows_name,
                                         windows_sid, unix_name, uid,
                                         hard_limit, soft_limit)
            changed = True

        # Delete Tree Quota
        if state == "absent" and quota_details:
            changed = self.delete_quota(quota_type, quota_details['id'])

        self.result["changed"] = changed

        quota_details = self.show_quota_details(
            quota_id, quota_type, path, filesystem_id, uid, unix_name,
            windows_name, windows_sid, state)
        self.result["quota_details"] = quota_details
        self.module.exit_json(**self.result)


def to_modify(description, hard_limit, soft_limit, quota_details):
    """
    Check if the quota attributes are to be modified or not.
    :param description: Additional Info about the Tree Quota.
    :param hard_limit: Hard limit imposed on the Quota
    :param soft_limit: Soft limit imposed on the Quota
    :param quota_details: Details of the Quota.
    :return: True if modification is required, else False.
    """
    if description is not None and "description" in quota_details.keys() \
            and description != quota_details['description']:
        return True
    # Validating the equality of limits up to MegaBytes level only.
    if hard_limit is not None and (hard_limit / (1024 * 1024)) != (
            quota_details['hard_limit'] / (1024 * 1024)):
        return True
    if soft_limit is not None and (soft_limit / (1024 * 1024)) != (
            quota_details['soft_limit'] / (1024 * 1024)):
        return True
    return False


def create_params_dict(**kwargs):
    """
    Create a dictionary of the parameters
    """
    payload_dict = {}
    if kwargs:
        for key, value in kwargs.items():
            if value is not None:
                payload_dict[key] = value
    return payload_dict


def add_limits_with_unit(quota_details):
    """
    Adds limits to the quota details with units.
    :param quota_details: Details of the Quota
    :return: Updated quota details if quota details exists else None
    """
    if quota_details is None:
        return None
    limit_list = ['hard_limit', 'soft_limit']
    for limit in limit_list:
        if quota_details[limit]:
            size_with_unit = utils.convert_size_with_unit(
                quota_details[limit]).split(" ")
            new_limit = limit + "(" + size_with_unit[1] + ")"
            quota_details[new_limit] = size_with_unit[0]
            quota_details.pop(limit)
    return quota_details


def get_powerstore_quota_parameters():
    """This method provides parameters required for the ansible Quota
    module on Powerstore"""
    return dict(
        path=dict(), nas_server=dict(), filesystem=dict(),
        quota_type=dict(choices=['user', 'tree']),
        description=dict(),
        quota_id=dict(), windows_name=dict(), unix_name=dict(),
        uid=dict(type='int'), windows_sid=dict(),
        quota=dict(
            type='dict', options=dict(
                soft_limit=dict(type='int'),
                hard_limit=dict(type='int'),
                cap_unit=dict(choices=['GB', 'TB'], default='GB')
            ),
        ),
        state=dict(required=True, choices=['present', 'absent'])
    )


def main():
    """ Create Quota object and perform actions on it
    based on user input from playbook"""

    obj = PowerStoreQuota()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
