#!/usr/bin/python
# Copyright: (c) 2019, DellEMC

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils import dellemc_ansible_utils as utils
import logging

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r'''
---
module: dellemc_powerstore_snapshotrule
version_added: '2.6'
short_description: SnapshotRule operations on PowerStore storage system
description:
- Performs all snapshot rule opeations on PowerStore Storage System.
- This modules supports get details of an existing snapshot rule
  create new Snapshot Rule with Interval, create new Snapshot Rule
  with specific time and days_of_week with all supported
  parameters
- Modify Snapshot Rule with supported parameter
- Delete a specific Snapshot Rule etc.
extends_documentation_fragment:
  - dellemc.dellemc_powerstore
author:
- Arindam Datta (arindam.datta@dell.com)
options:
  name:
    description:
    - String variable, indicates the name of the Snapshot Rule
    required: False
  snapshotrule_id:
    description:
    - String variable, indicates the id of the Snapshot Rule
    required: False

  new_name:
    description:
    - String variable, indicates the new name of the Snapshot Rule
    - Used for renaming operation
    required: False
  days_of_week:
    description:
    - List of string to specify days of the week on which the rule 
      should be applied.
      Must be applied for rules where the 'time_of_day' parameter is set.
      Optional for the rule created with interval
      When 'days_of_week' is not specified for a new snapshot rule, the rule is
      applied on every day of the week.
    required: False
    choices: [ Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday ]
  interval:
    description :
    - String variable , indicates the interval between snapshots.
    - While creating a snapshot rule, specify either 'interval' or
      'time_of_day' (but not both)"
    required : False
    choices: [ Five_Minutes, Fifteen_Minutes, Thirty_Minutes, One_Hour,
    Two_Hours, Three_Hours, Four_Hours, Six_Hours, Eight_Hours, Twelve_Hours,
    One_Day ]
  desired_retention:
    description:
    - Integer variable, indicates desired snapshot retention period.
    - It is required when creating a new snapshot rule.
    required : False
  time_of_day:
    description:
    - String variable , indicates the time of the day to take a daily snapshot,
     with format "hh:mm" in 24 hour time format
    - While creating a snapshot rule, specify either 'interval' or
      'time_of_day' (but not both)"
    required : False
  delete_snaps:
    description:
    - Boolean variable to specify whether all snapshots previously created by
      this rule should also be deleted when this rule is removed.
    - True specifies to delete all previously created snapshots by this rule
      while deleting this rule.
    - False specifies to retain all previously created snapshots while deleting
      this rule
  state:
    description:
    - String variable indicates the state of Snapshot Rule.
    - Only for "delete" operation it should be set to "absent"
    - For all Create, Modify or Get details operation it should be set to
      "present"
    required : True
    choices: [ present, absent]

'''

EXAMPLES = r'''

- name: Get details of an existing snapshot rule by name
  dellemc_powerstore_snapshotrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    state: "present"

- name: Get details of an existing snapshot rule by id
  dellemc_powerstore_snapshotrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    snapshotrule_id: "{{snapshotrule_id}}"
    state: "present"

- name: Create new snapshot rule by interval
  dellemc_powerstore_snapshotrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    interval: "{{interval}}"
    days_of_week:
          - Monday
    desired_retention: "{{desired_retention}}"
    state: "present"


- name: Create new snapshot rule by time_of_day and days_of_week
  dellemc_powerstore_snapshotrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
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
  dellemc_powerstore_snapshotrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
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
  dellemc_powerstore_snapshotrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    interval: "{{interval}}"
    state: "present"

- name: Delete an existing snapshot rule by name
  dellemc_powerstore_snapshotrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    state: "absent"

'''

RETURN = r'''  '''


LOG = utils.get_logger(
    'dellemc_powerstore_snapshotrule',
    log_devel=logging.INFO)

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.0'

