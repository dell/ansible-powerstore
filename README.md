# Ansible Modules for Dell Technologies PowerStore
The Ansible Modules for Dell Technologies (Dell) PowerStore allow Data Center and IT administrators to use RedHat Ansible to automate and orchestrate the configuration and management of Dell PowerStore arrays.

The capabilities of the Ansible modules are managing volumes, volume groups, hosts, host groups, snapshots, snapshot rules, replication rules, replication sessions, protection policies, file systems, NAS servers, SMB shares, user and tree quotas, file system snapshots, NFS exports, Clusters, Networks, Local users, Jobs, Roles, Certificates, Remote systems, security configuration, DNS server, Email notification destination, NTP server, Remote support configuration, Remote support contacts, SMTP configuration, LDAP accounts and LDAP domain configuration. It also allows gathering high level info from the array. The options available for each are list, show, create, modify and delete. These tasks can be executed by running simple playbooks written in yaml syntax. The modules are written so that all the operations are idempotent, so making multiple identical requests has the same effect as making a single request.
## License
Ansible collection for PowerStore is released and licensed under the GPL-3.0 license. See [LICENSE](https://github.com/dell/ansible-powerstore/blob/1.6.0/LICENSE) for the full terms. Ansible modules and modules utilities that are part of the Ansible collection for PowerStore are released and licensed under the Apache 2.0 license. See [MODULE-LICENSE](https://github.com/dell/ansible-powerstore/blob/1.6.0/MODULE-LICENSE) for the full terms.

## Support
Ansible collections for PowerStore are supported by Dell and is provided under the terms of the license attached to the collection. Please see the [LICENSE](#license) for the full terms.
Dell does not provide any support for the source code modifications.
For any Ansible modules issues, questions or feedback, join the [Dell Automation Community](https://www.dell.com/community/Automation/bd-p/Automation).

## Prerequisites

   | **Ansible Modules** | **PowerStore Version** | **Red Hat Enterprise Linux**| **SDK version** | **Python version** | **Ansible**              |
|---------------------|-----------------------|------------------------------|-----------------|--------------------|--------------------------|
| v1.6.0              | 1.x <br> 2.0 <br> 2.1 |7.9 <br> 8.4 <br> 8.5| 1.7.0           | 3.8.x <br> 3.9.x <br> 3.10.x | 2.11 <br> 2.12 <br> 2.13 |


  * Please follow PyPowerStore installation instructions on [PyPowerStore Documentation](https://github.com/dell/python-powerstore)

## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. It essentially means that the result of a successfully performed request is independent of the number of times it is executed.

## List of Ansible Modules for Dell PowerStore
* [Volume module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#volume-module)
* [Volume group module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#volume-group-module)
* [Host module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#host-module)
* [Host group module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#host-group-module)
* [Snapshot module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#snapshot-module)
* [Snapshot rule module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#snapshot-rule-module)
* [Replication rule module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#replication-rule-module)
* [Replication session module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#replication-session-module)
* [Protection policy module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#protection-policy-module)
* [Info module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#info-module)
* [File system module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#file-system-module)
* [NAS server module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#nas-server-module)
* [SMB share module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#smb-share-module)
* [Quota module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#quota-module)
* [File system snapshot module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#filesystem-snapshot-module)
* [NFS export module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#nfs-export-module)
* [Cluster module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#cluster-module)
* [Network module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#network-module)
* [Local user module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#local-user-module)
* [Role module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#role-module)
* [Job module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#job-module)
* [Certificate module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#certificate-module)
* [Remote system module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#remote-system-module)
* [Security config module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#security-config-module)
* [DNS module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#dns-module)
* [Email module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#email-module)
* [NTP module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#ntp-module)
* [Remote support module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#remote-support-module)
* [Remote support contact module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#remote-support-contact-module)
* [SMTP config module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#smtp-config-module)
* [LDAP Account module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#ldap-account-module)
* [LDAP Domain module](https://github.com/dell/ansible-powerstore/blob/1.6.0/docs/Product%20Guide.md#ldap-domain-module)
## Installation of SDK
* Install the python SDK named [PyPowerStore](https://pypi.org/project/PyPowerStore/). It can be installed using pip, based on appropriate python version. Execute this command:

        pip install PyPowerStore
* Alternatively, Clone the repo "https://github.com/dell/python-powerstore"
   using command:
   
        git clone https://github.com/dell/python-powerstore.git
    * Go to the root directory of setup.
    * Execute this command:
      
            pip install .

## Building Collections
  * Use this command to build the collection from source code:

        ansible-galaxy collection build

  For more details on how to build a tar ball, please refer: [Building the collection](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections_distributing.html#building-your-collection-tarball)

## Installing Collections
#### Online Installation of Collections 
  1. Use this command to install the latest collection hosted in galaxy:

	     ansible-galaxy collection install dellemc.powerstore -p <install_path>

#### Offline Installation of Collections
  1. Download the latest tar build from any of the available distribution channel [Ansible Galaxy](https://galaxy.ansible.com/dellemc/powerstore) /[Automation Hub](https://console.redhat.com/ansible/automation-hub/repo/published/dellemc/powerstore) and use this command to install the collection anywhere in your system:


	     ansible-galaxy collection install dellemc-powerstore-1.6.0.tar.gz -p <install_path>


  2. Set the environment variable:

	     export ANSIBLE_COLLECTIONS_PATHS=$ANSIBLE_COLLECTIONS_PATHS:<install_path>

## Using Collections
  1. In order to use any Ansible module, ensure that the importing of a proper FQCN (Fully Qualified Collection Name) must be embedded in the playbook. Refer to this example:

	     collections:
	     - dellemc.powerstore

  2. In order to use an installed collection specific to the task use a proper FQCN (Fully Qualified Collection Name). Refer to this example:

	     tasks:
         - name: Get Volume details
	       dellemc.powerstore.volume

  3. For generating Ansible documentation for a specific module, embed the FQCN  before the module name. Refer to this example:

	     ansible-doc dellemc.powerstore.info

## Running Ansible Modules
The Ansible server must be configured with Python library for PowerStore to run the Ansible playbooks. The [Documents](https://github.com/dell/ansible-powerstore/tree/1.6.0/docs) provide information on different Ansible modules along with their functions and syntax. The parameters table in the Product Guide provides information on various parameters which needs to be configured before running the modules.

## SSL Certificate Validation
 1. Copy the CA certificate to this "/etc/pki/ca-trust/source/anchors" path of the host by any external means.
 2. Set the "REQUESTS_CA_BUNDLE" environment variable to the path of the SSL certificate using this command:
	
		export REQUESTS_CA_BUNDLE=/etc/pki/ca-trust/source/anchors/<<Certificate_Name>>
	
 3. Import the SSL certificate to host using this command:

		update-ca-trust

## Results
Each module returns the updated state and details of the entity. 
For example, if you are using the cluster module, all calls will return the updated details of the cluster.
Sample result is shown in each module's documentation.


## Ansible Execution Environment
Ansible can also be installed in a container environment. Ansible Builder provides the ability to create reproducible, self-contained environments as container images that can be run as Ansible execution environments.
* Install the ansible builder package using:

       pip3 install ansible-builder
* Create the execution environment using:

       ansible-builder build --tag <tag_name> --container-runtime docker
* After the image is built, run the container using:

       docker run -it <tag_name> /bin/bash
* Verify collection installation using command:

       ansible-galaxy collection list
* The playbook can be run on the container using:

      docker run --rm -v $(pwd):/runner <tag_name> ansible-playbook info_test.yml


## Maintenance
Ansible Modules for Dell Technologies PowerStore deprecation cycle is aligned with [Ansible](https://docs.ansible.com/ansible/latest/dev_guide/module_lifecycle.html).
