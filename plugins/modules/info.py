#!/usr/bin/python
# Copyright: (c) 2019-2021, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: info
version_added: '1.0.0'
short_description: Gathers information about PowerStore Storage entities
description:
- Gathers the list of specified PowerStore Storage System entities, includes
  block/file provisioning modules, replication modules, configuration modules,
  and virtualization modules.
- Block provisioning module includes volumes, volume groups, hosts,
  host groups, snapshot rules, and protection policies.
- File provisioning module includes NAS servers, NFS exports, SMB shares,
  tree quotas, user quotas, and file systems.
- Replication module includes replication rules, replication sessions,
  replication groups, and remote system.
- Virtualization module includes vCenters and virtual volumes.
- Configuration module includes cluster nodes, networks, roles, local users,
  appliances, discovered appliances, security configs, certificates,
  AD/LDAP servers, LDAP accounts, and LDAP domain.
- It also includes DNS/NTP servers, smtp configs, email destinations,
  remote support, and remote support contacts.
author:
- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
- Vivek Soni (@v-soni11) <ansible.team@dell.com>
- Akash Shendge (@shenda1) <ansible.team@dell.com>
- Bhavneet Sharma (@sharmb5) <ansible.team@dell.com>
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>
extends_documentation_fragment:
  - dellemc.powerstore.powerstore
options:
  gather_subset:
    description:
    - A list of string variables which specify the PowerStore system entities
      requiring information.
    - Volumes - C(vol).
    - All the nodes - C(node).
    - Volume groups - C(vg).
    - Protection policies - C(protection_policy).
    - Hosts - C(host).
    - Host groups - C(hg).
    - Snapshot rules - C(snapshot_rule).
    - NAS servers - C(nas_server).
    - NFS exports - C(nfs_export).
    - SMB shares - C(smb_share).
    - Tree quotas - C(tree_quota).
    - User quotas - C(user_quota).
    - File systems - C(file_system).
    - Replication rules - C(replication_rule).
    - Replication sessions - C(replication_session).
    - Remote systems - C(remote_system).
    - Various networks - C(network).
    - Roles - C(role).
    - Local users - C(user).
    - Appliances - C(appliance).
    - Security configurations - C(security_config).
    - Certificates - C(certificate).
    - Active directories - C(ad).
    - LDAPs - C(ldap).
    - DNS servers - C(dns).
    - NTP servers - C(ntp).
    - Email notification destinations - C(email_notification).
    - SMTP configurations - C(smtp_config).
    - Remote Support - C(remote_support).
    - Remote support contacts - C(remote_support_contact).
    - LDAP accounts - C(ldap_account).
    - LDAP domain - C(ldap_domain).
    - All vCenters - C(vcenter).
    - Virtual volumes - C(virtual_volume).
    - Storage containers - C(storage_container).
    - Replication groups - C(replication_group).
    - Discovered appliances - C(discovered_appliance).
    required: true
    elements: str
    choices: [vol, vg, host, hg, node, protection_policy, snapshot_rule,
              nas_server, nfs_export, smb_share, tree_quota, user_quota,
              file_system, replication_rule, replication_session,
              remote_system, network, role, ldap_account, user, appliance, ad,
              ldap, security_config, certificate, dns, ntp, smtp_config,
              email_notification, remote_support, remote_support_contact,
              ldap_domain, vcenter, virtual_volume, storage_container,
              replication_group, discovered_appliance]
    type: list
  filters:
    description:
    - A list of filters to support filtered output for storage entities.
    - Each filter is a list of I(filter_key), I(filter_operator), I(filter_value).
    - Supports passing of multiple filters.
    type: list
    elements: dict
    suboptions:
      filter_key:
        description:
        - Name identifier of the filter.
        type: str
        required: true
      filter_operator:
        description:
        - Operation to be performed on the filter key.
        type: str
        choices: [equal, greater, lesser, like, notequal]
        required: true
      filter_value:
        description:
        - Value of the filter key.
        type: str
        required: true
  all_pages:
    description:
    - Indicates whether to return all available entities on the storage
      system.
    - If set to C(true), the Info module will implement pagination and
      return all entities. Otherwise, a maximum of the first 100 entities of
      any type will be returned.
    type: bool
    default: false
notes:
- Pagination is not supported for role, local user, security configs, LDAP
  accounts, discovered appliances and LDAP domain. If I(all_pages) is passed,
  it will be ignored.
- The I(check_mode) is supported.
'''

EXAMPLES = r'''

- name: Get list of volumes, volume groups, hosts, host groups and node
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
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
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - replication_rule
      - replication_session
      - remote_system

- name: Get list of volumes whose state notequal to ready
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
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
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - protection_policy
      - snapshot_rule

- name: Get list of snapshot rules whose desired_retention between 101-499
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
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
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - nas_server
      - nfs_export
      - smb_share

- name: Get list of tree quota, user quota and file system
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - tree_quota
      - user_quota
      - file_system

- name: Get list of nas server whose name equal to 'nas_server'
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
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
    validate_certs: "{{validate_certs}}"
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
    validate_certs: "{{validate_certs}}"
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
    validate_certs: "{{validate_certs}}"
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
    validate_certs: "{{validate_certs}}"
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
    validate_certs: "{{validate_certs}}"
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
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
    - email_notification
    filters:
        - filter_key: 'notify_minor'
          filter_operator: 'equal'
          filter_value: 'false'

- name: Get list of LDAP accounts
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - ldap_account

- name: Get list of LDAP accounts with type as "User"
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
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
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - ldap_domain

- name: Get list of LDAP domain with protocol as "LDAPS"
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
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
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - vcenter

- name: Get list of virtual volumes
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - virtual_volume
      - replication_group

- name: Get list of storage containers and discovered appliances
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - storage_container
      - discovered_appliance
