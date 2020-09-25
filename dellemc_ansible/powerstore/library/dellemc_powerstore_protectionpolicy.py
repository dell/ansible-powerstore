#!/usr/bin/python
# Copyright: (c) 2019, DellEMC

from ansible.module_utils.basic import AnsibleModule
from PyPowerStore.utils.exception import PowerStoreException
from ansible.module_utils.storage.dell import \
    dellemc_ansible_powerstore_utils as utils
import logging
from uuid import UUID

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r'''
---

module: dellemc_powerstore_protectionpolicy
version_added: '2.7'
short_description: Protection policy operations on PowerStore storage system
description:
- Performs all protection policy operations on PowerStore Storage System.
- This modules supports get details of an existing protection policy.
- Create new protection policy with existing Snapshot Rule
- Modify protection policy to change the name and description,
  add or remove existing Snapshot Rules
- Delete an existing protection policy.
extends_documentation_fragment:
  - dellemc_powerstore.dellemc_powerstore
author:
- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
options:
  name:
    description:
    - String variable, indicates the name of the protection policy
    required: False
  protectionpolicy_id:
    description:
    - String variable, indicates the id of the protection policy
    required: False
  new_name:
    description:
    - String variable, indicates the new name of the protection policy
    - Used for renaming operation
  snapshotrules:
    description:
    - List of string to specify the name or ids of snapshot rules
      which is to be added or removed to or from the protection policy.
    required: False
  description:
    description:
    - String variable , indicates the description about the protection policy
    required : False
  state:
    description:
    - String variable indicates the state of protection policy.
    - Only for "delete" operation it should be set to "absent"
    - For all other operations like Create, Modify or Get details,
      it should be set to "present"
    required : True
    choices: [ present, absent]
  snapshotrule_state:
    description:
    - String variable , indicates the state of a snapshotrule in a
      protectionpolicy.
    - When snapshot rules are specified, this variable is required
    - present-in-policy indicates to add to protectionpolicy.
    - absent-in-policy indicates to remove from protectionpolicy.
    required : False
    choices: [ present-in-policy, absent-in-policy]

'''

EXAMPLES = r'''

- name: Create a protection policy with snapshot rule
  dellemc_powerstore_protectionpolicy:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    name: "{{name}}"
    description: "{{description}}"
    snapshotrules:
      - "Ansible_test_snap_rule_1"
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

  - name : Modify protection policy, remove snapshot rule
    dellemc_powerstore_protectionpolicy:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      name: "{{name}}"
      snapshotrules:
        - "Ansible_test_to_be_removed"
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

'''

RETURN = r'''

changed:
    description: Whether or not the resource has changed
    returned: always
    type: bool

protectionpolicy_details:
    description: Details of the protection policy
    returned: When protection policy exists
    type: complex
    contains:
        id:
            description:
                - The system generated ID given to the protection policy
            type: str
        name:
            description:
                - Name of the protection policy
            type: str
        description:
            description:
                - description about the protection policy
            type: str
        type:
            description:
                - The type for the protection policy
            type: str
        replication_rules:
            description:
                - The replication rules details of the protection policy
            type: complex
            contains:
                id:
                    description:
                        - The replication rule ID of the protection policy
                    type: str
                name:
                    description:
                        - The replication rule name of the protection policy
                    type: str
        snapshot_rules:
            description:
                - The snapshot rules details of the protection policy
            type: complex
            contains:
                id:
                    description:
                        - The snapshot rule ID of the protection policy
                    type: str
                name:
                    description:
                        - The snapshot rule name of the protection policy
                    type: str
'''

LOG = utils.get_logger(
    'dellemc_powerstore_protectionpolicy',
    log_devel=logging.INFO)

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.1'


