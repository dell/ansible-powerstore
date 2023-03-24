.. _info_module:


info -- Gathers information about PowerStore Storage entities
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Gathers the list of specified PowerStore Storage System entities, includes block/file provisioning modules, replication modules, configuration modules, and virtualization modules.

Block provisioning module includes volumes, volume groups, hosts, host groups, snapshot rules, and protection policies.

File provisioning module includes NAS servers, NFS exports, SMB shares, tree quotas, user quotas, and file systems.

Replication module includes replication rules, replication sessions, and remote system.

Virtualization module includes vCenters and virtual volumes.

Configuration module includes cluster nodes, networks, roles, local users, appliances, security configs, certificates, AD/LDAP servers, LDAP accounts, and LDAP domain.

It also includes DNS/NTP servers, smtp configs, email destinations, remote support, and remote support contacts.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore Storage System. Ansible 2.12, 2.13 or 2.14



Parameters
----------

  gather_subset (True, list, None)
    A list of string variables which specify the PowerStore system entities requiring information.

    Volumes - vol.

    All the nodes - node.

    Volume groups - vg.

    Protection policies - protection_policy.

    Hosts - host.

    Host groups - hg.

    Snapshot rules - snapshot_rule.

    NAS servers - nas_server.

    NFS exports - nfs_export.

    SMB shares - smb_share.

    Tree quotas - tree_quota.

    User quotas - user_quota.

    File systems - file_system.

    Replication rules - replication_rule.

    Replication sessions - replication_session.

    Remote systems - remote_system.

    Various networks - network.

    Roles - role.

    Local users - user.

    Appliances - appliance.

    Security configurations - security_config.

    Certificates - certificate.

    Active directories - ad.

    LDAPs - ldap.

    DNS servers - dns.

    NTP servers - ntp.

    Email notification destinations - email_notification.

    SMTP configurations - smtp_config.

    Remote Support - remote_support.

    Remote support contacts - remote_support_contact.

    LDAP accounts - ldap_account.

    LDAP domain - ldap_domain.

    All vCenters - vcenter.

    Virtual volumes - virtual_volume.


  filters (False, list, None)
    A list of filters to support filtered output for storage entities.

    Each filter is a list of filter_key, filter_operator, filter_value.

    Supports passing of multiple filters.


    filter_key (True, str, None)
      Name identifier of the filter.


    filter_operator (True, str, None)
      Operation to be performed on the filter key.


    filter_value (True, str, None)
      Value of the filter key.



  all_pages (optional, bool, False)
    Indicates whether to return all available entities on the storage system.

    If set to True, the Info module will implement pagination and return all entities. Otherwise, a maximum of the first 100 entities of any type will be returned.


  array_ip (True, str, None)
    IP or FQDN of the PowerStore management system.


  verifycert (True, bool, None)
    Boolean variable to specify whether to validate SSL certificate or not.

    True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.

    False - indicates that the SSL certificate should not be verified.


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
   - Pagination is not supported for role, local user, security configs, LDAP accounts and LDAP domain. If all_pages is passed, it will be ignored.
   - The check_mode is supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    

    - name: Get list of volumes, volume groups, hosts, host groups and node
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
          - vol
          - vg
          - host
          - hg
          - node

    - name: Get list of replication related entities
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
          - replication_rule
          - replication_session
          - remote_system

    - name: Get list of volumes whose state notequal to ready
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
          - vol
        filters:
          - filter_key: "state"
            filter_operator: "notequal"
            filter_value: "ready"

    - name: Get list of protection policies and snapshot rules
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
          - protection_policy
          - snapshot_rule

    - name: Get list of snapshot rules whose desired_retention between 101-499
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
          - snapshot_rule
        filters:
          - filter_key: "desired_retention"
            filter_operator: "greater"
            filter_value: "100"
          - filter_key: "desired_retention"
            filter_operator: "lesser"
            filter_value: "500"

    - name: Get list of nas server, nfs_export and smb share
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
          - nas_server
          - nfs_export
          - smb_share

    - name: Get list of tree quota, user quota and file system
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
          - tree_quota
          - user_quota
          - file_system

    - name: Get list of nas server whose name equal to 'nas_server'
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
          - nas_server
        filters:
          - filter_key: "name"
            filter_operator: "equal"
            filter_value: "nas_server"

    - name: Get list of smb share whose name contains 'share'
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
          - nas_server
        filters:
          - filter_key: "name"
            filter_operator: "like"
            filter_value: "*share*"

    - name: Get list of user, role, network and appliances
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
          - user
          - role
          - network
          - appliance

    - name: Get list of ad, certificate, security config and ldaps
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
          - ad
          - ldap
          - certificate
          - security_config

    - name: Get list of networks whose name contains 'Management'
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
          - network
        filters:
          - filter_key: "name"
            filter_operator: "like"
            filter_value: "*Management*"

    - name: Get list of dns, email notification, ntp, remote support, remote support contact and smtp config
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
          - dns
          - email_notification
          - ntp
          - remote_support
          - remote_support_contact
          - smtp_config

    - name: Get list of emails which receives minor notifications
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
        - email_notification
        filters:
            - filter_key: 'notify_minor'
              filter_operator: 'equal'
              filter_value: 'False'

    - name: Get list of LDAP accounts
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
          - ldap_account

    - name: Get list of LDAP accounts with type as "User"
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
        - ldap_account
        filters:
            - filter_key: 'type'
              filter_operator: 'equal'
              filter_value: 'User'

    - name: Get list of LDAP domain
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
          - ldap_domain

    - name: Get list of LDAP domain with protocol as "LDAPS"
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
        - ldap_domain
        filters:
            - filter_key: 'protocol'
              filter_operator: 'equal'
              filter_value: 'LDAPS'

    - name: Get list of vCenters
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
          - vcenter

    - name: Get list of virtual volumes
      dellemc.powerstore.info:
        array_ip: "{{array_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        gather_subset:
          - virtual_volume




