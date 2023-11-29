.. _quota_module:


quota -- Manage Tree Quotas and User Quotas on PowerStore
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing  Quotas on PowerStore storage system includes getting details, modifying, creating and deleting Quotas.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.14 or later.
- PyPowerStore 2.1.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  path (optional, str, None)
    The path on which the quota will be imposed.

    Path is relative to the root of the filesystem.

    For user quota, if \ :emphasis:`path`\  is not specified, quota will be created at the root of the filesystem.


  quota_type (optional, str, None)
    The type of quota which will be imposed.


  quota_id (optional, str, None)
    Id of the user/tree quota.

    If \ :emphasis:`quota\_id`\  is mentioned, then \ :emphasis:`path`\ /\ :emphasis:`nas\_server`\ /\ :emphasis:`file\_system`\ /\ :emphasis:`quota\_type`\  is not required.


  filesystem (optional, str, None)
    The ID/Name of the filesystem for which the Tree/User Quota  will be created.

    If filesystem name is specified, then \ :emphasis:`nas\_server`\  is required to uniquely identify the filesystem.


  nas_server (optional, str, None)
    The NAS server. This could be the name or ID of the NAS server.


  description (optional, str, None)
    Additional information that can be mentioned for a Tree Quota.

    Description parameter can only be used when \ :emphasis:`quota\_type`\  is \ :literal:`tree`\ .


  unix_name (optional, str, None)
    The name of the unix user account for which quota operations will be performed.

    Any one among \ :literal:`uid`\ /\ :literal:`unix\_name`\ /\ :literal:`windows\_name`\ /\ :literal:`windows\_sid`\  is required when \ :emphasis:`quota\_type`\  is \ :literal:`user`\ .


  windows_name (optional, str, None)
    The name of the Windows User for which quota operations will be performed.

    The name should be mentioned along with Domain Name as 'DOMAIN\_NAME\\user\_name' or as "DOMAIN\_NAME\\\\user\_name".

    Any one among \ :literal:`uid`\ /\ :literal:`unix\_name`\ /\ :literal:`windows\_name`\ /\ :literal:`windows\_sid`\  is required when \ :emphasis:`quota\_type`\  is \ :literal:`user`\ .


  uid (optional, int, None)
    The ID of the unix user account for which quota operations will be performed.

    Any one among \ :literal:`uid`\ /\ :literal:`unix\_name`\ /\ :literal:`windows\_name`\ /\ :literal:`windows\_sid`\  is required when \ :emphasis:`quota\_type`\  is \ :literal:`user`\ .


  windows_sid (optional, str, None)
    The SID of the Windows User account for which quota operations will be performed.

    Any one among \ :literal:`uid`\ /\ :literal:`unix\_name`\ /\ :literal:`windows\_name`\ /\ :literal:`windows\_sid`\  is required when \ :emphasis:`quota\_type`\  is \ :literal:`user`\ .


  quota (optional, dict, None)
    Specifies Quota parameters.


    soft_limit (optional, int, None)
      Soft limit of the User/Tree quota.

      No Soft limit when set to \ :literal:`0`\ .


    hard_limit (optional, int, None)
      Hard limit of the user quota.

      No hard limit when set to \ :literal:`0`\ .


    cap_unit (optional, str, GB)
      Unit of storage for the hard and soft limits.

      This parameter is required if limit is specified.



  state (True, str, None)
    Define whether the Quota should exist or not.

    Value \ :literal:`present`\   indicates that the Quota should exist on the system.

    Value \ :literal:`absent`\   indicates that the Quota should not exist on the system.


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
   - Tree quota cannot be created at the root of the filesystem.
   - When the ID of the filesystem is passed then \ :emphasis:`nas\_server`\  is not required. If passed, then filesystem should exist for the \ :emphasis:`nas\_server`\ , else the task will fail.
   - If a primary directory of the current directory or a subordinate directory of the path is having a Tree Quota configured, then the quota for that path cannot be created.
   - Hierarchical tree quotas are not allowed.
   - When the first quota is created for a directory/user in a filesystem then the quotas will be enabled for that filesystem automatically.
   - If a user quota is to be created on a tree quota, then the user quotas will be enabled automatically in a tree quota.
   - \ :literal:`Delete`\  User Quota operation is not supported.
   - The \ :emphasis:`check\_mode`\  is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create a Quota for a User using unix name
      dellemc.powerstore.quota:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
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
      dellemc.powerstore.quota:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
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
      dellemc.powerstore.quota:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        quota_id: "{{quota_id}}"
        quota:
          soft_limit: 10
          hard_limit: 15
          cap_unit: "TB"
        state: "present"

    - name: Get details of User Quota
      dellemc.powerstore.quota:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        quota_type: "user"
        uid: 100
        path: "/home"
        filesystem: "{{filesystem_id}}"
        state: "present"

    - name: Get details of Tree Quota
      dellemc.powerstore.quota:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        quota_id: "{{quota_id}}"
        state: "present"

    - name: Delete a Tree Quota
      dellemc.powerstore.quota:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        quota_type: "tree"
        path: "/home"
        filesystem: "sample_fs"
        nas_server: "sample_nas_server"
        state: "absent"