class PowerstoreProtectionpolicy(object):
    """Protectionpolicy operations"""
    cluster_name = ' '
    cluster_global_id = ' '

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(
            get_powerstore_protectionpolicy_parameters())

        # initialize the Ansible module
        mut_ex_args = [['name', 'protectionpolicy_id']]
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mut_ex_args
        )
        LOG.info('HAS_PY4PS = {0} , IMPORT_ERROR = {1}'.format(
            HAS_PY4PS, IMPORT_ERROR))
        if HAS_PY4PS is False:
            self.module.fail_json(msg=IMPORT_ERROR)
        LOG.info('IS_SUPPORTED_PY4PS_VERSION = {0} , VERSION_ERROR = '
                 '{1}'.format(IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR))
        if IS_SUPPORTED_PY4PS_VERSION is False:
            self.module.fail_json(msg=VERSION_ERROR)

        self.conn = utils.get_powerstore_connection(
            self.module.params, application_type=APPLICATION_TYPE)
        self.provisioning = self.conn.provisioning
        LOG.info('Got Py4ps instance for provisioning on PowerStore {0}'.
                 format(self.provisioning))
        self.protection = self.conn.protection
        LOG.info('Got Py4ps instance for protection on PowerStore {0}'.
                 format(self.protection))

    def get_snapshot_rule_details(self, name=None, id=None):
        """Get snapshot rule details by name or id"""
        try:
            LOG.info('Getting the details of snapshot rule , Name:{0} ,'
                     ' ID:{1}'.format(name, id))
            if name:
                resp = self.protection.get_snapshot_rule_by_name(name)
                if resp and len(resp) > 0:
                    LOG.info(
                        'Successfully got the details of snapshot '
                        'rule name {0} from array name {1} and '
                        'global id {2}'.format(
                            name, self.cluster_name, self.cluster_global_id))

                    return True, resp[0].get('id')
            if id:
                detail_resp = self.protection.get_snapshot_rule_details(id)
                if detail_resp and len(detail_resp) > 0:
                    LOG.info('Successfully got the details of snapshot '
                             'rule id {0} from array name {1} and '
                             'global id {2}'.format(id, self.cluster_name,
                                                    self.cluster_global_id))
                    return True, detail_resp['id']

            msg = 'No snapshot rule present with name {0} or ID {1}'.format(
                name, id)
            LOG.info(msg)
            return False, None

        except Exception as e:
            msg = 'Get details of snapshot rule name: {0} or ID {1} from ' \
                  'array name : {2} failed with ' \
                  'error : {3} '.format(name, id, self.cluster_name, str(e))
            if isinstance(e, PowerStoreException) and \
                    e.err_code == PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_protection_policy_details(self, name=None, id=None):
        """Get protection policy"""
        try:
            LOG.info('Getting the details of protection policy with '
                     ' name: {0} , id: {1}'.format(name, id))
            if name:
                resp = self.protection.get_protection_policy_by_name(name)
                if resp and len(resp) > 0:
                    detail_resp = \
                        self.protection.get_protection_policy_details(
                            policy_id=resp[0]['id'])
                    LOG.info(
                        'Successfully got the details of protection policy '
                        'name {0} from array name {1} and '
                        'global id {2}'.format(
                            name, self.cluster_name, self.cluster_global_id))
                    return detail_resp

            elif id:
                detail_resp = self.protection.get_protection_policy_details(
                    policy_id=id)
                if detail_resp and len(detail_resp) > 0:
                    LOG.info(
                        'Successfully got the details of protection policy '
                        'id {0} from array name {1} and '
                        'global id {2}'.format(
                            id, self.cluster_name, self.cluster_global_id))
                    return detail_resp

            msg = 'No protection policy present with name {0} or id {1}'. \
                format(name, id)
            LOG.info(msg)
            return None

        except Exception as e:
            msg = 'Get details of protection policy name: {0},ID: {1}:' \
                  ' from  array name: {2} failed with ' \
                  'error : {3} '.format(name, id, self.cluster_name, str(e))
            if isinstance(e, PowerStoreException) and \
                    e.err_code == PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def create_protection_policy(self, name, description=None,
                                 snapshot_rule_ids=None, ):
        """create protection policy with snapshot rule"""

        try:
            LOG.info('Creating protection policy with snapshot rule')
            resp = self.protection.create_protection_policy(
                name=name,
                description=description,
                snapshot_rule_ids=snapshot_rule_ids)
            msg = 'Successfully created protection policy , id: {0} on' \
                  ' powerstore array name : {1} , global id : {2}' \
                  ''.format(resp.get("id"), self.cluster_name,
                            self.cluster_global_id)
            LOG.info(msg)
            return True, resp

        except Exception as e:
            msg = 'create protectionpolicy on powerstore array name' \
                  ': {0} , global id : {1} failed with' \
                  ' error {2}'.format(self.cluster_name,
                                      self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def modify_protection_policy(self, policy_id, name=None,
                                 description=None, snapshot_rule_ids=None,
                                 add_snapshot_rule_ids=None,
                                 remove_snapshot_rule_ids=None):
        """ Modify an existing protection policy of a given PowerStore
         storage system"""

        try:
            LOG.info('Modifying an existing protection policy')
            resp = self.protection.modify_protection_policy(
                policy_id,
                name=name,
                description=description,
                snapshot_rule_ids=snapshot_rule_ids,
                add_snapshot_rule_ids=add_snapshot_rule_ids,
                remove_snapshot_rule_ids=remove_snapshot_rule_ids)
            msg = 'Successfully modified protection policy id {0} of' \
                  ' powerstore array name : {1},' \
                  'global id : {2}'.format(policy_id, self.cluster_name,
                                           self.cluster_global_id)
            LOG.info(msg)
            return resp

        except Exception as e:
            msg = 'Modify protection policy id: {0} on powerstore array ' \
                  'name: {1}, global id:{2} failed with' \
                  ' error {3}'.format(policy_id, self.cluster_name,
                                      self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def delete_protection_policy(self, policy_id):
        """delete a protection policy by id of a given PowerStore storage
        system"""

        try:
            LOG.info('deleting protection policy id {0}'.format(policy_id))
            self.protection.delete_protection_policy(policy_id=policy_id)
            LOG.info(
                'Successfully deleted protection policy id {0} from '
                'powerstore array name : {1} ,'
                ' global id : {2}'.format(
                    policy_id, self.cluster_name, self.cluster_global_id))
            return True

        except Exception as e:
            msg = 'delete protection policy id {0} for powerstore array' \
                  ' name :{1}, global id: {2} failed with ' \
                  'error {3}'.format(policy_id, self.cluster_name,
                                     self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_clusters(self):
        """Get the clusters"""
        try:
            clusters = self.provisioning.get_cluster_list()
            return clusters

        except Exception as e:
            msg = 'Failed to get the clusters with ' \
                  'error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def perform_module_operation(self):
        """collect input"""
        name = self.module.params['name']
        new_name = self.module.params['new_name']
        snapshotrules = self.module.params['snapshotrules']
        description = self.module.params['description']
        snapshotrule_state = self.module.params['snapshotrule_state']
        state = self.module.params['state']
        prot_pol_id = self.module.params['protectionpolicy_id']

        result = dict(
            changed=False,
            protectionpolicy_details=''
        )

        clusters = self.get_clusters()
        if len(clusters) > 0:
            self.cluster_name = clusters[0]['name']
            self.cluster_global_id = clusters[0]['id']
        else:
            msg = "Unable to find any active cluster on this array "
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        if not prot_pol_id and not name:
            msg = "Either prot_pol_id or name is required"
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        protection_pol = self.get_protection_policy_details(name,
                                                            prot_pol_id)

        '''populating id and name at the begining'''
        if prot_pol_id is None and protection_pol:
            prot_pol_id = protection_pol['id']
        if name is None and protection_pol:
            name = protection_pol['name']

        snapshotrule_ids = []
        """get snapshotrule id from name"""
        if snapshotrules:
            for each_snap in snapshotrules:
                entity_type = utils.name_or_id(each_snap)
                if entity_type == 'NAME':
                    is_present, sn = self.get_snapshot_rule_details(
                        name=each_snap)
                    if is_present:
                        snapshotrule_ids.append(sn)
                    else:
                        msg = "snapshot rule name: {0} is not found on" \
                              " the array".format(each_snap)
                        LOG.error(msg)
                        self.module.fail_json(msg=msg)
                if entity_type == 'ID':
                    '''if a valid id'''
                    is_present, sn = self.get_snapshot_rule_details(
                        id=each_snap)
                    if is_present:
                        snapshotrule_ids.append(sn)
                    else:
                        msg = "snapshot rule id: {0} is not found on the " \
                              "array".format(each_snap)
                        LOG.error(msg)
                        self.module.fail_json(msg=msg)

        """create operation"""
        if not protection_pol and state == "present":

            if len(snapshotrule_ids) == 0 \
                    or snapshotrule_state != "present-in-policy":
                msg = "we must add atleast 1 snapshot rule to protection " \
                      "policy and snapshotrule_state must be set to " \
                      "present-in-policy"
                LOG.error(msg)
                self.module.fail_json(msg=msg)

            result['changed'], resp = \
                self.create_protection_policy(
                    name=name,
                    description=description,
                    snapshot_rule_ids=snapshotrule_ids)

            result['protectionpolicy_details'] = resp

            self.module.exit_json(**result)

        """delete operation"""
        if protection_pol and state == "absent":
            result['changed'] = self.delete_protection_policy(
                policy_id=prot_pol_id)

            self.module.exit_json(**result)

        """modify operation,add/remove snapshot rules"""
        if protection_pol and snapshotrule_state:
            protection_pol = self.get_protection_policy_details(
                id=prot_pol_id)
            if new_name:
                resp = self.get_protection_policy_details(name=new_name)
                if resp:
                    msg = "Protection policy with name {0} already " \
                          "exist".format(new_name)
                    LOG.error(msg)
                    self.module.fail_json(msg=msg)

            present_sn_list = []
            for s_rule in protection_pol['snapshot_rules']:
                present_sn_list.append(s_rule.get('id'))

            """add snapshot rules"""
            if snapshotrule_state == "present-in-policy":
                to_be_added = []

                for eachrule in snapshotrule_ids:
                    if eachrule not in present_sn_list:
                        to_be_added.append(eachrule)

                if to_be_added and len(to_be_added) > 0:
                    result['protectionpolicy_details'] = self\
                        .modify_protection_policy(
                        policy_id=prot_pol_id, name=new_name,
                        description=description,
                        add_snapshot_rule_ids=to_be_added)
                    result['changed'] = True
                    self.module.exit_json(**result)

            '''remove snapshot rules'''
            if snapshotrule_state == "absent-in-policy":
                to_be_removed = []

                for eachrule in snapshotrule_ids:
                    if eachrule in present_sn_list:
                        to_be_removed.append(eachrule)

                if to_be_removed and len(to_be_removed) > 0:
                    result['protectionpolicy_details'] = \
                        self.modify_protection_policy(
                            policy_id=prot_pol_id,
                            name=new_name,
                            description=description,
                            remove_snapshot_rule_ids=to_be_removed)
                    result['changed'] = True
                    self.module.exit_json(**result)

        '''modify operation name and description'''
        if protection_pol and new_name and name != new_name:
            resp = self.get_protection_policy_details(name=new_name)
            if resp:
                msg = "Protection policy with name {0} already " \
                      "exist".format(new_name)
                LOG.error(msg)
                self.module.fail_json(msg=msg)

            result['protectionpolicy_details'] = self.\
                modify_protection_policy(
                policy_id=prot_pol_id, name=new_name,
                description=description)
            result['changed'] = True
            self.module.exit_json(**result)

        '''modify only description'''
        if protection_pol and description and state == 'present':

            protection_pol = self.get_protection_policy_details(
                id=prot_pol_id)

            present_description = protection_pol.get('description')
            if present_description != description:
                result['protectionpolicy_details'] = self.\
                    modify_protection_policy(
                    policy_id=prot_pol_id, description=description)
                result['changed'] = True
                self.module.exit_json(**result)

        '''display details of protection policy'''
        if prot_pol_id and state == "present":
            resp = self.get_protection_policy_details(id=prot_pol_id)
            result['changed'] = False
            result['protectionpolicy_details'] = resp

        self.module.exit_json(**result)


def get_powerstore_protectionpolicy_parameters():
    """This method provide the parameters required for the
    protectionpolicy operations on PowerStore"""

    return dict(
        name=dict(required=False, type='str'),
        protectionpolicy_id=dict(required=False, type='str'),
        new_name=dict(required=False, type='str'),
        description=dict(required=False, type='str'),
        snapshotrules=dict(required=False, type='list'),
        snapshotrule_state=dict(required=False, type='str',
                                choices=['present-in-policy',
                                         'absent-in-policy']),
        state=dict(required=True, type='str', choices=['present', 'absent']),
    )


def main():
    """ Create Protectionpolicy object and perform action on it
        based on user input from playbook """
    obj = PowerstoreProtectionpolicy()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
