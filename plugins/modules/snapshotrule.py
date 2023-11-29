#!/usr/bin/python
# Copyright: (c) 2019-2021, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: snapshotrule
version_added: '1.0.0'
short_description: Snapshot Rule operations on a PowerStore storage system
description:
- Performs all snapshot rule operations on PowerStore Storage System.
- This modules supports get details of a snapshot rule, create new Snapshot
  Rule with Interval, create new Snapshot Rule with specific time and
  days_of_week. Modify Snapshot Rule. Delete Snapshot Rule.
extends_documentation_fragment:
  - dellemc.powerstore.powerstore
author:
- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
options:
  name:
    description:
    - String variable. Indicates the name of the Snapshot rule.
    type: str
  snapshotrule_id:
    description:
    - String variable. Indicates the ID of the Snapshot rule.
    type: str
  new_name:
    description:
    - String variable. Indicates the new name of the Snapshot rule.
    - Used for renaming operation.
    type: str
  days_of_week:
    description:
    - List of strings to specify days of the week on which the Snapshot rule
      should be applied. Must be applied for Snapshot rules where the
      I(time_of_day) parameter is set.
    - Optional for the Snapshot rule created with an interval. When
      I(days_of_week) is not specified for a new Snapshot rule, the rule is
      applied on every day of the week.
    choices: [ Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,
     Sunday ]
    type: list
    elements: str
  interval:
    description :
    - String variable. Indicates the interval between Snapshots.
    - When creating a Snapshot rule, specify either I(interval) or
      I(time_of_day), but not both.
    required : false
    choices: [ Five_Minutes, Fifteen_Minutes, Thirty_Minutes, One_Hour,
    Two_Hours, Three_Hours, Four_Hours, Six_Hours, Eight_Hours, Twelve_Hours,
    One_Day ]
    type: str
  desired_retention:
    description:
    - Integer variable. Indicates the desired Snapshot retention period.
    - It is required when creating a new Snapshot rule.
    required : false
    type: int
  time_of_day:
    description:
    - String variable. Indicates the time of the day to take a daily
      Snapshot, with the format "hh:mm" in 24 hour time format.
    - When creating a Snapshot rule, specify either I(interval) or
      I(time_of_day) but not both.
    required : false
    type: str
  delete_snaps:
    description:
    - Boolean variable to specify whether all Snapshots previously created by
      this rule should also be deleted when this rule is removed.
    - C(true) specifies to delete all previously created Snapshots by this rule
      while deleting this rule.
    - C(false) specifies to retain all previously created Snapshots while
      deleting this rule.
    type: bool
    default: false
  state:
    description:
    - String variable indicates the state of Snapshot rule.
    - For "Delete" operation only, it should be set to C(absent).
    - For all Create, Modify or Get details operation it should be set to
      C(present).
    required : true
    choices: [ present, absent]
    type: str

notes:
- The I(check_mode) is not supported.
'''

EXAMPLES = r'''
- name: Get details of an existing snapshot rule by name
  dellemc.powerstore.snapshotrule:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    state: "present"

- name: Get details of an existing snapshot rule by id
  dellemc.powerstore.snapshotrule:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    snapshotrule_id: "{{snapshotrule_id}}"
    state: "present"

- name: Create new snapshot rule by interval
  dellemc.powerstore.snapshotrule:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    interval: "{{interval}}"
    days_of_week:
      - Monday
    desired_retention: "{{desired_retention}}"
    state: "present"


- name: Create new snapshot rule by time_of_day and days_of_week
  dellemc.powerstore.snapshotrule:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    desired_retention: "{{desired_retention}}"
    days_of_week:
      - Monday
      - Wednesday
      - Friday
    time_of_day: "{{time_of_day}}"
    state: "present"

- name: Modify existing snapshot rule to time_of_day and days_of_week
  dellemc.powerstore.snapshotrule:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    days_of_week:
      - Monday
      - Wednesday
      - Friday
      - Sunday
    time_of_day: "{{time_of_day}}"
    state: "present"

- name: Modify existing snapshot rule to interval
  dellemc.powerstore.snapshotrule:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    interval: "{{interval}}"
    state: "present"

- name: Delete an existing snapshot rule by name
  dellemc.powerstore.snapshotrule:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    state: "absent"