Return Values
-------------

changed (always, bool, true)
  Whether or not the resource has changed.


quota_details (When Quota exists., complex, {'description': 'Tree quota created on filesystem', 'file_system': {'filesystem_type': 'Primary', 'id': '61d68a87-6000-3cc3-f816-96e8abdcbab0', 'name': 'sample_file_system', 'nas_server': {'id': '60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9', 'name': 'ansible_nas_server_2'}}, 'hard_limit(GB)': '90.0', 'id': '00000006-08f2-0000-0200-000000000000', 'is_user_quotas_enforced': False, 'path': '/sample_file_system', 'remaining_grace_period': -1, 'size_used': 0, 'soft_limit(GB)': '50.0', 'state': 'Ok'})
  The quota details.


  id (, str, 2nQKAAEAAAAAAAAAAAAAQIMCAAAAAAAA)
    The ID of the Quota.


  file_system (, complex, )
    Includes ID and Name of filesystem and nas server for which smb share exists.


    filesystem_type (, str, Primary)
      Type of filesystem.


    id (, str, 5f73f516-e67b-b179-8901-72114981c1f3)
      ID of filesystem.


    name (, str, sample_filesystem)
      Name of filesystem.


    nas_server (, dict, )
      nas\_server of filesystem.



  hard_limit(cap_unit) (, int, 4.0)
    Value of the Hard Limit imposed on the quota.


  soft_limit(cap_unit) (, int, 2.0)
    Value of the Soft Limit imposed on the quota.


  remaining_grace_period (, int, 86400)
    The time period remaining after which the grace period will expire.


  description (, str, Sample Tree quota's description)
    Additional information about the tree quota. Only applicable for Tree Quotas.


  uid (, int, )
    The ID of the unix host for which user quota exists. Only applicable for user quotas.


  unix_name (, str, )
    The Name of the unix host for which user quota exists. Only applicable for user quotas.


  windows_name (, str, )
    The Name of the Windows host for which user quota exists. Only applicable for user quotas.


  windows_sid (, str, )
    The SID of the windows host for which user quota exists. Only applicable for user quotas.


  tree_quota_id (, str, )
    ID of the Tree Quota on which the specific User Quota exists. Only applicable for user quotas.


  tree_quota_for_user_quota (, complex, )
    Additional Information of Tree Quota limits on which user quota exists. Only applicable for User Quotas.


    description (, str, Primary)
      Description of Tree Quota for user quota.


    hard_limit(cap_unit) (, int, 2.0)
      Value of the Hard Limit imposed on the quota.


    path (, str, /sample_path)
      The path on which the quota will be imposed.



  size_used (, int, )
    Size currently consumed by Tree/User on the filesystem.


  state (, str, Ok)
    State of the user quota or tree quota record period. OK means No quota limits are exceeded. Soft\_Exceeded means Soft limit is exceeded, and grace period is not expired. Soft\_Exceeded\_And\_Expired means Soft limit is exceeded, and grace period is expired. Hard\_Reached means Hard limit is reached.


  state_l10n (, str, Ok)
    Localized message string corresponding to state.






Status
------





Authors
~~~~~~~

- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

