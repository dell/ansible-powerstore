.. _volume_module:


volume -- Manage volumes on a PowerStore storage system
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing volume on PowerStore storage system includes create volume, get details of volume, modify volume attributes, map or unmap volume to host/host group, and delete volume.

Volume module also supports start or end of a metro configuration for a volume, clone, refresh and restore a volume.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.6.0.0 or later.
- PyPowerStore 3.4.1.
- Ansible-core 2.17 or later.
- Python 3.11, 3.12 or 3.13.



Parameters
----------

  appliance_id (optional, str, None)
    ID of the appliance on which the volume is provisioned.

    :emphasis:`appliance\_id` and :emphasis:`appliance\_name` are mutually exclusive.


  appliance_name (optional, str, None)
    Name of the appliance on which the volume is provisioned.

    :emphasis:`appliance\_id` and :emphasis:`appliance\_name` are mutually exclusive.


  app_type (optional, str, None)
    Application type to indicate the intended use of the volume.


  app_type_other (optional, str, None)
    Application type for volume when :emphasis:`app\_type` is set to :literal:`\*Other` types.


  backup_snap_profile (optional, dict, None)
    Details of the backup snapshot set to be created.


    description (optional, str, None)
      Description of the backup snapshot set.


    expiration_timestamp (optional, str, None)
      Time after which the snapshot set can be auto-purged.


    name (optional, str, None)
      Name of the backup snapshot set to be created.

      The default name of the volume snapshot is the date and time when the snapshot is taken.


    performance_policy (optional, str, None)
      Performance policy assigned to the snapshot.



  cap_unit (optional, str, None)
    Volume size unit.

    Used to signify unit of the size provided for creation and expansion of volume.

    It defaults to :literal:`GB`\ , if not specified.


  clone_volume (optional, dict, None)
    Details of the volume clone.


    description (optional, str, None)
      Description of the clone.


    host (optional, str, None)
      Unique identifier or name of the host to be attached to the clone.


    host_group (optional, str, None)
      Unique identifier or name of the host group to be attached to the clone.


    logical_unit_number (optional, int, None)
      logical unit number when creating a :literal:`mapped` volume.

      If no :literal:`host\_id` or :literal:`host\_group\_id` is specified, :literal:`logical\_unit\_number` is ignored.


    name (optional, str, None)
      Name of the clone set to be created.


    performance_policy (optional, str, None)
      The performance policy of the clone set to be created.


    protection_policy (optional, str, None)
      The protection policy of the clone set to be created.



  create_backup_snap (optional, bool, None)
    Indicates whether a backup snapshot of the target volume will be created or not.


  delete_remote_volume (optional, bool, None)
    Whether to delete the remote volume during removal of metro session.

    This is parameter is added in the PowerStore version 3.0.0.0.


  description (optional, str, None)
    Description for the volume.

    Optional parameter when creating a volume.

    To modify, pass the new value in description field.


  end_metro_config (optional, bool, False)
    Whether to end the metro session from a volume.

    This is mandatory for end metro configuration operation.


  hlu (optional, int, None)
    Logical unit number for the host/host group volume access.

    Optional parameter when mapping a volume to host/host group.

    HLU modification is not supported.


  host (optional, str, None)
    Host to be mapped/unmapped to a volume. If not specified, an unmapped volume is created. Only one of the host or host group can be supplied in one call.

    To represent host, both name or ID can be used interchangeably. The module will detect both.


  hostgroup (optional, str, None)
    Hostgroup to be mapped/unmapped to a volume. If not specified, an unmapped volume is created.

    Only one of the host or host group can be mapped in one call.

    To represent a hostgroup, both name or ID can be used interchangeably. The module will detect both.


  mapping_state (optional, str, None)
    Define whether the volume should be mapped to a host or hostgroup.

    Value :literal:`mapped` - indicates that the volume should be mapped to the host or host group.

    Value :literal:`unmapped` - indicates that the volume should not be mapped to the host or host group.

    Only one of a host or host group can be supplied in one call.


  new_name (optional, str, None)
    The new volume name for the volume, used in case of rename functionality.


  performance_policy (optional, str, None)
    The :emphasis:`performance\_policy` for the volume.

    A volume can be assigned a performance policy at the time of creation of the volume, or later.

    The policy can also be changed for a given volume, by simply passing the new value.

    Check examples for more clarity.

    If not given, performance policy will be :literal:`medium`.


  protection_policy (optional, str, None)
    The :emphasis:`protection\_policy` of the volume.

    To represent policy, both name or ID can be used interchangably. The module will detect both.

    A volume can be assigned a protection policy at the time of creation of the volume or later.

    The policy can also be changed for a given volume by simply passing the new value.

    The policy can be removed by passing an empty string.

    Check examples for more clarity.


  remote_appliance_id (optional, str, None)
    A remote system appliance ID to which volume will be assigned.

    This parameter is added in PowerStore version 3.0.0.0.


  remote_system (optional, str, None)
    The remote system to which metro relationship will be established.

    The remote system must support metro volume.

    This is mandatory while configuring a metro volume.

    To represent remote system, both name and ID are interchangeable.

    This parameter is added in PowerStore version 3.0.0.0.


  size (optional, float, None)
    Size of the volume. Minimum volume size is 1MB. Maximum volume size is 256TB. Size must be a multiple of 8192.

    Required in case of create and expand volume.


  source_snap (optional, str, None)
    Unique identifier or name of the source snapshot that will be used for the restore operation.


  source_volume (optional, str, None)
    Unique identifier or name of the volume to refresh from.


  state (optional, str, present)
    Define whether the volume should exist or not.

    Value :literal:`present` - indicates that the volume should exist on the system.

    Value :literal:`absent` - indicates that the volume should not exist on the system.


  vg_name (optional, str, None)
    The name of the volume group. A volume can optionally be assigned to a volume group at the time of creation.

    Use the Volume Group Module for modification of the assignment.


  vol_id (optional, str, None)
    The 36 character long ID of the volume, automatically generated when a volume is created.

    Cannot be used while creating a volume. All other functionalities on a volume are supported using volume name or ID.


  vol_name (optional, str, None)
    Unique name of the volume. This value must contain 128 or fewer printable unicode characters.

    Required when creating a volume. All other functionalities on a volume are supported using volume name or ID.


  array_ip (True, str, None)
    IP or FQDN of the PowerStore management system.


  validate_certs (optional, bool, True)
    Boolean variable to specify whether to validate SSL certificate or not.

    :literal:`true` - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS\_CA\_BUNDLE to the path of the SSL certificate.

    :literal:`false` - indicates that the SSL certificate should not be verified.


  user (True, str, None)
    The username of the PowerStore host.


  password (True, str, None)
    The password of the PowerStore host.


  timeout (optional, int, 120)
    Time after which the connection will get terminated.

    It is to be mentioned in seconds.


  port (optional, int, None)
    Port number for the PowerStore array.

    If not passed, it will take 443 as default.





