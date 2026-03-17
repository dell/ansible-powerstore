**Ansible Modules for Dell Technologies PowerStore**
=========================================
### Release Notes 3.8.1

>   © 2026 Dell Inc. or its subsidiaries. All rights reserved. Dell,
>   and other trademarks are trademarks of Dell Inc. or its
>   subsidiaries. Other trademarks may be trademarks of their respective
>   owners.

Content
-------
These release notes contain supplemental information about Ansible
Modules for Dell Technologies (Dell) PowerStore.

-   [Revision History](#revision-history)
-   [Product Description](#product-description)
-   [New Features & Enhancements](#new-features--enhancements)
-   [Bug Fixes](#bug-fixes)
-   [Known Issues](#known-issues)
-   [Limitations](#limitations)
-   [Distribution](#distribution)
-   [Documentation](#documentation)

Revision history
----------------
The table in this section lists the revision history of this document.

Table 1. Revision history

| Revision | Date         | Description                                               |
|----------|--------------|-----------------------------------------------------------|
| 03       | March 2026 | Ansible Modules for Dell PowerStore 3.8.1 |
| 02       | May 2025 | Ansible Modules for Dell PowerStore 3.8.0 |
| 01       | December 2024 | Ansible Modules for Dell PowerStore 3.7.0 |

Product Description
-------------------
The Ansible modules for Dell PowerStore are used to automate and orchestrate the deployment, configuration, and management of Dell PowerStore storage systems. The capabilities of Ansible modules are managing Volumes, Volume groups, Hosts, Host groups, Protection policies, Replication rules, Replication sessions, NFS exports, SMB shares, NAS server, File interfaces, File DNS, File NIS, SMB servers, NFS servers, service configurations, File systems, File system snapshots, Tree quotas, User quotas, Clusters, Networks, Local users, Roles, Jobs, Certificates, Remote systems, Security Configuration, DNS server, Email notification destinations, NTP server, Remote support contacts, Remote support configuration, SMTP configuration, LDAP accounts, LDAP domain, and obtaining high-level information about a PowerStore system. The options available are list, show, create, delete, and modify.

New features & enhancements
---------------------------
This section describes the features or enhancements of the Ansible Modules for Dell PowerStore for this release.

The Ansible Modules for Dell PowerStore release 3.8.1 provides the following enhancements:

- Added support for PowerStore v4.2 and v4.3.

Bug fixes
---------
This section describes the bug fixes for the Ansible Modules for Dell PowerStore for this release.

The following bugs have been fixed in version 3.8.1:

- Fixed hostname regex parsing in nfs.py module.
- Fixed issue where logfile is created in Ansible directory.
- Fixed host detailed initiator configuration not being properly updated.
- Added requirement notice for PyPowerStore python library installation.

Known issues
------------
Hosts in IPv4/prefix_length format do not get mapped to an NFS export in Foothills Prime version of PowerStore.

Limitations
-----------
- All occurrences of Password and related parameters do not support Idempotency.
- Exchange, reset and add/import of certificates do not support Idempotency.
- Verify connection  and send test alert for remote support module do not support Idempotency.
- Sending test alert through SMTP configuration and Email module does not support Idempotency.
- Verify operation for LDAP domain module does not support Idempotency.

Distribution
----------------
The software package is available for download from the [Ansible Modules
for PowerStore GitHub](https://github.com/dell/ansible-powerstore/tree/main) page.

Documentation
-------------
The documentation is available on [Ansible Modules for PowerStore GitHub](https://github.com/dell/ansible-powerstore/tree/main/docs)
page. It includes these:
- README
- Release Notes (this document)