Return Values
-------------

changed (always, bool, false)
  Shows whether or not the resource has changed.


Array_Software_Version (always, str, 2.1.0.0)
  API version of PowerStore array.


ActiveDirectory (When ad is in a given gather_subset, list, [{'id': '60866158-5d00-3d7a-971b-5adabf42d82c'}])
  Provides details of all active directories.


  id (, str, )
    ID of the active directory.



Appliance (When appliance is in a given gather_subset, list, [{'id': 'A1', 'model': 'PowerStore 1000T', 'name': 'Appliance-WND8977'}])
  Provides details of all appliances.


  id (, str, )
    ID of the appliance.


  name (, str, )
    Name of the appliance.


  model (, str, )
    Model type of the PowerStore.



Certificate (When certificates is in a given gather_subset, list, [{'id': 'e940144f-393f-4e9c-8f54-9a4d57b38c48'}])
  Provides details of all certificates.


  id (, str, )
    ID of the certificate.



Cluster (always, list, [{'id': '0', 'name': 'RT-D1006'}])
  Provides details of all clusters.


  id (always, str, )
    ID of the cluster.


  name (always, str, )
    Name of the cluster.



DNS (When dns is in a given gather_subset, list, [{'id': 'DNS1'}])
  Provides details of all DNS servers.


  id (always, str, )
    ID of the DNS server.



EmailNotification (When email_notification is in a given gather_subset, list, [{'email_address': 'abc', 'id': '9c3e5cba-17d5-4d64-b97c-350f91e2b714'}])
  Provides details of all emails to which notifications will be sent.


  id (always, str, )
    ID of the email.


  email_address (always, str, )
    Email address.



FileSystems (When file_system is in a given gather_subset, list, [{'id': '61ef399b-f4c4-ccb6-1761-16c6ac7490fc', 'name': 'test_fs'}])
  Provides details of all filesystems.


  id (, str, )
    ID of the filesystem.


  name (, str, )
    Name of the filesystem.



