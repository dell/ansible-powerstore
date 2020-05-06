# Ansible Modules for Dell EMC PowerStore

The Ansible Modules for Dell EMC PowerStore allow Data Center and IT administrators to use RedHat Ansible to automate and orchestrate the configuartion and management of Dell EMC PowerStore arrays.

The capabilities of the Ansible modules are managing volumes, volume groups, hosts, host groups, snapshots, snapshot rules and protection policies; and to gather facts from the array. The options available for each are list, show, create, modify and delete. These tasks can be executed by running simple playbooks written in yaml syntax. The modules are written so that all the operations are idempotent, so making multiple identical requests has the same effect as making a single request.

## Supported Platforms
  * Dell EMC PowerStore Arrays version 1.0

## Prerequisites
  * Ansible 2.7 or higher
  * Python >= 2.7.12
  * Red Hat Enterprise Linux 7.5
  * Python Library for PowerStore version 1.1

## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. It essentially means that the result of a successfully performed request is independent of the number of times it is executed.

## List of Ansible Modules for Dell EMC PowerStore
  * Volume module
  * Volume group module
  * Host module
  * Host group module
  * Snapshot module
  * Snapshot rule module
  * Protection policy module
  * Gather facts module

## Installation

  * Clone the latest development repository and install the ansible modules. 
  
  git clone https://github.com/dell/ansible-powerstore

  cd ansible-powerstore/dellemc_ansible
  
### For python 2.7 environment
  * Copy utils/dellemc_ansible_utils.py to  /usr/lib/python2.7/site-packages/ansible/module_utils/ 
  * Copy all module Python files in the 'powerstore/library' folder to  /usr/lib/python2.7/site-packages/ansible/modules/storage/dellemc/
  * Copy dellemc.py from /doc_fragments folder to /usr/lib/python2.7/site-packages/ansible/plugins/doc_fragments/
### For python 3.5 environment
  * Copy utils/dellemc_ansible_utils.py to  /usr/lib/python3.5/site-packages/ansible/module_utils/
  * Copy all module Python files in the 'powerstore/library' folder to  /usr/lib/python3.5/site-packages/ansible/modules/storage/dellemc/
  * Copy dellemc.py from /doc_fragments folder to /usr/lib/python3.5/site-packages/ansible/plugins/doc_fragments/  


## SSL Certificate Validation
  * Export the SSL certificate from the intended storage array in .crt format.
  * Copy the certificate to this "/usr/local/share/ca-certificates" path of the host.
  * Import the SSL certificate to host using the command "sudo update-ca-certificates".
  * Set the "REQUESTS_CA_BUNDLE" environment variable to the path of the SSL certificate using the command "export REQUESTS_CA_BUNDLE=/usr/local/share/ca-certificates/<<Certificate_Name>>"

## Documentation
Check documentation from each module's file in /ansible-powerstore/dellemc_ansible/powerstore/library/

## Examples
Check examples from each module's file in /ansible-powerstore/dellemc_ansible/powerstore/library/

## Results
Each module returns the updated state and details of the entity, For example, if you are using the Volume module, all calls will return the updated details of the volume. Sample result is shown in each module's documentation.

## Support
Ansible for PowerStore Modules are supported by Dell EMC and are provided under the terms of the license attached to the source code.
For any setup, configuration issues, questions or feedback, join the [Dell EMC Automation community](https://www.dell.com/community/Automation/bd-p/Automation).
For any Dell EMC storage issues, please contact Dell support at: https://www.dell.com/support.
For clarity, Dell EMC does not provide support for any source code modifications.
