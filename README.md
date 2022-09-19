# Ansible Modules for Dell Technologies PowerStore
The Ansible Modules for Dell Technologies (Dell) PowerStore allow Data Center and IT administrators to use RedHat Ansible to automate and orchestrate the configuration and management of Dell PowerStore arrays.

The capabilities of the Ansible modules are managing volumes, volume groups, hosts, host groups, snapshots, snapshot rules, replication rules, replication sessions, protection policies, file systems, NAS servers, SMB shares, user and tree quotas, file system snapshots, NFS exports, Clusters, Networks, Local users, Jobs, Roles, Certificates, Remote systems, security configuration, DNS server, Email notification destination, NTP server, Remote support configuration, Remote support contacts, SMTP configuration, LDAP accounts and LDAP domain configuration. It also allows gathering high level info from the array. The options available for each are list, show, create, modify and delete. These tasks can be executed by running simple playbooks written in yaml syntax. The modules are written so that all the operations are idempotent, so making multiple identical requests has the same effect as making a single request.
## Table of contents

* [Code of conduct](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/CODE_OF_CONDUCT.md)
* [Maintainer guide](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/MAINTAINER_GUIDE.md)
* [Committer guide](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/COMMITTER_GUIDE.md)
* [Contributing guide](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/CONTRIBUTING.md)
* [Branching strategy](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/BRANCHING.md)
* [List of adopters](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/ADOPTERS.md)
* [Maintainers](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/MAINTAINERS.md)
* [Support](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/SUPPORT.md)
* [License](#license)
* [Security](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/SECURITY.md)
* [Prerequisites](#prerequisites)
* [List of Ansible modules for Dell PowerStore](#list-of-ansible-modules-for-dell-powerstore)
* [Installation and execution of Ansible modules for Dell PowerStore](#installation-and-execution-of-ansible-modules-for-dell-powerstore)
* [Maintenance](#maintenance)

## License
The Ansible collection for PowerStore is released and licensed under the GPL-3.0 license. See [LICENSE](https://github.com/dell/ansible-powerstore/blob/1.7.0/LICENSE) for the full terms. Ansible modules and modules utilities that are part of the Ansible collection for PowerStore are released and licensed under the Apache 2.0 license. See [MODULE-LICENSE](https://github.com/dell/ansible-powerstore/blob/1.7.0/MODULE-LICENSE) for the full terms.

## Prerequisites

   | **Ansible Modules** | **PowerStore Version** | **Red Hat Enterprise Linux**| **SDK version** | **Python version** | **Ansible**              |
|---------------------|-----------------------|------------------------------|-----------------|--------------------|--------------------------|
| v1.7.0              | 2.0.x <br> 2.1.x <br> 3.0.x |7.9 <br> 8.4 <br> 8.5| 1.8.0           | 3.8.x <br> 3.9.x <br> 3.10.x | 2.11 <br> 2.12 <br> 2.13 |


  * Please follow PyPowerStore installation instructions on [PyPowerStore Documentation](https://github.com/dell/python-powerstore)

## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. It essentially means that the result of a successfully performed request is independent of the number of times it is executed.

## List of Ansible Modules for Dell PowerStore
* [Volume module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#volume-module)
* [Volume group module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#volume-group-module)
* [Host module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#host-module)
* [Host group module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#host-group-module)
* [Snapshot module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#snapshot-module)
* [Snapshot rule module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#snapshot-rule-module)
* [Replication rule module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#replication-rule-module)
* [Replication session module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#replication-session-module)
* [Protection policy module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#protection-policy-module)
* [Info module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#info-module)
* [File system module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#file-system-module)
* [NAS server module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#nas-server-module)
* [SMB share module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#smb-share-module)
* [Quota module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#quota-module)
* [File system snapshot module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#filesystem-snapshot-module)
* [NFS export module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#nfs-export-module)
* [Cluster module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#cluster-module)
* [Network module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#network-module)
* [Local user module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#local-user-module)
* [Role module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#role-module)
* [Job module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#job-module)
* [Certificate module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#certificate-module)
* [Remote system module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#remote-system-module)
* [Security config module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#security-config-module)
* [DNS module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#dns-module)
* [Email module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#email-module)
* [NTP module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#ntp-module)
* [Remote support module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#remote-support-module)
* [Remote support contact module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#remote-support-contact-module)
* [SMTP config module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#smtp-config-module)
* [LDAP Account module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#ldap-account-module)
* [LDAP Domain module](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/Product%20Guide.md#ldap-domain-module)

## Installation and execution of Ansible modules for Dell PowerStore
The installation and execution steps of Ansible modules for Dell PowerStore can be found [here](https://github.com/dell/ansible-powerstore/blob/1.7.0/docs/INSTALLATION.md)

## Maintenance
Ansible Modules for Dell Technologies PowerStore deprecation cycle is aligned with [Ansible](https://docs.ansible.com/ansible/latest/dev_guide/module_lifecycle.html).