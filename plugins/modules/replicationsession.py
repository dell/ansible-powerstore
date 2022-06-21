#!/usr/bin/python
# Copyright: (c) 2021, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: replicationsession
version_added: '1.2.0'
short_description: Replication session operations on a PowerStore storage
                   system
description:
- Performs all replication session state change operations on a PowerStore
  Storage System.
- This module supports get details of an existing replication session.
  Updating the state of the replication session.
extends_documentation_fragment:
  - dellemc.powerstore.powerstore
author:
- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>
options:
  volume_group:
    description:
    - Name/ID of the volume group for which a replication session exists.
    - Parameter volume_group, volume, and session_id are mutually exclusive.
    required: False
    type: str
  volume:
    description:
    - Name/ID of the volume for which replication session exists.
    - Parameter volume_group, volume, and session_id are mutually exclusive.
    required: False
    type: str
  session_id:
    description:
    - ID of the replication session.
    - Parameter volume_group, volume, and session_id are mutually exclusive.
    required: False
    type: str
  session_state:
    description:
    - State in which the replication session is present after performing
      the task.
    required: False
    choices: [ 'failed_over', 'paused', 'synchronizing']
    type: str
notes:
- Manual synchronization for a replication session is not supported through
  the Ansible module.
- When the current state of the replication session is 'OK' and in the
  playbook task 'synchronizing', then it will return "changed" as False.
- The changed as False in above scenario is because of there is a scheduled
  synchronization in place with the associated replication rule's RPO in the
  protection policy.
- The check_mode is not supported.
'''

EXAMPLES = r'''

- name: Pause a replication session
  dellemc.powerstore.replicationsession:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    volume: "sample_volume_1"
    session_state: "paused"

- name: Synchronize a replication session
  dellemc.powerstore.replicationsession:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    volume: "sample_volume_1"
    session_state: "synchronizing"

- name: Get details of a replication session
  dellemc.powerstore.replicationsession:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    volume: "sample_volume_1"

- name: Fail over a replication session
  dellemc.powerstore.replicationsession:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    volume: "sample_volume_1"
    session_state: "failed_over"
'''

RETURN = r'''

changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"

