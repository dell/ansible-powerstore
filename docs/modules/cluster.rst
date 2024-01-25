.. _cluster_module:


cluster -- Manage cluster related operations on PowerStore
==========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing cluster on PowerStore storage system includes creating cluster, validating create cluster attributes, getting details and modifying cluster configuration parameters.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.13 or later.
- PyPowerStore 3.0.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  cluster_name (optional, str, None)
    The Name of cluster.


  chap_mode (optional, str, None)
    The mode that describes or sets the iSCSI CHAP mode for the cluster.


  cluster_id (optional, str, None)
    Id of the cluster.


  new_name (optional, str, None)
    The new name for the cluster.


  service_password (optional, str, None)
    The password for the service user.


  appliance_id (optional, str, None)
    ID of the appliance.

    Parameters *appliance_id* and *appliance_name* are mutually exclusive.

    Parameter *is_ssh_enabled* has to be passed along with *appliance_id*.


  appliance_name (optional, str, None)
    Name of the appliance.

    Parameters *appliance_id* and *appliance_name* are mutually exclusive.

    Parameter *is_ssh_enabled* has to be passed along with *appliance_name*.


  is_ssh_enabled (optional, bool, None)
    Whether SSH access is enabled for the cluster.

    Either *appliance_id* or *appliance_name* is to be passed along with *is_ssh_enabled*.


  physical_mtu (optional, int, None)
    MTU for ethernet ports in the cluster.

    The MTU can be set between 1500 to 9000.


  ignore_network_warnings (optional, bool, None)
    Whether to ignore the network warning about unreachable external network.


  appliances (optional, list, None)
    Appliance configuration setting during cluster creation.

    This is mandatory for create cluster operation.


    link_local_address (True, str, None)
      The unique IPv4 address of the appliance and is set by zeroconf.


    name (optional, str, None)
      Name of new appliance.


    drive_failure_tolerance_level (optional, str, None)
      Specifies the possible drive failure tolerance levels.



  dns_servers (optional, list, None)
    DNS server addresses in IPv4 format. At least one DNS server should be provided.

    This is mandatory for create cluster operation.


  ntp_servers (optional, list, None)
    NTP server addresses in IPv4 or hostname format. At least one NTP server should be provided.

    This is mandatory for create cluster operation.


  physical_switches (optional, list, None)
    Physical switch setting for a new cluster.


    name (True, str, None)
      Name of the physical switch.


    purpose (True, str, None)
      Specifies the purpose of the physical switch.


    connections (True, list, None)
      specifies the supported connection for the physical switch.


      address (True, str, None)
        Specifies the physical switch address in IPv4 or DNS hostname format.


      port (optional, int, None)
        Specifies the port used for connection to switch.


      connect_method (True, str, None)
        Specifies the connection method type for the physical Switch.


      username (optional, str, None)
        Specifies username to connect a physical switch for SSH connection method.


      ssh_password (optional, str, None)
        Specifies SSH password to connect a physical switch.


      snmp_community_string (optional, str, None)
        Specifies ``SNMPv2`` community string, if ``SNMPv2`` connect method is selected.




  networks (optional, list, None)
    Configuration of one or more network(s) based on network type.

    This is mandatory for create cluster operation.


    type (True, str, None)
      Specifies the type of the network.


    vlan_id (optional, int, None)
      The ID of the VLAN.


    prefix_length (True, int, None)
      Network prefix length.


    gateway (optional, str, None)
      Network gateway in IPv4 format.


    cluster_mgmt_address (optional, str, None)
      New cluster management IP address in IPv4 format.


    storage_discovery_address (optional, str, None)
      New storage discovery IP address in IPv4 format.

      This can be specified only when configure the storage network type.


    addresses (True, list, None)
      IP addresses in IPv4 format.


    purposes (optional, list, None)
      Purpose of the network.

      Only applicable for storage network.



  vcenters (optional, list, None)
    Configure vCenter settings when creating cluster.

    Currently, for vcenters parameter API supports only single element.

    This is required when creating PowerStore X cluster and optional for PowerStore T.


    address (True, str, None)
      IP address of vCenter in IPv4 or hostname format.


    username (True, str, None)
      User name to login to vCenter.


    password (True, str, None)
      Password to login to vCenter.


    is_verify_server_cert (True, bool, None)
      Whether or not the connection will be secured with the vcenter SSL certificate.


    data_center_name (optional, str, None)
      Name of the data center.

      This is used to join an existing datacenter in vcenter.

      This should be specified when creating PowerStore X cluster.

      Mutually exclusive with *data_center_id*.


    data_center_id (optional, str, None)
      The VMWare ID of datacenter.

      This is used to join an existing datacenter in vcenter.

      This should be specified when creating PowerStore X cluster.

      Mutually exclusive with *data_center_name*.


    esx_cluster_name (optional, str, None)
      Name of the ESXi cluster.

      This should be specified when creating PowerStore X cluster.


    vasa_provider_credentials (True, dict, None)
      Storage system credentials for vCenter to use for communicating with the storage system using VASA.


      username (True, str, None)
        Username of the local user account which will be used by vSphere to register VASA provider.


      password (True, str, None)
        Password of the local user account which will be used by vSphere to register VASA provider.




  is_http_redirect_enabled (optional, bool, None)
    Whether to redirect the HTTP requests to HTTPS.


  validate_create (optional, bool, True)
    Whether to perform create cluster validate call.


  wait_for_completion (optional, bool, False)
    Flag to indicate if the operation should be run synchronously or asynchronously.

    ``true`` signifies synchronous execution. By default, create cluster operation will run asynchronously.


  state (True, str, None)
    Define whether the cluster should exist or not.

    Value ``present`` indicates that the cluster should exist on the system.

    Value ``absent`` indicates that the cluster should not exist on the system.


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
   - Deletion of a cluster is not supported by ansible module.
   - The *check_mode* is not supported.
   - Before performing create operation, the default password for admin user and service user should be changed.
   - For management type network during cluster creation, *storage_discovery_address* and purposes should not be passed.
   - The *vcenters* parameter is mandatory for PowerStore X cluster creation.
   - Minimum 3 and 5 addresses are required for management network for PowerStore T and X model respectively.
   - The ``File_Mobility`` purpose is supported only in FootHills Prime and above.
   - Parameter *is_http_redirect_enabled* is supported only in PowerStore FootHills Prime and above.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get the details of cluster using id
      dellemc.powerstore.cluster:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        cluster_id: "0"
        state: "present"

    - name: Modify details of cluster using the name
      dellemc.powerstore.cluster:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        cluster_name: "RT-D1320"
        appliance_id: "A1"
        is_ssh_enabled: true
        service_password: "S@mple_password"
        chap_mode: "Disabled"
        new_name: "new_RT-D1320"
        state: "present"

    - name: Validate create cluster
      dellemc.powerstore.cluster:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        cluster_name: "RT-D1320"
        ignore_network_warnings: true
        appliances:
          - link_local_address: "1.2.x.x"
            name: "Ansible_cluster"
            drive_failure_tolerance_level: "Double"
        dns_servers:
          - "1.1.x.x"
        ntp_servers:
          - "1.3.x.x"
        networks:
          - type: "Management"
            vlan_id: 0
            prefix_length: 24
            gateway: "1.x.x.x"
            cluster_mgmt_address: "1.x.x.x"
            addresses:
              - "2.x.x.x"
              - "3.x.x.x"
          - type: "Storage"
            vlan_id: 0
            prefix_length: 42
            gateway: "1.x.x.x"
            storage_discovery_address: "1.x.x.x"
            addresses:
              - "2.x.x.x"
              - "3.x.x.x"
            purpose:
              - "ISCSI"
        is_http_redirect_enabled: true
        validate_create: true
        state: "present"

    - name: Create cluster
      dellemc.powerstore.cluster:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        cluster_name: "RT-D1320"
        ignore_network_warnings: true
        appliances:
          - link_local_address: "1.2.x.x"
            name: "Ansible_cluster"
            drive_failure_tolerance_level: "Double"
        dns_servers:
          - "1.1.x.x"
        ntp_servers:
          - "1.3.x.x"
        physical_switch:
          - name: "Ansible_switch"
            purpose: "Management_Only"
            connections:
              - address: "1.x.x.x"
                port: 20
                connect_method: "SSH"
                username: "user"
                ssh_password: "password"
        networks:
          - type: "Management"
            vlan_id: 0
            prefix_length: 24
            gateway: "1.x.x.x"
            cluster_mgmt_address: "1.x.x.x"
            addresses:
              - "2.x.x.x"
              - "3.x.x.x"
          - type: "Storage"
            vlan_id: 0
            prefix_length: 42
            gateway: "1.x.x.x"
            storage_discovery_address: "1.x.x.x"
            addresses:
              - "2.x.x.x"
              - "3.x.x.x"
            purpose:
              - "ISCSI"
        vcenters:
          - address: "1.x.x.x"
            username: "user"
            password: "password"
            is_verify_server_cert: true
            vasa_provider_credentials:
              username: "user"
              password: "password"
        is_http_redirect_enabled: true
        wait_for_completion: false
        state: "present"



