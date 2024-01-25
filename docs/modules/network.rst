.. _network_module:


network -- Manage networks for PowerStore
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing networks on PowerStore Storage System includes getting details of network, modifying attributes of network and adding/removing IP ports to/from storage network.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.13 or later.
- PyPowerStore 3.0.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  network_name (optional, str, None)
    The name of the network.

    This parameter is added in 2.0.0.0.

    Specify either *network_name* or *network_id* for any operation.


  network_id (optional, str, None)
    The ID of the network.


  vlan_id (optional, int, None)
    The ID of the VLAN.


  gateway (optional, str, None)
    Network gateway in IPv4 format. IP version.

    Specify empty string to remove the gateway.


  prefix_length (optional, int, None)
    Network prefix length.


  new_cluster_mgmt_address (optional, str, None)
    New cluster management IP address in IPv4 format.


  storage_discovery_address (optional, str, None)
    New storage discovery IP address in IPv4 format.

    Specify empty string to remove the storage discovery IP address.


  mtu (optional, int, None)
    Maximum Transmission Unit (MTU) packet size set on network interfaces, in bytes.


  new_name (optional, str, None)
    New name of the network.


  addresses (optional, list, None)
    IP addresses to add/remove in IPv4 format.


    current_address (optional, str, None)
      Existing IPv4 address.


    new_address (optional, str, None)
      New IPv4 address.



  ports (optional, list, None)
    Ports to be mapped/unmapped to/from the storage network.


  port_state (optional, str, None)
    Specifies whether port should mapped/unmapped from the storage network.


  vasa_provider_credentials (optional, dict, None)
    Credentials required for re-registering the VASA vendor provider during the reconfiguration of the cluster management IP address.


    username (True, str, None)
      VASA vendor provider user name.


    password (True, str, None)
      VASA vendor provider password.



  esxi_credentials (optional, list, None)
    Credentials required for re-registering the ESXi hosts in the vCenter.

    It should be passed only when ESXi host addresses or management network VLAN / prefix / gateway are changed during the reconfiguration of the PowerStore X model appliances.

    This parameter is applicable only for PowerStore X model.

    This parameter will be ignored if passed for PowerStore T model.


    node_id (True, str, None)
      Node identifier corresponding to the ESXi host.


    password (True, str, None)
      ESXi host root password.



  wait_for_completion (optional, bool, False)
    Flag to indicate if the operation should be run synchronously or asynchronously. ``true`` signifies synchronous execution. By default, modify operation will run ``asynchronously``.


  state (True, str, None)
    Define whether the network exist or not.


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
   - It is recommended to perform task asynchronously while changing cluster management address.
   - Idempotency is not supported for *vasa_provider_credentials* and *esxi_credentials*.
   - For PowerStore X model, *vasa_provider_credentials* has to be specified along with *new_cluster_mgmt_address*.
   - The *check_mode* is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get network details using ID
      dellemc.powerstore.network:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        network_id: "NW1"
        state: "present"

    - name: Get network details using name
      dellemc.powerstore.network:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        network_name: "Default Management Network"
        state: "present"

    - name: Rename the storage network
      dellemc.powerstore.network:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        network_name: "Default Storage Network"
        new_name: "iSCSI Network"
        wait_for_completion: true
        state: "present"

    - name: Replace the IP's in the management network and re-register VASA vendor provider
      dellemc.powerstore.network:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        network_id: "NW1"
        addresses:
          - current_address: "100.230.x.x"
            new_address: "100.230.x.x"
          - current_address: "100.230.x.x"
            new_address: "100.230.x.x"
          - current_address: "100.230.x.x"
            new_address: "100.230.x.x"
        new_cluster_mgmt_address: "100.230.x.x"
        vasa_provider_credentials:
          username: "vmadmin"
          password: "{{vm_password}}"
        state: "present"

    - name: Map port to the storage network
      dellemc.powerstore.network:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        network_id: "NW6"
        ports:
          - "IP1"
        port_state: "present-in-network"
        state: "present"

    - name: Unmap port from the storage network
      dellemc.powerstore.network:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        network_id: "NW6"
        ports:
          - "IP1"
        port_state: "absent-in-network"
        state: "present"

    - name: Replace the IP's in the management network and re-register VASA vendor
            provider for X model
      dellemc.powerstore.network:
        array_ip: "{{array_ip1}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        network_id: "NW1"
        vlan_id: 0
        gateway: "100.231.x.x"
        mtu: 1500
        prefix_length: 24
        addresses:
          - current_address: "100.230.x.x"
            new_address: "100.231.x.x"
          - current_address: "100.230.x.x"
            new_address: "100.231.x.x"
          - current_address: "100.230.x.x"
            new_address: "100.231.x.x"
          - current_address: "100.230.x.x"
            new_address: "100.231.x.x"
          - current_address: "100.230.x.x"
            new_address: "100.231.x.x"
        new_cluster_mgmt_address: "100.231.x.x"
        vasa_provider_credentials:
          username: "vmadmin"
          password: "{{vm_password}}"
        esxi_credentials:
          - "node_id": "N1"
            "password": "{{node_password}}"
          - "node_id": "N2"
            "password": "{{node_password}}"
        state: "present"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


