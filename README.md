# Ansible Modules for Dell Technologies PowerStore

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](https://github.com/dell/ansible-powerstore/blob/main/docs/CODE_OF_CONDUCT.md)
[![License](https://img.shields.io/github/license/dell/ansible-powerstore)](https://github.com/dell/ansible-powerstore/blob/main/LICENSE)
[![Python version](https://img.shields.io/badge/python-3.9.6+-blue.svg)](https://www.python.org/downloads/)
[![Ansible version](https://img.shields.io/badge/ansible-2.15.6+-blue.svg)](https://pypi.org/project/ansible/)
[![PyPowerStore](https://img.shields.io/github/v/release/dell/python-powerstore?include_prereleases&label=PyPowerStore&style=flat-square)](https://github.com/dell/python-powerstore/releases)
[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/dell/ansible-powerstore?include_prereleases&label=latest&style=flat-square)](https://github.com/dell/ansible-powerstore/releases)
[![codecov](https://codecov.io/gh/dell/ansible-powerstore/branch/main/graph/badge.svg)](https://app.codecov.io/gh/dell/ansible-powerstore)

The Ansible Modules for Dell Technologies (Dell) PowerStore allow Data Center and IT administrators to use RedHat Ansible to automate and orchestrate the configuration and management of Dell PowerStore arrays.

The capabilities of the Ansible modules are managing volumes, volume groups, vCenters, hosts, host groups, snapshots, snapshot rules, replication rules, replication sessions, protection policies, file systems, NAS servers, SMB shares, user and tree quotas, file system snapshots, NFS exports, Clusters, Networks, Local users, Jobs, Roles, Certificates, Remote systems, security configuration, DNS server, Email notification destination, NTP server, Remote support configuration, Remote support contacts, SMTP configuration, LDAP accounts, LDAP domain configuration, storage containers, File DNS, File interface, File NIS, NFS server, SMB Server and service config. It also allows gathering high level info from the array. The options available for each are list, show, create, modify and delete. These tasks can be executed by running simple playbooks written in yaml syntax. The modules are written so that all the operations are idempotent, so making multiple identical requests has the same effect as making a single request.

## Table of contents

* [Code of conduct](https://github.com/dell/ansible-powerstore/blob/main/docs/CODE_OF_CONDUCT.md)
* [Maintainer guide](https://github.com/dell/ansible-powerstore/blob/main/docs/MAINTAINER_GUIDE.md)
* [Committer guide](https://github.com/dell/ansible-powerstore/blob/main/docs/COMMITTER_GUIDE.md)
* [Contributing guide](https://github.com/dell/ansible-powerstore/blob/main/docs/CONTRIBUTING.md)
* [Branching strategy](https://github.com/dell/ansible-powerstore/blob/main/docs/BRANCHING.md)
* [List of adopters](https://github.com/dell/ansible-powerstore/blob/main/docs/ADOPTERS.md)
* [Maintainers](https://github.com/dell/ansible-powerstore/blob/main/docs/MAINTAINERS.md)
* [Support](https://github.com/dell/ansible-powerstore/blob/main/docs/SUPPORT.md)
* [License](#license)
* [Security](https://github.com/dell/ansible-powerstore/blob/main/docs/SECURITY.md)
* [Requirements](#requirements)
* [List of Ansible modules for Dell PowerStore](#list-of-ansible-modules-for-dell-powerstore)
* [Installation and execution of Ansible modules for Dell PowerStore](#installation-and-execution-of-ansible-modules-for-dell-powerstore)
* [Releasing, Maintenance and Deprecation](#releasing-maintenance-and-deprecation)


## Requirements

   | **Ansible Modules** | **PowerStore Version** | **SDK version** | **Python version** | **Ansible**              |
|---------------------|-----------------------|-----------------|--------------------|--------------------------|
| v3.5.0              | 2.9.x <br> 3.2.x <br> 3.5.x <br> 3.6.x <br> 4.0.x | 3.3.0          | 3.9.x <br> 3.10.x <br> 3.11.x <br> 3.12.x | 2.15 <br> 2.16 <br> 2.17 |


  * Please follow PyPowerStore installation instructions on [PyPowerStore Documentation](https://github.com/dell/python-powerstore)


## Installation and execution of Ansible modules for Dell PowerStore
The installation and execution steps of Ansible modules for Dell PowerStore can be found [here](https://github.com/dell/ansible-powerstore/blob/main/docs/INSTALLATION.md)


## Use Cases
Refer the [example playbooks](https://github.com/dell/ansible-powerstore/tree/main/playbooks) on how the collection can be used for [modules](https://github.com/dell/ansible-powerstore/tree/main/playbooks/modules).


## Testing
The following tests are done on ansible-powerstore collection
- Unit tests
- Integration tests.


## Support
Refer [Support](https://github.com/dell/ansible-powerstore/blob/main/docs/SUPPORT.md) documenetation for more information on the support from Dell Technologies.


## Release, Maintenance and Deprecation
Ansible Modules for Dell Technologies PowerStore follows [Semantic Versioning](https://semver.org/).

New version will be release regularly if significant changes (bug fix or new feature) are made in the collection.

Released code versions are located on "release" branches with names of the form "release-x.y.z" where x.y.z corresponds to the version number. More information on branching strategy followed can be found [here](https://github.com/dell/ansible-powerstore/blob/main/docs/BRANCHING.md).

Ansible Modules for Dell Technologies PowerStore deprecation cycle is aligned with that of [Ansible](https://docs.ansible.com/ansible/latest/dev_guide/module_lifecycle.html).

See [change logs](https://github.com/dell/ansible-powerstore/blob/main/CHANGELOG.rst) for more information on what is new in the releases.


## Related Information

## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. It essentially means that the result of a successfully performed request is independent of the number of times it is executed.

## List of Ansible Modules for Dell PowerStore
* [Volume module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/volume.rst)
* [Volume group module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/volumegroup.rst)
* [Host module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/host.rst)
* [Host group module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/hostgroup.rst)
* [Snapshot module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/snapshot.rst)
* [Snapshot rule module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/snapshotrule.rst)
* [Replication rule module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/replicationrule.rst)
* [Replication session module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/replicationsession.rst)
* [Protection policy module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/protectionpolicy.rst)
* [Info module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/info.rst)
* [File system module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/filesystem.rst)
* [NAS server module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/nasserver.rst)
* [SMB share module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/smbshare.rst)
* [Quota module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/quota.rst)
* [File system snapshot module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/filesystem_snapshot.rst)
* [NFS export module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/nfs.rst)
* [Cluster module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/cluster.rst)
* [Network module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/network.rst)
* [Local user module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/local_user.rst)
* [Role module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/role.rst)
* [Job module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/job.rst)
* [Certificate module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/certificate.rst)
* [Remote system module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/remotesystem.rst)
* [Security config module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/security_config.rst)
* [DNS module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/dns.rst)
* [Email module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/email.rst)
* [NTP module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/ntp.rst)
* [Remote support module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/remote_support.rst)
* [Remote support contact module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/remote_support_contact.rst)
* [SMTP config module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/smtp_config.rst)
* [LDAP Account module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/ldap_account.rst)
* [LDAP Domain module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/ldap_domain.rst)
* [vCenter module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/vcenter.rst)
* [Storage container module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/storage_container.rst)
* [File interface module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/file_interface.rst)
* [File DNS module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/file_dns.rst)
* [File NIS module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/file_nis.rst)
* [SMB server module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/smb_server.rst)
* [NFS server module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/nfs_server.rst)
* [Service config module](https://github.com/dell/ansible-powerstore/blob/main/docs/modules/service_config.rst)


## License
The Ansible collection for PowerStore is released and licensed under the GPL-3.0 license. See [LICENSE](https://github.com/dell/ansible-powerstore/blob/main/LICENSE) for the full terms.