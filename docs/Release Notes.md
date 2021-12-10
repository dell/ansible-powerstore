**Ansible Modules for Dell EMC PowerStore**
=========================================
### Release Notes 1.4.0

>   © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell,
>   EMC, and other trademarks are trademarks of Dell Inc. or its
>   subsidiaries. Other trademarks may be trademarks of their respective
>   owners.

Content
-------
These release notes contain supplemental information about Ansible
Modules for Dell EMC PowerStore.

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
| 01       | December 2021  | Current release of Ansible Modules for Dell EMC PowerStore 1.4.0 |

Product Description
-------------------
The Ansible modules for Dell EMC PowerStore are used to automate and orchestrate the deployment, configuration, and management of Dell EMC PowerStore storage systems. The capabilities of Ansible modules are managing Volumes, Volume groups, Hosts, Host groups, Protection policies, Replication rules, Replication sessions, NFS exports, SMB shares, NAS server, File systems, File system snapshots, Tree quotas, User quotas, Cluster, Networks, Local users, Roles, Job, Certificates, Remote systems, Security Configuration and obtaining high-level information about a PowerStore system information. The options available are list, show, create, delete, and modify.

New features & enhancements
---------------------------
Along with the previous release deliverables, this release supports the following features -

-   Certificate module supports the following functionalities:
    -   Get certificate details
    -   Exchange certificate
    -   Reset certificate
    -   Add/import a certificate    
    -   Modify attributes of certificate

-   Remote system module supports the following functionalities:
    -   Get remote system details
    -   Add a remote system
    -   Modify attributes of the remote system
    -   Delete a remote system

-   Security config module has the following functionalities:
    -   Get security config details
    -   Modify attributes of security config

-   Host module has the following enhancements:
    -   Extended support for NVMe initiators
    
-   Info(Gather facts renamed) module has the following enhancements:
    -  List of AD providers
    -  List of certificates
    -  List of LDAP providers
    -  List of security configurations

Known issues
------------
- Importing and modifying a certificate might not be successful in certain PowerStore system due to some open issues.

Limitations
-----------
-   All occurrences of Password and related parameters do not support Idempotency.
-   Exchange, reset and add/import of certificates do not support Idempotency.

Distribution
----------------
The software package is available for download from the [Ansible Modules
for PowerStore GitHub](https://github.com/dell/ansible-powerstore/tree/1.4.0) page.

Documentation
-------------
The documentation is available on [Ansible Modules for PowerStore GitHub](../docs)
page. It includes the following:
- README
- Release Notes (this document)
- Product Guide
