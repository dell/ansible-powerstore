#!/usr/bin/python
# Copyright: (c) 2019-2021, DellEMC
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: snapshot
version_added: '1.0.0'
short_description: Manage Snapshots on Dell EMC PowerStore.
description:
- Managing Snapshots on PowerStore storage system, Create a new Volume Group
  Snapshot, Get details of Volume Group Snapshot, Modify Volume Group
  Snapshot, Delete an existing Volume Group Snapshot, Create a new Volume
  Snapshot, Get details of Volume Snapshot, Modify Volume Snapshot, Delete an
  existing Volume Snapshot.
author:
- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>
- Prashant Rakheja (@prashant-dell) <ansible.team@dell.com>
extends_documentation_fragment:
- dellemc.powerstore.dellemc_powerstore.powerstore
options:
  snapshot_name:
    description:
    - The name of the Snapshot. Either snapshot name or ID is required.
    type: str
  snapshot_id:
    description:
    - The ID of the Snapshot. Either snapshot ID or Snapshot name is required.
    type: str
  volume:
    description:
    - The volume. This could be the volume name or ID.
    type: str
  volume_group:
    description:
    - The volume group. This could be the volume group name or ID.
    type: str
  new_snapshot_name:
    description:
    - The new name of the Snapshot.
    type: str
  desired_retention:
    description:
    - The retention value for the Snapshot.
    - If the retention value is not specified, the Snapshot
      details would be returned.
    - To create a Snapshot, either a retention or expiration
      timestamp must be given.
    - If the Snapshot does not have any retention value - specify it as 'None'.
    type: str
  retention_unit:
    description:
    - The unit for retention.
    - If this unit is not specified, 'hours' is taken as default
      retention_unit.
    - If desired_retention is specified, expiration_timestamp cannot be
      specified.
    choices: [hours, days]
    type: str
  expiration_timestamp:
    description:
    - The expiration timestamp of the Snapshot. This should be provided in
      UTC format, e.g 2019-07-24T10:54:54Z.
    type: str
  description:
    description:
    - The description for the Snapshot.
    type: str
  state:
    description:
    - Defines whether the Snapshot should exist or not.
    required: true
    choices: [absent, present]
    type: str
  '''

EXAMPLES = r'''
    - name: Create a volume snapshot on PowerStore
      snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        volume: "{{volume}}"
        description: "{{description}}"
        desired_retention: "{{desired_retention}}"
        retention_unit: "{{retention_unit_days}}"
        state: "{{state_present}}"

    - name: Get details of a volume snapshot
      snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        volume: "{{volume}}"
        state: "{{state_present}}"

    - name: Rename volume snapshot
      snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        new_snapshot_name: "{{new_snapshot_name}}"
        volume: "{{volume}}"
        state: "{{state_present}}"

    - name: Delete volume snapshot
      snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{new_snapshot_name}}"
        volume: "{{volume}}"
        state: "{{state_absent}}"

    - name: Create a volume group snapshot on PowerStore
      snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        volume_group: "{{volume_group}}"
        description: "{{description}}"
        expiration_timestamp: "{{expiration_timestamp}}"
        state: "{{state_present}}"

    - name: Get details of a volume group snapshot
      snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        volume_group: "{{volume_group}}"
        state: "{{state_present}}"

    - name: Modify volume group snapshot expiration timestamp
      snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        volume_group: "{{volume_group}}"
        description: "{{description}}"
        expiration_timestamp: "{{expiration_timestamp_new}}"
        state: "{{state_present}}"

    - name: Rename volume group snapshot
      snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        new_snapshot_name: "{{new_snapshot_name}}"
        volume_group: "{{volume_group}}"
        state: "{{state_present}}"

    - name: Delete volume group snapshot
      snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{new_snapshot_name}}"
        volume_group: "{{volume_group}}"
        state: "{{state_absent}}"
'''

RETURN = r'''

changed:
    description: Whether or not the resource has changed
    returned: always
    type: bool

create_vg_snap:
    description: A boolean flag to indicate whether volume group snapshot got
                 created.
    returned: When value exists
    type: bool

create_vol_snap:
    description: A boolean flag to indicate whether volume snapshot got
                 created.
    returned: When value exists
    type: bool

