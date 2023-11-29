.. _snapshotrule_module:


snapshotrule -- Snapshot Rule operations on a PowerStore storage system
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Performs all snapshot rule operations on PowerStore Storage System.

This modules supports get details of a snapshot rule, create new Snapshot Rule with Interval, create new Snapshot Rule with specific time and days\_of\_week. Modify Snapshot Rule. Delete Snapshot Rule.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.14 or later.
- PyPowerStore 2.1.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  name (optional, str, None)
    String variable. Indicates the name of the Snapshot rule.


  snapshotrule_id (optional, str, None)
    String variable. Indicates the ID of the Snapshot rule.


  new_name (optional, str, None)
    String variable. Indicates the new name of the Snapshot rule.

    Used for renaming operation.


  days_of_week (optional, list, None)
    List of strings to specify days of the week on which the Snapshot rule should be applied. Must be applied for Snapshot rules where the \ :emphasis:`time\_of\_day`\  parameter is set.

    Optional for the Snapshot rule created with an interval. When \ :emphasis:`days\_of\_week`\  is not specified for a new Snapshot rule, the rule is applied on every day of the week.


  interval (False, str, None)
    String variable. Indicates the interval between Snapshots.

    When creating a Snapshot rule, specify either \ :emphasis:`interval`\  or \ :emphasis:`time\_of\_day`\ , but not both.


  desired_retention (False, int, None)
    Integer variable. Indicates the desired Snapshot retention period.

    It is required when creating a new Snapshot rule.


  time_of_day (False, str, None)
    String variable. Indicates the time of the day to take a daily Snapshot, with the format "hh:mm" in 24 hour time format.

    When creating a Snapshot rule, specify either \ :emphasis:`interval`\  or \ :emphasis:`time\_of\_day`\  but not both.


  delete_snaps (optional, bool, False)
    Boolean variable to specify whether all Snapshots previously created by this rule should also be deleted when this rule is removed.

    \ :literal:`true`\  specifies to delete all previously created Snapshots by this rule while deleting this rule.

    \ :literal:`false`\  specifies to retain all previously created Snapshots while deleting this rule.


  state (True, str, None)
    String variable indicates the state of Snapshot rule.

    For "Delete" operation only, it should be set to \ :literal:`absent`\ .

    For all Create, Modify or Get details operation it should be set to \ :literal:`present`\ .


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
   - The \ :emphasis:`check\_mode`\  is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
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



Return Values
-------------

changed (always, bool, true)
  Whether or not the resource has changed.


snapshotrule_details (When snapshot rule exists, complex, {'days_of_week': ['Sunday', 'Thursday'], 'desired_retention': 24, 'id': 'afa86b51-1171-498f-9786-2c78c33b4c14', 'interval': 'Five_Minutes', 'name': 'Sample_snapshot_rule', 'policies': [], 'time_of_day': None})
  Details of the snapshot rule.


  id (, str, )
    The system generated ID given to the snapshot rule.


  name (, str, )
    Name of the snapshot rule.


  days_of_week (, list, )
    List of string to specify days of the week on which the rule should be applied.


  time_of_day (, str, )
    The time of the day to take a daily snapshot.


  interval (, str, )
    The interval between snapshots.


  desired_retention (, int, )
    Desired snapshot retention period.


  policies (, complex, )
    The protection policies details of the snapshot rule.


    id (, str, )
      The protection policy ID in which the snapshot rule is selected.


    name (, str, )
      Name of the protection policy in which the snapshot rule is selected.







Status
------





Authors
~~~~~~~

- Arindam Datta (@dattaarindam) <ansible.team@dell.com>

