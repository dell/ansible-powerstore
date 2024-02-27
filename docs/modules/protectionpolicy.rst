.. _protectionpolicy_module:


protectionpolicy -- Perform Protection policy operations for PowerStore storage system
======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Performs all protection policy operations on PowerStore Storage System. This module supports create, modify, get and delete a protection policy.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.13 or later.
- PyPowerStore 3.1.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  name (optional, str, None)
    String variable. Indicates the name of the protection policy.


  protectionpolicy_id (optional, str, None)
    String variable. Indicates the id of the protection policy.


  new_name (optional, str, None)
    String variable. Indicates the new name of the protection policy.

    Used for renaming operation.


  snapshotrules (optional, list, None)
    List of strings to specify the name or ids of snapshot rules which are to be added or removed, to or from, the protection policy.


  replicationrule (optional, str, None)
    The name or ids of the replcation rule which is to be added to the protection policy.

    To remove the replication rule, an empty string has to be passed.


  description (optional, str, None)
    String variable. Indicates the description of the protection policy.


  state (True, str, None)
    String variable. Indicates the state of protection policy.

    For Delete operation only, it should be set to ``absent``.

    For all other operations like Create, Modify or Get details, it should be set to ``present``.


  snapshotrule_state (False, str, None)
    String variable. Indicates the state of a snapshotrule in a protection policy.

    When snapshot rules are specified, this variable is required.

    Value ``present-in-policy`` indicates to add to protection policy.

    Value ``absent-in-policy`` indicates to remove from protection policy.


  array_ip (True, str, None)
    IP or FQDN of the PowerStore management system.


  validate_certs (optional, bool, True)
    Boolean variable to specify whether to validate SSL certificate or not.

    ``true`` - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.

    ``false`` - indicates that the SSL certificate should not be verified.


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
   - Before deleting a protection policy, the replication rule has to be removed from the protection policy.
   - In PowerStore version 3.0.0.0, protection policy without snapshot rule/replication rule is not allowed.
   - The *check_mode* is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    

    - name: Create a protection policy with snapshot rule and replication rule
      dellemc.powerstore.protectionpolicy:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        name: "{{name}}"
        description: "{{description}}"
        snapshotrules:
          - "Ansible_test_snap_rule_1"
        replicationrule: "ansible_replication_rule_1"
        snapshotrule_state: "present-in-policy"
        state: "present"

    - name: Modify protection policy, change name
      dellemc.powerstore.protectionpolicy:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        name: "{{name}}"
        new_name: "{{new_name}}"
        state: "present"

    - name: Modify protection policy, add snapshot rule
      dellemc.powerstore.protectionpolicy:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        name: "{{name}}"
        snapshotrules:
          - "Ansible_test_snaprule_1"
        snapshotrule_state: "present-in-policy"
        state: "present"

    - name: Modify protection policy, remove snapshot rule, replication rule
      dellemc.powerstore.protectionpolicy:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        name: "{{name}}"
        snapshotrules:
          - "Ansible_test_to_be_removed"
        replicationrule: ""
        snapshotrule_state: "absent-in-policy"
        state: "present"

    - name: Get details of protection policy by name
      dellemc.powerstore.protectionpolicy:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        name: "{{name}}"
        state: "present"

    - name: Get details of protection policy by ID
      dellemc.powerstore.protectionpolicy:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        protectionpolicy_id: "{{protectionpolicy_id}}"
        state: "present"

    - name: Delete protection policy
      dellemc.powerstore.protectionpolicy:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        name: "{{name}}"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


protectionpolicy_details (When protection policy exists, complex, {'description': None, 'id': 'bce845ea-78ba-4414-ada1-8130f3a49e74', 'name': 'sample_protection_policy', 'replication_rules': [{'id': '7ec83605-bed4-4e2b-8405-504a614db318'}, {'name': 'sample_replication_rule'}], 'snapshot_rules': [], 'type': 'Protection'})
  Details of the protection policy.


  id (, str, )
    The system generated ID given to the protection policy.


  name (, str, )
    Name of the protection policy.


  description (, str, )
    description about the protection policy.


  type (, str, )
    The type for the protection policy.


  replication_rules (, complex, )
    The replication rule details of the protection policy.


    id (, str, )
      The replication rule ID of the protection policy.


    name (, str, )
      The replication rule name of the protection policy.



  snapshot_rules (, complex, )
    The snapshot rules details of the protection policy.


    id (, str, )
      The snapshot rule ID of the protection policy.


    name (, str, )
      The snapshot rule name of the protection policy.







Status
------





Authors
~~~~~~~

- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

