.. _file_dns_module:


file_dns -- Manage File DNS for PowerStore
==========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing storage containers on PowerStore Storage System includes creating a file DNS, getting details of a file DNS, modifying a file DNS and deleting a file DNS.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.13 or later.
- PyPowerStore 3.2.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  file_dns_id (optional, str, None)
    The unique identifier of the file DNS.


  nas_server (optional, str, None)
    Unique identifier/name of the associated NAS Server instance that uses this DNS Service object.


  domain (optional, str, None)
    Name of the DNS domain, where the NAS Server does host names lookup when an FQDN is not specified in the request.


  add_ip_addresses (optional, list, None)
    IP addresses to add to the current list.

    IPv4 and IPv6 are supported.


  remove_ip_addresses (optional, list, None)
    IP addresses to remove from the current list.

    IPv4 and IPv6 are supported.


  transport (optional, str, None)
    Transport used when connecting to the DNS Server.

    ``UDP`` - DNS uses the UDP protocol.

    ``TCP`` - DNS uses the TCP protocol.


  is_destination_override_enabled (optional, bool, None)
    In order to modify any properties of this resource when the associated NAS server is a replication destination, the *is_destination_override_enabled* flag must be set to ``true``.


  state (optional, str, present)
    Define whether the file DNS should be enabled or not.

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
   - The details of a file DNS can be fetched using *file_dns_id* or *nas_server*.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    

    - name: Enable file DNS
      register: result
      dellemc.powerstore.file_dns:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        nas_server: "{{ nas_server_name }}"
        domain: "NAS_domain"
        add_ip_addresses:
          - "10.**.**.**"
        transport: "UDP"
        state: "present"

    - name: Get File DNS
      dellemc.powerstore.file_dns:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        file_dns_id: "{{ result.file_dns_details.id }}"

    - name: Get File DNS with NAS server
      dellemc.powerstore.file_dns:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        nas_server: "{{ result.file_dns_details.nas_server_id }}"

    - name: Modify File DNS
      dellemc.powerstore.file_dns:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        file_dns_id: "{{ result.file_dns_details.id }}"
        domain: "NAS_domain"
        add_ip_addresses:
          - "10.**.**.@@"
        remove_ip_addresses:
          - "10.**.**.**"
        transport: "UDP"

    - name: Delete file DNS
      dellemc.powerstore.file_dns:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        file_dns_id: "{{ result.file_dns_details.id }}"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


file_nis_details (When file DNS exists., complex, {'domain': 'NAS_domain', 'id': '65ab7e44-7009-e3e5-907a-62b767ad9845', 'ip_addresses': ['10.**.**.**'], 'is_destination_override_enabled': False, 'nas_server_id': '6581683c-61a3-76ab-f107-62b767ad9845', 'transport': 'UDP'})
  Details of the file DNS.


  domain (, str, )
    Name of the DNS domain.


  id (, str, )
    The unique identifier of the file DNS.


  ip_addresses (, list, )
    The addresses may be IPv4 or IPv6.


  is_destination_override_enabled (, bool, )
    Used in replication context when the user wants to override the settings on the destination.


  nas_server_id (, str, )
    Unique identifier of the NAS server.


  transport (, str, )
    Transport used when connecting to the DNS Server.






Status
------





Authors
~~~~~~~

- Trisha Datta (@trisha-dell) <ansible.team@dell.com>

