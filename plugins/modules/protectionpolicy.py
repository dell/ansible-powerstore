#!/usr/bin/python
# Copyright: (c) 2019-2021, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---

module: protectionpolicy
version_added: '1.0.0'
short_description: Perform Protection policy operations for PowerStore storage
                   system
description:
- Performs all protection policy operations on PowerStore Storage System. This
  module supports create, modify, get and delete a protection policy.
extends_documentation_fragment:
  - dellemc.powerstore.powerstore
author:
- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>
options:
  name:
    description:
    - String variable. Indicates the name of the protection policy.
    required: False
    type: str
  protectionpolicy_id:
    description:
    - String variable. Indicates the id of the protection policy.
    required: False
    type: str
  new_name:
    description:
    - String variable. Indicates the new name of the protection policy.
    - Used for renaming operation.
    type: str
  snapshotrules:
    description:
    - List of strings to specify the name or ids of snapshot rules
      which are to be added or removed, to or from, the protection policy.
    required: False
    type: list
    elements: str
  replicationrule:
    description:
    - The name or ids of the replcation rule which is to be added to the
      protection policy.
    - To remove the replication rule, an empty string has to be passed.
    required: False
    type: str
  description:
    description:
    - String variable. Indicates the description of the protection policy.
    required : False
    type: str
  state:
    description:
    - String variable. Indicates the state of protection policy.
    - For Delete operation only, it should be set to "absent".
    - For all other operations like Create, Modify or Get details,
      it should be set to "present".
    required : True
    choices: [ present, absent]
    type: str
  snapshotrule_state:
    description:
    - String variable. Indicates the state of a snapshotrule in a
      protection policy.
    - When snapshot rules are specified, this variable is required.
    - Value present-in-policy indicates to add to protection policy.
    - Value absent-in-policy indicates to remove from protection policy.
    required : False
    choices: [ present-in-policy, absent-in-policy]
    type: str
notes:
- Before deleting a protection policy, the replication rule has to be removed
  from the protection policy.
- In PowerStore version 3.0.0.0, protection policy without snapshot rule/replication rule
  is not allowed.
- The check_mode is not supported.
'''

EXAMPLES = r'''

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
'''

RETURN = r'''

changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"