Notes
-----

.. note::
   - To create a new volume, :emphasis:`vol\_name` and :emphasis:`size` is required. :emphasis:`cap\_unit`\ , :emphasis:`description`\ , :emphasis:`vg\_name`\ , :emphasis:`performance\_policy`\ , and :emphasis:`protection\_policy` are optional.
   - Parameter :emphasis:`new\_name` should not be provided when creating a new volume.
   - The :emphasis:`size`\ is a required parameter for expand volume.
   - Clones or Snapshots of a deleted production volume or a clone are not deleted.
   - A volume that is attached to a host/host group, or that is part of a volume group cannot be deleted.
   - If volume in metro session, volume can only be modified, refreshed and restored when session is in the pause state.
   - :emphasis:`performance\_policy` and :emphasis:`host\_group` details are not in the return values for PowerStore 4.0.0.0.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create volume
      dellemc.powerstore.volume:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        vol_name: "{{vol_name}}"
        size: 5
        cap_unit: "{{cap_unit}}"
        state: 'present'
        description: 'Description'
        performance_policy: 'low'
        protection_policy: 'protection_policy_name'
        vg_name: "{{vg_name}}"
        mapping_state: 'mapped'
        host: "{{host_name}}"
        app_type: "Relational_Databases_Other"
        app_type_other: "MaxDB"
        appliance_name: "Appliance_Name"

    - name: Get volume details using ID
      dellemc.powerstore.volume:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        vol_id: "{{result.volume_details.id}}"
        state: "present"

    - name: Modify volume size, name, description, protection,  performance policy and app_type
      dellemc.powerstore.volume:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        new_name: "{{new_name}}"
        vol_name: "{{vol_name}}"
        state: "present"
        size: 2
        performance_policy: 'high'
        description: 'new description'
        protection_policy: ''
        app_type: "Business_Applications_CRM"

    - name: Map volume to a host with HLU
      dellemc.powerstore.volume:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        vol_name: "{{vol_name}}"
        state: 'present'
        mapping_state: 'mapped'
        host: 'host1'
        hlu: 12

    - name: Clone a volume
      dellemc.powerstore.volume:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        vol_name: "{{vol_name}}"
        clone_volume:
          name: 'test_name'
          description: 'test description'
          host: 'test_host'
          host_group: 'test_host_group'
          logical_unit_number: 1
          protection_policy: 'TEST_PP'
          performance_policy: 'low'
        state: "present"

    - name: Refresh a volume
      dellemc.powerstore.volume:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        vol_name: "{{vol_name}}"
        source_volume_name: 'test1'
        create_backup_snap: true
        backup_snap_profile:
          name: 'refresh_backup_snap'
          description: 'test refresh_backup_snap'
          expiration_timestamp: '2022-12-23T01:20:00Z'
          performance_policy: 'low'
        state: "present"

    - name: Restore a volume
      dellemc.powerstore.volume:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        vol_name: "{{vol_name}}"
        source_snap: 'refresh_backup_snap'
        create_backup_snap: true
        backup_snap_profile:
          name: 'restore_snap_2'
          description: 'test backup snap'
          expiration_timestamp: '2022-12-23T01:20:00Z'
          performance_policy: 'low'
        state: "present"

    - name: Configure a metro volume
      dellemc.powerstore.volume:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        vol_name: "{{vol_name}}"
        remote_system: "remote-D123"
        state: "present"

    - name: End a metro volume configuration
      dellemc.powerstore.volume:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        vol_name: "{{vol_name}}"
        end_metro_config: true
        delete_remote_volume: true
        state: "present"

    - name: Delete volume
      dellemc.powerstore.volume:
        array_ip: "{{array_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        vol_id: "{{result.volume_details.id}}"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


