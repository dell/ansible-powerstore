# ansible-powerstore Change Log
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