protectionpolicy_details:
    description: Details of the protection policy.
    returned: When protection policy exists
    type: complex
    contains:
        id:
            description: The system generated ID given to the protection
                         policy.
            type: str
        name:
            description: Name of the protection policy.
            type: str
        description:
            description: description about the protection policy.
            type: str
        type:
            description: The type for the protection policy.
            type: str
        replication_rules:
            description: The replication rule details of the protection
                         policy.
            type: complex
            contains:
                id:
                    description: The replication rule ID of the protection
                                 policy.
                    type: str
                name:
                    description: The replication rule name of the protection
                                 policy.
                    type: str
        snapshot_rules:
            description: The snapshot rules details of the protection policy.
            type: complex
            contains:
                id:
                    description: The snapshot rule ID of the protection
                                 policy.
                    type: str
                name:
                    description: The snapshot rule name of the protection
                                 policy.
                    type: str
    sample: {
        "description": null,
        "id": "bce845ea-78ba-4414-ada1-8130f3a49e74",
        "name": "sample_protection_policy",
        "replication_rules": [
            "id": "7ec83605-bed4-4e2b-8405-504a614db318",
            "name": "sample_replication_rule"
        ],
        "snapshot_rules": [],
        "type": "Protection"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils
import logging

LOG = utils.get_logger(
    'protectionpolicy',
    log_devel=logging.INFO)

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.6.0'


class PowerstoreProtectionpolicy(object):
    """Protection policy operations"""
    cluster_name = ' '
    cluster_global_id = ' '

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(
            get_powerstore_protectionpolicy_parameters())

        # initialize the Ansible module
        mut_ex_args = [['name', 'protectionpolicy_id']]
        required_one_of = [['name', 'protectionpolicy_id']]
        required_together = [['snapshotrules', 'snapshotrule_state']]
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mut_ex_args,
            required_one_of=required_one_of,
            required_together=required_together
        )
        LOG.info('HAS_PY4PS = %s, IMPORT_ERROR = %s', HAS_PY4PS, IMPORT_ERROR)
        if HAS_PY4PS is False:
            self.module.fail_json(msg=IMPORT_ERROR)
        LOG.info('IS_SUPPORTED_PY4PS_VERSION = %s , VERSION_ERROR = '
                 '%s', IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR)
        if IS_SUPPORTED_PY4PS_VERSION is False:
            self.module.fail_json(msg=VERSION_ERROR)

        self.conn = utils.get_powerstore_connection(
            self.module.params, application_type=APPLICATION_TYPE)
        self.provisioning = self.conn.provisioning
        LOG.info('Got Py4ps instance for provisioning on PowerStore %s',
                 self.provisioning)
        self.protection = self.conn.protection
        LOG.info('Got Py4ps instance for protection on PowerStore %s',
                 self.protection)

    def get_snapshot_rule_details(self, rule_name=None, rule_id=None):
        """Get snapshot rule details by name or id"""
        try:
            LOG.info('Getting the details of snapshot rule , Name:%s ,'
                     ' ID:%s', rule_name, rule_id)
            if rule_name:
                resp = self.protection.get_snapshot_rule_by_name(rule_name)
                if resp and len(resp) > 0:
                    LOG.info('Successfully got the details of snapshot rule'
                             ' name %s from array name %s and global id %s',
                             rule_name, self.cluster_name,
                             self.cluster_global_id)

                    return True, resp[0].get('id')
            if rule_id:
                detail_resp = self.protection.get_snapshot_rule_details(
                    rule_id)
                if detail_resp and len(detail_resp) > 0:
                    LOG.info('Successfully got the details of snapshot rule'
                             ' id %s from array name %s and global id %s',
                             rule_id, self.cluster_name,
                             self.cluster_global_id)
                    return True, detail_resp['id']

            msg = 'No snapshot rule present with name {0} or ID {1}'.format(
                rule_name, rule_id)
            LOG.info(msg)
            return False, None

        except Exception as e:
            msg = 'Get details of snapshot rule name: {0} or ID {1} from ' \
                  'array name : {2} failed with ' \
                  'error : {3} '.format(rule_name, rule_id, self.cluster_name,
                                        str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_replication_rule_details(self, rep_rule_name=None,
                                     rep_rule_id=None):
        """Get replication rule details by name or id"""
        try:
            LOG.info('Getting the details of replication rule , Name:%s ,'
                     ' ID:%s', str(rep_rule_name), str(rep_rule_id))
            detail_resp = None
            if rep_rule_name:
                resp = self.protection.get_replication_rule_by_name(
                    rep_rule_name)
                if resp and len(resp) > 0:
                    LOG.info('Successfully got the details of replication rule'
                             'with name: %s', rep_rule_name)
                    detail_resp = self.protection.get_replication_rule_details(
                        resp[0]['id'])
                    return detail_resp
            else:
                detail_resp = self.protection.get_replication_rule_details(
                    rep_rule_id)
                if detail_resp and len(detail_resp) > 0:
                    msg = 'Successfully got the details of replication ' \
                          'rule with id: %s ' % rep_rule_id
                    LOG.info(msg)
                    return detail_resp

            msg = 'No replication rule present with name {0} or ID {1}'.format(
                rep_rule_name, rep_rule_id)
            LOG.info(msg)
            return detail_resp

        except Exception as e:
            msg = 'Get details of replication rule name: {0} or ID {1} ' \
                  'failed with error : {2} '.format(rep_rule_name, rep_rule_id,
                                                    str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_protection_policy_details(self, name=None, policy_id=None):
        """Get protection policy"""
        try:
            LOG.info('Getting the details of protection policy with name: %s,'
                     ' id: %s', name, policy_id)
            if name:
                resp = self.protection.get_protection_policy_by_name(name)
                if resp and len(resp) > 0:
                    detail_resp = \
                        self.protection.get_protection_policy_details(
                            policy_id=resp[0]['id'])
                    LOG.info('Successfully got the details of protection'
                             ' policy name %s from array name %s and global'
                             ' id %s', name, self.cluster_name,
                             self.cluster_global_id)
                    return detail_resp

            elif policy_id:
                detail_resp = self.protection.get_protection_policy_details(
                    policy_id=policy_id)
                if detail_resp and len(detail_resp) > 0:
                    LOG.info('Successfully got the details of protection'
                             ' policy id %s from array name %s and global id'
                             ' %s', policy_id, self.cluster_name,
                             self.cluster_global_id)
                    return detail_resp

            msg = 'No protection policy present with name {0} or id {1}'. \
                format(name, policy_id)
            LOG.info(msg)
            return None

        except Exception as e:
            msg = 'Get details of protection policy name: {0},ID: {1}:' \
                  ' from  array name: {2} failed with ' \
                  'error : {3} '.format(name, policy_id, self.cluster_name,
                                        str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def create_protection_policy(self, name, description=None,
                                 snapshot_rule_ids=None,
                                 replication_rule_id=None):
        """create protection policy with snapshot rule and replication rule"""

        try:
            LOG.info('Creating protection policy with snapshot rule and'
                     ' replication rule')
            resp = self.protection.create_protection_policy(
                name=name,
                description=description,
                snapshot_rule_ids=snapshot_rule_ids,
                replication_rule_ids=replication_rule_id)
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
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def modify_protection_policy(self, policy_id, name=None,
                                 description=None, snapshot_rule_ids=None,
                                 add_snapshot_rule_ids=None,
                                 remove_snapshot_rule_ids=None,
                                 add_rep_rule_id=None,
                                 remove_rep_rule_id=None):
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
                remove_snapshot_rule_ids=remove_snapshot_rule_ids,
                add_replication_rule_ids=add_rep_rule_id,
                remove_replication_rule_ids=remove_rep_rule_id)
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
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def delete_protection_policy(self, policy_id):
        """delete a protection policy by id of a given PowerStore storage
        system"""

        try:
            LOG.info('deleting protection policy id %s', policy_id)
            self.protection.delete_protection_policy(policy_id=policy_id)
            LOG.info('Successfully deleted protection policy id %s from'
                     ' powerstore array name : %s , global id : %s',
                     policy_id, self.cluster_name, self.cluster_global_id)
            return True

        except Exception as e:
            msg = 'delete protection policy id {0} for powerstore array' \
                  ' name :{1}, global id: {2} failed with ' \
                  'error {3}'.format(policy_id, self.cluster_name,
                                     self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_clusters(self):
        """Get the clusters"""
        try:
            clusters = self.provisioning.get_cluster_list()
            return clusters

        except Exception as e:
            msg = 'Failed to get the clusters with ' \
                  'error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def perform_module_operation(self):
        """collect input"""
        name = self.module.params['name']
        new_name = self.module.params['new_name']
        snapshotrules = self.module.params['snapshotrules']
        description = self.module.params['description']
        rep_rule = self.module.params['replicationrule']
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

        # check if the snapshot rules are passed or not.
        if snapshotrule_state and not snapshotrules:
            self.module.fail_json(msg="No snapshot rule found, Please provide "
                                      "a valid snapshot rule(s)")

        # Get protection policy details
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
                        rule_name=each_snap)
                    if is_present:
                        snapshotrule_ids.append(sn)
                    else:
                        if snapshotrule_state == "present-in-policy":
                            msg = "snapshot rule name: {0} is not found on the " \
                                  "array".format(each_snap)
                            LOG.error(msg)
                            self.module.fail_json(msg=msg)

                if entity_type == 'ID':
                    '''if a valid id'''
                    if snapshotrule_state == "present-in-policy":
                        is_present, sn = self.get_snapshot_rule_details(
                            rule_id=each_snap)
                        if is_present:
                            snapshotrule_ids.append(sn)
                    else:
                        snapshotrule_ids.append(sn)

        """Get replication rule id"""
        rep_rule_id = None
        if rep_rule:
            if utils.name_or_id(rep_rule) == "ID":
                rep_rule_details = self.get_replication_rule_details(
                    rep_rule_id=rep_rule)
                rep_rule_id = rep_rule_details['id']
            else:
                rep_rule_details = self.get_replication_rule_details(
                    rep_rule_name=rep_rule)
                if rep_rule_details is None:
                    msg = "Replication rule with name {0} not found." \
                          " Please enter a valid name.".format(rep_rule)
                    self.module.fail_json(msg=msg)
                rep_rule_id = rep_rule_details['id']

        """create operation"""
        if not protection_pol and state == "present":

            if not rep_rule and (len(snapshotrule_ids) == 0
                                 or snapshotrule_state != "present-in-policy"):
                msg = "we must add atleast 1 snapshot rule or replication " \
                      "rule to protection policy and snapshotrule_state " \
                      "must be set to present-in-policy"
                LOG.error(msg)
                self.module.fail_json(msg=msg)
            if rep_rule_id:
                result['changed'], resp = \
                    self.create_protection_policy(
                        name=name,
                        description=description,
                        snapshot_rule_ids=snapshotrule_ids,
                        replication_rule_id=[rep_rule_id])
            else:
                result['changed'], resp = \
                    self.create_protection_policy(
                        name=name,
                        description=description,
                        snapshot_rule_ids=snapshotrule_ids)

            result['protectionpolicy_details'] = resp

            self.module.exit_json(**result)

        """delete operation"""
        if protection_pol and state == "absent":
            if protection_pol['snapshot_rules'] and\
                    protection_pol["replication_rules"]:
                self.module.fail_json(
                    msg="Deletion of protection policy is not allowed if both "
                        "replication rule and snapshot rules are attached to "
                        "the policy. Please remove the replication rule from "
                        "protection policy before deleting the "
                        "protection policy")
            result['changed'] = self.delete_protection_policy(
                policy_id=prot_pol_id)

            self.module.exit_json(**result)

        """modify operation,add/remove snapshot rules"""
        changed = False
        if protection_pol and snapshotrule_state:
            protection_pol = self.get_protection_policy_details(
                policy_id=prot_pol_id)
            present_sn_list = []
            for s_rule in protection_pol['snapshot_rules']:
                present_sn_list.append(s_rule.get('id'))

            """add snapshot rules"""
            if snapshotrule_state == "present-in-policy":
                to_be_added = list(set(snapshotrule_ids) -
                                   (set(present_sn_list)))
                if to_be_added and len(to_be_added) > 0:
                    self.modify_protection_policy(
                        policy_id=prot_pol_id,
                        add_snapshot_rule_ids=to_be_added)
                    changed = True

            '''remove snapshot rules'''
            if snapshotrule_state == "absent-in-policy":
                to_be_removed = \
                    list(set(snapshotrule_ids).intersection(
                        set(present_sn_list)))

                if to_be_removed and len(to_be_removed) > 0:
                    self.modify_protection_policy(
                        policy_id=prot_pol_id,
                        remove_snapshot_rule_ids=to_be_removed)
                    changed = True

        ''' modify operation name'''
        # error if new_name is passed as empty string or with white spaces
        if new_name is not None and new_name.strip() == '':
            self.module.fail_json(
                msg="Empty string or spaces is not allowed in renaming the "
                    "protection policy. Please enter a valid new_name.")

        if protection_pol and new_name and name != new_name:
            resp = self.get_protection_policy_details(name=new_name)
            # error, if policy exists with new_name
            if resp:
                msg = "Protection policy with name {0} already " \
                      "exist".format(new_name)
                LOG.error(msg)
            self.modify_protection_policy(policy_id=prot_pol_id, name=new_name)
            changed = True

        '''modify only description'''
        if protection_pol and description and state == 'present':

            protection_pol = self.get_protection_policy_details(
                policy_id=prot_pol_id)
            present_description = protection_pol.get('description')
            if present_description != description:
                self.modify_protection_policy(policy_id=prot_pol_id,
                                              description=description)
                changed = True

        '''modify replication rule'''
        if protection_pol and (rep_rule_id or rep_rule == "") \
                and state == 'present':
            protection_pol = self.get_protection_policy_details(
                policy_id=prot_pol_id)
            present_rep_rule = protection_pol['replication_rules']

            # If the replication rule is attached and
            # replication rule is to be removed.
            if present_rep_rule and rep_rule == "":
                self.modify_protection_policy(
                    policy_id=prot_pol_id,
                    remove_rep_rule_id=[present_rep_rule[0]['id']])
                changed = True

            # If no replication rule is attached to the policy and new
            # replication rule is to be added.
            if not present_rep_rule and rep_rule_id:
                self.modify_protection_policy(policy_id=prot_pol_id,
                                              add_rep_rule_id=[rep_rule_id])
                changed = True

            # If a replication rule is attached and
            # is to be replaced by new replication rule
            if present_rep_rule and rep_rule_id and\
                    rep_rule_id != present_rep_rule[0]['id']:
                # remove the old replication rule and add the new replication rule
                self.modify_protection_policy(
                    policy_id=prot_pol_id,
                    remove_rep_rule_id=[present_rep_rule[0]['id']],
                    add_rep_rule_id=[rep_rule_id])
                changed = True
        result['changed'] = changed
        result['protectionpolicy_details'] = \
            self.get_protection_policy_details(policy_id=prot_pol_id)
        self.module.exit_json(**result)

        '''display details of protection policy'''
        if prot_pol_id and state == "present":
            result['changed'] = False
            result['protectionpolicy_details'] = protection_pol

        self.module.exit_json(**result)


def get_powerstore_protectionpolicy_parameters():
    """This method provides the parameters required for the
    protection policy operations on PowerStore"""

    return dict(
        name=dict(required=False, type='str'),
        protectionpolicy_id=dict(required=False, type='str'),
        new_name=dict(required=False, type='str'),
        description=dict(required=False, type='str'),
        replicationrule=dict(required=False, type='str'),
        snapshotrules=dict(required=False, type='list', elements='str'),
        snapshotrule_state=dict(required=False, type='str',
                                choices=['present-in-policy',
                                         'absent-in-policy']),
        state=dict(required=True, type='str', choices=['present', 'absent']),
    )


def main():
    """ Create protection policy object and perform action on it
        based on user input from playbook """
    obj = PowerstoreProtectionpolicy()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