replication_session_details:
    description: Details of the replication session.
    returned: When replication session exists
    type: complex
    contains:
        id:
            description: The system generated ID of the replication session.
                         Unique across source and destination roles.
            type: str
        name:
            description: Name of the replication rule.
            type: str
        role:
            description: Role of the replication session. Source - The local
                         resource is the source of the remote replication
                         session. Destination - The local resource is the
                         destination of the remote replication session.
            type: str
        resource_type:
            description: Storage resource type eligible for replication
                         protection. volume - Replication session created on a
                         volume. volume_group - Replication session created on
                         a volume group.
            type: str
        local_resource_id:
            description: Unique identifier of the local storage resource for
                         the replication session.
            type: str
        remote_resource_id:
            description: Unique identifier of the remote storage resource for
                         the replication session.
            type: str
        remote_system_id:
            description: Unique identifier of the remote system instance.
            type: str
        progress_percentage:
            description: Progress of the current replication operation.
            type: int
        replication_rule_id:
            description: Associated replication rule instance if created by
                         policy engine.
            type: str
        state:
            description: State of the replication session.
            type: str
        last_sync_timestamp:
            description: Time of last successful synchronization.
            type: str
        estimated_completion_timestamp:
            description: Estimated completion time of the current replication
                         operation.
            type: str
    sample: {
        "estimated_completion_timestamp": null,
        "id": "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
        "last_sync_timestamp": "2022-01-06T06:55:01.870946+00:00",
        "local_resource_id": "b0acb8de-446b-48e4-82ae-89ed05a35d01",
        "local_resource_name": "sample_volume",
        "migration_session": null,
        "progress_percentage": null,
        "remote_resource_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
        "remote_system": {
            "id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
            "name": "WN-D8989"
        },
        "remote_system_id": "b5f62edd-f7aa-483a-afaa-4364ab6fcd3a",
        "replication_rule": {
            "id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
            "name": "sample_replication_rule"
        },
        "replication_rule_id": "05777d33-b2fb-4e65-8202-208ff4fe5878",
        "resource_type": "Volume",
        "resource_type_l10n": "Volume",
        "role": "Destination",
        "role_l10n": "Destination",
        "state": "Paused",
        "state_l10n": "Paused",
        "storage_element_pairs": [
            {
                "local_storage_element_id": "b0acb8de-446b-48e4-82ae-89ed05a35d01",
                "remote_storage_element_id": "c1535ab7-e874-42eb-8692-7aa12aa4346e",
                "replication_shadow_id": null,
                "storage_element_type": "volume"
            }
        ]
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

LOG = utils.get_logger('replicationsession')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.6.0'
"""
===============================================================================
Idempotency table for the replication session ansible module on the basis of
the current state of the session on the PowerStore array.
===============================================================================
current_state       | playbook task         | intended operation/
of the session      | session_state         | idempotency
-------------------------------------------------------------------------------
                    | synchronizing         | idempotency case
ok                  | paused                | issue a pause sdk call
                    | failed_over           | issue a failed_over sdk call
-------------------------------------------------------------------------------
                    |synchronizing          | idempotency case
synchronizing       |paused                 | issue a pause sdk call
                    |failed_over            | issue a failed_over sdk call
-------------------------------------------------------------------------------
                    |synchronizing          | resume and sync sdk calls
paused              |paused                 | idempotency case
                    |failed_over            | issue a failed_over sdk call
-------------------------------------------------------------------------------
                    |synchronizing          | reprotect and sync sdk calls at
                    |                       | new source or error at new
failed_over         |                       | destination.
                    |paused                 | error
                    |failed_over            | idempotency case
-------------------------------------------------------------------------------
                    |synchronizing          | invalid transition/ error
failing_over,       |paused                 | invalid transition/ error
failing_over_for_dr |failed_over            | idempotency case
-------------------------------------------------------------------------------
initializing,       |synchronizing          | invalid transition/ error
resuming,           |paused                 | invalid transition/ error
reprotecting,       |failed_over            | invalid transition/ error
system_paused,      |                       |
paused_for_migration|                       |
paused_for_ndu,     |                       |
partial_cutover_for_migration,|             |
-------------------------------------------------------------------------------
error               |synchronizing/pause/   | error
                    |failed_over            |
-------------------------------------------------------------------------------

"""


class PowerstoreReplicationSession(object):
    """Replication Session operations"""
    cluster_name = ' '
    cluster_global_id = ' '

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_rep_session_parameters())

        # initialize the Ansible module
        mut_ex_args = [['volume', 'volume_group', 'session_id']]
        required_one_of = [['volume', 'volume_group', 'session_id']]
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mut_ex_args,
            required_one_of=required_one_of
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

    def get_replication_session_details(self, session_id=None,
                                        vol=None, vol_grp=None):
        """Get replication session details"""
        msg = 'Getting the details of replication session, with ' \
              'session_id:{0} or vol: ' \
              '{1} or vol_grp: {2}'.format(session_id, vol, vol_grp)
        LOG.info(msg)
        try:
            if session_id:
                session_details = \
                    self.protection.get_replication_session_details(session_id)
                if not session_details:
                    msg = 'No replication session present with ID {0} '.format(
                        session_id)
                    LOG.info(msg)
                    self.module.fail_json(msg=msg)

                msg = 'Successfully got the details of replication ' \
                      'session with id: {0}'.format(session_id)
                LOG.info(msg)

            else:
                local_resource_id = self.get_vol_or_vol_grp_id(vol, vol_grp)
                filter_dict = {'local_resource_id': "eq." + local_resource_id}
                # Get replication session returns the list of replication
                # session ids
                sessions_list = self.protection.get_replication_sessions(
                    filter_dict=filter_dict, all_pages=True)
                err_msg = "No replication session found for the local " \
                          "resource with ID: {0}".format(local_resource_id)
                if not sessions_list:
                    self.module.fail_json(msg=err_msg)
                # Getting the replication session details using the fetched
                # session id
                session_id = sessions_list[0]['id']
                session_details = \
                    self.protection.get_replication_session_details(session_id)
                msg = 'Successfully got the details of replication ' \
                      'session with local resource' \
                      ' id: {0}'.format(local_resource_id)
                LOG.info(msg)

            return session_details

        except Exception as e:
            msg = 'Get details of replication session with ID: {0} or ' \
                  'vol: {1} or vol_grp {2} on failed with error : ' \
                  '{3} '.format(session_id, vol, vol_grp, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_vol_or_vol_grp_id(self, vol=None, vol_grp=None):
        """
        Get the local resource id from the input playbook task parameters.
        This ID is of either the volume or the volume group which has the
        replication session associated with it.
        """
        try:
            if vol:
                # when name of the volume is entered in vol parameter, then,
                # fetching the id of the volume by name.
                if utils.name_or_id(vol) == "NAME":
                    vol_details = self.provisioning.get_volume_by_name(vol)
                    msg = "Volume details {0} fetched by volume name" \
                          " {1}".format(str(vol_details), vol)
                    LOG.info(msg)

                    if not vol_details:
                        err_msg = "Volume with name: {0} not found. Please " \
                                  "enter a valid name of the " \
                                  "volume.".format(vol)
                        self.module.fail_json(msg=err_msg)
                    return vol_details[0]['id']

                # if ID is passed in vol parameter
                return vol

            else:
                # when name of the volume group is entered in vol_grp parameter
                # ,then fetching the id of the volume group by name.
                if utils.name_or_id(vol_grp) == "NAME":
                    vol_grp_details = \
                        self.provisioning.get_volume_group_by_name(vol_grp)
                    msg = "Volume group details {0} fetched by volume group" \
                          " name {1}".format(str(vol_grp_details), vol_grp)
                    LOG.info(msg)

                    if not vol_grp_details:
                        err_msg = "Volume group with name: {0} not found. " \
                                  "Please enter a valid name of the volume" \
                                  " group.".format(vol_grp)
                        self.module.fail_json(msg=err_msg)
                    return vol_grp_details[0]['id']

                # if ID is passed in vol parameter
                return vol_grp

        except Exception as e:
            msg = 'Get local resource id for volume: {0} or ' \
                  'volume group {1} on failed with error : ' \
                  '{2} '.format(vol, vol_grp, str(e))

            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None

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

    def change_state_from_ok(self, session_state, current_state,
                             rep_session_details, err_msg):
        """
        The operation will be performed when the current state of the
        replication session is OK.
        """
        try:
            session_id = rep_session_details['id']
            role = rep_session_details['role'].lower()
            if session_state == 'synchronizing':
                return False

            if session_state == "paused":
                self.protection.pause_replication_session(session_id)
                return True

            if session_state == "failed_over":
                # At source only planned fail over can be done
                if role == "source":
                    self.protection.failover_replication_session(session_id)
                    return True
                # At destination unplanned fail over takes place
                if role == "destination":
                    self.protection.failover_replication_session(
                        session_id, is_planned=False)
                    return True

        except Exception as e:
            err_msg = err_msg.format(session_state, rep_session_details['id'],
                                     current_state, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(err_msg)
                return None
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg, **utils.failure_codes(e))

    def change_state_from_sync(self, session_state, current_state,
                               rep_session_details, err_msg):
        """
        The operation will be performed when the current state of the
        replication session is synchronizing.
        """
        try:
            session_id = rep_session_details['id']
            role = rep_session_details['role'].lower()

            if session_state == 'synchronizing':
                if role == "destination":
                    self.module.fail_json(msg="Sync call can be performed only"
                                              " on source. The current system "
                                              "is destination")
                # current state and session state are same and role is source
                # so idempotency case.
                return False

            if session_state == "paused":
                self.protection.pause_replication_session(session_id)
                return True

            if session_state == "failed_over":
                # At source only planned fail over can be done
                if role == "source":
                    self.protection.failover_replication_session(session_id)
                    return True
                # At destination unplanned fail over takes place
                if role == "destination":
                    self.protection.failover_replication_session(
                        session_id, is_planned=False)
                    return True

        except Exception as e:
            err_msg = err_msg.format(session_state, rep_session_details['id'],
                                     current_state, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(err_msg)
                return None
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg, **utils.failure_codes(e))

    def change_state_from_paused(self, session_state, current_state,
                                 rep_session_details, err_msg):
        """
            The operation will be performed when the current state of the
            replication session is paused.
        """
        try:
            session_id = rep_session_details['id']
            role = rep_session_details['role'].lower()

            if session_state == 'synchronizing':
                # As the current state is paused so first the session has to be
                # resumed then it can be synced
                if role == "source":
                    self.protection.resume_replication_session(session_id)
                    self.protection.sync_replication_session(session_id)
                    return True
                # when role is destination
                self.module.fail_json(msg="Synchronization at destination is"
                                          " not supported. Please synchronize "
                                          "at source")

            # Current state is paused and entered session state is also same
            # so it will be considered as idempotency case
            if session_state == "paused":
                return False

            # First session will be resumed then depending on the role
            # (source/destination) planned or unplanned failover will
            # be performed
            if session_state == "failed_over":

                self.protection.resume_replication_session(session_id)
                # At source only planned fail over can be done
                if role == "source":
                    self.protection.failover_replication_session(session_id)
                    return True
                # At destination unplanned fail over takes place
                if role == "destination":
                    self.protection.failover_replication_session(
                        session_id, is_planned=False)
                    return True

        except Exception as e:
            err_msg = err_msg.format(session_state, rep_session_details['id'],
                                     current_state, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(err_msg)
                return None
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg, **utils.failure_codes(e))

    def change_state_from_failing_over(self, session_state, current_state,
                                       rep_session_details, err_msg):
        """
            The operation will be performed when the current state of the
            replication session is failing_over.
        """
        try:
            session_id = rep_session_details['id']

            if session_state == 'synchronizing':
                # As the current state is failing_over so during failing over
                # of the session, sync call will throw an exception mentioning
                # this an invalid transition.
                self.protection.sync_replication_session(session_id)

            if session_state == "paused":
                # As the current state is failing_over so during failing over
                # of the session, pause call will throw an exception mentioning
                # this an invalid transition.
                self.protection.pause_replication_session(session_id)

            if session_state == "failed_over":
                return False

        except Exception as e:
            err_msg = err_msg.format(session_state, rep_session_details['id'],
                                     current_state, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(err_msg)
                return None
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg, **utils.failure_codes(e))

    def change_state_from_failed_over(self, session_state, current_state,
                                      rep_session_details, err_msg):

        """
        The operation will be performed when the current state of the
        replication session is failed_over.
        """
        try:
            session_id = rep_session_details['id']
            role = rep_session_details['role'].lower()

            if session_state == 'synchronizing':
                # As the current state is failed_over so first the session
                # has to be reprotected then it can be synced
                if role == "source":

                    self.protection.reprotect_replication_session(session_id)
                    self.protection.sync_replication_session(session_id)
                    return True
                if role == "destination":
                    self.module.fail_json(msg="Sync call can not be made at "
                                              "the destination when the "
                                              "session is in failed_over "
                                              "state")

            # Current state is failed_over and entered session state is paused.
            # This is an invalid transition
            if session_state == "paused":
                self.module.fail_json(msg="replication session is in "
                                          "failed_over state, invalid "
                                          "transition to paused state. ")

            if session_state == "failed_over":
                # At source only only reprotect can be done and as failed_over
                # is passed in session_state by user so it will be treated
                # as idempotency
                if role == "source":
                    return False
                # At destination unplanned forced fail over cannot be done.
                # Hence will be idempotency case.
                if role == "destination":
                    return False

        except Exception as e:
            err_msg = err_msg.format(session_state, rep_session_details['id'],
                                     current_state, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(err_msg)
                return None
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg, **utils.failure_codes(e))

    def change_state_from_transitioning_states(self, session_state,
                                               current_state):
        """
        The operation will be performed when the current state of the
        replication session is resuming/initializing/reprotecting.
        """
        err_msg = "Replication Session is in {0} state. " \
                  "Please perform {1} operation once this transition is" \
                  " completed.".format(current_state, session_state)
        self.module.fail_json(msg=err_msg)

    def change_state_from_remaining_states(self, current_state):
        """
        The operation will be performed when the current state of the
        replication session is system_paused/ paused_for_migration/
        paused_for_ndu'/partial_cutover_for_migration/error.
        """
        err_msg = "Replication Session is in {0} state. " \
                  "Any state change from this state is not supported by" \
                  " ansible module.".format(current_state)
        self.module.fail_json(msg=err_msg)

    def perform_module_operation(self):
        """collect input"""
        vol = self.module.params['volume']
        vol_grp = self.module.params['volume_group']
        session_id = self.module.params['session_id']
        session_state = self.module.params['session_state']
        result = dict()
        changed = False

        # Get the cluster details
        clusters = self.get_clusters()
        if len(clusters) > 0:
            self.cluster_name = clusters[0]['name']
            self.cluster_global_id = clusters[0]['id']
        else:
            msg = "Unable to find any active cluster on this array"
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        # Get the replication session details.
        rep_session_details = self.get_replication_session_details(
            session_id, vol, vol_grp)

        if not rep_session_details:
            err_msg = "No replication session found with id {0}/ volume {1}/" \
                      " volume group{2}.".format(session_id, vol, vol_grp)
            self.module.fail_json(msg=err_msg)
        if not session_id:
            session_id = rep_session_details['id']

        current_state = rep_session_details['state'].lower()
        err_msg = None
        if current_state and session_state:
            msg = "Current state of the replication session: {0} and entered" \
                  " session state: {1}".format(current_state, session_state)
            LOG.info(msg)
            err_msg = '{0} call on replication session with id: {1} having'\
                      ' current state: {2}, failed with error: {3}'
        # perform operation for the given session state parameter in playbook
        # task, if current replication state is OK
        if session_state and current_state == "ok":
            changed = self.change_state_from_ok(
                session_state, current_state, rep_session_details, err_msg)

        # perform operation for the given session state parameter in playbook
        # task, if current replication state is synchronizing
        if session_state and current_state == "synchronizing":
            changed = self.change_state_from_sync(session_state, current_state,
                                                  rep_session_details, err_msg)

        # perform operation for the given session state parameter in playbook
        # task, if current replication state is paused
        if session_state and current_state == "paused":
            changed = self.change_state_from_paused(
                session_state, current_state, rep_session_details, err_msg)

        # perform operation for the given session state parameter in playbook
        # task, if current replication state is failed_over
        if session_state and current_state == "failed_over":
            changed = self.change_state_from_failed_over(
                session_state, current_state, rep_session_details, err_msg)

        # perform operation for the given session state parameter in playbook
        # task, if current replication state is failing_over
        if session_state and current_state == "failing_over" or \
                current_state == "failing_over_for_dr":
            changed = self.change_state_from_failing_over(
                session_state, current_state, rep_session_details, err_msg)

        transitioning_states = ['resuming', 'reprotecting', 'initializing']
        if session_state and current_state in transitioning_states:
            self.change_state_from_transitioning_states(
                session_state, current_state)

        remaining_states = ['system_paused', 'paused_for_migration',
                            'paused_for_ndu', 'error',
                            'partial_cutover_for_migration ']
        if session_state and current_state in remaining_states:
            self.change_state_from_remaining_states(current_state)

        result['changed'] = changed
        result['replication_session_details'] = self.show_output(session_id)
        self.module.exit_json(**result)

    def show_output(self, session_id):
        """
        Adding the additional information in the replication session
        details
        """
        try:
            LOG.info("Getting details of replication session to "
                     "show in output.")
            rep_session_details = self.get_replication_session_details(
                session_id=session_id)

            res_id = rep_session_details['local_resource_id']
            if rep_session_details["resource_type"] == "volume_group":
                vg_details = self.provisioning.get_volume_group_details(res_id)
                rep_session_details['local_resource_name'] = \
                    vg_details['name']

            if rep_session_details["resource_type"] == "volume":
                vol_details = self.provisioning.get_volume_details(res_id)
                rep_session_details['local_resource_name'] = \
                    vol_details['name']
            return rep_session_details

        except Exception as e:
            msg = 'Show replication session details failed with' \
                  ' error: {0}'.format(str(e))

            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))


def get_powerstore_rep_session_parameters():
    """This method provides the parameters required for the replication session
     operations for PowerStore"""

    return dict(
        volume_group=dict(), volume=dict(),
        session_id=dict(),
        session_state=dict(type='str', choices=['synchronizing', 'paused',
                                                'failed_over'])
    )


def main():
    """ Create PowerStore replication session object and perform action on it
        based on user input from playbook """
    obj = PowerstoreReplicationSession()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
