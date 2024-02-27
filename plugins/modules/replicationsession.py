#!/usr/bin/python
# Copyright: (c) 2024, Dell Technologies
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
  filesystem:
    description:
    - Name/ID of the filesystem for which replication session exists.
    - Parameter I(filesystem), I(nas_server), I(volume_group), I(volume),
      I(replication_group), and I(session_id) are mutually exclusive.
    type: str
  nas_server:
    description:
    - Name/ID of the NAS server for which replication session exists.
    - Parameter I(filesystem), I(nas_server), I(volume_group), I(volume),
      I(replication_group), and I(session_id) are mutually exclusive.
    type: str
  volume_group:
    description:
    - Name/ID of the volume group for which a replication session exists.
    - Parameter I(filesystem), I(nas_server), I(volume_group), I(volume),
      I(replication_group), and I(session_id) are mutually exclusive.
    type: str
  volume:
    description:
    - Name/ID of the volume for which replication session exists.
    - Parameter I(filesystem), I(nas_server), I(volume_group), I(volume),
      I(replication_group), and I(session_id) are mutually exclusive.
    type: str
  replication_group:
    description:
    - Name or ID of the replication group for which replication session exists.
    - Parameter I(filesystem), I(nas_server), I(volume_group), I(volume),
      I(replication_group), and I(session_id) are mutually exclusive.
    type: str
  session_id:
    description:
    - ID of the replication session.
    - Parameter I(filesystem), I(nas_server), I(volume_group), I(volume),
      I(replication_group), and I(session_id) are mutually exclusive.
    type: str
  session_state:
    description:
    - State in which the replication session is present after performing
      the task.
    choices: [ 'failed_over', 'paused', 'synchronizing']
    type: str
  role:
    description:
    - Role of the metro replication session.
    choices: ['Metro_Preferred', 'Metro_Non_Preferred']
    type: str
notes:
- Manual synchronization for a replication session is not supported through
  the Ansible module.
- When the current state of the replication session is 'OK' and in the
  playbook task C(synchronizing), then it will return "changed" as false.
- The changed as false in above scenario is because there is a scheduled
  synchronization in place with the associated replication rule's RPO in the
  protection policy.
- The I(check_mode) is not supported.
- Parameter I(nas_server), I(filesystem), I(replication_group), and I(role)
  parameters are supported only for PowerStore version 3.0.0. and above.
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