job_details (When asynchronous task is performed., complex, {'description_l10n': 'Modify network parameters.', 'end_time': '2022-01-06T07:39:05.846+00:00', 'estimated_completion_time': None, 'id': 'be0d099c-a6cf-44e8-88d7-9be80ccae369', 'parent_id': None, 'phase': 'Completed', 'phase_l10n': 'Completed', 'progress_percentage': 100, 'resource_action': 'modify', 'resource_action_l10n': 'modify', 'resource_id': 'nw6', 'resource_name': None, 'resource_type': 'network', 'resource_type_l10n': 'network', 'response_body': None, 'response_status': None, 'response_status_l10n': None, 'root_id': 'be0d099c-a6cf-44e8-88d7-9be80ccae369', 'start_time': '2022-01-06T07:39:05.47+00:00', 'state': 'COMPLETED', 'state_l10n': 'Completed', 'step_order': 23792565, 'user': 'admin'})
  The job details.


  id (, str, )
    The ID of the job.



network_details (When network exists., complex, {'cluster_details': {'appliance_count': 1, 'chap_mode': 'Disabled', 'compatibility_level': 10, 'global_id': 'PS00d01e1bb312', 'id': 0, 'is_encryption_enabled': True, 'management_address': '10.xx.xx.xx', 'master_appliance_id': 'A1', 'name': 'WN-D8977', 'physical_mtu': 1500, 'service_config_details': None, 'state': 'Configured', 'state_l10n': 'Configured', 'storage_discovery_address': '10.xx.xx.xx', 'system_time': '2022-02-04T11:18:37.441Z'}, 'gateway': '10.xx.xx.xx', 'id': 'NW1', 'ip_version': 'IPv4', 'ip_version_l10n': 'IPv4', 'member_ips': [{'address': '10.xx.xx.xx', 'appliance_id': None, 'id': 'IP1', 'ip_port_id': None, 'name': 'Default Management Network (10.xx.xx.xx)', 'network_id': 'NW1', 'node_id': None, 'purposes': ['Mgmt_Cluster_Floating'], 'purposes_l10n': ['Mgmt_Cluster_Floating']}, {'address': '10.xx.xx.xx', 'appliance_id': None, 'id': 'IP2', 'ip_port_id': None, 'name': 'Default Management Network (10.xx.xx.xx)', 'network_id': 'NW1', 'node_id': None, 'purposes': ['Mgmt_Appliance_Floating'], 'purposes_l10n': ['Mgmt_Appliance_Floating']}], 'mtu': 1500, 'name': 'Default Management Network', 'prefix_length': 24, 'purposes': [], 'purposes_l10n': None, 'type': 'Management', 'type_l10n': 'Management', 'vcenter_details': {'address': '10.xx.xx.xx', 'id': '0d330d6c-3fe6-41c6-8023-5bd3fa7c61cd', 'instance_uuid': 'c4c14fbb-828b-40f3-99bb-5bd4db723516', 'username': 'administrator@vsphere.local', 'vendor_provider_status': 'Online', 'vendor_provider_status_l10n': 'Online'}, 'vlan_id': 0})
  The network details.


  name (, str, )
    The name of the network.


  id (, str, )
    The ID of the network.


  gateway (, str, )
    The gateway of the network.


  vlan_id (, int, )
    VLAN identifier.


  prefix_length (, int, )
    Network prefix length.


  mtu (, int, )
    Maximum Transmission Unit (MTU) packet size set on network interfaces, in bytes.


  ip_version (, str, )
    IP protocol version


  type (, str, )
    Network type


  purposes (, list, )
    Purposes of the network.


  cluster_details (, complex, )
    The details of the cluster.


    id (, str, )
      The unique identifier of the cluster.


    name (, str, )
      The name of the cluster.


    management_address (, str, )
      The floating management IP address for the cluster in IPv4 or IPv6 format.


    storage_discovery_address (, str, )
      The floating storage discovery IP address for the cluster in IPv4 or IPv6 format.


    appliance_count (, int, )
      Number of appliances configured in this cluster.



  member_ips (, complex, )
    Properties of the IP pool address.


    id (, str, )
      Unique identifier of the IP address.


    name (, str, )
      Name of the IP address.


    network_id (, str, )
      Unique identifier of the network to which the IP address belongs.


    ip_port_id (, str, )
      Unique identifier of the port that uses this IP address to provide access to storage network services, such as iSCSI. This attribute can be set only for an IP address used by networks of type Storage.


    appliance_id (, str, )
      Unique identifier of the appliance to which the IP address belongs.


    node_id (, str, )
      Unique identifier of the cluster node to which the IP address belongs.


    address (, str, )
      IP address value, in IPv4 or IPv6 format.


    purposes (, list, )
      IP address purposes.



  vcenter_details (, complex, )
    Details of the vcenter.


    address (, str, )
      IP address of vCenter host, in IPv4, IPv6, or hostname format.


    id (, str, )
      Unique identifier of the vCenter instance.


    instance_uuid (, str, )
      UUID instance of the vCenter.


    username (, str, )
      User name to login to vCenter.


    vendor_provider_status (, str, )
      General status of the VASA vendor provider in vCenter.







Status
------





Authors
~~~~~~~

- Akash Shendge (@shenda1) <ansible.team@dell.com>

