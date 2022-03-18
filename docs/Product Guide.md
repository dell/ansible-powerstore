# Ansible Modules for Dell Technologies PowerStore
## Product Guide 1.5.0
© 2022 Dell Inc. or its subsidiaries. All rights reserved. Dell, and other trademarks are trademarks of Dell Inc. or its subsidiaries. Other trademarks may be trademarks of their respective owners.

--------------
## Contents
*   [Cluster Module](#cluster-module)
    *   [Synopsis](#synopsis)
    *   [Parameters](#parameters)
    *   [Notes](#notes)
    *   [Examples](#examples)
    *   [Return Values](#return-values)
    *   [Authors](#authors)
*   [NTP Module](#ntp-module)
    *   [Synopsis](#synopsis-1)
    *   [Parameters](#parameters-1)
    *   [Notes](#notes-1)
    *   [Examples](#examples-1)
    *   [Return Values](#return-values-1)
    *   [Authors](#authors-1)
*   [Volume Module](#volume-module)
    *   [Synopsis](#synopsis-2)
    *   [Parameters](#parameters-2)
    *   [Notes](#notes-2)
    *   [Examples](#examples-2)
    *   [Return Values](#return-values-2)
    *   [Authors](#authors-2)
*   [Local User Module](#local-user-module)
    *   [Synopsis](#synopsis-3)
    *   [Parameters](#parameters-3)
    *   [Notes](#notes-3)
    *   [Examples](#examples-3)
    *   [Return Values](#return-values-3)
    *   [Authors](#authors-3)
*   [Quota Module](#quota-module)
    *   [Synopsis](#synopsis-4)
    *   [Parameters](#parameters-4)
    *   [Notes](#notes-4)
    *   [Examples](#examples-4)
    *   [Return Values](#return-values-4)
    *   [Authors](#authors-4)
*   [SMTP Config Module](#smtp-config-module)
    *   [Synopsis](#synopsis-5)
    *   [Parameters](#parameters-5)
    *   [Notes](#notes-5)
    *   [Examples](#examples-5)
    *   [Return Values](#return-values-5)
    *   [Authors](#authors-5)
*   [SMB Share Module](#smb-share-module)
    *   [Synopsis](#synopsis-6)
    *   [Parameters](#parameters-6)
    *   [Notes](#notes-6)
    *   [Examples](#examples-6)
    *   [Return Values](#return-values-6)
    *   [Authors](#authors-6)
*   [DNS Module](#dns-module)
    *   [Synopsis](#synopsis-7)
    *   [Parameters](#parameters-7)
    *   [Notes](#notes-7)
    *   [Examples](#examples-7)
    *   [Return Values](#return-values-7)
    *   [Authors](#authors-7)
*   [Role Module](#role-module)
    *   [Synopsis](#synopsis-8)
    *   [Parameters](#parameters-8)
    *   [Notes](#notes-8)
    *   [Examples](#examples-8)
    *   [Return Values](#return-values-8)
    *   [Authors](#authors-8)
*   [Replication Rule Module](#replication-rule-module)
    *   [Synopsis](#synopsis-9)
    *   [Parameters](#parameters-9)
    *   [Notes](#notes-9)
    *   [Examples](#examples-9)
    *   [Return Values](#return-values-9)
    *   [Authors](#authors-9)
*   [Host Group Module](#host-group-module)
    *   [Synopsis](#synopsis-10)
    *   [Parameters](#parameters-10)
    *   [Notes](#notes-10)
    *   [Examples](#examples-10)
    *   [Return Values](#return-values-10)
    *   [Authors](#authors-10)
*   [Network Module](#network-module)
    *   [Synopsis](#synopsis-11)
    *   [Parameters](#parameters-11)
    *   [Notes](#notes-11)
    *   [Examples](#examples-11)
    *   [Return Values](#return-values-11)
    *   [Authors](#authors-11)
*   [NFS Module](#nfs-module)
    *   [Synopsis](#synopsis-12)
    *   [Parameters](#parameters-12)
    *   [Notes](#notes-12)
    *   [Examples](#examples-12)
    *   [Return Values](#return-values-12)
    *   [Authors](#authors-12)
*   [Snapshot Rule Module](#snapshot-rule-module)
    *   [Synopsis](#synopsis-13)
    *   [Parameters](#parameters-13)
    *   [Notes](#notes-13)
    *   [Examples](#examples-13)
    *   [Return Values](#return-values-13)
    *   [Authors](#authors-13)
*   [Volume Group Module](#volume-group-module)
    *   [Synopsis](#synopsis-14)
    *   [Parameters](#parameters-14)
    *   [Notes](#notes-14)
    *   [Examples](#examples-14)
    *   [Return Values](#return-values-14)
    *   [Authors](#authors-14)
*   [Remote Support Contact Module](#remote-support-contact-module)
    *   [Synopsis](#synopsis-15)
    *   [Parameters](#parameters-15)
    *   [Notes](#notes-15)
    *   [Examples](#examples-15)
    *   [Return Values](#return-values-15)
    *   [Authors](#authors-15)
*   [NAS Server Module](#nas-server-module)
    *   [Synopsis](#synopsis-16)
    *   [Parameters](#parameters-16)
    *   [Notes](#notes-16)
    *   [Examples](#examples-16)
    *   [Return Values](#return-values-16)
    *   [Authors](#authors-16)
*   [Filesystem Snapshot Module](#filesystem-snapshot-module)
    *   [Synopsis](#synopsis-17)
    *   [Parameters](#parameters-17)
    *   [Notes](#notes-17)
    *   [Examples](#examples-17)
    *   [Return Values](#return-values-17)
    *   [Authors](#authors-17)
*   [Security Config Module](#security-config-module)
    *   [Synopsis](#synopsis-18)
    *   [Parameters](#parameters-18)
    *   [Notes](#notes-18)
    *   [Examples](#examples-18)
    *   [Return Values](#return-values-18)
    *   [Authors](#authors-18)
*   [Host Module](#host-module)
    *   [Synopsis](#synopsis-19)
    *   [Parameters](#parameters-19)
    *   [Notes](#notes-19)
    *   [Examples](#examples-19)
    *   [Return Values](#return-values-19)
    *   [Authors](#authors-19)
*   [Job Module](#job-module)
    *   [Synopsis](#synopsis-20)
    *   [Parameters](#parameters-20)
    *   [Notes](#notes-20)
    *   [Examples](#examples-20)
    *   [Return Values](#return-values-20)
    *   [Authors](#authors-20)
*   [Remote Support Module](#remote-support-module)
    *   [Synopsis](#synopsis-21)
    *   [Parameters](#parameters-21)
    *   [Notes](#notes-21)
    *   [Examples](#examples-21)
    *   [Return Values](#return-values-21)
    *   [Authors](#authors-21)
*   [Replication Session Module](#replication-session-module)
    *   [Synopsis](#synopsis-22)
    *   [Parameters](#parameters-22)
    *   [Notes](#notes-22)
    *   [Examples](#examples-22)
    *   [Return Values](#return-values-22)
    *   [Authors](#authors-22)
*   [Remote System Module](#remote-system-module)
    *   [Synopsis](#synopsis-23)
    *   [Parameters](#parameters-23)
    *   [Notes](#notes-23)
    *   [Examples](#examples-23)
    *   [Return Values](#return-values-23)
    *   [Authors](#authors-23)
*   [File System Module](#file-system-module)
    *   [Synopsis](#synopsis-24)
    *   [Parameters](#parameters-24)
    *   [Notes](#notes-24)
    *   [Examples](#examples-24)
    *   [Return Values](#return-values-24)
    *   [Authors](#authors-24)
*   [Certificate Module](#certificate-module)
    *   [Synopsis](#synopsis-25)
    *   [Parameters](#parameters-25)
    *   [Notes](#notes-25)
    *   [Examples](#examples-25)
    *   [Return Values](#return-values-25)
    *   [Authors](#authors-25)
*   [Email Module](#email-module)
    *   [Synopsis](#synopsis-26)
    *   [Parameters](#parameters-26)
    *   [Notes](#notes-26)
    *   [Examples](#examples-26)
    *   [Return Values](#return-values-26)
    *   [Authors](#authors-26)
*   [Protection Policy Module](#protection-policy-module)
    *   [Synopsis](#synopsis-27)
    *   [Parameters](#parameters-27)
    *   [Notes](#notes-27)
    *   [Examples](#examples-27)
    *   [Return Values](#return-values-27)
    *   [Authors](#authors-27)
*   [Snapshot Module](#snapshot-module)
    *   [Synopsis](#synopsis-28)
    *   [Parameters](#parameters-28)
    *   [Notes](#notes-28)
    *   [Examples](#examples-28)
    *   [Return Values](#return-values-28)
    *   [Authors](#authors-28)
*   [Info Module](#info-module)
    *   [Synopsis](#synopsis-29)
    *   [Parameters](#parameters-29)
    *   [Notes](#notes-29)
    *   [Examples](#examples-29)
    *   [Return Values](#return-values-29)
    *   [Authors](#authors-29)

--------------

# Cluster Module

Manage cluster related opeartions on PowerStore

### Synopsis
 Managing cluster on PowerStore storage system includes getting details and modifying cluster configuration parameters.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > chap_mode</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>Disabled</li>  <li>Single</li>  <li>Mutual</li> </ul></td>
            <td> <br> The mode that describes or sets the iSCSI CHAP mode for the cluster. </td>
        </tr>
                    <tr>
            <td colspan=1 > is_ssh_enabled</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Whether SSH access is enabled for the cluster.  <br> Either appliance_id or appliance_name is to be passed along with is_ssh_enabled. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > appliance_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> ID of the appliance.  <br> Parameters appliance_id and appliance_name are mutually exclusive.  <br> Parameter is_ssh_enabled has to be passed along with appliance_id. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The new name for the cluster. </td>
        </tr>
                    <tr>
            <td colspan=1 > cluster_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The Name of cluster. </td>
        </tr>
                    <tr>
            <td colspan=1 > appliance_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the appliance.  <br> Parameters appliance_id and appliance_name are mutually exclusive.  <br> Parameter is_ssh_enabled has to be passed along with appliance_name. </td>
        </tr>
                    <tr>
            <td colspan=1 > service_password</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The password for the service user. </td>
        </tr>
                    <tr>
            <td colspan=1 > cluster_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Id of the cluster. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the cluster should exist or not.  <br> Value present indicates that the cluster should exist on the system.  <br> Value absent indicates that the cluster should not exist on the system. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > physical_mtu</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> MTU for ethernet ports in the cluster.  <br> The MTU can be set between 1500 to 9000. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                            </table>

### Notes
* Creation and deletion of cluster is not supported by ansible modules.
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
- name: Get the details of cluster using id
  dellemc.powerstore.cluster:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    cluster_id: "0"
    state: "present"

- name: Modify details of cluster using the name
  dellemc.powerstore.cluster:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    cluster_name: "RT-D1320"
    appliance_id: "A1"
    is_ssh_enabled: True
    service_password: "S@mple_password"
    chap_mode: "Disabled"
    new_name: "new_RT-D1320"
    state: "present"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=5>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=5 > cluster_details </td>
            <td>  complex </td>
            <td> When Cluster exists. </td>
            <td> The cluster details. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > appliance_count </td>
                <td> int </td>
                <td>success</td>
                <td> Number of appliances configured in this cluster. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > service_user_details </td>
                <td> complex </td>
                <td>success</td>
                <td> Details of the service user for which the password can be updated. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Id of the service user. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > is_built_in </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Whether the service user is built in or not. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > is_default_password </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Whether the service user has default password or not. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Name of the service user. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > global_id </td>
                <td> str </td>
                <td>success</td>
                <td> The global unique identifier of the cluster. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > primary_appliance_id </td>
                <td> str </td>
                <td>success</td>
                <td> The unique identifier of the appliance acting as primary. This parameter was added in version 2.0.0.0. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > service_config_details </td>
                <td> complex </td>
                <td>success</td>
                <td> Details of the service config for the entered appliance. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Id of the service configuration. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > appliance_id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Id of the appliance for which the service configuration exists. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > is_ssh_enabled </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Whether the ssh is enabled for the appliance or not. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the cluster. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > storage_discovery_address </td>
                <td> str </td>
                <td>success</td>
                <td> The floating storage discovery IP address for the cluster in IPv4 or IPv6 format. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > master_appliance_id </td>
                <td> str </td>
                <td>success</td>
                <td> The unique identifier of the appliance acting as primary. This parameter is deprecated in version 2.0.0.0. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > appliance_details </td>
                <td> complex </td>
                <td>success</td>
                <td> Name and Id of the appliance for which is_ssh_enabled parameter is used. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Id of the appliance. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Name of the appliance. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > is_encryption_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether or not Data at Rest Encryption is enabled on the cluster. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > system_time </td>
                <td> str </td>
                <td>success</td>
                <td> Current clock time for the system. System time and all the system reported times are in UTC (GMT+0:00) format. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > management_address </td>
                <td> str </td>
                <td>success</td>
                <td> The floating management IP address for the cluster in IPv4 or IPv6 format. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > compatibility_level </td>
                <td> int </td>
                <td>success</td>
                <td> The behavioral version of the software version API, It is used to ensure the compatibility across potentially different software versions. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > state </td>
                <td> str </td>
                <td>success</td>
                <td> Possible cluster states. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the cluster. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > physical_mtu </td>
                <td> int </td>
                <td>success</td>
                <td> MTU for the cluster. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > is_ssh_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether or not the ssh is enabled. </td>
            </tr>
                                        <tr>
            <td colspan=5 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

--------------------------------
# NTP Module

NTP operations on a PowerStore storage system

### Synopsis
 Performs all NTP operations on a PowerStore Storage System. This module supports get details of an existing NTP instance. You can modify existing NTP instance with supported parameters.

### Parameters
                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > ntp_id</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> Unique identifier of the NTP instance. </td>
        </tr>
                    <tr>
            <td colspan=1 > ntp_addresses</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> NTP server addresses, may contain host names or IPv4 addresses. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > ntp_address_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-ntp</li>  <li>absent-in-ntp</li> </ul></td>
            <td> <br> State of the addresses mentioned in ntp_addresses. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> The state of the NTP instance after the task is performed.  <br> For get and modify operations it should be set to "present". </td>
        </tr>
                            </table>

### Notes
* Minimum 1 and maximum 3 addresses can be associated to a NTP instance.
* Parameters ntp_addresses and ntp_address_state are required together.
* Creation and deletion of NTP is not supported.
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
  - name: Get details of NTP instance
    dellemc.powerstore.ntp:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       ntp_id: "NTP1"
       state: "present"

  - name: Add addresses to NTP instance
    dellemc.powerstore.ntp:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       ntp_id: "NTP1"
       ntp_addresses:
        - "XX.XX.XX.XX"
        - "YY.YY.YY.YY"
       ntp_address_state: "present-in-ntp"
       state: "present"

  - name: Remove addresses from NTP instance
    dellemc.powerstore.ntp:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       ntp_id: "NTP1"
       ntp_addresses:
        - "YY.YY.YY.YY"
       ntp_address_state: "absent-in-ntp"
       state: "present"
```

### Return Values
                                                                                                                                                                                
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > ntp_details </td>
            <td>  complex </td>
            <td> When NTP exists. </td>
            <td> Details of the NTP instance. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > addresses </td>
                <td> str </td>
                <td>success</td>
                <td> NTP server addresses, may contain host names or IPv4 addresses. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of NTP instance. </td>
            </tr>
                                        <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Shows whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Bhavneet Sharma (@sharmb5) <ansible.team@dell.com>

--------------------------------
# Volume Module

Manage volumes on a PowerStore storage system

### Synopsis
 Managing volume on PowerStore storage system includes create volume, get details of volume, modify volume attributes, map or unmap volume to host/host group, and delete volume.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > performance_policy</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>high</li>  <li>medium</li>  <li>low</li> </ul></td>
            <td> <br> The performance_policy for the volume.  <br> A volume can be assigned a performance policy at the time of creation of the volume, or later as well.  <br> The policy can also be changed for a given volume, by simply passing the new value.  <br> Check examples for more clarity.  <br> If not given, performance policy will be 'medium'. </td>
        </tr>
                    <tr>
            <td colspan=1 > vg_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the volume group. A volume can optionally be assigned to a volume group at the time of creation.  <br> Use the Volume Group Module for modification of the assignment. </td>
        </tr>
                    <tr>
            <td colspan=1 > mapping_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>mapped</li>  <li>unmapped</li> </ul></td>
            <td> <br> Define whether the volume should be mapped to a host or hostgroup.  <br> Value mapped - indicates that the volume should be mapped to the host or host group.  <br> Value unmapped - indicates that the volume should not be mapped to the host or host group.  <br> Only one of a host or host group can be supplied in one call. </td>
        </tr>
                    <tr>
            <td colspan=1 > cap_unit</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>MB</li>  <li>GB</li>  <li>TB</li> </ul></td>
            <td> <br> Volume size unit.  <br> Used to signify unit of the size provided for creation and expansion of volume.  <br> It defaults to 'GB', if not specified. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > vol_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The 36 character long ID of the volume, automatically generated when a volume is created.  <br> Cannot be used while creating a volume. All other functionalities on a volume are supported using volume name or ID. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > size</td>
            <td> float  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Size of the volume. Minimum volume size is 1MB. Maximum volume size is 256TB. Size must be a multiple of 8192.  <br> Required in case of create and expand volume. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > hlu</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Logical unit number for the host/host group volume access.  <br> Optional parameter when mapping a volume to host/host group.  <br> HLU modification is not supported. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The new volume name for the volume, used in case of rename functionality. </td>
        </tr>
                    <tr>
            <td colspan=1 > host</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Host to be mapped/unmapped to a volume. If not specified, an unmapped volume is created. Only one of the host or host group can be supplied in one call.  <br> To represent host, both name or ID can be used interchangeably. The module will detect both. </td>
        </tr>
                    <tr>
            <td colspan=1 > hostgroup</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Hostgroup to be mapped/unmapped to a volume. If not specified, an unmapped volume is created.  <br> Only one of the host or host group can be mapped in one call.  <br> To represent a hostgroup, both name or ID can be used interchangeably. The module will detect both. </td>
        </tr>
                    <tr>
            <td colspan=1 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Description for the volume.  <br> Optional parameter when creating a volume.  <br> To modify, pass the new value in description field. </td>
        </tr>
                    <tr>
            <td colspan=1 > vol_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Unique name of the volume. This value must contain 128 or fewer printable unicode characters.  <br> Required when creating a volume. All other functionalities on a volume are supported using volume name or ID. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the volume should exist or not.  <br> Value present - indicates that the volume should exist on the system.  <br> Value absent - indicates that the volume should not exist on the system. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > protection_policy</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The protection_policy of the volume.  <br> To represent policy, both name or ID can be used interchangably. The module will detect both.  <br> A volume can be assigned a protection policy at the time of creation of volume or later as well.  <br> The policy can also be changed for a given volume by simply passing the new value.  <br> The policy can be removed by passing an empty string.  <br> Check examples for more clarity. </td>
        </tr>
                            </table>

### Notes
* To create a new volume, vol_name and size is required. cap_unit, description, vg_name, performance_policy, and protection_policy are optional.
* Parameter new_name should not be provided when creating a new volume.
* The size is a required parameter for expand volume.
* Clones or Snapshots of a deleted production volume or a clone are not deleted.
* A volume that is attached to a host/host group, or that is part of a volume group cannot be deleted.
* The Check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
- name: Create stand-alone volume
  dellemc.powerstore.volume:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vol_name: "{{vol_name}}"
    size: 1
    cap_unit: "{{cap_unit}}"
    state: 'present'

- name: Create stand-alone volume with performance and protection policy
  dellemc.powerstore.volume:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vol_name: "{{vol_name}}"
    size: 5
    cap_unit: "{{cap_unit}}"
    state: 'present'
    description: 'Description'
    performance_policy: 'low'
    protection_policy: 'protection_policy_name'

- name: Create volume and assign to a volume group
  dellemc.powerstore.volume:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vol_name: "{{vol_name}}"
    vg_name: "{{vg_name}}"
    size: 1
    cap_unit: "{{cap_unit}}"
    state: 'present'

- name: Create volume and map it to a host
  dellemc.powerstore.volume:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vol_name: "{{vol_name}}"
    size: 1
    cap_unit: "{{cap_unit}}"
    mapping_state: 'mapped'
    host: "{{host_name}}"
    state: 'present'

- name: Get volume details using ID
  dellemc.powerstore.volume:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vol_id: "{{result.volume_details.id}}"
    state: "present"

- name: Get volume details using name
  dellemc.powerstore.volume:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vol_name: "{{vol_name}}"
    state: "present"

- name: Modify volume size, name, description and performance policy
  dellemc.powerstore.volume:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    new_name: "{{new_name}}"
    vol_name: "{{vol_name}}"
    state: "present"
    size: 2
    performance_policy: 'high'
    description: 'new description'

- name: Remove protection policy from Volume
  dellemc.powerstore.volume:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    new_name: "{{new_name}}"
    vol_name: "{{vol_name}}"
    state: "present"
    protection_policy: ""

- name: Map volume to a host with HLU
  dellemc.powerstore.volume:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vol_name: "{{vol_name}}"
    state: 'present'
    mapping_state: 'mapped'
    host: 'host1'
    hlu: 12

- name: Map volume to a host without HLU
  dellemc.powerstore.volume:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vol_name: "{{vol_name}}"
    state: 'present'
    mapping_state: 'mapped'
    host: 'host2'

- name: Delete volume
  dellemc.powerstore.volume:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vol_id: "{{result.volume_details.id}}"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=7>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=7 > volume_details </td>
            <td>  complex </td>
            <td> When volume exists </td>
            <td> Details of the volume. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=6 > performance_policy_id </td>
                <td> str </td>
                <td>success</td>
                <td> The performance policy for the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=6 > nguid </td>
                <td> int </td>
                <td>success</td>
                <td> NVMe Namespace globally unique identifier. Used for volumes attached to NVMEoF hosts. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=6 > host_group </td>
                <td> complex </td>
                <td>success</td>
                <td> Host groups details mapped to the volume. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=5 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The host group ID mapped to the volume. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=5 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Name of the Host group mapped to the volume. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=6 > mapped_volumes </td>
                <td> complex </td>
                <td>success</td>
                <td> This is the inverse of the resource type host_volume_mapping association. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=5 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Unique identifier of a mapping between a host and a volume. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=5 > logical_unit_number </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Logical unit number for the host volume access. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=6 > hlu_details </td>
                <td> complex </td>
                <td>success</td>
                <td> HLU details for mapped host/host group. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=5 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The HLU ID. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=5 > host_group_id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The host group ID mapped to the volume. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=5 > host_id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The host ID mapped to the volume. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=5 > logical_unit_number </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Logical unit number for the host/host group volume access. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=6 > wwn </td>
                <td> str </td>
                <td>success</td>
                <td> The world wide name of the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=6 > size </td>
                <td> int </td>
                <td>success</td>
                <td> Size of the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=6 > protection_policy_id </td>
                <td> str </td>
                <td>success</td>
                <td> The protection policy of the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=6 > nsid </td>
                <td> int </td>
                <td>success</td>
                <td> NVMe Namespace unique identifier in the NVME subsystem. Used for volumes attached to NVMEoF hosts. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=6 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID given to the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=6 > node_affinity </td>
                <td> str </td>
                <td>success</td>
                <td> This attribute shows which node will be advertised as the optimized IO path to the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=6 > description </td>
                <td> str </td>
                <td>success</td>
                <td> description about the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=6 > volume_groups </td>
                <td> complex </td>
                <td>success</td>
                <td> The volume group details of the volume. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=5 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The system generated ID given to the volume group. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=5 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Name of the volume group. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=6 > host </td>
                <td> complex </td>
                <td>success</td>
                <td> Hosts details mapped to the volume. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=5 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The host ID mapped to the volume. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=5 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Name of the Host mapped to the volume. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=6 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the volume. </td>
            </tr>
                                        <tr>
            <td colspan=7 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Ambuj Dubey (@AmbujDube) <ansible.team@dell.com>
* Manisha Agrawal (@agrawm3) <ansible.team@dell.com>

--------------------------------
# Local User Module

Local user operations on PowerStore Storage System

### Synopsis
 Supports the provisioning operations on a Local user such as create, modify, delete and get the details of a local user.

### Parameters
                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > role_id</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The unique identifier of the role to which the local user account will be mapped.  <br> It is mutually exclusive with role_name. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > user_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the local user account. Mutually exclusive with user_id.  <br> Mandatory only for create operation. </td>
        </tr>
                    <tr>
            <td colspan=1 > user_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Unique identifier of the local user account.  <br> Mutually exclusive with user_name. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_password</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New password for the existing local user account. </td>
        </tr>
                    <tr>
            <td colspan=1 > role_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the role to which the local user account will be mapped.  <br> It is mutually exclusive with role_id. </td>
        </tr>
                    <tr>
            <td colspan=1 > user_password</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Password for the new local user account to be created.  <br> Mandatory only for create operation. </td>
        </tr>
                    <tr>
            <td colspan=1 > is_locked</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Whether the user account is locked or not.  <br> Defaults to false at creation time. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the local user should exist or not. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                            </table>

### Notes
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
- name: Create local user
  dellemc.powerstore.local_user:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    user_name: "ansible_user_1"
    user_password: "Password123#"
    role_name: "role_1"
    is_locked: False
    state: "present"

- name: Get the details local user with user id
  dellemc.powerstore.local_user:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    user_id: "{{user_id}}"
    state: "present"

- name: Get the details local user with user name
  dellemc.powerstore.local_user:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    user_name: "ansible_user_1"
    state: "present"

- name: Modify attributes of local user
  dellemc.powerstore.local_user:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    user_name: "ansible_user_1"
    user_password: "Password123#"
    new_password: "Ansible123#"
    role_id: 4
    is_locked: True
    state: "present"

- name: Delete local user
  dellemc.powerstore.local_user:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    user_name: "ansible_user_1"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > local_user_details </td>
            <td>  complex </td>
            <td> When local user exists </td>
            <td> Details of the local user. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > role_id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the role local user account is mapped to. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_default_password </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether the user account has a default password or not. Only applies to default user accounts </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID given to the local user. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the local user. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_built_in </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether the user account is built-in or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > role_name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the role to which local user account is mapped. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_locked </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether the user account is locked or not. Defaults to false at creation time. </td>
            </tr>
                                        <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Arindam Datta (@dattaarindam) <ansible.team@dell.com>

--------------------------------
# Quota Module

Manage Tree Quotas and User Quotas on PowerStore

### Synopsis
 Managing  Quotas on PowerStore storage system includes getting details, modifying, creating and deleting Quotas.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=2>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=2 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=2 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=2 > uid</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the unix user account for which quota operations will be performed.  <br> Any one among uid/unix_name/windows_name/windows_sid is required when quota_type is 'user'. </td>
        </tr>
                    <tr>
            <td colspan=2 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=2 > quota</td>
            <td> dict  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Specifies Quota parameters. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > cap_unit </td>
                <td> str  </td>
                <td></td>
                <td> GB </td>
                <td> <ul> <li>GB</li>  <li>TB</li> </ul></td>
                <td>  <br> Unit of storage for the hard and soft limits.  <br> This parameter is required if limit is specified.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > hard_limit </td>
                <td> int  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Hard limit of the user quota.  <br> No hard limit when set to 0.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > soft_limit </td>
                <td> int  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Soft limit of the User/Tree quota.  <br> No Soft limit when set to 0.  </td>
            </tr>
                            <tr>
            <td colspan=2 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=2 > filesystem</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID/Name of the filesystem for which the Tree/User Quota  will be created.  <br> If filesystem name is specified, then nas_server is required to uniquely identify the filesystem. </td>
        </tr>
                    <tr>
            <td colspan=2 > quota_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Id of the user/tree quota.  <br> If quota_id is mentioned, then path/nas_server/file_system/quota_type is not required. </td>
        </tr>
                    <tr>
            <td colspan=2 > windows_sid</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The SID of the Windows User account for which quota operations will be performed.  <br> Any one among uid/unix_name/windows_name/windows_sid is required when quota_type is 'user'. </td>
        </tr>
                    <tr>
            <td colspan=2 > windows_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the Windows User for which quota operations will be performed.  <br> The name should be mentioned along with Domain Name as 'DOMAIN_NAME\user_name' or as "DOMAIN_NAME\\user_name".  <br> Any one among uid/unix_name/windows_name/windows_sid is required when quota_type is 'user'. </td>
        </tr>
                    <tr>
            <td colspan=2 > quota_type</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>user</li>  <li>tree</li> </ul></td>
            <td> <br> The type of quota which will be imposed. </td>
        </tr>
                    <tr>
            <td colspan=2 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Additional information that can be mentioned for a Tree Quota.  <br> Description parameter can only be used when quota_type is 'tree'. </td>
        </tr>
                    <tr>
            <td colspan=2 > nas_server</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The NAS server. This could be the name or ID of the NAS server. </td>
        </tr>
                    <tr>
            <td colspan=2 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the Quota should exist or not.  <br> Value present  indicates that the Quota should exist on the system.  <br> Value absent  indicates that the Quota should not exist on the system. </td>
        </tr>
                    <tr>
            <td colspan=2 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=2 > path</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The path on which the quota will be imposed.  <br> Path is relative to the root of the filesystem.  <br> For user quota, if path is not specified, quota will be created at the root of the filesystem. </td>
        </tr>
                    <tr>
            <td colspan=2 > unix_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the unix user account for which quota operations will be performed.  <br> Any one among uid/unix_name/windows_name/windows_sid is required when quota_type is 'user'. </td>
        </tr>
                            </table>

### Notes
* Tree quota cannot be created at the root of the filesystem.
* When the ID of the filesystem is passed then nas_server is not required. If passed, then filesystem should exist for the nas_server, else the task will fail.
* If a primary directory of the current directory or a subordinate directory of the path is having a Tree Quota configured, then the quota for that path cannot be created.
* Hierarchical tree quotas are not allowed.
* When the first quota is created for a directory/user in a filesystem then the quotas will be enabled for that filesystem automatically.
* If a user quota is to be created on a tree quota, then the user quotas will be enabled automatically in a tree quota.
* Delete User Quota operation is not supported.
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
    - name: Create a Quota for a User using unix name
      dellemc.powerstore.quota:
        array_ip: "{{array_ip}}"
        verifycert: "{{verify_cert}}"
        user: "{{user}}"
        password: "{{password}}"
        quota_type: "user"
        unix_name: "{{unix_name}}"
        filesystem: "sample_fs"
        nas_server: "{{nas_server_id}}"
        quota:
          soft_limit: 5
          hard_limit: 10
          cap_unit: "TB"
        state: "present"

    - name: Create a Tree Quota
      dellemc.powerstore.quota:
        array_ip: "{{array_ip}}"
        verifycert: "{{verify_cert}}"
        user: "{{user}}"
        password: "{{password}}"
        quota_type: "tree"
        path: "/home"
        filesystem: "sample_fs"
        nas_server: "sample_nas_server"
        quota:
          soft_limit: 5
          hard_limit: 10
          cap_unit: "TB"
        state: "present"

    - name: Modify attributes for Tree Quota
      dellemc.powerstore.quota:
        array_ip: "{{array_ip}}"
        verifycert: "{{verify_cert}}"
        user: "{{user}}"
        password: "{{password}}"
        quota_id: "{{quota_id}}"
        quota:
          soft_limit: 10
          hard_limit: 15
          cap_unit: "TB"
        state: "present"

    - name: Get details of User Quota
      dellemc.powerstore.quota:
        array_ip: "{{array_ip}}"
        verifycert: "{{verify_cert}}"
        user: "{{user}}"
        password: "{{password}}"
        quota_type: "user"
        uid: 100
        path: "/home"
        filesystem: "{{filesystem_id}}"
        state: "present"

    - name: Get details of Tree Quota
      dellemc.powerstore.quota:
        array_ip: "{{array_ip}}"
        verifycert: "{{verify_cert}}"
        user: "{{user}}"
        password: "{{password}}"
        quota_id: "{{quota_id}}"
        state: "present"

    - name: Delete a Tree Quota
      dellemc.powerstore.quota:
        array_ip: "{{array_ip}}"
        verifycert: "{{verify_cert}}"
        user: "{{user}}"
        password: "{{password}}"
        quota_type: "tree"
        path: "/home"
        filesystem: "sample_fs"
        nas_server: "sample_nas_server"
        state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=4>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=4 > quota_details </td>
            <td>  complex </td>
            <td> When Quota exists. </td>
            <td> The quota details. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > hard_limit(cap_unit) </td>
                <td> int </td>
                <td>success</td>
                <td> Value of the Hard Limit imposed on the quota. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > tree_quota_id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the Tree Quota on which the specific User Quota exists. Only applicable for user quotas. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > uid </td>
                <td> int </td>
                <td>success</td>
                <td> The ID of the unix host for which user quota exists. Only applicable for user quotas. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > unix_name </td>
                <td> str </td>
                <td>success</td>
                <td> The Name of the unix host for which user quota exists. Only applicable for user quotas. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > state_l10n </td>
                <td> str </td>
                <td>success</td>
                <td> Localized message string corresponding to state. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > size_used </td>
                <td> int </td>
                <td>success</td>
                <td> Size currently consumed by Tree/User on the filesystem. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > tree_quota_for_user_quota </td>
                <td> complex </td>
                <td>success</td>
                <td> Additional Information of Tree Quota limits on which user quota exists. Only applicable for User Quotas. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > description </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Description of Tree Quota for user quota. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > hard_limit(cap_unit) </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Value of the Hard Limit imposed on the quota. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > path </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The path on which the quota will be imposed. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > remaining_grace_period </td>
                <td> int </td>
                <td>success</td>
                <td> The time period remaining after which the grace period will expire. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the Quota. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > file_system </td>
                <td> complex </td>
                <td>success</td>
                <td> Includes ID and Name of filesystem and nas server for which smb share exists. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > filesystem_type </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Type of filesystem. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > nas_server </td>
                    <td> dict </td>
                    <td>success</td>
                    <td> nas_server of filesystem. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Name of filesystem. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> ID of filesystem. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > windows_sid </td>
                <td> str </td>
                <td>success</td>
                <td> The SID of the windows host for which user quota exists. Only applicable for user quotas. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > windows_name </td>
                <td> str </td>
                <td>success</td>
                <td> The Name of the Windows host for which user quota exists. Only applicable for user quotas. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Additional information about the tree quota. Only applicable for Tree Quotas. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > soft_limit(cap_unit) </td>
                <td> int </td>
                <td>success</td>
                <td> Value of the Soft Limit imposed on the quota. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > state </td>
                <td> str </td>
                <td>success</td>
                <td> State of the user quota or tree quota record period. OK means No quota limits are exceeded. Soft_Exceeded means Soft limit is exceeded, and grace period is not expired. Soft_Exceeded_And_Expired means Soft limit is exceeded, and grace period is expired. Hard_Reached means Hard limit is reached. </td>
            </tr>
                                        <tr>
            <td colspan=4 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

--------------------------------
# SMTP Config Module

SMTP configuration operations on a PowerStore storage system

### Synopsis
 Performs all SMTP configuration operations on a PowerStore Storage System.
 This module supports get details of an existing SMTP configuration. You can modify an existing SMTP configuration with supported parameters. You can also send a test mail through configured SMTP server.

### Parameters
                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > smtp_port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port used for sending SMTP messages. </td>
        </tr>
                    <tr>
            <td colspan=1 > smtp_id</td>
            <td> int  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> Unique identifier of the SMTP configuration. </td>
        </tr>
                    <tr>
            <td colspan=1 > source_email</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Source email address used for sending SMTP messages. </td>
        </tr>
                    <tr>
            <td colspan=1 > destination_email</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Destination email address for the test. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > smtp_address</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> IP address of the SMTP server. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> The state of the SMTP configuration after the task is performed.  <br> For Delete operation only, it should be set to "absent".  <br> For all operations it should be set to "present". </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                            </table>

### Notes
* Idempotency is not supported for test operation for smtp_config module.
* Creation and deletion of SMTP configuration is not supported.
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
  - name: Get details of SMTP configuration
    dellemc.powerstore.smtp_config:
      array_ip: "{{array_ip}}"
      user: "{{user}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      smtp_id: "0"
      state: "present"

  - name: Modify SMTP config details
    dellemc.powerstore.smtp_config:
      array_ip: "{{array_ip}}"
      user: "{{user}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      smtp_id: "0"
      smtp_address: "sample.smtp.com"
      source_email: "def@dell.com"
      state: "present"

  - name: Send a test mail through the SMTP server
    dellemc.powerstore.smtp_config:
      array_ip: "{{array_ip}}"
      user: "{{user}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      smtp_id: "0"
      destination_email: "abc@dell.com"
      state: "present"
```

### Return Values
                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > smtp_config_details </td>
            <td>  complex </td>
            <td> When SMTP configuration exists. </td>
            <td> Details of the SMTP configuration. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> int </td>
                <td>success</td>
                <td> Unique identifier of SMTP configuration. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > source_email </td>
                <td> str </td>
                <td>success</td>
                <td> Source email address used for sending SMTP messages. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > port </td>
                <td> int </td>
                <td>success</td>
                <td> Port used for sending SMTP messages. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > address </td>
                <td> str </td>
                <td>success</td>
                <td> IP address of the SMTP server. </td>
            </tr>
                                        <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>

--------------------------------
# SMB Share Module

Manage SMB shares on a PowerStore storage system

### Synopsis
 Managing SMB Shares on PowerStore storage system includes create, get, modify, and delete the SMB shares.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > is_abe_enabled</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Indicates whether Access-based Enumeration (ABE) for SMB share is enabled.  <br> During creation, if not mentioned, then the default is False. </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshot</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID/Name of the Snapshot.  <br> Either filesystem or snapshot is required for creation of the SMB share.  <br> If snapshot name is specified, then nas_server is required to uniquely identify the snapshot.  <br> If snapshot parameter is provided, then filesystem cannot be specified.  <br> SMB share can be created only if access type of snapshot is "protocol". </td>
        </tr>
                    <tr>
            <td colspan=1 > is_continuous_availability_enabled</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Indicates whether continuous availability for SMB 3.0 is enabled.  <br> During creation, if not mentioned, then the default is False. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > is_branch_cache_enabled</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Indicates whether Branch Cache optimization for SMB share is enabled.  <br> During creation, if not mentioned then default is False. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > offline_availability</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>MANUAL</li>  <li>DOCUMENTS</li>  <li>PROGRAMS</li>  <li>NONE</li> </ul></td>
            <td> <br> Defines valid states of Offline Availability.  <br> MANUAL- Only specified files will be available offline.  <br> DOCUMENTS- All files that users open will be available offline.  <br> PROGRAMS- Program will preferably run from the offline cache even when connected to the network. All files that users open will be available offline.  <br> NONE- Prevents clients from storing documents and programs in offline cache. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > share_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> ID of the SMB share.  <br> Should not be specified during creation. ID is auto generated.  <br> For all other operations either share_name or share_id is required.  <br> If share_id is used then no need to pass nas_server/filesystem/snapshot/ path. </td>
        </tr>
                    <tr>
            <td colspan=1 > umask</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The default UNIX umask for new files created on the SMB Share.  <br> During creation, if not mentioned, then the default is "022".  <br> For all other operations, the default is None. </td>
        </tr>
                    <tr>
            <td colspan=1 > filesystem</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID/Name of the File System.  <br> Either filesystem or snapshot is required for creation of the SMB share.  <br> If filesystem name is specified, then nas_server is required to uniquely identify the filesystem.  <br> If filesystem parameter is provided, then snapshot cannot be specified. </td>
        </tr>
                    <tr>
            <td colspan=1 > share_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the SMB share.  <br> Required during creation of the SMB share.  <br> For all other operations either share_name or share_id is required. </td>
        </tr>
                    <tr>
            <td colspan=1 > is_encryption_enabled</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Indicates whether encryption for SMB 3.0 is enabled at the shared folder level.  <br> During creation, if not mentioned then default is False. </td>
        </tr>
                    <tr>
            <td colspan=1 > nas_server</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID/Name of the NAS Server.  <br> It is not required if share_id is used. </td>
        </tr>
                    <tr>
            <td colspan=1 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Description for the SMB share.  <br> Optional parameter when creating a share.  <br> To modify, pass the new value in description field. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > path</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Local path to the file system/Snapshot or any existing sub-folder of the file system/Snapshot that is shared over the network.  <br> Path is relative to the base of the NAS server and must start with the name of the filesystem.  <br> Required for creation of the SMB share. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the SMB share should exist or not.  <br> Value present indicates that the share should exist on the system.  <br> Value absent indicates that the share should not exist on the system. </td>
        </tr>
                            </table>

### Notes
* When the ID of the filesystem/snapshot is passed then nas_server is not required. If passed, then the filesystem/snapshot should exist for the nas_server, else the task will fail.
* Multiple SMB shares can be created for the same local path.
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
- name: Create SMB share for a filesystem
  dellemc.powerstore.smbshare:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    share_name: "sample_smb_share"
    filesystem: "sample_fs"
    nas_server: "{{nas_server_id}}"
    path: "{{path}}"
    description: "Sample SMB share created"
    is_abe_enabled: True
    is_branch_cache_enabled: True
    offline_availability: "DOCUMENTS"
    is_continuous_availability_enabled: True
    is_encryption_enabled: True
    state: "present"

- name: Modify Attributes of SMB share for a filesystem
  dellemc.powerstore.smbshare:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    share_name: "sample_smb_share"
    nas_server: "sample_nas_server"
    description: "Sample SMB share attributes updated"
    is_abe_enabled: False
    is_branch_cache_enabled: False
    offline_availability: "MANUAL"
    is_continuous_availability_enabled: False
    is_encryption_enabled: False
    umask: "022"
    state: "present"

- name: Create SMB share for a snapshot
  dellemc.powerstore.smbshare:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    share_name: "sample_snap_smb_share"
    snapshot: "sample_snapshot"
    nas_server: "{{nas_server_id}}"
    path: "{{path}}"
    description: "Sample SMB share created for snapshot"
    is_abe_enabled: True
    is_branch_cache_enabled: True
    is_continuous_availability_enabled: True
    state: "present"

- name: Modify Attributes of SMB share for a snapshot
  dellemc.powerstore.smbshare:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    share_name: "sample_snap_smb_share"
    nas_server: "sample_nas_server"
    description: "Sample SMB share attributes updated for snapshot"
    is_abe_enabled: False
    is_branch_cache_enabled: False
    offline_availability: "MANUAL"
    is_continuous_availability_enabled: False
    umask: "022"
    state: "present"

- name: Get details of SMB share
  dellemc.powerstore.smbshare:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    share_id: "{{smb_share_id}}"
    state: "present"

- name: Delete SMB share
  dellemc.powerstore.smbshare:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    share_id: "{{smb_share_id}}"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=3 > smb_share_details </td>
            <td>  complex </td>
            <td> When share exists. </td>
            <td> The SMB share details. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Additional information about the share. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > is_continuous_availability_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether the share will be available continuously or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > is_encryption_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether encryption is enabled or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > is_branch_cache_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether branch cache is enabled or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the SMB share. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > is_ABE_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether Access Based enumeration is enforced or not </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the SMB share. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > file_system </td>
                <td> complex </td>
                <td>success</td>
                <td> Includes ID and Name of filesystem and nas server for which smb share exists. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > filesystem_type </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Type of filesystem. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > nas_server </td>
                    <td> dict </td>
                    <td>success</td>
                    <td> nas_server of filesystem. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Name of filesystem. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> ID of filesystem. </td>
                </tr>
                                                                    <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

--------------------------------
# DNS Module

DNS operations on a PowerStore storage system

### Synopsis
 Performs all DNS operations on a PowerStore Storage System. This module supports get details of an existing DNS instance. You can modify existing DNS instance with supported parameters.

### Parameters
                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > dns_addresses</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> DNS server addresses in IPv4 format. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > dns_address_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-dns</li>  <li>absent-in-dns</li> </ul></td>
            <td> <br> State of the addresses mentioned in dns_addresses. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > dns_id</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> Unique identifier of the DNS instance. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> The state of the DNS instance after the task is performed.  <br> For get and modify operations it should be set to "present". </td>
        </tr>
                            </table>

### Notes
* Minimum 1 and maximum 3 addresses can be associated to a DNS instance.
* Parameters dns_addresses and dns_address_state are required together.
* Creation and deletion of DNS is not supported.
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
  - name: Get details of DNS instance
    dellemc.powerstore.dns:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       dns_id: "DNS1"
       state: "present"

  - name: Add addresses to DNS instance
    dellemc.powerstore.dns:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       dns_id: "DNS1"
       dns_addresses:
        - "XX.XX.XX.XX"
        - "YY.YY.YY.YY"
       dns_address_state: "present-in-dns"
       state: "present"

  - name: Remove addresses from DNS instance
    dellemc.powerstore.dns:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       dns_id: "DNS1"
       dns_addresses:
        - "YY.YY.YY.YY"
       dns_address_state: "absent-in-dns"
       state: "present"
```

### Return Values
                                                                                                                                                                                
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > dns_details </td>
            <td>  complex </td>
            <td> When DNS exists. </td>
            <td> Details of the DNS instance. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > addresses </td>
                <td> str </td>
                <td>success</td>
                <td> DNS server addresses in IPv4 format. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of DNS instance. </td>
            </tr>
                                        <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>

--------------------------------
# Role Module

Get details of the roles present on the PowerStore storage system

### Synopsis
 Manage role in PowerStore storage system includes getting the details of a role.

### Parameters
                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > role_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Id of the role. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the role should exist or not.  <br> Value present, indicates that the role should exist on the system.  <br> Value absent, indicates that the role should not exist on the system. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > role_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the role. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                            </table>

### Notes
* Only getting the details of the role is supported by the ansible module.
* Creation, modification and deletion of roles is not supported by the ansible modules.
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
- name: Get the details of role by name
  dellemc.powerstore.role:
    array_ip: "{{array_ip}}"
    verifycert: "{{verify_cert}}"
    user: "{{user}}"
    password: "{{password}}"
    role_name: "Administrator"
    state: "present"

- name: Get the details of role by id
  dellemc.powerstore.role:
    array_ip: "{{array_ip}}"
    verifycert: "{{verify_cert}}"
    user: "{{user}}"
    password: "{{password}}"
    role_id: "1"
    state: "present"
```

### Return Values
                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > role_details </td>
            <td>  complex </td>
            <td> When role exists. </td>
            <td> The role details. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Description of the role. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the role. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_built_in </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates whether the role is built-in. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the role. </td>
            </tr>
                                        <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

--------------------------------
# Replication Rule Module

Replication rule operations on a PowerStore storage system

### Synopsis
 Performs all replication rule operations on a PowerStore Storage System.
 This module supports get details of an existing replication rule, create new replication rule for supported parameters, modify replication rule and delete a specific replication rule.

### Parameters
                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > remote_system_address</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The management IPv4 address of the remote system.  <br> It is required in case the remote system name passed in remote_system parameter is not unique on the PowerStore Array.  <br> If ID of the remote system is passed then no need to pass remote_system_address. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > rpo</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>Five_Minutes</li>  <li>Fifteen_Minutes</li>  <li>Thirty_Minutes</li>  <li>One_Hour</li>  <li>Six_Hours</li>  <li>Twelve_Hours</li>  <li>One_Day</li> </ul></td>
            <td> <br> Recovery point objective (RPO), which is the acceptable amount of data, measured in units of time, that may be lost in case of a failure. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New name of the replication rule.  <br> Used for renaming a replication rule. </td>
        </tr>
                    <tr>
            <td colspan=1 > replication_rule_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> ID of the replication rule.  <br> ID for the rule is autogenerated, cannot be passed during creation of a replication rule.  <br> Parameter replication_rule_name and replication_rule_id are mutually exclusive. </td>
        </tr>
                    <tr>
            <td colspan=1 > replication_rule_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the replication rule.  <br> Required during creation of a replication rule.  <br> Parameter replication_rule_name and replication_rule_id are mutually exclusive. </td>
        </tr>
                    <tr>
            <td colspan=1 > alert_threshold</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Acceptable delay between the expected and actual replication sync intervals. The system generates an alert if the delay between the expected and actual sync exceeds this threshold.  <br> During creation, if not passed, then by default one RPO in minutes will be passed.  <br> The range of integers supported are in between 0 and 1440 (inclusive of both). </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> The state of the replication rule after the task is performed.  <br> For Delete operation only, it should be set to "absent".  <br> For all Create, Modify or Get details operations it should be set to "present". </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > remote_system</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> ID or name of the remote system to which this rule will replicate the associated resources. </td>
        </tr>
                            </table>

### Notes
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
- name: Create new replication rule
  dellemc.powerstore.replicationrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    replication_rule_name: "sample_replication_rule"
    rpo: "Five_Minutes"
    alert_threshold: "15"
    remote_system: "WN-D8877"
    state: "present"

- name: Modify existing replication rule
  dellemc.powerstore.replicationrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    replication_rule_name: "sample_replication_rule"
    new_name: "new_sample_replication_rule"
    rpo: "One_Hour"
    alert_threshold: "60"
    remote_system: "WN-D0517"
    state: "present"

- name: Get details of replication rule
  dellemc.powerstore.replicationrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    replication_rule_id: "{{id}}"
    state: "present"

- name: Delete an existing replication rule
  dellemc.powerstore.replicationrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    replication_rule_name: "new_sample_replication_rule"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > replication_rule_details </td>
            <td>  complex </td>
            <td> When replication rule exists </td>
            <td> Details of the replication rule. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > remote_system_id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the remote system to which this rule will replicate the associated resources. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > remote_system_name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the remote system to which this rule will replicate the associated resources. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID of the replication rule. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > alert_threshold </td>
                <td> int </td>
                <td>success</td>
                <td> Acceptable delay in minutes between the expected and actual replication sync intervals. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the replication rule. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > rpo </td>
                <td> str </td>
                <td>success</td>
                <td> Recovery point objective (RPO), which is the acceptable amount of data, measured in units of time, that may be lost in case of a failure. </td>
            </tr>
                                        <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

--------------------------------
# Host Group Module

Manage host group on PowerStore Storage System

### Synopsis
 Managing host group on PowerStore storage system includes create host group with a set of hosts, add/remove hosts from host group, rename host group, and delete host group.
 Deletion of a host group results in deletion of the containing hosts as well. Remove hosts from the host group first to retain them.

### Parameters
                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > hostgroup_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The host group name. This value must contain 128 or fewer printable Unicode characters.  <br> Creation of an empty host group is not allowed.  <br> Required when creating a host group.  <br> Use either hostgroup_id or hostgroup_name for modify and delete tasks. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > hostgroup_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The 36-character long host group id, automatically generated when a host group is created.  <br> Use either hostgroup_id or hostgroup_name for modify and delete tasks.  <br> The hostgroup_id cannot be used while creating host group, as it is generated by the array after creation of host group. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The new name for host group renaming function. This value must contain 128 or fewer printable Unicode characters. </td>
        </tr>
                    <tr>
            <td colspan=1 > hosts</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> List of hosts to be added or removed from the host group.  <br> Subordinate hosts in a host group can only be of one type, either FC or iSCSI.  <br> Required when creating a host group.  <br> To represent host, both name or ID can be used interchangeably. The module will detect both. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the host group should exist or not.  <br> Value present - indicates that the host group should exist on the system.  <br> Value absent - indicates that the host group should not exist on the system.  <br> Deletion of a host group results in deletion of the containing hosts as well. Remove hosts from the host group first to retain them. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > host_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-group</li>  <li>absent-in-group</li> </ul></td>
            <td> <br> Define whether the hosts should be present or absent in host group.  <br> Value present-in-group - indicates that the hosts should exist on the host group.  <br> Value absent-in-group - indicates that the hosts should not exist on the host group.  <br> Required when creating a host group with hosts or adding/removing hosts from existing host group. </td>
        </tr>
                            </table>

### Notes
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
  - name: Create host group with hosts using host name
    dellemc.powerstore.hostgroup:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      hostgroup_name: "{{hostgroup_name}}"
      hosts:
        - host1
        - host2
      state: 'present'
      host_state: 'present-in-group'

  - name: Create host group with hosts using host ID
    dellemc.powerstore.hostgroup:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      hostgroup_name: "{{hostgroup_name}}"
      hosts:
        - c17fc987-bf82-480c-af31-9307b89923c3
      state: 'present'
      host_state: 'present-in-group'

  - name: Get host group details
    dellemc.powerstore.hostgroup:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      hostgroup_name: "{{hostgroup_name}}"
      state: 'present'

  - name: Get host group details using ID
    dellemc.powerstore.hostgroup:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      hostgroup_id: "{{host group_id}}"
      state: 'present'

  - name: Add hosts to host group
    dellemc.powerstore.hostgroup:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      hostgroup_name: "{{hostgroup_name}}"
      hosts:
        - host3
      host_state: 'present-in-group'
      state: 'present'

  - name: Remove hosts from host group
    dellemc.powerstore.hostgroup:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      hostgroup_name: "{{hostgroup_name}}"
      hosts:
        - host3
      host_state: 'absent-in-group'
      state: 'present'

  - name: Rename host group
    dellemc.powerstore.hostgroup:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      hostgroup_name: "{{hostgroup_name}}"
      new_name: "{{new_hostgroup_name}}"
      state: 'present'

  - name: Delete host group
    dellemc.powerstore.hostgroup:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      hostgroup_name: "{{hostgroup_name}}"
      state: 'absent'
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=3 > hostgroup_details </td>
            <td>  complex </td>
            <td> When host group exists </td>
            <td> Details of the host group. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Description about the host group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID given to the host group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > hosts </td>
                <td> complex </td>
                <td>success</td>
                <td> The hosts details which are part of this host group. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The ID of the host. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The name of the host. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the host group. </td>
            </tr>
                                        <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Manisha Agrawal (@agrawm3) <ansible.team@dell.com>

--------------------------------
# Network Module

Manage networks on Dell EMC PowerStore

### Synopsis
 Managing networks on PowerStore Storage System includes getting details of network, modifying attributes of network and adding/removing IP ports to/from storage network.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=2>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=2 > vlan_id</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the VLAN. </td>
        </tr>
                    <tr>
            <td colspan=2 > network_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the network. </td>
        </tr>
                    <tr>
            <td colspan=2 > vasa_provider_credentials</td>
            <td> dict  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Credentials required for re-registering the VASA vendor provider during the reconfiguration of the cluster management IP address. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > password </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td></td>
                <td>  <br> VASA vendor provider password.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > username </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td></td>
                <td>  <br> VASA vendor provider user name.  </td>
            </tr>
                            <tr>
            <td colspan=2 > new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New name of the network. </td>
        </tr>
                    <tr>
            <td colspan=2 > addresses</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> IP addresses to add/remove in IPv4 format. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > current_address </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Existing IPv4 address.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > new_address </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> New IPv4 address.  </td>
            </tr>
                            <tr>
            <td colspan=2 > new_cluster_mgmt_address</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New cluster management IP address in IPv4 format. </td>
        </tr>
                    <tr>
            <td colspan=2 > esxi_credentials</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Credentials required for re-registering the ESXi hosts in the vCenter.  <br> It should be passed only when ESXi host addresses or management network VLAN / prefix / gateway are changed during the reconfiguration of the PowerStore X model appliances.  <br> This parameter is applicable only for PowerStore X model.  <br> This parameter will be ignored if passed for PowerStore T model. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > node_id </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td></td>
                <td>  <br> Node identifier corresponding to the ESXi host.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > password </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td></td>
                <td>  <br> ESXi host root password.  </td>
            </tr>
                            <tr>
            <td colspan=2 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=2 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=2 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=2 > mtu</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Maximum Transmission Unit (MTU) packet size set on network interfaces, in bytes. </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=2 > gateway</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Network gateway in IPv4 format. IP version.  <br> Specify empty string to remove the gateway. </td>
        </tr>
                    <tr>
            <td colspan=2 > wait_for_completion</td>
            <td> bool  </td>
            <td></td>
            <td> False </td>
            <td></td>
            <td> <br> Flag to indicate if the operation should be run synchronously or asynchronously. True signifies synchronous execution. By default, modify operation will run asynchronously. </td>
        </tr>
                    <tr>
            <td colspan=2 > storage_discovery_address</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New storage discovery IP address in IPv4 format.  <br> Specify empty string to remove the storage discovery IP address. </td>
        </tr>
                    <tr>
            <td colspan=2 > port_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-network</li>  <li>absent-in-network</li> </ul></td>
            <td> <br> Specifies whether port should mapped/unmapped from the storage network. </td>
        </tr>
                    <tr>
            <td colspan=2 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the network exist or not. </td>
        </tr>
                    <tr>
            <td colspan=2 > network_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the network.  <br> This parameter is added in 2.0.0.0.  <br> Specify either network_name or network_id for any operation. </td>
        </tr>
                    <tr>
            <td colspan=2 > ports</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Ports to be mapped/unmapped to/from the storage network. </td>
        </tr>
                    <tr>
            <td colspan=2 > prefix_length</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Network prefix length. </td>
        </tr>
                    <tr>
            <td colspan=2 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=2 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                            </table>

### Notes
* It is recommended to perform task asynchronously while changing cluster management address.
* Idempotency is not supported for vasa_provider_credentials and esxi_credentials.
* For PowerStore X model, vasa_provider_credentials has to be specified along with new_cluster_mgmt_address.
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
- name: Get network details using ID
  dellemc.powerstore.network:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    network_id: "NW1"
    state: "present"

- name: Get network details using name
  dellemc.powerstore.network:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    network_name: "Default Management Network"
    state: "present"

- name: Rename the storage network
  dellemc.powerstore.network:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    network_name: "Default Storage Network"
    new_name: "iSCSI Network"
    wait_for_completion: True
    state: "present"

- name: Replace the IP's in the management network and re-register VASA vendor provider
  dellemc.powerstore.network:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    network_id: "NW1"
    addresses:
    - current_address: "100.230.x.x"
      new_address: "100.230.x.x"
    - current_address: "100.230.x.x"
      new_address: "100.230.x.x"
    - current_address: "100.230.x.x"
      new_address: "100.230.x.x"
    new_cluster_mgmt_address: "100.230.x.x"
    vasa_provider_credentials:
      username: "vmadmin"
      password: "{{vm_password}}"
    state: "present"

- name: Map port to the storage network
  dellemc.powerstore.network:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    network_id: "NW6"
    ports:
    - "IP1"
    port_state: "present-in-network"
    state: "present"

- name: Unmap port from the storage network
  dellemc.powerstore.network:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    network_id: "NW6"
    ports:
    - "IP1"
    port_state: "absent-in-network"
    state: "present"

- name: Replace the IP's in the management network and re-register VASA vendor
        provider for X model
  dellemc.powerstore.network:
    array_ip: "{{array_ip1}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    network_id: "NW1"
    vlan_id: 0
    gateway: "100.231.x.x"
    mtu: 1500
    prefix_length: 24
    addresses:
    - current_address: "100.230.x.x"
      new_address: "100.231.x.x"
    - current_address: "100.230.x.x"
      new_address: "100.231.x.x"
    - current_address: "100.230.x.x"
      new_address: "100.231.x.x"
    - current_address: "100.230.x.x"
      new_address: "100.231.x.x"
    - current_address: "100.230.x.x"
      new_address: "100.231.x.x"
    new_cluster_mgmt_address: "100.231.x.x"
    vasa_provider_credentials:
      username: "vmadmin"
      password: "{{vm_password}}"
    esxi_credentials:
    - "node_id": "N1"
      "password": "{{node_password}}"
    - "node_id": "N2"
      "password": "{{node_password}}"
    state: "present"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=5>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=5 > job_details </td>
            <td>  complex </td>
            <td> When asynchronous task is performed. </td>
            <td> The job details. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the job. </td>
            </tr>
                                        <tr>
            <td colspan=5 > network_details </td>
            <td>  complex </td>
            <td> When network exists. </td>
            <td> The network details. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > vcenter_details </td>
                <td> complex </td>
                <td>success</td>
                <td> Details of the vcenter. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Unique identifier of the vCenter instance. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > instance_uuid </td>
                    <td> str </td>
                    <td>success</td>
                    <td> UUID instance of the vCenter. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > address </td>
                    <td> str </td>
                    <td>success</td>
                    <td> IP address of vCenter host, in IPv4, IPv6, or hostname format. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > vendor_provider_status </td>
                    <td> str </td>
                    <td>success</td>
                    <td> General status of the VASA vendor provider in vCenter. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > username </td>
                    <td> str </td>
                    <td>success</td>
                    <td> User name to login to vCenter. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > ip_version </td>
                <td> str </td>
                <td>success</td>
                <td> IP protocol version </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > vlan_id </td>
                <td> int </td>
                <td>success</td>
                <td> VLAN identifier. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > purposes </td>
                <td> list </td>
                <td>success</td>
                <td> Purposes of the network. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the network. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > type </td>
                <td> str </td>
                <td>success</td>
                <td> Network type </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > gateway </td>
                <td> str </td>
                <td>success</td>
                <td> The gateway of the network. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > cluster_details </td>
                <td> complex </td>
                <td>success</td>
                <td> The details of the cluster. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > management_address </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The floating management IP address for the cluster in IPv4 or IPv6 format. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > appliance_count </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Number of appliances configured in this cluster. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The name of the cluster. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > storage_discovery_address </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The floating storage discovery IP address for the cluster in IPv4 or IPv6 format. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The unique identifier of the cluster. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > member_ips </td>
                <td> complex </td>
                <td>success</td>
                <td> Properties of the IP pool address. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > node_id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Unique identifier of the cluster node to which the IP address belongs. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > address </td>
                    <td> str </td>
                    <td>success</td>
                    <td> IP address value, in IPv4 or IPv6 format. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > purposes </td>
                    <td> list </td>
                    <td>success</td>
                    <td> IP address purposes. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > network_id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Unique identifier of the network to which the IP address belongs. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Unique identifier of the IP address. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > appliance_id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Unique identifier of the appliance to which the IP address belongs. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Name of the IP address. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=3 > ip_port_id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Unique identifier of the port that uses this IP address to provide access to storage network services, such as iSCSI. This attribute can be set only for an IP address used by networks of type Storage. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > prefix_length </td>
                <td> int </td>
                <td>success</td>
                <td> Network prefix length. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > mtu </td>
                <td> int </td>
                <td>success</td>
                <td> Maximum Transmission Unit (MTU) packet size set on network interfaces, in bytes. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=4 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the network. </td>
            </tr>
                                        <tr>
            <td colspan=5 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Akash Shendge (@shenda1) <ansible.team@dell.com>

--------------------------------
# NFS Module

Manage NFS exports on Dell EMC PowerStore

### Synopsis
 Managing NFS exports on PowerStore Storage System includes creating new NFS Export, getting details of NFS export, modifying attributes of NFS export, and deleting NFS export.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > snapshot</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID/Name of the Snapshot for which NFS export will be created.  <br> Either filesystem or snapshot is required for creation of the NFS Export.  <br> If snapshot name is specified, then nas_server is required to uniquely identify the snapshot.  <br> If snapshot parameter is provided, then filesystem cannot be specified.  <br> NFS export can be created only if access type of snapshot is "protocol". </td>
        </tr>
                    <tr>
            <td colspan=1 > min_security</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>SYS</li>  <li>KERBEROS</li>  <li>KERBEROS_WITH_INTEGRITY</li>  <li>KERBEROS_WITH_ENCRYPTION</li> </ul></td>
            <td> <br> NFS enforced security type for users accessing an NFS export.  <br> If not specified at the time of creation, it will be set to SYS. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > nfs_export_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the NFS export. </td>
        </tr>
                    <tr>
            <td colspan=1 > read_write_hosts</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Hosts with read and write access to the NFS export. </td>
        </tr>
                    <tr>
            <td colspan=1 > default_access</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>NO_ACCESS</li>  <li>READ_ONLY</li>  <li>READ_WRITE</li>  <li>ROOT</li>  <li>READ_ONLY_ROOT</li> </ul></td>
            <td> <br> Default access level for all hosts that can access the Export.  <br> For hosts that need different access than the default, they can be configured by adding to the list.  <br> If default_access is not mentioned during creation, then NFS export will be created with No_Access. </td>
        </tr>
                    <tr>
            <td colspan=1 > no_access_hosts</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Hosts with no access to the NFS export. </td>
        </tr>
                    <tr>
            <td colspan=1 > read_only_hosts</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Hosts with read-only access to the NFS export. </td>
        </tr>
                    <tr>
            <td colspan=1 > nas_server</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The NAS server. This could be the name or ID of the NAS server. </td>
        </tr>
                    <tr>
            <td colspan=1 > anonymous_uid</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Specifies the user ID of the anonymous account.  <br> If not specified at the time of creation, it will be set to -2. </td>
        </tr>
                    <tr>
            <td colspan=1 > is_no_suid</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> If set, do not allow access to set SUID. Otherwise, allow access.  <br> If not specified at the time of creation, it will be set to False. </td>
        </tr>
                    <tr>
            <td colspan=1 > path</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Local path to export relative to the NAS server root.  <br> With NFS, each export of a file_system or file_snap must have a unique local path.  <br> Mandatory while creating NFS export. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the NFS export should exist or not. </td>
        </tr>
                    <tr>
            <td colspan=1 > nfs_export_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the NFS export.  <br> Mandatory for create operation.  <br> Specify either nfs_export_name or nfs_export_id(but not both) for any operation. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > read_only_root_hosts</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Hosts with read-only access for root user to the NFS export. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > anonymous_gid</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Specifies the group ID of the anonymous account.  <br> If not specified at the time of creation, it will be set to -2. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > read_write_root_hosts</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Hosts with read and write access for root user to the NFS export. </td>
        </tr>
                    <tr>
            <td colspan=1 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The description for the NFS export. </td>
        </tr>
                    <tr>
            <td colspan=1 > filesystem</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID/Name of the filesystem for which the NFS export will be created.  <br> Either filesystem or snapshot is required for creation of the NFS Export.  <br> If filesystem name is specified, then nas_server is required to uniquely identify the filesystem.  <br> If filesystem parameter is provided, then snapshot cannot be specified. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > host_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-export</li>  <li>absent-in-export</li> </ul></td>
            <td> <br> Define whether the hosts can access the NFS export.  <br> Required when adding or removing host access from the export. </td>
        </tr>
                            </table>

### Notes
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
- name: Create NFS export (filesystem)
  dellemc.powerstore.nfs:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    nfs_export_name: "{{export_name1}}"
    filesystem: "{{filesystem}}"
    nas_server: "{{nas_server}}"
    path: "{{path1}}"
    description: "sample description"
    default_access: "NO_ACCESS"
    no_access_hosts:
      - "{{host5}}"
    read_only_hosts:
      - "{{host1}}"
    read_only_root_hosts:
      - "{{host2}}"
    read_write_hosts:
      - "{{host3}}"
    read_write_root_hosts:
      - "{{host4}}"
    min_security: "SYS"
    anonymous_uid: 1000
    anonymous_gid: 1000
    is_no_suid: True
    host_state: "present-in-export"
    state: "present"

- name: Create NFS export Create NFS export for filesystem snapshot with mandatory parameters
  dellemc.powerstore.nfs:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    nfs_export_name: "{{export_name2}}"
    snapshot: "{{snapshot}}"
    nas_server: "{{nas_server}}"
    path: "{{path2}}"
    state: "present"

- name: Get NFS export details using ID
  dellemc.powerstore.nfs:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    nfs_export_id: "{{export_id}}"
    state: "present"

- name: Add Read-Only and Read-Write hosts to NFS export
  dellemc.powerstore.nfs:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    nfs_export_id: "{{export_id}}"
    read_only_hosts:
      - "{{host5}}"
    read_write_hosts:
      - "{{host6}}"
    host_state: "present-in-export"
    state: "present"

- name: Remove Read-Only and Read-Write hosts from NFS export
  dellemc.powerstore.nfs:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    nfs_export_id: "{{export_id}}"
    read_only_hosts:
      - "{{host1}}"
    read_write_hosts:
      - "{{host3}}"
    host_state: "absent-in-export"
    state: "present"

- name: Modify the attributes of NFS export
  dellemc.powerstore.nfs:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    nfs_export_id: "{{export_id}}"
    description: "modify description"
    default_access: "ROOT"
    state: "present"

- name: Delete NFS export using name
  dellemc.powerstore.nfs:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    nfs_export_name: "{{export_name}}"
    nas_server: "{{nas_server}}"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=4>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=4 > nfs_export_details </td>
            <td>  complex </td>
            <td> When NFS export exists. </td>
            <td> The NFS export details. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > read_only_root_hosts </td>
                <td> list </td>
                <td>success</td>
                <td> Hosts with read-only for root user access to the NFS export. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > min_security </td>
                <td> str </td>
                <td>success</td>
                <td> NFS enforced security type for users accessing an NFS export. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > anonymous_GID </td>
                <td> int </td>
                <td>success</td>
                <td> The group ID of the anonymous account. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > path </td>
                <td> str </td>
                <td>success</td>
                <td> Local path to a location within the file system. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > read_write_hosts </td>
                <td> list </td>
                <td>success</td>
                <td> Hosts with read and write access to the NFS export. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > default_access </td>
                <td> str </td>
                <td>success</td>
                <td> Default access level for all hosts that can access the export. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > is_no_SUID </td>
                <td> bool </td>
                <td>success</td>
                <td> If set, do not allow access to set SUID. Otherwise, allow access. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the NFS export. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > file_system </td>
                <td> complex </td>
                <td>success</td>
                <td> Details of filesystem and NAS server on which NFS export is present. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > filesystem_type </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The type of the filesystem. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > nas_server </td>
                    <td> complex </td>
                    <td>success</td>
                    <td> Details of NAS server. </td>
                </tr>
                                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=1 > id </td>
                        <td> str </td>
                        <td>success</td>
                        <td> The ID of the NAS server. </td>
                    </tr>
                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=1 > name </td>
                        <td> str </td>
                        <td>success</td>
                        <td> The name of the NAS server. </td>
                    </tr>
                                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The name of the filesystem. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The ID of the filesystem. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > read_write_root_hosts </td>
                <td> list </td>
                <td>success</td>
                <td> Hosts with read and write for root user access to the NFS export. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > read_only_hosts </td>
                <td> list </td>
                <td>success</td>
                <td> Hosts with read-only access to the NFS export. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > no_access_hosts </td>
                <td> list </td>
                <td>success</td>
                <td> Hosts with no access to the NFS export. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > description </td>
                <td> str </td>
                <td>success</td>
                <td> The description for the NFS export. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > anonymous_UID </td>
                <td> int </td>
                <td>success</td>
                <td> The user ID of the anonymous account. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the NFS export. </td>
            </tr>
                                        <tr>
            <td colspan=4 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Akash Shendge (@shenda1) <ansible.team@dell.com>

--------------------------------
# Snapshot Rule Module

Snapshot Rule operations on a PowerStore storage system

### Synopsis
 Performs all snapshot rule operations on PowerStore Storage System.
 This modules supports get details of a snapshot rule, create new Snapshot Rule with Interval, create new Snapshot Rule with specific time and days_of_week. Modify Snapshot Rule. Delete Snapshot Rule.

### Parameters
                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshotrule_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> String variable. Indicates the ID of the Snapshot rule. </td>
        </tr>
                    <tr>
            <td colspan=1 > time_of_day</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> String variable. Indicates the time of the day to take a daily Snapshot, with the format "hh:mm" in 24 hour time format.  <br> When creating a Snapshot rule, specify either "interval"or "time_of_day" but not both. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > desired_retention</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Integer variable. Indicates the desired Snapshot retention period.  <br> It is required when creating a new Snapshot rule. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > delete_snaps</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Boolean variable to specify whether all Snapshots previously created by this rule should also be deleted when this rule is removed.  <br> True specifies to delete all previously created Snapshots by this rule while deleting this rule.  <br> False specifies to retain all previously created Snapshots while deleting this rule. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> String variable. Indicates the new name of the Snapshot rule.  <br> Used for renaming operation. </td>
        </tr>
                    <tr>
            <td colspan=1 > days_of_week</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td> <ul> <li>Monday</li>  <li>Tuesday</li>  <li>Wednesday</li>  <li>Thursday</li>  <li>Friday</li>  <li>Saturday</li>  <li>Sunday</li> </ul></td>
            <td> <br> List of strings to specify days of the week on which the Snapshot rule should be applied. Must be applied for Snapshot rules where the 'time_of_day' parameter is set.  <br> Optional for the Snapshot rule created with an interval. When 'days_of_week' is not specified for a new Snapshot rule, the rule is applied on every day of the week. </td>
        </tr>
                    <tr>
            <td colspan=1 > interval</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>Five_Minutes</li>  <li>Fifteen_Minutes</li>  <li>Thirty_Minutes</li>  <li>One_Hour</li>  <li>Two_Hours</li>  <li>Three_Hours</li>  <li>Four_Hours</li>  <li>Six_Hours</li>  <li>Eight_Hours</li>  <li>Twelve_Hours</li>  <li>One_Day</li> </ul></td>
            <td> <br> String variable. Indicates the interval between Snapshots.  <br> When creating a Snapshot rule, specify either "interval" or "time_of_day", but not both. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> String variable indicates the state of Snapshot rule.  <br> For "Delete" operation only, it should be set to "absent".  <br> For all Create, Modify or Get details operation it should be set to "present". </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> String variable. Indicates the name of the Snapshot rule. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                            </table>

### Notes
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
- name: Get details of an existing snapshot rule by name
  dellemc.powerstore.snapshotrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    state: "present"

- name: Get details of an existing snapshot rule by id
  dellemc.powerstore.snapshotrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    snapshotrule_id: "{{snapshotrule_id}}"
    state: "present"

- name: Create new snapshot rule by interval
  dellemc.powerstore.snapshotrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    interval: "{{interval}}"
    days_of_week:
          - Monday
    desired_retention: "{{desired_retention}}"
    state: "present"


- name: Create new snapshot rule by time_of_day and days_of_week
  dellemc.powerstore.snapshotrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    desired_retention: "{{desired_retention}}"
    days_of_week:
      - Monday
      - Wednesday
      - Friday
    time_of_day: "{{time_of_day}}"
    state: "present"

- name: Modify existing snapshot rule to time_of_day and days_of_week
  dellemc.powerstore.snapshotrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    days_of_week:
      - Monday
      - Wednesday
      - Friday
      - Sunday
    time_of_day: "{{time_of_day}}"
    state: "present"

- name: Modify existing snapshot rule to interval
  dellemc.powerstore.snapshotrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    interval: "{{interval}}"
    state: "present"

- name: Delete an existing snapshot rule by name
  dellemc.powerstore.snapshotrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=3 > snapshotrule_details </td>
            <td>  complex </td>
            <td> When snapshot rule exists </td>
            <td> Details of the snapshot rule. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > days_of_week </td>
                <td> list </td>
                <td>success</td>
                <td> List of string to specify days of the week on which the rule should be applied. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > policies </td>
                <td> complex </td>
                <td>success</td>
                <td> The protection policies details of the snapshot rule. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The protection policy ID in which the snapshot rule is selected. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Name of the protection policy in which the snapshot rule is selected. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > desired_retention </td>
                <td> int </td>
                <td>success</td>
                <td> Desired snapshot retention period. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID given to the snapshot rule. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > interval </td>
                <td> str </td>
                <td>success</td>
                <td> The interval between snapshots. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the snapshot rule. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > time_of_day </td>
                <td> str </td>
                <td>success</td>
                <td> The time of the day to take a daily snapshot. </td>
            </tr>
                                        <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Arindam Datta (@dattaarindam) <ansible.team@dell.com>

--------------------------------
# Volume Group Module

Manage volume groups on a PowerStore Storage System

### Synopsis
 Managing volume group on PowerStore Storage System includes creating new volume group, adding volumes to volume group, removing volumes from volume group.
 Module also include renaming volume group, modifying volume group, and deleting volume group.

### Parameters
                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > is_write_order_consistent</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> A boolean flag to indicate whether Snapshot sets of the volume group will be write-order consistent.  <br> If this parameter is not specified, the array by default sets it to true. </td>
        </tr>
                    <tr>
            <td colspan=1 > vg_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the volume group. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > volumes</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This is a list of volumes.  <br> Either the volume ID or name must be provided for adding/removing existing volumes from a volume group.  <br> If volumes are given, then vol_state should also be specified. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > vol_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-group</li>  <li>absent-in-group</li> </ul></td>
            <td> <br> String variable. Describes the state of volumes inside a volume group.  <br> If volume is given, then vol_state should also be specified. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > vg_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The id of the volume group.  <br> It can be used only for Modify, Add/Remove, or Delete operation. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_vg_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The new name of the volume group. </td>
        </tr>
                    <tr>
            <td colspan=1 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Description about the volume group. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the volume group should exist or not. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > protection_policy</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> String variable. Represents Protection policy id or name used for volume group.  <br> Specifying an empty string or "" removes the existing protection policy from volume group. </td>
        </tr>
                            </table>

### Notes
* Parameter vol_state is mandatory if volumes are provided.
* A protection policy can be specified either for an volume group, or for the individual volumes inside the volume group.
* A volume can be a member of at most one volume group.
* Specifying "protection_policy" as empty string or "" removes the existing protection policy from a volume group.
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
- name: Create volume group without protection policy
  dellemc.powerstore.volumegroup:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vg_name: "{{vg_name}}"
    description: "This volume group is for ansible"
    state: "present"

- name: Get details of volume group
  dellemc.powerstore.volumegroup:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vg_name: "{{vg_name}}"
    state: "present"

- name: Add volumes to volume group
  dellemc.powerstore.volumegroup:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vg_name: "{{vg_name}}"
    state: "present"
    volumes:
      - "7f879569-676c-4749-a06f-c2c30e09b295"
      - "68e4dad5-5de5-4644-a98f-6d4fb916e169"
      - "Ansible_Testing"
    vol_state: "present-in-group"

- name: Remove volumes from volume group
  dellemc.powerstore.volumegroup:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vg_name: "{{vg_name}}"
    state: "present"
    volumes:
      - "7f879569-676c-4749-a06f-c2c30e09b295"
      - "Ansible_Testing"
    vol_state: "absent-in-group"

- name: Rename volume group and change is_write_order_consistent flag
  dellemc.powerstore.volumegroup:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vg_name: "{{vg_name}}"
    new_vg_name: "{{new_vg_name}}"
    is_write_order_consistent: False
    state: "present"

- name: Get details of volume group by ID
  dellemc.powerstore.volumegroup:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vg_id: "{{vg_id}}"
    state: "present"

- name: Delete volume group
  dellemc.powerstore.volumegroup:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{new_vg_name}}"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=3 > delete_vg </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume group got deleted. </td>
        </tr>
                    <tr>
            <td colspan=3 > add_vols_to_vg </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume/s got added to volume group. </td>
        </tr>
                    <tr>
            <td colspan=3 > create_vg </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume group got created. </td>
        </tr>
                    <tr>
            <td colspan=3 > remove_vols_from_vg </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume/s got removed from volume group. </td>
        </tr>
                    <tr>
            <td colspan=3 > modify_vg </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume group got modified. </td>
        </tr>
                    <tr>
            <td colspan=3 > volume_group_details </td>
            <td>  complex </td>
            <td> When volume group exists </td>
            <td> Details of the volume group. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > description </td>
                <td> str </td>
                <td>success</td>
                <td> description about the volume group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > volumes </td>
                <td> complex </td>
                <td>success</td>
                <td> The volumes details of the volume group. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The system generated ID given to the volume associated with the volume group. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The name of the volume associated with the volume group. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID given to the volume group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > type </td>
                <td> str </td>
                <td>success</td>
                <td> The type of the volume group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > is_write_order_consistent </td>
                <td> bool </td>
                <td>success</td>
                <td> A boolean flag to indicate whether snapshot sets of the volume group will be write-order consistent. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the volume group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > protection_policy_id </td>
                <td> str </td>
                <td>success</td>
                <td> The protection policy of the volume group. </td>
            </tr>
                                        <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Akash Shendge (@shenda1) <ansible.team@dell.com>
* Arindam Datta (@dattaarindam) <ansible.team@dell.com>

--------------------------------
# Remote Support Contact Module

Remote Support Contact operations on a PowerStore storage system

### Synopsis
 Performs all Remote Support Contact operations on a PowerStore Storage system. This module supports get details and you can modify a Remote Support Contact with supported parameters.

### Parameters
                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > phone</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The phone number of this support contact for this system. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > first_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The first name of the support contact for this system. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > last_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The last name of the support contact for this system. </td>
        </tr>
                    <tr>
            <td colspan=1 > email</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The email address of the support contact for this system. </td>
        </tr>
                    <tr>
            <td colspan=1 > contact_id</td>
            <td> int  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> Unique identifier of the remote support contact. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> The state of the remote support contact after the task is performed.  <br> For Delete operation only, it should be set to "absent".  <br> For get/modify operation it should be set to "present". </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                            </table>

### Notes
* Creation and deletion of remote support contact is not supported.
* Parameters first_name, last_name, email and phone can be removed by passing empty string.
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
  - name: Get details of remote support contact
    dellemc.powerstore.remote_support_contact:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       contact_id: 0
       state: "present"

  - name: Modify remote support contact
    dellemc.powerstore.remote_support_contact:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       contact_id: 0
       first_name: "abc"
       last_name: "xyz"
       phone: "111-222-333-444"
       email: "abc_xyz@dell.com"
       state: "present"
```

### Return Values
                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > remote_support_contact_details </td>
            <td>  complex </td>
            <td> When remote support contact exists. </td>
            <td> Details of the remote support contact. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> int </td>
                <td>success</td>
                <td> Unique identifier of remote support contact. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > phone </td>
                <td> str </td>
                <td>success</td>
                <td> The phone number of this support contact for this system. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > email </td>
                <td> str </td>
                <td>success</td>
                <td> The email address of the support contact for this system. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > last_name </td>
                <td> str </td>
                <td>success</td>
                <td> The last name of the support contact for this system. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > first_name </td>
                <td> str </td>
                <td>success</td>
                <td> The first name of the support contact for this system. </td>
            </tr>
                                        <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>

--------------------------------
# NAS Server Module

NAS Server operations on PowerStore Storage system

### Synopsis
 Supports getting the details and modifying the attributes of a NAS server.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Description of the NAS server. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > current_unix_directory_service</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>NIS</li>  <li>LDAP</li>  <li>LOCAL_FILES</li>  <li>LOCAL_THEN_NIS</li>  <li>LOCAL_THEN_LDAP</li> </ul></td>
            <td> <br> Define the Unix directory service used for looking up identity information for Unix such as UIDs, GIDs, net groups, and so on. </td>
        </tr>
                    <tr>
            <td colspan=1 > preferred_node</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Unique identifier or name of the preferred node for the NAS server. The initial value (on NAS server create) is taken from the current node. </td>
        </tr>
                    <tr>
            <td colspan=1 > default_windows_user</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Default Windows user name used for granting access in case of Unix to Windows user mapping failure. When empty, access in such case is denied. </td>
        </tr>
                    <tr>
            <td colspan=1 > current_node</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Unique identifier or name of the node on which the NAS server is running. </td>
        </tr>
                    <tr>
            <td colspan=1 > nas_server_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Unique id of the NAS server. Mutually exclusive with nas_server_name. </td>
        </tr>
                    <tr>
            <td colspan=1 > nas_server_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the NAS server. Mutually exclusive with nas_server_id. </td>
        </tr>
                    <tr>
            <td colspan=1 > default_unix_user</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Default Unix user name used for granting access in case of Windows to Unix user mapping failure. When empty, access in such case is denied. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the nas server should exist or not. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > nas_server_new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New name of the NAS server for a rename operation. </td>
        </tr>
                            </table>

### Notes
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
 - name: Get details of NAS Server by name
   dellemc.powerstore.nasserver:
     array_ip: "{{array_ip}}"
     verifycert: "{{verifycert}}"
     user: "{{user}}"
     password: "{{password}}"
     nas_server_name: "{{nas_server_name}}"
     state: "present"

 - name: Get Details of NAS Server by ID
   dellemc.powerstore.nasserver:
     array_ip: "{{array_ip}}"
     verifycert: "{{verifycert}}"
     user: "{{user}}"
     password: "{{password}}"
     nas_server_id: "{{nas_id}}"
     state: "present"

 - name: Rename NAS Server by Name
   dellemc.powerstore.nasserver:
     array_ip: "{{array_ip}}"
     verifycert: "{{verifycert}}"
     user: "{{user}}"
     password: "{{password}}"
     nas_server_name: "{{nas_server_name}}"
     nas_server_new_name : "{{nas_server_new_name}}"
     state: "present"

 - name: Modify NAS Server attributes by ID
   dellemc.powerstore.nasserver:
     array_ip: "{{array_ip}}"
     verifycert: "{{verifycert}}"
     user: "{{user}}"
     password: "{{password}}"
     nas_server_id: "{{nas_id}}"
     current_unix_directory_service: "LOCAL_FILES"
     current_node: "{{cur_node_n1}}"
     preferred_node: "{{prefered_node}}"
     state: "present"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > nasserver_details </td>
            <td>  complex </td>
            <td> When nas server exists </td>
            <td> Details about the nas server. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > backup_IPv4_interface_id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the preferred IPv4 backup interface. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > production_IPv6_interface_id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the preferred IPv6 production interface. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > smb_servers </td>
                <td> str </td>
                <td>success</td>
                <td> This is the inverse of the resource type smb_server association. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > backup_IPv6_interface_id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the preferred IPv6 backup interface. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > file_interfaces </td>
                <td> dict </td>
                <td>success</td>
                <td> This is the inverse of the resource type file_interface association. Will return the id,name & ip_address of the associated file interface. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > operational_status </td>
                <td> str </td>
                <td>success</td>
                <td> NAS server operational status. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > file_ldaps </td>
                <td> str </td>
                <td>success</td>
                <td> This is the inverse of the resource type file_ldap association. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > nfs_servers </td>
                <td> str </td>
                <td>success</td>
                <td> This is the inverse of the resource type nfs_server association. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_username_translation_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Enable the possibility to match a windows account to a Unix account with different names. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > current_unix_directory_service </td>
                <td> str </td>
                <td>success</td>
                <td> Define the Unix directory service used for looking up identity information for Unix such as UIDs, GIDs, net groups, and so on. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > preferred_node </td>
                <td> dict </td>
                <td>success</td>
                <td> Unique identifier and name of the preferred node for the NAS server. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID given to the nas server. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > production_IPv4_interface_id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the preferred IPv4 production interface. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > current_node </td>
                <td> dict </td>
                <td>success</td>
                <td> Unique identifier and name of the node on which the NAS server is running. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > default_unix_user </td>
                <td> str </td>
                <td>success</td>
                <td> Default Unix user name used for granting access in case of Windows to Unix user mapping failure. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Additional information about the nas server. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the nas server. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > file_systems </td>
                <td> dict </td>
                <td>success</td>
                <td> This is the inverse of the resource type file_system association. </td>
            </tr>
                                        <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Arindam Datta (@dattaarindam) <ansible.team@dell.com>

--------------------------------
# Filesystem Snapshot Module

Manage Filesystem Snapshots on Dell EMC PowerStore

### Synopsis
 Supports the provisioning operations on a filesystem snapshot such as create, modify, delete and get the details of a filesystem snapshot.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshot_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the filesystem snapshot.  <br> Mandatory for create operation.  <br> Specify either snapshot name or ID (but not both) for any operation. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > desired_retention</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The retention value for the Snapshot.  <br> If the desired_retention/expiration_timestamp is not mentioned during creation, snapshot will be created with unlimited retention.  <br> Maximum supported desired retention is 31 days. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > retention_unit</td>
            <td> str  </td>
            <td></td>
            <td> hours </td>
            <td> <ul> <li>hours</li>  <li>days</li> </ul></td>
            <td> <br> The unit for retention. </td>
        </tr>
                    <tr>
            <td colspan=1 > filesystem</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID/Name of the filesystem for which snapshot will be taken.  <br> If filesystem name is specified, then nas_server is required to uniquely identify the filesystem.  <br> Mandatory for create operation. </td>
        </tr>
                    <tr>
            <td colspan=1 > access_type</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>SNAPSHOT</li>  <li>PROTOCOL</li> </ul></td>
            <td> <br> Specifies whether the snapshot directory or protocol access is granted to the filesystem snapshot.  <br> For create operation, if access_type is not specified, snapshot will be created with 'SNAPSHOT' access type. </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshot_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the Snapshot. </td>
        </tr>
                    <tr>
            <td colspan=1 > expiration_timestamp</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The expiration timestamp of the snapshot. This should be provided in UTC format, e.g 2020-07-24T10:54:54Z.  <br> To remove the expiration timestamp, specify it as an empty string. </td>
        </tr>
                    <tr>
            <td colspan=1 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The description for the filesystem snapshot. </td>
        </tr>
                    <tr>
            <td colspan=1 > nas_server</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The NAS server, this could be the name or ID of the NAS server. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the filesystem snapshot should exist or not. </td>
        </tr>
                            </table>

### Notes
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
- name: Create filesystem snapshot
  dellemc.powerstore.filesystem_snapshot:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      snapshot_name: "sample_filesystem_snapshot"
      nas_server: "ansible_nas_server"
      filesystem: "sample_filesystem"
      desired_retention: 20
      retention_unit: "days"
      state: "present"

- name: Get the details of filesystem snapshot
  dellemc.powerstore.filesystem_snapshot:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      snapshot_id: "{{fs_snapshot_id}}"
      state: "present"

- name: Modify the filesystem snapshot
  dellemc.powerstore.filesystem_snapshot:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      snapshot_name: "sample_filesystem_snapshot"
      nas_server: "ansible_nas_server"
      description: "modify description"
      expiration_timestamp: ""
      state: "present"

- name: Delete filesystem snapshot
  dellemc.powerstore.filesystem_snapshot:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      snapshot_id: "{{fs_snapshot_id}}"
      state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=3 > create_fs_snap </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has created. </td>
        </tr>
                    <tr>
            <td colspan=3 > filesystem_snap_details </td>
            <td>  dict </td>
            <td> When snapshot exists. </td>
            <td> Details of the snapshot. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > access_type </td>
                <td> str </td>
                <td>success</td>
                <td> Displays the type of access allowed to the snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > parent_name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the filesystem on which snapshot is taken. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > expiration_timestamp </td>
                <td> str </td>
                <td>success</td>
                <td> The date and time the snapshot is due to be automatically deleted by the system. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the filesystem snapshot instance. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > nas_server </td>
                <td> dict </td>
                <td>success</td>
                <td> Details of NAS server on which snapshot is present. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> ID of the NAS server. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Name of the NAS server </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Description of the filesystem snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > creation_timestamp </td>
                <td> str </td>
                <td>success</td>
                <td> The date and time the snapshot was created. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > parent_id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the filesystem on which snapshot is taken. </td>
            </tr>
                                        <tr>
            <td colspan=3 > delete_fs_snap </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has deleted. </td>
        </tr>
                    <tr>
            <td colspan=3 > modify_fs_snap </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has modified. </td>
        </tr>
                    <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Akash Shendge (@shenda1) <ansible.team@dell.com>

--------------------------------
# Security Config Module

Security configuration operations on PowerStore Storage System

### Synopsis
 Managing security configuration on PowerStore storage system includes getting details and modifying security configuration parameters.

### Parameters
                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > protocol_mode</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>TLSv1_0</li>  <li>TLSv1_1</li>  <li>TLSv1_2</li> </ul></td>
            <td> <br> Protocol mode of the security configuration.  <br> Mandatory only for modify operation. </td>
        </tr>
                    <tr>
            <td colspan=1 > security_config_id</td>
            <td> int  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> ID of the security configuration.  <br> Mandatory for all operations. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the security config should exist or not. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                            </table>

### Notes
* Creation and deletion of security configs is not supported by Ansible modules.
* Modification of protocol mode is only supported for PowerStore v2.0.0.0 and above.
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
- name: Get security config
  dellemc.powerstore.security_config:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    security_config_id: 1
    state: "present"

- name: Modify attribute of security config
  dellemc.powerstore.security_config:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    security_config_id: 1
    protocol_mode: "TLSv1_1"
    state: "present"
```

### Return Values
                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > security_config_details </td>
            <td>  complex </td>
            <td> When security config exists </td>
            <td> Details of the security configuration. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID given to the security configuration. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > protocol_mode </td>
                <td> str </td>
                <td>success</td>
                <td> The protocol mode of the security configuration. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > idle_timeout </td>
                <td> int </td>
                <td>success</td>
                <td> Idle time (in seconds) after which login sessions will expire and require re-authentication. </td>
            </tr>
                                        <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Bhavneet Sharma (@sharmb5) <ansible.team@dell.com>

--------------------------------
# Host Module

Manage host on PowerStore storage system

### Synopsis
 Managing host on PowerStore storage system includes create host with a set of initiators, add/remove initiators from host, rename host and delete host.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=2>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=2 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=2 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=2 > host_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The 36 character long host id automatically generated when a host is created.  <br> Use either host_id or host_name for modify and delete tasks.  <br> The host_id cannot be used while creating host, as it is generated by the array after creation of host. </td>
        </tr>
                    <tr>
            <td colspan=2 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the host should exist or not.  <br> Value present - indicates that the host should exist in system.  <br> Value absent - indicates that the host should not exist in system. </td>
        </tr>
                    <tr>
            <td colspan=2 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=2 > new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The new name of host for renaming function. This value must contain 128 or fewer printable Unicode characters.  <br> Cannot be specified when creating a host. </td>
        </tr>
                    <tr>
            <td colspan=2 > initiator_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-host</li>  <li>absent-in-host</li> </ul></td>
            <td> <br> Define whether the initiators should be present or absent in host.  <br> Value present-in-host - indicates that the initiators should exist on host.  <br> Value absent-in-host - indicates that the initiators should not exist on host.  <br> Required when creating a host with initiators or adding/removing initiators to/from existing host. </td>
        </tr>
                    <tr>
            <td colspan=2 > host_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The host name. This value must contain 128 or fewer printable Unicode characters.  <br> Creation of an empty host is not allowed.  <br> Required when creating a host.  <br> Use either host_id or host_name for modify and delete tasks. </td>
        </tr>
                    <tr>
            <td colspan=2 > os_type</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>Windows</li>  <li>Linux</li>  <li>ESXi</li>  <li>AIX</li>  <li>HP-UX</li>  <li>Solaris</li> </ul></td>
            <td> <br> Operating system of the host.  <br> Required when creating a host.  <br> OS type cannot be modified for a given host. </td>
        </tr>
                    <tr>
            <td colspan=2 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=2 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=2 > detailed_initiators</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Initiator properties.  <br> It is mutually exclusive with initiators. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > chap_mutual_username </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Username for mutual CHAP authentication.  <br> CHAP username is required when the cluster CHAP mode is mutual authentication.  <br> Minimum length is 1 and maximum length is 64 characters.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > port_name </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td></td>
                <td>  <br> Name of port type.  <br> The port_name is mandatory key.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > chap_single_username </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Username for single CHAP authentication.  <br> CHAP username is required when the cluster CHAP mode is mutual authentication.  <br> Minimum length is 1 and maximum length is 64 characters.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > chap_single_password </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Password for single CHAP authentication.  <br> CHAP password is required when the cluster CHAP mode is mutual authentication.  <br> Minimum length is 12 and maximum length is 64 characters.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > port_type </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td> <ul> <li>iSCSI</li>  <li>FC</li>  <li>NVMe</li> </ul></td>
                <td>  <br> Protocol type of the host initiator.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > chap_mutual_password </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Password for mutual CHAP authentication.  <br> CHAP password is required when the cluster CHAP mode is mutual authentication.  <br> Minimum length is 12 and maximum length is 64 characters.  </td>
            </tr>
                            <tr>
            <td colspan=2 > initiators</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> List of Initiator WWN or IQN or NQN to be added or removed from the host.  <br> Subordinate initiators in a host can only be of one type, either FC or iSCSI.  <br> Required when creating a host.  <br> It is mutually exclusive with detailed_initiators. </td>
        </tr>
                            </table>

### Notes
* Only completely and correctly configured iSCSI initiators can be associated with a host.
* The parameters initiators and detailed_initiators are mutually exclusive.
* For mutual CHAP authentication, single CHAP credentials are mandatory.
* Support of NVMe type of initiators is for PowerStore 2.0 and beyond.
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
  - name: Create host with FC initiator
    dellemc.powerstore.host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_name: "ansible-test-host-1"
      os_type: 'Windows'
      initiators:
        - 21:00:00:24:ff:31:e9:fc
      state: 'present'
      initiator_state: 'present-in-host'

  - name: Create host with iSCSI initiator and its details
    dellemc.powerstore.host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_name: "ansible-test-host-2"
      os_type: 'Windows'
      detailed_initiators:
        - port_name: 'iqn.1998-01.com.vmware:lgc198248-5b06fb37'
          port_type: 'iSCSI'
          chap_single_username: 'chapuserSingle'
          chap_single_password: 'chappasswd12345'
        - port_name: 'iqn.1998-01.com.vmware:imn198248-5b06fb37'
          port_type: 'iSCSI'
          chap_mutual_username: 'chapuserMutual'
          chap_mutual_password: 'chappasswd12345'
      state: 'present'
      initiator_state: 'present-in-host'

  - name: Get host details by name
    dellemc.powerstore.host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_name: "ansible-test-host-1"
      state: 'present'

  - name: Get host details by id
    dellemc.powerstore.host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_id: "5c1e869b-ed8a-4845-abae-b102bc249d41"
      state: 'present'

  - name: Add initiators to host by name
    dellemc.powerstore.host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_name: "ansible-test-host-1"
      initiators:
        - 21:00:00:24:ff:31:e9:ee
      initiator_state: 'present-in-host'
      state: 'present'

  - name: Add initiators to host by id
    dellemc.powerstore.host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_id: "5c1e869b-ed8a-4845-abae-b102bc249d41"
      detailed_initiators:
        - port_name: 'iqn.1998-01.com.vmware:imn198248-5b06fb37'
          port_type: 'iSCSI'
          chap_mutual_username: 'chapuserMutual'
          chap_mutual_password: 'chappasswd12345'
      initiator_state: 'present-in-host'
      state: 'present'

  - name: Remove initiators from host by name
    dellemc.powerstore.host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_name: "ansible-test-host-2"
      detailed_initiators:
        - port_name: 'iqn.1998-01.com.vmware:imn198248-5b06fb37'
          port_type: 'iSCSI'
          chap_mutual_username: 'chapuserMutual'
          chap_mutual_password: 'chappasswd12345'
      initiator_state: 'absent-in-host'
      state: 'present'

  - name: Remove initiators from by id
    dellemc.powerstore.host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_id: "8c1e869b-fe8a-4845-hiae-h802bc249d41"
      initiators:
        - 21:00:00:24:ff:31:e9:ee
      initiator_state: 'absent-in-host'
      state: 'present'

  - name: Rename host by name
    dellemc.powerstore.host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_name: "ansible-test-host-1"
      new_name: "ansible-test-host-1-new"
      state: 'present'

  - name: Rename host by id
    dellemc.powerstore.host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_id: "5c1e869b-ed8a-4845-abae-b102bc249d41"
      new_name: "ansible-test-host-2-new"
      state: 'present'

  - name: Delete host
    dellemc.powerstore.host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_name: "ansible-test-host-1-new"
      state: 'absent'

  - name: Delete host by id
    dellemc.powerstore.host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_id: "5c1e869b-ed8a-4845-abae-b102bc249d41"
      state: 'absent'
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=6>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=6 > host_details </td>
            <td>  complex </td>
            <td> When host exists </td>
            <td> Details of the host. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Description about the host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > os_type </td>
                <td> str </td>
                <td>success</td>
                <td> The os type of the host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > mapped_hosts </td>
                <td> complex </td>
                <td>success</td>
                <td> This is the inverse of the resource type host_volume_mapping association. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Unique identifier of a mapping between a host and a volume. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > volume </td>
                    <td> dict </td>
                    <td>success</td>
                    <td> Details about a volume which has mapping with the host. </td>
                </tr>
                                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=3 > id </td>
                        <td> str </td>
                        <td>success</td>
                        <td> ID of the volume. </td>
                    </tr>
                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=3 > name </td>
                        <td> str </td>
                        <td>success</td>
                        <td> Name of the volume. </td>
                    </tr>
                                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > host_group </td>
                    <td> dict </td>
                    <td>success</td>
                    <td> Details about a host group to which host is mapped. </td>
                </tr>
                                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=3 > id </td>
                        <td> str </td>
                        <td>success</td>
                        <td> ID of the host group. </td>
                    </tr>
                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=3 > name </td>
                        <td> str </td>
                        <td>success</td>
                        <td> Name of the host group. </td>
                    </tr>
                                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > logical_unit_number </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Logical unit number for the host volume access. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID given to the host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > type </td>
                <td> str </td>
                <td>success</td>
                <td> Type of the host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > host_group_id </td>
                <td> str </td>
                <td>success</td>
                <td> The host group ID of host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > host_initiators </td>
                <td> complex </td>
                <td>success</td>
                <td> The initiator details of this host. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > active_sessions </td>
                    <td> list </td>
                    <td>success</td>
                    <td> List of active login sessions between an initiator and a target port. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > chap_mutual_username </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Username for mutual CHAP authentication. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > port_name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Name of the port. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > chap_single_username </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Username for single CHAP authentication. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > port_type </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The type of the port. </td>
                </tr>
                                                                    <tr>
            <td colspan=6 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Manisha Agrawal (@agrawm3) <ansible.team@dell.com>

--------------------------------
# Job Module

Manage jobs on Dell EMC PowerStore

### Synopsis
 Managing jobs on PowerStore Storage System includes getting details of job.

### Parameters
                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > job_id</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The ID of the job. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                            </table>

### Notes
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
- name: Get Job Details
  dellemc.powerstore.job:
    array_ip: "{{mgmt_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    job_id: "a544981c-e94a-40ab-9eae-e578e182d2bb"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=4>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=4 > job_details </td>
            <td>  complex </td>
            <td> When job exists. </td>
            <td> The job details. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > start_time </td>
                <td> str </td>
                <td>success</td>
                <td> Date and time when the job execution started. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > user </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the user associated with the job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > end_time </td>
                <td> str </td>
                <td>success</td>
                <td> Date and time when the job execution completed. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > step_order </td>
                <td> int </td>
                <td>success</td>
                <td> Order of a given job step with respect to its siblings within the job hierarchy. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > resource_action </td>
                <td> str </td>
                <td>success</td>
                <td> User-specified action to be performed on the given resource. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > response_status </td>
                <td> str </td>
                <td>success</td>
                <td> Possible HTTP status values of completed or failed jobs. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > description_l10n </td>
                <td> str </td>
                <td>success</td>
                <td> Description of the job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > root_id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the root job, if applicable. The root job is the job at the top of the parent hierarchy. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > estimated_completion_time </td>
                <td> str </td>
                <td>success</td>
                <td> Estimated completion date and time. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > resource_id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the resource on which the job is operating. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > resource_type </td>
                <td> str </td>
                <td>success</td>
                <td> Resource Type for the given resource. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > resource_name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the resource on which the job is operating. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > state </td>
                <td> str </td>
                <td>success</td>
                <td> Current status of the job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > progress_percentage </td>
                <td> int </td>
                <td>success</td>
                <td> Percent complete of the job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > response_body </td>
                <td> complex </td>
                <td>success</td>
                <td> Base response object. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > messages </td>
                    <td> complex </td>
                    <td>success</td>
                    <td> The details of the error response. </td>
                </tr>
                                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=1 > code </td>
                        <td> str </td>
                        <td>success</td>
                        <td> Hexadecimal code of the error. </td>
                    </tr>
                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=1 > message_l10n </td>
                        <td> str </td>
                        <td>success</td>
                        <td> The description of the error. </td>
                    </tr>
                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=1 > severity </td>
                        <td> str </td>
                        <td>success</td>
                        <td> Type of the severity. </td>
                    </tr>
                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=1 > arguments </td>
                        <td> list </td>
                        <td>success</td>
                        <td> Values involved in the error. </td>
                    </tr>
                                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > response_type </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Job error response. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > phase </td>
                <td> str </td>
                <td>success</td>
                <td> Current status of the job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > parent_id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the parent job, if applicable. </td>
            </tr>
                                        <tr>
            <td colspan=4 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Akash Shendge (@shenda1) <ansible.team@dell.com>

--------------------------------
# Remote Support Module

Remote Support operations on a PowerStore storage system

### Synopsis
 Performs all Remote Support operations on a PowerStore Storage System. This module supports getting details of an existing Remote Support configuration.
 This module also supports modifying an existing Remote Support configuration. Verify a remote support configuration. You can send a test alert through the remote support configuration.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=2>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=2 > remote_support_id</td>
            <td> int  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> Unique identifier of the remote support configuration. </td>
        </tr>
                    <tr>
            <td colspan=2 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=2 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=2 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> The state of the remote support configuration after the task is performed.  <br> For Delete operation only, it should be set to "absent".  <br> For get/modify operation it should be set to "present". </td>
        </tr>
                    <tr>
            <td colspan=2 > proxy_username</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> User name for proxy server access. </td>
        </tr>
                    <tr>
            <td colspan=2 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=2 > support_type</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>SRS_Gateway</li>  <li>SRS_Gateway_Tier2</li>  <li>SRS_Gateway_Tier3</li>  <li>SRS_Integrated_Tier2</li>  <li>SRS_Integrated_Tier3</li>  <li>Disabled</li> </ul></td>
            <td> <br> The type of remote support that is configured.  <br> Mandatory for modify and verify operation.  <br> SRS_Gateway support_type is only supported for verify operation. </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=2 > wait_for_completion</td>
            <td> bool  </td>
            <td></td>
            <td> False </td>
            <td></td>
            <td> <br> Flag to indicate if the operation should be run synchronously or asynchronously. True signifies synchronous execution. By default, modify operation will run asynchronously. </td>
        </tr>
                    <tr>
            <td colspan=2 > is_icw_configured</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Client already configured ICW. </td>
        </tr>
                    <tr>
            <td colspan=2 > is_support_assist_license_accepted</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Indicates whether user has accepted remote support license agreement before enabling the Support Assist on the system for the first time. </td>
        </tr>
                    <tr>
            <td colspan=2 > is_cloudiq_enabled</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Indicates whether support for CloudIQ is enabled. </td>
        </tr>
                    <tr>
            <td colspan=2 > verify_connection</td>
            <td> bool  </td>
            <td></td>
            <td> False </td>
            <td></td>
            <td> <br> Indicates whether to perform the verify call or not. </td>
        </tr>
                    <tr>
            <td colspan=2 > proxy_password</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Password for proxy server access. </td>
        </tr>
                    <tr>
            <td colspan=2 > is_rsc_enabled</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Indicates whether support for Remote Service Credentials is enabled. </td>
        </tr>
                    <tr>
            <td colspan=2 > server_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-server</li>  <li>absent-in-server</li> </ul></td>
            <td> <br> Indicates the state of the remote-support_servers.  <br> Required with remote_support_servers. </td>
        </tr>
                    <tr>
            <td colspan=2 > proxy_port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Proxy server port number. </td>
        </tr>
                    <tr>
            <td colspan=2 > remote_support_servers</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> One or two remote support servers. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > port </td>
                <td> int  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Gateway server port.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_primary </td>
                <td> bool  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Indicates whether the server is acting as the primary.  <br> One server must be set to false when two servers are configured.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > address </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td></td>
                <td>  <br> Gateway server IP address (IPv4).  <br> The address is a mandatory key.  </td>
            </tr>
                            <tr>
            <td colspan=2 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=2 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=2 > send_test_alert</td>
            <td> bool  </td>
            <td></td>
            <td> False </td>
            <td></td>
            <td> <br> Indicates whether to send a test alert or not. </td>
        </tr>
                    <tr>
            <td colspan=2 > return_support_license_text</td>
            <td> bool  </td>
            <td></td>
            <td> False </td>
            <td></td>
            <td> <br> Indicates whether to return support license agreement text or not. </td>
        </tr>
                    <tr>
            <td colspan=2 > proxy_address</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Proxy server IP address (IPv4). </td>
        </tr>
                            </table>

### Notes
* Creation and deletion of remote support configuration is not supported.
* Support for check_mode is not available for this module.
* Verify and send test alert operations do not support idempotency.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
  - name: Get details of remote support configuration
    dellemc.powerstore.remote_support:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       remote_support_id: 0
       state: "present"

  - name: Modify remote support configuration - SRS_Gateway_Tier2
    dellemc.powerstore.remote_support:
      array_ip: "{{array_ip}}"
      user: "{{user}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      remote_support_id: 0
      support_type: "SRS_Gateway_Tier2"
      remote_support_servers:
      - address: "10.XX.XX.XX"
        port: 9443
        is_primary: True
      - address: "10.XX.XX.YY"
        port: 9443
        is_primary: False
      server_state: "present-in-server"
      is_rsc_enabled: True
      is_cloudiq_enabled: False
      timeout: 300
      state: "present"

  - name: Modify remote support configuration - SRS_Integrated_Tier2
    dellemc.powerstore.remote_support:
      array_ip: "{{array_ip}}"
      user: "{{user}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      remote_support_id: 0
      support_type: "SRS_Integrated_Tier2"
      proxy_address: "10.XX.XX.ZZ"
      proxy_port: 3128
      proxy_username: "user"
      proxy_password: "password"
      timeout: 300
      state: "present"

  - name: Verify remote support configuration
    dellemc.powerstore.remote_support:
      array_ip: "{{array_ip}}"
      user: "{{user}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      remote_support_id: 0
      support_type: "SRS_Integrated_Tier3"
      timeout: 300
      verify_connection: True
      state: "present"

  - name: Send a test alert
    dellemc.powerstore.remote_support:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       remote_support_id: 0
       send_test_alert: True
       state: "present"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=3 > job_details </td>
            <td>  complex </td>
            <td> When asynchronous task is performed. </td>
            <td> The job details. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the job. </td>
            </tr>
                                        <tr>
            <td colspan=3 > remote_support_details </td>
            <td>  complex </td>
            <td> When remote support configuration exists. </td>
            <td> Details of the remote support configuration. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > is_rsc_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates whether support for Remote Service Credentials is enabled. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > proxy_address </td>
                <td> str </td>
                <td>success</td>
                <td> Proxy server IP address (IPv4). </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > proxy_password </td>
                <td> str </td>
                <td>success</td>
                <td> Password for proxy server access. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > type </td>
                <td> str </td>
                <td>success</td>
                <td> The type of remote support that is configured. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> int </td>
                <td>success</td>
                <td> Unique identifier of remote support configuration. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > support_assist_license_agreement_text </td>
                <td> str </td>
                <td>success</td>
                <td> The support assist license agreement text. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > proxy_username </td>
                <td> str </td>
                <td>success</td>
                <td> User name for proxy server access. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > proxy_port </td>
                <td> int </td>
                <td>success</td>
                <td> Proxy server port number. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > remote_support_servers </td>
                <td> complex </td>
                <td>success</td>
                <td> ['Details of two remote support servers.'] </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Unique identifier of the remote support server. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > port </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Gateway server port. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > is_primary </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether the server is acting as the primary. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > address </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Gateway server IP address (IPv4). </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > is_support_assist_license_accepted </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates whether user has accepted remote support license agreement before enabling the Support Assist on the system for the first time. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > is_cloudiq_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates whether support for CloudIQ is enabled. </td>
            </tr>
                                        <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>

--------------------------------
# Replication Session Module

Replication session operations on a PowerStore storage system

### Synopsis
 Performs all replication session state change operations on a PowerStore Storage System.
 This module supports get details of an existing replication session. Updating the state of the replication session.

### Parameters
                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > session_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>failed_over</li>  <li>paused</li>  <li>synchronizing</li> </ul></td>
            <td> <br> State in which the replication session is present after performing the task. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > session_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> ID of the replication session.  <br> Parameter volume_group, volume, and session_id are mutually exclusive. </td>
        </tr>
                    <tr>
            <td colspan=1 > volume</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name/ID of the volume for which replication session exists.  <br> Parameter volume_group, volume, and session_id are mutually exclusive. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > volume_group</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name/ID of the volume group for which a replication session exists.  <br> Parameter volume_group, volume, and session_id are mutually exclusive. </td>
        </tr>
                            </table>

### Notes
* Manual synchronization for a replication session is not supported through the Ansible module.
* When the current state of the replication session is 'OK' and in the playbook task 'synchronizing', then it will return "changed" as False.
* The changed as False in above scenario is because of there is a scheduled synchronization in place with the associated replication rule's RPO in the protection policy.
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
- name: Pause a replication session
  dellemc.powerstore.replicationsession:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    volume: "sample_volume_1"
    session_state: "paused"

- name: Synchronize a replication session
  dellemc.powerstore.replicationsession:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    volume: "sample_volume_1"
    session_state: "synchronizing"

- name: Get details of a replication session
  dellemc.powerstore.replicationsession:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    volume: "sample_volume_1"

- name: Fail over a replication session
  dellemc.powerstore.replicationsession:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    volume: "sample_volume_1"
    session_state: "failed_over"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > replication_session_details </td>
            <td>  complex </td>
            <td> When replication session exists </td>
            <td> Details of the replication session. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > resource_type </td>
                <td> str </td>
                <td>success</td>
                <td> Storage resource type eligible for replication protection. volume - Replication session created on a volume. volume_group - Replication session created on a volume group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > role </td>
                <td> str </td>
                <td>success</td>
                <td> Role of the replication session. Source - The local resource is the source of the remote replication session. Destination - The local resource is the destination of the remote replication session. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID of the replication session. Unique across source and destination roles. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > estimated_completion_timestamp </td>
                <td> str </td>
                <td>success</td>
                <td> Estimated completion time of the current replication operation. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > progress_percentage </td>
                <td> int </td>
                <td>success</td>
                <td> Progress of the current replication operation. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > local_resource_id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the local storage resource for the replication session. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > remote_system_id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the remote system instance. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > last_sync_timestamp </td>
                <td> str </td>
                <td>success</td>
                <td> Time of last successful synchronization. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > remote_resource_id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the remote storage resource for the replication session. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > state </td>
                <td> str </td>
                <td>success</td>
                <td> State of the replication session. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the replication rule. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > replication_rule_id </td>
                <td> str </td>
                <td>success</td>
                <td> Associated replication rule instance if created by policy engine. </td>
            </tr>
                                        <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

--------------------------------
# Remote System Module

Remote system operations on a PowerStore storage system

### Synopsis
 Performs all remote system operations on a PowerStore Storage System.
 This module supports get details of a remote systems, create/Add new remote system for all supported parameters, modify remote system with supported parameters and delete/remove a remote system.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > new_remote_address</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New management IP of the remote system. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > remote_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the remote system.  <br> Parameter remote_name cannot be mentioned during addition of a new remote system. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > wait_for_completion</td>
            <td> bool  </td>
            <td></td>
            <td> False </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Flag to indicate if the operation should be run synchronously or asynchronously.  <br> True signifies synchronous execution.  <br> By default, modify and delete operation will run asynchronously. </td>
        </tr>
                    <tr>
            <td colspan=1 > remote_password</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Password used in basic authentication to remote PowerStore cluster.  <br> It can be mentioned only during creation of the remote system. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > remote_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> ID of the remote system.  <br> ID for the remote system is autogenerated, cannot be passed during creation of a remote system.  <br> Parameter remote_id and remote_address are mutually exclusive. </td>
        </tr>
                    <tr>
            <td colspan=1 > network_latency</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>Low</li>  <li>High</li> </ul></td>
            <td> <br> Replication traffic can be tuned for higher efficiency depending on the expected network latency.  <br> Setting to low will have latency of less than five milliseconds.  <br> Setting to high will have latency of more than five milliseconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > remote_user</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Username used in basic authentication to remote PowerStore cluster.  <br> It can be mentioned only during creation of the remote system. </td>
        </tr>
                    <tr>
            <td colspan=1 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Additional information about the remote system.  <br> To remove the description empty string is to be passed. </td>
        </tr>
                    <tr>
            <td colspan=1 > remote_address</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Management IP of the remote system.  <br> Parameter remote_id and remote_address are mutually exclusive. </td>
        </tr>
                    <tr>
            <td colspan=1 > remote_port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Remote system's port number.  <br> It can be mentioned only during creation of the remote system. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> The state of the remote system after the task is performed.  <br> For Delete operation only, it should be set to "absent".  <br> For all Create, Modify or Get details operations it should be set to "present". </td>
        </tr>
                            </table>

### Notes
* The module support allows create/delete/update only for remote PowerStore arrays.
* Get details can be done for all type of remote arrays.
* Parameters remote_user, remote_port and remote_password are not required during modification, getting and deleting. If passed then these parameters will be ignored and the operation will be performed.
* If wait_for_completion is set to True then the connection will be terminated after the timeout is exceeded. User can tweak timeout and pass it in the playbook task.
* By default, the timeout is set to 120 seconds.
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
- name: Add a new remote system
  dellemc.powerstore.remotesystem:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    remote_address: "xxx.xxx.xxx.xxx"
    remote_user: "admin"
    remote_password: "{{remote_password}}"
    remote_port: 443
    network_latency: "Low"
    decription: "Adding a new remote system"
    state: "present"

- name: Modify attributes of remote system using remote_id
  dellemc.powerstore.remotesystem:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    remote_id: "7d7e7917-735b-3eef-8cc3-1302001c08e7"
    remote_address: "xxx.xxx.xxx.xxx"
    network_latency: "Low"
    wait_for_completion: True
    timeout: 300
    decription: "Updating the description"
    state: "present"

- name: Get details of remote system using remote_id
  dellemc.powerstore.remotesystem:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    remote_id: "D7d7e7917-735b-3eef-8cc3-1302001c08e7"
    state: "present"

- name: Delete remote system using remote_id
  dellemc.powerstore.remotesystem:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    remote_id: "D7d7e7917-735b-3eef-8cc3-1302001c08e7"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=3 > job_details </td>
            <td>  complex </td>
            <td> When wait_for_completion is not set to True. </td>
            <td> Details of the job. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The id of the job. </td>
            </tr>
                                        <tr>
            <td colspan=3 > remote_system_details </td>
            <td>  complex </td>
            <td> When remote system exists </td>
            <td> Details of the remote system. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > user_name </td>
                <td> str </td>
                <td>success</td>
                <td> Username used to access the non-PowerStore remote systems. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > session_chap_mode </td>
                <td> str </td>
                <td>success</td>
                <td> Challenge Handshake Authentication Protocol (CHAP) status. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > type </td>
                <td> str </td>
                <td>success</td>
                <td> Remote system connection type between the local system. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > data_connections </td>
                <td> complex </td>
                <td>success</td>
                <td> ['List of data connections from each appliance in the local cluster to iSCSI target IP address.'] </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > node_id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Unique identifier of the local, initiating node. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > target_address </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Target address from the remote system. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > initiator_address </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Initiating address from the local node. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > status </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Possible transit connection statuses. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > serial_number </td>
                <td> str </td>
                <td>success</td>
                <td> Serial number of the remote system instance. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > management_address </td>
                <td> str </td>
                <td>success</td>
                <td> The management cluster IP address of the remote system. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > discovery_chap_mode </td>
                <td> str </td>
                <td>success</td>
                <td> Challenge Handshake Authentication Protocol (CHAP) statu. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > version </td>
                <td> str </td>
                <td>success</td>
                <td> ['Version of the remote system.', 'It was added in PowerStore version 2.0.0.0.'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID of the remote system. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > data_network_latency </td>
                <td> str </td>
                <td>success</td>
                <td> ['Network latency choices for a remote system. Replication traffic can be tuned for higher efficiency depending on the expected network latency.', 'This will only be used when the remote system type is PowerStore.'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > state </td>
                <td> str </td>
                <td>success</td>
                <td> ['Possible remote system states.', 'OK, Normal conditions.', 'Update_Needed, Verify and update needed to handle network configuration changes on the systems.', 'Management_Connection_Lost, Management connection to the remote peer is lost.'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > description </td>
                <td> str </td>
                <td>success</td>
                <td> User-specified description of the remote system instance. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the remote system. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > data_connection_state </td>
                <td> str </td>
                <td>success</td>
                <td> Data connection states of a remote system. </td>
            </tr>
                                        <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

--------------------------------
# File System Module

Filesystem operations on PowerStore Storage system

### Synopsis
 Supports the provisioning operations on a filesystem such as create, modify, delete and get the details of a filesystem.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=2>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=2 > filesystem_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Unique id of the file system. Mutually exclusive with filesystem_name. </td>
        </tr>
                    <tr>
            <td colspan=2 > smb_properties</td>
            <td> dict  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Advance settings for SMB. It contains below optional candidate variables. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_smb_no_notify_enabled </td>
                <td> bool  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Indicates whether notifications of changes to directory file structure are enabled.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_smb_notify_on_access_enabled </td>
                <td> bool  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Indicates whether file access notifications are enabled on the file system.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_smb_notify_on_write_enabled </td>
                <td> bool  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Indicates whether file write notifications are enabled on the file system.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_smb_sync_writes_enabled </td>
                <td> bool  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Indicates whether the synchronous writes option is enabled on the file system.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_smb_op_locks_enabled </td>
                <td> bool  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Indicates whether opportunistic file locking is enabled on the file system.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > smb_notify_on_change_dir_depth </td>
                <td> int  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Integer variable , determines the lowest directory level to which the enabled notifications apply. minimum value is 1.  </td>
            </tr>
                            <tr>
            <td colspan=2 > cap_unit</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>GB</li>  <li>TB</li> </ul></td>
            <td> <br> Capacity unit for the size.  <br> It defaults to 'GB', if not specified. </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=2 > folder_rename_policy</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>ALL_ALLOWED</li>  <li>SMB_FORBIDDEN</li>  <li>ALL_FORBIDDEN</li> </ul></td>
            <td> <br> File system folder rename policies for the file system with multi-protocol access enabled.  <br> ALL_ALLOWED - All protocols are allowed to rename directories without any restrictions.  <br> SMB_FORBIDDEN - A directory rename from the SMB protocol will be denied if at least one file is opened in the directory or in one of its child directories.  <br> All_FORBIDDEN - Any directory rename request will be denied regardless of the protocol used, if at least one file is opened in the directory or in one of its child directories. </td>
        </tr>
                    <tr>
            <td colspan=2 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=2 > size</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Size that the file system presents to the host or end user. Mandatory only for create operation. </td>
        </tr>
                    <tr>
            <td colspan=2 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=2 > quota_defaults</td>
            <td> dict  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Contains the default attributes for a filesystem quota.It contains below optional candidate variables. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > default_soft_limit </td>
                <td> int  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Default soft limit of user quotas and tree quotas.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > default_hard_limit </td>
                <td> int  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Default hard limit of user quotas and tree quotas.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > grace_period </td>
                <td> int  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Grace period of soft limit.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > cap_unit </td>
                <td> str  </td>
                <td> False </td>
                <td></td>
                <td> <ul> <li>GB</li>  <li>TB</li> </ul></td>
                <td>  <br> Capacity unit for default hard & soft limit.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > grace_period_unit </td>
                <td> str  </td>
                <td> False </td>
                <td></td>
                <td> <ul> <li>days</li>  <li>weeks</li>  <li>months</li> </ul></td>
                <td>  <br> Unit of the grace period of soft limit.  </td>
            </tr>
                            <tr>
            <td colspan=2 > filesystem_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the file system. Mutually exclusive with filesystem_id. Mandatory only for create operation. </td>
        </tr>
                    <tr>
            <td colspan=2 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Description of the file system. </td>
        </tr>
                    <tr>
            <td colspan=2 > protection_policy</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name or ID of the protection policy applied to the file system.  <br> Specifying "" (empty string) removes the existing protection policy from file system. </td>
        </tr>
                    <tr>
            <td colspan=2 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=2 > nas_server</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name or ID of the NAS Server on which the file system is created. Mandatory parameter whenever filesystem_name is provided, since filesystem names are unique only within a NAS server. </td>
        </tr>
                    <tr>
            <td colspan=2 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the filesystem should exist or not. </td>
        </tr>
                    <tr>
            <td colspan=2 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=2 > locking_policy</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>ADVISORY</li>  <li>MANDATORY</li> </ul></td>
            <td> <br> File system locking policies. ADVISORY- No lock checking for NFS and honor SMB lock range only for SMB. MANDATORY- Honor SMB and NFS lock range. </td>
        </tr>
                    <tr>
            <td colspan=2 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=2 > access_policy</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>NATIVE</li>  <li>UNIX</li>  <li>WINDOWS</li> </ul></td>
            <td> <br> File system security access policies. </td>
        </tr>
                            </table>

### Notes
* It is recommended to remove the protection policy before deleting the filesystem.
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
 - name: Create FileSystem by Name
   register: result_fs
   dellemc.powerstore.filesystem:
     array_ip: "{{array_ip}}"
     verifycert: "{{verifycert}}"
     user: "{{user}}"
     password: "{{password}}"
     filesystem_name: "{{filesystem_name}}"
     description: "{{description}}"
     nas_server: "{{nas_server_id}}"
     size: "5"
     cap_unit: "GB"
     access_policy: "UNIX"
     locking_policy: "MANDATORY"
     smb_properties:
       is_smb_no_notify_enabled: True
       is_smb_notify_on_access_enabled: True
     quota_defaults:
       grace_period: 1
       grace_period_unit: 'days'
       default_hard_limit: 3
       default_soft_limit: 2
     protection_policy: "{{protection_policy_id}}"
     state: "present"

 - name: Modify File System by id
   dellemc.powerstore.filesystem:
     array_ip: "{{array_ip}}"
     verifycert: "{{verifycert}}"
     user: "{{user}}"
     password: "{{password}}"
     filesystem_id: "{{fs_id}}"
     folder_rename_policy: "ALL_ALLOWED"
     smb_properties:
       is_smb_op_locks_enabled: True
       smb_notify_on_change_dir_depth: 3
     quota_defaults:
       grace_period: 2
       grace_period_unit: 'weeks'
       default_hard_limit: 2
       default_soft_limit: 1
     state: "present"

 - name: Get File System details by id
   dellemc.powerstore.filesystem:
     array_ip: "{{array_ip}}"
     verifycert: "{{verifycert}}"
     user: "{{user}}"
     password: "{{password}}"
     filesystem_id: "{{result_fs.filesystem_details.id}}"
     state: "present"

 - name: Delete File System by id
   dellemc.powerstore.filesystem:
     array_ip: "{{array_ip}}"
     verifycert: "{{verifycert}}"
     user: "{{user}}"
     password: "{{password}}"
     filesystem_id: "{{result_fs.filesystem_details.id}}"
     state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > filesystem_details </td>
            <td>  complex </td>
            <td> When filesystem exists </td>
            <td> Details of the filesystem. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > default_soft_limit </td>
                <td> int </td>
                <td>success</td>
                <td> Default soft limit period for a filesystem quota in byte. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_smb_op_locks_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether smb op lock is enabled. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > total_size_with_unit </td>
                <td> str </td>
                <td>success</td>
                <td> Total size of the filesystem with appropriate unit. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > used_size_with_unit </td>
                <td> str </td>
                <td>success</td>
                <td> Used size of the filesystem with appropriate unit. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > size_used </td>
                <td> int </td>
                <td>success</td>
                <td> Used size of the filesystem in bytes. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > snapshots </td>
                <td> list </td>
                <td>success</td>
                <td> Id and name of the snapshots of a filesystem. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID given to the filesystem. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_smb_no_notify_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether smb notify policy is enabled for a filesystem. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > size_total </td>
                <td> int </td>
                <td>success</td>
                <td> Total size of the filesystem in bytes. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_smb_notify_on_access_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether smb on access notify policy is enabled. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > description </td>
                <td> str </td>
                <td>success</td>
                <td> The description about the filesystem. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > nas_server </td>
                <td> dict </td>
                <td>success</td>
                <td> Id and name of the nas server to which the filesystem belongs. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > default_hard_limit </td>
                <td> int </td>
                <td>success</td>
                <td> Default hard limit period for a filesystem quota in byte. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > grace_period </td>
                <td> int </td>
                <td>success</td>
                <td> Default grace period for a filesystem quota in second. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the filesystem. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > locking_policy </td>
                <td> str </td>
                <td>success</td>
                <td> Locking policy about the filesystem. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > protection_policy </td>
                <td> dict </td>
                <td>success</td>
                <td> Id and name of the protection policy associated with the filesystem. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > access_policy </td>
                <td> str </td>
                <td>success</td>
                <td> Access policy about the filesystem. </td>
            </tr>
                                        <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Arindam Datta (@dattaarindam) <ansible.team@dell.com>

--------------------------------
# Certificate Module

Certificate operations on PowerStore Storage System

### Synopsis
 Supports the provisioning operations on a Certificate such as add/import, modify, reset, exchange and get the details of a certificate.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > remote_password</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The password of the remote cluster. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > certificate_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Unique identifier of the certificate.  <br> Mandatory only for modify operation. </td>
        </tr>
                    <tr>
            <td colspan=1 > certificate</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Concatenated PEM encoded x509_certificate string from end-entity certificate to root certificate. </td>
        </tr>
                    <tr>
            <td colspan=1 > scope</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Defines a subset of certificates belonging to one Service. </td>
        </tr>
                    <tr>
            <td colspan=1 > is_current</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Indicates whether this is the current X509 certificate to be used by the service or this X509 Certificate will be used in the future. </td>
        </tr>
                    <tr>
            <td colspan=1 > certificate_type</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>Server</li>  <li>Client</li>  <li>CA_Client_Validation</li>  <li>CA_Server_Validation</li> </ul></td>
            <td> <br> Type of the certificate. </td>
        </tr>
                    <tr>
            <td colspan=1 > remote_user</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The username of the remote cluster. </td>
        </tr>
                    <tr>
            <td colspan=1 > remote_address</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> IPv4 or DNS name of the remote cluster. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the certificate should exist or not. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > remote_port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The port address of the remote cluster. </td>
        </tr>
                    <tr>
            <td colspan=1 > service</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>Management_HTTP</li>  <li>Replication_HTTP</li>  <li>VASA_HTTP</li>  <li>Import_HTTP</li>  <li>LDAP_HTTP</li>  <li>Syslog_HTTP</li> </ul></td>
            <td> <br> Type of the service for which the certificate is used.  <br> Mandatory for reset and exchange operation. </td>
        </tr>
                            </table>

### Notes
* Idempotency is not supported for adding/importing certificates, exchange of certificates and the reset of certificates.
* Only is_current parameter is supported for modification of certificate.
* Reset operation can reset more than one certificate at a time.
* Add/import, modify and reset are supported for PowerStore versions 2.0 and above only.
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
- name: Get details of certificate with certificate_id
  dellemc.powerstore.certificate:
    array_ip: "{{array_ip}}"
    user: "{{user}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    certificate_id: "e940144f-393f-4e9c-8f54-9a4d57b38c48"
    state: "present"

- name: Reset certificates
  dellemc.powerstore.certificate:
    array_ip: "{{array_ip}}"
    user: "{{user}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    service: "VASA_HTTP"
    state: "present"

- name: Exchange certificates
  dellemc.powerstore.certificate:
    array_ip: "{{array_ip}}"
    user: "{{user}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    service: "Replication_HTTP"
    remote_address: "{{remote_array_ip}}"
    remote_port: 443
    remote_user: "{{remote_user}}"
    remote_password: "{{remote_password}}"
    state: "present"

- name: Add/import a certificate
  dellemc.powerstore.certificate:
    array_ip: "{{array_ip}}"
    user: "{{user}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    certificate_type: "CA_Client_Validation"
    service: "VASA_HTTP"
    certificate: "{{certificate_string}}"
    is_current: True
    state: "present"

- name: Modify certificate
  dellemc.powerstore.certificate:
    array_ip: "{{array_ip}}"
    user: "{{user}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    certificate_id: "37b76535-612b-456a-a694-1389f17632c7"
    is_current: True
    state: "present"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=3 > certificate_details </td>
            <td>  complex </td>
            <td> When certificate exists </td>
            <td> Details of the certificate. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > is_current </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether the certificate can be used now or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > type_l10n </td>
                <td> str </td>
                <td>success</td>
                <td> Localized message string corresponding to type. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID given to the certificate. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > type </td>
                <td> str </td>
                <td>success</td>
                <td> Type of the certificate. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > service_l10n </td>
                <td> str </td>
                <td>success</td>
                <td> Localized message string corresponding to service. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > is_valid </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates whether this is a valid X509 certificate. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > members </td>
                <td> complex </td>
                <td>success</td>
                <td> Member certificates included in this x509_certificate. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > key_length </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Private key length. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > thumbprint </td>
                    <td> str </td>
                    <td>success</td>
                    <td> CeHash value of the certificate. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > subject </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Certificate subject or so called distinguished name. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > public_key_algorithm </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Public key algorithm used to generate the key pair. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > signature_algorithm </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Certificate signature algorithm. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > depth </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Depth indicates the position of this member certificate in the X509 Certificate chain. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > thumbprint_algorithm_l10n </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Localized message string corresponding to thumbprint_algorithm. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > subject_alternative_names </td>
                    <td> list </td>
                    <td>success</td>
                    <td> Additional DNS names or IP addresses in the x509_certificate. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > serial_number </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Certificate serial number. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > valid_from </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Date and time when the certificate becomes valid. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > certificate </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Base64 encoded certificate without any line breaks. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > thumbprint_algorithm </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The thumbprint algorithm. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > valid_to </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Date and time when the certificate will expire. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > issuer </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Distinguished name of the certificate issuer. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > service </td>
                <td> str </td>
                <td>success</td>
                <td> Type of the service for which the certificate is used. </td>
            </tr>
                                        <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>

--------------------------------
# Email Module

Destination Email operations on a PowerStore storage system

### Synopsis
 Performs all destination email operations on a PowerStore Storage System.
 This module supports get details of an existing destination email address. Create/Add new destination email address for all supported parameters.
 This Module supports modify destination email address with supported parameters.
 This Module supports delete/remove a specific destination email address. Send a test mail to a specific destination email address.

### Parameters
                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=2>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=2 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=2 > email_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Unique identifier of the destination email address.  <br> Mutually exclusive with email_address. </td>
        </tr>
                    <tr>
            <td colspan=2 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=2 > new_address</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New email address to receive notifications. </td>
        </tr>
                    <tr>
            <td colspan=2 > send_test_email</td>
            <td> bool  </td>
            <td></td>
            <td> False </td>
            <td></td>
            <td> <br> Whether to send the test email to the destination email address. </td>
        </tr>
                    <tr>
            <td colspan=2 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=2 > notify</td>
            <td> dict  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Whether to send different types of notifications. It contains below optional candidate variables. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > critical </td>
                <td> bool  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Whether to send notifications for critical alerts.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > info </td>
                <td> bool  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Whether to send notifications for informational alerts.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > minor </td>
                <td> bool  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Whether to send notifications for minor alerts.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > major </td>
                <td> bool  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Whether to send notifications for major alerts.  </td>
            </tr>
                            <tr>
            <td colspan=2 > email_address</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Email address to receive notifications.  <br> Mutually exclusive with email_id. </td>
        </tr>
                    <tr>
            <td colspan=2 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> The state of the destination email address after the task is performed.  <br> For Delete operation only, it should be set to "absent".  <br> For all Create, Modify, Test or Get details operations it should be set to "present". </td>
        </tr>
                    <tr>
            <td colspan=2 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=2 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                            </table>

### Notes
* Idempotency is not supported for Test operation of Email module.
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
  - name: Get details of destination email with email_id
    dellemc.powerstore.email:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       email_id: "780b6220-2d0b-4b9f-a485-4ae7f673bd98"
       state: "present"

  - name: Get details of destination email with email_address
    dellemc.powerstore.email:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       email_address: "abc@dell.com"
       state: "present"

  - name: Create destination email
    dellemc.powerstore.email:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       email_address: "abc_xyz@dell.com"
       notify:
         info: True
         critical: True
         major: False
       state: "present"

  - name: Modify destination email
    dellemc.powerstore.email:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       email_address: "abc_xyz@dell.com"
       new_address: "def_pqr@dell.com"
       notify:
         info: False
         major: False
       state: "present"

  - name: Send a test mail to the destination email with email_id
    dellemc.powerstore.email:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       email_id: "780b6220-2d0b-4b9f-a485-4ae7f673bd98"
       send_test_email: True
       state: "present"

  - name: Delete destination email
    dellemc.powerstore.email:
       array_ip: "{{array_ip}}"
       user: "{{user}}"
       password: "{{password}}"
       verifycert: "{{verifycert}}"
       email_address: "def_pqr@dell.com"
       state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=3 > email_details </td>
            <td>  complex </td>
            <td> When destination email address exists </td>
            <td> Details of the destination email address. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID of the destination email instance. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > notify </td>
                <td> complex </td>
                <td>success</td>
                <td> ['Whether to send different types of notifications.'] </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > critical </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Whether to send notifications for critical alerts. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > info </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Whether to send notifications for informational alerts. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > minor </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Whether to send notifications for minor alerts. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > major </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Whether to send notifications for major alerts. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > email_address </td>
                <td> str </td>
                <td>success</td>
                <td> Email address to receive notifications. </td>
            </tr>
                                        <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>

--------------------------------
# Protection Policy Module

Perform Protection policy operations on PowerStore storage system

### Synopsis
 Performs all protection policy operations on PowerStore Storage System. This module supports create, modify, get and delete a protection policy.

### Parameters
                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshotrules</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> List of strings to specify the name or ids of snapshot rules which are to be added or removed, to or from, the protection policy. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > protectionpolicy_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> String variable. Indicates the id of the protection policy. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> String variable. Indicates the new name of the protection policy.  <br> Used for renaming operation. </td>
        </tr>
                    <tr>
            <td colspan=1 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> String variable. Indicates the description of the protection policy. </td>
        </tr>
                    <tr>
            <td colspan=1 > replicationrule</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name or ids of the replcation rule which is to be added to the protection policy.  <br> To remove the replication rule, an empty string has to be passed. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> String variable. Indicates the state of protection policy.  <br> For Delete operation only, it should be set to "absent".  <br> For all other operations like Create, Modify or Get details, it should be set to "present". </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> String variable. Indicates the name of the protection policy. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshotrule_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-policy</li>  <li>absent-in-policy</li> </ul></td>
            <td> <br> String variable. Indicates the state of a snapshotrule in a protection policy.  <br> When snapshot rules are specified, this variable is required.  <br> Value present-in-policy indicates to add to protection policy.  <br> Value absent-in-policy indicates to remove from protection policy. </td>
        </tr>
                            </table>

### Notes
* Before deleting a protection policy, the replication rule has to be removed from the protection policy.
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
- name: Create a protection policy with snapshot rule and replication rule
  dellemc.powerstore.protectionpolicy:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    description: "{{description}}"
    snapshotrules:
      - "Ansible_test_snap_rule_1"
    replicationrule: "ansible_replication_rule_1"
    snapshotrule_state: "present-in-policy"
    state: "present"


- name : Modify protection policy, change name
  dellemc.powerstore.protectionpolicy:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    new_name: "{{new_name}}"
    state: "present"


- name : Modify protection policy, add snapshot rule
  dellemc.powerstore.protectionpolicy:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    snapshotrules:
      - "Ansible_test_snaprule_1"
    snapshotrule_state: "present-in-policy"
    state: "present"

- name : Modify protection policy, remove snapshot rule, replication rule
  dellemc.powerstore.protectionpolicy:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    snapshotrules:
      - "Ansible_test_to_be_removed"
    replicationrule: ""
    snapshotrule_state: "absent-in-policy"
    state: "present"

- name : Get details of protection policy by name
  dellemc.powerstore.protectionpolicy:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    state: "present"

- name : Get details of protection policy by ID
  dellemc.powerstore.protectionpolicy:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    protectionpolicy_id: "{{protectionpolicy_id}}"
    state: "present"

- name : Delete protection policy
  dellemc.powerstore.protectionpolicy:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=4>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=4 > protectionpolicy_details </td>
            <td>  complex </td>
            <td> When protection policy exists </td>
            <td> Details of the protection policy. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > description </td>
                <td> str </td>
                <td>success</td>
                <td> description about the protection policy. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > snapshot_rules </td>
                <td> complex </td>
                <td>success</td>
                <td> The snapshot rules details of the protection policy. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The snapshot rule ID of the protection policy. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The snapshot rule name of the protection policy. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID given to the protection policy. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > type </td>
                <td> str </td>
                <td>success</td>
                <td> The type for the protection policy. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the protection policy. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > replication_rules </td>
                <td> complex </td>
                <td>success</td>
                <td> The replication rule details of the protection policy. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The replication rule ID of the protection policy. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The replication rule name of the protection policy. </td>
                </tr>
                                                                    <tr>
            <td colspan=4 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Arindam Datta (@dattaarindam) <ansible.team@dell.com>
* P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

--------------------------------
# Snapshot Module

Manage Snapshots on Dell EMC PowerStore

### Synopsis
 Managing Snapshots on PowerStore storage system, Create a new Volume Group Snapshot, Get details of Volume Group Snapshot, Modify Volume Group Snapshot, Delete an existing Volume Group Snapshot.
 Module also supports Create a new Volume Snapshot, Get details of Volume Snapshot, Modify Volume Snapshot, Delete an existing Volume Snapshot.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshot_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the Snapshot. Either snapshot name or ID is required. </td>
        </tr>
                    <tr>
            <td colspan=1 > desired_retention</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The retention value for the Snapshot.  <br> If the retention value is not specified, the Snapshot details would be returned.  <br> To create a Snapshot, either a retention or expiration timestamp must be given.  <br> If the Snapshot does not have any retention value - specify it as 'None'. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=1 > retention_unit</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>hours</li>  <li>days</li> </ul></td>
            <td> <br> The unit for retention.  <br> If this unit is not specified, 'hours' is taken as default retention_unit.  <br> If desired_retention is specified, expiration_timestamp cannot be specified. </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshot_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the Snapshot. Either snapshot ID or Snapshot name is required. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_snapshot_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The new name of the Snapshot. </td>
        </tr>
                    <tr>
            <td colspan=1 > expiration_timestamp</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The expiration timestamp of the Snapshot. This should be provided in UTC format, e.g 2019-07-24T10:54:54Z. </td>
        </tr>
                    <tr>
            <td colspan=1 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The description for the Snapshot. </td>
        </tr>
                    <tr>
            <td colspan=1 > volume</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The volume. This could be the volume name or ID. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Defines whether the Snapshot should exist or not. </td>
        </tr>
                    <tr>
            <td colspan=1 > volume_group</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The volume group. This could be the volume group name or ID. </td>
        </tr>
                            </table>

### Notes
* The check_mode is not supported.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
    - name: Create a volume snapshot on PowerStore
      dellemc.powerstore.snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        volume: "{{volume}}"
        description: "{{description}}"
        desired_retention: "{{desired_retention}}"
        retention_unit: "{{retention_unit_days}}"
        state: "{{state_present}}"

    - name: Get details of a volume snapshot
      dellemc.powerstore.snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        volume: "{{volume}}"
        state: "{{state_present}}"

    - name: Rename volume snapshot
      dellemc.powerstore.snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        new_snapshot_name: "{{new_snapshot_name}}"
        volume: "{{volume}}"
        state: "{{state_present}}"

    - name: Delete volume snapshot
      dellemc.powerstore.snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{new_snapshot_name}}"
        volume: "{{volume}}"
        state: "{{state_absent}}"

    - name: Create a volume group snapshot on PowerStore
      dellemc.powerstore.snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        volume_group: "{{volume_group}}"
        description: "{{description}}"
        expiration_timestamp: "{{expiration_timestamp}}"
        state: "{{state_present}}"

    - name: Get details of a volume group snapshot
      dellemc.powerstore.snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        volume_group: "{{volume_group}}"
        state: "{{state_present}}"

    - name: Modify volume group snapshot expiration timestamp
      dellemc.powerstore.snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        volume_group: "{{volume_group}}"
        description: "{{description}}"
        expiration_timestamp: "{{expiration_timestamp_new}}"
        state: "{{state_present}}"

    - name: Rename volume group snapshot
      dellemc.powerstore.snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        new_snapshot_name: "{{new_snapshot_name}}"
        volume_group: "{{volume_group}}"
        state: "{{state_present}}"

    - name: Delete volume group snapshot
      dellemc.powerstore.snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{new_snapshot_name}}"
        volume_group: "{{volume_group}}"
        state: "{{state_absent}}"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=3 > create_fs_snap </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has created. </td>
        </tr>
                    <tr>
            <td colspan=3 > filesystem_snap_details </td>
            <td>  dict </td>
            <td> When snapshot exists. </td>
            <td> Details of the snapshot. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > access_type </td>
                <td> str </td>
                <td>success</td>
                <td> Displays the type of access allowed to the snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > parent_name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the filesystem on which snapshot is taken. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > expiration_timestamp </td>
                <td> str </td>
                <td>success</td>
                <td> The date and time the snapshot is due to be automatically deleted by the system. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the filesystem snapshot instance. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > nas_server </td>
                <td> dict </td>
                <td>success</td>
                <td> Details of NAS server on which snapshot is present. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> ID of the NAS server. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Name of the NAS server </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Description of the filesystem snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > creation_timestamp </td>
                <td> str </td>
                <td>success</td>
                <td> The date and time the snapshot was created. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > parent_id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the filesystem on which snapshot is taken. </td>
            </tr>
                                        <tr>
            <td colspan=3 > delete_fs_snap </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has deleted. </td>
        </tr>
                    <tr>
            <td colspan=3 > modify_fs_snap </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has modified. </td>
        </tr>
                    <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Rajshree Khare (@khareRajshree) <ansible.team@dell.com>
* Prashant Rakheja (@prashant-dell) <ansible.team@dell.com>

--------------------------------
# Info Module

Gathers information about PowerStore Storage entities

### Synopsis
 Gathers the list of specified PowerStore Storage System entities, includes block/file provisioning modules, replication modules and configuration modules.
 Block provisioning module includes volumes, volume groups, hosts, host groups, snapshot rules, protection policies.
 File provisioning module includes NAS servers, NFS exports, SMB shares, tree quotas, user quotas, file systems.
 Replication module includes replication rules, replication sessions, remote system.
 Configuration module includes cluster nodes, network, roles, local users, appliances, security configs, certificates, AD/LDAP servers.
 It also includes DNS/NTP servers, smtp configs, email destinations, remote support, remote support contacts.

### Parameters
                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=2>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=2 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=2 > gather_subset</td>
            <td> list   <br> elements: str </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>vol</li>  <li>vg</li>  <li>host</li>  <li>hg</li>  <li>node</li>  <li>protection_policy</li>  <li>snapshot_rule</li>  <li>nas_server</li>  <li>nfs_export</li>  <li>smb_share</li>  <li>tree_quota</li>  <li>user_quota</li>  <li>file_system</li>  <li>replication_rule</li>  <li>replication_session</li>  <li>remote_system</li>  <li>network</li>  <li>role</li>  <li>user</li>  <li>appliance</li>  <li>ad</li>  <li>ldap</li>  <li>security_config</li>  <li>certificate</li>  <li>dns</li>  <li>ntp</li>  <li>smtp_config</li>  <li>email_notification</li>  <li>remote_support</li>  <li>remote_support_contact</li> </ul></td>
            <td> <br> A list of string variables which specify the PowerStore system entities requiring information.  <br> Volumes - vol.  <br> All the nodes - node.  <br> Volume groups - vg.  <br> Protection policies - protection_policy.  <br> Hosts - host.  <br> Host groups - hg.  <br> Snapshot rules - snapshot_rule.  <br> NAS servers - nas_server.  <br> NFS exports - nfs_export.  <br> SMB shares - smb_share.  <br> Tree quotas - tree_quota.  <br> User quotas - user_quota.  <br> File systems - file_system.  <br> Replication rules - replication_rule.  <br> Replication sessions - replication_session.  <br> Remote systems - remote_system.  <br> Various networks - network.  <br> Roles - role.  <br> Local users - user.  <br> Appliances - appliance.  <br> Security configurations - security_config.  <br> Certificates - certificate.  <br> Active directories - ad.  <br> LDAPs - ldap.  <br> DNS servers - dns.  <br> NTP servers - ntp.  <br> Email notification destinations - email_notification.  <br> SMTP configurations - smtp_config.  <br> Remote Support - remote_support.  <br> Remote support contacts - remote_support_contact. </td>
        </tr>
                    <tr>
            <td colspan=2 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which the connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=2 > filters</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> A list of filters to support filtered output for storage entities.  <br> Each filter is a list of filter_key, filter_operator, filter_value.  <br> Supports passing of multiple filters. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > filter_operator </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td> <ul> <li>equal</li>  <li>greater</li>  <li>lesser</li>  <li>like</li>  <li>notequal</li> </ul></td>
                <td>  <br> Operation to be performed on the filter key.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > filter_key </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td></td>
                <td>  <br> Name identifier of the filter.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > filter_value </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td></td>
                <td>  <br> Value of the filter key.  </td>
            </tr>
                            <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=2 > all_pages</td>
            <td> bool  </td>
            <td></td>
            <td> False </td>
            <td></td>
            <td> <br> Indicates whether to return all available entities on the storage system.  <br> If set to True, the Info module will implement pagination and return all entities. Otherwise, a maximum of the first 100 entities of any type will be returned. </td>
        </tr>
                    <tr>
            <td colspan=2 > port</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Port number for the PowerStore array.  <br> If not passed, it will take 443 as default. </td>
        </tr>
                    <tr>
            <td colspan=2 > array_ip</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerStore management system. </td>
        </tr>
                    <tr>
            <td colspan=2 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                            </table>

### Notes
* Pagination is not supported for role, local user and security configs. If all_pages is passed, it will be ignored.
* Check mode is not currently supported for info Ansible module.
* The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell EMC PowerStore storage platform.

### Examples
```
- name: Get list of volumes, volume groups, hosts, host groups and node
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - vol
      - vg
      - host
      - hg
      - node

- name: Get list of replication related entities
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - replication_rule
      - replication_session
      - remote_system

- name: Get list of volumes whose state notequal to ready
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - vol
    filters:
      - filter_key: "state"
        filter_operator: "notequal"
        filter_value: "ready"

- name: Get list of protection policies and snapshot rules
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - protection_policy
      - snapshot_rule

- name: Get list of snapshot rules whose desired_retention between 101-499
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - snapshot_rule
    filters:
      - filter_key: "desired_retention"
        filter_operator: "greater"
        filter_value: "100"
      - filter_key: "desired_retention"
        filter_operator: "lesser"
        filter_value: "500"

- name: Get list of nas server, nfs_export and smb share
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - nas_server
      - nfs_export
      - smb_share

- name: Get list of tree quota, user quota and file system
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - tree_quota
      - user_quota
      - file_system

- name: Get list of nas server whose name equal to 'nas_server'
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - nas_server
    filters:
      - filter_key: "name"
        filter_operator: "equal"
        filter_value: "nas_server"

- name: Get list of smb share whose name contains 'share'
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - nas_server
    filters:
      - filter_key: "name"
        filter_operator: "like"
        filter_value: "*share*"

- name: Get list of user, role, network and appliances
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - user
      - role
      - network
      - appliance

- name: Get list of ad, certificate, security config and ldaps
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - ad
      - ldap
      - certificate
      - security_config

- name: Get list of networks whose name contains 'Management'
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - network
    filters:
      - filter_key: "name"
        filter_operator: "like"
        filter_value: "*Management*"

- name: Get list of dns, email notification, ntp, remote support, remote support contact and smtp config
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - dns
      - email_notification
      - ntp
      - remote_support
      - remote_support_contact
      - smtp_config

- name: Get list of emails which receives minor notifications
  dellemc.powerstore.info:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
    - email_notification
    filters:
        - filter_key: 'notify_minor'
          filter_operator: 'equal'
          filter_value: 'False'
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > VolumeGroups </td>
            <td>  list </td>
            <td> When vg is in a given gather_subset </td>
            <td> Provides details of all volume groups. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the volume group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the volume group. </td>
            </tr>
                                        <tr>
            <td colspan=2 > RemoteSupport </td>
            <td>  list </td>
            <td> When remote_support is in a given gather_subset </td>
            <td> Provides details of all remote support config. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the remote support. </td>
            </tr>
                                        <tr>
            <td colspan=2 > UserQuotas </td>
            <td>  list </td>
            <td> When user_quota is in a given gather_subset </td>
            <td> Provides details of all user quotas. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the user quota. </td>
            </tr>
                                        <tr>
            <td colspan=2 > SMBShares </td>
            <td>  list </td>
            <td> When smb_share is in a given gather_subset </td>
            <td> Provides details of all smb shares. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the smb share. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> name of the smb share. </td>
            </tr>
                                        <tr>
            <td colspan=2 > SecurityConfig </td>
            <td>  list </td>
            <td> When security_config is in a given gather_subset </td>
            <td> Provides details of all security configs. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the security config. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Volumes </td>
            <td>  list </td>
            <td> When vol is in a given gather_subset </td>
            <td> Provides details of all volumes. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the volume. </td>
            </tr>
                                        <tr>
            <td colspan=2 > FileSystems </td>
            <td>  list </td>
            <td> When file_system is in a given gather_subset </td>
            <td> Provides details of all filesystems. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the filesystem. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the filesystem. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Nodes </td>
            <td>  list </td>
            <td> When a node is in a given gather_subset </td>
            <td> Provides details of all nodes. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the node. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the node. </td>
            </tr>
                                        <tr>
            <td colspan=2 > RemoteSystems </td>
            <td>  list </td>
            <td> When remote_system is in a given gather_subset </td>
            <td> Provides details of all remote systems. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the remote system. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the remote system. </td>
            </tr>
                                        <tr>
            <td colspan=2 > HostGroups </td>
            <td>  list </td>
            <td> When hg is in a given gather_subset </td>
            <td> Provides details of all host groups. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the host group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the host group. </td>
            </tr>
                                        <tr>
            <td colspan=2 > NASServers </td>
            <td>  list </td>
            <td> When nas_server is in a given gather_subset </td>
            <td> Provides details of all nas servers. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the nas server. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the nas server. </td>
            </tr>
                                        <tr>
            <td colspan=2 > NTP </td>
            <td>  list </td>
            <td> When ntp is in a given gather_subset </td>
            <td> Provides details of all NTP servers. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the NTP server. </td>
            </tr>
                                        <tr>
            <td colspan=2 > DNS </td>
            <td>  list </td>
            <td> When dns is in a given gather_subset </td>
            <td> Provides details of all DNS servers. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the DNS server. </td>
            </tr>
                                        <tr>
            <td colspan=2 > LDAP </td>
            <td>  list </td>
            <td> When ldap is in a given gather_subset </td>
            <td> Provides details of all LDAPs. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the LDAP. </td>
            </tr>
                                        <tr>
            <td colspan=2 > ActiveDirectory </td>
            <td>  list </td>
            <td> When ad is in a given gather_subset </td>
            <td> Provides details of all active directories. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the active directory. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Appliance </td>
            <td>  list </td>
            <td> When appliance is in a given gather_subset </td>
            <td> Provides details of all appliances. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the appliance. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the appliance. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > model </td>
                <td> str </td>
                <td>success</td>
                <td> Model type of the PowerStore. </td>
            </tr>
                                        <tr>
            <td colspan=2 > EmailNotification </td>
            <td>  list </td>
            <td> When email_notification is in a given gather_subset </td>
            <td> Provides details of all emails to which notifications will be sent. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the email. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > email_address </td>
                <td> str </td>
                <td>success</td>
                <td> Email address. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Cluster </td>
            <td>  list </td>
            <td> always </td>
            <td> Provides details of all clusters. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the cluster. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the cluster. </td>
            </tr>
                                        <tr>
            <td colspan=2 > TreeQuotas </td>
            <td>  list </td>
            <td> When tree_quota is in a given gather_subset </td>
            <td> Provides details of all tree quotas. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the tree quota. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > path </td>
                <td> str </td>
                <td>success</td>
                <td> Path of the tree quota. </td>
            </tr>
                                        <tr>
            <td colspan=2 > NFSExports </td>
            <td>  list </td>
            <td> When nfs_export is in a given gather_subset </td>
            <td> Provides details of all nfs exports. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the nfs export. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the nfs export. </td>
            </tr>
                                        <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Shows whether or not the resource has changed. </td>
        </tr>
                    <tr>
            <td colspan=2 > ProtectionPolicies </td>
            <td>  list </td>
            <td> When protection_policy is in a given gather_subset </td>
            <td> Provides details of all protection policies. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the protection policy. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the protection policy. </td>
            </tr>
                                        <tr>
            <td colspan=2 > ReplicationSession </td>
            <td>  list </td>
            <td> when replication_session given in gather_subset </td>
            <td> Details of all replication sessions. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the replication session. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Roles </td>
            <td>  list </td>
            <td> When role is in a given gather_subset </td>
            <td> Provides details of all roles. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the role. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the role. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Certificate </td>
            <td>  list </td>
            <td> When certificates is in a given gather_subset </td>
            <td> Provides details of all certificates. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the certificate. </td>
            </tr>
                                        <tr>
            <td colspan=2 > SnapshotRules </td>
            <td>  list </td>
            <td> When snapshot_rule is in a given gather_subset </td>
            <td> Provides details of all snapshot rules. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the snapshot rule. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the snapshot rule. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Array_Software_Version </td>
            <td>  str </td>
            <td> always </td>
            <td> API version of PowerStore array. </td>
        </tr>
                    <tr>
            <td colspan=2 > RemoteSupportContact </td>
            <td>  list </td>
            <td> When remote_support_contact is in a given gather_subset </td>
            <td> Provides details of all remote support contacts. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the remote support contact. </td>
            </tr>
                                        <tr>
            <td colspan=2 > SMTPConfig </td>
            <td>  list </td>
            <td> When smtp_config is in a given gather_subset </td>
            <td> Provides details of all smtp config. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the smtp config. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Networks </td>
            <td>  list </td>
            <td> When network is in a given gather_subset </td>
            <td> Provides details of all networks. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the network. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the network. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Hosts </td>
            <td>  list </td>
            <td> When host is in a given gather_subset </td>
            <td> Provides details of all hosts. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the host. </td>
            </tr>
                                        <tr>
            <td colspan=2 > LocalUsers </td>
            <td>  list </td>
            <td> When user is in a given gather_subset </td>
            <td> Provides details of all local users. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the user. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the user. </td>
            </tr>
                                        <tr>
            <td colspan=2 > ReplicationRules </td>
            <td>  list </td>
            <td> When replication_rule is in a given gather_subset </td>
            <td> Provides details of all replication rules. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the replication rule. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the replication rule. </td>
            </tr>
                                        </table>

### Authors
* Arindam Datta (@dattaarindam) <ansible.team@dell.com>
* Vivek Soni (@v-soni11) <ansible.team@dell.com>
* Akash Shendge (@shenda1) <ansible.team@dell.com>

--------------------------------
