.. _nasserver_module:


nasserver -- NAS Server operations for PowerStore Storage system
================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Supports getting the details, creating, modifying the attributes of a NAS server and deleting a NAS server.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.14 or later.
- PyPowerStore 2.1.0.
- Python 3.9, 3.10 or 3.11.




Parameters
----------

  nas_server_name (optional, str, None)
    Name of the NAS server. Mutually exclusive with \ :emphasis:`nas\_server\_id`\ .


  nas_server_id (optional, str, None)
    Unique id of the NAS server. Mutually exclusive with \ :emphasis:`nas\_server\_name`\ .


  description (optional, str, None)
    Description of the NAS server.


  nas_server_new_name (optional, str, None)
    New name of the NAS server for a rename operation.


  current_node (optional, str, None)
    Unique identifier or name of the node on which the NAS server is running.


  preferred_node (optional, str, None)
    Unique identifier or name of the preferred node for the NAS server. The initial value (on NAS server create) is taken from the current node.


  current_unix_directory_service (optional, str, None)
    Define the Unix directory service used for looking up identity information for Unix such as UIDs, GIDs, net groups, and so on.


  default_unix_user (optional, str, None)
    Default Unix user name used for granting access in case of Windows to Unix user mapping failure. When empty, access in such case is denied.


  default_windows_user (optional, str, None)
    Default Windows user name used for granting access in case of Unix to Windows user mapping failure. When empty, access in such case is denied.


  protection_policy (optional, str, None)
    Name/ID of the protection policy applied to the nas server.

    Policy can be removed by passing an empty string in the \ :emphasis:`protection\_policy`\  parameter.


  is_username_translation_enabled (optional, bool, None)
    Enable the possibility to match a Windows account with an Unix account with different names.


  is_auto_user_mapping_enabled (optional, bool, None)
    To automatically generate the unix user (uid), if the windows user does not have any in the configured Unix Directory Service (UDS).

    In a pure SMB or non multi-protocol environment, this should be set to true.


  state (True, str, None)
    Define whether the nas server should exist or not.


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
   - Adding/Removing protection policy to/from a NAS server is supported for PowerStore version 3.0.0 and above.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create a NAS Server
      dellemc.powerstore.nasserver:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        nas_server_name: "test-nas-server"
        description: "NAS Server test"
        current_unix_directory_service: "LDAP"
        default_unix_user: "user1"
        default_windows_user: "user2"
        is_username_translation_enabled: true
        is_auto_user_mapping_enabled: true
        protection_policy: "ansible_policy"
        state: "present"

    - name: Get details of NAS Server by name
      dellemc.powerstore.nasserver:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        nas_server_name: "{{ nas_server_name }}"
        state: "present"

    - name: Get Details of NAS Server by ID
      dellemc.powerstore.nasserver:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        nas_server_id: "{{ nas_id }}"
        state: "present"

    - name: Rename NAS Server by Name
      dellemc.powerstore.nasserver:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        nas_server_name: "{{ nas_server_name }}"
        nas_server_new_name: "{{ nas_server_new_name }}"
        state: "present"

    - name: Modify NAS Server attributes by ID
      dellemc.powerstore.nasserver:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        nas_server_id: "{{ nas_id }}"
        current_unix_directory_service: "LOCAL_FILES"
        current_node: "{{ cur_node_n1 }}"
        preferred_node: "{{ prefered_node }}"
        protection_policy: "protection_policy_1"
        state: "present"

    - name: Remove protection policy
      dellemc.powerstore.nasserver:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        nas_server_id: "{{ nas_id }}"
        protection_policy: ""
        state: "present"

    - name: Delete NAS Server
      dellemc.powerstore.nasserver:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        nas_server_id: "{{ nas_id }}"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


nasserver_details (When nas server exists, complex, {'backup_IPv4_interface_id': None, 'backup_IPv6_interface_id': None, 'current_node': {'id': 'N2', 'name': 'Appliance-WND8977-node-B'}, 'current_node_id': 'Appliance-WND8977-node-B', 'current_preferred_IPv4_interface_id': '60c02-b5d8-9d9b-7e6f-feb93c9', 'current_preferred_IPv6_interface_id': None, 'current_unix_directory_service': 'LDAP', 'current_unix_directory_service_l10n': 'LDAP', 'default_unix_user': None, 'default_windows_user': None, 'description': '', 'file_interfaces': [{'id': '0c05652-b5d8-9d9b-7e6f-fe8be1eb93c9', 'ip_address': '1.2.3.4', 'name': 'PROD001_827ee18708a9_6'}], 'file_ldaps': [{'id': '60c05ba8-362e-159a-0205-ee6f605dfe5a'}], 'file_nises': [], 'file_systems': [{'id': '61c55b57-4a70-08dd-a240-96e8abdcbab0', 'name': 'sample_fs'}], 'id': '60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9', 'is_auto_user_mapping_enabled': True, 'is_username_translation_enabled': False, 'name': 'ansible_nas_server_2', 'nfs_servers': [{'id': '60c05653-4fd3-2033-2da0-ee6f605dfe5a'}], 'operational_status': 'Started', 'operational_status_l10n': 'Started', 'preferred_node': {'id': 'N2', 'name': 'Appliance-WND8977-node-B'}, 'preferred_node_id': 'Appliance-WND8977-node-B', 'production_IPv4_interface_id': '60c05652-b5d8-9d9b-7e6f-fe8be1eb93c', 'production_IPv6_interface_id': None, 'protection_policy_id': None, 'smb_servers': [{'id': '60c05c18-6806-26ae-3b0d-fe8be1eb93c'}]})
  Details about the nas server.


  id (, str, )
    The system generated ID given to the nas server.


  name (, str, )
    Name of the nas server.


  description (, str, )
    Additional information about the nas server.


  operational_status (, str, )
    NAS server operational status.


  current_node (, dict, )
    Unique identifier and name of the node on which the NAS server is running.


  preferred_node (, dict, )
    Unique identifier and name of the preferred node for the NAS server.


  default_unix_user (, str, )
    Default Unix user name used for granting access in case of Windows to Unix user mapping failure.


  current_unix_directory_service (, str, )
    Define the Unix directory service used for looking up identity information for Unix such as UIDs, GIDs, net groups, and so on.


  is_username_translation_enabled (, bool, )
    Enable the possibility to match a windows account to a Unix account with different names.


  production_IPv4_interface_id (, str, )
    Unique identifier of the preferred IPv4 production interface.


  production_IPv6_interface_id (, str, )
    Unique identifier of the preferred IPv6 production interface.


  backup_IPv4_interface_id (, str, )
    Unique identifier of the preferred IPv4 backup interface.


  backup_IPv6_interface_id (, str, )
    Unique identifier of the preferred IPv6 backup interface.


  file_interfaces (, dict, )
    This is the inverse of the resource type file\_interface association. Will return the id,name & ip\_address of the associated file interface.


  nfs_servers (, str, )
    This is the inverse of the resource type nfs\_server association.


  smb_servers (, str, )
    This is the inverse of the resource type smb\_server association.


  file_ldaps (, str, )
    This is the inverse of the resource type file\_ldap association.


  file_systems (, dict, )
    This is the inverse of the resource type file\_system association.


  protection_policy_id (, str, )
    Id of the protection policy applied to the nas server.






Status
------





Authors
~~~~~~~

- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
- Jennifer John (@johnj9) <ansible.team@dell.com>