delete_vg_snap:
    description: A boolean flag to indicate whether volume group snapshot got
                 deleted.
    returned: When value exists
    type: bool

delete_vol_snap:
    description: A boolean flag to indicate whether volume snapshot got
                 deleted.
    returned: When value exists
    type: bool

modify_vg_snap:
    description: A boolean flag to indicate whether volume group snapshot got
                 modified.
    returned: When value exists
    type: bool

modify_vol_snap:
    description: A boolean flag to indicate whether volume snapshot got
                 modified.
    returned: When value exists
    type: bool

snap_details:
    description: Details of the snapshot
    returned: When snapshot exists
    type: complex
    contains:
        id:
            description: The system generated ID given to the snapshot.
            type: str
        name:
            description: Name of the snapshot.
            type: str
        size:
            description: Size of the snapshot.
            type: int
        description:
            description: Description about the snapshot.
            type: str
        creation_timestamp:
            description: The creation timestamp of the snapshot.
            type: str
        performance_policy_id:
            description: The performance policy for the snapshot.
            type: str
        protection_policy_id:
            description: The protection policy of the snapshot.
            type: str
        state:
            description: The state of the snapshot.
            type: str
        type:
            description: The type of the snapshot.
            type: str
        protection_data:
            description: The protection data of the snapshot.
            type: complex
            contains:
                expiration_timestamp:
                    description: The expiration timestamp of the snapshot.
                    type: str
        volumes:
            description: The volumes details of the volume group snapshot.
            type: complex
            contains:
                id:
                    description: The system generated ID given to the volume
                                 associated with the volume group.
                    type: str