'''

RETURN = r'''

changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "true"

snapshotrule_details:
    description: Details of the snapshot rule.
    returned: When snapshot rule exists
    type: complex
    contains:
        id:
            description: The system generated ID given to the snapshot rule.
            type: str
        name:
            description: Name of the snapshot rule.
            type: str
        days_of_week:
            description: List of string to specify days of the week on which
                         the rule should be applied.
            type: list
        time_of_day:
            description: The time of the day to take a daily snapshot.
            type: str
        interval:
            description: The interval between snapshots.
            type: str
        desired_retention:
            description: Desired snapshot retention period.
            type: int
        policies:
            description: The protection policies details of the snapshot rule.
            type: complex
            contains:
                id:
                    description: The protection policy ID in which the
                                 snapshot rule is selected.
                    type: str
                name:
                    description: Name of the protection policy in which the
                                 snapshot rule is selected.
                    type: str
    sample: {
        "days_of_week": [
            "Sunday",
            "Thursday"
        ],
        "desired_retention": 24,
        "id": "afa86b51-1171-498f-9786-2c78c33b4c14",
        "interval": "Five_Minutes",
        "name": "Sample_snapshot_rule",
        "policies": [],
        "time_of_day": null
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import utils
import logging

LOG = utils.get_logger(
    'snapshotrule',
    log_devel=logging.INFO)

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/3.0.0'


class PowerstoreSnapshotrule(object):
    """Snapshot Rule operations"""
    cluster_name = ' '
    cluster_global_id = ' '

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_snapshotrule_parameters())

        # initialize the Ansible module
        mut_ex_args = [['snapshotrule_id', 'name'],
                       ['interval', 'time_of_day']]
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mut_ex_args
        )
        LOG.info('HAS_PY4PS = %s , IMPORT_ERROR = %s', HAS_PY4PS,
                 IMPORT_ERROR)
        if HAS_PY4PS is False:
            self.module.fail_json(msg=IMPORT_ERROR)
        LOG.info('IS_SUPPORTED_PY4PS_VERSION = %s , VERSION_ERROR = '
                 '%s', IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR)
        if IS_SUPPORTED_PY4PS_VERSION is False:
            self.module.fail_json(msg=VERSION_ERROR)

        self.conn = utils.get_powerstore_connection(
            self.module.params, application_type=APPLICATION_TYPE)
        self.provisioning = self.conn.provisioning
        LOG.info('Got Py4ps instance for provisioning on PowerStore %s',
                 self.provisioning)
        self.protection = self.conn.protection
        LOG.info('Got Py4ps instance for protection on PowerStore %s',
                 self.protection)

    def get_snapshot_rule_details(self, name=None, id=None):
        """Get snapshot rule details by name or id"""
        try:
            LOG.info('Getting the details of snapshot rule , Name:%s ,'
                     ' ID:%s', name, id)
            if name:
                resp = self.protection.get_snapshot_rule_by_name(name)
                if resp and len(resp) > 0:
                    LOG.info('Successfully got the details of snapshot rule'
                             ' name %s from array name %s and global id %s',
                             name, self.cluster_name, self.cluster_global_id)
                    detail_resp = self.protection.get_snapshot_rule_details(
                        resp[0]['id'])
                    return False, detail_resp
            if id:
                detail_resp = self.protection.get_snapshot_rule_details(id)
                if detail_resp and len(detail_resp) > 0:
                    LOG.info('Successfully got the details of snapshot '
                             'rule id %s from array name %s and '
                             'global id %s', id, self.cluster_name,
                             self.cluster_global_id)
                    return False, detail_resp

            msg = 'No snapshot rule present with name {0} or ID {1}'.format(
                name, id)
            LOG.info(msg)
            return False, None

        except Exception as e:
            msg = 'Get details of snapshot rule name: {0} or ID {1} from ' \
                  'array name : {2} failed with' \
                  ' error : {3} '.format(name, id, self.cluster_name, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def create_snapshot_rule_by_interval(
            self,
            name,
            interval,
            desired_retention,
            days_of_week=None):
        """create snapshot rule with  name, desired_retention,
        interval and days_of_week """

        try:
            LOG.info('Creating snapshot rule with interval')
            resp = self.protection.create_snapshot_rule_by_interval(
                name=name, desired_retention=desired_retention,
                days_of_week=days_of_week,
                interval=interval)

            res = self.protection.get_snapshot_rule_details(resp.get('id'))
            LOG.info('Successfully created snapshot rule by interval , id: %s'
                     ' on powerstore array name : %s , global id : %s',
                     resp.get("id"), self.cluster_name,
                     self.cluster_global_id)
            return True, res

        except Exception as e:
            msg = 'create snapshot rule by interval on powerstore array name'\
                  ': {0} , global id : {1} failed with error {2}'.format(
                      self.cluster_name, self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def create_snapshot_rule_by_time_of_day(self, name, desired_retention,
                                            time_of_day, days_of_week=None):
        """create snapshot rule by days_of_week and time_of_day """

        try:
            LOG.info('create snapshot rule by time_of_day ')
            resp = self.protection.create_snapshot_rule_by_time_of_day(
                name, desired_retention, time_of_day, days_of_week)
            result = self.protection.get_snapshot_rule_details(resp.get('id'))
            LOG.info(
                'Successfully created snapshot rule by by time_of_day %s'
                'on powerstore array name : %s ,global id : %s',
                resp.get("id"), self.cluster_name, self.cluster_global_id)
            return True, result

        except Exception as e:
            msg = 'create snapshot rule time_of_day on powerstore array name'\
                  ': {0} , global id : {1} failed with error {2}'.format(
                      self.cluster_name, self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def modify_snapshot_rule(self, snapshot_rule_id, new_name=None,
                             desired_retention=None, interval=None,
                             time_of_day=None, days_of_week=None):
        """modify an existing snapshot rule of a given PowerStore storage
        system"""

        try:
            LOG.info('Modifying an existing snapshot rule ')
            resp = self.protection.modify_snapshot_rule(
                snapshot_rule_id=snapshot_rule_id, name=new_name,
                desired_retention=desired_retention,
                interval=interval, time_of_day=time_of_day,
                days_of_week=days_of_week)

            LOG.info('Successfully modified snapshot rule id %s of powerstore'
                     ' array name : %s,global id : %s', snapshot_rule_id,
                     self.cluster_name, self.cluster_global_id)
            return True, resp

        except Exception as e:
            msg = 'Modify snapshot rule id: {0} on powerstore array ' \
                  'name: {1}, global id:{2} failed with error {3}'.format(
                      snapshot_rule_id, self.cluster_name,
                      self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def delete_snapshot_rule(self, snapshot_rule_id, delete_snaps=False):
        """delete a snapshot rule by id of a given PowerStore storage
         system"""

        try:
            LOG.info('deleting snapshot rule id %s', snapshot_rule_id)
            self.protection.delete_snapshot_rule(
                snapshot_rule_id=snapshot_rule_id,
                delete_snaps=delete_snaps)
            LOG.info('Successfully deleted snapshot rule id %s from'
                     ' powerstore array name : %s , global id : %s',
                     snapshot_rule_id, self.cluster_name,
                     self.cluster_global_id)
            return True

        except Exception as e:
            msg = 'delete snapshot rule id {0} for powerstore array name :' \
                  ' {1} , global id : {2} failed with error {3} '.format(
                      snapshot_rule_id, self.cluster_name,
                      self.cluster_global_id, str(e))
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

    def perform_module_operation(self):
        """collect input"""
        snap_rule_id = self.module.params['snapshotrule_id']
        name = self.module.params['name']
        new_name = self.module.params['new_name']
        days_of_week = self.module.params['days_of_week']
        interval = self.module.params['interval']
        time_of_day = self.module.params['time_of_day']
        desired_retention = self.module.params['desired_retention']
        delete_snaps = self.module.params['delete_snaps']
        state = self.module.params['state']

        result = dict(
            changed=False,
            snapshotrule_details=''
        )

        clusters = self.get_clusters()
        if len(clusters) > 0:
            self.cluster_name = clusters[0]['name']
            self.cluster_global_id = clusters[0]['id']
        else:
            msg = "Unable to find any active cluster on this array"
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        if not snap_rule_id and not name:
            msg = "Either snapshotrule_id or name is required"
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        changed, snap_rule = self.get_snapshot_rule_details(
            name,
            snap_rule_id)

        if snap_rule and not snap_rule_id:
            snap_rule_id = snap_rule['id']
        if snap_rule and not name:
            name = snap_rule['name']

        if not snap_rule and state == "present":

            if not desired_retention:
                msg = "desired_retention is required for this operation"
                LOG.error(msg)
                self.module.fail_json(msg=msg)
            if not interval and not time_of_day:
                msg = "To create a snapshot rule either 'interval' or '" \
                      "time_of_day' is required"
                LOG.error(msg)
                self.module.fail_json(msg=msg)

            if interval is not None:
                result['changed'], result['snapshotrule_details'] = self.\
                    create_snapshot_rule_by_interval(
                    name, interval, desired_retention, days_of_week)

            elif time_of_day is not None:
                result['changed'], result['snapshotrule_details'] = self. \
                    create_snapshot_rule_by_time_of_day(
                    name, desired_retention, time_of_day,
                    days_of_week)

            self.module.exit_json(**result)

        if snap_rule and state == "absent":

            result['changed'] = self.delete_snapshot_rule(
                snap_rule_id, delete_snaps)
            self.module.exit_json(**result)

        if snap_rule and state == "present":

            changed, snap_rule = self.get_snapshot_rule_details(
                id=snap_rule_id)

            # temporary fix until get clarification
            snap_rule['time_of_day'] = snap_rule['time_of_day'][0:5]\
                if snap_rule['time_of_day'] is not None else None

            name = new_name if new_name is not None else name

            new_snaprule_dict = {'name': name,
                                 'days_of_week': days_of_week,
                                 'interval': interval,
                                 'time_of_day': time_of_day,
                                 'desired_retention': desired_retention
                                 }

            to_modify = modify_snapshotrule_required(
                snap_rule, new_snaprule_dict)
            LOG.debug("ToModify : %s", to_modify)

            if to_modify:
                result['changed'], result['snapshotrule_details'] = \
                    self.modify_snapshot_rule(
                    snap_rule_id, new_name, desired_retention,
                    interval, time_of_day, days_of_week)
                self.module.exit_json(**result)
            else:
                ignore, result['snapshotrule_details'] = self.\
                    get_snapshot_rule_details(id=snap_rule_id)

        self.module.exit_json(**result)


def get_powerstore_snapshotrule_parameters():
    """This method provide the parameters required for the snapshot rule
     operations on PowerStore"""

    return dict(
        snapshotrule_id=dict(required=False, type='str'),
        name=dict(required=False, type='str'),
        new_name=dict(required=False, type='str'),
        days_of_week=dict(required=False, type='list', elements='str',
                          choices=['Monday', 'Tuesday', 'Wednesday',
                                   'Thursday', 'Friday', 'Saturday',
                                   'Sunday']),
        interval=dict(required=False, type='str', choices=['Five_Minutes',
                                                           'Fifteen_Minutes',
                                                           'Thirty_Minutes',
                                                           'One_Hour',
                                                           'Two_Hours',
                                                           'Three_Hours',
                                                           'Four_Hours',
                                                           'Six_Hours',
                                                           'Eight_Hours',
                                                           'Twelve_Hours',
                                                           'One_Day']),
        time_of_day=dict(required=False, type='str'),
        desired_retention=dict(required=False, type='int'),
        delete_snaps=dict(required=False, type='bool', default=False),
        state=dict(required=True, type='str', choices=['present', 'absent'])
    )


def modify_snapshotrule_required(snapruledict1, snapruledict2):
    """to compare two snapshot rule"""
    for key in snapruledict1.keys():
        if key in snapruledict2.keys() and snapruledict2[key] is not None and \
                ((isinstance(snapruledict1[key], list) and
                  set(snapruledict1[key]) != set(snapruledict2[key])) or
                 ((not isinstance(snapruledict1[key], list)) and (snapruledict1[key] != snapruledict2[key]))):
            LOG.debug("Key %s in snapruledict1=%s, snapruledict2=%s", key, snapruledict1[key], snapruledict2[key])
            return True
    return False


def main():
    """ Create PowerstoreSnapshotrule object and perform action on it
        based on user input from playbook """
    obj = PowerstoreSnapshotrule()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