- name: Modify a replication session
  dellemc.powerstore.replicationsession:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    volume: "sample_volume_1"
    role: "Metro_Preferred"

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
APPLICATION_TYPE = 'Ansible/3.2.0'
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
                    |synchronizing          | resume or sync sdk calls
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
        mut_ex_args = [['volume', 'volume_group', 'session_id', 'nas_server'],
                       ['volume', 'volume_group', 'session_id', 'filesystem',
                        'replication_group']]
        required_one_of = [['volume', 'volume_group', 'session_id',
                            'filesystem', 'nas_server', 'replication_group']]
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
                                        vol=None, vol_grp=None,
                                        filesystem=None, nas_server=None,
                                        replication_group=None):
        """Get replication session details"""
        msg = 'Getting the details of replication session, with ' \
              'session_id:{0} or vol: {1}, vol_grp: {2}, filesystem: {3} or' \
              ' nas_server: {4} or replication group {5}'.\
            format(session_id, vol, vol_grp, filesystem, nas_server,
                   replication_group)
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
                local_resource_id = self.get_resource_id(
                    vol, vol_grp, filesystem, nas_server, replication_group)
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
                  'vol: {1}, vol_grp {2}, filesystem{3} or nas_server {4} or' \
                  ' replication group {5} failed with error : {6} '.\
                format(session_id, vol, vol_grp, filesystem, nas_server,
                       replication_group, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_nas_server(self, nas_server):
        """Get the details of NAS Server of a given Powerstore storage
        system"""

        try:
            msg = 'Getting NAS Server details {0}'.format(nas_server)
            LOG.info(msg)
            id_or_name = utils.name_or_id(val=nas_server)
            if id_or_name == "NAME":
                nas_details = self.provisioning.get_nas_server_by_name(
                    nas_server_name=nas_server)
                if nas_details:
                    nas_details = nas_details[0]['id']
            else:
                nas_details = self.provisioning.get_nas_server_details(
                    nas_server_id=nas_server)
                if nas_details:
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

    def get_resource_id(self, vol=None, vol_grp=None, filesystem=None,
                        nas_server=None, replication_group=None):
        """
        Get the local resource id from the input playbook task parameters.
        This ID is of either the volume or the volume group which has the
        replication session associated with it.
        """
        if vol:
            # when name of the volume is entered in vol parameter, then,
            # fetching the id of the volume by name.
            vol_id = self.get_volume_id(vol)
            if vol_id:
                return vol_id

        elif vol_grp:
            # when name of the volume group is entered in vol_grp parameter
            # ,then fetching the id of the volume group by name.
            vg_id = self.get_volume_group_id(vol_grp)
            if vg_id:
                return vg_id

        elif filesystem:
            # when name of the filesystem is entered in filesystem
            # parameter,then fetching the id of the filesystem by name.
            fs_id = self.get_filesystem_id(filesystem, nas_server)
            if fs_id:
                return fs_id

        elif replication_group:
            # when name of the replication group is entered in
            # replication_group parameter, then fetching the id of the
            # replication group by name.
            rep_grp_id = self.get_replication_group_id(replication_group)
            if rep_grp_id:
                return rep_grp_id

        else:
            # when name of the NAS server is entered in nas_server
            # parameter, then fetching the id of the NAS server by name.
            nas_id = self.get_nas_server_id(nas_server)
            if nas_id:
                return nas_id

    def get_volume_id(self, vol):
        """Get volume ID."""
        try:
            if utils.name_or_id(vol) == "NAME":
                vol_details = self.provisioning.get_volume_by_name(vol)
                msg = f"Volume details {vol_details} fetched by volume" \
                      f" name {vol}"
                LOG.info(msg)

                if not vol_details:
                    err_msg = f"Volume with name: {vol} not found. Please " \
                              f"enter a valid name of the volume."
                    self.module.fail_json(msg=err_msg)
                return vol_details[0]['id']

            # if ID is passed in vol parameter
            return vol
        except Exception as e:
            msg = f'Get local resource id for volume: {vol} failed with' \
                  f' error {str(e)} : '

            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_volume_group_id(self, vol_grp):
        """Get Volume group ID"""
        try:
            if utils.name_or_id(vol_grp) == "NAME":
                vol_grp_details = \
                    self.provisioning.get_volume_group_by_name(vol_grp)
                msg = f"Volume group details {vol_grp_details} fetched by" \
                      f" volume group name {vol_grp}"
                LOG.info(msg)

                if not vol_grp_details:
                    err_msg = f"Volume group with name: {vol_grp} not found." \
                              f" Please enter a valid name of the volume" \
                              f" group."
                    self.module.fail_json(msg=err_msg)
                return vol_grp_details[0]['id']
            # if ID is passed in vol parameter
            return vol_grp

        except Exception as e:
            msg = f'Get local resource id for volume group: {vol_grp} ' \
                  f'failed with error {str(e)} : '

            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_filesystem_id(self, filesystem, nas_server):
        """Get file system ID"""
        try:
            if utils.name_or_id(filesystem) == "NAME":
                nas_server = self.get_nas_server(nas_server)
                filesystem_details = \
                    self.provisioning.get_filesystem_by_name(filesystem,
                                                             nas_server)
                msg = f"Filesystem details {filesystem_details} fetched by" \
                      f" Filesystem name {filesystem}."
                LOG.info(msg)

                if not filesystem_details:
                    err_msg = f"Filesystem with name: {filesystem} not found" \
                              f". Please enter a valid name of the filesystem."
                    self.module.fail_json(msg=err_msg)
                return filesystem_details[0]['id']
            # if ID is passed in filesystem parameter
            return filesystem

        except Exception as e:
            msg = f'Get local resource id for filesystem: {filesystem}' \
                  f' failed with error {str(e)} : '

            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_nas_server_id(self, nas_server):
        """Get the NAS Server ID"""
        try:
            if utils.name_or_id(nas_server) == "NAME":
                nas_server_details = \
                    self.provisioning.get_nas_server_by_name(nas_server)
                msg = f"NAS server details {nas_server_details} fetched by" \
                      f" NAS server name {nas_server}"
                LOG.info(msg)

                if not nas_server_details:
                    err_msg = f"NAS server with name: {nas_server} not found" \
                              f". Please enter a valid name of the NAS server."
                    self.module.fail_json(msg=err_msg)
                return nas_server_details[0]['id']
            # if ID is passed in nas_server parameter
            return nas_server

        except Exception as e:
            msg = f'Get local resource id for nas server: {nas_server}' \
                  f' failed with error {str(e)} : '

            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_replication_group_id(self, replication_group):
        """Get the ID of the replication group."""
        try:
            if utils.name_or_id(replication_group) == "NAME":
                rpl_grp_details = self.protection.\
                    get_replication_group_details_by_name(replication_group)
                msg = f"Replication group details {rpl_grp_details} fetched" \
                      f" by replication group name {replication_group}"
                LOG.info(msg)

                if not rpl_grp_details:
                    err_msg = f"Replication group with name:" \
                              f" {replication_group} not found. Please enter" \
                              f" a valid name of the Replication group."
                    self.module.fail_json(msg=err_msg)
                return rpl_grp_details[0]['id']
            # if ID is passed in replication group parameter
            return replication_group

        except Exception as e:
            msg = f'Get local resource id for replication group:' \
                  f' {replication_group} failed with error {str(e)} : '
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
            session_type = rep_session_details['type']

            if session_state == 'synchronizing':
                # As the current state is paused so first the session has to be
                # resumed then it can be synced
                if session_type == "Metro_Active_Active":
                    self.protection.resume_replication_session(session_id)
                    return True
                elif role == "source":
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

    def modify_replication_session(self, session_id, role):
        """ Modify the role of the replication session"""
        try:
            self.protection.modify_replication_session(
                session_id=session_id, role=role)
            return True
        except Exception as e:
            err_msg = "Modifying the role {0} of replication session {1}" \
                      " failed with error {2}".format(role, session_id, str(e))
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg, **utils.failure_codes(e))

    def perform_module_operation(self):
        """collect input"""
        vol = self.module.params['volume']
        vol_grp = self.module.params['volume_group']
        filesystem = self.module.params['filesystem']
        nas_server = self.module.params['nas_server']
        replication_group = self.module.params['replication_group']
        session_id = self.module.params['session_id']
        session_state = self.module.params['session_state']
        role = self.module.params['role']
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
            session_id, vol, vol_grp, filesystem, nas_server,
            replication_group)

        if not rep_session_details:
            err_msg = "No replication session found with id {0}/ volume {1}/" \
                      " volume group{2}/ filesystem{3}/ NAS server{4} / " \
                      "Replication Group {5}.".format(session_id, vol, vol_grp,
                                                      filesystem, nas_server,
                                                      replication_group)
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

        transitioning_states = ['resuming', 'reprotecting', 'initializing',
                                'fractured', 'switching_to_metro_sync']
        if session_state and current_state in transitioning_states:
            self.change_state_from_transitioning_states(
                session_state, current_state)

        remaining_states = ['system_paused', 'paused_for_migration',
                            'paused_for_ndu', 'error',
                            'partial_cutover_for_migration ']
        if session_state and current_state in remaining_states:
            self.change_state_from_remaining_states(current_state)

        if rep_session_details and role is not None and \
                rep_session_details['role'] != role:
            changed = self.modify_replication_session(
                rep_session_details['id'], role)

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

            elif rep_session_details["resource_type"] == "volume":
                vol_details = self.provisioning.get_volume_details(res_id)
                rep_session_details['local_resource_name'] = \
                    vol_details['name']

            elif rep_session_details["resource_type"] == "filesystem":
                filesystem_details = self.provisioning.\
                    get_filesystem_details(res_id)
                rep_session_details['local_resource_name'] = \
                    filesystem_details['name']

            elif rep_session_details["resource_type"] == "nas_server":
                nas_server_details = self.provisioning.\
                    get_nas_server_details(res_id)
                rep_session_details['local_resource_name'] = \
                    nas_server_details['name']

            elif rep_session_details["resource_type"] == "replication_group":
                rep_group_details = self.protection.\
                    get_replication_group_details(res_id)
                rep_session_details['local_resource_name'] = \
                    rep_group_details['name']

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
        volume_group=dict(), volume=dict(), replication_group=dict(),
        filesystem=dict(), nas_server=dict(), session_id=dict(),
        session_state=dict(type='str', choices=['synchronizing', 'paused',
                                                'failed_over']),
        role=dict(
            required=False, type='str',
            choices=['Metro_Preferred', 'Metro_Non_Preferred'])
    )


def main():
    """ Create PowerStore replication session object and perform action on it
        based on user input from playbook """
    obj = PowerstoreReplicationSession()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