HostGroups (When hg is in a given gather_subset, list, [{'id': 'f62b97b4-f262-417c-8dc9-39bec9024665', 'name': 'test_hg'}])
  Provides details of all host groups.


  id (, str, )
    ID of the host group.


  name (, str, )
    Name of the host group.



Hosts (When host is in a given gather_subset, list, [{'id': '42a0d739-20e6-49ec-afa6-65d2b3c006c8', 'name': 'test_host'}])
  Provides details of all hosts.


  id (, str, )
    ID of the host.


  name (, str, )
    Name of the host.



LDAP (When ldap is in a given gather_subset, list, [{'id': '60ba0edd-551a-64f1-ce49-8a83a5bce479'}])
  Provides details of all LDAPs.


  id (, str, )
    ID of the LDAP.



LDAPAccounts (When LDAP account is in a given gather_subset, list, [{'id': '5', 'role_id': '1', 'domain_id': '2', 'name': 'sample_ldap_user', 'type': 'User', 'type_l10n': 'User', 'dn': 'cn=sample_ldap_user,dc=ldap,dc=com'}])
  Provides details of all LDAP accounts.


  id (, str, )
    ID of the LDAP account.


  role_id (, int, )
    Unique identifier of the role to which the LDAP account is mapped.


  domain_id (, int, )
    Unique identifier of the LDAP domain to which LDAP user or group belongs.


  name (, str, )
    Name of the LDAP account.


  type (, str, )
    Type of LDAP account.


  dn (, str, )
    Types of directory service protocol.



LDAPDomain (When LDAP domain configuration is in a given gather_subset, list, [{'id': '9', 'domain_name': 'domain.com', 'port': 636, 'protocol': 'LDAPS', 'protocol_l10n': 'LDAPS', 'bind_user': 'cn=ldapadmin,dc=domain,dc=com', 'ldap_timeout': 300000, 'ldap_server_type': 'OpenLDAP', 'ldap_server_type_l10n': 'OpenLDAP', 'is_global_catalog': False, 'user_id_attribute': 'uid', 'user_object_class': 'inetOrgPerson', 'user_search_path': 'dc=domain,dc=com', 'group_name_attribute': 'cn', 'group_member_attribute': 'member', 'group_object_class': 'groupOfNames', 'group_search_path': 'dc=domain,dc=com', 'group_search_level': 0, 'ldap_servers': ['10.xxx.xx.xxx']}])
  Provides details of the LDAP domain configurations.


  id (, str, )
    Unique identifier of the new LDAP server configuration.


  domain_name (, str, )
    Name of the LDAP authority to construct the LDAP server configuration.


  ldap_servers (, list, )
    List of IP addresses of the LDAP servers for the domain. IP addresses are in IPv4 format.


  port (, int, )
    Port number used to connect to the LDAP server(s).


  ldap_server_type (, str, )
    Types of LDAP server.


  protocol (, str, )
    Types of directory service protocol.


  bind_user (, str, )
    Distinguished Name (DN) of the user to be used when binding.


  ldap_timeout (, int, )
    Timeout for establishing a connection to an LDAP server. Default value is 30000 (30 seconds).


  is_global_catalog (, bool, )
    Whether or not the catalog is global. Default value is false.


  user_id_attribute (, str, )
    Name of the LDAP attribute whose value indicates the unique identifier of the user.


  user_object_class (, str, )
    LDAP object class for users.


  user_search_path (, str, )
    Path used to search for users on the directory server.


  group_name_attribute (, str, )
    Name of the LDAP attribute whose value indicates the group name.


  group_member_attribute (, str, )
    Name of the LDAP attribute whose value contains the names of group members within a group.


  group_object_class (, str, )
    LDAP object class for groups.


  group_search_path (, str, )
    Path used to search for groups on the directory server.


  group_search_level (, int, )
    Nested search level for performing group search.


  ldap_server_type_l10n (, str, )
    Localized message string corresponding to ldap_server_type.


  protocol_l10n (, str, )
    Localized message string corresponding to protocol.