'''

RETURN = r'''
changed:
    description: Shows whether or not the resource has changed.
    returned: always
    type: bool
    sample: 'false'

Array_Software_Version:
    description: API version of PowerStore array.
    returned: always
    type: str
    sample: "2.2.0.0"
ActiveDirectory:
    description: Provides details of all active directories.
    type: list
    returned: When C(ad) is in a given I(gather_subset)
    contains:
        id:
            description: ID of the active directory.
            type: str
    sample: [
          {
            "id": "60866158-5d00-3d7a-971b-5adabf42d82c"
          }
    ]
Appliance:
    description: Provides details of all appliances.
    type: list
    returned: When C(appliance) is in a given I(gather_subset)
    contains:
        id:
            description: ID of the appliance.
            type: str
        name:
            description: Name of the appliance.
            type: str
        service_tag:
            description: Dell service tag of the appliance.
            type: str
        express_service_code:
            description: Express service code.
            type: str
        model:
            description: Model type of the PowerStore.
            type: str
        node_count:
            description: Number of nodes deployed on an appliance. It was added
                         in version 3.0.0.0.
            type: int
        drive_failure_tolerance_level:
            description: Drive failure tolerance level.
            type: str
        is_hyper_converged:
            description: Whether the appliance is a hyper-converged appliance.
                         It was added in version 3.2.0.0.
            type: bool
        nodes:
            description: Provides details of all nodes.
            type: list
        ip_pool_addresses:
            description: Provides details of all IP pool addresses.
            type: list
        veth_ports:
            description: Provides details of all veth ports.
            type: list
        virtual_volumes:
            description: Provides details of all virtual volumes.
            type: list
        maintenance_windows:
            description: Provides details of all maintenance windows.
            type: list
        fc_ports:
            description: Provides details of all FC ports.
            type: list
        sas_ports:
            description: Provides details of all SAS ports.
            type: list
        eth_ports:
            description: Provides details of all Ethernet ports.
            type: list
        eth_be_ports:
            description: Provides details of all eth_be_ports. It was added in
                         version 3.0.0.0.
            type: list
        software_installed:
            description: Provides details of all software installed.
            type: list
        hardware:
            description: Provides details of all hardware.
            type: list
        volumes:
            description: Provides details of all volumes.
            type: list
    sample: [
        {
            "id": "A1",
            "name": "Appliance-WND8977",
            "service_tag": "A1",
            "express_service_code": "A1",
            "model": "PowerStore 1000T",
            "node_count": 1,
            "drive_failure_tolerance_level": "None",
            "is_hyper_converged": false,
            "nodes": [],
            "ip_pool_addresses": [],
            "veth_ports": [],
            "virtual_volumes": [],
            "maintenance_windows": [],
            "fc_ports": [],
            "sas_ports": [],
            "eth_ports": [],
            "eth_be_ports": [],
            "software_installed": [],
            "hardware": [],
            "volumes": []
        }
    ]
Certificate:
    description: Provides details of all certificates.
    type: list
    returned: When C(certificates) is in a given I(gather_subset)
    contains:
        id:
            description: ID of the certificate.
            type: str
    sample: [
          {
            "id": "e940144f-393f-4e9c-8f54-9a4d57b38c48"
          }
    ]
Cluster:
    description: Provides details of all clusters.
    type: list
    returned: always
    contains:
        id:
            description: ID of the cluster.
            type: str
            returned: always
        name:
            description: Name of the cluster.
            type: str
            returned: always
    sample: [
          {
              "id": "0",
              "name": "RT-D1006"
          }
    ]
DiscoveredAppliances:
    description: Provides details of all discovered appliances.
    type: list
    returned: When C(discovered_appliance) is in a given I(gather_subset)
    contains:
        id:
            description: ID of a discovered appliance. The local discovered
                         appliance has the id "0".
            type: str
        link_local_address:
            description: Link local IPv4 address of the discovered appliance.
            type: str
        service_name:
            description: Service name of the discovered appliance.
            type: str
        service_tag:
            description: The Dell service tag.
            type: str
        state:
            description: Possible unmanaged appliance states.
            type: str
        mode:
            description: Storage access mode supported by the appliance.
            type: str
        model:
            description: The model of the appliance.
            type: str
        express_service_code:
            description: Express service code for the appliance.
            type: str
        is_local:
            description: Indicates whether appliance is local or not.
            type: bool
        management_service_ready:
            description: Indicates whether the management services are ready.
            type: bool
        software_version_compatibility:
            description: Compatibility of the software version on an appliance
                         compared to the software version on the appliance
                         running the request.
            type: str
        build_version:
            description: Build version of the installed software package
                         release.
            type: str
        build_id:
            description: Build ID.
            type: str
        power_score:
            description: Power rating of the appliance.
            type: int
        node_count:
            description: Number of nodes deployed on an appliance.
            type: int
        is_unified_capable:
            description: Indicates whether the appliance is capable of unified
                         configuration.
            type: bool
        drive_failure_tolerance_level_and_availability:
            description: Drive failure tolerance level and availability.
            type: list
        is_hyper_converged:
            description: Indicates whether the appliance is a hyper converged
                         or not. It was added in version 3.2.0.0.
            type: bool
    sample: [
        {
            "id": "A1",
            "link_local_address": "1.0.2.x",
            "service_name": "Appliance-WND8977",
            "service_tag": "A8977",
            "state": "Unconfigured",
            "mode": "Unified",
            "model": "PowerStore 1000T",
            "express_service_code": "A8977",
            "is_local": true,
            "management_service_ready": true,
            "software_version_compatibility": "3.0.0.0",
            "build_version": "3.0.0.0",
            "build_id": "3202",
            "power_score": 0,
            "node_count": 2,
            "is_unified_capable": true,
            "is_hyper_converged": false
        }
    ]