'''

import logging
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import dellemc_ansible_powerstore_utils as utils
from datetime import datetime, timedelta

LOG = utils.get_logger('snapshot',
                       log_devel=logging.INFO)

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.4.0'


class PowerStoreSnapshot(object):
    """Class with Snapshot operations"""

    def __init__(self):
        """Define all the parameters required by this module"""

        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(
            get_powerstore_snapshot_parameters())

        mutually_exclusive = [
            ['volume', 'volume_group'], ['snapshot_name', 'snapshot_id'],
            ['desired_retention', 'expiration_timestamp']

        ]

        required_one_of = [
            ['snapshot_name', 'snapshot_id'], ['volume', 'volume_group']
        ]

        # Initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mutually_exclusive,
            required_one_of=required_one_of
        )

        LOG.info('HAS_PY4PS = %s , IMPORT_ERROR = %s',
                 HAS_PY4PS, IMPORT_ERROR)
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

    def get_vol_snap_details(self, snapshot):
        """Returns details of a Volume Snapshot"""
        if snapshot is None:
            self.module.fail_json(msg="Snapshot not found")
        try:
            return self.protection.get_volume_snapshot_details(snapshot['id'])
        except Exception as e:
            self.module.fail_json(msg="Failed to get details of Volume snap: "
                                      "%s with error %s"
                                      % (snapshot['name'], str(e)), **utils.failure_codes(e))

    def get_vol_group_snap_details(self, snapshot):
        """Returns details of a Volume Group Snapshot"""
        if snapshot is None:
            self.module.fail_json(msg="Snapshot not found")
        try:
            return self.protection.get_volume_group_snapshot_details(
                snapshot['id'])
        except Exception as e:
            self.module.fail_json(msg="Failed to get details of VG snap: %s"
                                      " with error %s"
                                      % (snapshot['name'], str(e)), **utils.failure_codes(e))

    def get_vol_snapshot(self, volume_id, snapshot_name, snapshot_id):
        """Get the volume snapshot"""
        try:
            vol_snaps = self.protection.get_volume_snapshots(volume_id)
            snapshot = None
            for snap in vol_snaps:
                if snapshot_name is not None:
                    if snap['name'] == snapshot_name:
                        LOG.info("Found snapshot by name: %s", snapshot_name)
                        snapshot = snap
                        break
                elif snapshot_id is not None and snap['id'] == snapshot_id:
                    LOG.info("Found snapshot by ID: %s", snapshot_id)
                    snapshot = snap
                    break
            return snapshot
        except Exception as e:
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR \
                    and e.status_code == "404":
                msg = ('No Volume Snapshot present with name %s, id %s'
                       ' error: %s', snapshot_name, snapshot_id, str(e))
                LOG.info(msg)
                return None
            msg = ("Not able to get snapshot details for volume: %s with "
                   "error %s", volume_id, str(e))
            LOG.info(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_vol_group_snapshot(self, vg_id, snapshot_name, snapshot_id):
        """Get Volume Group Snapshot"""
        try:
            vg_snaps = self.protection.get_volume_group_snapshots(vg_id)
            snapshot = None
            for snap in vg_snaps:
                if snapshot_name is not None:
                    if snap['name'] == snapshot_name:
                        LOG.info("Found snapshot by name: %s", snapshot_name)
                        snapshot = snap
                        break
                elif snapshot_id is not None and snap['id'] == snapshot_id:
                    LOG.info("Found snapshot by ID: %s", snapshot_id)
                    snapshot = snap
                    break
            return snapshot
        except Exception as e:
            msg = ("Not able to get snapshot details for volume group: %s"
                   " with error %s", vg_id, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR \
                    and e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.info(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_vol_id_from_volume(self, volume):
        """Maps the volume to volume ID"""

        is_valid_uuid = utils.name_or_id(volume)
        if is_valid_uuid == "ID":
            try:
                vol = self.provisioning.get_volume_details(volume)
                return vol['id']
            except Exception as e:
                LOG.info("No volume found by ID: %s, looking it up by name. "
                         "Error: %s", volume, str(e))

        try:
            vol = \
                self.provisioning.get_volume_by_name(volume)
            if vol:
                return vol[0]['id']
            else:
                self.module.fail_json(
                    msg=("Volume %s was not found on the array." % volume))
        except Exception as e:
            self.module.fail_json(msg="Failed to get vol %s by name with "
                                      "error %s" % (volume, str(e)), **utils.failure_codes(e))

    def get_vol_group_id_from_vg(self, volume_group):
        """Maps the volume group to Volume Group ID"""

        is_valid_uuid = utils.name_or_id(volume_group)

        if is_valid_uuid == "ID":
            try:
                vg = self.provisioning.get_volume_group_details(
                    volume_group_id=volume_group)
                return vg['id']
            except Exception as e:
                LOG.info("No volume group found by ID: %s, looking it up by "
                         "name. Error %s", volume_group, str(e))

        try:
            vg = \
                self.provisioning.get_volume_group_by_name(volume_group)
            if vg:
                return vg[0]['id']
            else:
                self.module.fail_json(
                    msg="Volume Group %s was not found on the array."
                        % volume_group)
        except Exception as e:
            self.module.fail_json(msg="Failed to get volume group: %s by "
                                      "name with error: %s"
                                      % (volume_group, str(e)), **utils.failure_codes(e))

    def create_vol_snapshot(self, snapshot_name,
                            description,
                            volume_id,
                            desired_retention,
                            expiration_timestamp,
                            new_name):
        """Create a snap for a volume on PowerStore"""

        if snapshot_name is None:
            self.module.fail_json(msg="Please provide a "
                                      "valid snapshot name.")

        if desired_retention is None and expiration_timestamp is None:
            self.module.fail_json(msg="Please provide "
                                      "desired_retention or expiration_"
                                      "timestamp for creating a snapshot")

        if new_name is not None:
            self.module.fail_json(msg="Invalid param: new_name while "
                                      "creating a new snapshot.")

        snapshot = self.get_vol_snapshot(volume_id, snapshot_name, None)
        if snapshot is not None:
            LOG.error("Snapshot: %s already exists", snapshot_name)
            return False

        try:
            resp = \
                self.protection.create_volume_snapshot(
                    name=snapshot_name,
                    description=description,
                    volume_id=volume_id,
                    expiration_timestamp=expiration_timestamp)
            return True, resp
        except Exception as e:
            error_message = ('Failed to create snapshot: %s for volume %s '
                             'with error: %s'
                             % (snapshot_name, self.module.params['volume'],
                                str(e)))
            LOG.error(error_message)
            self.module.fail_json(msg=error_message, **utils.failure_codes(e))

    def create_vg_snapshot(self, snapshot_name,
                           description,
                           vg_id,
                           desired_retention,
                           expiration_timestamp,
                           new_name):
        """Create a snap for a VG on PowerStore"""

        if snapshot_name is None:
            self.module.fail_json(msg="Please provide a "
                                      "valid snapshot name.")

        if desired_retention is None and expiration_timestamp is None:
            self.module.fail_json(msg="Please provide "
                                      "desired_retention or expiration_"
                                      "timestamp for creating a snapshot")

        if new_name is not None:
            self.module.fail_json(msg="Invalid param: new_name while "
                                      "creating a new snapshot.")

        try:
            resp = \
                self.protection.create_volume_group_snapshot(
                    name=snapshot_name,
                    description=description,
                    volume_group_id=vg_id,
                    expiration_timestamp=expiration_timestamp)
            return True, resp
        except Exception as e:
            error_message = ('Failed to create snapshot: %s for VG %s '
                             'with error: %s'
                             % (snapshot_name,
                                self.module.params['volume_group'],
                                str(e)))
            LOG.error(error_message)
            self.module.fail_json(msg=error_message, **utils.failure_codes(e))

    def delete_vol_snapshot(self, snapshot):
        """Deletes a Vol snapshot on PowerStore"""
        try:
            self.protection.delete_volume_snapshot(snapshot['id'])
            return True
        except Exception as e:
            e_msg = str(e)
            error_message = ('Failed to delete snapshot: %s with error: %s'
                             % (snapshot['name'], e_msg))
            LOG.error(error_message)
            self.module.fail_json(msg=error_message, **utils.failure_codes(e))

    def delete_vol_group_snapshot(self, snapshot):
        """Deletes a Vol group snapshot on PowerStore"""
        try:
            self.protection.delete_volume_group_snapshot(snapshot['id'])
            return True
        except Exception as e:
            error_message = ("Failed to delete snapshot: %s with error: %s"
                             % snapshot['name'], str(e))
            LOG.error(error_message)
            self.module.fail_json(msg=error_message, **utils.failure_codes(e))

    def rename_vol_snapshot(self, snapshot, new_name):
        """Renames a vol snapshot"""
        # Check if new name is same is present name

        if snapshot is None:
            self.module.fail_json(msg="Snapshot not found.")

        if snapshot['name'] == new_name:
            return False, None
        try:
            changed = False
            self.protection.modify_volume_snapshot(
                snapshot_id=snapshot['id'],
                name=new_name)
            changed = True

            if changed:
                resp = self.get_vol_snap_details(snapshot)
                return changed, resp
            else:
                return changed, None
        except Exception as e:
            error_message = ('Failed to rename snapshot: %s with error: %s'
                             % (snapshot['name'], str(e)))
            LOG.error(error_message)
            self.module.fail_json(msg=error_message, **utils.failure_codes(e))

    def rename_vol_group_snapshot(self, snapshot, new_name):
        """Renames a vol group snapshot"""

        if snapshot is None:
            self.module.fail_json(msg="Snapshot not found.")

        if snapshot['name'] == new_name:
            return False, None
        try:
            changed = False
            self.protection.modify_volume_group_snapshot(
                snapshot_id=snapshot['id'],
                name=new_name)
            changed = True

            if changed:
                resp = self.get_vol_group_snap_details(snapshot)
                return changed, resp
            else:
                return changed, None
        except Exception as e:
            error_message = ('Failed to delete snapshot: %s with error: %s'
                             % (snapshot['name'], str(e)))
            LOG.error(error_message)
            self.module.fail_json(msg=error_message, **utils.failure_codes(e))

    def check_snapshot_modified(self, snapshot, volume, volume_group,
                                description, desired_retention,
                                retention_unit, expiration_timestamp):
        """Determines whether the snapshot has been modified"""
        LOG.info("Determining if the snap has been modified...")
        snapshot_modification_details = dict()
        snapshot_modification_details['is_description_modified'] = False
        snapshot_modification_details['new_description_value'] = None
        snapshot_modification_details['is_timestamp_modified'] = False
        snapshot_modification_details['new_expiration_timestamp_value'] = None
        datetime_format = "%Y-%m-%dT%H:%MZ"

        if desired_retention is None and expiration_timestamp is None:
            LOG.info("desired_retention and expiration_time are both "
                     "not provided, we don't check for snapshot modification "
                     "in this case. The snapshot details would be returned, "
                     "if available.")
            return False, snapshot_modification_details

        snap_details = None
        if volume is not None:
            snap_details = self.get_vol_snap_details(snapshot)
        elif volume_group is not None:
            snap_details = self.get_vol_group_snap_details(snapshot)

        snap_creation_timestamp = None
        if 'creation_timestamp' in snap_details:
            # Only taking into account YYYY-MM-DDTHH-MM, ignoring
            # seconds component.
            snap_creation_timestamp = \
                snap_details['creation_timestamp'][0:16] + 'Z'

        if desired_retention is not None and desired_retention != 'None':
            if retention_unit is None or retention_unit == 'hours':
                expiration_timestamp = (datetime.strptime(
                    snap_creation_timestamp, datetime_format) +
                    timedelta(
                    hours=int(desired_retention))
                ).isoformat() \
                    + 'Z'
            elif retention_unit == 'days':
                expiration_timestamp = (datetime.strptime(
                    snap_creation_timestamp, datetime_format) + timedelta(
                    days=int(desired_retention))).isoformat() + 'Z'
        elif desired_retention == 'None':
            expiration_timestamp = None

        LOG.info("The new expiration timestamp is %s", expiration_timestamp)

        modified = False
        # Only taking into account YYYY-MM-DDTHH-MM, ignoring
        # seconds component.
        if snap_details['protection_data']['expiration_timestamp'] \
                and expiration_timestamp and \
                snap_details['protection_data']['expiration_timestamp'][0:16]\
                != expiration_timestamp[0:16]:
            # We can tolerate a delta of two minutes.
            existing_timestamp = \
                snap_details['protection_data']['expiration_timestamp'][
                    0:16] + 'Z'
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
                snapshot_modification_details[
                    'is_timestamp_modified'] = True
                snapshot_modification_details[
                    'new_expiration_timestamp_value'] = \
                    expiration_timestamp
                modified = True

        if (not snap_details['protection_data']['expiration_timestamp']) \
                and expiration_timestamp:
            snapshot_modification_details['is_timestamp_modified'] = True
            snapshot_modification_details[
                'new_expiration_timestamp_value'] = expiration_timestamp
            modified = True

        if (not expiration_timestamp) and \
                snap_details['protection_data']['expiration_timestamp']:
            snapshot_modification_details['is_timestamp_modified'] = True
            snapshot_modification_details['new_expiration_timestamp_value'] =\
                expiration_timestamp
            modified = True

        if 'description' in snap_details and description is not None and \
                snap_details['description'] != description:
            snapshot_modification_details['is_description_modified'] = True
            snapshot_modification_details['new_description_value'] = \
                description
            modified = True

        LOG.info("Snapshot modified %s, modification details: %s",
                 modified, snapshot_modification_details)

        return modified, snapshot_modification_details

    def modify_vol_snapshot(self, snapshot,
                            snapshot_modification_details):
        """Modify a volume snapshot"""
        try:
            changed = False
            if snapshot_modification_details['is_description_modified']:
                new_description = \
                    snapshot_modification_details['new_description_value']
                self.protection.modify_volume_snapshot(
                    snapshot_id=snapshot['id'],
                    description=new_description)
                changed = True
            if snapshot_modification_details['is_timestamp_modified']:
                new_timestamp = \
                    snapshot_modification_details[
                        'new_expiration_timestamp_value']
                self.protection.modify_volume_snapshot(
                    snapshot_id=snapshot['id'],
                    expiration_timestamp=new_timestamp)
                changed = True
            if changed:
                resp = self.get_vol_snap_details(
                    snapshot)
                return changed, resp
            else:
                return changed, None
        except Exception as e:
            error_message = ('Failed to modify snapshot %s with error %s'
                             % (snapshot['name'], str(e)))
            LOG.info(error_message)
            self.module.fail_json(msg=error_message, **utils.failure_codes(e))

    def modify_vol_group_snapshot(self, snapshot,
                                  snapshot_modification_details):
        """Modify a volume group snapshot"""
        try:
            changed = False
            if snapshot_modification_details['is_description_modified']:
                new_description = \
                    snapshot_modification_details['new_description_value']
                self.protection.modify_volume_group_snapshot(
                    snapshot_id=snapshot['id'],
                    description=new_description)
                changed = True
            if snapshot_modification_details['is_timestamp_modified']:
                new_timestamp = \
                    snapshot_modification_details[
                        'new_expiration_timestamp_value']
                self.protection.modify_volume_group_snapshot(
                    snapshot_id=snapshot['id'],
                    expiration_timestamp=new_timestamp)
                changed = True
            if changed:
                resp = self.get_vol_group_snap_details(
                    snapshot)
                return changed, resp
            else:
                return changed, None
        except Exception as e:
            error_message = ('Failed to modify snapshot %s with error %s'
                             % (snapshot['name'], str(e)))
            LOG.info(error_message)
            self.module.fail_json(msg=error_message, **utils.failure_codes(e))

    def validate_expiration_timestamp(self, expiration_timestamp):
        """Validates whether the expiration timestamp is valid"""
        try:
            datetime.strptime(expiration_timestamp,
                              '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            self.module.fail_json(msg='Incorrect date format, '
                                      'should be YYYY-MM-DDTHH:MM:SSZ')

    def validate_desired_retention(self, desired_retention, retention_unit):
        """Validates the specified desired retention"""

        if desired_retention == 'None':
            LOG.info("Desired retention is set to 'None'")
            return

        try:
            desired_retention = int(desired_retention)
            if (retention_unit == 'hours' or retention_unit is None) and \
                    (desired_retention < 1 or desired_retention > 744):
                self.module.fail_json(msg="Please provide a valid integer "
                                          "as the desired retention between "
                                          "1 and 744.")
            elif retention_unit == 'days' and (desired_retention < 1 or
                                               desired_retention > 31):
                self.module.fail_json(msg="Please provide a valid integer as "
                                          "the desired retention between 1 "
                                          "and 31.")
        except ValueError:
            self.module.fail_json(msg="Please provide a valid integer"
                                      " as the desired retention.")

    def perform_module_operation(self):
        """
        Perform different actions on VG or volume Snapshot based on user
        parameter chosen in playbook
        """

        volume = self.module.params['volume']
        volume_group = self.module.params['volume_group']
        snapshot_name = self.module.params['snapshot_name']
        snapshot_id = self.module.params['snapshot_id']
        new_snapshot_name = self.module.params['new_snapshot_name']
        desired_retention = self.module.params['desired_retention']
        retention_unit = self.module.params['retention_unit']
        expiration_timestamp = self.module.params['expiration_timestamp']
        description = self.module.params['description']
        state = self.module.params['state']

        result = dict(
            changed=False,
            create_vg_snap='',
            delete_vg_snap='',
            modify_vg_snap='',
            create_vol_snap='',
            delete_vol_snap='',
            modify_vol_snap='',
            snap_details='',
        )
        snapshot = None
        volume_id = None
        volume_group_id = None

        if expiration_timestamp is not None:
            self.validate_expiration_timestamp(expiration_timestamp)

        if desired_retention is not None:
            self.validate_desired_retention(desired_retention, retention_unit)

        if volume is not None:
            volume_id = self.get_vol_id_from_volume(volume)
        elif volume_group is not None:
            volume_group_id = self.get_vol_group_id_from_vg(volume_group)

        if volume is not None:
            snapshot = self.get_vol_snapshot(volume_id, snapshot_name,
                                             snapshot_id)
        elif volume_group is not None:
            snapshot = self.get_vol_group_snapshot(volume_group_id,
                                                   snapshot_name,
                                                   snapshot_id)

        is_snap_modified = False
        snapshot_modification_details = dict()
        if snapshot is not None:
            is_snap_modified, snapshot_modification_details = \
                self.check_snapshot_modified(snapshot, volume, volume_group,
                                             description, desired_retention,
                                             retention_unit,
                                             expiration_timestamp)

        if state == 'present' and volume and not snapshot:
            LOG.info("Creating new snapshot: %s for volume: %s",
                     snapshot_name, volume)
            result['create_vol_snap'], result['snap_details'] = \
                self.create_vol_snapshot(snapshot_name,
                                         description,
                                         volume_id,
                                         desired_retention,
                                         expiration_timestamp,
                                         new_snapshot_name)
            snapshot = result['snap_details']
            is_snap_modified, snapshot_modification_details = \
                self.check_snapshot_modified(snapshot, volume,
                                             volume_group, description,
                                             desired_retention,
                                             retention_unit,
                                             expiration_timestamp)
        elif state == 'absent' and (snapshot_name or snapshot_id) and \
                volume and snapshot:
            LOG.info("Deleting snapshot %s for Volume %s",
                     snapshot['name'], volume)
            result['delete_vol_snap'] = \
                self.delete_vol_snapshot(snapshot)

        if state == 'present' and volume_group and not snapshot:
            LOG.info("Creating new snapshot: %s for VG: %s",
                     snapshot_name, volume_group)
            result['create_vg_snap'], result['snap_details'] = \
                self.create_vg_snapshot(snapshot_name, description,
                                        volume_group_id, desired_retention,
                                        expiration_timestamp,
                                        new_snapshot_name)
            snapshot = result['snap_details']
            is_snap_modified, snapshot_modification_details = \
                self.check_snapshot_modified(result['snap_details'], volume,
                                             volume_group, description,
                                             desired_retention,
                                             retention_unit,
                                             expiration_timestamp)
        elif state == 'absent' and (
                snapshot_name or snapshot_id) and volume_group \
                and snapshot:
            LOG.info("Deleting snapshot %s for VG %s",
                     snapshot['name'], volume_group)
            result['delete_vg_snap'] = \
                self.delete_vol_group_snapshot(snapshot)

        if state == 'present' and volume and new_snapshot_name:
            LOG.info("Renaming snapshot %s to new name %s",
                     snapshot['name'], new_snapshot_name)
            result['modify_vol_snap'], result['snap_details'] = \
                self.rename_vol_snapshot(snapshot, new_snapshot_name)
        elif state == 'present' and volume_group \
                and new_snapshot_name:
            LOG.info("Renaming snapshot %s to new name %s",
                     snapshot['name'], new_snapshot_name)
            result['modify_vg_snap'], result['snap_details'] = \
                self.rename_vol_group_snapshot(snapshot, new_snapshot_name)

        if state == 'present' and snapshot and volume and is_snap_modified:
            LOG.info("Modifying snapshot %s", snapshot['name'])
            result['modify_vol_snap'], result['snap_details'] = \
                self.modify_vol_snapshot(snapshot,
                                         snapshot_modification_details) or \
                result['modify_vol_snap']
        elif state == 'present' and snapshot and volume_group \
                and is_snap_modified:
            LOG.info("Modifying snapshot %s", snapshot['name'])
            result['modify_vg_snap'], result['snap_details'] = \
                self.modify_vol_group_snapshot(
                    snapshot,
                    snapshot_modification_details) or \
                result['modify_vg_snap']

        if result['create_vol_snap'] or result['delete_vol_snap'] or result[
            'modify_vol_snap'] or result['create_vg_snap'] \
                or result['delete_vg_snap'] or result['modify_vg_snap']:
            result['changed'] = True

        if state == 'present' and (snapshot_name or snapshot_id) and volume\
                and not result['changed']:
            result['snap_details'] = self.get_vol_snap_details(snapshot)
        elif state == 'present' and (snapshot_name or snapshot_id) and \
                volume_group and not result['changed']:
            result['snap_details'] = self.get_vol_group_snap_details(
                snapshot)

        # Finally update the module result!
        self.module.exit_json(**result)


def get_powerstore_snapshot_parameters():
    return dict(
        volume_group=dict(required=False, type='str'),
        volume=dict(required=False, type='str'),
        snapshot_name=dict(required=False, type='str'),
        snapshot_id=dict(required=False, type='str'),
        new_snapshot_name=dict(required=False, type='str'),
        desired_retention=dict(required=False, type='str'),
        retention_unit=dict(required=False, choices=['hours', 'days'],
                            type='str'),
        expiration_timestamp=dict(required=False, type='str'),
        description=dict(required=False, type='str'),
        state=dict(required=True, choices=['present', 'absent'],
                   type='str')
    )


def main():
    """Create PowerStore Snapshot object and perform action on it
        based on user input from playbook"""
    obj = PowerStoreSnapshot()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