LocalUsers (When user is in a given gather_subset, list, [{'id': '1', 'name': 'admin'}])
  Provides details of all local users.


  id (, str, )
    ID of the user.


  name (, str, )
    Name of the user.



NASServers (When nas_server is in a given gather_subset, list, [{'id': '61e1c9bb-b791-550e-a785-16c6ac7490fc', 'name': 'test_nas'}])
  Provides details of all nas servers.


  id (, str, )
    ID of the nas server.


  name (, str, )
    Name of the nas server.



Networks (When network is in a given gather_subset, list, [{'id': 'NW1', 'name': 'Default Management Network'}])
  Provides details of all networks.


  id (, str, )
    ID of the network.


  name (, str, )
    Name of the network.



NFSExports (When nfs_export is in a given gather_subset, list, [{'id': '61ef39a0-09b3-5339-c8bb-16c6ac7490fc', 'name': 'test_nfs'}])
  Provides details of all nfs exports.


  id (, str, )
    ID of the nfs export.


  name (, str, )
    Name of the nfs export.



Nodes (When a node is in a given gather_subset, list, [{'id': 'N1', 'name': 'Appliance-RT-D1006-node-A'}])
  Provides details of all nodes.


  id (, str, )
    ID of the node.


  name (, str, )
    Name of the node.



NTP (When ntp is in a given gather_subset, list, [{'id': 'NTP1'}])
  Provides details of all NTP servers.


  id (always, str, )
    ID of the NTP server.



ProtectionPolicies (When protection_policy is in a given gather_subset, list, [{'id': '4eff379c-090c-48e0-9949-b2cd0ce2cf88', 'name': 'test_protection_policy'}])
  Provides details of all protection policies.


  id (, str, )
    ID of the protection policy.


  name (, str, )
    Name of the protection policy.



RemoteSupport (When remote_support is in a given gather_subset, list, [{'id': '0'}])
  Provides details of all remote support config.


  id (, str, )
    ID of the remote support.



RemoteSupportContact (When remote_support_contact is in a given gather_subset, list, [{'id': '0'}, {'id': '1'}])
  Provides details of all remote support contacts.


  id (, str, )
    ID of the remote support contact.



ReplicationRules (When replication_rule is in a given gather_subset, list, [{'id': '55d14477-de22-4d39-b24d-07cf08ba329f', 'name': 'ansible_rep_rule'}])
  Provides details of all replication rules.


  id (, str, )
    ID of the replication rule.


  name (, str, )
    Name of the replication rule.



ReplicationSession (when replication_session given in gather_subset, list, [{'id': '0b0a7ae9-c0c4-4dce-8c49-570f4ea80bb0'}])
  Details of all replication sessions.


  id (, str, )
    ID of the replication session.



RemoteSystems (When remote_system is in a given gather_subset, list, [{'id': 'f07be373-dafd-4a46-8b21-f7cf790c287f', 'name': 'WN-D8978'}])
  Provides details of all remote systems.


  id (, str, )
    ID of the remote system.


  name (, str, )
    Name of the remote system.



Roles (When role is in a given gather_subset, list, [{'id': '1', 'name': 'Administrator'}, {'id': '2', 'name': 'Storage Administrator'}, {'id': '3', 'name': 'Operator'}, {'id': '4', 'name': 'VM Administrator'}, {'id': '5', 'name': 'Security Administrator'}, {'id': '6', 'name': 'Storage Operator'}])
  Provides details of all roles.


  id (, str, )
    ID of the role.


  name (, str, )
    Name of the role.



SecurityConfig (When security_config is in a given gather_subset, list, [{'id': '1'}])
  Provides details of all security configs.


  id (, str, )
    ID of the security config.



SMBShares (When smb_share is in a given gather_subset, list, [{'id': '72ef39a0-09b3-5339-c8bb-16c6ac7490fc', 'name': 'test_smb'}])
  Provides details of all smb shares.


  id (, str, )
    ID of the smb share.


  name (, str, )
    name of the smb share.



