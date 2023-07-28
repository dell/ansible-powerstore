# Ansible Modules for Dell Technologies PowerStore

The Ansible Modules for Dell Technologies (Dell) PowerStore allow Data Center and IT administrators to use RedHat Ansible to automate and orchestrate the configuration and management of Dell PowerStore arrays.

The capabilities of the Ansible modules are managing volumes, volume groups, vCenters, hosts, host groups, snapshots, snapshot rules, replication rules, replication sessions, protection policies, file systems, NAS servers, SMB shares, user and tree quotas, file system snapshots, NFS exports, Clusters, Networks, Local users, Jobs, Roles, Certificates, Remote systems, security configuration, DNS server, Email notification destination, NTP server, Remote support configuration, Remote support contacts, SMTP configuration, LDAP accounts, LDAP domain configuration and storage containers. It also allows gathering high level info from the array. The options available for each are list, show, create, modify and delete. These tasks can be executed by running simple playbooks written in yaml syntax. The modules are written so that all the operations are idempotent, so making multiple identical requests has the same effect as making a single request.
## Table of contents

* [Code of conduct](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/CODE_OF_CONDUCT.md)
* [Maintainer guide](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/MAINTAINER_GUIDE.md)
* [Committer guide](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/COMMITTER_GUIDE.md)
* [Contributing guide](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/CONTRIBUTING.md)
* [Branching strategy](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/BRANCHING.md)
* [List of adopters](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/ADOPTERS.md)
* [Maintainers](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/MAINTAINERS.md)
* [Support](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/SUPPORT.md)
* [License](#license)
* [Security](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/SECURITY.md)
* [Prerequisites](#prerequisites)
* [List of Ansible modules for Dell PowerStore](#list-of-ansible-modules-for-dell-powerstore)
* [Installation and execution of Ansible modules for Dell PowerStore](#installation-and-execution-of-ansible-modules-for-dell-powerstore)
* [Maintenance](#maintenance)

## License
The Ansible collection for PowerStore is released and licensed under the GPL-3.0 license. See [LICENSE](https://github.com/dell/ansible-powerstore/blob/2.1.0/LICENSE) for the full terms. Ansible modules and modules utilities that are part of the Ansible collection for PowerStore are released and licensed under the Apache 2.0 license. See [MODULE-LICENSE](https://github.com/dell/ansible-powerstore/blob/2.1.0/MODULE-LICENSE) for the full terms.

## Prerequisites

   | **Ansible Modules** | **PowerStore Version** | **SDK version** | **Python version** | **Ansible**              |
|---------------------|-----------------------|-----------------|--------------------|--------------------------|
| v2.1.0              | 3.0.x <br> 3.2.x <br> 3.5.x | 2.0.0          | 3.9.x <br> 3.10.x <br> 3.11.x | 2.13 <br> 2.14 <br> 2.15 |


  * Please follow PyPowerStore installation instructions on [PyPowerStore Documentation](https://github.com/dell/python-powerstore)

## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. It essentially means that the result of a successfully performed request is independent of the number of times it is executed.

## List of Ansible Modules for Dell PowerStore
* [Volume module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/volume.rst)
* [Volume group module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/volumegroup.rst)
* [Host module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/host.rst)
* [Host group module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/hostgroup.rst)
* [Snapshot module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/snapshot.rst)
* [Snapshot rule module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/snapshotrule.rst)
* [Replication rule module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/replicationrule.rst)
* [Replication session module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/replicationsession.rst)
* [Protection policy module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/protectionpolicy.rst)
* [Info module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/info.rst)
* [File system module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/filesystem.rst)
* [NAS server module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/nasserver.rst)
* [SMB share module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/smbshare.rst)
* [Quota module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/quota.rst)
* [File system snapshot module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/filesystem_snapshot.rst)
* [NFS export module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/nfs.rst)
* [Cluster module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/cluster.rst)
* [Network module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/network.rst)
* [Local user module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/local_user.rst)
* [Role module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/role.rst)
* [Job module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/job.rst)
* [Certificate module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/certificate.rst)
* [Remote system module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/remotesystem.rst)
* [Security config module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/security_config.rst)
* [DNS module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/dns.rst)
* [Email module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/email.rst)
* [NTP module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/ntp.rst)
* [Remote support module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/remote_support.rst)
* [Remote support contact module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/remote_support_contact.rst)
* [SMTP config module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/smtp_config.rst)
* [LDAP Account module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/ldap_account.rst)
* [LDAP Domain module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/ldap_domain.rst)
* [vCenter module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/vcenter.rst)
* [Storage container module](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/modules/storage_container.rst)

## Installation and execution of Ansible modules for Dell PowerStore
The installation and execution steps of Ansible modules for Dell PowerStore can be found [here](https://github.com/dell/ansible-powerstore/blob/2.1.0/docs/INSTALLATION.md)

## Maintenance
Ansible Modules for Dell Technologies PowerStore deprecation cycle is aligned with [Ansible](https://docs.ansible.com/ansible/latest/dev_guide/module_lifecycle.html).