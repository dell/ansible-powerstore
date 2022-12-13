================================
Dellemc.Powerstore Change Logs
================================

.. contents:: Topics


v1.8.0
======

Minor Changes
-------------

- Added support for PowerStore version 3.2.0.0.
- Added support for host connectivity option to host and host group.
- Added support to clone, refresh and restore a volume.
- Added support to configure/remove the metro relationship for volume.
- Added support to modify the role of replication sessions.
- Updated modules to adhere with ansible community guidelines.

v1.7.0
======

Minor Changes
-------------

- Added support for cluster creation and validating cluster creation attributes.
- Added support to associate/disassociate protection policy to/from a NAS server.
- Added support to clone, refresh and restore a volume group.
- Added support to handle filesystem and NAS server replication sessions.

v1.6.0
======

Minor Changes
-------------

- Added execution environment manifest file to support building an execution environment with ansible-builder.
- Enabled the check_mode support for info module.
- Info module is enhanced to list ldap domain, ldap accounts.

New Modules
-----------

- dellemc.powerstore.ldap_account - Manage LDAP account on Dell PowerStore
- dellemc.powerstore.ldap_domain - Manage LDAP domain on Dell PowerStore

v1.5.0
======

Minor Changes
-------------

- Info module is enhanced to list dns servers, email notification destinations, NTP servers, remote support configuration, remote support contacts and SMTP configuration.
- Remote support module is added to get the details, modify the attributes, verify the connection and send a test alert.

New Modules
-----------

- dellemc.powerstore.dns - Manage DNS on Dell PowerStore
- dellemc.powerstore.email - Manage email on Dell PowerStore
- dellemc.powerstore.ntp - Manage NTP on Dell PowerStore
- dellemc.powerstore.remote_support - Manage Remote support on Dell PowerStore
- dellemc.powerstore.remote_support_contact - Manage Remote support contact on Dell PowerStore
- dellemc.powerstore.smtp_config - Manage SMTP config on Dell PowerStore

v1.4.0
======

Minor Changes
-------------

- Host module is enhanced to provide support for NVMe initiators.
- Info module is enhanced to list certificates, AD/LDAP providers and security configuration.
- Names of previously released modules have been changed from dellemc_powerstore_\<module name> to \<module name>.

New Modules
-----------

- dellemc.powerstore.certificate - Manage Certificates on Dell PowerStore
- dellemc.powerstore.remotesystem - Manage Remote system on Dell PowerStore
- dellemc.powerstore.security_config - Manage Security config on Dell PowerStore

v1.3.0
======

Minor Changes
-------------

- Added dual licensing.
- Gather facts module is enhanced to list users, roles, networks and appliances.

New Modules
-----------

- dellemc.powerstore.cluster - Manage Cluster on Dell PowerStore
- dellemc.powerstore.job - Manage Job on Dell PowerStore
- dellemc.powerstore.local_user - Manage local user on Dell PowerStore
- dellemc.powerstore.network - Manage Network operations on Dell PowerStore
- dellemc.powerstore.role - Manage Roles on Dell PowerStore

v1.2.0
======

Minor Changes
-------------

- Gather facts module is enhanced to list remote systems, replication rules and replication sessions.
- Protection policy module is enhanced to add/remove replication rule to/from protection policy.

New Modules
-----------

- dellemc.powerstore.replicationrule - Manage Replication Rules on Dell PowerStore
- dellemc.powerstore.replicationsession - Manage Replication Session on Dell PowerStore

v1.1.0
======

Minor Changes
-------------

- Gather facts module is enhanced to list filesystems, NAS servers, NFS exports, SMB shares, tree quotas, user quotas.

New Modules
-----------

- dellemc.powerstore.filesystem - Manage File System on Dell PowerStore
- dellemc.powerstore.filesystem_snapshot - Manage Filesystem Snapshot on Dell PowerStore
- dellemc.powerstore.nasserver - Manage NAS server on Dell PowerStore
- dellemc.powerstore.nfs - Manage NFS Export on Dell PowerStore
- dellemc.powerstore.quota - Manage Quota on Dell PowerStore
- dellemc.powerstore.smbshare - Manage SMB Share on Dell PowerStore
- dellemc.powerstore.snapshot - Manage Snapshot on Dell PowerStore

v1.0.0
======

New Modules
-----------

- dellemc.powerstore.host - Managing Dell PowerStore host
- dellemc.powerstore.hostgroup - Manage host group on Dell PowerStore
- dellemc.powerstore.info - Gathering information about Dell PowerStore
- dellemc.powerstore.protectionpolicy - Manage Protection policies on Dell PowerStore
- dellemc.powerstore.snapshotrule - Manage Snapshot Rule on Dell PowerStore
- dellemc.powerstore.volume - Manage volumes on Dell PowerStore
- dellemc.powerstore.volumegroup - Manage volume group on Dell PowerStore