.. _nfs_server_module:


nfs_server -- Manage NFS server for PowerStore
==============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing storage containers on PowerStore Storage System includes creating an NFS server, getting details of an NFS server, modifying an NFS server and deleting an NFS server.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.13 or later.
- PyPowerStore 3.0.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  nfs_server_id (optional, str, None)
    The unique identifier of the NFS server.


  nas_server (optional, str, None)
    Unique identifier/name of the NAS server to which the network interface belongs, as defined by the *nas_server* resource type.


  host_name (optional, str, None)
    The name that will be used by NFS clients to connect to this NFS server.


  is_nfsv3_enabled (optional, bool, None)
    Indicates whether NFSv3 is enabled on the NAS server.


  is_nfsv4_enabled (optional, bool, None)
    Indicates whether NFSv4 is enabled on the NAS server.


  is_secure_enabled (optional, bool, None)
    Indicates whether secure NFS is enabled on the NFS server.


  is_use_smb_config_enabled (optional, bool, None)
    Indicates whether SMB authentication is used to authenticate to the KDC.


  is_extended_credentials_enabled (optional, bool, None)
    Indicates whether the NFS server supports more than 16 Unix groups in a Unix credential.


  credentials_cache_TTL (optional, int, None)
    Sets the Time-To-Live (in minutes) expiration time in minutes for a Windows entry in the credentials cache.


  is_skip_unjoin (optional, bool, None)
    Allow to bypass NFS server unjoin.

    If false modification will fail if secure is enabled and current kdc_type is MS Windows.

    If secure is enabled either unjoin NFS server before deleting or set value to true.


  state (optional, str, present)
    Define whether the NFS server should be enabled or not.

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
   - The details of an NFS server can be fetched using *nfs_server_id* or *nas_server*.
   - To set *is_use_smb_config_enabled* as ``true``, *is_secure_enabled* should be set to ``true``.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    

    - name: Enable NFS server
      register: result
      dellemc.powerstore.nfs_server:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        nas_server: "{{ nas_server_name }}"
        host_name: "sample.hostname"
        is_nfsv3_enabled: true
        is_nfsv4_enabled: true
        is_secure_enabled: false
        is_extended_credentials_enabled: false
        credentials_cache_TTL: 60
        state: "present"

    - name: Get NFS server
      dellemc.powerstore.nfs_server:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        nfs_server_id: "{{ result.nfs_server_details.id }}"

    - name: Get NFS server with NAS server
      dellemc.powerstore.nfs_server:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        nas_server: "{{ result.nfs_server_details.nas_server_id }}"

    - name: Modify NFS server
      dellemc.powerstore.nfs_server:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        nfs_server_id: "{{ result.nfs_server_details.id }}"
        is_nfsv4_enabled: false
        is_extended_credentials_enabled: true
        credentials_cache_TTL: 120

    - name: Delete NFS server
      dellemc.powerstore.nfs_server:
        array_ip: "{{ array_ip }}"
        validate_certs: "{{ validate_certs }}"
        user: "{{ user }}"
        password: "{{ password }}"
        nfs_server_id: "{{ result.nfs_server_details.id }}"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


nfs_server_details (When NFS server is enabled., complex, {'credentials_cache_TTL': 120, 'host_name': 'sample_host_name', 'id': '65ad14fe-5f6e-beb3-424f-62b767ad9845', 'is_extended_credentials_enabled': True, 'is_joined': False, 'is_nfsv3_enabled': True, 'is_nfsv4_enabled': False, 'is_secure_enabled': False, 'is_use_smb_config_enabled': None, 'nas_server_id': '6581683c-61a3-76ab-f107-62b767ad9845', 'service_principal_name': None})
  Details of the NFS server.


  credentials_cache_TTL (, int, )
    Sets the Time-To-Live (in minutes) expiration timestamp for a Windows entry in the credentials cache.


  id (, str, )
    The unique identifier of the NFS server.


  host_name (, str, )
    The name that will be used by NFS clients to connect to this NFS server.


  is_extended_credentials_enabled (, bool, )
    Indicates whether the NFS server supports more than 16 Unix groups in a Unix credential.


  is_joined (, bool, )
    Indicates whether the NFS server is joined to Active Directory.


  is_nfsv3_enabled (, bool, )
    Indicates whether NFSv3 is enabled on the NAS server.


  is_nfsv4_enabled (, bool, )
    Indicates whether NFSv4 is enabled on the NAS server.


  nas_server_id (, str, )
    Unique identifier of the NAS server.


  is_secure_enabled (, bool, )
    Indicates whether secure NFS is enabled on the NFS server.


  is_use_smb_config_enabled (, bool, )
    Indicates whether SMB authentication is used to authenticate to the KDC.


  service_principal_name (, str, )
    The Service Principal Name (SPN) for the NFS server.






Status
------





Authors
~~~~~~~

- Trisha Datta (@trisha-dell) <ansible.team@dell.com>