DNS:
    description: Provides details of all DNS servers.
    type: list
    returned: When C(dns) is in a given I(gather_subset)
    contains:
        id:
            description: ID of the DNS server.
            type: str
            returned: always
    sample: [
          {
            "id": "DNS1"
          }
    ]
EmailNotification:
    description: Provides details of all emails to which notifications will be sent.
    type: list
    returned: When C(email_notification) is in a given I(gather_subset)
    contains:
        id:
            description: ID of the email.
            type: str
            returned: always
        email_address:
            description: Email address.
            type: str
            returned: always
    sample: [
          {
            "email_address": "abc",
            "id": "9c3e5cba-17d5-4d64-b97c-350f91e2b714"
          }
    ]
FileSystems:
    description: Provides details of all filesystems.
    type: list
    returned: When C(file_system) is in a given I(gather_subset)
    contains:
        id:
            description: ID of the filesystem.
            type: str
        name:
            description: Name of the filesystem.
            type: str
    sample: [
          {
            "id": "61ef399b-f4c4-ccb6-1761-16c6ac7490fc",
            "name": "test_fs"
          }
    ]
HostGroups:
    description: Provides details of all host groups.
    type: list
    returned: When C(hg) is in a given I(gather_subset)
    contains:
        id:
            description: ID of the host group.
            type: str
        name:
            description: Name of the host group.
            type: str
    sample: [
          {
            "id": "f62b97b4-f262-417c-8dc9-39bec9024665",
            "name": "test_hg"
          }
    ]
Hosts:
    description: Provides details of all hosts.
    type: list
    returned: When C(host) is in a given I(gather_subset)
    contains:
        id:
            description: ID of the host.
            type: str
        name:
            description: Name of the host.
            type: str
    sample: [
          {
            "id": "42a0d739-20e6-49ec-afa6-65d2b3c006c8",
            "name": "test_host"
          }
    ]
LDAP:
    description: Provides details of all LDAPs.
    type: list
    returned: When C(ldap) is in a given I(gather_subset)
    contains:
        id:
            description: ID of the LDAP.
            type: str
    sample: [
          {
            "id": "60ba0edd-551a-64f1-ce49-8a83a5bce479"
          }
    ]
LDAPAccounts:
    description: Provides details of all LDAP accounts.
    type: list
    returned: When C(ldap_account) is in a given I(gather_subset)
    contains:
        id:
            description: ID of the LDAP account.
            type: str
        role_id:
            description: Unique identifier of the role to which the LDAP account is mapped.
            type: int
        domain_id:
            description: Unique identifier of the LDAP domain to which LDAP user or group belongs.
            type: int
        name:
            description: Name of the LDAP account.
            type: str
        type:
            description: Type of LDAP account.
            type: str
        dn:
            description: Types of directory service protocol.
            type: str
    sample: [
        {
            "id": "5",
            "role_id": "1",
            "domain_id": "2",
            "name": "sample_ldap_user",
            "type": "User",
            "type_l10n": "User",
            "dn": "cn=sample_ldap_user,dc=ldap,dc=com"
        }
    ]
LDAPDomain:
    description: Provides details of the LDAP domain configurations.
    type: list
    returned: When C(ldap_domain) configuration is in a given I(gather_subset)
    contains:
        id:
            description: Unique identifier of the new LDAP server configuration.
            type: str
        domain_name:
            description: Name of the LDAP authority to construct the LDAP server configuration.
            type: str
        ldap_servers:
            description: List of IP addresses of the LDAP servers for the domain. IP addresses are in IPv4 format.
            type: list
        port:
            description: Port number used to connect to the LDAP server(s).
            type: int
        ldap_server_type:
            description: Types of LDAP server.
            type: str
        protocol:
            description: Types of directory service protocol.
            type: str
        bind_user:
            description: Distinguished Name (DN) of the user to be used when binding.
            type: str
        ldap_timeout:
            description: Timeout for establishing a connection to an LDAP server. Default value is 30000 (30 seconds).
            type: int
        is_global_catalog:
            description: Whether or not the catalog is global. Default value is C(false).
            type: bool
        user_id_attribute:
            description: Name of the LDAP attribute whose value indicates the unique identifier of the user.
            type: str
        user_object_class:
            description: LDAP object class for users.
            type: str
        user_search_path:
            description: Path used to search for users on the directory server.
            type: str
        group_name_attribute:
            description: Name of the LDAP attribute whose value indicates the group name.
            type: str
        group_member_attribute:
            description: Name of the LDAP attribute whose value contains the names of group members within a group.
            type: str
        group_object_class:
            description: LDAP object class for groups.
            type: str
        group_search_path:
            description: Path used to search for groups on the directory server.
            type: str
        group_search_level:
            description: Nested search level for performing group search.
            type: int
        ldap_server_type_l10n:
            description: Localized message string corresponding to ldap_server_type.
            type: str
        protocol_l10n:
            description: Localized message string corresponding to protocol.
            type: str
    sample: [
        {
            "id": "9",
            "domain_name": "domain.com",
            "port": 636,
            "protocol": "LDAPS",
            "protocol_l10n": "LDAPS",
            "bind_user": "cn=ldapadmin,dc=domain,dc=com",
            "ldap_timeout": 300000,
            "ldap_server_type": "OpenLDAP",
            "ldap_server_type_l10n": "OpenLDAP",
            "is_global_catalog": false,
            "user_id_attribute": "uid",
            "user_object_class": "inetOrgPerson",
            "user_search_path": "dc=domain,dc=com",
            "group_name_attribute": "cn",
            "group_member_attribute": "member",
            "group_object_class": "groupOfNames",
            "group_search_path": "dc=domain,dc=com",
            "group_search_level": 0,
            "ldap_servers": [
                "10.xxx.xx.xxx"
            ]
        }
    ]
LocalUsers:
    description: Provides details of all local users.
    type: list
    returned: When C(user) is in a given I(gather_subset)
    contains:
        id:
            description: ID of the user.
            type: str
        name:
            description: Name of the user.
            type: str
    sample: [
          {
            "id": "1",
            "name": "admin"
          }
    ]
