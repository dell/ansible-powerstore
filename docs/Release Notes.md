**Ansible Modules for Dell Technologies PowerStore**
=========================================
### Release Notes 1.5.0

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
| 01       | March 2022  | Current release of Ansible Modules for Dell PowerStore 1.5.0 |

Product Description
-------------------
The Ansible modules for Dell PowerStore are used to automate and orchestrate the deployment, configuration, and management of Dell PowerStore storage systems. The capabilities of Ansible modules are managing Volumes, Volume groups, Hosts, Host groups, Protection policies, Replication rules, Replication sessions, NFS exports, SMB shares, NAS server, File systems, File system snapshots, Tree quotas, User quotas, Clusters, Networks, Local users, Roles, Jobs, Certificates, Remote systems, Security Configuration, DNS server, Email notification destinations, NTP server, Remote support contacts, Remote support configuration, SMTP configuration, and obtaining high-level information about a PowerStore system. The options available are list, show, create, delete, and modify.

New features & enhancements
---------------------------
Along with the previous release deliverables, this release supports these features -

-   DNS module supports these functionalities:
    -   Get DNS server details.
    -   Add/Remove addresses to/from a DNS server.

-   Email module supports these functionalities:
    -   Get email notification destination details.
    -   Add an email notification destination.
    -   Modify attributes of the email notification destination.
    -   Send a test alert to the email notification destination. 
    -   Delete an email notification destination.

-   NTP module supports these functionalities:
    -   Get NTP server details.
    -   Add/Remove addresses to/from an NTP server.

-   Remote support module has these functionalities:
    -   Get Remote support details.
    -   Modify attributes of a Remote support configuration.
    -   Verify a remote support configuration.
    -   Send test alert from the remote support configuration.

-   Remote support contact module has these functionalities:
    -   Get Remote support contact details.
    -   Modify attributes of a Remote support contact.

-   SMTP configuration module has these functionalities:
    -   Get SMTP configuration details.
    -   Modify attributes of an SMTP configuration.
    -   Send a test email from the SMTP configuration.
    
-   Info(Gather facts renamed) module has these enhancements:
    -  List of DNS servers.
    -  List of email notification destinations.
    -  List of NTP servers.
    -  List of remote support configurations.
    -  List of remote support contacts.
    -  List of SMTP configurations.

Known issues
------------
- Importing and modifying a certificate might not be successful in certain PowerStore system due to some open issues.

Limitations
-----------
-   All occurrences of Password and related parameters do not support Idempotency.
-   Exchange, reset and add/import of certificates do not support Idempotency.
-   Verify connection  and send test alert for remote support module do not support Idempotency.
-   Sending test alert through SMTP configuration and Email module does not support Idempotency.

Distribution
----------------
The software package is available for download from the [Ansible Modules
for PowerStore GitHub](https://github.com/dell/ansible-powerstore/tree/1.5.0) page.

Documentation
-------------
The documentation is available on [Ansible Modules for PowerStore GitHub](https://github.com/dell/ansible-powerstore/tree/1.5.0/docs)
page. It includes these:
- README
- Release Notes (this document)
- Product Guide
