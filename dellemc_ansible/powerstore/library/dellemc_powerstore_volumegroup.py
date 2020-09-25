#!/usr/bin/python
# Copyright: (c) 2019, DellEMC

from ansible.module_utils.basic import AnsibleModule
from PyPowerStore.utils.exception import PowerStoreException
from ansible.module_utils.storage.dell import \
    dellemc_ansible_powerstore_utils as utils
import logging

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r'''
---
module: dellemc_powerstore_volumegroup
version_added: '2.7'
short_description: Manage volume groups on PowerStore Storage System
description:
- Managing volume group on PowerStore Storage System includes
  creating new volume group, adding volumes to volume
  group, removing volumes from volume group, renaming volume group,
  modifying volume group and deleting volume group.
author:
- Akash Shendge (@shenda1) <ansible.team@dell.com>
- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
extends_documentation_fragment:
  - dellemc_powerstore.dellemc_powerstore
options:
  vg_name:
    description:
    - The name of the volume group.
    required: False
  vg_id:
    description:
    - The id of the volume group.
    - It can be used only for Modify, Add/Remove or Delete operation.
    required: False
  volumes:
    description:
    - This is a list of volumes. 
    - Either the volume ID or name must be provided for adding/removing 
      existing volumes from volume group.
    - If volumes are given, then vol_state should also be specified.
  vol_state:
    description:
    - String variable , describes the state of volumes inside VG
    - If volume are given, then vol_state should also be specified.
    choices: [present-in-group , absent-in-group]
  new_vg_name:
    description:
     - The new name of the volume group.
  description:
    description:
    - Description about the volume group.
  protection_policy:
    description:
    - String variable, represents Protection policy id or name 
      used for volume group.
    - Specifying an empty string or "" removes the existing 
      protection policy from Volume Group.
    required: false
  is_write_order_consistent:
    description:
    - A boolean flag to indicate whether snapshot sets of the volume group will be write-order consistent.
    - If this parameter is not specified, the array by default sets it to true.
    required: false    
  state:
    description:
    - Define whether the volume group should exist or not.
    choices: [absent, present]
    required: true
Notes:
- vol_state is mandatory if volumes are provided.
- A protection policy can be specified either for an volume group, or 
  for the individual volumes inside the volume group.  
- A volume can be a member of at most one volume group.
- Specifying "protection_policy" as empty string or "" removes the existing 
  protection policy from a Volume Group. 
  
'''

EXAMPLES = r'''
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
      
'''

RETURN = r'''

changed:
    description: Whether or not the resource has changed
    returned: always
    type: bool

add_vols_to_vg:
    description: A boolean flag to indicate whether volume/s got added to
     volume group
    returned: When value exists
    type: bool

create_vg:
    description: A boolean flag to indicate whether volume group got created
    returned: When value exists
    type: bool

delete_vg:
    description: A boolean flag to indicate whether volume group got deleted
    returned: When value exists
    type: bool

modify_vg:
    description:
        - A boolean flag to indicate whether volume group got modified
    type: bool

remove_vols_from_vg:
    description: A boolean flag to indicate whether volume/s got removed from
     volume group
    returned: When value exists
    type: bool

volume_group_details:
    description: Details of the volume group
    returned: When volume group exists
    type: complex
    contains:
        id:
            description:
                - The system generated ID given to the volume group
            type: str
        name:
            description:
                - Name of the volume group 
            type: str
        description:
            description:
                - description about the volume group
            type: str
        protection_policy_id:
            description:
                - The protection policy of the volume group
            type: str
        is_write_order_consistent:
            description:
                - A boolean flag to indicate whether snapshot sets of the
                 volume group will be write-order consistent
            type: bool
        type:
            description:
                - The type of the volume group
            type: str
        volumes:
            description:
                - The volumes details of the volume group
            type: complex
            contains:
                id:
                    description:
                        - The system generated ID given to the volume
                         associated with the volume group
                    type: str
'''

LOG = utils.get_logger('dellemc_powerstore_volumegroup',
                       log_devel=logging.INFO)

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.1'


