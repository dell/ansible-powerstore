# ansible-powerstore Change Log
## Version 1.6.0 - released on 28/06/2022
- Added CRUD operations for LDAP domain and LDAP account.
- Added execution environment manifest file to support building an execution environment with ansible-builder.
- Info module is enhanced to list ldap domain, ldap accounts.
- Enabled the check_mode support for info module

## Version 1.5.0 - released on 25/03/2022
- Added CRUD operations and sending test email for email module.
- DNS module is added to get the details and add/remove addresses.
- NTP module is added to get the details and add/remove addresses.
- Remote support module is added to get the details, modify the attributes, verify the connection and send a test alert.
- Remote support contact module is added to get the details and modify the attributes.
- SMTP config module is added to get the details, modify the attributes and send a test email.
- Info module is enhanced to list dns servers, email notification destinations, NTP servers, remote support configuration, remote support contacts and SMTP configuration.

## Version 1.4.0 - released on 16/12/2021
- Added CRUD operations for remote system.
- Certificate module is added to get the details, add/import a certificate, exchange certificate, reset certificates and modify attributes of network.
- Security config module is added to get the details and modify attributes of a security configuration.
- Host module is enhanced to provide support for NVMe initiators.
- Info module is enhanced to list certificates, AD/LDAP providers and security configuration.
- Names of previously released modules have been changed from dellemc_powerstore_\<module name> to \<module name>.

## Version 1.3.0 - released on 28/09/2021
- Added dual licensing.
- Added CRUD operations for local user.
- Network module is added to get the details and modify attributes of network.
- Cluster module is added to get the details and modify attributes of cluster.
- Job module is added to get the details of given job ID.
- Role module is added to get the details of given role name or role ID.
- Gather facts module is enhanced to list users, roles, networks and appliances.

## Version 1.2.0 - released on 25/06/2021
- Added CRUD operations for replication rule.
- Replication session module is added to get the details and modify state of replication session.
- Protection policy module is enhanced to add/remove replication rule to/from protection policy.
- Gather facts module is enhanced to list remote systems, replication rules and replication sessions.

## Version 1.1.0 - released on 25/09/2020
- Added CRUD operations for filesystem.
- Added CRUD operations for NFS export.
- Added CRUD operations for SMB share.
- Added CRUD operations for quota.
- Added CRUD operations for filesystem snapshot.
- NAS server module is added to get and modify NAS server attributes.
- Gather facts module is enhanced to list filesystems, NAS servers, NFS exports, SMB shares, tree quotas, user quotas.

## Version 1.0.0 - released on 06/05/2020
- Added CRUD operations for volume.
- Added CRUD operations for volume group.
- Added CRUD operations for host.
- Added CRUD operations for host group.
- Added CRUD operations for volume and volume group snapshot.
- Added CRUD operations for snapshot rule.
- Added CRUD operations for protection policy.
- Gather facts module is added to list nodes, volumes, volume groups, hosts, host groups, snapshot rules, protection policies.