class PowerstoreSnapshotrule(object):
    """Snapshot Rule operations"""
    cluster_name = ' '
    cluster_global_id = ' '

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_snapshotrule_parameters())

        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True
        )
        LOG.info('HAS_PY4PS = {0} , IMPORT_ERROR = {1}'.format(
            HAS_PY4PS, IMPORT_ERROR))
        if HAS_PY4PS is False:
            self.module.fail_json(msg=IMPORT_ERROR)
        LOG.info('IS_SUPPORTED_PY4PS_VERSION = {0} , VERSION_ERROR = '
                 '{1}'.format(IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR))
        if IS_SUPPORTED_PY4PS_VERSION is False:
            self.module.fail_json(msg=VERSION_ERROR)

        self.conn = utils.get_powerstore_connection(self.module.params,
            application_type=APPLICATION_TYPE)
        self.provisioning = self.conn.provisioning
        LOG.info('Got Py4ps instance for provisioning on PowerStore {0}'.
                 format(self.provisioning))
        self.protection = self.conn.protection
        LOG.info('Got Py4ps instance for protection on PowerStore {0}'.
                 format(self.protection))

    def get_snapshot_rule_details(self, name=None, id=None):
        """Get snapshot rule details by name or id"""
        try:
            LOG.info('Getting the details of snapshot rule , Name:{0} ,'
                     ' ID:{1}'.format(name, id))
            if name:
                resp = self.protection.get_snapshot_rule_by_name(name)
                if resp and len(resp) > 0:
                    LOG.info(
                        'Successfully got the details of snapshot '
                        'rule name {0} from array name {1} and '
                        'glboal id {2}'.format(
                            name, self.cluster_name, self.cluster_global_id))
                    detail_resp = self.protection.get_snapshot_rule_details(
                        resp[0]['id'])
                    return False, detail_resp
            if id:
                detail_resp = self.protection.get_snapshot_rule_details(id)
                if detail_resp and len(detail_resp) > 0:
                    LOG.info('Successfully got the details of snapshot '
                             'rule id {0} from array name {1} and '
                             'glboal id {2}'.format(
                                 id, self.cluster_name,
                                 self.cluster_global_id))
                    return False, detail_resp

            msg = 'No snapshot rule present with name {0} or ID {1}'.format(
                name, id)
            LOG.debug(msg)
            return False, None

        except Exception as e:
            msg = 'Get details of snapshot rule name: {0} or ID {1} from ' \
                  'array name : {2} failed with error : {3} '.format(
                      name, id, self.cluster_name, str(e))
            LOG.error(msg)
            return False, None

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
            LOG.info(
                'Successfully created snapshot rule by interval , id: '
                '{0} on powerstore array name : {1} , global id : {2}'
                .format(resp.get("id"), self.cluster_name,
                        self.cluster_global_id))
            return True, res

        except Exception as e:
            msg = 'create snapshot rule by interval on powerstore array name' \
                  ': {0} , global id : {1} failed with error {2}'.format(
                      self.cluster_name, self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def create_snapshot_rule_by_time_of_day(self, name, desired_retention,
                                            time_of_day, days_of_week=None):
        """create snapshot rule by days_of_week and time_of_day """

        try:
            LOG.info('create snapshot rule by time_of_day ')
            resp = self.protection.create_snapshot_rule_by_time_of_day(
                name, desired_retention, time_of_day, days_of_week)
            result = self.protection.get_snapshot_rule_details(resp.get('id'))
            LOG.info(
                'Successfully created snapshot rule by by time_of_day {0}'
                'on powerstore array name : {1} ,global id : {2}'.format(
                    resp.get("id"), self.cluster_name, self.cluster_global_id))
            return True, result

        except Exception as e:
            msg = 'create snapshot rule time_of_day on powerstore array name' \
                  ': {0} , global id : {1} failed with error {2}'.format(
                      self.cluster_name, self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

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

            LOG.info(
                'Successfully modified snapshot rule id {0} of powerstore'
                'array name : {1},global id : {2}'.format(
                    snapshot_rule_id,
                    self.cluster_name,
                    self.cluster_global_id))
            return True, resp

        except Exception as e:
            msg = 'Modify snapshot rule id: {0} on powerstore array ' \
                  'name: {1}, global id:{2} failed with error {3}'.format(
                      snapshot_rule_id, self.cluster_name,
                      self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def delete_snapshot_rule(self, snapshot_rule_id, delete_snaps=False):
        """delete a snapshot rule by id of a given PowerStore storage system"""

        try:
            LOG.info('deleting snapshot rule id {0}'.format(snapshot_rule_id))
            self.protection.delete_snapshot_rule(
                snapshot_rule_id=snapshot_rule_id,
                delete_snaps=delete_snaps)
            LOG.info(
                'Successfully deleted snapshot rule id {0} from '
                'powerstore array name : {1} ,'
                ' global id : {2}'.format(
                    snapshot_rule_id,
                    self.cluster_name,
                    self.cluster_global_id))
            return True

        except Exception as e:
            msg = 'delete snapshot rule id {0} for powerstore array name :' \
                  ' {1} , global id : {2} failed with error {3} '.format(
                      snapshot_rule_id, self.cluster_name,
                      self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def modify_snapshotrule_required(self, snapruledict1, snapruledict2):
        """to compare two snapshot rule"""
        for key in snapruledict1.keys():
            if key in snapruledict2.keys():
                if snapruledict2[key] is not None:
                    if isinstance(snapruledict1[key], list):
                        if set(snapruledict1[key]) != set(snapruledict2[key]):
                            LOG.debug("Key {0} in snapruledict1={1},"
                                      "snapruledict2={2}".format(
                                key, snapruledict1[key], snapruledict2[key]))
                            return True
                    else:
                        if snapruledict1[key] != snapruledict2[key]:
                            LOG.debug("Key {0} in snapruledict1={1},"
                                      "snapruledict2={2}".format(
                                key,snapruledict1[key],snapruledict2[key]))
                            return True
        return False

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

        clusters = self.provisioning.get_cluster_list()
        if len(clusters) > 0:
            self.cluster_name = clusters[0]['name']
            self.cluster_global_id = clusters[0]['id']
        else:
            msg = "Unable to find any active cluster on this array"
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        if interval and time_of_day:
            msg = "Cannot have interval and time_of_day together"
            LOG.error(msg)
            self.module.fail_json(msg=msg)
        if snap_rule_id and name:
            msg = "Cannot have snaprule_id and name"
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

            # temporary fix untill get clarification
            snap_rule['time_of_day'] = snap_rule['time_of_day'][0:5]\
                if snap_rule['time_of_day'] is not None else None

            name = new_name if new_name is not None else name

            new_snaprule_dict = {'name': name,
                                 'days_of_week': days_of_week,
                                 'interval': interval,
                                 'time_of_day': time_of_day,
                                 'desired_retention': desired_retention
                                 }

            to_modify = self.modify_snapshotrule_required(
                snap_rule, new_snaprule_dict)
            LOG.debug("ToModify : {0}".format(to_modify))

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
        days_of_week=dict(required=False, type='list', choices=['Monday', 
            'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 
            'Sunday' ]),
        interval=dict(required=False, type='str', choices=['Five_Minutes', 
            'Fifteen_Minutes', 'Thirty_Minutes', 'One_Hour', 'Two_Hours',
            'Three_Hours', 'Four_Hours', 'Six_Hours', 'Eight_Hours', 
            'Twelve_Hours', 'One_Day']),
        time_of_day=dict(required=False, type='str'),
        desired_retention=dict(required=False, type='int'),
        delete_snaps=dict(required=False, type='bool'),
        state=dict(required=True, type='str', choices=['present', 
            'absent'])
    )


def main():
    """ Create PowerstoreSnapshotrule object and perform action on it
        based on user input from playbook """
    obj = PowerstoreSnapshotrule()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