class PowerStoreVolumeGroup(object):
    """Class with Volume Group operations"""

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_volume_group_parameters())

        mutually_exclusive = [['vg_name', 'vg_id']]
        required_one_of = [['vg_name', 'vg_id']]
        required_together = [['volumes', 'vol_state']]

        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mutually_exclusive,
            required_one_of=required_one_of,
            required_together=required_together
        )

        LOG.info('HAS_PY4PS = {0} , IMPORT_ERROR = {1}'.format(
                 HAS_PY4PS, IMPORT_ERROR))
        if not HAS_PY4PS:
            self.module.fail_json(msg=IMPORT_ERROR)
        LOG.info('IS_SUPPORTED_PY4PS_VERSION = {0} , '
                 'VERSION_ERROR = {1}'.format(
                  IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR))
        if not IS_SUPPORTED_PY4PS_VERSION:
            self.module.fail_json(msg=VERSION_ERROR)

        self.conn = utils.get_powerstore_connection(self.module.params,
          application_type=APPLICATION_TYPE)
        self.provisioning = self.conn.provisioning
        LOG.info('Got Py4ps instance for provisioning on PowerStore {0}'.
                 format(self.conn))
        self.protection = self.conn.protection
        LOG.info('Got Py4ps instance for protection on PowerStore {0}'.
                 format(self.protection))

    def get_volume_group_details(self, vg_id=None, name=None):
        """Get volume group details"""
        try:
            LOG.info("Getting VG Details {0} {1}".format(vg_id, name))

            if vg_id:
                resp = self.provisioning.get_volume_group_details(vg_id)
                LOG.info("Successfully Got VG with id {0}".format(vg_id))
                if len(resp) > 0:
                    return resp
                else:
                    return None

            if name:
                resp = self.provisioning.get_volume_group_by_name(name)
                if resp and len(resp) > 0:
                    id = resp[0]['id']
                    vg_details = self.provisioning.\
                        get_volume_group_details(id)
                    LOG.info("Successfully Got VG with name {0}".format(name))
                    return vg_details
            return None
        except Exception as e:
            id_or_name = vg_id if vg_id else name
            errormsg = "Failed to get volume group {0} with error {1}". \
                format(id_or_name, str(e))
            if isinstance(e, PowerStoreException) and \
                    e.err_code == PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(errormsg)
                return None
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def delete_volume_group(self, volume_group_id):
        """Delete volume group"""
        try:
            self.provisioning.delete_volume_group(volume_group_id)
            return True

        except PowerStoreException as pe:
            errormsg = "Failed to delete volume group {0} with error {1}". \
                format(volume_group_id, str(pe))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

        except Exception as e:
            errormsg = "Failed to delete volume group {0} with error {1}".\
                format(volume_group_id, str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def get_volume_id_by_name(self, vol_name):
        """Get the details of a volume by name"""

        try:
            resp = self.provisioning.get_volume_by_name(vol_name)
            if len(resp) > 0:
                return resp[0]['id']
            else:
                return None

        except Exception as e:
            msg = "Failed to get the volume with name {0} with " \
                  "error {1}".format(vol_name, str(e))
            LOG.error(msg)

    def get_volume_details_by_id(self, volume_id):
        """Get the details of a volume by name"""

        try:
            LOG.info("getting volume with id {0}".format(volume_id))
            resp = self.provisioning.get_volume_details(volume_id)
            if len(resp) > 0:
                LOG.info("got volume with id {0} is {1}".format(volume_id, resp))
                return resp['id']
            else:
                return None

        except Exception as e:
            msg = "Failed to get the volume with id {0} with " \
                  "error {1}".format(volume_id, str(e))
            LOG.error(msg)

    def remove_volumes_from_volume_group(self, vg_id, vol_list):
        """Remove volumes from volume group"""

        vol_group_details = self.get_volume_group_details(vg_id=vg_id)
        existing_volumes_in_vg = vol_group_details['volumes']
        LOG.debug("Existing Volumes: {0}".format(existing_volumes_in_vg))

        existing_vol_ids = []
        for vol in existing_volumes_in_vg:
            if vol:
                existing_vol_ids.append(vol['id'])

        LOG.debug("Existing Volume IDs {0}".format(existing_vol_ids))

        ids_to_remove = []

        vol_name_list = []
        vol_id_list = []

        for each_vol in vol_list:
            if each_vol:
                identifier_type = utils.name_or_id(each_vol)
                if identifier_type == "ID" and not (each_vol in vol_id_list):
                    vol_id_list.append(each_vol)
                elif identifier_type == "NAME" and not (each_vol in vol_name_list):
                    vol_name_list.append(each_vol)

        """remove by name"""
        for vol in vol_name_list:
            id = self.get_volume_id_by_name(vol)
            if id and (id in existing_vol_ids):
                if id not in ids_to_remove:
                    ids_to_remove.append(id)
            else:
                msg = "Unable to remove volume name {0} since is not " \
                      "present in volume group {1}".format(vol, vg_id)
                LOG.warn(msg)
                self.module.fail_json(msg=msg)

        """remove by id"""
        for vol in vol_id_list:
            if vol in existing_vol_ids:
                if vol not in ids_to_remove:
                    ids_to_remove.append(vol)
                else:
                    msg = "Unable to remove volume id {0} since is not " \
                          "present in volume group {1}".format(vol, vg_id)
                    LOG.warn(msg)
                    self.module.fail_json(msg=msg)

        LOG.debug("Volume IDs to Remove {0}".format(ids_to_remove))

        if len(ids_to_remove) == 0:
            return False

        try:
            self.provisioning.remove_members_from_volume_group(
                vg_id, ids_to_remove)

            return True

        except PowerStoreException as pe:
            errormsg = "Remove existing volume(s) from volume group {0} " \
                       "failed with error {1}".format(vg_id, str(pe))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

        except Exception as e:
            errormsg = "Remove existing volume(s) from volume group {0} " \
                       "failed with error {1}".format(vg_id, str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def add_volumes_to_volume_group(self,vg_id, vol_list):
        """adds volumes to volume group"""

        vol_group_details = self.get_volume_group_details(vg_id=vg_id)
        existing_volumes_in_vg = vol_group_details['volumes']
        LOG.debug("Existing Volumes: {0}".format(existing_volumes_in_vg))
        existing_vol_ids = []
        for vol in existing_volumes_in_vg:
            if vol:
                existing_vol_ids.append(vol['id'])

        LOG.debug("Existing Volume IDs {0}".format(existing_vol_ids))

        ids_to_add = []
        vol_name_list = []
        vol_id_list = []

        for each_vol in vol_list:
            if each_vol:
                identifier_type = utils.name_or_id(each_vol)
                if identifier_type == "ID" and not (each_vol in vol_id_list):
                    vol_id_list.append(each_vol)
                elif identifier_type == "NAME" and not (each_vol in vol_name_list):
                    vol_name_list.append(each_vol)

        """add volume by name"""
        for vol in vol_name_list:
            id = self.get_volume_id_by_name(vol)
            if id and (id not in existing_vol_ids):
                if id not in ids_to_add:
                    ids_to_add.append(id)
            else:
                msg = "Unable to add volume name {0}, either it doesn't" \
                      " exist or already in volume group ".format(vol)
                LOG.warn(msg)
                self.module.fail_json(msg=msg)

        """add volume by id"""
        for vol in vol_id_list:
            """verifying if volume id exists in array"""
            vol_by_id = self.get_volume_details_by_id(volume_id=vol)

            if vol_by_id not in existing_vol_ids:
                if vol_by_id not in ids_to_add:
                    ids_to_add.append(vol_by_id)
            else:
                msg = "Unable to add volume id {0}, either it doesn't" \
                      " exist or already in volume group ".format(vol)
                LOG.warn(msg)
                self.module.fail_json(msg=msg)

        LOG.debug("Volume IDs to add {0}".format(ids_to_add))

        if len(ids_to_add) == 0:
            return False

        try:
            self.provisioning.add_members_to_volume_group(
                vg_id, ids_to_add)

            return True
        except PowerStoreException as pe:
            errormsg = "Add existing volumes to volume group {0} " \
                       "failed with error {1}".format(vg_id, str(pe))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

        except Exception as e:
            errormsg = "Add existing volumes to volume group {0} " \
                       "failed with error {1}".format(vg_id, str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def modify_volume_group(self, vg_id, vg_name, description,
                            is_write_order_consistent,
                            protection_policy_id):
        """Modify volume group"""
        try:
            LOG.info("Modifying volume group: {0}".format(
                vg_id))

            self.provisioning.modify_volume_group(
                vg_id, vg_name, description, is_write_order_consistent,
                protection_policy_id)

            LOG.info("Successfully modified volume group: {0}".format(
                vg_id))

            return True

        except PowerStoreException as pe:
            errormsg = "Modify volume group {0} failed with error {1}". \
                format(vg_id, str(pe))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

        except Exception as e:
            errormsg = "Modify volume group {0} failed with error {1}".\
                format(vg_id, str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def is_volume_group_modified(self, volume_group,protection_policy):
        """Check if the desired volume group state is different from existing
        volume group"""
        modified = False

        if(('name' in volume_group and self.module.params['new_vg_name']
            is not None) and (volume_group['name'].lower() !=
                              self.module.params['new_vg_name'].lower())):
            modified = True
        elif((volume_group['description'] is not None and self.module.params[
            'description'] is not None and volume_group['description'].lower()
              != self.module.params['description'].lower()) or
             (volume_group['description'] is None and
              self.module.params['description'] is not None and
              self.module.params['description'].lower() != 'none')):
            modified = True
        elif(('protection_policy_id' in volume_group and
              protection_policy is not None and
              volume_group['protection_policy_id'] !=
              protection_policy) or
                ('protection_policy_id' not in volume_group and
                 protection_policy is not None and
                 protection_policy.lower() != 'none')):
            modified = True
        elif('is_write_order_consistent' in volume_group and
                self.module.params['is_write_order_consistent'] is not None
                and volume_group['is_write_order_consistent'] !=
                self.module.params['is_write_order_consistent']):
            modified = True

        return modified

    def create_volume_group(self, vg_name,
                            description,
                            protection_policy_id,
                            is_write_order_consistent):
        """Create a volume group"""
        try:
            LOG.info('Creating empty volume group {0} '.format(vg_name))
            resp = self.provisioning.create_volume_group(
                vg_name, description,
                protection_policy_id=protection_policy_id,
                is_write_order_consistent=is_write_order_consistent)
            return True, resp

        except PowerStoreException as pe:
            errormsg = "Failed to create volume group {0} with error {1}". \
                format(vg_name, str(pe))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

        except Exception as e:
            errormsg = "Failed to create volume group {0} with error {1}".\
                format(vg_name, str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def get_protection_policy_id_by_name(self, name):
        """Get protection policy by name"""
        try:
            LOG.info('Getting the details of protection policy '
                     '{0}'.format(name))
            resp = self.protection.get_protection_policy_by_name(name)
            if None is resp or len(resp) <= 0:
                msg = 'No protection policy present with name {0}'.format(
                    name)
                LOG.error(msg)
                self.module.fail_json(msg=msg)
            else:
                LOG.info('Successfully got the protection policy '
                         'name {0}'.format(name))
                return resp[0]['id']

        except Exception as e:
            msg = 'Get details of protection policy name: {0} failed' \
                  ' with error : {1} '.format(name, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_protection_policy_details_by_id(self, policy_id):
        """Get protection policy details by id"""

        try:
            LOG.info('Getting the details of protection policy by id'
                     ' {0}'.format(policy_id))
            resp = self.protection.get_protection_policy_details(
                policy_id=policy_id)
            if resp and len(resp) > 0:
                LOG.info('Successfully got the details of '
                         'protection policy id {0}'.format(policy_id))

                return resp['id']
            else:
                msg = 'No protection policy present with id {0}'.format(
                    policy_id)
                LOG.error(msg)
                self.module.fail_json(msg=msg)

        except Exception as e:
            msg = 'Get details of protection policy id: {0} failed' \
                  ' with error {1}'.format(policy_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def perform_module_operation(self):
        """
        Perform different actions on volume group based on user parameter
        chosen in playbook
        """

        vg_id = self.module.params['vg_id']
        state = self.module.params['state']
        vg_name = self.module.params['vg_name']
        volumes = self.module.params['volumes']
        vol_state = self.module.params['vol_state']
        new_vg_name = self.module.params['new_vg_name']
        description = self.module.params['description']
        protection_policy = self.module.params['protection_policy']
        is_write_order_consistent = self.module.params[
            'is_write_order_consistent']

        volume_group = None

        volume_group = self.get_volume_group_details(vg_id=vg_id, name=vg_name)
        LOG.debug('volume_group details: {0}'.format(volume_group))

        if protection_policy:
            prot_pol_identifier_type = utils.name_or_id(protection_policy)
            if prot_pol_identifier_type == "ID":
                protection_policy = self.get_protection_policy_details_by_id(
                    protection_policy)
            if prot_pol_identifier_type == "NAME":
                protection_policy = self.get_protection_policy_id_by_name(
                    protection_policy)

        modified = False

        if volume_group:
            modified = self.is_volume_group_modified(volume_group,protection_policy)
            LOG.debug('Modified Flag: {0}'.format(modified))
        else:
            if not vg_name:
                self.module.fail_json(msg="vg_name is required to "
                                          "create a Volume Group")
            if new_vg_name:
                self.module.fail_json(msg="Invalid argument, "
                                          "new_vg_name is not required")

        if vg_id is None and volume_group:
            vg_id = volume_group['id']
        if vg_name is None and volume_group:
            vg_name = volume_group['name']

        result = dict(
            changed=False,
            create_vg='',
            modify_vg='',
            add_vols_to_vg='',
            remove_vols_from_vg='',
            delete_vg='',
            volume_group_details='',
        )

        if state == 'present' and not volume_group:
            LOG.info('Creating volume group {0}'.format(vg_name))
            result['create_vg'], resp = self.\
                create_volume_group(vg_name, description,
                                    protection_policy,
                                    is_write_order_consistent)
            result['volume_group_details'] = resp
            volume_group = self.get_volume_group_details(vg_id=resp['id'])
            vg_id = volume_group['id']
        elif state == 'absent' and volume_group:
            LOG.info('Deleting volume group {0}'.format(vg_id))
            result['delete_vg'] = self.delete_volume_group(vg_id)

        if state == 'present' and vol_state == 'present-in-group' and \
                volume_group and volumes:
            result['add_vols_to_vg'] = self.add_volumes_to_volume_group(
                vg_id, volumes)
        elif state == 'present' and vol_state == 'absent-in-group' and \
                volume_group and volumes:
            LOG.info('Remove existing volume(s) from volume group {0}'.
                     format(vg_id))
            result['remove_vols_from_vg'] = self.\
                remove_volumes_from_volume_group(vg_id, volumes)

        if state == 'present' and volume_group and modified:
            LOG.info("From Modify : {0}".format(protection_policy))
            result['modify_vg'] = self.modify_volume_group(
                 vg_id, new_vg_name, description, is_write_order_consistent,
                 protection_policy)

        if state == 'present' and volume_group:
            updated_vg = self.get_volume_group_details(vg_id=vg_id)
            result['volume_group_details'] = updated_vg

        if result['create_vg'] or result['modify_vg'] or result[
            'add_vols_to_vg'] or result['remove_vols_from_vg'] or \
                result['delete_vg']:
            result['changed'] = True

        self.module.exit_json(**result)


def get_powerstore_volume_group_parameters():
    return dict(
        vg_name=dict(required=False, type='str'),
        vg_id=dict(required=False, type='str'),
        new_vg_name=dict(required=False, type='str'),
        volumes=dict(required=False, type='list', elements='str'),
        vol_state=dict(required=False, choices=['absent-in-group',
                                                'present-in-group'],
                       type='str'),
        state=dict(required=True, choices=['present', 'absent'], type='str'),
        description=dict(required=False, type='str'),
        is_write_order_consistent=dict(required=False, type='bool'),
        protection_policy=dict(required=False, type='str')
    )


def main():
    """Create PowerStore volume group object and perform action on it
        based on user input from playbook"""
    obj = PowerStoreVolumeGroup()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
