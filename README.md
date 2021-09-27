# Ansible Modules for Dell EMC PowerStore
The Ansible Modules for Dell EMC PowerStore allow Data Center and IT administrators to use RedHat Ansible to automate and orchestrate the configuration and management of Dell EMC PowerStore arrays.

The capabilities of the Ansible modules are managing volumes, volume groups, hosts, host groups, snapshots, snapshot rules, replication rules, replication sessions, protection policies, file systems, NAS servers, SMB shares, user and tree quotas, file system snapshots, NFS exports, Cluster, Networks, Local users, Job, and Roles. It also allows the capability to gather facts from the array. The options available for each are list, show, create, modify and delete. These tasks can be executed by running simple playbooks written in yaml syntax. The modules are written so that all the operations are idempotent, so making multiple identical requests has the same effect as making a single request.
## License
Ansible collection for PowerStore is released and licensed under the GPL-3.0 license. See [LICENSE](LICENSE) for the full terms. Ansible modules and modules utilities that are part of the Ansible collection for PowerStore are released and licensed under the Apache 2.0 license. See [MODULE-LICENSE](MODULE-LICENSE) for the full terms.

## Support
Ansible collections for PowerStore are supported by Dell EMC and are provided under the terms of the license attached to the collection. Please see the [LICENSE](#license) for the full terms.
Dell EMC does not provide any support for the source code modifications.
For any Ansible modules issues, questions or feedback, join the [Dell EMC Automation Community](https://www.dell.com/community/Automation/bd-p/Automation).

## Prerequisites
   | **Ansible Modules** | **PowerStore Version** | **Red Hat Enterprise Linux**| **SDK version**| **Python version** | **Ansible** |
|---------------------|-----------------------|------------------------------|--------------------|--------------------|-------------|
| v1.3.0 | 1.x <br> 2.0 |7.8, <br>8.2 | 1.4.0 | 3.6.x <br> 3.7.x <br> 3.8.x | 2.9 <br> 2.10 <br> 2.11 | 
  * Please follow PyPowerStore installation instructions on [PyPowerStore Documentation](https://github.com/dell/python-powerstore)

## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. It essentially means that the result of a successfully performed request is independent of the number of times it is executed.

## List of Ansible Modules for Dell EMC PowerStore
  * Volume module
  * Volume group module
  * Host module
  * Host group module
  * Snapshot module
  * Snapshot rule module
  * Replication rule module
  * Replication session module
  * Protection policy module
  * Gather facts module
  * File system module
  * NAS server module
  * SMB share module
  * Quota module
  * File system snapshot module
  * NFS export module
  * Cluster module
  * Network module
  * Local user module
  * Role module
  * Job module

## Installation of SDK
  1. Clone the repo using the command: 
	 
	git clone https://github.com/dell/python-powerstore/tree/1.4.0

  2. Go to the root directory of setup.
  3. Execute the following command:<br/>
	
	pip install .

## Building Collections
  * Use the following command to build the collection from source code:

        ansible-galaxy collection build

  For more details on how to build a tar ball, please refer: [Building the collection](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections_distributing.html#building-your-collection-tarball)

## Installing Collections
#### Online Installation of Collections 
  1. Use the following command to install the latest collection hosted in galaxy:

	ansible-galaxy collection install dellemc.powerstore -p <install_path>

#### Offline Installation of Collections
  1. Download the latest tar build from any of the available distribution channel [Ansible Galaxy](https://galaxy.ansible.com/dellemc/powerstore) /[Automation Hub](https://console.redhat.com/ansible/automation-hub/repo/published/dellemc/powerstore) and use the following command to install the collection anywhere in your system:

	ansible-galaxy collection install dellemc-powerstore-1.3.0.tar.gz -p <install_path>

  2. Set the environemnt variable:

	export ANSIBLE_COLLECTIONS_PATHS=$ANSIBLE_COLLECTIONS_PATHS:<install_path>

## Using Collections
  1. In order to use any Ansible module, ensure that the importing of a proper FQCN (Fully Qualified Collection Name) must be embedded in the playbook. Refer to the followig example:

	collections:
	- dellemc.powerstore

  2. In order to use an installed collection specific to the task use a proper FQCN (Fully Qualified Collection Name). Refer to the followig example:

	tasks:
    - name: Get Volume details
	  dellemc.powerstore.dellemc_powerstore_volume

  3. For generating Ansible documentaion for a specific module, embed the FQCN  before the module name. Refer to the following example:

	ansible-doc dellemc.powerstore.dellemc_powerstore_gatherfacts

## Running Ansible Modules
The Ansible server must be configured with Python library for PowerStore to run the Ansible playbooks. The [Documents]( https://github.com/dell/ansible-powerstore/tree/1.3.0/docs ) provide information on different Ansible modules along with their functions and syntax. The parameters table in the Product Guide provides information on various parameters which needs to be configured before running the modules.

## SSL Certificate Validation
 1. Copy the CA certificate to this "/etc/pki/ca-trust/source/anchors" path of the host by any external means.
 2. Set the "REQUESTS_CA_BUNDLE" environment variable to the path of the SSL certificate using the following command:
	
		export REQUESTS_CA_BUNDLE=/etc/pki/ca-trust/source/anchors/<<Certificate_Name>>
	
 3. Import the SSL certificate to host using the following command:

		update-ca-trust

## Results
Each module returns the updated state and details of the entity. 
For example, if you are using the group module, all calls will return the updated details of the group.
Sample result is shown in each module's documentation.
