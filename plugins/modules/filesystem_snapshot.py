#!/usr/bin/python
# Copyright: (c) 2024, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Ansible module for managing filesystem snapshots on PowerStore"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
module: filesystem_snapshot
version_added: '1.1.0'
short_description: Manage Filesystem Snapshots for PowerStore
description:
- Supports the provisioning operations on a filesystem snapshot such as
  create, modify, delete and get the details of a filesystem snapshot.

author:
- Akash Shendge (@shenda1) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerstore.powerstore

options:
  snapshot_name:
    description:
    - The name of the filesystem snapshot.
    - Mandatory for create operation.
    - Specify either snapshot name or ID (but not both) for any operation.
    type: str
  snapshot_id:
    description:
    - The ID of the Snapshot.
    type: str
  filesystem:
    description:
    - The ID/Name of the filesystem for which snapshot will be taken.
    - If filesystem name is specified, then I(nas_server) is required to uniquely
      identify the filesystem.
    - Mandatory for create operation.
    type: str
  nas_server:
    description:
    - The NAS server, this could be the name or ID of the NAS server.
    type: str
  description:
    description:
    - The description for the filesystem snapshot.
    type: str
  desired_retention:
    description:
    - The retention value for the Snapshot.
    - If the I(desired_retention)/I(expiration_timestamp) is not mentioned during
      creation, snapshot will be created with unlimited retention.
    - Maximum supported desired retention is 31 days.
    type: int
  retention_unit:
    description:
    - The unit for retention.
    default: 'hours'
    choices: [hours, days]
    type: str
  expiration_timestamp:
    description:
    - The expiration timestamp of the snapshot. This should be provided in
      UTC format, e.g 2020-07-24T10:54:54Z.
    - To remove the expiration timestamp, specify it as an empty string.
    type: str
  access_type:
    description:
    - Specifies whether the snapshot directory or protocol access is granted
      to the filesystem snapshot.
    - For create operation, if I(access_type) is not specified, snapshot will be
      created with C(SNAPSHOT) access type.
    choices: ['SNAPSHOT', 'PROTOCOL']
    type: str
  state:
    description:
    - Define whether the filesystem snapshot should exist or not.
    required: true
    choices: ['absent', 'present']
    type: str
notes:
- The I(check_mode) is not supported.
"""

EXAMPLES = r"""
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
"""

RETURN = r"""
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"
create_fs_snap:
    description: Whether or not the resource has created.
    returned: always
    type: bool
    sample: "false"
delete_fs_snap:
    description: Whether or not the resource has deleted.
    returned: always
    type: bool
    sample: "false"
modify_fs_snap:
    description: Whether or not the resource has modified.
    returned: always
    type: bool
    sample: "false"
filesystem_snap_details:
    description: Details of the snapshot.
    returned: When snapshot exists.
    type: dict
    contains:
        access_type:
            description: Displays the type of access allowed to the snapshot.
            type: str
        creation_timestamp:
            description: The date and time the snapshot was created.
            type: str
        description:
            description: Description of the filesystem snapshot.
            type: str
        expiration_timestamp:
            description: The date and time the snapshot is due to be
                         automatically deleted by the system.
            type: str
        id:
            description: Unique identifier of the filesystem snapshot
                         instance.
            type: str
        name:
            description: The name of the snapshot.
            type: str
        nas_server:
            description: Details of NAS server on which snapshot is present.
            type: dict
            contains:
                id:
                    description: ID of the NAS server.
                    type: str
                name:
                    description: Name of the NAS server
                    type: str
        parent_id:
            description: ID of the filesystem on which snapshot is taken.
            type: str
        parent_name:
            description: Name of the filesystem on which snapshot is taken.
            type: str
    sample: {
        "access_policy": null,
        "access_policy_l10n": null,
        "access_type": "Snapshot",
        "access_type_l10n": "Snapshot",
        "creation_timestamp": "2022-01-16T21:58:02+00:00",
        "creator_type": "User",
        "creator_type_l10n": "User",
        "default_hard_limit": null,
        "default_soft_limit": null,
        "description": null,
        "expiration_timestamp": "2022-01-17T00:58:00+00:00",
        "filesystem_type": "Snapshot",
        "filesystem_type_l10n": "Snapshot",
        "folder_rename_policy": null,
        "folder_rename_policy_l10n": null,
        "grace_period": null,
        "id": "61e49f3f-9b57-e69b-1038-aa02b52a030f",
        "is_async_MTime_enabled": false,
        "is_modified": false,
        "is_quota_enabled": null,
        "is_smb_no_notify_enabled": null,
        "is_smb_notify_on_access_enabled": null,
        "is_smb_notify_on_write_enabled": null,
        "is_smb_op_locks_enabled": null,
        "is_smb_sync_writes_enabled": null,
        "last_refresh_timestamp": null,
        "last_writable_timestamp": null,
        "locking_policy": null,
        "locking_policy_l10n": null,
        "name": "sample-filesystem-snapshot",
        nas_server: {
            "id": "6026056b-5405-0e36-7697-c285b9fa42b7",
            "name": "ansible_nas_server_2"
        },
        "parent_id": "61e4947b-8992-3db7-2859-aa02b52a0308",
        "parent_name": "sample-filesystem",
        "protection_policy": null,
        "size_total": "214748364800",
        "size_used": "1621098496",
        "smb_notify_on_change_dir_depth": 0
    }
