**Ansible Modules for Dell Technologies PowerStore**
=========================================
### Release Notes 1.6.0

>   © 2022 Dell Inc. or its subsidiaries. All rights reserved. Dell,
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
-   [Known Issues](#known-issues)
-   [Limitations](#limitations)
-   [Distribution](#distribution)
-   [Documentation](#documentation)

Revision history
----------------
The table in this section lists the revision history of this document.

Table 1. Revision history

| Revision | Date      | Description                                               |
|----------|-----------|-----------------------------------------------------------|
| 01       | June 2022  | Current release of Ansible Modules for Dell PowerStore 1.6.0 |

Product Description
-------------------
The Ansible modules for Dell PowerStore are used to automate and orchestrate the deployment, configuration, and management of Dell PowerStore storage systems. The capabilities of Ansible modules are managing Volumes, Volume groups, Hosts, Host groups, Protection policies, Replication rules, Replication sessions, NFS exports, SMB shares, NAS server, File systems, File system snapshots, Tree quotas, User quotas, Clusters, Networks, Local users, Roles, Jobs, Certificates, Remote systems, Security Configuration, DNS server, Email notification destinations, NTP server, Remote support contacts, Remote support configuration, SMTP configuration, LDAP accounts, LDAP domain, and obtaining high-level information about a PowerStore system. The options available are list, show, create, delete, and modify.

New features & enhancements
---------------------------
Along with the previous release deliverables, this release supports these features -

-   LDAP account module supports these functionalities:
    -   Get LDAP account details.
    -   Create an LDAP account.
    -   Modify attributes of an LDAP account.
    -   Delete an LDAP account.

-   LDAP domain module supports these functionalities:
    -   Get LDAP domain configuration details.
    -   Configure an LDAP domain.
    -   Modify attributes of an LDAP domain configuration.
    -   Verify an LDAP domain configuration.
    -   Delete an LDAP domain configuration.
    
-   Info module has these enhancements:
    -  List of LDAP accounts.
    -  List of LDAP domain configurations.
    -  Enabled check mode support.
    
- Added execution environment manifest file to support building an execution environment with ansible-builder.

Known issues
------------
There are no known issues.

Limitations
-----------
-   All occurrences of Password and related parameters do not support Idempotency.
-   Exchange, reset and add/import of certificates do not support Idempotency.
-   Verify connection  and send test alert for remote support module do not support Idempotency.
-   Sending test alert through SMTP configuration and Email module does not support Idempotency.
-   Verify operation for LDAP domain module does not support Idempotency.

Distribution
----------------
The software package is available for download from the [Ansible Modules
for PowerStore GitHub](https://github.com/dell/ansible-powerstore/tree/1.6.0) page.

Documentation
-------------
The documentation is available on [Ansible Modules for PowerStore GitHub](https://github.com/dell/ansible-powerstore/tree/1.6.0/docs)
page. It includes these:
- README
- Release Notes (this document)
- Product Guide
