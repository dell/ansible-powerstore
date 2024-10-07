#!/usr/bin/python
# Copyright: (c) 2024, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: volume
version_added: '1.0.0'
short_description:  Manage volumes on a PowerStore storage system
description:
- Managing volume on PowerStore storage system includes create volume, get
  details of volume, modify volume attributes, map or unmap volume to
  host/host group, and delete volume.
- Volume module also supports start or end of a metro configuration for a
  volume, clone, refresh and restore a volume.
author:
- Ambuj Dubey (@AmbujDube) <ansible.team@dell.com>
- Manisha Agrawal (@agrawm3) <ansible.team@dell.com>
- Ananthu S Kuttattu (@kuttattz) <ansible.team@dell.com>
- Bhavneet Sharma (@Bhavneet-Sharma) <ansible.team@dell.com>
- Pavan Mudunuri(@Pavan-Mudunuri) <ansible.team@dell.com>
extends_documentation_fragment:
  - dellemc.powerstore.powerstore
options:
  vol_name:
    description:
    - Unique name of the volume. This value must contain 128 or fewer
      printable unicode characters.
    - Required when creating a volume. All other functionalities on a volume
      are supported using volume name or ID.
    type: str
  vg_name:
    description:
    - The name of the volume group. A volume can optionally be assigned to a
      volume group at the time of creation.
    - Use the Volume Group Module for modification of the assignment.
    type: str
  vol_id:
    description:
    - The 36 character long ID of the volume, automatically generated
      when a volume is created.
    - Cannot be used while creating a volume. All other functionalities on a
      volume are supported using volume name or ID.
    type: str
  size:
    description:
    - Size of the volume. Minimum volume size is 1MB. Maximum volume size is
      256TB. Size must be a multiple of 8192.
    - Required in case of create and expand volume.
    type: float
  cap_unit:
    description:
    - Volume size unit.
    - Used to signify unit of the size provided for creation and expansion of
      volume.
    - It defaults to C(GB), if not specified.
    choices: [MB, GB, TB]
    type: str
  new_name:
    description:
    - The new volume name for the volume, used in case of rename
      functionality.
    type: str
  description:
    description:
    - Description for the volume.
    - Optional parameter when creating a volume.
    - To modify, pass the new value in description field.
    type: str
  app_type:
    description:
    - Application type to indicate the intended use of the volume.
    choices: [Relational_Databases_Other, Relational_Databases_Oracle,
      Relational_Databases_SQL_Server, Relational_Databases_PostgreSQL,
      Relational_Databases_MySQL, Relational_Databases_IBM_DB2,
      Big_Data_Analytics_Other, Big_Data_Analytics_MongoDB,
      Big_Data_Analytics_Cassandra, Big_Data_Analytics_SAP_HANA,
      Big_Data_Analytics_Spark, Big_Data_Analytics_Splunk,
      Big_Data_Analytics_ElasticSearch, Business_Applications_Other,
      Business_Applications_ERP_SAP, Business_Applications_CRM,
      Business_Applications_Exchange, Business_Applications_Sharepoint,
      Healthcare_Other, Healthcare_Epic, Healthcare_MEDITECH,
      Healthcare_Allscripts, Healthcare_Cerner, Virtualization_Other,
      Virtualization_Virtual_Servers_VSI, Virtualization_Containers_Kubernetes,
      Virtualization_Virtual_Desktops_VDI, Other]
    type: str
  app_type_other:
    description:
    - Application type for volume when I(app_type) is set to C(*Other) types.
    type: str
  appliance_id:
    description:
    - ID of the appliance on which the volume is provisioned.
    - I(appliance_id) and I(appliance_name) are mutually exclusive.
    type: str
  appliance_name:
    description:
    - Name of the appliance on which the volume is provisioned.
    - I(appliance_id) and I(appliance_name) are mutually exclusive.
    type: str
  protection_policy:
    description:
    - The I(protection_policy) of the volume.
    - To represent policy, both name or ID can be used interchangably.
      The module will detect both.
    - A volume can be assigned a protection policy at the time of creation of the
      volume or later.
    - The policy can also be changed for a given volume by simply passing the
      new value.
    - The policy can be removed by passing an empty string.
    - Check examples for more clarity.
    type: str
  performance_policy:
    description:
    - The I(performance_policy) for the volume.
    - A volume can be assigned a performance policy at the time of creation of
      the volume, or later.
    - The policy can also be changed for a given volume, by simply passing the
      new value.
    - Check examples for more clarity.
    - If not given, performance policy will be C(medium).
    choices: [high, medium, low]
    type: str
  host:
    description:
    - Host to be mapped/unmapped to a volume. If not specified, an unmapped
      volume is created. Only one of the host or host group can be supplied in
      one call.
    - To represent host, both name or ID can be used interchangeably.
      The module will detect both.
    type: str
  hostgroup:
    description:
    - Hostgroup to be mapped/unmapped to a volume. If not specified, an
      unmapped volume is created.
    - Only one of the host or host group can be mapped in one call.
    - To represent a hostgroup, both name or ID can be used interchangeably.
      The module will detect both.
    type: str
  mapping_state:
    description:
    - Define whether the volume should be mapped to a host or hostgroup.
    - Value C(mapped) - indicates that the volume should be mapped to the host
      or host group.
    - Value C(unmapped) - indicates that the volume should not be mapped to the
      host or host group.
    - Only one of a host or host group can be supplied in one call.
    choices: [mapped, unmapped]
    type: str
  hlu:
    description:
    - Logical unit number for the host/host group volume access.
    - Optional parameter when mapping a volume to host/host group.
    - HLU modification is not supported.
    type: int
  clone_volume:
    description:
    - Details of the volume clone.
    type: dict
    suboptions:
      name:
        description:
        - Name of the clone set to be created.
        type: str
      description:
        description:
        - Description of the clone.
        type: str
      host:
        description:
        - Unique identifier or name of the host to be attached to the clone.
        type: str
      host_group:
        description:
        - Unique identifier or name of the host group to be attached to the clone.
        type: str
      logical_unit_number:
        description:
        - logical unit number when creating a C(mapped) volume.
        - If no C(host_id) or C(host_group_id) is specified, C(logical_unit_number) is ignored.
        type: int
      protection_policy:
        description:
        - The protection policy of the clone set to be created.
        type: str
      performance_policy:
        description:
        - The performance policy of the clone set to be created.
        choices: ['high', 'medium', 'low']
        type: str
  source_volume:
    description:
    - Unique identifier or name of the volume to refresh from.
    type: str
  source_snap:
    description:
    - Unique identifier or name of the source snapshot that will be used for the restore operation.
    type: str
  create_backup_snap:
    description:
    - Indicates whether a backup snapshot of the target volume will be created or not.
    type: bool
  backup_snap_profile:
    description:
    - Details of the backup snapshot set to be created.
    type: dict
    suboptions:
      name:
        description:
        - Name of the backup snapshot set to be created.
        - The default name of the volume snapshot is the date and time when the snapshot is taken.
        type: str
      description:
        description:
        - Description of the backup snapshot set.
        type: str
      performance_policy:
        description:
        - Performance policy assigned to the snapshot.
        choices: ['high', 'medium', 'low']
        type: str
      expiration_timestamp:
        description:
        - Time after which the snapshot set can be auto-purged.
        type: str
  state:
    description:
    - Define whether the volume should exist or not.
    - Value C(present) - indicates that the volume should exist on the system.
    - Value C(absent) - indicates that the volume should not exist on the system.
    required: true
    choices: [absent, present]
    type: str
  remote_system:
    description:
    - The remote system to which metro relationship will be established.
    - The remote system must support metro volume.
    - This is mandatory while configuring a metro volume.
    - To represent remote system, both name and ID are interchangeable.
    - This parameter is added in PowerStore version 3.0.0.0.
    type: str
  remote_appliance_id:
    description:
    - A remote system appliance ID to which volume will be assigned.
    - This parameter is added in PowerStore version 3.0.0.0.
    type: str
  end_metro_config:
    description:
    - Whether to end the metro session from a volume.
    - This is mandatory for end metro configuration operation.
    type: bool
    default: false
  delete_remote_volume:
    description:
    - Whether to delete the remote volume during removal of metro session.
    - This is parameter is added in the PowerStore version 3.0.0.0.
    type: bool