Return Values
-------------

changed (always, bool, true)
  Whether or not the resource has changed.


job_details (When asynchronous task is performed., complex, {'description_l10n': 'Create Cluster.', 'end_time': '2022-01-06T07:39:05.846+00:00', 'estimated_completion_time': None, 'id': 'be0d099c-a6cf-44e8-88d7-9be80ccae369', 'parent_id': None, 'phase': 'Completed', 'phase_l10n': 'Completed', 'progress_percentage': 100, 'resource_action': 'create', 'resource_action_l10n': 'create', 'resource_id': '0', 'resource_name': None, 'resource_type': 'cluster', 'resource_type_l10n': 'cluster', 'response_body': {'id': 0, 'response_type': 'job_create_response'}, 'response_status': None, 'response_status_l10n': None, 'root_id': 'be0d099c-a6cf-44e8-88d7-9be80ccae369', 'start_time': '2022-01-06T07:39:05.47+00:00', 'state': 'COMPLETED', 'state_l10n': 'Completed', 'step_order': 23792565, 'user': 'admin'})
  The job details.


  id (, str, )
    The ID of the job.



cluster_details (When Cluster exists., complex, {'appliance_count': 1, 'chap_mode': 'Disabled', 'compatibility_level': 10, 'global_id': 'PS00d01e1bb312', 'id': 0, 'is_encryption_enabled': True, 'management_address': '1.2.3.4', 'master_appliance_id': 'A1', 'name': 'WN-D8977', 'physical_mtu': 1500, 'service_config_details': None, 'state': 'Configured', 'state_l10n': 'Configured', 'storage_discovery_address': '10.230.42.228', 'system_time': '2022-02-04T11:18:37.441Z'})
  The cluster details.


  id (, str, )
    The ID of the cluster.


  name (, str, )
    Name of the cluster.


  is_ssh_enabled (, bool, )
    Whether or not the ssh is enabled.


  physical_mtu (, int, )
    MTU for the cluster.


  global_id (, str, )
    The global unique identifier of the cluster.


  management_address (, str, )
    The floating management IP address for the cluster in IPv4 or IPv6 format.


  storage_discovery_address (, str, )
    The floating storage discovery IP address for the cluster in IPv4 or IPv6 format.


  master_appliance_id (, str, )
    The unique identifier of the appliance acting as primary. This parameter is deprecated in version 2.0.0.0.


  primary_appliance_id (, str, )
    The unique identifier of the appliance acting as primary. This parameter was added in version 2.0.0.0.


  appliance_count (, int, )
    Number of appliances configured in this cluster.


  is_encryption_enabled (, bool, )
    Whether or not Data at Rest Encryption is enabled on the cluster.


  compatibility_level (, int, )
    The behavioral version of the software version API, It is used to ensure the compatibility across potentially different software versions.


  state (, str, )
    Possible cluster states.


  system_time (, str, )
    Current clock time for the system. System time and all the system reported times are in UTC (GMT+0:00) format.


  service_config_details (When is_ssh_enabled is passed in the playbook task, complex, )
    Details of the service config for the entered appliance.


    id (, str, )
      Id of the service configuration.


    appliance_id (, str, )
      Id of the appliance for which the service configuration exists.


    is_ssh_enabled (, bool, )
      Whether the ssh is enabled for the appliance or not.



  service_user_details (when the cluster exists., complex, )
    Details of the service user for which the password can be updated.


    id (, str, )
      Id of the service user.


    name (, str, )
      Name of the service user.


    is_default_password (, bool, )
      Whether the service user has default password or not.


    is_built_in (, bool, )
      Whether the service user is built in or not.



  appliance_details (When appliance name or id is passed in the playbook task., complex, )
    Name and Id of the appliance for which *is_ssh_enabled* parameter is used.


    id (, str, )
      Id of the appliance.


    name (, str, )
      Name of the appliance.







Status
------





Authors
~~~~~~~

- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>
- Bhavneet Sharma (@sharmb5) <ansible.team@dell.com>