SMTPConfig (When smtp_config is in a given gather_subset, list, [{'id': '0'}])
  Provides details of all smtp config.


  id (, str, )
    ID of the smtp config.



SnapshotRules (When snapshot_rule is in a given gather_subset, list, [{'id': 'e1b1bc3e-f8a1-4c81-a143-9ffd6af55837', 'name': 'Snapshot Rule Test'}])
  Provides details of all snapshot rules.


  id (, str, )
    ID of the snapshot rule.


  name (, str, )
    Name of the snapshot rule.



VolumeGroups (When vg is in a given gather_subset, list, [{'id': 'faaa8370-c62e-4fa2-b8ca-7f54419a5b40', 'name': 'Volume Group Test'}])
  Provides details of all volume groups.


  id (, str, )
    ID of the volume group.


  name (, str, )
    Name of the volume group.



Volumes (When vol is in a given gather_subset, list, [{'id': '01854336-94ef-4df9-b1e7-0a729ca7c944', 'name': 'test_vol'}])
  Provides details of all volumes.


  id (, str, )
    ID of the volume.


  name (, str, )
    Name of the volume.



TreeQuotas (When tree_quota is in a given gather_subset, list, [{'id': '00000003-0fe0-0001-0000-0000e8030000'}])
  Provides details of all tree quotas.


  id (, str, )
    ID of the tree quota.


  path (, str, )
    Path of the tree quota.



UserQuotas (When user_quota is in a given gather_subset, list, [{'id': '00000003-0708-0000-0000-000004000080'}])
  Provides details of all user quotas.


  id (, str, )
    ID of the user quota.



vCenter (When vCenter is in a given gather_subset, list, [{'id': '0d330d6c-3fe6-41c6-8023-5bd3fa7c61cd', 'instance_uuid': '0d330d6c-3fe6-41c6-8023-5bd3fa7c61cd', 'address': '10.x.x.x', 'username': 'administrator', 'version': '7.0.3', 'vendor_provider_status': 'Online', 'vendor_provider_status_l10n': 'Online', 'virtual_machines': [], 'datastores': [], 'vsphere_hosts': []}])
  Provide details of all vCenters.


  id (, str, )
    Unique identifier of vCenter.


  instance_uuid (, str, )
    UUID instance of vCenter.


  address (, str, )
    IP address of vCenter host, in IPv4, IPv6 or hostname format.


  username (, str, )
    Username to login to vCenter.


  version (, str, )
    Version of vCenter including its build number. Was added in PowerStore version 3.0.0.0.


  vendor_provider_status (, str, )
    General status of the VASA vendor provider in vCenter.


  vendor_provider_status_l10n (, str, )
    Localized message string corresponding to vendor_provider_status.


  virtual_machines (, list, )
    Virtual Machine associated with vCenter.


  datastores (, list, )
    Datastores that exists on a specific vCenter. Was added in PowerStore version 3.0.0.0.


  vsphere_hosts (, list, )
    All vSphere hosts that exists on a specific vCenter. Was added in PowerStore version 3.0.0.0.



