.. _smb_server_module:


smb_server -- Manage SMB server for PowerStore
==============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing storage containers on PowerStore Storage System includes creating an SMB server, getting details of an SMB server, modifying an SMB server and deleting an SMB server.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.13 or later.
- PyPowerStore 3.0.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  smb_server_id (optional, str, None)
    The unique identifier of the SMB server.


  nas_server (optional, str, None)
    Unique identifier/name of the NAS server to which the network interface belongs, as defined by the *nas_server* resource type.


  is_standalone (optional, bool, None)
    Indicates whether the SMB server is standalone.

    *true* - SMB server is standalone.

    *false* - SMB server is joined to the Active Directory.


  computer_name (optional, str, None)
    DNS Name of the associated Computer Account when the SMB server is joined to an Active Directory domain.


  domain (optional, str, None)
    Domain name where SMB server is registered in Active Directory, if applicable.


  netbios_name (optional, str, None)
    NetBIOS name is the network name of the standalone SMB server.


  workgroup (optional, str, None)
    Windows network workgroup for the SMB server.

    Applies to standalone SMB servers only.


  description (optional, str, None)
    Description of the SMB server in UTF-8 characters.


  local_admin_password (optional, str, None)
    Password for the local administrator account of the SMB server.


  state (optional, str, present)
    Define whether the SMB server should be enabled or not.

    For Delete operation only, it should be set to ``absent``.


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
   - The *check_mode* is supported.
   - The details of an SMB server can be fetched using *smb_server_id* or *nas_server*
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    

    - name: Enable SMB server
      register: result
      dellemc.powerstore.smb_server:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        nas_server: "{{ nas_server_name }}"
        is_standalone: true
        netbios_name: "string"
        workgroup: "string"
        description: "string"
        local_admin_password: "string"
        state: "present"

    - name: Get SMB server
      dellemc.powerstore.smb_server:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        smb_server_id: "{{ result.smb_server_details.id }}"

    - name: Get SMB server with NAS server
      dellemc.powerstore.smb_server:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        nas_server: "{{ result.smb_server_details.nas_server_id }}"

    - name: Modify SMB server
      dellemc.powerstore.smb_server:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        smb_server_id: "{{ result.smb_server_details.id }}"
        netbios_name: "string2"
        workgroup: "string2"
        description: "string2"
        local_admin_password: "string2"

    - name: Delete SMB server
      dellemc.powerstore.smb_server:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        smb_server_id: "{{ result.smb_server_details.id }}"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


smb_server_details (When SMB server exists., complex, {'computer_name': None, 'description': 'string2', 'domain': None, 'id': '65ad211b-374b-5f77-2946-62b767ad9845', 'is_joined': False, 'is_standalone': True, 'nas_server_id': '6581683c-61a3-76ab-f107-62b767ad9845', 'netbios_name': 'STRING2', 'workgroup': 'STRING2'})
  Details of the SMB server.


  computer_name (, str, )
    DNS name of the associated computer account when the SMB server is joined to an Active Directory domain.


  id (, str, )
    The unique identifier of the SMB server.


  description (, str, )
    Description of the SMB server.


  domain (, str, )
    Domain name where SMB server is registered in Active Directory, if applicable.


  is_joined (, bool, )
    Indicates whether the SMB server is joined to the Active Directory.


  is_standalone (, bool, )
    Indicates whether the SMB server is standalone.


  netbios_name (, str, )
    NetBIOS name is the network name of the standalone SMB server.


  nas_server_id (, str, )
    Unique identifier of the NAS server.


  workgroup (, str, )
    Windows network workgroup for the SMB server.






Status
------





Authors
~~~~~~~

- Trisha Datta (@trisha-dell) <ansible.team@dell.com>

