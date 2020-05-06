#!/usr/bin/python
# Copyright: (c) 2019, DellEMC

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils import dellemc_ansible_utils as utils
import logging

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r'''
---
module: dellemc_powerstore_volume
version_added: '2.6'
short_description:  Manage volumes on PowerStore storage system
description:
- Managing volume on PowerStore storage system includes create volume, get
  details of volume, modify name, size, description, protection policy,
  performance policy, map or unmap volume to host/host group and delete volume
author:
- Ambuj Dubey (Ambuj.Dubey@emc.com)
- Manisha Agrawal (Manisha.Agrawal@dell.com)
extends_documentation_fragment:
  - dellemc.dellemc_powerstore
options:
  vol_name:
    description:
    - Unique name of the volume. This value must contain 128 or fewer printable
      unicode characters.
    - Required when creating a volume. All other functionalities on a volume
      are supported using volume name or ID.
  vg_name:
    description:
    - The name of the volume group. A volume can optionally be assigned to a
      volume group at the time of creation.
    - Use the Volume Group Module for modification of the assignment.
  vol_id:
    description:
    - The 36 character long ID of the volume, automatically generated
      when a volume is created.
    - Cannot be used while creating a volume. All other functionalities on a
      volume are supported using volume name or ID.
  size:
    description:
    - Size of the volume. Minimum volume size is 1MB. Maximum volume size is
      256TB. Size must be a multiple of 8192.
    - Required in case of create and expand volume.
  cap_unit:
    description:
    - Volume size unit.
    - Used to signify unit of the size provided for creation and expansion of
      volume.
    default: GB
    choices: [MB, GB, TB]
  new_name:
    description:
    - The new volume name for the volume, used in case of rename functionality.
  description:
    description:
    - Description for the volume.
    - Optional parameter when creating a volume.
    - To modify, pass the new value in description field.
  protection_policy:
    description:
    - The protection_policy of the volume.
    - To represent policy, both name or ID can be used interchangably.
      The module will detect both.
    - A volume can be assigned a protection policy at the time of creation of
      volume or later as well.
    - The policy can also be changed for a given volume, by simply passing the
      new value.
    - The policy can be removed by passing an empty string.
    - Check examples for more clarity.
  performance_policy:
    description:
    - The performance_policy for the volume.
    - A volume can be assigned a performance policy at the time of creation of
      volume or later as well.
    - The policy can also be changed for a given volume, by simply passing the
      new value.
    - Check examples for more clarity.
    default: medium
    choices: [high, medium, low]
  host:
    description:
    - Host to be mapped/unmapped to a volume. If not specified, an unmapped
      volume is created. Only one of host or host group can be supplied in one
      call.
    - To represent host, both name or ID can be used interchangeably.
      The module will detect both.
  hostgroup:
    description:
    - Hostgroup to be mapped/unmapped to a volume. If not specified, an
      unmapped volume is created.
    - Only one of host or host group can be mapped in one call.
    - To represent hostgroup, both name or ID can be used interchangeably. The
      module will detect both.
  mapping_state:
    description:
    - Define whether the volume should be mapped to a host or hostgroup.
    - mapped - indicates that the volume should be mapped to the host or host
      group.
    - unmapped - indicates that the volume should not be mapped to the host or
      host group.
    - Only one of host or host group can be supplied in one call.
    choices: [mapped, unmapped]
  hlu:
    description:
    - Logical unit number for the host/host group volume access.
    - Optional parameter when mapping a volume to host/host group.
    - HLU modification is not supported.
    required: False
  state:
    description:
    - Define whether the volume should exist or not.
    - present - indicates that the volume should exist on the system.
    - absent - indicates that the volume should not exist on the system.
    required: true
    choices: [absent, present]

Notes:
- To create a new volume, vol_name and size is required. cap_unit, description,
  vg_name, performance policy, protection policy are optional.
- new_name  should not be provided when creating a new volume.
- size is a required parameter for expand volume.
- Clones or snapshots of a deleted production volume or a clone are not
  deleted.
- A volume that is attached to a host/host group or is part of a volume group
  cannot be deleted.
  '''

