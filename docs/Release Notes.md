**Ansible Modules for Dell EMC PowerStore** 
=========================================
### Release Notes 1.3.0

>   © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell,
>   EMC, and other trademarks are trademarks of Dell Inc. or its
>   subsidiaries. Other trademarks may be trademarks of their respective
>   owners.

Content
-------
These release notes contain supplemental information about Ansible
Modules for Dell EMC PowerStore.

-   Revision History
-   Product Description
-   New Features & Enhancements
-   Known Issues
-   Limitations
-   Distribution
-   Documentation

Revision history
----------------
The table in this section lists the revision history of this document.

Table 1. Revision history

| Revision | Date      | Description                                               |
|----------|-----------|-----------------------------------------------------------|
| 01       | September 2021  | Current release of Ansible Modules for Dell EMC PowerStore 1.3.0 |

Product Description
-------------------
The Ansible modules for Dell EMC PowerStore are used to automate and orchestrate the deployment, configuration, and management of Dell EMC PowerStore storage systems. The capabilities of Ansible modules are managing Volumes, Volume groups, Hosts, Host groups, Protection policies, Replication rules, Replication sessions, NFS exports, SMB shares, NAS server, File systems, File system snapshots, Quota tree, Quotas for filesystem, Cluster, Networks, Local users, Roles, Job, and obtaining PowerStore system information. The options available for each capability are list, show, create, delete, and modify. The only exception is for NAS server for which the options available are list & modify.

New features & enhancements
---------------------------
Along with the previous release deliverables, this release supports the following features -

-   Cluster module supports the following functionalities:
    -   Get cluster details    
    -   Modify attributes of cluster

-   Network module supports the following functionalities:
    -   Get network details    
    -   Modify attributes of the network

-   Local user module has the following functionalities:
    -   Create a local user
    -   Get local user details
    -   Modify attributes of local user
    -   Delete a local user

-   Role module has the following functionalities:
    -   Get role details

-   Job module has the following functionalities:
    -   Get job details for a given job ID
    
-   Gather Facts Module has the following enhancements:
    -  List of users
    -  List of roles
    -  List of networks
    -  List of appliances

Known issues
------------
There are no known issues.

Limitations
-----------
-   All occurrences of Password and related parameters do not support Idempotency.

Distribution
----------------
The software package is available for download from the [Ansible Modules
for PowerStore GitHub](https://github.com/dell/ansible-powerstore/) page.

Documentation
-------------
The documentation is available on [Ansible Modules for PowerStore GitHub](https://github.com/dell/ansible-powerstore/tree/1.2.0/docs)
page. It includes the following:
- README
- Release Notes (this document)
- Product Guide