is_volume_cloned (always, bool, false)
  Whether or not the clone of volume is created.


is_volume_refreshed (always, bool, false)
  Whether or not the volume is refreshed.


is_volume_restored (always, bool, false)
  Whether or not the volume is restored.


volume_details (When volume exists, complex, {'appliance_id': 'A1', 'creation_timestamp': '2022-01-06T05:41:59.381459+00:00', 'description': 'Volume created', 'hlu_details': [], 'host': [], 'host_group': [], 'id': '634e4b95-e7bd-49e7-957b-6dc932642464', 'is_replication_destination': False, 'location_history': None, 'mapped_volumes': [], 'migration_session_id': None, 'name': 'sample_volume', 'nguid': 'nguid.ac8ab0e2506d99be8ccf096800e29e40', 'node_affinity': 'System_Select_At_Attach', 'node_affinity_l10n': 'System Select At Attach', 'nsid': 54768, 'performance_policy': {'id': 'default_medium', 'name': 'Medium'}, 'performance_policy_id': 'default_medium', 'protection_data': {'copy_signature': None, 'created_by_rule_id': None, 'created_by_rule_name': None, 'creator_type': 'User', 'creator_type_l10n': 'User', 'expiration_timestamp': None, 'family_id': '634e4b95-e7bd-49e7-957b-6dc932642464', 'is_app_consistent': False, 'parent_id': None, 'source_id': None, 'source_timestamp': None}, 'protection_policy': {'id': '4bbb6333-59e4-489c-9015-c618d3e8384b', 'name': 'sample_protection_policy'}, 'snapshots': [{'id': '2a07be43-xxxx-4fd0-xxxx-18eaa4081bd9', 'name': 'sample_snap_2'}], 'protection_policy_id': '4bbb6333-59e4-489c-9015-c618d3e8384b', 'size': 1073741824, 'state': 'Ready', 'state_l10n': 'Ready', 'type': 'Primary', 'type_l10n': 'Primary', 'volume_groups': [], 'wwn': 'naa.68ccf09800ac8ab0e2506d99bee29e40'})
  Details of the volume.


  app_type (, str, )
    Application type indicating the intended use of the volume.


  app_type_other (, str, )
    Application type for volume when app\_type is set to \*Other.


  id (, str, )
    The system generated ID given to the volume.


  name (, str, )
    Name of the volume.


  size (, int, )
    Size of the volume.


  description (, str, )
    description about the volume.


  performance_policy_id (, str, )
    The performance policy for the volume.


  protection_policy_id (, str, )
    The protection policy of the volume.


  appliance_id (, str, )
    ID of appliance on which the volume is provisioned.


  appliance_name (, str, )
    Name of appliance on which the volume is provisioned.


  snapshots (, complex, )
    List of snapshot associated with the volume.


    id (, str, )
      The system generated ID given to the snapshot.


    name (, str, )
      Name of the snapshot.



  volume_groups (, complex, )
    The volume group details of the volume.


    id (, str, )
      The system generated ID given to the volume group.


    name (, str, )
      Name of the volume group.



  host (, complex, )
    Hosts details mapped to the volume.


    id (, str, )
      The Host ID mapped to the volume.


    name (, str, )
      Name of the Host mapped to the volume.



  host_group (, complex, )
    Host groups details mapped to the volume.


    id (, str, )
      The Host group ID mapped to the volume.


    name (, str, )
      Name of the Host group mapped to the volume.



  hlu_details (, complex, )
    HLU details for mapped host/host group.


    host_group_id (, str, )
      The Host group ID mapped to the volume.


    host_id (, str, )
      The Host ID mapped to the volume.


    id (, str, )
      The HLU ID.


    logical_unit_number (, int, )
      Logical unit number for the host/host group volume access.



  wwn (, str, )
    The world wide name of the volume.


  nsid (, int, )
    NVMe Namespace unique identifier in the NVME subsystem. Used for volumes attached to NVMEoF hosts.


  nguid (, int, )
    NVMe Namespace globally unique identifier. Used for volumes attached to NVMEoF hosts.


  node_affinity (, str, )
    This attribute shows which node will be advertised as the optimized IO path to the volume.


  metro_replication_session_id (, str, )
    The ID of the metro replication session assigned to volume.


  mapped_volumes (, complex, )
    This is the inverse of the resource type host\_volume\_mapping association.


    id (, str, )
      Unique identifier of a mapping between a host and a volume.


    logical_unit_number (, int, )
      Logical unit number for the host volume access.







Status
------





Authors
~~~~~~~

- Ambuj Dubey (@AmbujDube) <ansible.team@dell.com>
- Manisha Agrawal (@agrawm3) <ansible.team@dell.com>
- Ananthu S Kuttattu (@kuttattz) <ansible.team@dell.com>
- Bhavneet Sharma (@Bhavneet-Sharma) <ansible.team@dell.com>
- Pavan Mudunuri(@Pavan-Mudunuri) <ansible.team@dell.com>
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>

