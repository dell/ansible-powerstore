.. _replicationsession_module:


replicationsession -- Replication session operations on a PowerStore storage system
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Performs all replication session state change operations on a PowerStore Storage System.

This module supports get details of an existing replication session. Updating the state of the replication session.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.14 or later.
- PyPowerStore 2.1.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  filesystem (optional, str, None)
    Name/ID of the filesystem for which replication session exists.

    Parameter \ :emphasis:`filesystem`\ , \ :emphasis:`nas\_server`\ , \ :emphasis:`volume\_group`\ , \ :emphasis:`volume`\ , \ :emphasis:`replication\_group`\ , and \ :emphasis:`session\_id`\  are mutually exclusive.


  nas_server (optional, str, None)
    Name/ID of the NAS server for which replication session exists.

    Parameter \ :emphasis:`filesystem`\ , \ :emphasis:`nas\_server`\ , \ :emphasis:`volume\_group`\ , \ :emphasis:`volume`\ , \ :emphasis:`replication\_group`\ , and \ :emphasis:`session\_id`\  are mutually exclusive.


  volume_group (optional, str, None)
    Name/ID of the volume group for which a replication session exists.

    Parameter \ :emphasis:`filesystem`\ , \ :emphasis:`nas\_server`\ , \ :emphasis:`volume\_group`\ , \ :emphasis:`volume`\ , \ :emphasis:`replication\_group`\ , and \ :emphasis:`session\_id`\  are mutually exclusive.


  volume (optional, str, None)
    Name/ID of the volume for which replication session exists.

    Parameter \ :emphasis:`filesystem`\ , \ :emphasis:`nas\_server`\ , \ :emphasis:`volume\_group`\ , \ :emphasis:`volume`\ , \ :emphasis:`replication\_group`\ , and \ :emphasis:`session\_id`\  are mutually exclusive.


  replication_group (optional, str, None)
    Name or ID of the replication group for which replication session exists.

    Parameter \ :emphasis:`filesystem`\ , \ :emphasis:`nas\_server`\ , \ :emphasis:`volume\_group`\ , \ :emphasis:`volume`\ , \ :emphasis:`replication\_group`\ , and \ :emphasis:`session\_id`\  are mutually exclusive.


  session_id (optional, str, None)
    ID of the replication session.

    Parameter \ :emphasis:`filesystem`\ , \ :emphasis:`nas\_server`\ , \ :emphasis:`volume\_group`\ , \ :emphasis:`volume`\ , \ :emphasis:`replication\_group`\ , and \ :emphasis:`session\_id`\  are mutually exclusive.


  session_state (optional, str, None)
    State in which the replication session is present after performing the task.


  role (optional, str, None)
    Role of the metro replication session.


  array_ip (True, str, None)
    IP or FQDN of the PowerStore management system.


  validate_certs (optional, bool, True)
    Boolean variable to specify whether to validate SSL certificate or not.

    \ :literal:`true`\  - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS\_CA\_BUNDLE to the path of the SSL certificate.

    \ :literal:`false`\  - indicates that the SSL certificate should not be verified.


  user (True, str, None)
    The username of the PowerStore host.


  password (True, str, None)
    The password of the PowerStore host.


  timeout (optional, int, 120)
    Time after which the connection will get terminated.

    It is to be mentioned in seconds.


  port (optional, int, None)
    Port number for the PowerStore array.

    If not passed, it will take 443 as default.





Notes
-----

.. note::
   - Manual synchronization for a replication session is not supported through the Ansible module.
   - When the current state of the replication session is 'OK' and in the playbook task \ :literal:`synchronizing`\ , then it will return "changed" as false.
   - The changed as false in above scenario is because there is a scheduled synchronization in place with the associated replication rule's RPO in the protection policy.
   - The \ :emphasis:`check\_mode`\  is not supported.
   - Parameter \ :emphasis:`nas\_server`\ , \ :emphasis:`filesystem`\ , \ :emphasis:`replication\_group`\ , and \ :emphasis:`role`\  parameters are supported only for PowerStore version 3.0.0. and above.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
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



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


replication_session_details (When replication session exists, complex, {'estimated_completion_timestamp': None, 'id': 'b05b5108-26b6-4567-a1d8-1c7795b2e6bc', 'last_sync_timestamp': '2022-01-06T06:55:01.870946+00:00', 'local_resource_id': 'b0acb8de-446b-48e4-82ae-89ed05a35d01', 'local_resource_name': 'sample_volume', 'migration_session': None, 'progress_percentage': None, 'remote_resource_id': 'c1535ab7-e874-42eb-8692-7aa12aa4346e', 'remote_system': {'id': 'b5f62edd-f7aa-483a-afaa-4364ab6fcd3a', 'name': 'WN-D8989'}, 'remote_system_id': 'b5f62edd-f7aa-483a-afaa-4364ab6fcd3a', 'replication_rule': {'id': '05777d33-b2fb-4e65-8202-208ff4fe5878', 'name': 'sample_replication_rule'}, 'replication_rule_id': '05777d33-b2fb-4e65-8202-208ff4fe5878', 'resource_type': 'Volume', 'resource_type_l10n': 'Volume', 'role': 'Destination', 'role_l10n': 'Destination', 'state': 'Paused', 'state_l10n': 'Paused', 'storage_element_pairs': [{'local_storage_element_id': 'b0acb8de-446b-48e4-82ae-89ed05a35d01', 'remote_storage_element_id': 'c1535ab7-e874-42eb-8692-7aa12aa4346e', 'replication_shadow_id': None, 'storage_element_type': 'volume'}]})
  Details of the replication session.


  id (, str, )
    The system generated ID of the replication session. Unique across source and destination roles.


  name (, str, )
    Name of the replication rule.


  role (, str, )
    Role of the replication session. Source - The local resource is the source of the remote replication session. Destination - The local resource is the destination of the remote replication session.


  resource_type (, str, )
    Storage resource type eligible for replication protection. volume - Replication session created on a volume. volume\_group - Replication session created on a volume group.


  local_resource_id (, str, )
    Unique identifier of the local storage resource for the replication session.


  remote_resource_id (, str, )
    Unique identifier of the remote storage resource for the replication session.


  remote_system_id (, str, )
    Unique identifier of the remote system instance.


  progress_percentage (, int, )
    Progress of the current replication operation.


  replication_rule_id (, str, )
    Associated replication rule instance if created by policy engine.


  state (, str, )
    State of the replication session.


  last_sync_timestamp (, str, )
    Time of last successful synchronization.


  estimated_completion_timestamp (, str, )
    Estimated completion time of the current replication operation.






Status
------





Authors
~~~~~~~

- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

