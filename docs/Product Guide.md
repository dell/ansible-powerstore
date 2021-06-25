# Ansible Modules for Dell EMC PowerStore
## Product Guide 1.2
© 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell, EMC, and other trademarks are trademarks of Dell Inc. or its subsidiaries. Other trademarks may be trademarks of their respective owners.

--------------
## Contents
*   [File System Module](#file-system-module)
    *   [Synopsis](#synopsis)
    *   [Parameters](#parameters)
    *   [Notes](#notes)
    *   [Examples](#examples)
    *   [Return Values](#return-values)
    *   [Authors](#authors)
*   [Volume Module](#volume-module)
    *   [Synopsis](#synopsis-1)
    *   [Parameters](#parameters-1)
    *   [Notes](#notes-1)
    *   [Examples](#examples-1)
    *   [Return Values](#return-values-1)
    *   [Authors](#authors-1)
*   [Quota Module](#quota-module)
    *   [Synopsis](#synopsis-2)
    *   [Parameters](#parameters-2)
    *   [Notes](#notes-2)
    *   [Examples](#examples-2)
    *   [Return Values](#return-values-2)
    *   [Authors](#authors-2)
*   [Host Module](#host-module)
    *   [Synopsis](#synopsis-3)
    *   [Parameters](#parameters-3)
    *   [Examples](#examples-3)
    *   [Return Values](#return-values-3)
    *   [Authors](#authors-3)
*   [Snapshot Rule Module](#snapshot-rule-module)
    *   [Synopsis](#synopsis-4)
    *   [Parameters](#parameters-4)
    *   [Examples](#examples-4)
    *   [Return Values](#return-values-4)
    *   [Authors](#authors-4)
*   [Gatherfacts Module](#gatherfacts-module)
    *   [Synopsis](#synopsis-5)
    *   [Parameters](#parameters-5)
    *   [Examples](#examples-5)
    *   [Return Values](#return-values-5)
    *   [Authors](#authors-5)
*   [Replication Session Module](#replication-session-module)
    *   [Synopsis](#synopsis-6)
    *   [Parameters](#parameters-6)
    *   [Notes](#notes-3)
    *   [Examples](#examples-6)
    *   [Return Values](#return-values-6)
    *   [Authors](#authors-6)
*   [Host Group Module](#host-group-module)
    *   [Synopsis](#synopsis-7)
    *   [Parameters](#parameters-7)
    *   [Examples](#examples-7)
    *   [Return Values](#return-values-7)
    *   [Authors](#authors-7)
*   [NFS Module](#nfs-module)
    *   [Synopsis](#synopsis-8)
    *   [Parameters](#parameters-8)
    *   [Examples](#examples-8)
    *   [Return Values](#return-values-8)
    *   [Authors](#authors-8)
*   [Volume Group Module](#volume-group-module)
    *   [Synopsis](#synopsis-9)
    *   [Parameters](#parameters-9)
    *   [Notes](#notes-4)
    *   [Examples](#examples-9)
    *   [Return Values](#return-values-9)
    *   [Authors](#authors-9)
*   [NAS Server Module](#nas-server-module)
    *   [Synopsis](#synopsis-10)
    *   [Parameters](#parameters-10)
    *   [Examples](#examples-10)
    *   [Return Values](#return-values-10)
    *   [Authors](#authors-10)
*   [SMB Share Module](#smb-share-module)
    *   [Synopsis](#synopsis-11)
    *   [Parameters](#parameters-11)
    *   [Notes](#notes-5)
    *   [Examples](#examples-11)
    *   [Return Values](#return-values-11)
    *   [Authors](#authors-11)
*   [Snapshot Module](#snapshot-module)
    *   [Synopsis](#synopsis-12)
    *   [Parameters](#parameters-12)
    *   [Examples](#examples-12)
    *   [Return Values](#return-values-12)
    *   [Authors](#authors-12)
*   [Replication Rule Module](#replication-rule-module)
    *   [Synopsis](#synopsis-13)
    *   [Parameters](#parameters-13)
    *   [Examples](#examples-13)
    *   [Return Values](#return-values-13)
    *   [Authors](#authors-13)
*   [Protection Policy Module](#protection-policy-module)
    *   [Synopsis](#synopsis-14)
    *   [Parameters](#parameters-14)
    *   [Notes](#notes-6)
    *   [Examples](#examples-14)
    *   [Return Values](#return-values-14)
    *   [Authors](#authors-14)
*   [Filesystem Snapshot Module](#filesystem-snapshot-module)
    *   [Synopsis](#synopsis-15)
    *   [Parameters](#parameters-15)
    *   [Examples](#examples-15)
    *   [Return Values](#return-values-15)
    *   [Authors](#authors-15)

--------------

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
            <td colspan=2 > filesystem_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the file system. Mutually exclusive with filesystem_id. Mandatory only for create operation. </td>
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
            <td colspan=2 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Description of the file system. </td>
        </tr>
                    <tr>
            <td colspan=2 > nas_server</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name or ID of the NAS Server on which the file system is created. Mandatory parameter whenever filesystem_name is provided, since filesystem names are unique only within a NAS server </td>
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
            <td colspan=2 > cap_unit</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>GB</li>  <li>TB</li> </ul></td>
            <td> <br> capacity unit for the size.  <br> It defaults to 'GB', if not specified. </td>
        </tr>
                    <tr>
            <td colspan=2 > access_policy</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>NATIVE</li>  <li>UNIX</li>  <li>WINDOWS</li> </ul></td>
            <td> <br> File system security access policies. </td>
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
            <td colspan=2 > folder_rename_policy</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>ALL_ALLOWED</li>  <li>SMB_FORBIDDEN</li>  <li>ALL_FORBIDDEN</li> </ul></td>
            <td> <br> File system folder rename policies for the file system with multi-protocol access enabled.  <br> ALL_ALLOWED - All protocols are allowed to rename directories without any restrictions.  <br> SMB_FORBIDDEN - A directory rename from the SMB protocol will be denied if at least one file is opened in the directory or in one of its child directories.  <br> All_FORBIDDEN - Any directory rename request will be denied regardless of the protocol used, if at least one file is opened in the directory or in one of its child directories. </td>
        </tr>
                    <tr>
            <td colspan=2 > smb_properties</td>
            <td> dict  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Advance settings for SMB. It contains below optional candidate variables </td>
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
                <td colspan=1 > is_smb_no_notify_enabled </td>
                <td> bool  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Indicates whether notifications of changes to directory file structure are enabled.  </td>
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
                <td>  <br> Indicates whether file write notifications are enabled on the file system  </td>
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
            <td colspan=2 > protection_policy</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name or ID of the protection policy applied to the file system.  <br> Specifying "" (empty string) removes the existing protection policy from file system. </td>
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
                <td colspan=1 > grace_period </td>
                <td> int  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Grace period of soft limit.  </td>
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
                <td colspan=1 > default_soft_limit </td>
                <td> int  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Default soft limit of user quotas and tree quotas.  </td>
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
            <td colspan=2 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the filesystem should exist or not. </td>
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
                    <tr>
            <td colspan=2 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                                                    </table>

### Notes
* It is recommended to remove the protection policy before deleting the filesystem.

### Examples
```
 - name: Create FileSystem by Name
   register: result_fs
   dellemc_powerstore_filesystem:
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
   dellemc_powerstore_filesystem:
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
   dellemc_powerstore_filesystem:
     array_ip: "{{array_ip}}"
     verifycert: "{{verifycert}}"
     user: "{{user}}"
     password: "{{password}}"
     filesystem_id: "{{result_fs.filesystem_details.id}}"
     state: "present"

 - name: Delete File System by id
   dellemc_powerstore_filesystem:
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
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=2 > filesystem_details </td>
            <td>  complex </td>
            <td> When filesystem exists </td>
            <td> Details of the filesystem </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > access_policy </td>
                <td> str </td>
                <td>success</td>
                <td> Access policy about the filesystem. </td>
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
                <td colspan=1 > default_soft_limit </td>
                <td> int </td>
                <td>success</td>
                <td> Default soft limit period for a filesystem quota in byte. </td>
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
                <td colspan=1 > grace_period </td>
                <td> int </td>
                <td>success</td>
                <td> Default grace period for a filesystem quota in second. </td>
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
                <td colspan=1 > is_smb_notify_on_access_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether smb on access notify policy is enabled. </td>
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
                <td colspan=1 > locking_policy </td>
                <td> str </td>
                <td>success</td>
                <td> Locking policy about the filesystem. </td>
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
                <td colspan=1 > nas_server </td>
                <td> dict </td>
                <td>success</td>
                <td> Id and name of the nas server to which the filesystem belongs. </td>
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
                <td colspan=1 > size_total </td>
                <td> int </td>
                <td>success</td>
                <td> Total size of the filesystem in bytes. </td>
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
                                        </table>

### Authors
* Arindam Datta (@dattaarindam) <ansible.team@dell.com>

--------------------------------
# Volume Module

Manage volumes on a PowerStore storage system.

### Synopsis
 Managing volume on PowerStore storage system includes create volume, get details of volume, modify name, size, description, protection policy, performance policy, map or unmap volume to host/host group, and delete volume.

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
            <td colspan=1 > vol_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Unique name of the volume. This value must contain 128 or fewer printable unicode characters.  <br> Required when creating a volume. All other functionalities on a volume are supported using volume name or ID. </td>
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
            <td colspan=1 > vol_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The 36 character long ID of the volume, automatically generated when a volume is created.  <br> Cannot be used while creating a volume. All other functionalities on a volume are supported using volume name or ID. </td>
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
            <td colspan=1 > cap_unit</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>MB</li>  <li>GB</li>  <li>TB</li> </ul></td>
            <td> <br> Volume size unit.  <br> Used to signify unit of the size provided for creation and expansion of volume.  <br> It defaults to 'GB', if not specified. </td>
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
            <td colspan=1 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Description for the volume.  <br> Optional parameter when creating a volume.  <br> To modify, pass the new value in description field. </td>
        </tr>
                    <tr>
            <td colspan=1 > protection_policy</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The protection_policy of the volume.  <br> To represent policy, both name or ID can be used interchangably. The module will detect both.  <br> A volume can be assigned a protection policy at the time of creation of volume or later as well.  <br> The policy can also be changed for a given volume by simply passing the new value.  <br> The policy can be removed by passing an empty string.  <br> Check examples for more clarity. </td>
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
            <td colspan=1 > mapping_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>mapped</li>  <li>unmapped</li> </ul></td>
            <td> <br> Define whether the volume should be mapped to a host or hostgroup.  <br> mapped - indicates that the volume should be mapped to the host or host group.  <br> unmapped - indicates that the volume should not be mapped to the host or host group.  <br> Only one of a host or host group can be supplied in one call. </td>
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
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the volume should exist or not.  <br> present - indicates that the volume should exist on the system.  <br> absent - indicates that the volume should not exist on the system. </td>
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
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                                                    </table>

### Notes
* To create a new volume, vol_name and size is required. cap_unit, description, vg_name, performance_policy, and protection_policy are optional.
* new_name  should not be provided when creating a new volume.
* size is a required parameter for expand volume.
* Clones or Snapshots of a deleted production volume or a clone are not deleted.
* A volume that is attached to a host/host group, or that is part of a volume group cannot be deleted.

### Examples
```
- name: Create stand-alone volume
  dellemc_powerstore_volume:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vol_name: "{{vol_name}}"
    size: 1
    cap_unit: "{{cap_unit}}"
    state: 'present'

- name: Create stand-alone volume with performance and protection policy
  dellemc_powerstore_volume:
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
  dellemc_powerstore_volume:
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
  dellemc_powerstore_volume:
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
  dellemc_powerstore_volume:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vol_id: "{{result.volume_details.id}}"
    state: "present"

- name: Get volume details using name
  dellemc_powerstore_volume:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vol_name: "{{vol_name}}"
    state: "present"

- name: Modify volume size, name, description and performance policy
  dellemc_powerstore_volume:
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
  dellemc_powerstore_volume:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    new_name: "{{new_name}}"
    vol_name: "{{vol_name}}"
    state: "present"
    protection_policy: ""

- name: Map volume to a host with HLU
  dellemc_powerstore_volume:
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
  dellemc_powerstore_volume:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vol_name: "{{vol_name}}"
    state: 'present'
    mapping_state: 'mapped'
    host: 'host2'

- name: Delete volume
  dellemc_powerstore_volume:
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
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=3 > add_vols_to_vg </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume/s got added to volume group </td>
        </tr>
                    <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=3 > create_vg </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume group got created </td>
        </tr>
                    <tr>
            <td colspan=3 > delete_vg </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume group got deleted </td>
        </tr>
                    <tr>
            <td colspan=3 > modify_vg </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume group got modified </td>
        </tr>
                    <tr>
            <td colspan=3 > remove_vols_from_vg </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume/s got removed from volume group </td>
        </tr>
                    <tr>
            <td colspan=3 > volume_group_details </td>
            <td>  complex </td>
            <td> When volume group exists </td>
            <td> Details of the volume group </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > description </td>
                <td> str </td>
                <td>success</td>
                <td> ['description about the volume group'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ['The system generated ID given to the volume group'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > is_write_order_consistent </td>
                <td> bool </td>
                <td>success</td>
                <td> ['A boolean flag to indicate whether snapshot sets of the volume group will be write-order consistent'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> ['Name of the volume group'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > protection_policy_id </td>
                <td> str </td>
                <td>success</td>
                <td> ['The protection policy of the volume group'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > type </td>
                <td> str </td>
                <td>success</td>
                <td> ['The type of the volume group'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > volumes </td>
                <td> complex </td>
                <td>success</td>
                <td> ['The volumes details of the volume group'] </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> ['The system generated ID given to the volume associated with the volume group'] </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> ['The name of the volume associated with the volume group.'] </td>
                </tr>
                                                                    </table>

### Authors
* Ambuj Dubey (@AmbujDube) <ansible.team@dell.com>
* Manisha Agrawal (@agrawm3) <ansible.team@dell.com>

--------------------------------
# Quota Module

Manage Tree Quotas and User Quotas on PowerStore.

### Synopsis
 Managing  Quotas on Powerstore storage system includes getting details, modifying, creating and deleting  Quotas.

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
            <td colspan=2 > path</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The path on which the quota will be imposed.  <br> Path is relative to the root of the filesystem.  <br> For user quota, if path is not specified, quota will be created at the root of the filesystem. </td>
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
            <td colspan=2 > quota_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Id of the user/tree quota.  <br> If quota_id is mentioned, then path/nas_server/file_system/quota_type is not required. </td>
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
            <td colspan=2 > nas_server</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The NAS server. This could be the name or ID of the NAS server. </td>
        </tr>
                    <tr>
            <td colspan=2 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Additional information that can be mentioned for a Tree Quota.  <br> Description parameter can only be used when quota_type is 'tree' </td>
        </tr>
                    <tr>
            <td colspan=2 > unix_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the unix user account for which quota operations will be performed.  <br> Any one among uid/unix_name/windows_name/windows_sid is required when quota_type is 'user'. </td>
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
            <td colspan=2 > uid</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the unix user account for which quota operations will be performed.  <br> Any one among uid/unix_name/windows_name/windows_sid is required when quota_type is 'user'. </td>
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
            <td colspan=2 > quota</td>
            <td> dict  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Specifies Quota parameters. </td>
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
                <td colspan=1 > cap_unit </td>
                <td> str  </td>
                <td></td>
                <td> GB </td>
                <td> <ul> <li>GB</li>  <li>TB</li> </ul></td>
                <td>  <br> Unit of storage for the hard and soft limits.  <br> This parameter is required if limit is specified.  </td>
            </tr>
                            <tr>
            <td colspan=2 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the Quota should exist or not.  <br> present  indicates that the Quota should exist on the system.  <br> absent  indicates that the Quota should not exist on the system. </td>
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
                    <tr>
            <td colspan=2 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                                                    </table>

### Notes
* Tree quota can not be created at the root of the filesystem.
* When the ID of the filesystem is passed then nas_server is not required. If passed, then filesystem should exist for the nas_server, else the task will fail.
* If a primary directory of the current directory or a subordinate directory of the path is having a Tree Quota configured, then the quota for that path can't be created. Hierarchical tree quotas are not allowed.
* When the first quota is created for a directory/user in a filesystem then the quotas will be enabled for that filesystem automatically.
* If a user quota is to be created on a tree quota, then the user quotas will be enabled automatically in a tree quota.
* Delete User Quota operation is not supported.

### Examples
```
    - name: Create a Quota for a User using unix name
      dellemc_powerstore_quota:
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
      dellemc_powerstore_quota:
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
      dellemc_powerstore_quota:
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
      dellemc_powerstore_quota:
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
      dellemc_powerstore_quota:
        array_ip: "{{array_ip}}"
        verifycert: "{{verify_cert}}"
        user: "{{user}}"
        password: "{{password}}"
        quota_id: "{{quota_id}}"
        state: "present"

    - name: Delete a Tree Quota
      dellemc_powerstore_quota:
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
            <td colspan=4 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=4 > quota_details </td>
            <td>  complex </td>
            <td> When Quota exists. </td>
            <td> The quota details. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > description </td>
                <td> str </td>
                <td>success</td>
                <td> ['Additional information about the tree quota.', 'Only applicable for Tree Quotas.'] </td>
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
                    <td colspan=2 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> ID of filesystem. </td>
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
                    <td colspan=2 > nas_server </td>
                    <td> dict </td>
                    <td>success</td>
                    <td> nas_server of filesystem. </td>
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
                <td colspan=3 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the Quota. </td>
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
                <td colspan=3 > size_used </td>
                <td> int </td>
                <td>success</td>
                <td> Size currently consumed by Tree/User on the filesystem. </td>
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
                <td> ['State of the user quota or tree quota record period.', 'OK means No quota limits are exceeded.', 'Soft_Exceeded means Soft limit is exceeded, and grace period is not expired.', 'Soft_Exceeded_And_Expired means Soft limit is exceeded, and grace period is expired.', 'Hard_Reached means Hard limit is reached.'] </td>
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
                <td colspan=3 > tree_quota_for_user_quota </td>
                <td> complex </td>
                <td>success</td>
                <td> ['Additional Information of Tree Quota limits on which user quota exists.', 'Only applicable for User Quotas'] </td>
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
                <td colspan=3 > tree_quota_id </td>
                <td> str </td>
                <td>success</td>
                <td> ['ID of the Tree Quota on which the specific User Quota exists.', 'Only applicable for user quotas.'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > uid </td>
                <td> int </td>
                <td>success</td>
                <td> ['The ID of the unix host for which user quota exists.', 'Only applicable for user quotas.'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > unix_name </td>
                <td> str </td>
                <td>success</td>
                <td> ['The Name of the unix host for which user quota exists.', 'Only applicable for user quotas.'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > windows_name </td>
                <td> str </td>
                <td>success</td>
                <td> ['The Name of the Windows host for which user quota exists.', 'Only applicable for user quotas.'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > windows_sid </td>
                <td> str </td>
                <td>success</td>
                <td> ['The SID of the windows host for which user quota exists.', 'Only applicable for user quotas.'] </td>
            </tr>
                                        </table>

### Authors
* P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

--------------------------------
# Host Module

Manage host on PowerStore storage system.

### Synopsis
 Managing host on PowerStore storage system includes create host with a set of initiators, add/remove initiators from host, rename host and delete host.

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
            <td colspan=1 > host_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The host name. This value must contain 128 or fewer printable Unicode characters.  <br> Creation of an empty host is not allowed.  <br> Required when creating a host.  <br> Use either host_id or host_name for modify and delete tasks. </td>
        </tr>
                    <tr>
            <td colspan=1 > host_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The 36 character long host id automatically generated when a host is created.  <br> Use either host_id or host_name for modify and delete tasks.  <br> host_id cannot be used while creating host, as it is generated by the array after creation of host. </td>
        </tr>
                    <tr>
            <td colspan=1 > os_type</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>Windows</li>  <li>Linux</li>  <li>ESXi</li>  <li>AIX</li>  <li>HP-UX</li>  <li>Solaris</li> </ul></td>
            <td> <br> Operating system of the host.  <br> Required when creating a host  <br> OS type cannot be modified for a given host. </td>
        </tr>
                    <tr>
            <td colspan=1 > initiators</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> List of Initiator WWN or IQN to be added or removed from the host.  <br> Subordinate initiators in a host can only be of one type, either FC or iSCSI.  <br> Required when creating a host. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the host should exist or not.  <br> present - indicates that the host should exist in system.  <br> absent - indicates that the host should not exist in system. </td>
        </tr>
                    <tr>
            <td colspan=1 > initiator_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-host</li>  <li>absent-in-host</li> </ul></td>
            <td> <br> Define whether the initiators should be present or absent in host.  <br> present-in-host - indicates that the initiators should exist on host.  <br> absent-in-host - indicates that the initiators should not exist on host.  <br> Required when creating a host with initiators or adding/removing initiators to/from existing host. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The new name of host for renaming function. This value must contain 128 or fewer printable Unicode characters.  <br> Cannot be specified when creating a host. </td>
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
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                                            </table>


### Examples
```
  - name: Create host
    dellemc_powerstore_host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_name: "{{host_name}}"
      os_type: 'Windows'
      initiators:
        -21:00:00:24:ff:31:e9:fc
      state: 'present'
      initiator_state: 'present-in-host'

  - name: Get host details by name
    dellemc_powerstore_host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_name: "{{host_name}}"
      state: 'present'

  - name: Get host details by id
    dellemc_powerstore_host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_id: "{{host_id}}"
      state: 'present'

  - name: Add initiators to host
    dellemc_powerstore_host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_name: "{{host_name}}"
      initiators:
        -21:00:00:24:ff:31:e9:ee
      initiator_state: 'present-in-host'
      state: 'present'

  - name: Remove initiators from host
    dellemc_powerstore_host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_name: "{{host_name}}"
      initiators:
        -21:00:00:24:ff:31:e9:ee
      initiator_state: 'absent-in-host'
      state: 'present'

  - name: Rename host
    dellemc_powerstore_host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_name: "{{host_name}}"
      new_name: "{{new_host_name}}"
      state: 'present'

  - name: Delete host
    dellemc_powerstore_host:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      host_name: "{{new_host_name}}"
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
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=3 > hostgroup_details </td>
            <td>  complex </td>
            <td> When host group exists </td>
            <td> Details of the host group </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Description about the host group </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > hosts </td>
                <td> complex </td>
                <td>success</td>
                <td> The hosts details which are part of this host group </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The ID of the host </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The name of the host </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID given to the host group </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the host group </td>
            </tr>
                                        </table>

### Authors
* Manisha Agrawal (@agrawm3) <ansible.team@dell.com>

--------------------------------
# Snapshot Rule Module

SnapshotRule operations on a PowerStore storage system.

### Synopsis
 Performs all snapshot rule operations on PowerStore Storage System.
 This modules supports get details of an existing snapshot rule, create new Snapshot Rule with Interval, create new Snapshot Rule with specific time and days_of_week with all supported. parameters.
 Modify Snapshot Rule with supported parameters.
 Delete a specific Snapshot Rule.

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
            <td colspan=1 > name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> String variable. Indicates the name of the Snapshot rule. </td>
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
            <td colspan=1 > new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> String variable. Indicates the new name of the Snapshot rule.  <br> Used for renaming operation </td>
        </tr>
                    <tr>
            <td colspan=1 > days_of_week</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td> <ul> <li>Monday</li>  <li>Tuesday</li>  <li>Wednesday</li>  <li>Thursday</li>  <li>Friday</li>  <li>Saturday</li>  <li>Sunday</li> </ul></td>
            <td> <br> List of strings to specify days of the week on which the Snapshot rule. should be applied. Must be applied for Snapshot rules where the 'time_of_day' parameter is set. Optional for the Snapshot rule created with an interval. When 'days_of_week' is not specified for a new Snapshot rule, the rule is applied on every day of the week. </td>
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
            <td colspan=1 > desired_retention</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Integer variable. Indicates the desired Snapshot retention period.  <br> It is required when creating a new Snapshot rule. </td>
        </tr>
                    <tr>
            <td colspan=1 > time_of_day</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> String variable. Indicates the time of the day to take a daily Snapshot, with the format "hh:mm" in 24 hour time format  <br> When creating a Snapshot rule, specify either "interval"or "time_of_day" but not both. </td>
        </tr>
                    <tr>
            <td colspan=1 > delete_snaps</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Boolean variable to specify whether all Snapshots previously created by this rule should also be deleted when this rule is removed.  <br> True specifies to delete all previously created Snapshots by this rule while deleting this rule.  <br> False specifies to retain all previously created Snapshots while deleting this rule </td>
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
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                                            </table>


### Examples
```
- name: Get details of an existing snapshot rule by name
  dellemc_powerstore_snapshotrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    state: "present"

- name: Get details of an existing snapshot rule by id
  dellemc_powerstore_snapshotrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    snapshotrule_id: "{{snapshotrule_id}}"
    state: "present"

- name: Create new snapshot rule by interval
  dellemc_powerstore_snapshotrule:
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
  dellemc_powerstore_snapshotrule:
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
  dellemc_powerstore_snapshotrule:
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
  dellemc_powerstore_snapshotrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    interval: "{{interval}}"
    state: "present"

- name: Delete an existing snapshot rule by name
  dellemc_powerstore_snapshotrule:
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
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=3 > snapshotrule_details </td>
            <td>  complex </td>
            <td> When snapshot rule exists </td>
            <td> Details of the snapshot rule </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > days_of_week </td>
                <td> list </td>
                <td>success</td>
                <td> List of string to specify days of the week on which the rule should be applied </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > desired_retention </td>
                <td> int </td>
                <td>success</td>
                <td> Desired snapshot retention period </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID given to the snapshot rule </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > interval </td>
                <td> str </td>
                <td>success</td>
                <td> The interval between snapshots </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the snapshot rule </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > policies </td>
                <td> complex </td>
                <td>success</td>
                <td> The protection policies details of the snapshot rule </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The protection policy ID in which the snapshot rule is selected </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Name of the protection policy in which the snapshot rule is selected </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > time_of_day </td>
                <td> str </td>
                <td>success</td>
                <td> The time of the day to take a daily snapshot </td>
            </tr>
                                        </table>

### Authors
* Arindam Datta (@dattaarindam) <ansible.team@dell.com>

--------------------------------
# Gatherfacts Module

Gathers information about PowerStore Storage entities

### Synopsis
 Gathers the list of specified PowerStore Storage System entities, such as the list of cluster nodes, volumes, volume groups, hosts, host groups, snapshot rules, protection policies, NAS servers, NFS exports, SMB shares, tree quotas, user quotas, and file systems.

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
            <td colspan=2 > gather_subset</td>
            <td> list   <br> elements: str </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>vol</li>  <li>vg</li>  <li>host</li>  <li>hg</li>  <li>node</li>  <li>protection_policy</li>  <li>snapshot_rule</li>  <li>nas_server</li>  <li>nfs_export</li>  <li>smb_share</li>  <li>tree_quota</li>  <li>user_quota</li>  <li>file_system</li>  <li>replication_rule</li>  <li>replication_session</li>  <li>remote_system</li> </ul></td>
            <td> <br> A list of string variables which specify the PowerStore system entities requiring information.information.  <br> vol - volumes  <br> node - all the nodes  <br> vg - volume groups  <br> protection_policy - protection policy  <br> host - hosts  <br> hg -  host groups  <br> snapshot_rule - snapshot rule  <br> nas_server - NAS servers  <br> nfs_export - NFS exports  <br> smb_share - SMB shares  <br> tree_quota - tree quotas  <br> user_quota - user quotas  <br> file_system - file systems  <br> replication_rule - replication rules  <br> replication_session - replication sessions  <br> remote_system - remote systems </td>
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
                <td colspan=1 > filter_key </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td></td>
                <td>  <br> Name identifier of the filter.  </td>
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
                <td colspan=1 > filter_value </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td></td>
                <td>  <br> Value of the filter key.  </td>
            </tr>
                            <tr>
            <td colspan=2 > all_pages</td>
            <td> bool  </td>
            <td></td>
            <td> False </td>
            <td></td>
            <td> <br> Indicates whether to return all available entities on the storage system.  <br> If set to True, the Gather Facts module will implement pagination and return all entities. Otherwise, a maximum of the first 100 entities of any type will be returned. </td>
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
                    <tr>
            <td colspan=2 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                                            </table>


### Examples
```
- name: Get list of volumes, volume groups, hosts, host groups and node
  dellemc_powerstore_gatherfacts:
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
  dellemc_powerstore_gatherfacts:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - replication_rule
      - replication_session
      - remote_system

- name: Get list of volumes whose state notequal to ready
  dellemc_powerstore_gatherfacts:
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
  dellemc_powerstore_gatherfacts:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - protection_policy
      - snapshot_rule

- name: Get list of snapshot rules whose desired_retention between 101-499
  dellemc_powerstore_gatherfacts:
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
  dellemc_powerstore_gatherfacts:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - nas_server
      - nfs_export
      - smb_share

- name: Get list of tree quota, user quota and file system
  dellemc_powerstore_gatherfacts:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - tree_quota
      - user_quota
      - file_system

- name: Get list of nas server whose name equal to 'nas_server'
  dellemc_powerstore_gatherfacts:
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
  dellemc_powerstore_gatherfacts:
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
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=19>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=19 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Shows whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=19 > subset_result </td>
            <td>  complex </td>
            <td> always </td>
            <td> Provides details of all given subsets. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=18 > Cluster </td>
                <td> list </td>
                <td>success</td>
                <td> Provides details of all clusters. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> cluster id </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> cluster name </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=18 > FileSystems </td>
                <td> list </td>
                <td>success</td>
                <td> Provides details of all filesystems. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> filesystem id </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> filesystem name </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=18 > HostGroups </td>
                <td> list </td>
                <td>success</td>
                <td> Provides details of all hostgroups. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> hostgroup id </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> hostgroup name </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=18 > Hosts </td>
                <td> list </td>
                <td>success</td>
                <td> Provides details of all hosts. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> host id </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> host name </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=18 > NASServers </td>
                <td> list </td>
                <td>success</td>
                <td> Provides details of all nas servers. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> nas server id </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> nas server name </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=18 > NFSExports </td>
                <td> list </td>
                <td>success</td>
                <td> Provides details of all nfs exports. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> nfs export id </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> nfs export name </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=18 > Nodes </td>
                <td> list </td>
                <td>success</td>
                <td> Provides details of all nodes. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> node id </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> node name </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=18 > ProtectionPolicies </td>
                <td> list </td>
                <td>success</td>
                <td> Provides details of all protectionpolicies. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> protectionpolicy id </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> protectionpolicy name </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=18 > RemoteSystems </td>
                <td> list </td>
                <td>success</td>
                <td> Provides details of all remote systems. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> remote system id </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> remote system name </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=18 > ReplicationRules </td>
                <td> list </td>
                <td>success</td>
                <td> Provides details of all replication rules. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> replication rule id </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> replication rule name </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=18 > ReplicationSession </td>
                <td> list </td>
                <td>success</td>
                <td> details of all replication sessions </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> replication session id </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=18 > SMBShares </td>
                <td> list </td>
                <td>success</td>
                <td> Provides details of all smb shares. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> smb share id </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> smb share name </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=18 > SnapshotRules </td>
                <td> list </td>
                <td>success</td>
                <td> Provides details of all snapshot rules. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> snapshot rule id </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> snapshot rule name </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=18 > TreeQuotas </td>
                <td> list </td>
                <td>success</td>
                <td> Provides details of all tree quotas. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> tree quota id </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > path </td>
                    <td> str </td>
                    <td>success</td>
                    <td> tree quota path </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=18 > UserQuotas </td>
                <td> list </td>
                <td>success</td>
                <td> Provides details of all user quotas </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> user quota id </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=18 > VolumeGroups </td>
                <td> list </td>
                <td>success</td>
                <td> Provides details of all volumegroups. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> volumegroup id </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> volumegroup name </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=18 > Volumes </td>
                <td> list </td>
                <td>success</td>
                <td> Provides details of all volumes. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> volume id </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=17 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> volume name </td>
                </tr>
                                                                    </table>

### Authors
* Arindam Datta (@dattaarindam) <ansible.team@dell.com>
* Vivek Soni (@v-soni11) <ansible.team@dell.com>

--------------------------------
# Replication Session Module

Replication session operations on a PowerStore storage system.

### Synopsis
 Performs all replication session state change operations on a PowerStore Storage System.
 This module supports get details of an existing replication session.
 Updating the state of the replication session.

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
            <td colspan=1 > volume_group</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name/ID of the volume group for which a replication session exists.  <br> volume_group, volume, and session_id are mutually exclusive. </td>
        </tr>
                    <tr>
            <td colspan=1 > volume</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name/ID of the volume for which replication session exists.  <br> volume_group, volume, and session_id are mutually exclusive. </td>
        </tr>
                    <tr>
            <td colspan=1 > session_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> ID of the replication session.  <br> volume_group, volume, and session_id are mutually exclusive. </td>
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
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                                                    </table>

### Notes
* Manual synchronization for a replication session is not supported through the Ansible module.
* When the current state of the replication session is 'OK' and in the playbook task 'synchronizing', then it will return "changed" as False. This is because there is a scheduled synchronization in place with the associated replication rule's RPO in the protection policy.

### Examples
```
- name: Pause a replication session
  dellemc_powerstore_replicationsession:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    volume: "sample_volume_1"
    session_state: "paused"

- name: Synchronize a replication session
  dellemc_powerstore_replicationsession:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    volume: "sample_volume_1"
    session_state: "synchronizing"

- name: Get details of a replication session
  dellemc_powerstore_replicationsession:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    volume: "sample_volume_1"

- name: Fail over a replication session
  dellemc_powerstore_replicationsession:
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
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=2 > replication_session_details </td>
            <td>  complex </td>
            <td> When replication session exists </td>
            <td> Details of the replication session </td>
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
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ['The system generated ID of the replication session.', 'Unique across source and destination roles.'] </td>
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
                <td colspan=1 > local_resource_id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the local storage resource for the replication session. </td>
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
                <td colspan=1 > progress_percentage </td>
                <td> int </td>
                <td>success</td>
                <td> Progress of the current replication operation. </td>
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
                <td colspan=1 > remote_system_id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the remote system instance. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > replication_rule_id </td>
                <td> str </td>
                <td>success</td>
                <td> Associated replication rule instance if created by policy engine. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > resource_type </td>
                <td> str </td>
                <td>success</td>
                <td> ['Storage resource type eligible for replication protection.', 'volume - Replication session created on a volume.', 'volume_group - Replication session created on a volume group.'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > role </td>
                <td> str </td>
                <td>success</td>
                <td> ['Role of the replication session.', 'Source - The local resource is the source of the remote replication session.', 'Destination - The local resource is the destination of the remote replication session.'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > state </td>
                <td> str </td>
                <td>success</td>
                <td> State of the replication session. </td>
            </tr>
                                        </table>

### Authors
* P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

--------------------------------
# Host Group Module

Manage host group on PowerStore Storage System.

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
            <td colspan=1 > hostgroup_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The host group name. This value must contain 128 or fewer printable Unicode characters.  <br> Creation of an empty host group is not allowed.  <br> Required when creating a host group.  <br> Use either hostgroup_id or hostgroup_name for modify and delete tasks. </td>
        </tr>
                    <tr>
            <td colspan=1 > hostgroup_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The 36-character long host group id, automatically generated when a host group is created.  <br> Use either hostgroup_id or hostgroup_name for modify and delete tasks.  <br> hostgroup_id cannot be used while creating host group, as it is generated by the array after creation of host group. </td>
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
            <td> <br> Define whether the host group should exist or not.  <br> present - indicates that the host group should exist on the system.  <br> absent - indicates that the host group should not exist on the system.  <br> Deletion of a host group results in deletion of the containing hosts as well. Remove hosts from the host group first to retain them. </td>
        </tr>
                    <tr>
            <td colspan=1 > host_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-group</li>  <li>absent-in-group</li> </ul></td>
            <td> <br> Define whether the hosts should be present or absent in host group.  <br> present-in-group - indicates that the hosts should exist on the host group.  <br> absent-in-group - indicates that the hosts should not exist on the host group.  <br> Required when creating a host group with hosts or adding/removing hosts from existing host group. </td>
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
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                                            </table>


### Examples
```
  - name: Create host group with hosts using host name
    dellemc_powerstore_hostgroup:
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
    dellemc_powerstore_hostgroup:
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
    dellemc_powerstore_hostgroup:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      hostgroup_name: "{{hostgroup_name}}"
      state: 'present'

  - name: Get host group details using ID
    dellemc_powerstore_hostgroup:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      hostgroup_id: "{{host group_id}}"
      state: 'present'

  - name: Add hosts to host group
    dellemc_powerstore_hostgroup:
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
    dellemc_powerstore_hostgroup:
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
    dellemc_powerstore_hostgroup:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      hostgroup_name: "{{hostgroup_name}}"
      new_name: "{{new_hostgroup_name}}"
      state: 'present'

  - name: Delete host group
    dellemc_powerstore_hostgroup:
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
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=3 > hostgroup_details </td>
            <td>  complex </td>
            <td> When host group exists </td>
            <td> Details of the host group </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Description about the host group </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > hosts </td>
                <td> complex </td>
                <td>success</td>
                <td> The hosts details which are part of this host group </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The ID of the host </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The name of the host </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID given to the host group </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the host group </td>
            </tr>
                                        </table>

### Authors
* Manisha Agrawal (@agrawm3) <ansible.team@dell.com>

--------------------------------
# NFS Module

Manage NFS exports on Dell EMC PowerStore.

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
            <td colspan=1 > nfs_export_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the NFS export.  <br> Mandatory for create operation.  <br> Specify either nfs_export_name or nfs_export_id(but not both) for any operation. </td>
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
            <td colspan=1 > filesystem</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID/Name of the filesystem for which the NFS export will be created.  <br> Either filesystem or snapshot is required for creation of the NFS Export.  <br> If filesystem name is specified, then nas_server is required to uniquely identify the filesystem.  <br> If filesystem parameter is provided, then snapshot cannot be specified. </td>
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
            <td colspan=1 > nas_server</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The NAS server. This could be the name or ID of the NAS server. </td>
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
            <td colspan=1 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The description for the NFS export. </td>
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
            <td colspan=1 > read_only_root_hosts</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Hosts with read-only access for root user to the NFS export. </td>
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
            <td colspan=1 > read_write_root_hosts</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Hosts with read and write access for root user to the NFS export. </td>
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
            <td colspan=1 > anonymous_uid</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Specifies the user ID of the anonymous account.  <br> If not specified at the time of creation, it will be set to -2. </td>
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
            <td colspan=1 > is_no_suid</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> If set, do not allow access to set SUID. Otherwise, allow access.  <br> If not specified at the time of creation, it will be set to False. </td>
        </tr>
                    <tr>
            <td colspan=1 > host_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-export</li>  <li>absent-in-export</li> </ul></td>
            <td> <br> Define whether the hosts can access the NFS export.  <br> Required when adding or removing host access from the export. </td>
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
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                                            </table>


### Examples
```
- name: Create NFS export (filesystem)
  dellemc_powerstore_nfs:
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
  dellemc_powerstore_nfs:
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
  dellemc_powerstore_nfs:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    nfs_export_id: "{{export_id}}"
    state: "present"

- name: Add Read-Only and Read-Write hosts to NFS export
  dellemc_powerstore_nfs:
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
  dellemc_powerstore_nfs:
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
  dellemc_powerstore_nfs:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    nfs_export_id: "{{export_id}}"
    description: "modify description"
    default_access: "ROOT"
    state: "present"

- name: Delete NFS export using name
  dellemc_powerstore_nfs:
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
            <td colspan=4 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=4 > nfs_export_details </td>
            <td>  complex </td>
            <td> When NFS export exists. </td>
            <td> The NFS export details. </td>
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
                <td colspan=3 > anonymous_UID </td>
                <td> int </td>
                <td>success</td>
                <td> The user ID of the anonymous account. </td>
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
                <td colspan=3 > description </td>
                <td> str </td>
                <td>success</td>
                <td> The description for the NFS export. </td>
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
                    <td colspan=2 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The ID of the filesystem. </td>
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
                <td colspan=3 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the NFS export. </td>
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
                <td colspan=3 > min_security </td>
                <td> str </td>
                <td>success</td>
                <td> NFS enforced security type for users accessing an NFS export. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the NFS export. </td>
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
                <td colspan=3 > path </td>
                <td> str </td>
                <td>success</td>
                <td> Local path to a location within the file system. </td>
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
                <td colspan=3 > read_only_root_hosts </td>
                <td> list </td>
                <td>success</td>
                <td> Hosts with read-only for root user access to the NFS export. </td>
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
                <td colspan=3 > read_write_root_hosts </td>
                <td> list </td>
                <td>success</td>
                <td> Hosts with read and write for root user access to the NFS export. </td>
            </tr>
                                        </table>

### Authors
* Akash Shendge (@shenda1) <ansible.team@dell.com>

--------------------------------
# Volume Group Module

Manage volume groups on a PowerStore Storage System

### Synopsis
 Managing volume group on PowerStore Storage System includes creating new volume group, adding volumes to volume group, removing volumes from volume group, renaming volume group, modifying volume group, and deleting volume group.

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
            <td colspan=1 > vg_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the volume group. </td>
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
            <td colspan=1 > volumes</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This is a list of volumes.  <br> Either the volume ID or name must be provided for adding/removing existing volumes from a volume group.  <br> If volumes are given, then vol_state should also be specified. </td>
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
            <td colspan=1 > protection_policy</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> String variable. Represents Protection policy id or name used for volume group.  <br> Specifying an empty string or "" removes the existing protection policy from volume group. </td>
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
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the volume group should exist or not. </td>
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
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                                                    </table>

### Notes
* vol_state is mandatory if volumes are provided.
* A protection policy can be specified either for an volume group, or for the individual volumes inside the volume group.
* A volume can be a member of at most one volume group.
* Specifying "protection_policy" as empty string or "" removes the existing protection policy from a volume group.

### Examples
```
- name: Create volume group without protection policy
  dellemc_powerstore_volumegroup:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vg_name: "{{vg_name}}"
    description: "This volume group is for ansible"
    state: "present"

- name: Get details of volume group
  dellemc_powerstore_volumegroup:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vg_name: "{{vg_name}}"
    state: "present"

- name: Add volumes to volume group
  dellemc_powerstore_volumegroup:
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
  dellemc_powerstore_volumegroup:
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
  dellemc_powerstore_volumegroup:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vg_name: "{{vg_name}}"
    new_vg_name: "{{new_vg_name}}"
    is_write_order_consistent: False
    state: "present"

- name: Get details of volume group by ID
  dellemc_powerstore_volumegroup:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    vg_id: "{{vg_id}}"
    state: "present"

- name: Delete volume group
  dellemc_powerstore_volumegroup:
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
            <td colspan=3 > add_vols_to_vg </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume/s got added to volume group </td>
        </tr>
                    <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=3 > create_vg </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume group got created </td>
        </tr>
                    <tr>
            <td colspan=3 > delete_vg </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume group got deleted </td>
        </tr>
                    <tr>
            <td colspan=3 > modify_vg </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume group got modified </td>
        </tr>
                    <tr>
            <td colspan=3 > remove_vols_from_vg </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume/s got removed from volume group </td>
        </tr>
                    <tr>
            <td colspan=3 > volume_group_details </td>
            <td>  complex </td>
            <td> When volume group exists </td>
            <td> Details of the volume group </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > description </td>
                <td> str </td>
                <td>success</td>
                <td> ['description about the volume group'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ['The system generated ID given to the volume group'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > is_write_order_consistent </td>
                <td> bool </td>
                <td>success</td>
                <td> ['A boolean flag to indicate whether snapshot sets of the volume group will be write-order consistent'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> ['Name of the volume group'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > protection_policy_id </td>
                <td> str </td>
                <td>success</td>
                <td> ['The protection policy of the volume group'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > type </td>
                <td> str </td>
                <td>success</td>
                <td> ['The type of the volume group'] </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > volumes </td>
                <td> complex </td>
                <td>success</td>
                <td> ['The volumes details of the volume group'] </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> ['The system generated ID given to the volume associated with the volume group'] </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> ['The name of the volume associated with the volume group.'] </td>
                </tr>
                                                                    </table>

### Authors
* Akash Shendge (@shenda1) <ansible.team@dell.com>
* Arindam Datta (@dattaarindam) <ansible.team@dell.com>

--------------------------------
# NAS Server Module

NAS Server operations on PowerStore Storage system.

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
            <td colspan=1 > nas_server_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the NAS server. Mutually exclusive with nas_server_id. </td>
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
            <td colspan=1 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Description of the NAS server. </td>
        </tr>
                    <tr>
            <td colspan=1 > nas_server_new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New name of the NAS server for a rename operation. </td>
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
            <td colspan=1 > preferred_node</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Unique identifier or name of the preferred node for the NAS server. The initial value (on NAS server create) is taken from the current node. </td>
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
            <td colspan=1 > default_unix_user</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Default Unix user name used for granting access in case of Windows to Unix user mapping failure. When empty, access in such case is denied. </td>
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
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the nas server should exist or not. </td>
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
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                                            </table>


### Examples
```
 - name: Get details of NAS Server by name
   dellemc_powerstore_nasserver:
     array_ip: "{{array_ip}}"
     verifycert: "{{verifycert}}"
     user: "{{user}}"
     password: "{{password}}"
     nas_server_name: "{{nas_server_name}}"
     state: "present"

 - name: Get Details of NAS Server by ID
   dellemc_powerstore_nasserver:
     array_ip: "{{array_ip}}"
     verifycert: "{{verifycert}}"
     user: "{{user}}"
     password: "{{password}}"
     nas_server_id: "{{nas_id}}"
     state: "present"

 - name: Rename NAS Server by Name
   dellemc_powerstore_nasserver:
     array_ip: "{{array_ip}}"
     verifycert: "{{verifycert}}"
     user: "{{user}}"
     password: "{{password}}"
     nas_server_name: "{{nas_server_name}}"
     nas_server_new_name : "{{nas_server_new_name}}"
     state: "present"

 - name: Modify NAS Server attributes by ID
   dellemc_powerstore_nasserver:
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
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=2 > nasserver_details </td>
            <td>  complex </td>
            <td> When nas server exists </td>
            <td> Details about the nas server </td>
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
                <td colspan=1 > backup_IPv6_interface_id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the preferred IPv6 backup interface. </td>
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
                <td colspan=1 > current_unix_directory_service </td>
                <td> str </td>
                <td>success</td>
                <td> Define the Unix directory service used for looking up identity information for Unix such as UIDs, GIDs, net groups, and so on. </td>
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
                <td colspan=1 > file_interfaces </td>
                <td> dict </td>
                <td>success</td>
                <td> This is the inverse of the resource type file_interface association.Will return the id,name & ip_address of the associated file interface </td>
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
                <td colspan=1 > file_systems </td>
                <td> dict </td>
                <td>success</td>
                <td> This is the inverse of the resource type file_system association. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID given to the nas server </td>
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
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the nas server </td>
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
                <td colspan=1 > operational_status </td>
                <td> str </td>
                <td>success</td>
                <td> NAS server operational status. </td>
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
                <td colspan=1 > production_IPv4_interface_id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the preferred IPv4 production interface. </td>
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
                                        </table>

### Authors
* Arindam Datta (@dattaarindam) <ansible.team@dell.com>

--------------------------------
# SMB Share Module

Manage SMB shares on a PowerStore storage system.

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
            <td colspan=1 > share_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the SMB share.  <br> Required during creation of the SMB share.  <br> For all other operations either share_name or share_id is required. </td>
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
            <td colspan=1 > path</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Local path to the file system/Snapshot or any existing sub-folder of the file system/Snapshot that is shared over the network.  <br> Path is relative to the base of the NAS server and must start with the name of the filesystem.  <br> Required for creation of the SMB share. </td>
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
            <td colspan=1 > snapshot</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID/Name of the Snapshot.  <br> Either filesystem or snapshot is required for creation of the SMB share.  <br> If snapshot name is specified, then nas_server is required to uniquely identify the snapshot.  <br> If snapshot parameter is provided, then filesystem cannot be specified.  <br> SMB share can be created only if access type of snapshot is "protocol". </td>
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
            <td colspan=1 > is_abe_enabled</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Indicates whether Access-based Enumeration (ABE) for SMB share is enabled.  <br> During creation, if not mentioned, then the default is False. </td>
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
            <td colspan=1 > is_continuous_availability_enabled</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Indicates whether continuous availability for SMB 3.0 is enabled.  <br> During creation, if not mentioned, then the default is False. </td>
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
            <td colspan=1 > offline_availability</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>MANUAL</li>  <li>DOCUMENTS</li>  <li>PROGRAMS</li>  <li>NONE</li> </ul></td>
            <td> <br> Defines valid states of Offline Availability.  <br> MANUAL- Only specified files will be available offline.  <br> DOCUMENTS- All files that users open will be available offline.  <br> PROGRAMS- Program will preferably run from the offline cache even when connected to the network. All files that users open will be available offline.  <br> NONE- Prevents clients from storing documents and programs in offline cache. </td>
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
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the SMB share should exist or not.  <br> present  indicates that the share should exist on the system.  <br> absent  indicates that the share should not exist on the system. </td>
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
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                                                    </table>

### Notes
* When the ID of the filesystem/snapshot is passed then nas_server is not required. If passed, then the filesystem/snapshot should exist for the nas_server, else the task will fail.
* Multiple SMB shares can be created for the same local path.

### Examples
```
- name: Create SMB share for a filesystem
  dellemc_powerstore_smbshare:
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
  dellemc_powerstore_smbshare:
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
  dellemc_powerstore_smbshare:
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
  dellemc_powerstore_smbshare:
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
  dellemc_powerstore_smbshare:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    share_id: "{{smb_share_id}}"
    state: "present"

- name: Delete SMB share
  dellemc_powerstore_smbshare:
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
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
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
                    <td colspan=1 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> ID of filesystem. </td>
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
                    <td colspan=1 > nas_server </td>
                    <td> dict </td>
                    <td>success</td>
                    <td> nas_server of filesystem. </td>
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
                <td colspan=2 > is_branch_cache_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether branch cache is enabled or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > is_continuous_availability_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether the share will be available continuously or not </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > is_encryption_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether encryption is enabled or not </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the SMB share. </td>
            </tr>
                                        </table>

### Authors
* P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

--------------------------------
# Snapshot Module

Manage Snapshots on Dell EMC PowerStore.

### Synopsis
 Managing Snapshots on PowerStore.
 Create a new Volume Group Snapshot.
 Get details of Volume Group Snapshot.
 Modify Volume Group Snapshot
 Delete an existing Volume Group Snapshot.
 Create a new Volume Snapshot.
 Get details of Volume Snapshot.
 Modify Volume Snapshot.
 Delete an existing Volume Snapshot.

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
            <td colspan=1 > snapshot_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the Snapshot. Either snapshot name or ID is required. </td>
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
            <td colspan=1 > volume</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The volume. This could be the volume name or ID. </td>
        </tr>
                    <tr>
            <td colspan=1 > volume_group</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The volume group. This could be the volume group name or ID. </td>
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
            <td colspan=1 > desired_retention</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The retention value for the Snapshot.  <br> If the retention value is not specified, the Snapshot details would be returned.  <br> To create a Snapshot, either a retention or expiration timestamp must be given.  <br> If the Snapshot does not have any retention value - specify it as 'None'. </td>
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
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Defines whether the Snapshot should exist or not. </td>
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
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                                            </table>


### Examples
```
    - name: Create a volume snapshot on PowerStore
      dellemc_powerstore_snapshot:
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
      dellemc_powerstore_snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        volume: "{{volume}}"
        state: "{{state_present}}"

    - name: Rename volume snapshot
      dellemc_powerstore_snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        new_snapshot_name: "{{new_snapshot_name}}"
        volume: "{{volume}}"
        state: "{{state_present}}"

    - name: Delete volume snapshot
      dellemc_powerstore_snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{new_snapshot_name}}"
        volume: "{{volume}}"
        state: "{{state_absent}}"

    - name: Create a volume group snapshot on PowerStore
      dellemc_powerstore_snapshot:
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
      dellemc_powerstore_snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        volume_group: "{{volume_group}}"
        state: "{{state_present}}"

    - name: Modify volume group snapshot expiration timestamp
      dellemc_powerstore_snapshot:
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
      dellemc_powerstore_snapshot:
        array_ip: "{{mgmt_ip}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        snapshot_name: "{{snapshot_name}}"
        new_snapshot_name: "{{new_snapshot_name}}"
        volume_group: "{{volume_group}}"
        state: "{{state_present}}"

    - name: Delete volume group snapshot
      dellemc_powerstore_snapshot:
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
        <th colspan=4>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=4 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=4 > create_vg_snap </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume group snapshot got created </td>
        </tr>
                    <tr>
            <td colspan=4 > create_vol_snap </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume snapshot got created </td>
        </tr>
                    <tr>
            <td colspan=4 > delete_vg_snap </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume group snapshot got deleted </td>
        </tr>
                    <tr>
            <td colspan=4 > delete_vol_snap </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume snapshot got deleted </td>
        </tr>
                    <tr>
            <td colspan=4 > modify_vg_snap </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume group snapshot got modified </td>
        </tr>
                    <tr>
            <td colspan=4 > modify_vol_snap </td>
            <td>  bool </td>
            <td> When value exists </td>
            <td> A boolean flag to indicate whether volume snapshot got modified </td>
        </tr>
                    <tr>
            <td colspan=4 > snap_details </td>
            <td>  complex </td>
            <td> When snapshot exists </td>
            <td> Details of the snapshot </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > creation_timestamp </td>
                <td> str </td>
                <td>success</td>
                <td> The creation timestamp of the snapshot </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Description about the snapshot </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID given to the snapshot </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the snapshot </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > performance_policy_id </td>
                <td> str </td>
                <td>success</td>
                <td> The performance policy for the snapshot </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > protection_data </td>
                <td> complex </td>
                <td>success</td>
                <td> The protection data of the snapshot </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > expiration_timestamp </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The expiration timestamp of the snapshot </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > protection_policy_id </td>
                <td> str </td>
                <td>success</td>
                <td> The protection policy of the snapshot </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > size </td>
                <td> int </td>
                <td>success</td>
                <td> Size of the snapshot </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > state </td>
                <td> str </td>
                <td>success</td>
                <td> The state of the snapshot </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > type </td>
                <td> str </td>
                <td>success</td>
                <td> The type of the snapshot </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > volumes </td>
                <td> complex </td>
                <td>success</td>
                <td> The volumes details of the volume group snapshot </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The system generated ID given to the volume associated with the volume group </td>
                </tr>
                                                                    </table>

### Authors
* Rajshree Khare (@khareRajshree) <ansible.team@dell.com>
* Prashant Rakheja (@prashant-dell) <ansible.team@dell.com>

--------------------------------
# Replication Rule Module

Replication rule operations on a PowerStore storage system.

### Synopsis
 Performs all replication rule operations on a PowerStore Storage System.
 This module supports get details of an existing replication rule.
 Create new replication rule for all supported parameters.
 Modify replication rule with supported parameters.
 Delete a specific replication rule.

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
            <td colspan=1 > replication_rule_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the replication rule.  <br> Required during creation of a replication rule.  <br> replication_rule_name and replication_rule_id are mutually exclusive. </td>
        </tr>
                    <tr>
            <td colspan=1 > replication_rule_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> ID of the replication rule.  <br> ID for the rule is autogenerated, cannot be passed during creation of a replication rule.  <br> replication_rule_name and replication_rule_id are mutually exclusive. </td>
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
            <td colspan=1 > rpo</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>Five_Minutes</li>  <li>Fifteen_Minutes</li>  <li>Thirty_Minutes</li>  <li>One_Hour</li>  <li>Six_Hours</li>  <li>Twelve_Hours</li>  <li>One_Day</li> </ul></td>
            <td> <br> Recovery point objective (RPO), which is the acceptable amount of data, measured in units of time, that may be lost in case of a failure. </td>
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
            <td colspan=1 > remote_system</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> ID or name of the remote system to which this rule will replicate the associated resources. </td>
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
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                                            </table>


### Examples
```
- name: Create new replication rule
  dellemc_powerstore_replicationrule:
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
  dellemc_powerstore_replicationrule:
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
  dellemc_powerstore_replicationrule:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    replication_rule_id: "{{id}}"
    state: "present"

- name: Delete an existing replication rule
  dellemc_powerstore_replicationrule:
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
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=2 > replication_rule_details </td>
            <td>  complex </td>
            <td> When replication rule exists </td>
            <td> Details of the replication rule </td>
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
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID of the replication rule </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the replication rule </td>
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
                <td colspan=1 > rpo </td>
                <td> str </td>
                <td>success</td>
                <td> Recovery point objective (RPO), which is the acceptable amount of data, measured in units of time, that may be lost in case of a failure. </td>
            </tr>
                                        </table>

### Authors
* P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

--------------------------------
# Protection Policy Module

Perform Protection policy operations on PowerStore storage system

### Synopsis
 Performs all protection policy operations on PowerStore Storage System.
 This modules supports get details of an existing protection policy.
 Create new protection policy with existing Snapshot Rule or replication rule.
 Modify protection policy to change the name and description, and add or remove existing snapshot rules/ replication rule.
 Delete an existing protection policy.

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
            <td colspan=1 > name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> String variable. Indicates the name of the protection policy. </td>
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
            <td colspan=1 > new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> String variable. Indicates the new name of the protection policy.  <br> Used for renaming operation </td>
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
            <td colspan=1 > replicationrule</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name or ids of the replcation rule which is to be added to the protection policy.  <br> To remove the replication rule, an empty string has to be passed. </td>
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
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> String variable. Indicates the state of protection policy.  <br> For Delete operation only, it should be set to "absent"  <br> For all other operations like Create, Modify or Get details, it should be set to "present" </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshotrule_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-policy</li>  <li>absent-in-policy</li> </ul></td>
            <td> <br> String variable. Indicates the state of a snapshotrule in a protection policy.  <br> When snapshot rules are specified, this variable is required.  <br> present-in-policy indicates to add to protection policy.  <br> absent-in-policy indicates to remove from protection policy. </td>
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
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                                                    </table>

### Notes
* Before deleting a protection policy, the replication rule has to be removed from the protection policy.

### Examples
```
- name: Create a protection policy with snapshot rule and replication rule
  dellemc_powerstore_protectionpolicy:
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
  dellemc_powerstore_protectionpolicy:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    new_name: "{{new_name}}"
    state: "present"


- name : Modify protection policy, add snapshot rule
  dellemc_powerstore_protectionpolicy:
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
  dellemc_powerstore_protectionpolicy:
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
  dellemc_powerstore_protectionpolicy:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    state: "present"

- name : Get details of protection policy by ID
  dellemc_powerstore_protectionpolicy:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    protectionpolicy_id: "{{protectionpolicy_id}}"
    state: "present"

- name : Delete protection policy
  dellemc_powerstore_protectionpolicy:
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
            <td colspan=4 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=4 > protectionpolicy_details </td>
            <td>  complex </td>
            <td> When protection policy exists </td>
            <td> Details of the protection policy </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > description </td>
                <td> str </td>
                <td>success</td>
                <td> description about the protection policy </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID given to the protection policy </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the protection policy </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > replication_rules </td>
                <td> complex </td>
                <td>success</td>
                <td> The replication rule details of the protection policy </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The replication rule ID of the protection policy </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The replication rule name of the protection policy </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > snapshot_rules </td>
                <td> complex </td>
                <td>success</td>
                <td> The snapshot rules details of the protection policy </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The snapshot rule ID of the protection policy </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The snapshot rule name of the protection policy </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > type </td>
                <td> str </td>
                <td>success</td>
                <td> The type for the protection policy </td>
            </tr>
                                        </table>

### Authors
* Arindam Datta (@dattaarindam) <ansible.team@dell.com>
* P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

--------------------------------
# Filesystem Snapshot Module

Manage Filesystem Snapshots on Dell EMC PowerStore

### Synopsis
 Managing filesystem snapshots on PowerStore Storage System includes creating new filesystem snapshot, getting details of filesystem snapshot, modifying attributes of filesystem snapshot and deleting filesystem snapshot.

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
            <td colspan=1 > snapshot_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the filesystem snapshot.  <br> Mandatory for create operation.  <br> Specify either snapshot name or ID (but not both) for any operation. </td>
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
            <td colspan=1 > filesystem</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID/Name of the filesystem for which snapshot will be taken.  <br> If filesystem name is specified, then nas_server is required to uniquely identify the filesystem.  <br> Mandatory for create operation. </td>
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
            <td colspan=1 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The description for the filesystem snapshot. </td>
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
            <td colspan=1 > retention_unit</td>
            <td> str  </td>
            <td></td>
            <td> hours </td>
            <td> <ul> <li>hours</li>  <li>days</li> </ul></td>
            <td> <br> The unit for retention. </td>
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
            <td colspan=1 > access_type</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>SNAPSHOT</li>  <li>PROTOCOL</li> </ul></td>
            <td> <br> Specifies whether the snapshot directory or protocol access is granted to the filesystem snapshot.  <br> For create operation, if access_type is not specified, snapshot will be created with 'SNAPSHOT' access type. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the filesystem snapshot should exist or not. </td>
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
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerStore host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerStore host. </td>
        </tr>
                                            </table>


### Examples
```
- name: Create filesystem snapshot
  dellemc_powerstore_filesystem_snapshot:
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
  dellemc_powerstore_filesystem_snapshot:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      snapshot_id: "{{fs_snapshot_id}}"
      state: "present"

- name: Modify the filesystem snapshot
  dellemc_powerstore_filesystem_snapshot:
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
  dellemc_powerstore_filesystem_snapshot:
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
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=3 > create_fs_snap </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has created </td>
        </tr>
                    <tr>
            <td colspan=3 > delete_fs_snap </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has deleted </td>
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
                <td colspan=2 > creation_timestamp </td>
                <td> str </td>
                <td>success</td>
                <td> The date and time the snapshot was created. </td>
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
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the snapshot. </td>
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
                <td colspan=2 > parent_id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the filesystem on which snapshot is taken. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > parent_name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the filesystem on which snapshot is taken. </td>
            </tr>
                                        <tr>
            <td colspan=3 > modify_fs_snap </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has modified </td>
        </tr>
                    </table>

### Authors
* Akash Shendge (@shenda1) <ansible.team@dell.com>

--------------------------------