"""

from datetime import datetime, timedelta
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import utils

LOG = utils.get_logger('filesystem_snapshot',
                       log_devel=utils.logging.INFO)

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/3.2.0'


class PowerStoreFilesystemSnapshot(object):
    """Class with Filesystem Snapshot operations"""

    def __init__(self):
        """Define all the parameters required by this module"""

        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(
            get_powerstore_filesystem_snapshot_parameters())

        mutually_exclusive = [['snapshot_name', 'snapshot_id'],
                              ['desired_retention', 'expiration_timestamp'],
                              ['snapshot_id', 'filesystem'],
                              ['snapshot_id', 'nas_server']]

        required_one_of = [['snapshot_name', 'snapshot_id']]

        # Initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True,
            mutually_exclusive=mutually_exclusive,
            required_one_of=required_one_of
        )

        LOG.info('HAS_PY4PS = %s , IMPORT_ERROR = %s', HAS_PY4PS,
                 IMPORT_ERROR)

        if not HAS_PY4PS:
            self.module.fail_json(msg=IMPORT_ERROR)

        LOG.info('IS_SUPPORTED_PY4PS_VERSION = %s , VERSION_ERROR = %s',
                 IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR)

        if not IS_SUPPORTED_PY4PS_VERSION:
            self.module.fail_json(msg=VERSION_ERROR)

        self.py4ps_conn = utils.get_powerstore_connection(
            self.module.params, application_type=APPLICATION_TYPE)
        self.protection = self.py4ps_conn.protection
        self.provisioning = self.py4ps_conn.provisioning
        LOG.info('Got Py4ps instance for PowerStore')

    def validate_expiration_timestamp(self, expiration_timestamp):
        """Validates whether the expiration timestamp is valid"""

        try:
            datetime.strptime(expiration_timestamp,
                              '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            error_msg = 'Incorrect date format, should be ' \
                        'YYYY-MM-DDTHH:MM:SSZ'
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def validate_desired_retention(self, desired_retention, retention_unit):
        """Validates the specified desired retention.
            :param desired_retention: Desired retention of the filesystem
            snapshot
            :param retention_unit: Retention unit for the filesystem snapshot
        """

        if retention_unit == 'hours' and (desired_retention < 1 or
                                          desired_retention > 744):
            self.module.fail_json(msg="Please provide a valid integer as the"
                                      " desired retention between 1 and 744.")
        elif retention_unit == 'days' and (desired_retention < 1 or
                                           desired_retention > 31):
            self.module.fail_json(msg="Please provide a valid integer as the"
                                      " desired retention between 1 and 31.")

    def get_nas_server(self, nas_server_name=None, nas_server_id=None):
        """Get the id of the NAS server.
            :param nas_server_name: The name of the NAS server
            :param nas_server_id: The id of the NAS server
            :return ID of the NAS server if exists
        """

        nas_server_id_or_name = nas_server_id if nas_server_id else \
            nas_server_name
        try:
            if nas_server_name is not None:
                nas_server_details = self.provisioning.get_nas_server_by_name(
                    nas_server_name=nas_server_name)
            else:
                nas_server_details = self.provisioning.get_nas_server_details(
                    nas_server_id=nas_server_id)

            if not nas_server_details:
                self.module.fail_json(msg="Please provide valid NAS server "
                                          "details")

            if isinstance(nas_server_details, list):
                return nas_server_details[0]['id']
            else:
                return nas_server_details['id']

        except Exception as e:
            error_msg = "Failed to get details of NAS server {0} with error" \
                        " {1}".format(nas_server_id_or_name, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def get_fs_id_from_filesystem(self, filesystem, nas_server):
        """Get the id of the filesystem.
            :param filesystem: The name/id of the filesystem
            :param nas_server: The name/id of the NAS server
            :return: The id of the filesystem
        """

        try:
            is_valid_uuid = utils.name_or_id(filesystem)
            if is_valid_uuid == "NAME":
                # Get the filesystem details using name
                nas_server_id = nas_server
                if nas_server is not None:
                    is_valid_uuid = utils.name_or_id(nas_server)
                    if is_valid_uuid == "ID":
                        nas_server_id = self.get_nas_server(
                            nas_server_id=nas_server)
                    else:
                        nas_server_id = self.get_nas_server(
                            nas_server_name=nas_server)
                else:
                    error_msg = "Please provide NAS Server details along " \
                                "with filesystem"
                    LOG.error(error_msg)
                    self.module.fail_json(msg=error_msg)

                fs = self.provisioning.get_filesystem_by_name(
                    filesystem_name=filesystem, nas_server_id=nas_server_id)
                if fs:
                    return fs[0]['id']
            else:
                # Get the filesystem details using id
                fs = self.provisioning.get_filesystem_details(filesystem)
                return fs['id']

            error_msg = "Filesystem {0} not found on the array.".format(
                filesystem)
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)
        except Exception as e:
            error_msg = "Failed to get the filesystem {0} by name with " \
                        "error {1}".format(filesystem, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def get_fs_name(self, filesystem_id):
        """Get filesystem name.
            :param filesystem_id: The id of the filesystem
            :return Filesystem name
        """

        try:
            fs = self.provisioning.get_filesystem_details(
                filesystem_id=filesystem_id)
            return fs['name']
        except Exception as e:
            error_msg = "Filesystem {0} not found on the array.".format(
                filesystem_id)
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def get_fs_snapshot(self, snapshot_name, snapshot_id, filesystem_id,
                        nas_server):
        """Get filesystem snapshot details.
            :param snapshot_name: The name of the snapshot
            :param snapshot_id: The id of the snapshot
            :param filesystem_id: The id of the filesystem
            :param nas_server: The name/id of the NAS server
            :return Dict containing filesystem snapshot details if exists
        """

        error_msg = "Failed to get the filesystem snapshot {0} with error {1}"
        nas_server_id = nas_server

        if snapshot_name and (filesystem_id is None and nas_server
                              is None):
            self.module.fail_json(msg="Please provide filesystem or NAS "
                                      "server details along with snapshot "
                                      "name.")

        if snapshot_name:
            if nas_server:
                is_valid_uuid = utils.name_or_id(nas_server)
                if is_valid_uuid == "ID":
                    nas_server_id = self.get_nas_server(
                        nas_server_id=nas_server)
                else:
                    nas_server_id = self.get_nas_server(
                        nas_server_name=nas_server)

            try:
                if nas_server_id:
                    snapshot = self.protection.\
                        get_filesystem_snapshot_details_by_name(
                            snapshot_name=snapshot_name,
                            nas_server_id=nas_server_id)

                    # Check if given filesystem_id matches with the parent_id
                    # of the snapshot
                    if snapshot and filesystem_id and \
                            snapshot[0]['parent_id'] != filesystem_id:
                        error_msg = "Given filesystem {0} does not match" \
                                    " with the filesystem of the snapshot. " \
                                    "Please provide valid filesystem.".\
                            format(filesystem_id)
                        LOG.error(error_msg)
                        self.module.fail_json(msg=error_msg)
                else:
                    snapshot = self.protection.\
                        get_filesystem_snapshot_details_by_name(
                            snapshot_name=snapshot_name,
                            filesystem_id=filesystem_id)

                if snapshot and len(snapshot) > 0:
                    snapshot_id = snapshot[0]['id']
                    snapshot = self.protection.\
                        get_filesystem_snapshot_details(
                            snapshot_id=snapshot_id)
                    snapshot['parent_name'] = self.get_fs_name(
                        snapshot['parent_id'])
                return snapshot
            except Exception as e:
                msg = error_msg.format(snapshot_name, str(e))
                if isinstance(e, utils.PowerStoreException) and \
                        e.err_code == utils.PowerStoreException.HTTP_ERR and \
                        e.status_code == "404":
                    LOG.info(msg)
                    return None
                LOG.error(msg)
                self.module.fail_json(msg=msg, **utils.failure_codes(e))

        try:
            snapshot = self.protection.get_filesystem_snapshot_details(
                snapshot_id=snapshot_id)
            snapshot['parent_name'] = self.get_fs_name(snapshot['parent_id'])
            return snapshot
        except Exception as e:
            msg = error_msg.format(snapshot_name, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def create_filesystem_snapshot(self, filesystem_id, snapshot_name,
                                   description, expiration_timestamp,
                                   access_type, nas_server):
        """Create a snapshot for a filesystem on PowerStore"""

        if snapshot_name is None or (len(snapshot_name.strip()) == 0):
            self.module.fail_json(msg="Please provide valid snapshot name.")

        if filesystem_id is None:
            error_msg = "Snapshot with name {0} is not found on nas_server " \
                "{1}. Please provide filesystem details to create a " \
                "new snapshot.".format(snapshot_name, nas_server)
            self.module.fail_json(msg=error_msg)

        if access_type:
            access_type = access_type.title()

        try:
            self.protection.create_filesystem_snapshot(
                name=snapshot_name, description=description,
                filesystem_id=filesystem_id,
                expiration_timestamp=expiration_timestamp,
                access_type=access_type)
            return True
        except Exception as e:
            error_message = 'Failed to create snapshot: {0} for filesystem ' \
                            '{1} with error: {2}'.format(snapshot_name,
                                                         self.module.params[
                                                             'filesystem'],
                                                         str(e))
            LOG.error(error_message)
            self.module.fail_json(msg=error_message, **utils.failure_codes(e))

    def check_fs_snapshot_modified(self, snapshot, filesystem_id, description,
                                   desired_retention, retention_unit,
                                   expiration_timestamp, access_type,
                                   nas_server):
        """Determines whether the snapshot has been modified"""
        LOG.info("Determining if the filesystem snapshot has been modified..")
        datetime_format = "%Y-%m-%dT%H:%MZ"

        if access_type and access_type.title() != snapshot['access_type']:
            error_message = "Modification of access type is not allowed."
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

        snap_modify_dict = dict()

        creation_timestamp = None
        if 'creation_timestamp' in snapshot:
            # Only taking into account YYYY-MM-DDTHH:MM, ignoring
            # seconds component.
            creation_timestamp = \
                snapshot['creation_timestamp'][0:16] + 'Z'

        if desired_retention:
            if retention_unit == "days":
                expiration_timestamp = \
                    (datetime.strptime(creation_timestamp,
                                       datetime_format) + timedelta(
                        days=int(desired_retention))).isoformat() + 'Z'
            else:
                expiration_timestamp = \
                    (datetime.strptime(creation_timestamp,
                                       datetime_format) + timedelta(
                        hours=int(desired_retention))).isoformat() + 'Z'

        LOG.info("The new expiration timestamp is %s", expiration_timestamp)

        if snapshot['expiration_timestamp'] and expiration_timestamp:
            # Only taking into account YYYY-MM-DDTHH:MM, ignoring seconds
            # component.
            if snapshot['expiration_timestamp'][0:16] != \
                    expiration_timestamp[0:16]:
                # We can tolerate a delta of two minutes.
                existing_timestamp = \
                    snapshot['expiration_timestamp'][0:16] + 'Z'
                new_timestamp = expiration_timestamp[0:16] + 'Z'

                existing_time_obj = datetime.strptime(existing_timestamp,
                                                      datetime_format)
                new_time_obj = datetime.strptime(new_timestamp,
                                                 datetime_format)

                if existing_time_obj > new_time_obj:
                    td = existing_time_obj - new_time_obj
                else:
                    td = new_time_obj - existing_time_obj

                td_mins = int(round(td.total_seconds() / 60))

                if td_mins > 2:
                    snap_modify_dict['expiration_timestamp'] = \
                        expiration_timestamp

        elif not snapshot['expiration_timestamp'] and expiration_timestamp:
            snap_modify_dict[
                'expiration_timestamp'] = expiration_timestamp

        elif snapshot['expiration_timestamp'] and expiration_timestamp == "":
            snap_modify_dict[
                'expiration_timestamp'] = "1970-01-01T00:00:00.000Z"

        if (description is not None and
            snapshot['description'] != description) and \
                ((snapshot['description'] is None and description != "") or
                 (snapshot['description'] is not None)):
            snap_modify_dict['description'] = description

        LOG.info("Snapshot modification details: %s", snap_modify_dict)

        return snap_modify_dict

    def modify_filesystem_snapshot(self, snapshot, fs_snapshot_dict):
        """Modify filesystem snapshot.

            :param snapshot: The details of filesystem snapshot.
            :param fs_snapshot_dict: Dict containing details to be modified
            :return: The boolean value to indicate if filesystem snapshot
                     modified
        """

        try:
            self.protection.modify_filesystem_snapshot(snapshot['id'],
                                                       **fs_snapshot_dict)
            return True
        except Exception as e:
            errormsg = "Modify operation of filesystem snapshot with " \
                       "name: {0}, id: {1} failed with error {2}".\
                format(snapshot['name'], snapshot['id'], str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg, **utils.failure_codes(e))

    def delete_filesystem_snapshot(self, snapshot):
        """Delete filesystem snapshot.
            :param snapshot: The details of filesystem snapshot
            :return The boolean value to indicate if filesystem snapshot
                    deleted
        """

        try:
            self.protection.delete_filesystem_snapshot(snapshot['id'])
            return True
        except Exception as e:
            e_msg = str(e)
            if isinstance(e, utils.PowerStoreException) and \
                    e.status_code == "422" and \
                    "not found in the system" in e_msg:
                return False
            errormsg = "Delete operation of filesystem snapshot with " \
                       "name: {0}, id: {1} failed with error {2}".\
                format(snapshot['name'], snapshot['id'], e_msg)
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg, **utils.failure_codes(e))

    def perform_module_operation(self):
        """
        Perform different actions Filesystem Snapshot based on user
        parameter chosen in playbook
        """

        snapshot_name = self.module.params['snapshot_name']
        snapshot_id = self.module.params['snapshot_id']
        filesystem = self.module.params['filesystem']
        nas_server = self.module.params['nas_server']
        description = self.module.params['description']
        desired_retention = self.module.params['desired_retention']
        retention_unit = self.module.params['retention_unit']
        expiration_timestamp = self.module.params['expiration_timestamp']
        access_type = self.module.params['access_type']
        state = self.module.params['state']

        result = dict(
            changed=False,
            create_fs_snap='',
            modify_fs_snap='',
            delete_fs_snap='',
            filesystem_snap_details=''
        )

        filesystem_id = None

        if expiration_timestamp:
            self.validate_expiration_timestamp(expiration_timestamp)

        if desired_retention is not None:
            self.validate_desired_retention(desired_retention, retention_unit)

        if filesystem is not None:
            filesystem_id = self.get_fs_id_from_filesystem(
                filesystem, nas_server)

        snapshot = self.get_fs_snapshot(
            snapshot_name, snapshot_id, filesystem_id, nas_server)

        fs_snap_modify_dict = dict()
        if state == 'present' and snapshot:
            fs_snap_modify_dict = \
                self.check_fs_snapshot_modified(
                    snapshot, filesystem_id, description, desired_retention,
                    retention_unit, expiration_timestamp, access_type,
                    nas_server)

        if state == 'present' and not snapshot:
            result['create_fs_snap'] =\
                self.create_filesystem_snapshot(
                    filesystem_id, snapshot_name, description,
                    expiration_timestamp, access_type, nas_server)

            snapshot = self.get_fs_snapshot(
                snapshot_name, snapshot_id, filesystem_id, nas_server)

            fs_snap_modify_dict = \
                self.check_fs_snapshot_modified(
                    snapshot, filesystem_id, description, desired_retention,
                    retention_unit, expiration_timestamp, access_type,
                    nas_server)

        elif state == 'absent' and snapshot:
            result['delete_fs_snap'] = self.delete_filesystem_snapshot(
                snapshot)

        if state == 'present' and snapshot and fs_snap_modify_dict:
            result['modify_fs_snap'] = self.modify_filesystem_snapshot(
                snapshot, fs_snap_modify_dict)

        if result['create_fs_snap'] or result['modify_fs_snap'] or\
                result['delete_fs_snap']:
            result['changed'] = True

        if state == 'present':
            result['filesystem_snap_details'] = self.get_fs_snapshot(
                snapshot_name, snapshot_id, filesystem_id, nas_server)

        # Finally update the module result!
        self.module.exit_json(**result)


def get_powerstore_filesystem_snapshot_parameters():
    """This method provide parameters required for the ansible filesystem
     snapshot module on PowerStore"""

    return dict(
        snapshot_name=dict(required=False, type='str'),
        snapshot_id=dict(required=False, type='str'),
        filesystem=dict(required=False, type='str'),
        nas_server=dict(required=False, type='str'),
        description=dict(required=False, type='str'),
        desired_retention=dict(required=False, type='int'),
        retention_unit=dict(required=False, choices=['hours', 'days'],
                            default='hours', type='str'),
        expiration_timestamp=dict(required=False, type='str'),
        access_type=dict(required=False, type='str',
                         choices=['SNAPSHOT', 'PROTOCOL']),
        state=dict(required=True, type='str', choices=['present', 'absent'])
    )


def main():
    """ Create PowerStore Filesystem Snapshot object and perform action on it
        based on user input from playbook"""

    obj = PowerStoreFilesystemSnapshot()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
