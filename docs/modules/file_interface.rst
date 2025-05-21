.. _file_interface_module:


file_interface -- Manage File interface for PowerStore
======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing file interfaces on PowerStore Storage System includes creating a file interface, getting details of a file interface, modifying a file interface and deleting a file interface.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- PyPowerStore 3.4.1.



Parameters
----------

  file_interface_id (optional, str, None)
    The unique identifier of the file interface.


  nas_server (optional, str, None)
    Unique identifier/name of the NAS server to which the network interface belongs, as defined by the *nas_server* resource type.


  ip_address (optional, str, None)
    IP address of the network interface.

    IPv4 and IPv6 are supported.


  prefix_length (optional, int, None)
    Prefix length for the interface.

    IPv4 and IPv6 are supported.


  gateway (optional, str, None)
    Gateway address for the network interface.

    IPv4 and IPv6 are supported.


  vlan_id (optional, int, None)
    Virtual Local Area Network (VLAN) identifier for the interface.


  role (optional, str, None)
    ``Production`` type of network interface is used for all file protocols and services of a NAS server. This type of interface is inactive while a NAS server is in destination mode.

    ``Backup`` type of network interface is used only for NDMP/NFS backup or disaster recovery testing. This type of interface is always active in all NAS server modes.

    ``System`` type of interface are reserved for system traffic such as for NAS server migration, they can not be used for the production traffic.

    ``System`` type is not supported during create interface.


  is_disabled (optional, bool, None)
    Indicates whether the network interface is disabled.


  ip_port_id (optional, str, None)
    Unique Identifier of the IP Port that is associated with the file interface.


  is_destination_override_enabled (optional, bool, None)
    Used in replication context when the user wants to override the settings on the destination.


  state (optional, str, present)
    Define whether the file interface should exist or not.

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
   - The details of a file interface can be fetched using *file_interface_id* or *nas_server* and *ip_address*.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    

    - name: Create File interface
      register: result
      dellemc.powerstore.file_interface:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        nas_server: "{{ nas_server_id }}"
        ip_address: "10.**.**.**"
        vlan_id: 0
        prefix_length: 21
        gateway: "10.**.**.1"
        state: "present"

    - name: Get file interface with file_interface_id
      dellemc.powerstore.file_interface:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        file_interface_id: "{{ file_interface_id }}"

    - name: Get file interface with nas_server_name and ip_addresss
      dellemc.powerstore.file_interface:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        nas_server: "sample_nas_server"
        ip_address: "10.**.**.**"

    - name: Modify file interface
      dellemc.powerstore.file_interface:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        file_interface_id: "{{ file_interface_id }}"
        ip_address: "10.**.**.@@"
        vlan_id: 0
        prefix_length: 21
        gateway: "10.**.**.1"
        state: "present"

    - name: Delete file interface
      dellemc.powerstore.file_interface:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        file_interface_id: "{{ file_interface_id }}"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


file_interface_details (When file interface exists., complex, {'gateway': '10.**.**.1', 'id': '65a50e0d-25f9-bd0a-8ca7-62b767ad9845', 'ip_address': '10.**.**.**', 'ip_port_id': 'IP_PORT2', 'is_destination_override_enabled': False, 'is_disabled': False, 'is_dr_test': False, 'name': 'PROD022_19c8adfb1d41_1d', 'nas_server_id': '6581683c-61a3-76ab-f107-62b767ad9845', 'prefix_length': 21, 'role': 'Production', 'source_parameters': 'None', 'vlan_id': 0})
  Details of the file interface.


  gateway (, str, )
    Gateway address for the network interface.


  id (, str, )
    The unique identifier of the file interface.


  ip_address (, str, )
    IP address of the network interface.


  ip_port_id (, str, )
    Unique Identifier of the IP Port that is associated with the file interface.


  is_destination_override_enabled (, bool, )
    Used in replication context when the user wants to override the settings on the destination.


  is_disabled (, bool, )
    Indicates whether the network interface is disabled.


  name (, str, )
    Name of the network interface. This property supports case-insensitive filtering.


  nas_server_id (, str, )
    Unique identifier of the NAS server.


  prefix_length (, int, )
    Prefix length for the interface.


  role (, str, )
    Role of the interface


  vlan_id (, int, )
    Virtual Local Area Network (VLAN) identifier for the interface.






Status
------





Authors
~~~~~~~

- Trisha Datta (@trisha-dell) <ansible.team@dell.com>