EXAMPLES = r'''
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
'''

RETURN = r'''
'''

LOG = utils.get_logger('dellemc_powerstore_volume', log_devel=logging.INFO)

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.0'

class PowerStoreVolume(object):
    """Class with volume operations"""

    def __init__(self):
        """ Define all parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(self.get_powerstore_volume_parameters())

        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params, supports_check_mode=True)

        LOG.info(
            'HAS_PY4PS = {0} , IMPORT_ERROR = {1}'.format(
                HAS_PY4PS, IMPORT_ERROR))
        if HAS_PY4PS is False:
            self.module.fail_json(msg=IMPORT_ERROR)
        LOG.info(
            'IS_SUPPORTED_PY4PS_VERSION = {0} , VERSION_ERROR = {1}'.format(
                IS_SUPPORTED_PY4PS_VERSION,
                VERSION_ERROR))
        if IS_SUPPORTED_PY4PS_VERSION is False:
            self.module.fail_json(msg=VERSION_ERROR)

        # result is a dictionary that contains changed status and
        # volume details
        self.result = {"changed": False, "volume_details": {}}
        self.conn = utils.get_powerstore_connection(self.module.params,
          application_type=APPLICATION_TYPE)
        self.provisioning = self.conn.provisioning
        self.performance_policy_dict = {
            'low': 'default_low',
            'medium': 'default_medium',
            'high': 'default_high'
        }
        LOG.info(
            'Got Py4Ps instance for provisioning on PowerStore {0}'.format(
                self.conn))

    def get_volume(self):
        """Get volume details"""
        try:
            vol_id = self.module.params['vol_id']
            if vol_id is not None:
                return self.provisioning.get_volume_details(vol_id)
            else:
                volume_name = self.module.params['vol_name']
                volume_info = self.provisioning.get_volume_by_name(volume_name)
                if volume_info:
                    if len(volume_info) > 1:
                        error_msg = 'Multiple volumes by the same name found'
                        LOG.error(error_msg)
                        self.module.fail_json(msg=error_msg)
                    return volume_info[0]
                return None
        except Exception as e:
            LOG.error('Got error {0} while getting details of volume '.format(
                str(e)))
        return None

    def create_volume(self, vol_name,
                      size,
                      volume_group_id,
                      protection_policy_id,
                      performance_policy,
                      description):
        """Create PowerStore volume"""

        try:
            msg = (
                "Creating volume {0} of size {1} with performance policy {2}, "
                "protection_policy {3}, description {4} and volume_group {5}" .format(
                    vol_name,
                    size,
                    performance_policy,
                    protection_policy_id,
                    description,
                    volume_group_id))
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
            self.module.fail_json(msg=msg)

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
            self.module.fail_json(msg=msg)

    def map_unmap_volume_to_host(self, vol, host, mapping_state):
        current_hosts = vol['host']
        current_host_ids = []
        host_identifier = self.module.params['host']
        for host_t in current_hosts:
            current_host_ids.append(host_t['id'])

        if mapping_state == 'mapped' and host in current_host_ids:
            LOG.info(
                'Volume {0} is already mapped to host {1}'.format(
                    vol['name'], host_identifier))
            return False

        if mapping_state == 'mapped' and host not in current_host_ids:
            hlu = self.module.params['hlu']
            LOG.info(
                'Mapping volume {0} to host {1} with HLU {2}'.format(
                    vol['name'], host_identifier, hlu))
            try:
                self.provisioning.map_volume_to_host(
                    volume_id=vol['id'],
                    host_id=host,
                    logical_unit_number=hlu)
                return True
            except Exception as e:
                error_msg = (
                    'Mapping volume {0} to host {1} failed with error {2}' .format(
                        vol['name'], host_identifier, str(e)))
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)

        if mapping_state == 'unmapped' and host not in current_host_ids:
            LOG.info(
                'Volume {0} is not mapped to host {1}'.format(
                    vol['name'], host_identifier))
            return False

        if mapping_state == 'unmapped' and host in current_host_ids:
            LOG.info(
                'Unmapping volume {0} from host {1}'.format(
                    vol['name'], host_identifier))
            try:
                self.provisioning.unmap_volume_from_host(volume_id=vol['id'],
                                                         host_id=host)
                return True
            except Exception as e:
                error_msg = (
                    'Unmapping volume {0} from host {1} failed with error {2}' .format(
                        vol['name'], host_identifier, str(e)))
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)
        return False

    def map_unmap_volume_to_hostgroup(self, vol, hostgroup, mapping_state):
        host_group_identifier = self.module.params['hostgroup']
        current_hostgroups = vol['host_group']
        current_hostgroup_ids = []
        for hostgroup_t in current_hostgroups:
            current_hostgroup_ids.append(hostgroup_t['id'])

        if mapping_state == 'mapped' and hostgroup in current_hostgroup_ids:
            LOG.info(
                'Volume {0} is already mapped to hostgroup {1}'.format(
                    vol['name'], host_group_identifier))
            return False

        if mapping_state == 'mapped' and hostgroup not in current_hostgroup_ids:
            hlu = self.module.params['hlu']
            LOG.info(
                'Mapping volume {0} to hostgroup {1} with HLU {2}'.format(
                    vol['name'], host_group_identifier, hlu))
            try:
                self.provisioning.map_volume_to_host_group(
                    volume_id=vol['id'],
                    host_group_id=hostgroup,
                    logical_unit_number=hlu)
                return True
            except Exception as e:
                error_msg = (
                    'Mapping volume {0} to hostgroup {1} failed with error {2}' .format(
                        vol['name'], host_group_identifier, str(e)))
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)

        if mapping_state == 'unmapped' and hostgroup not in current_hostgroup_ids:
            LOG.info(
                'Volume {0} is not mapped to hostgroup {1}'.format(
                    vol['name'], host_group_identifier))
            return False

        if mapping_state == 'unmapped' and hostgroup in current_hostgroup_ids:
            LOG.info(
                'Unmapping volume {0} from hostgroup {1}'.format(
                    vol['name'], host_group_identifier))
            try:
                self.provisioning.unmap_volume_from_host_group(
                    volume_id=vol['id'], host_group_id=hostgroup)
                return True
            except Exception as e:
                error_msg = (
                    'Unmapping volume {0} from hostgroup{1} failed with error {2}' .format(
                        vol['name'], host_group_identifier, str(e)))
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)
        return False

    def delete_volume(self, volume):
        """
        Delete volume from system
        """
        try:
            LOG.info('Deleting volume {0}'.format(volume['name']))
            self.provisioning.delete_volume(volume['id'])
            return True
        except Exception as e:
            error_msg = 'Delete volume {0} failed with error {1}'.format(
                volume['name'], str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def perform_module_operation(self):
        """
        Perform different actions on volume based on user parameters
        chosen in playbook
        """
        size = self.module.params['size']
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

        if vol_id is None and vol_name is None:
            self.module.fail_json(
                msg='Specify either Volume ID or Volume name')
        elif vol_id is not None and vol_name is not None:
            self.module.fail_json(msg='Specify Volume ID or Volume name,'
                                      ' not both')
        changed = False
        volume = self.get_volume()
        if volume is not None:
            vol_id = volume['id']
        if size:
            size = int(utils.get_size_bytes(size, self.module.params[
                'cap_unit']))
        # Call to create volume
        if state == 'present' and volume is None:
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
                volume = self.get_volume()

        if state == 'present' and volume:
            if host and hostgroup:
                msg = 'Only one of host or hostgroup can be mapped to a volume in one call'
                LOG.info(msg)
                self.module.fail_json(msg=msg)
            hlu_mod_flag = True
            if host and hlu:
                hlu_mod_flag, error = self.check_for_hlu_modification(
                    volume, host=host, hlu=hlu)
            if hostgroup and hlu:
                hlu_mod_flag, error = self.check_for_hlu_modification(
                    volume, hostgroup=hostgroup, hlu=hlu)
            if hlu_mod_flag is False:
                msg = 'Modification of HLU is not supported. {0}'.format(error)
                LOG.info(msg)
                self.module.fail_json(msg=msg)
            vg_mod_flag = True
            if(volume['volume_groups']):
                if len(volume['volume_groups']) > 0:
                    # check for modification of VG
                    if volume_group_id is not None and volume_group_id != volume[
                            'volume_groups'][0]['id']:
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
                    msg = (
                        "Current volume size {0} B is greater than {1} B "
                        "specified. Only expansion of volume size is allowed" .format(
                            current_size, size))
                    LOG.info(msg)
                    self.module.fail_json(msg=msg)

                if current_size == size:
                    # passing the same size to the API results in a error, hence
                    # sending None instead which indicates no change
                    msg = (
                        'Current volume size {0} B is same as {1} B specified' .format(
                            current_size, size))
                    LOG.info(msg)
                    size = None

            new_volume_dict = {
                'name': name,
                'description': description,
                'protection_policy_id': protection_policy_id,
                'performance_policy_id': performance_policy,
                'size': size
            }

            if(self.check_modify_volume_required(volume, new_volume_dict)):
                if mapping_state is not None or hlu is not None:
                    msg = 'Volume modification and host mapping cannot be done in the same call'
                    LOG.info(msg)
                    self.module.fail_json(msg=msg)
                changed = self.modify_volume(
                    vol_id=vol_id,
                    old_volume_name=volume['name'],
                    name=name,
                    size=size,
                    protection_policy_id=protection_policy_id,
                    performance_policy=performance_policy,
                    description=description) or changed
                if changed and name is not vol_name:
                    self.module.params['vol_name'] = new_name

        if state == 'present' and volume and mapping_state in [
                None, 'unmapped']:
            if hlu:
                error_msg = 'Invalid paramter HLU provided'
                LOG.info(error_msg)
                self.module.fail_json(msg=error_msg)

        if host or hostgroup:
            if state == 'present' and volume and mapping_state is None:
                error_msg = 'Mapping state not provided, mandatory for mapping'
                LOG.info(error_msg)
                self.module.fail_json(msg=error_msg)

        if state == 'present' and volume and mapping_state:
            if not host and not hostgroup:
                msg = 'Specify either host or hostgroup to be mapped to a volume'
                LOG.info(msg)
                self.module.fail_json(msg=msg)

            if host:
                changed = self.map_unmap_volume_to_host(
                    volume, host, mapping_state) or changed
            if hostgroup:
                changed = self.map_unmap_volume_to_hostgroup(
                    volume, hostgroup, mapping_state) or changed

        if state == 'absent' and volume:
            LOG.info('Deleting volume {0} '.format(volume['name']))
            changed = self.delete_volume(volume) or changed

        '''
        Finally update the module changed state and volume details
        '''

        self.result["changed"] = changed
        if state == 'present':
            self.result["volume_details"] = self.get_volume()
        self.module.exit_json(**self.result)

    def get_powerstore_volume_parameters(self):
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
            cap_unit=dict(required=False, choices=['MB', 'GB', 'TB'], type='str',
                          default='GB'),
            state=dict(required=True, choices=['present', 'absent'], type='str'),
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

    def get_volume_id_by_name(self, volume_name):
        volume_info = self.provisioning.get_volume_by_name(volume_name)
        if volume_info:
            if len(volume_info) > 1:
                error_msg = 'Multiple volumes by the same name found'
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)
            return volume_info[0]['id']
        return None

    def get_volume_group_id_by_name(self, volume_group_name):
        if volume_group_name is None:
            return None
        if len(volume_group_name) == 36:
            try:
                if self.provisioning.get_volume_group_details(
                        volume_group_name):
                    return volume_group_name
            except Exception as e:
                LOG.info(
                    'Unable to get details of volume group ID: {0} -- error: {1}, trying name instead' .format(
                        volume_group_name, str(e)))
        volume_group_info = self.provisioning.get_volume_group_by_name(
            volume_group_name)
        if volume_group_info:
            if len(volume_group_info) > 1:
                error_msg = 'Multiple volume groups by the same name found'
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)
            return volume_group_info[0]['id']
        else:
            error_msg = ("volume group {0} not found".format(
                volume_group_name))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)
        return None

    def get_protection_policy_id_by_name(self, protection_policy_name):
        if protection_policy_name is None:
            return None
        if (len(protection_policy_name) == 0):
            return ''
        if len(protection_policy_name) == 36:
            try:
                if self.conn.protection.get_protection_policy_details(
                        protection_policy_name):
                    return protection_policy_name
            except Exception as e:
                LOG.info(
                    'Unable to get details of protection policy ID: {0} -- error: {1}, , trying name instead' .format(
                        protection_policy_name, str(e)))
        protection_policy_info = self.conn.protection.get_protection_policy_by_name(
            protection_policy_name)
        if protection_policy_info:
            if len(protection_policy_info) > 1:
                error_msg = 'Multiple protection policies by the same name found'
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)
            return protection_policy_info[0]['id']
        else:
            error_msg = ("protection policy {0} not found".format(
                protection_policy_name))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)
        return None

    def get_host_id_by_name(self, host_name):
        if host_name is None:
            return None
        if len(host_name) == 36:
            try:
                if self.provisioning.get_host_details(host_name):
                    return host_name
            except Exception as e:
                LOG.info(
                    'Unable to get details of host group ID: {0} -- error: {1}, trying name instead' .format(
                        host_name, str(e)))

        host_info = self.provisioning.get_host_by_name(host_name)
        if host_info:
            if len(host_info) > 1:
                error_msg = 'Multiple hosts by the same name found'
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)
            return host_info[0]['id']
        else:
            error_msg = ("Host {0} not found".format(
                host_name))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)
        return None

    def get_host_group_id_by_name(self, host_group_name):
        if host_group_name is None:
            return None
        if len(host_group_name) == 36:
            try:
                if self.provisioning.get_host_group_details(
                        host_group_name):
                    return host_group_name
            except Exception as e:
                LOG.info(
                    'Unable to get details of host group ID: {0} -- error: {1}, trying name instead'
                    .format(host_group_name, str(e)))
        host_group_info = self.provisioning.get_host_group_by_name(
            host_group_name)
        if host_group_info:
            if len(host_group_info) > 1:
                error_msg = 'Multiple host groups by the same name found'
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)
            return host_group_info[0]['id']
        else:
            error_msg = ("Host group {0} not found".format(
                host_group_name))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)
        return None

    def get_performance_policy(self, performance_policy):
        if performance_policy is None:
            return None
        else:
            return self.performance_policy_dict.get(performance_policy)

    def check_modify_volume_required(self, vol, vol_dict2):
        vol_dict1 = {
            'name': vol['name'],
            'description': vol['description'],
            'protection_policy_id': vol['protection_policy_id'],
            'performance_policy_id': vol['performance_policy_id'],
            'size': vol['size']
        }
        """to compare two volumes"""
        for key in vol_dict1.keys():
            if key in vol_dict2.keys():
                if vol_dict2[key] is not None and vol_dict1[key] != vol_dict2[key]:
                    if key == 'protection_policy_id' and vol_dict1[key] is None and vol_dict2[key] == '':
                        pass
                    else:
                        LOG.debug(
                            "Key {0} in vol_dict1={1},vol_dict2={2}".format(
                                key, vol_dict1[key], vol_dict2[key]))
                        return True
        LOG.info('No change detected')
        return False
    
    def check_for_hlu_modification(
            self,
            volume,
            hlu,
            host=None,
            hostgroup=None):
        hlu_details = volume['hlu_details']
        if host:
            for element in hlu_details:
                if element.get('host_id') == host:
                    if int(element['logical_unit_number']) != hlu:
                        msg = 'Modification of HLU from {0} to {1} for host {2} was attempted'.format(
                            int(element['logical_unit_number']), hlu, host)
                        return False, msg
        if hostgroup:
            for element in hlu_details:
                if element.get('host_group_id') == hostgroup:
                    if int(element['logical_unit_number']) != hlu:
                        msg = 'Modification of HLU from {0} to {1} for hostgroup {2} was attempted'.format(
                            int(element['logical_unit_number']), hlu, hostgroup)
                        return False, msg
        return True, ""

def main():
    """ Create PowerStore volume object and perform action on it
        based on user input from playbook"""
    obj = PowerStoreVolume()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