NASServers:
    description: Provides details of all nas servers.
    type: list
    returned: When C(nas_server) is in a given I(gather_subset)
    contains:
        id:
            description: ID of the nas server.
            type: str
        name:
            description: Name of the nas server.
            type: str
    sample: [
          {
              "id": "61e1c9bb-b791-550e-a785-16c6ac7490fc",
              "name": "test_nas"
          }
    ]
Networks:
    description: Provides details of all networks.
    type: list
    returned: When C(network) is in a given I(gather_subset)
    contains:
        id:
            description: ID of the network.
            type: str
        name:
            description: Name of the network.
            type: str
    sample: [
          {
            "id": "NW1",
            "name": "Default Management Network"
          }
    ]
NFSExports:
    description: Provides details of all nfs exports.
    type: list
    returned: When C(nfs_export) is in a given I(gather_subset)
    contains:
        id:
            description: ID of the nfs export.
            type: str
        name:
            description: Name of the nfs export.
            type: str
    sample: [
          {
            "id": "61ef39a0-09b3-5339-c8bb-16c6ac7490fc",
            "name": "test_nfs"
          }
    ]
Nodes:
    description: Provides details of all nodes.
    type: list
    returned: When a C(node) is in a given I(gather_subset)
    contains:
        id:
            description: ID of the node.
            type: str
        name:
            description: Name of the node.
            type: str
    sample: [
          {
            "id": "N1",
            "name": "Appliance-RT-D1006-node-A"
          }
    ]
NTP:
    description: Provides details of all NTP servers.
    type: list
    returned: When C(ntp) is in a given I(gather_subset)
    contains:
          id:
            description: ID of the NTP server.
            type: str
            returned: always
    sample: [
          {
            "id": "NTP1"
          }
    ]
ProtectionPolicies:
    description: Provides details of all protection policies.
    type: list
    returned: When C(protection_policy) is in a given I(gather_subset)
    contains:
          id:
            description: ID of the protection policy.
            type: str
          name:
            description: Name of the protection policy.
            type: str
    sample: [
          {
            "id": "4eff379c-090c-48e0-9949-b2cd0ce2cf88",
            "name": "test_protection_policy"
          }
    ]
RemoteSupport:
    description: Provides details of all remote support config.
    type: list
    returned: When C(remote_support) is in a given I(gather_subset)
    contains:
          id:
            description: ID of the remote support.
            type: str
    sample: [
          {
            "id": "0"
          }
    ]
RemoteSupportContact:
    description: Provides details of all remote support contacts.
    type: list
    returned: When C(remote_support_contact) is in a given I(gather_subset)
    contains:
          id:
            description: ID of the remote support contact.
            type: str
    sample: [
          {
            "id": "0"
          },
          {
            "id": "1"
          }
    ]
ReplicationGroups:
    description: Provide details of all replication group.
    type: list
    returned: when C(replication_group) is in a given I(gather_subset).
    contains:
        id:
            description: ID of the replication group.
            type: str
        name:
            description: Name of the replication group.
            type: str
        storage_container_id:
            description: ID of the storage container.
            type: str
        description:
            description: Description of the replication group.
            type: str
        creator_type:
            description: Creator type of the storage resource.
            type: str
        creation_timestamp:
            description: Timestamp when given replication group was created.
            type: str
        is_replication_destination:
            description: Indicates whether replication group is replication
                         destination or not.
            type: bool
        creator_type_l10n:
            description: Localized message string corresponding to
                         creator_type.
            type: str
    sample: [
        {
            "id": "c4ba4ad3-2200-47d4-8f61-ddf51d83aac2",
            "storage_container_id": "0b460d65-b8b6-40bf-8578-aa2e2fd3d02a",
            "name": "Ansible_RTD8337_VM",
            "description": "Ansible_RTD8337_VM",
            "creator_type": "User",
            "creation_timestamp": "2023-05-16T13:58:09.348368+00:00",
            "is_replication_destination": false,
            "creator_type_l10n": "User"
        }
    ]
ReplicationRules:
    description: Provides details of all replication rules.
    type: list
    returned: When C(replication_rule) is in a given I(gather_subset)
    contains:
          id:
            description: ID of the replication rule.
            type: str
          name:
            description: Name of the replication rule.
            type: str
    sample: [
          {
            "id": "55d14477-de22-4d39-b24d-07cf08ba329f",
            "name": "ansible_rep_rule"
          }
    ]
ReplicationSession:
    description: Details of all replication sessions.
    type: list
    returned: when C(replication_session) given in I(gather_subset)
    contains:
          id:
            description: ID of the replication session.
            type: str
    sample: [
          {
            "id": "0b0a7ae9-c0c4-4dce-8c49-570f4ea80bb0"
          }
    ]
RemoteSystems:
    description: Provides details of all remote systems.
    type: list
    returned: When C(remote_system) is in a given I(gather_subset)
    contains:
          id:
            description: ID of the remote system.
            type: str
          name:
            description: Name of the remote system.
            type: str
    sample: [
          {
            "id": "f07be373-dafd-4a46-8b21-f7cf790c287f",
            "name": "WN-D8978"
          }
    ]