notes:
- To create a new volume, I(vol_name) and I(size) is required. I(cap_unit),
  I(description), I(vg_name), I(performance_policy), and I(protection_policy) are
  optional.
- Parameter I(new_name) should not be provided when creating a new volume.
- The I(size)is a required parameter for expand volume.
- Clones or Snapshots of a deleted production volume or a clone are not
  deleted.
- A volume that is attached to a host/host group, or that is part of a volume
  group cannot be deleted.
- If volume in metro session, volume can only be modified, refreshed and
  restored when session is in the pause state.
- The I(Check_mode) is not supported.
- I(performance_policy) and I(host_group) details are not in the return values for
  PowerStore 4.0.0.0.
'''

EXAMPLES = r'''
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
'''

RETURN = r'''

changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"
is_volume_cloned:
    description: Whether or not the clone of volume is created.
    returned: always
    type: bool
    sample: "false"
is_volume_refreshed:
    description: Whether or not the volume is refreshed.
    returned: always
    type: bool
    sample: "false"
is_volume_restored:
    description: Whether or not the volume is restored.
    returned: always
    type: bool
    sample: "false"
volume_details:
    description: Details of the volume.
    returned: When volume exists
    type: complex
    contains:
        app_type:
            description: Application type indicating the intended use of the volume.
            type: str
        app_type_other:
            description: Application type for volume when app_type is set to *Other.
            type: str
        id:
            description: The system generated ID given to the volume.
            type: str
        name:
            description: Name of the volume.
            type: str
        size:
            description: Size of the volume.
            type: int
        description:
            description: description about the volume.
            type: str
        performance_policy_id:
            description: The performance policy for the volume.
            type: str
        protection_policy_id:
            description: The protection policy of the volume.
            type: str
        appliance_id:
            description: ID of appliance on which the volume is provisioned.
            type: str
        appliance_name:
            description: Name of appliance on which the volume is provisioned.
            type: str
        snapshots:
            description: List of snapshot associated with the volume.
            type: complex
            contains:
                id:
                    description: The system generated ID given to the snapshot.
                    type: str
                name:
                    description: Name of the snapshot.
                    type: str
        volume_groups:
            description: The volume group details of the volume.
            type: complex
            contains:
                id:
                    description: The system generated ID given to the volume
                                 group.
                    type: str
                name:
                    description: Name of the volume group.
                    type: str
        host:
            description: Hosts details mapped to the volume.
            type: complex
            contains:
                id:
                    description: The Host ID mapped to the volume.
                    type: str
                name:
                    description: Name of the Host mapped to the volume.
                    type: str
        host_group:
            description: Host groups details mapped to the volume.
            type: complex
            contains:
                id:
                    description: The Host group ID mapped to the volume.
                    type: str
                name:
                    description: Name of the Host group mapped to the volume.
                    type: str
        hlu_details:
            description: HLU details for mapped host/host group.
            type: complex
            contains:
                host_group_id:
                    description: The Host group ID mapped to the volume.
                    type: str
                host_id:
                    description: The Host ID mapped to the volume.
                    type: str
                id:
                    description: The HLU ID.
                    type: str
                logical_unit_number:
                    description: Logical unit number for the host/host group
                                 volume access.
                    type: int
        wwn:
            description: The world wide name of the volume.
            type: str
        nsid:
            description: NVMe Namespace unique identifier in the NVME
                         subsystem. Used for volumes attached to NVMEoF hosts.
            type: int
        nguid:
            description: NVMe Namespace globally unique identifier. Used for
                         volumes attached to NVMEoF hosts.
            type: int
        node_affinity:
            description: This attribute shows which node will be advertised as
                         the optimized IO path to the volume.
            type: str
        metro_replication_session_id:
            description: The ID of the metro replication session assigned to
                         volume.
            type: str
        mapped_volumes:
            description: This is the inverse of the resource type
                         host_volume_mapping association.
            type: complex
            contains:
                id:
                    description: Unique identifier of a mapping between
                                 a host and a volume.
                    type: str
                logical_unit_number:
                    description: Logical unit number for the host volume
                                 access.
                    type: int
    sample: {
        "appliance_id": "A1",
        "creation_timestamp": "2022-01-06T05:41:59.381459+00:00",
        "description": "Volume created",
        "hlu_details": [],
        "host": [],
        "host_group": [],
        "id": "634e4b95-e7bd-49e7-957b-6dc932642464",
        "is_replication_destination": false,
        "location_history": null,
        "mapped_volumes": [],
        "migration_session_id": null,
        "name": "sample_volume",
        "nguid": "nguid.ac8ab0e2506d99be8ccf096800e29e40",
        "node_affinity": "System_Select_At_Attach",
        "node_affinity_l10n": "System Select At Attach",
        "nsid": 54768,
        "performance_policy": {
            "id": "default_medium",
            "name": "Medium"
        },
        "performance_policy_id": "default_medium",
        "protection_data": {
            "copy_signature": null,
            "created_by_rule_id": null,
            "created_by_rule_name": null,
            "creator_type": "User",
            "creator_type_l10n": "User",
            "expiration_timestamp": null,
            "family_id": "634e4b95-e7bd-49e7-957b-6dc932642464",
            "is_app_consistent": false,
            "parent_id": null,
            "source_id": null,
            "source_timestamp": null
        },
        "protection_policy": {
            "id": "4bbb6333-59e4-489c-9015-c618d3e8384b",
            "name": "sample_protection_policy"
        },
        "snapshots": [
            {
                "id": "2a07be43-xxxx-4fd0-xxxx-18eaa4081bd9",
                "name": "sample_snap_2"
            }
        ],
        "protection_policy_id": 4bbb6333-59e4-489c-9015-c618d3e8384b,
        "size": 1073741824,
        "state": "Ready",
        "state_l10n": "Ready",
        "type": "Primary",
        "type_l10n": "Primary",
        "volume_groups": [],
        "wwn": "naa.68ccf09800ac8ab0e2506d99bee29e40"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import utils
import logging

LOG = utils.get_logger('volume', log_devel=logging.INFO)

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']


class PowerStoreVolume(object):
    """Class with volume operations"""

    def __init__(self):
        """ Define all parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_volume_parameters())

        mutually_exclusive = [['vol_name', 'vol_id'], ['appliance_name', 'appliance_id']]
        required_one_of = [['vol_name', 'vol_id']]
        required_by = {
            'app_type_other': 'app_type',
        }

        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mutually_exclusive,
            required_one_of=required_one_of,
            required_by=required_by
        )

        LOG.info('HAS_PY4PS = %s , IMPORT_ERROR = %s', HAS_PY4PS,
                 IMPORT_ERROR)
        if not HAS_PY4PS:
            self.module.fail_json(msg=IMPORT_ERROR)
        LOG.info('IS_SUPPORTED_PY4PS_VERSION = %s , VERSION_ERROR = %s',
                 IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR)
        if not IS_SUPPORTED_PY4PS_VERSION:
            self.module.fail_json(msg=VERSION_ERROR)

        # result is a dictionary that contains changed status and
        # volume details
        self.result = {"changed": False, "volume_details": {}}
        self.conn = utils.get_powerstore_connection(
            self.module.params)
        self.provisioning = self.conn.provisioning
        self.protection = self.conn.protection
        self.configuration = self.conn.config_mgmt
        self.performance_policy_dict = {
            'low': 'default_low',
            'medium': 'default_medium',
            'high': 'default_high'
        }
        LOG.info('Got Py4Ps instance for provisioning and protection on '
                 'PowerStore %s', self.conn)

    def get_volume(self, vol_id=None, vol_name=None):
        """Get volume details"""
        try:
            if vol_id is not None:
                return self.provisioning.get_volume_details(vol_id)
            else:
                volume_info = self.provisioning.get_volume_by_name(vol_name)
                if volume_info:
                    if len(volume_info) > 1:
                        error_msg = 'Multiple volumes by the same name found'
                        LOG.error(error_msg)
                        self.module.fail_json(msg=error_msg)
                    return volume_info[0]
                return None
        except Exception as e:
            error_msg = "Got error {0} while getting details of volume"\
                .format(str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(error_msg)
                return None
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def update_volume_details(self, volume_info):
        try:
            appliance_id = volume_info['appliance_id']
            volume_info['appliance_name'] = self.configuration.get_appliance_details(appliance_id)['name']
            return volume_info['appliance_name']

        except Exception as e:
            error_msg = f"Failed to update volume details with appliance name {e}"
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def create_volume(self, vol_name,
                      size,
                      volume_group_id,
                      protection_policy_id,
                      performance_policy,
                      description,
                      app_type,
                      app_type_other,
                      appliance_id):
        """Create PowerStore volume"""

        try:
            msg = ("Creating volume {0} of size {1} with performance policy"
                   " {2}, protection_policy {3}, description {4} and"
                   " volume_group {5}" .format(vol_name, size,
                                               performance_policy,
                                               protection_policy_id,
                                               description, volume_group_id))
            LOG.info(msg)
            self.provisioning.create_volume(
                name=vol_name,
                size=size,
                description=description,
                performance_policy_id=performance_policy,
                protection_policy_id=protection_policy_id,
                volume_group_id=volume_group_id,
                app_type=app_type,
                app_type_other=app_type_other,
                appliance_id=appliance_id)
            return True
        except Exception as e:
            msg = 'Create volume {0} failed with error {1}'.format(
                vol_name, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def modify_volume(self, vol_id,
                      old_volume_name,
                      name,
                      size,
                      protection_policy_id,
                      performance_policy,
                      description,
                      app_type,
                      app_type_other):
        """Modify PowerStore volume"""
        # old_volume_name and name can be same if a new name is not passed
        # old_volume_name added for logging purpose
        try:
            msg = (
                "Modifying volume {0} with size {1}, performance policy {2}, "
                "protection_policy {3}, description {4} and name {5}".format(
                    old_volume_name,
                    size,
                    performance_policy,
                    protection_policy_id,
                    description,
                    name))
            LOG.info(msg)
            self.provisioning.modify_volume(
                volume_id=vol_id,
                name=name,
                size=size,
                description=description,
                performance_policy_id=performance_policy,
                protection_policy_id=protection_policy_id,
                app_type=app_type,
                app_type_other=app_type_other)
            return True
        except Exception as e:
            msg = 'Modify volume {0} failed with error {1}'.format(
                old_volume_name, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def map_unmap_volume_to_host(self, vol, host, mapping_state):
        current_hosts = []
        current_host_ids = []
        host_identifier = self.module.params['host']

        prepare_host_list(vol, current_hosts, current_host_ids)

        if mapping_state == 'mapped' and host in current_host_ids:
            LOG.info('Volume %s is already mapped to host %s', vol['name'],
                     host_identifier)
            return False

        if mapping_state == 'mapped' and host not in current_host_ids:
            hlu = self.module.params['hlu']
            LOG.info('Mapping volume %s to host %s with HLU %s', vol['name'],
                     host_identifier, hlu)
            try:
                self.provisioning.map_volume_to_host(
                    volume_id=vol['id'],
                    host_id=host,
                    logical_unit_number=hlu)
                return True
            except Exception as e:
                error_msg = ('Mapping volume {0} to host {1} failed with'
                             ' error {2}'.format(vol['name'], host_identifier,
                                                 str(e)))
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

        if mapping_state == 'unmapped' and host not in current_host_ids:
            LOG.info('Volume %s is not mapped to host %s', vol['name'],
                     host_identifier)
            return False

        if mapping_state == 'unmapped' and host in current_host_ids:
            LOG.info('Unmapping volume %s from host %s', vol['name'],
                     host_identifier)
            try:
                self.provisioning.unmap_volume_from_host(volume_id=vol['id'],
                                                         host_id=host)
                return True
            except Exception as e:
                error_msg = ('Unmapping volume {0} from host {1} failed with'
                             ' error {2}'.format(vol['name'], host_identifier,
                                                 str(e)))
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg, **utils.failure_codes(e))
        return False

    def map_unmap_volume_to_hostgroup(self, vol, hostgroup_details, mapping_state):
        host_group_identifier = self.module.params['hostgroup']
        current_volumes = hostgroup_details['mapped_host_groups']
        current_volume_ids = []
        for volume in range(len(current_volumes)):
            current_volume_ids.append(hostgroup_details['mapped_host_groups'][volume]['volume_id'])

        if hostgroup_details['mapped_host_groups'] != []:
            if mapping_state == 'mapped' and vol['id'] in current_volume_ids:
                LOG.info('Volume %s is already mapped to hostgroup %s',
                         vol['name'], host_group_identifier)
                return False

        if mapping_state == 'mapped' and vol['id'] not in current_volume_ids:
            hlu = self.module.params['hlu']
            LOG.info('Mapping volume %s to hostgroup %s with HLU %s',
                     vol['name'], host_group_identifier, hlu)
            try:
                self.provisioning.map_volume_to_host_group(
                    volume_id=vol['id'],
                    host_group_id=hostgroup_details['id'],
                    logical_unit_number=hlu)
                return True
            except Exception as e:
                error_msg = (
                    'Mapping volume {0} to hostgroup {1} failed with error'
                    ' {2}' .format(vol['name'], host_group_identifier,
                                   str(e)))
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

        if mapping_state == 'unmapped' and vol['id'] not in current_volume_ids:
            LOG.info('Volume %s is not mapped to hostgroup %s', vol['name'],
                     host_group_identifier)
            return False

        if mapping_state == 'unmapped' and vol['id'] in current_volume_ids:
            LOG.info('Unmapping volume %s from hostgroup %s', vol['name'],
                     host_group_identifier)
            try:
                self.provisioning.unmap_volume_from_host_group(
                    volume_id=vol['id'], host_group_id=hostgroup_details['id'])
                return True
            except Exception as e:
                error_msg = (
                    'Unmapping volume {0} from hostgroup{1} failed with error'
                    ' {2}' .format(vol['name'], host_group_identifier,
                                   str(e)))
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg, **utils.failure_codes(e))
        return False

    def delete_volume(self, volume):
        """
        Delete volume from system
        """
        try:
            LOG.info('Deleting volume %s', volume['name'])
            self.provisioning.delete_volume(volume['id'])
            return True
        except Exception as e:
            error_msg = 'Delete volume {0} failed with error {1}'.format(
                volume['name'], str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def validate_clone_details(self, clone_details):
        """
        Validate clone details
        :param clone_details: Clone details.
        :return: Validated clone details.
        """
        clone_details['performance_policy_id'] = None
        clone_details['protection_policy_id'] = None
        if clone_details['performance_policy'] is not None:
            clone_details['performance_policy_id'] = self.get_performance_policy(clone_details['performance_policy'])
        if clone_details['protection_policy'] is not None:
            clone_details['protection_policy_id'] = self.get_protection_policy_id_by_name(clone_details['protection_policy'])
        clone_details['host_id'] = None
        clone_details['host_group_id'] = None
        if clone_details['host'] is not None:
            clone_details['host_id'] = self.get_host_id_by_name(clone_details['host'])
        if clone_details['host_group'] is not None:
            clone_details['host_group_id'] = self.get_host_group_id_by_name(clone_details['host_group'])['id']
        if clone_details['host_id'] is None and clone_details['host_group_id'] is None and clone_details['logical_unit_number'] is not None:
            errormsg = "Either of host identifier or host group identifier is required along with logical_unit_number."
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)
        return clone_details

    def clone_volume(self, vol_id, clone_details):
        """
        Clone volume
        :param vol_id: Unique volume identifier.
        :param clone_details: Clone details.
        :return: True
        """
        try:
            LOG.info("Cloning volume")
            vol_details = self.get_volume(vol_name=clone_details['name'])
            if vol_details:
                return False
            clone_details = self.validate_clone_details(clone_details)
            clone_payload = {
                'volume_id': vol_id,
                'name': clone_details['name'],
                'description': clone_details['description'],
                'host_id': clone_details['host_id'],
                'host_group_id': clone_details['host_group_id'],
                'logical_unit_number': clone_details['logical_unit_number'],
                'protection_policy_id': clone_details['protection_policy_id'],
                'performance_policy_id': clone_details['performance_policy_id']
            }
            clone_result = self.provisioning.clone_volume(**clone_payload)
            LOG.debug(clone_result)
            return True
        except Exception as e:
            errormsg = "Cloning volume %s failed with error %s" % (vol_id, str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg, **utils.failure_codes(e))

    def get_volume_snapshots(self, vol_id, snap_name_or_id=None, all_snapshots=False):
        """
        Get volume snapshots
        :param vol_id: Unique volume identifier.
        :param snap_name_or_id: Existing snapshot name or id
        :param all_snapshots: Whether to retrieve all snapshots or not
        :return: Retrieve all snapshots of volume or given snapshot
        """
        try:
            LOG.info("Getting volume snapshots")
            vol_snapshots_list = self.provisioning.get_volumes(filter_dict={'type': 'eq.Snapshot', 'protection_data->>family_id': 'eq.' + vol_id})
            LOG.debug(vol_snapshots_list)
            if all_snapshots:
                return True, vol_snapshots_list
            for snap in vol_snapshots_list:
                if snap['name'] == snap_name_or_id or snap['id'] == snap_name_or_id:
                    return True, snap
            return False, None
        except Exception as e:
            errormsg = "Getting volume snapshots failed with error %s" % (str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg, **utils.failure_codes(e))

    def validate_refresh_op_params(self, data):
        """
        Validate refresh details
        :param data: Refresh details.
        :return: Validated refresh data.
        """
        if utils.name_or_id(data['source_volume']) == "NAME":
            vol_details = self.get_volume(vol_name=data['source_volume'])
        else:
            vol_details = self.get_volume(vol_id=data['source_volume'])

        if vol_details is None:
            errormsg = "Source volume does not exist."
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)
        elif vol_details['protection_data']['family_id'] != data['volume_family_id']:
            errormsg = "Source volume does not belong to the family of the current volume."
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)
        else:
            data['source_volume_id'] = vol_details['id']

        return data

    def validate_restore_op_params(self, data):
        """
        Validate restore details
        :param data: Restore details.
        :return: Validated restore data.
        """
        exists, snap_details = self.get_volume_snapshots(data['volume_family_id'], snap_name_or_id=data['source_snap'])
        if not exists:
            errormsg = "source snapshot does not exists."
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)
        data['source_snap_id'] = snap_details['id']

        return data

    def validate_refresh_restore_details(self, operation, data):
        """
        Validate refresh and restore details
        :param data: Refresh details or Restore details.
        :return: Validated data.
        """
        if operation == 'refresh':
            self.validate_refresh_op_params(data)
        if operation == 'restore':
            self.validate_restore_op_params(data)
        if data['backup_snap_profile'] is not None:
            if not data['create_backup_snap']:
                errormsg = "Specify create_back_snap as True to set backup_snap_profile."
                LOG.error(errormsg)
                self.module.fail_json(msg=errormsg)
            if data['backup_snap_profile']['performance_policy'] is not None:
                data['backup_snap_profile']['performance_policy_id'] = self.get_performance_policy(data['backup_snap_profile']['performance_policy'])
            if data['backup_snap_profile']['expiration_timestamp'] is not None and \
                    not utils.validate_timestamp(data['backup_snap_profile']['expiration_timestamp']):
                errormsg = 'Incorrect date format, should be YYYY-MM-DDTHH:MM:SSZ'
                LOG.error(errormsg)
                self.module.fail_json(msg=errormsg)
        return data

    def refresh_volume(self, volume, refresh_details):
        """
        Refresh volume
        :param volume: Volume details.
        :param refresh_details: Refresh details.
        :return: True
        """
        try:
            LOG.info("Refreshing volume")
            refresh_details['volume_family_id'] = volume['protection_data']['family_id']
            vol_id = volume['id']
            if 'backup_snap_profile' in refresh_details and refresh_details['backup_snap_profile'] \
                    and refresh_details['backup_snap_profile']['name'] is not None:
                exists, snap_details = self.get_volume_snapshots(refresh_details['volume_family_id'],
                                                                 snap_name_or_id=refresh_details['backup_snap_profile']['name'])
                LOG.debug(snap_details)
                if exists:
                    return False
            refresh_details = self.validate_refresh_restore_details('refresh', refresh_details)
            refresh_payload = {
                'volume_id': vol_id,
                'volume_id_to_refresh_from': refresh_details['source_volume_id'],
                'create_backup_snap': refresh_details['create_backup_snap']
            }
            refresh_payload.update(get_backupsnap_profile_details(refresh_details))
            refresh_result = self.provisioning.refresh_volume(**refresh_payload)
            LOG.debug(refresh_result)
            return True
        except Exception as e:
            errormsg = "Refreshing volume %s failed with error %s" % (vol_id, str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg, **utils.failure_codes(e))

    def restore_volume(self, volume, restore_details):
        """
        Restore volume
        :param vol_id: Unique volume identifier.
        :param restore_volume: Restore details.
        :return: True
        """
        try:
            LOG.info("Restoring volume")
            restore_details['volume_family_id'] = volume['protection_data']['family_id']
            vol_id = volume['id']
            if 'backup_snap_profile' in restore_details and restore_details['backup_snap_profile'] and \
                    restore_details['backup_snap_profile']['name'] is not None:
                exists, snap_details = self.get_volume_snapshots(restore_details['volume_family_id'],
                                                                 snap_name_or_id=restore_details['backup_snap_profile']['name'])
                LOG.debug(snap_details)
                if exists:
                    return False
            restore_details = self.validate_refresh_restore_details('restore', restore_details)
            restore_payload = {
                'volume_id': vol_id,
                'snap_id_to_restore_from': restore_details['source_snap_id'],
                'create_backup_snap': restore_details['create_backup_snap']
            }
            restore_payload.update(get_backupsnap_profile_details(restore_details))
            restore_result = self.provisioning.restore_volume(**restore_payload)
            LOG.debug(restore_result)
            return True
        except Exception as e:
            errormsg = "Restoring volume %s failed with error %s" % (vol_id, str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg, **utils.failure_codes(e))

    def configure_metro_volume(self, volume, remote_system,
                               remote_appliance_id=None):
        """Configure a metro volume
        :param volume: Volume details
        :type volume: dict
        :param remote_system: Remote system with which metro relationship will
                              be established
        :type remote_system: str
        :param remote_appliance_id: A specific remote system appliance to which
                                    volume will be configured
        :type remote_appliance_id: str
        :return: True if metro configuration is successful
        :rtype: bool
        """
        try:
            msg = "Establish a metro configuration for volume {0} to remote" \
                  " system {1}".format(volume['name'], remote_system)
            LOG.info(msg)
            self.provisioning.configure_metro_volume(
                volume_id=volume['id'], remote_system_id=remote_system,
                remote_appliance_id=remote_appliance_id)
            return True
        except Exception as e:
            err_msg = "Failed to configure metro for volume {0} with error" \
                      " {1}".format(volume['name'], str(e))
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg, **utils.failure_codes(e))

    def end_metro_volume(self, volume, delete_remote_volume=None):
        """Remove the metro configuration for volume
        :param volume: Details of the volume
        :type volume: dict
        :param delete_remote_volume: Whether to delete the remote volume
                                     during metro removal
        :type delete_remote_volume: bool
        return: True if removal of metro config is successful
        :rtype: bool
        """
        try:
            msg = "Removing the metro configuration for volume %s" % volume['name']
            LOG.info(msg)
            self.provisioning.end_volume_metro_config(
                volume_id=volume['id'],
                delete_remote_volume=delete_remote_volume)
            return True
        except Exception as e:
            err_msg = "Failed to remove the metro configuration for volume " \
                      "{0} with error {1}".format(volume['name'], str(e))
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg, **utils.failure_codes(e))

    def perform_module_operation(self):
        """
        Perform different actions on volume based on user parameters
        chosen in playbook
        """
        size = self.module.params['size']
        cap_unit = self.module.params['cap_unit']
        state = self.module.params['state']
        new_name = self.module.params['new_name']
        vol_id = self.module.params['vol_id']
        vol_name = self.module.params['vol_name']
        volume_group_id = self.get_volume_group_id_by_name(
            self.module.params['vg_name'])
        protection_policy_id = self.get_protection_policy_id_by_name(
            self.module.params['protection_policy'])
        performance_policy = self.get_performance_policy(
            self.module.params['performance_policy'])
        description = self.module.params['description']
        mapping_state = self.module.params['mapping_state']
        host = self.get_host_id_by_name(self.module.params['host'])
        hostgroup_details = self.get_host_group_id_by_name(
            self.module.params['hostgroup'])
        hostgroup = None
        if hostgroup_details:
            hostgroup = hostgroup_details['id']
        hlu = self.module.params['hlu']
        clone_volume = self.module.params['clone_volume']
        source_volume = self.module.params['source_volume']
        source_snap = self.module.params['source_snap']
        create_backup_snap = self.module.params['create_backup_snap']
        backup_snap_profile = self.module.params['backup_snap_profile']
        remote_system = self.get_remote_system_id(
            self.module.params['remote_system'])
        remote_appliance_id = self.get_remote_appliance_id(
            remote_system, self.module.params['remote_appliance_id'])
        end_metro_config = self.module.params['end_metro_config']
        delete_remote_volume = self.module.params['delete_remote_volume']
        app_type = self.module.params['app_type']
        app_type_other = self.module.params['app_type_other']
        appliance_id = self.module.params['appliance_id']
        if self.module.params['appliance_name']:
            appliance_id = self.get_appliance_id_by_name(
                self.module.params['appliance_name'])

        changed = False
        is_volume_refreshed = False
        is_volume_cloned = False
        is_volume_restored = False
        volume = self.get_volume(vol_id, vol_name)
        # fetching the volume id from volume details
        if volume is not None:
            vol_id = volume['id']

        if size:
            if cap_unit:
                size = int(utils.get_size_bytes(size, cap_unit))
            else:
                size = int(utils.get_size_bytes(size, 'GB'))

        if (cap_unit is not None) and not size:
            self.module.fail_json(msg="cap_unit can be specified along "
                                      "with size. Please enter a valid size.")

        if app_type_other is not None and len(app_type_other) > 32:
            self.module.fail_json(msg="Max Length for option "
                                      "'app_type_other' is 32. "
                                      "Enter a valid string.")

        # Call to create volume
        if state == 'present' and volume is None:
            if vol_name is None or len(vol_name.strip()) == 0:
                self.module.fail_json(msg="Please provide valid volume name.")

            if new_name:
                msg = 'new_name specified for non-existing volume'
                LOG.info(msg)
                self.module.fail_json(msg=msg)

            if size is None:
                msg = 'Size is a required parameter while creating volume'
                LOG.info(msg)
                self.module.fail_json(msg=msg)

            changed = self.create_volume(
                vol_name=vol_name,
                size=size,
                volume_group_id=volume_group_id,
                protection_policy_id=protection_policy_id,
                performance_policy=performance_policy,
                description=description,
                app_type=app_type,
                app_type_other=app_type_other,
                appliance_id=appliance_id)
            if changed:
                vol_id = self.get_volume_id_by_name(vol_name)
                volume = self.get_volume(vol_id=vol_id)

        if state == 'present' and volume:
            if host and hostgroup:
                msg = 'Only one of host or hostgroup can be mapped to a' \
                      ' volume in one call'
                LOG.info(msg)
                self.module.fail_json(msg=msg)
            hlu_mod_flag = True
            if appliance_id != volume['appliance_id'] and appliance_id:
                error_msg = f"Modifying the appliance of a volume to {appliance_id} is not allowed."
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)
            if host and hlu:
                hlu_mod_flag, error = check_for_hlu_modification(
                    volume, host=host, hlu=hlu)
            if hostgroup and hlu:
                hlu_mod_flag, error = check_for_hlu_modification(
                    volume, hostgroup=hostgroup, hlu=hlu)
            if hlu_mod_flag is False:
                msg = 'Modification of HLU is not supported. {0}'.format(
                    error)
                LOG.info(msg)
                self.module.fail_json(msg=msg)
            vg_mod_flag = True
            if volume['volume_groups']:
                # check for modification of VG
                if len(volume['volume_groups']) > 0 and \
                        volume_group_id is not None and \
                        volume_group_id != volume['volume_groups'][0]['id']:
                    vg_mod_flag = False
                # check for assignment of a VG to an already existing volume
            elif volume_group_id is not None:
                vg_mod_flag = False
            if not vg_mod_flag:
                msg = ("Modification or assignment of Volume Group for an "
                       "already present Volume is not supported using Volume "
                       "module. Use Volume Group module instead.")
                LOG.info(msg)
                self.module.fail_json(msg=msg)

            name = new_name if new_name is not None else vol_name
            current_size = volume['size']
            if size is not None:
                if current_size > size:
                    msg = ("Current volume size {0} B is greater than {1} B"
                           " specified. Only expansion of volume size is"
                           " allowed".format(current_size, size))
                    LOG.info(msg)
                    self.module.fail_json(msg=msg)

                if current_size == size:
                    # passing the same size to the API results in a error,
                    # hence
                    # sending None instead which indicates no change
                    msg = ('Current volume size {0} B is same as {1} B'
                           ' specified'.format(current_size, size))
                    LOG.info(msg)
                    size = None

            new_volume_dict = {
                'name': name,
                'description': description,
                'protection_policy_id': protection_policy_id,
                'performance_policy_id': performance_policy,
                'size': size,
                'app_type': app_type,
                'app_type_other': app_type_other,
                'appliance_id': appliance_id
            }

            # In update_dict parameters which are to be updated will have
            # values and other parameter's value will be set to None
            modify_flag, update_dict = \
                check_modify_volume_required(volume, new_volume_dict)
            if modify_flag:
                if mapping_state is not None or hlu is not None:
                    msg = 'Volume modification and host mapping cannot be' \
                          ' done in the same call'
                    LOG.info(msg)
                    self.module.fail_json(msg=msg)
                changed = self.modify_volume(
                    vol_id=vol_id,
                    old_volume_name=volume['name'],
                    name=update_dict['name'],
                    size=update_dict['size'],
                    protection_policy_id=update_dict['protection_policy_id'],
                    performance_policy=update_dict['performance_policy_id'],
                    description=update_dict['description'],
                    app_type=update_dict['app_type'],
                    app_type_other=update_dict['app_type_other']) or changed

        if state == 'present' and volume and mapping_state in [
                None, 'unmapped'] and hlu:
            error_msg = 'Invalid paramter HLU provided'
            LOG.info(error_msg)
            self.module.fail_json(msg=error_msg)

        if (host or hostgroup) and state == 'present' and volume and \
                mapping_state is None:
            error_msg = 'Mapping state not provided, mandatory for mapping'
            LOG.info(error_msg)
            self.module.fail_json(msg=error_msg)

        if state == 'present' and volume and mapping_state:
            if not host and not hostgroup:
                msg = 'Specify either host or hostgroup to be mapped to a' \
                      ' volume'
                LOG.info(msg)
                self.module.fail_json(msg=msg)

            if host:
                changed = self.map_unmap_volume_to_host(
                    volume, host, mapping_state) or changed
            if hostgroup:
                changed = self.map_unmap_volume_to_hostgroup(
                    volume, hostgroup_details, mapping_state) or changed

        if state == 'present' and clone_volume is not None:
            changed = self.clone_volume(vol_id, clone_volume)
            is_volume_cloned = changed

        if state == 'present' and source_volume is not None:
            refresh_details = {
                'source_volume': source_volume,
                'create_backup_snap': create_backup_snap,
                'backup_snap_profile': backup_snap_profile
            }
            changed = self.refresh_volume(volume, refresh_details)
            is_volume_refreshed = changed

        if state == 'present' and source_snap is not None:
            restore_details = {
                'source_snap': source_snap,
                'create_backup_snap': create_backup_snap,
                'backup_snap_profile': backup_snap_profile
            }
            changed = self.restore_volume(volume, restore_details)
            is_volume_restored = changed

        if state == "present" and volume and remote_system is not None:
            if 'metro_replication_session_id' in volume \
                    and volume['metro_replication_session_id'] is not None:
                session_id = volume['metro_replication_session_id']
                is_metro_exists = self.is_metro_configured(
                    session_id, remote_system)
                changed = is_metro_exists
            elif 'metro_replication_session_id' in volume and \
                    volume['metro_replication_session_id'] is None:
                changed = self.configure_metro_volume(
                    volume, remote_system, remote_appliance_id)

        if state == "present" and volume and end_metro_config is not None \
                and end_metro_config and \
                'metro_replication_session_id' in volume and \
                volume['metro_replication_session_id'] is not None:
            changed = self.end_metro_volume(volume, delete_remote_volume)

        if state == 'absent' and volume:
            LOG.info('Deleting volume %s ', volume['name'])
            changed = self.delete_volume(volume) or changed

        '''
        Finally update the module changed state and volume details
        '''

        self.result["changed"] = changed
        self.result["is_volume_cloned"] = is_volume_cloned
        self.result["is_volume_refreshed"] = is_volume_refreshed
        self.result["is_volume_restored"] = is_volume_restored
        if state == 'present':
            self.result["volume_details"] = self.get_volume(vol_id=vol_id)
            if self.result["volume_details"]:
                self.result["volume_details"].update(
                    snapshots=self.get_volume_snapshots(self.result["volume_details"]['id'], all_snapshots=True)[1])
                self.result["volume_details"].update(appliance_name=self.update_volume_details(self.result["volume_details"]))
        self.module.exit_json(**self.result)

    def is_metro_configured(self, session_id, remote_system):
        """Check whether metro is configured for volume"""
        try:
            session_details = self.protection.\
                get_replication_session_details(session_id=session_id)
            if session_details['remote_system_id'] == remote_system:
                return False
            msg = "Metro session is already configured for the volume."
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        except Exception as e:
            error_msg = "Get metro replication session {0} details failed " \
                        "with error: {1}".format(session_id, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def get_volume_id_by_name(self, volume_name):
        try:
            volume_info = self.provisioning.get_volume_by_name(volume_name)
            if volume_info:
                if len(volume_info) > 1:
                    error_msg = 'Multiple volumes by the same name found'
                    LOG.error(error_msg)
                    self.module.fail_json(msg=error_msg)
                return volume_info[0]['id']
            return None
        except Exception as e:
            error_msg = "Get volume: {0} failed with " \
                        "error: {1}".format(volume_name, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def get_volume_group_id_by_name(self, volume_group_name):
        try:
            if volume_group_name is None:
                return None

            if utils.name_or_id(volume_group_name) == "NAME":
                # Get the volume group details using name
                volume_group_info = self.provisioning. \
                    get_volume_group_by_name(volume_group_name)
                if volume_group_info:
                    if len(volume_group_info) > 1:
                        error_msg = 'Multiple volume groups by the same ' \
                                    'name found'
                        LOG.error(error_msg)
                        self.module.fail_json(msg=error_msg)
                    return volume_group_info[0]['id']
            else:
                # Get the volume group details using id
                if self.provisioning.get_volume_group_details(
                        volume_group_name):
                    return volume_group_name

            error_msg = ("volume group {0} not found".format(
                volume_group_name))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)
        except Exception as e:
            error_msg = "Get volume group: {0} failed with " \
                        "error: {1}".format(volume_group_name, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def get_appliance_id_by_name(self, appliance_name):
        try:

            # Get the appliance details using name
            appliance_info = self.configuration.get_appliance_by_name(appliance_name)
            if appliance_info:
                return appliance_info[0]['id']

            error_msg = f"Appliance {appliance_name} not found"
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)
        except Exception as e:
            error_msg = f"Get appliance: {appliance_name} failed with error: {e}"
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def get_protection_policy_id_by_name(self, protection_policy_name):
        try:
            if protection_policy_name is None:
                return None
            if len(protection_policy_name) == 0:
                return ''

            if utils.name_or_id(protection_policy_name) == "NAME":
                # Get the protection policy details using name
                protection_policy_info = self.conn.protection.\
                    get_protection_policy_by_name(protection_policy_name)
                if protection_policy_info:
                    if len(protection_policy_info) > 1:
                        error_msg = 'Multiple protection policies by the ' \
                                    'same name found'
                        LOG.error(error_msg)
                        self.module.fail_json(msg=error_msg)
                    return protection_policy_info[0]['id']
            else:
                # Get the protection policy details using id
                if self.conn.protection.get_protection_policy_details(
                        protection_policy_name):
                    return protection_policy_name
            error_msg = ("protection policy {0} not found".format(
                protection_policy_name))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)
        except Exception as e:
            error_msg = "Get protection policy: {0} failed with " \
                        "error: {1}".format(protection_policy_name, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def get_host_id_by_name(self, host_name):
        try:
            if host_name is None:
                return None

            if utils.name_or_id(host_name) == "NAME":
                # Get the host details using name
                host_info = self.provisioning.get_host_by_name(host_name)
                if host_info:
                    if len(host_info) > 1:
                        error_msg = 'Multiple hosts by the same name found'
                        LOG.error(error_msg)
                        self.module.fail_json(msg=error_msg)
                    return host_info[0]['id']
            else:
                # Get the host details using id
                if self.provisioning.get_host_details(host_name):
                    return host_name
            error_msg = ("Host {0} not found".format(host_name))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)
        except Exception as e:
            error_msg = "Get host: {0} failed with " \
                        "error: {1}".format(host_name, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def get_host_group_id_by_name(self, host_group_name):
        try:
            if host_group_name is None:
                return None

            if utils.name_or_id(host_group_name) == "NAME":
                # Get the host group details using name
                host_group_info = self.provisioning.\
                    get_host_group_by_name(host_group_name)
                if host_group_info:
                    if len(host_group_info) > 1:
                        error_msg = 'Multiple host groups by the same name ' \
                                    'found'
                        LOG.error(error_msg)
                        self.module.fail_json(msg=error_msg)
                    return host_group_info[0]
            else:
                # Get the host group details using id
                host_group_info = self.provisioning.get_host_group_details(host_group_name)
                if host_group_info:
                    return host_group_info

            error_msg = ("host group {0} not found".format(host_group_name))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)
        except Exception as e:
            error_msg = "Get host group: {0} failed with " \
                        "error: {1}".format(host_group_name, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def get_remote_system_id(self, remote_system):
        """ Fetch the remote system ID."""
        try:
            if remote_system is None:
                return None
            elif utils.name_or_id(remote_system) == "NAME":
                remote_system_info = self.protection.\
                    get_remote_system_by_name(name=remote_system)

                if remote_system_info and len(remote_system_info) == 1:
                    return remote_system_info[0]['id']
                elif remote_system_info and len(remote_system_info) > 1:
                    err_msg = "Multiple remote system found with same name."
                    LOG.error(err_msg)
                    self.module.fail_json(msg=err_msg)

            elif self.protection.get_remote_system_details(
                    remote_system_id=remote_system):
                return remote_system
            er_msg = "Remote system %s not found." % remote_system
            LOG.error(er_msg)
            self.module.fail_json(msg=er_msg)

        except Exception as e:
            error_msg = "Fetching remote system {0} failed with error " \
                        "{1}".format(remote_system, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def get_remote_appliance_id(self, remote_system, remote_appliance_id):
        """ Fetch the remote appliance ID."""
        try:
            if remote_appliance_id is None:
                return None
            else:
                remote_app_details = self.protection.\
                    get_remote_system_appliance_details(remote_system_id=remote_system)

                if remote_app_details is not None:
                    for apps in remote_app_details['remote_appliances']:
                        if apps['id'] == remote_appliance_id:
                            return remote_appliance_id

            er_msg = "No remote appliance {0} found in remote system {1}.".\
                format(remote_appliance_id, remote_system)
            LOG.error(er_msg)
            self.module.fail_json(msg=er_msg)

        except Exception as e:
            error_msg = "Fetching remote appliance {0} failed with error " \
                        "{1}".format(remote_system, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def get_performance_policy(self, performance_policy):
        if performance_policy is None:
            return None
        else:
            return self.performance_policy_dict.get(performance_policy)


def prepare_host_list(vol, current_hosts, current_host_ids):
    if 'host' in vol:
        current_hosts = vol['host']
    else:
        if 'hlu_details' in vol:
            for map_details in vol['hlu_details']:
                if map_details['host_id'] is not None:
                    current_hosts.append(map_details['host_id'])

    # In PowerStore version 3.0.0.0 volume response, will get the only list of host IDs mapped.
    # In PowerStore versions below 3.0.0.0 volume response, will get ID and name of host mapped.
    for host_t in current_hosts:
        if 'id' in host_t:
            current_host_ids.append(host_t['id'])
        else:
            current_host_ids.append(host_t)


def check_modify_volume_required(vol, vol_dict2):
    """Check if modification is required for volume"""
    vol_dict1 = {'name': vol['name'], 'description': vol['description'],
                 'protection_policy_id': vol['protection_policy_id'],
                 'performance_policy_id': vol['performance_policy_id'],
                 'size': vol['size'], 'app_type': vol['app_type'],
                 'app_type_other': vol['app_type_other']
                 }

    update_dict = {}
    modify_flag = False
    """to compare two volumes"""
    for key in vol_dict1.keys():
        if key in vol_dict2.keys():
            update_dict[key] = None
            if vol_dict2[key] is not None and vol_dict1[key] !=\
                    vol_dict2[key]:
                if key == 'protection_policy_id' and vol_dict1[key] is None\
                        and vol_dict2[key] == '':
                    continue
                LOG.debug("Key %s in vol_dict1=%s,vol_dict2=%s", key,
                          vol_dict1[key], vol_dict2[key])
                update_dict[key] = vol_dict2[key]
                modify_flag = True
    return modify_flag, update_dict


def check_for_hlu_modification(volume, hlu, host=None, hostgroup=None):
    hlu_details = volume['hlu_details']
    if host:
        for element in hlu_details:
            if element.get('host_id') == host and \
                    int(element['logical_unit_number']) != hlu:
                msg = 'Modification of HLU from {0} to {1} for host {2} was' \
                      ' attempted'.format(int(element['logical_unit_number']),
                                          hlu, host)
                return False, msg

    if hostgroup:
        for element in hlu_details:
            if element.get('host_group_id') == hostgroup and \
                    int(element['logical_unit_number']) != hlu:
                msg = 'Modification of HLU from {0} to {1} for hostgroup ' \
                      '{2} was attempted'.\
                    format(int(element['logical_unit_number']), hlu,
                           hostgroup)
                return False, msg
    return True, ""


def get_backup_profile_parameters():
    """
    This method provide parameter required for the backup_profile
    """
    return dict(type='dict', options=dict(name=dict(type='str'),
                                          description=dict(type='str'),
                                          performance_policy=dict(required=False, choices=['high', 'medium', 'low'], type='str'),
                                          expiration_timestamp=dict(type='str')))


def get_backupsnap_profile_details(data):
    """
    Get backupsnap profile details
    :param data: Refresh details or Restore details.
    :return: backupsnap profile details.
    """
    backup_snap_profile = {}
    if data['backup_snap_profile']:
        backup_snap_profile['backup_snap_name'] = data['backup_snap_profile']['name']
        backup_snap_profile['backup_snap_description'] = data['backup_snap_profile']['description']
        backup_snap_profile['backup_snap_expiration_timestamp'] = data['backup_snap_profile']['expiration_timestamp']
        if 'performance_policy_id' in data['backup_snap_profile']:
            backup_snap_profile['backup_snap_performance_policy_id'] = data['backup_snap_profile']['performance_policy_id']
    return backup_snap_profile


def get_powerstore_volume_parameters():
    """
    This method provide parameter required for the ansible volume
    modules on PowerStore
    """
    return dict(
        vol_name=dict(required=False, type='str'),
        vol_id=dict(required=False, type='str'),
        size=dict(required=False, type='float', default=None),
        vg_name=dict(required=False, type='str'),
        new_name=dict(required=False, type='str'),
        cap_unit=dict(required=False, choices=['MB', 'GB', 'TB'],
                      type='str'),
        state=dict(required=True, choices=['present', 'absent'],
                   type='str'),
        performance_policy=dict(required=False,
                                choices=['high', 'medium', 'low'],
                                type='str'),
        protection_policy=dict(required=False, type='str'),
        description=dict(required=False, type='str'),
        mapping_state=dict(required=False, choices=['mapped', 'unmapped'],
                           type='str'),
        host=dict(required=False, type='str'),
        hostgroup=dict(required=False, type='str'),
        hlu=dict(required=False, type='int'),
        clone_volume=dict(
            type='dict', options=dict(
                name=dict(type='str'),
                description=dict(type='str'),
                host=dict(type='str'),
                host_group=dict(type='str'),
                logical_unit_number=dict(type='int'),
                protection_policy=dict(type='str'),
                performance_policy=dict(required=False, choices=['high', 'medium', 'low'], type='str')
            )
        ),
        source_volume=dict(type='str'),
        source_snap=dict(type='str'),
        create_backup_snap=dict(type='bool'),
        backup_snap_profile=get_backup_profile_parameters(),
        remote_system=dict(required=False, type='str'),
        remote_appliance_id=dict(required=False, type='str'),
        end_metro_config=dict(required=False, type='bool', default=False),
        delete_remote_volume=dict(required=False, type='bool'),
        app_type=dict(
            type='str',
            choices=["Relational_Databases_Other",
                     "Relational_Databases_Oracle",
                     "Relational_Databases_SQL_Server",
                     "Relational_Databases_PostgreSQL",
                     "Relational_Databases_MySQL",
                     "Relational_Databases_IBM_DB2",
                     "Big_Data_Analytics_Other", "Big_Data_Analytics_MongoDB",
                     "Big_Data_Analytics_Cassandra",
                     "Big_Data_Analytics_SAP_HANA", "Big_Data_Analytics_Spark",
                     "Big_Data_Analytics_Splunk",
                     "Big_Data_Analytics_ElasticSearch",
                     "Business_Applications_Other",
                     "Business_Applications_ERP_SAP",
                     "Business_Applications_CRM",
                     "Business_Applications_Exchange",
                     "Business_Applications_Sharepoint", "Healthcare_Other",
                     "Healthcare_Epic", "Healthcare_MEDITECH",
                     "Healthcare_Allscripts", "Healthcare_Cerner",
                     "Virtualization_Other",
                     "Virtualization_Virtual_Servers_VSI",
                     "Virtualization_Containers_Kubernetes",
                     "Virtualization_Virtual_Desktops_VDI", "Other"]),
        app_type_other=dict(type='str'),
        appliance_name=dict(type='str'),
        appliance_id=dict(type='str')
    )


def main():
    """ Create PowerStore volume object and perform action on it
        based on user input from playbook"""
    obj = PowerStoreVolume()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
