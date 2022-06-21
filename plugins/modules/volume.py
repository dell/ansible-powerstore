#!/usr/bin/python
# Copyright: (c) 2019-2021, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

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
author:
- Ambuj Dubey (@AmbujDube) <ansible.team@dell.com>
- Manisha Agrawal (@agrawm3) <ansible.team@dell.com>
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
    - It defaults to 'GB', if not specified.
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
  protection_policy:
    description:
    - The protection_policy of the volume.
    - To represent policy, both name or ID can be used interchangably.
      The module will detect both.
    - A volume can be assigned a protection policy at the time of creation of
      volume or later as well.
    - The policy can also be changed for a given volume by simply passing the
      new value.
    - The policy can be removed by passing an empty string.
    - Check examples for more clarity.
    type: str
  performance_policy:
    description:
    - The performance_policy for the volume.
    - A volume can be assigned a performance policy at the time of creation of
      the volume, or later as well.
    - The policy can also be changed for a given volume, by simply passing the
      new value.
    - Check examples for more clarity.
    - If not given, performance policy will be 'medium'.
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
    - Value mapped - indicates that the volume should be mapped to the host
      or host group.
    - Value unmapped - indicates that the volume should not be mapped to the
      host or host group.
    - Only one of a host or host group can be supplied in one call.
    choices: [mapped, unmapped]
    type: str
  hlu:
    description:
    - Logical unit number for the host/host group volume access.
    - Optional parameter when mapping a volume to host/host group.
    - HLU modification is not supported.
    required: False
    type: int
  state:
    description:
    - Define whether the volume should exist or not.
    - Value present - indicates that the volume should exist on the system.
    - Value absent - indicates that the volume should not exist on the system.
    required: true
    choices: [absent, present]
    type: str

notes:
- To create a new volume, vol_name and size is required. cap_unit,
  description, vg_name, performance_policy, and protection_policy are
  optional.
- Parameter new_name should not be provided when creating a new volume.
- The size is a required parameter for expand volume.
- Clones or Snapshots of a deleted production volume or a clone are not
  deleted.
- A volume that is attached to a host/host group, or that is part of a volume
  group cannot be deleted.
- The Check_mode is not supported.
'''

EXAMPLES = r'''
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
'''

RETURN = r'''

changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"

volume_details:
    description: Details of the volume.
    returned: When volume exists
    type: complex
    contains:
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
                    description: The host ID mapped to the volume.
                    type: str
                name:
                    description: Name of the Host mapped to the volume.
                    type: str
        host_group:
            description: Host groups details mapped to the volume.
            type: complex
            contains:
                id:
                    description: The host group ID mapped to the volume.
                    type: str
                name:
                    description: Name of the Host group mapped to the volume.
                    type: str
        hlu_details:
            description: HLU details for mapped host/host group.
            type: complex
            contains:
                host_group_id:
                    description: The host group ID mapped to the volume.
                    type: str
                host_id:
                    description: The host ID mapped to the volume.
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

# Application type
APPLICATION_TYPE = 'Ansible/1.6.0'


class PowerStoreVolume(object):
    """Class with volume operations"""

    def __init__(self):
        """ Define all parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_volume_parameters())

        mutually_exclusive = [['vol_name', 'vol_id']]
        required_one_of = [['vol_name', 'vol_id']]

        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mutually_exclusive,
            required_one_of=required_one_of
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
            self.module.params, application_type=APPLICATION_TYPE)
        self.provisioning = self.conn.provisioning
        self.performance_policy_dict = {
            'low': 'default_low',
            'medium': 'default_medium',
            'high': 'default_high'
        }
        LOG.info('Got Py4Ps instance for provisioning on PowerStore %s',
                 self.conn)

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

    def create_volume(self, vol_name,
                      size,
                      volume_group_id,
                      protection_policy_id,
                      performance_policy,
                      description):
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
                volume_group_id=volume_group_id)
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
                      description):
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
                protection_policy_id=protection_policy_id)
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

    def map_unmap_volume_to_hostgroup(self, vol, hostgroup, mapping_state):
        host_group_identifier = self.module.params['hostgroup']
        current_hostgroups = vol['host_group']
        current_hostgroup_ids = []
        for hostgroup_t in current_hostgroups:
            current_hostgroup_ids.append(hostgroup_t['id'])

        if mapping_state == 'mapped' and hostgroup in current_hostgroup_ids:
            LOG.info('Volume %s is already mapped to hostgroup %s',
                     vol['name'], host_group_identifier)
            return False

        if mapping_state == 'mapped' and hostgroup not in\
                current_hostgroup_ids:
            hlu = self.module.params['hlu']
            LOG.info('Mapping volume %s to hostgroup %s with HLU %s',
                     vol['name'], host_group_identifier, hlu)
            try:
                self.provisioning.map_volume_to_host_group(
                    volume_id=vol['id'],
                    host_group_id=hostgroup,
                    logical_unit_number=hlu)
                return True
            except Exception as e:
                error_msg = (
                    'Mapping volume {0} to hostgroup {1} failed with error'
                    ' {2}' .format(vol['name'], host_group_identifier,
                                   str(e)))
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

        if mapping_state == 'unmapped' and hostgroup not in\
                current_hostgroup_ids:
            LOG.info('Volume %s is not mapped to hostgroup %s', vol['name'],
                     host_group_identifier)
            return False

        if mapping_state == 'unmapped' and hostgroup in current_hostgroup_ids:
            LOG.info('Unmapping volume %s from hostgroup %s', vol['name'],
                     host_group_identifier)
            try:
                self.provisioning.unmap_volume_from_host_group(
                    volume_id=vol['id'], host_group_id=hostgroup)
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
        hostgroup = self.get_host_group_id_by_name(
            self.module.params['hostgroup'])
        hlu = self.module.params['hlu']

        changed = False
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
                description=description)
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
                'size': size
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
                    description=update_dict['description']) or changed

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
                    volume, hostgroup, mapping_state) or changed

        if state == 'absent' and volume:
            LOG.info('Deleting volume %s ', volume['name'])
            changed = self.delete_volume(volume) or changed

        '''
        Finally update the module changed state and volume details
        '''

        self.result["changed"] = changed
        if state == 'present':
            self.result["volume_details"] = self.get_volume(vol_id=vol_id)
        self.module.exit_json(**self.result)

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
                    return host_group_info[0]['id']
            else:
                # Get the host group details using id
                if self.provisioning.get_host_group_details(host_group_name):
                    return host_group_name

            error_msg = ("host group {0} not found".format(host_group_name))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)
        except Exception as e:
            error_msg = "Get host group: {0} failed with " \
                        "error: {1}".format(host_group_name, str(e))
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
                 'size': vol['size']
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
        hlu=dict(required=False, type='int')
    )


def main():
    """ Create PowerStore volume object and perform action on it
        based on user input from playbook"""
    obj = PowerStoreVolume()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