Roles:
    description: Provides details of all roles.
    type: list
    returned: When C(role is in a given I(gather_subset
    contains:
          id:
            description: ID of the role.
            type: str
          name:
            description: Name of the role.
            type: str
    sample: [
          {
            "id": "1",
            "name": "Administrator"
          },
          {
            "id": "2",
            "name": "Storage Administrator"
          },
          {
            "id": "3",
            "name": "Operator"
          },
          {
            "id": "4",
            "name": "VM Administrator"
          },
          {
            "id": "5",
            "name": "Security Administrator"
          },
          {
            "id": "6",
            "name": "Storage Operator"
          }
    ]
SecurityConfig:
    description: Provides details of all security configs.
    type: list
    returned: When C(security_config) is in a given I(gather_subset)
    contains:
          id:
            description: ID of the security config.
            type: str
    sample: [
          {
            "id": "1"
          }
    ]
SMBShares:
    description: Provides details of all smb shares.
    type: list
    returned: When C(smb_share) is in a given I(gather_subset)
    contains:
          id:
            description: ID of the smb share.
            type: str
          name:
            description: name of the smb share.
            type: str
    sample: [
          {
            "id": "72ef39a0-09b3-5339-c8bb-16c6ac7490fc",
            "name": "test_smb"
          }
    ]
SMTPConfig:
    description: Provides details of all smtp config.
    type: list
    returned: When C(smtp_config) is in a given I(gather_subset)
    contains:
          id:
            description: ID of the smtp config.
            type: str
    sample: [
          {
            "id": "0"
          }
    ]
SnapshotRules:
    description: Provides details of all snapshot rules.
    type: list
    returned: When C(snapshot_rule) is in a given I(gather_subset)
    contains:
          id:
            description: ID of the snapshot rule.
            type: str
          name:
            description: Name of the snapshot rule.
            type: str
    sample: [
          {
            "id": "e1b1bc3e-f8a1-4c81-a143-9ffd6af55837",
            "name": "Snapshot Rule Test"
          }
    ]
StorageContainers:
    description: Provide details of all storage containers.
    type: list
    returned: When C(storage_container) is in a given I(gather_subset)
    contains:
        id:
            description: ID of the storage container.
            type: str
        name:
            description: Name of the storage container.
            type: str
        storage_protocol:
            description: The type of storage container.
            type: str
        quota:
            description: The total number of bytes that can be
                         provisioned/reserved against this storage container.
            type: int
        replication_groups:
            description: Properties of a Replication Group.
            type: list
            contains:
                id:
                    description: Unique identifier of the Replication Group
                                 instance.
                    type: str
                name:
                    description: Name of the Replication Group.
                    type: str
        virtual_volumes:
            description: The virtual volumes associated to the storage container.
            type: list
            contains:
                id:
                    description: The unique identifier of the virtual volume.
                    type: str
                name:
                    description: The name of the virtual volume.
                    type: str
        destinations:
            description: A storage container destination defines replication
                         destination for a local storage container on a remote
                         system.
            type: list
            contains:
                id:
                    description: The unique id of the storage container
                                 destination.
                    type: str
                remote_system_id:
                    description: The unique id of the remote system.
                    type: str
                remote_system_name:
                    description: The name of the remote system.
                    type: str
                remote_storage_container_id:
                    description: The unique id of the destination storage
                                 container on the remote system.
                    type: str
        datastores:
            description: List of associated datastores.
            type: list
            contains:
                id:
                    description: Unique identifier of the datastore instance.
                    type: str
                name:
                    description: User-assigned name of the datastore in vCenter.
                    type: str
    sample: [
        {
            "datastores": [],
            "destinations": [],
            "id": "e0ccd953-5650-41d8-9bce-f36d876d6a2a",
            "name": "Ansible_storage_container_1",
            "quota": 21474836480,
            "replication_groups": [],
            "storage_protocol": "NVMe",
            "storage_protocol_l10n": "NVMe",
            "virtual_volumes": []
        }
    ]
VolumeGroups:
    description: Provides details of all volume groups.
    type: list
    returned: When C(vg) is in a given I(gather_subset)
    contains:
          id:
            description: ID of the volume group.
            type: str
          name:
            description: Name of the volume group.
            type: str
    sample: [
          {
            "id": "faaa8370-c62e-4fa2-b8ca-7f54419a5b40",
            "name": "Volume Group Test"
          }
    ]
Volumes:
    description: Provides details of all volumes.
    type: list
    returned: When C(vol) is in a given I(gather_subset)
    contains:
          id:
            description: ID of the volume.
            type: str
          name:
            description: Name of the volume.
            type: str
    sample: [
          {
            "id": "01854336-94ef-4df9-b1e7-0a729ca7c944",
            "name": "test_vol"
          }
        ]
TreeQuotas:
    description: Provides details of all tree quotas.
    type: list
    returned: When C(tree_quota) is in a given I(gather_subset)
    contains:
          id:
            description: ID of the tree quota.
            type: str
          path:
            description: Path of the tree quota.
            type: str
    sample: [
          {
            "id": "00000003-0fe0-0001-0000-0000e8030000"
          }
    ]
UserQuotas:
    description: Provides details of all user quotas.
    type: list
    returned: When C(user_quota) is in a given I(gather_subset)
    contains:
          id:
            description: ID of the user quota.
            type: str
    sample: [
          {
            "id": "00000003-0708-0000-0000-000004000080"
          }
    ]
vCenter:
    description: Provide details of all vCenters.
    type: list
    returned: When C(vCenter) is in a given I(gather_subset)
    contains:
        id:
            description: Unique identifier of vCenter.
            type: str
        instance_uuid:
            description: UUID instance of vCenter.
            type: str
        address:
            description: IP address of vCenter host, in IPv4, IPv6 or hostname
                         format.
            type: str
        username:
            description: Username to login to vCenter.
            type: str
        version:
            description: Version of vCenter including its build number. Was
                         added in PowerStore version 3.0.0.0.
            type: str
        vendor_provider_status:
            description: General status of the VASA vendor provider in vCenter.
            type: str
        vendor_provider_status_l10n:
            description: Localized message string corresponding to
                         vendor_provider_status.
            type: str
        virtual_machines:
            description: Virtual Machine associated with vCenter.
            type: list
        datastores:
            description: Datastores that exists on a specific vCenter. Was
                         added in PowerStore version 3.0.0.0.
            type: list
        vsphere_hosts:
            description: All vSphere hosts that exists on a specific vCenter.
                         Was added in PowerStore version 3.0.0.0.
            type: list
    sample: [
        {
            "id": "0d330d6c-3fe6-41c6-8023-5bd3fa7c61cd",
            "instance_uuid": "0d330d6c-3fe6-41c6-8023-5bd3fa7c61cd",
            "address": "10.x.x.x",
            "username": "administrator",
            "version": "7.0.3",
            "vendor_provider_status": "Online",
            "vendor_provider_status_l10n": "Online",
            "virtual_machines": [],
            "datastores": [],
            "vsphere_hosts": []
        }
    ]
VirtualVolume:
    description: Provides details of all virtual volumes.
    type: list
    returned: When C(virtual_volume) is in a given I(gather_subset)
    contains:
        id:
            description: The unique identifier of the virtual volume.
            type: str
        name:
            description: The name of the virtual volume, based on metadata provided by vSphere.
            type: str
        size:
            description: The size of the virtual volume in bytes.
            type: int
        type:
            description: The logical type of a virtual volume.
            type: str
        usage_type:
            description: VMware's usage of the vVol.
            type: str
        appliance_id:
            description: The appliance where the virtual volume resides.
            type: str
        storage_container_id:
            description: The storage container where the virtual volume resides.
            type: str
        io_priority:
            description: The I/O priority for quality of service rules.
            type: str
        profile_id:
            description: The ID of the storage profile governing this virtual volume.
            type: str
        replication_group_id:
            description: The unique identifier of the replication group object that this virtual volume belongs to.
            type: str
        creator_type:
            description:
            - Creator type of the storage resource.
            - User - A resource created by a user.
            - System - A resource created by the replication engine.
            - Scheduler - A resource created by the snapshot scheduler.
            type: str
        is_readonly:
            description: Indicates whether the virtual volume is read-only.
            type: bool
        migration_session_id:
            description: If the virtual volume is part of a migration activity, the session ID for that migration.
            type: str
        virtual_machine_uuid:
            description: UUID of the virtual machine that owns this virtual volume.
            type: str
        family_id:
            description: Family id of the virtual volume.
            type: str
        parent_id:
            description: For snapshots and clones, the ID of the parent virtual volume.
            type: str
        source_id:
            description: Id of the virtual volume from which the content has been sourced.
            type: str
        source_timestamp:
            description: The source data time-stamp of the virtual volume.
            type: str
        creation_timestamp:
            description: Timestamp of the moment virtual volume was created at.
            type: str
        naa_name:
            description: The NAA name used by hosts for I/O.
            type: str
        is_replication_destination:
            description: Indicates whether virtual volume is replication destination or not.
            type: bool
        location_history:
            description: Storage resource location history.
            type: complex
            contains:
                from_appliance_id:
                    description: Unique identifier of the appliance from which the volume was relocated.
                    type: str
                to_appliance_id:
                    description: Unique identifier of the appliance to which the volume was relocated.
                    type: str
                reason:
                    description:
                    - Reason for storage resource relocation.
                    - Initial - Initial placement.
                    - Manual - Manual migration operation initiated by user.
                    - Recommended - Storage system recommended migration.
                    type: str
                migrated_on:
                    description: Time when the storage resource location changed.
                    type: str
                reason_l10n:
                    description: Localized message string corresponding to reason.
                    type: str
        protection_policy_id:
            description: The unique identifier of the protection policy applied to this virtual volume.
            type: str
        nsid:
            description: NVMe Namespace unique identifier in the NVMe subsystem.
            type: str
        nguid:
            description: NVMe Namespace globally unique identifier.
            type: str
        type_l10n:
            description: Localized message string corresponding to type.
            type: str
        usage_type_l10n:
            description: Localized message string corresponding to usage_type.
            type: str
        io_priority_l10n:
            description: Localized message string corresponding to io_priority.
            type: str
        creator_type_l10n:
            description: Localized message string corresponding to creator_type.
            type: str
        host_virtual_volume_mappings:
            description: Virtual volume mapping details.
            type: complex
            contains:
                id:
                    description: Unique identifier of a mapping between a host and a virtual volume.
                    type: str
                host_id:
                    description: Unique identifier of a host attached to a virtual volume.
                    type: str
                host_group_id:
                    description: Unique identifier of a host group attached to a virtual volume.
                    type: str
                virtual_volume_id:
                    description: Unique identifier of the virtual volume to which the host is attached.
                    type: str

    sample: [
        {
            "id": "85643b54-9429-49ee-b7c3-b061fcdaab7c",
            "name": "test-centos_2.vmdk",
            "size": 17179869184,
            "type": "Primary",
            "usage_type": "Data",
            "appliance_id": "A1",
            "storage_container_id": "4dff1460-4d1e-48b6-98d8-cae8d7bf63b5",
            "io_priority": "Medium",
            "profile_id": "f4e5bade-15a2-4805-bf8e-52318c4ce443",
            "replication_group_id": null,
            "creator_type": "User",
            "is_readonly": false,
            "migration_session_id": null,
            "virtual_machine_uuid": "503629e5-8677-b26f-bf2d-e9f639bcc77f",
            "family_id": "9ce8d828-14e3-44f8-bde1-a97f440a7259",
            "parent_id": null,
            "source_id": null,
            "source_timestamp": null,
            "creation_timestamp": "2022-12-27T10:01:32.622+00:00",
            "naa_name": "naa.68ccf09800918d7f008769d29bc6a43a",
            "is_replication_destination": false,
            "location_history": null,
            "protection_policy_id": null,
            "nsid": 5114,
            "nguid": "nguid.918d7f008769d29b8ccf096800c6a43a",
            "type_l10n": "Primary",
            "usage_type_l10n": "Data",
            "io_priority_l10n": "Medium",
            "creator_type_l10n": "User",
            "host_virtual_volume_mappings": []
}
    ]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import utils

LOG = utils.get_logger('info')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/2.2.0'


class PowerstoreInfo(object):
    """Info operations"""
    cluster_name = ' '
    cluster_global_id = ' '
    filter_mapping = {'equal': 'eq.', 'greater': 'gt.', 'notequal': 'neq.',
                      'lesser': 'lt.', 'like': 'ilike.'}

    def __init__(self):
        self.result = {}
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_info_parameters())

        self.filter_keys = sorted(
            [k for k in self.module_params['filters']['options'].keys()
             if 'filter' in k])
        LOG.info("Self.filter_keys: %s", self.filter_keys)
        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True
        )

        LOG.info('HAS_PY4PS = %s, IMPORT_ERROR = %s', HAS_PY4PS, IMPORT_ERROR)
        if HAS_PY4PS is False:
            self.module.fail_json(msg=IMPORT_ERROR)
        LOG.info('IS_SUPPORTED_PY4PS_VERSION = %s , '
                 'VERSION_ERROR = %s', IS_SUPPORTED_PY4PS_VERSION,
                 VERSION_ERROR)
        if IS_SUPPORTED_PY4PS_VERSION is False:
            self.module.fail_json(msg=VERSION_ERROR)

        self.conn = utils.get_powerstore_connection(
            self.module.params,
            application_type=APPLICATION_TYPE)
        self.provisioning = self.conn.provisioning
        self.protection = self.conn.protection
        self.configuration = self.conn.config_mgmt

        self.subset_mapping = {
            'vol': {
                'func': self.provisioning.get_volumes,
                'display_as': 'Volumes'
            },
            'vg': {
                'func': self.provisioning.get_volume_group_list,
                'display_as': 'VolumeGroups'
            },
            'host': {
                'func': self.provisioning.get_hosts,
                'display_as': 'Hosts'
            },
            'hg': {
                'func': self.provisioning.get_host_group_list,
                'display_as': 'HostGroups'
            },
            'node': {
                'func': self.provisioning.get_nodes,
                'display_as': 'Nodes'
            },
            'protection_policy': {
                'func': self.protection.get_protection_policies,
                'display_as': 'ProtectionPolicies'
            },
            'snapshot_rule': {
                'func': self.protection.get_snapshot_rules,
                'display_as': 'SnapshotRules'
            },
            'replication_group': {
                'func': self.protection.get_replication_groups,
                'display_as': 'ReplicationGroups'
            },
            'replication_rule': {
                'func': self.protection.get_replication_rules,
                'display_as': 'ReplicationRules'
            },
            'replication_session': {
                'func': self.protection.get_replication_sessions,
                'display_as': 'ReplicationSessions'
            },
            'remote_system': {
                'func': self.protection.get_remote_systems,
                'display_as': 'RemoteSystems'
            },
            'nas_server': {
                'func': self.provisioning.get_nas_servers,
                'display_as': 'NASServers'
            },
            'nfs_export': {
                'func': self.provisioning.get_nfs_exports,
                'display_as': 'NFSExports'
            },
            'smb_share': {
                'func': self.provisioning.get_smb_shares,
                'display_as': 'SMBShares'
            },
            'tree_quota': {
                'func': self.provisioning.get_file_tree_quotas,
                'display_as': 'TreeQuotas'
            },
            'user_quota': {
                'func': self.provisioning.get_file_user_quotas,
                'display_as': 'UserQuotas'
            },
            'file_system': {
                'func': self.provisioning.get_file_systems,
                'display_as': 'FileSystems'
            },
            'network': {
                'func': self.configuration.get_networks,
                'display_as': 'Networks'
            },
            'role': {
                'func': self.configuration.get_roles,
                'display_as': 'Roles'
            },
            'user': {
                'func': self.configuration.get_local_users,
                'display_as': 'LocalUsers'
            },
            'appliance': {
                'func': self.configuration.get_appliances,
                'display_as': 'Appliance'
            },
            'ad': {
                'func': self.provisioning.get_file_ads,
                'display_as': 'ActiveDirectory'
            },
            'ldap': {
                'func': self.provisioning.get_file_ldaps,
                'display_as': 'LDAP'
            },
            'certificate': {
                'func': self.configuration.get_certificates,
                'display_as': 'Certificate'
            },
            'security_config': {
                'func': self.configuration.get_security_configs,
                'display_as': 'SecurityConfig'
            },
            'dns': {
                'func': self.configuration.get_dns_list,
                'display_as': 'DNS'
            },
            'ntp': {
                'func': self.configuration.get_ntp_list,
                'display_as': 'NTP'
            },
            'smtp_config': {
                'func': self.configuration.get_smtp_configs,
                'display_as': 'SMTPConfig'
            },
            'email_notification': {
                'func': self.configuration.get_destination_emails,
                'display_as': 'EmailNotification'
            },
            'remote_support': {
                'func': self.configuration.get_remote_support_list,
                'display_as': 'RemoteSupport'
            },
            'remote_support_contact': {
                'func': self.configuration.get_remote_support_contact_list,
                'display_as': 'RemoteSupportContact'
            },
            'ldap_account': {
                'func': self.configuration.get_ldap_account_list,
                'display_as': 'LDAPAccounts'
            },
            'ldap_domain': {
                'func': self.configuration.get_ldap_domain_configuration_list,
                'display_as': 'LDAPDomain'
            },
            'vcenter': {
                'func': self.configuration.get_vcenters,
                'display_as': 'vCenter'
            },
            'virtual_volume': {
                'func': self.configuration.get_virtual_volume_list,
                'display_as': 'VirtualVolume'
            },
            'storage_container': {
                'func': self.configuration.get_storage_container_list,
                'display_as': 'StorageContainers'
            },
            'discovered_appliance': {
                'func': self.configuration.get_discovered_appliances,
                'display_as': 'DiscoveredAppliances'
            }
        }
        LOG.info('Got Py4ps connection object %s', self.conn)

    def update_result_with_item_list(self, item, filter_dict=None,
                                     all_pages=False):
        """Update the result json with list of item of a given PowerStore
           storage system"""

        try:
            LOG.info('Getting %s list', item)
            if item not in ['role', 'user']:
                item_list = self.subset_mapping[item]['func'](
                    filter_dict=filter_dict, all_pages=all_pages)
            else:
                item_list = self.subset_mapping[item]['func'](
                    filter_dict=filter_dict)
            LOG.info('Successfully listed %s %s from powerstore array name: '
                     '%s , global id : %s', len(item_list), self.
                     subset_mapping[item]['display_as'], self.cluster_name,
                     self.cluster_global_id)
            d = {
                self.subset_mapping[item]['display_as']: item_list,
            }
            self.result.update(d)
        except Exception as e:
            msg = 'Get {0} for powerstore array name : {1} , global id : {2}'\
                  ' failed with error {3} '\
                .format(self.subset_mapping[item]['display_as'], self.
                        cluster_name, self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def validate_filter(self, filter_dict):
        """ Validate given filter_dict """

        is_invalid_filter = self.filter_keys != sorted(list(filter_dict))
        if is_invalid_filter:
            msg = "Filter should have all keys: '{0}'".format(
                ", ".join(self.filter_keys))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        is_invalid_filter = [filter_dict[i] is None for i in filter_dict]
        if True in is_invalid_filter:
            msg = "Filter keys: '{0}' cannot be None".format(self.filter_keys)
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_filters(self, filters):
        """Get the filters to be applied"""

        filter_dict = {}
        for item in filters:
            self.validate_filter(item)
            f_op = item['filter_operator']
            if self.filter_mapping.get(f_op):
                f_key = item['filter_key']
                f_val = self.filter_mapping[f_op] + item['filter_value']
                if f_key in filter_dict:
                    # multiple filters on same key
                    if isinstance(filter_dict[f_key], list):
                        # prev_val is list, so append new f_val
                        filter_dict[f_key].append(f_val)
                    else:
                        # prev_val is not list,
                        # so create list with prev_val & f_val
                        filter_dict[f_key] = [filter_dict[f_key], f_val]
                else:
                    filter_dict[f_key] = f_val
            else:
                msg = "Given filter operator '{0}' is not supported." \
                    "supported operators are : '{1}'".format(
                        f_op,
                        list(self.filter_mapping.keys()))
                LOG.error(msg)
                self.module.fail_json(msg=msg)
        return filter_dict

    def get_clusters(self):
        """Get the clusters"""
        try:
            clusters = self.provisioning.get_cluster_list()
            return clusters

        except Exception as e:
            msg = 'Failed to get the clusters with ' \
                  'error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_array_software_version(self):
        """Get array software version"""
        try:
            soft_ver = self.provisioning.get_array_version()
            msg = 'Got array software version as {0}'.format(soft_ver)
            LOG.info(msg)
            return soft_ver

        except Exception as e:
            msg = 'Failed to get the array software version with ' \
                  'error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def perform_module_operation(self):
        clusters = self.get_clusters()
        cluster_state = ''
        if len(clusters) > 0:
            self.cluster_name = clusters[0]['name']
            self.cluster_global_id = clusters[0]['id']
            cluster_state = clusters[0]['state']
        else:
            self.module.fail_json(msg="Unable to find any active cluster on"
                                      " this array ")

        self.result.update(Cluster=clusters,
                           Array_Software_Version=None)
        if cluster_state == 'Configured':
            array_soft_ver = self.get_array_software_version()
            self.result.update(Cluster=clusters,
                               Array_Software_Version=array_soft_ver)

        subset = self.module.params['gather_subset']
        filters = self.module.params['filters']
        all_pages = self.module.params['all_pages']

        filter_dict = {}
        if filters:
            filter_dict = self.get_filters(filters)
            LOG.info('filters: %s', filter_dict)
        if subset is not None:
            for item in subset:
                if item in self.subset_mapping:
                    self.update_result_with_item_list(
                        item, filter_dict=filter_dict, all_pages=all_pages)
                else:
                    self.module.fail_json(
                        msg="subset_mapping do not have details for '{0}'"
                            .format(item))
        else:
            self.module.fail_json(msg="No subset specified in gather_subset")

        self.module.exit_json(**self.result)


def get_powerstore_info_parameters():
    """This method provides the parameters required for the ansible modules on
       PowerStore"""
    return dict(
        all_pages=dict(type='bool', required=False, default=False),
        gather_subset=dict(
            type='list', required=True, elements='str',
            choices=['vol', 'vg', 'host', 'hg', 'node', 'protection_policy',
                     'snapshot_rule', 'nas_server', 'nfs_export', 'smb_share',
                     'tree_quota', 'user_quota', 'file_system',
                     'replication_rule', 'replication_session',
                     'remote_system', 'network', 'role', 'user', 'appliance',
                     'ad', 'ldap', 'security_config', 'certificate', 'dns',
                     'ntp', 'smtp_config', 'email_notification',
                     'remote_support', 'remote_support_contact',
                     'ldap_account', 'ldap_domain', 'vcenter',
                     'virtual_volume', 'storage_container',
                     'replication_group', 'discovered_appliance']),
        filters=dict(type='list', required=False, elements='dict',
                     options=dict(filter_key=dict(type='str', required=True,
                                                  no_log=False),
                                  filter_operator=dict(
                                      type='str',
                                      required=True,
                                      choices=['equal', 'greater',
                                               'notequal', 'lesser',
                                               'like']),
                                  filter_value=dict(type='str',
                                                    required=True))
                     )
    )


def main():
    """ Create PowerStore Info object and perform action on it
        based on user input from playbook """
    obj = PowerstoreInfo()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