VirtualVolume (When virtual_volume is in a given gather_subset, list, [{'id': '85643b54-9429-49ee-b7c3-b061fcdaab7c', 'name': 'test-centos_2.vmdk', 'size': 17179869184, 'type': 'Primary', 'usage_type': 'Data', 'appliance_id': 'A1', 'storage_container_id': '4dff1460-4d1e-48b6-98d8-cae8d7bf63b5', 'io_priority': 'Medium', 'profile_id': 'f4e5bade-15a2-4805-bf8e-52318c4ce443', 'replication_group_id': None, 'creator_type': 'User', 'is_readonly': False, 'migration_session_id': None, 'virtual_machine_uuid': '503629e5-8677-b26f-bf2d-e9f639bcc77f', 'family_id': '9ce8d828-14e3-44f8-bde1-a97f440a7259', 'parent_id': None, 'source_id': None, 'source_timestamp': None, 'creation_timestamp': '2022-12-27T10:01:32.622+00:00', 'naa_name': 'naa.68ccf09800918d7f008769d29bc6a43a', 'is_replication_destination': False, 'location_history': None, 'protection_policy_id': None, 'nsid': 5114, 'nguid': 'nguid.918d7f008769d29b8ccf096800c6a43a', 'type_l10n': 'Primary', 'usage_type_l10n': 'Data', 'io_priority_l10n': 'Medium', 'creator_type_l10n': 'User', 'host_virtual_volume_mappings': []}])
  Provides details of all virtual volumes.


  id (, str, )
    The unique identifier of the virtual volume.


  name (, str, )
    The name of the virtual volume, based on metadata provided by vSphere.


  size (, int, )
    The size of the virtual volume in bytes.


  type (, str, )
    The logical type of a virtual volume.


  usage_type (, str, )
    VMware's usage of the vVol.


  appliance_id (, str, )
    The appliance where the virtual volume resides.


  storage_container_id (, str, )
    The storage container where the virtual volume resides.


  io_priority (, str, )
    The I/O priority for quality of service rules.


  profile_id (, str, )
    The ID of the storage profile governing this virtual volume.


  replication_group_id (, str, )
    The unique identifier of the replication group object that this virtual volume belongs to.


  creator_type (, str, )
    Creator type of the storage resource.

    User - A resource created by a user.

    System - A resource created by the replication engine.

    Scheduler - A resource created by the snapshot scheduler.


  is_readonly (, bool, )
    Indicates whether the virtual volume is read-only.


  migration_session_id (, str, )
    If the virtual volume is part of a migration activity, the session ID for that migration.


  virtual_machine_uuid (, str, )
    UUID of the virtual machine that owns this virtual volume.


  family_id (, str, )
    Family id of the virtual volume.


  parent_id (, str, )
    For snapshots and clones, the ID of the parent virtual volume.


  source_id (, str, )
    Id of the virtual volume from which the content has been sourced.


  source_timestamp (, str, )
    The source data time-stamp of the virtual volume.


  creation_timestamp (, str, )
    Timestamp of the moment virtual volume was created at.


  naa_name (, str, )
    The NAA name used by hosts for I/O.


  is_replication_destination (, bool, )
    Indicates whether virtual volume is replication destination or not.


  location_history (, complex, )
    Storage resource location history.


    from_appliance_id (, str, )
      Unique identifier of the appliance from which the volume was relocated.


    to_appliance_id (, str, )
      Unique identifier of the appliance to which the volume was relocated.


    reason (, str, )
      Reason for storage resource relocation.

      Initial - Initial placement.

      Manual - Manual migration operation initiated by user.

      Recommended - Storage system recommended migration.


    migrated_on (, str, )
      Time when the storage resource location changed.


    reason_l10n (, str, )
      Localized message string corresponding to reason.



  protection_policy_id (, str, )
    The unique identifier of the protection policy applied to this virtual volume.


  nsid (, str, )
    NVMe Namespace unique identifier in the NVMe subsystem.


  nguid (, str, )
    NVMe Namespace globally unique identifier.


  type_l10n (, str, )
    Localized message string corresponding to type.


  usage_type_l10n (, str, )
    Localized message string corresponding to usage_type.


  io_priority_l10n (, str, )
    Localized message string corresponding to io_priority.


  creator_type_l10n (, str, )
    Localized message string corresponding to creator_type.


  host_virtual_volume_mappings (, complex, )
    Virtual volume mapping details.


    id (, str, )
      Unique identifier of a mapping between a host and a virtual volume.


    host_id (, str, )
      Unique identifier of a host attached to a virtual volume.


    host_group_id (, str, )
      Unique identifier of a host group attached to a virtual volume.


    virtual_volume_id (, str, )
      Unique identifier of the virtual volume to which the host is attached.







Status
------





Authors
~~~~~~~

- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
- Vivek Soni (@v-soni11) <ansible.team@dell.com>
- Akash Shendge (@shenda1) <ansible.team@dell.com>
- Bhavneet Sharma (@sharmb5) <ansible.team@dell.com>
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>

