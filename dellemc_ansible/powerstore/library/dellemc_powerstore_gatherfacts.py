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
module: dellemc_powerstore_gatherfacts
version_added: '2.6'
short_description: Gathers information about PowerStore Storage entities
description:
- Gathers the list of specified PowerStore Storage System entities, like the
  list of cluster nodes, volumes, volume groups, hosts, host groups, snapshot rules,
  protection policies etc.
extends_documentation_fragment:
  - dellemc.dellemc_powerstore
author:
- Arindam Datta (arindam.datta@dell.com)
options:        
  gather_subset:
    description:
    - List of string variables to specify the PowerStore system entities for which
      information is required.
    - vol - volumes
    - nodes - all the nodes 
    - vg - volume groups
    - protection_policy - protection policy
    - host - hosts
    - hg -  host groups
    - snapshot_rule - snapshot rule    
    required: True 
    choices: [vol, nodes, vg, protectionpolicy, host, hg, snaprule]
'''

EXAMPLES = r'''

- name: Get list of volumes
  dellemc_powerstore_gatherfacts:
    array_ip: "{{array_ip}}"      
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"      
    gather_subset:
      - vol

- name: Get list of volume groups
  dellemc_powerstore_gatherfacts:
    array_ip: "{{array_ip}}"      
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"      
    gather_subset:
      - vg


- name: Get list of host
  dellemc_powerstore_gatherfacts:
    array_ip: "{{array_ip}}"      
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"      
    gather_subset:
      - host


- name: Get list of host groups
  dellemc_powerstore_gatherfacts:
    array_ip: "{{array_ip}}"      
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"      
    gather_subset:
      - hg


- name: Get list of nodes
  dellemc_powerstore_gatherfacts:
    array_ip: "{{array_ip}}"      
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"      
    gather_subset:
      - node


- name: Get list of protection policies
  dellemc_powerstore_gatherfacts:
    array_ip: "{{array_ip}}"      
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"      
    gather_subset:
      - protection_policy

- name: Get list of snapshot rules
  dellemc_powerstore_gatherfacts:
    array_ip: "{{array_ip}}"      
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"      
    gather_subset:
      - snapshot_rule

'''

RETURN = r'''  '''


LOG = utils.get_logger('dellemc_powerstore_gatherfacts', log_devel=logging.INFO)

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.0'

class PowerstoreGatherFacts(object):
    """Gather Facts operations"""
    cluster_name = ' '
    cluster_global_id = ' '

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_gatherfacts_parameters())

        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True
        )

        LOG.info('HAS_PY4PS = {0} , IMPORT_ERROR = {1}'.format(HAS_PY4PS, IMPORT_ERROR))
        if HAS_PY4PS is False:
            self.module.fail_json(msg=IMPORT_ERROR)
        LOG.info('IS_SUPPORTED_PY4PS_VERSION = {0} , '
                 'VERSION_ERROR = {1}'.format(
                  IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR))
        if IS_SUPPORTED_PY4PS_VERSION is False:
            self.module.fail_json(msg=VERSION_ERROR)

        self.conn = utils.get_powerstore_connection(self.module.params,
                                                   application_type=APPLICATION_TYPE)
        self.provisioning = self.conn.provisioning
        self.protection = self.conn.protection
        LOG.info('Got Py4ps instance for provisioning on PowerStore {0}'.
                 format(self.conn))

    def get_volume_list(self):
        """Get the list of volumes of a given PowerStore storage system"""

        try:
            LOG.info('Getting Volume List ')
            vol_list = self.provisioning.get_volumes()
            LOG.info('Successfully listed {0} volumes from powerstore array name : {1} , global id : {2}' .format(
                len(vol_list), self.cluster_name, self.cluster_global_id))
            return vol_list

        except Exception as e:
            msg = 'Get Volumes for powerstore array name : {0} , global id : {1} failed with error {2} '.format(
                self.cluster_name, self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_volume_group_list(self):
        """Get the list of volume groups of a given Powerstore storage
        system"""

        try:
            LOG.info('Getting Volume Group List ')
            vg_list = self.provisioning.get_volume_group_list()
            LOG.info(
                'Successfully listed {0} volume groups from powerstore array name : {1} , '
                'global id : {2}'.format(len(vg_list), self.cluster_name, self.cluster_global_id))
            return vg_list

        except Exception as e:
            msg = 'Get Volume groups for powerstore array name : {0} , global id : {1} ' \
                  'failed with error {2} '.format(self.cluster_name, self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_host_list(self):
        """Get the list of hosts of a given PowerStore storage system"""

        try:
            LOG.info('Getting host List ')
            host_list = self.provisioning.get_hosts()
            LOG.info(
                'Successfully listed {0} hosts from powerstore array name : {1} , '
                'global id : {2}'.format(len(host_list), self.cluster_name, self.cluster_global_id))
            return host_list

        except Exception as e:
            msg = 'Get hosts for powerstore array name : {0} , global id : {1} ' \
                  'failed with error {2} '.format(self.cluster_name, self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_hostgroup_list(self):
        """Get the list of host group of a given PowerStore storage
        system"""

        try:
            LOG.info('Getting host group List ')
            hg_list = self.provisioning.get_host_group_list()
            LOG.info(
                'Successfully listed {0} host groups from powerstore array name : {1} , '
                'global id : {2}'.format(len(hg_list), self.cluster_name, self.cluster_global_id))
            return hg_list

        except Exception as e:
            msg = 'Get host groups for powerstore array name : {0} , global id : {1} ' \
                  'failed with error {2} '.format(self.cluster_name, self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def node_list(self):
        """Get the list of nodes of a given PowerStore storage system"""

        try:
            LOG.info('Getting node List ')
            node_list = self.provisioning.get_nodes()
            LOG.info(
                'Successfully listed {0} nodes from powerstore array name : {1} ,'
                ' global id : {2}'.format(len(node_list), self.cluster_name, self.cluster_global_id))
            return node_list

        except Exception as e:
            msg = 'Get nodes for powerstore array name : {0} , global id : {1} ' \
                  'failed with error {2} '.format(self.cluster_name, self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_protectionpolicy_list(self):
        """Get the list of protectionpolicy of a given PowerStore storage
         system"""

        try:
            LOG.info('Getting protectionpolicy List ')
            protectionpolicy_list = self.protection.get_protection_policies()
            LOG.info(
                'Successfully listed {0} protectionpolicy from powerstore array name : {1} , '
                'global id : {2}'.format(len(protectionpolicy_list), self.cluster_name, self.cluster_global_id))
            return protectionpolicy_list

        except Exception as e:
            msg = 'Get protectionpolicy for powerstore array name : {0} , global id : {1} ' \
                  'failed with error {2} '.format(self.cluster_name, self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_snaprule_list(self):
        """Get the list of snapshot rule of a given PowerStore storage system"""

        try:
            LOG.info('Getting snapshot rule List ')
            snaprule_list = self.protection.get_snapshot_rules()
            LOG.info(
                'Successfully listed {0} snapshotrule from powerstore array name : {1} , '
                'global id : {2}'.format(len(snaprule_list), self.cluster_name, self.cluster_global_id))
            return snaprule_list

        except Exception as e:
            msg = 'Get snapshotrule for powerstore array name : {0} , global id : {1} ' \
                  'failed with error {2} '.format(self.cluster_name, self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def perform_module_operation(self):
        clusters = self.provisioning.get_cluster_list()
        if len(clusters) > 0:
            self.cluster_name = clusters[0]['name']
            self.cluster_global_id = clusters[0]['id']
        else:
            self.module.fail_json(msg="Unable to find any active cluster on this array ")

        subset = self.module.params['gather_subset']
        if subset is not None:
            vol = []
            vg = []
            protectionpolicy = []
            host = []
            hg = []
            snaprule = []
            node = []
            for item in subset:
                if item == 'vol':
                    vol = self.get_volume_list()
                if item == 'vg':
                    vg = self.get_volume_group_list()
                if item == 'host':
                    host = self.get_host_list()
                if item == 'hg':
                    hg = self.get_hostgroup_list()
                if item == 'node':
                    node = self.node_list()
                if item == 'protection_policy':
                    protectionpolicy = self.get_protectionpolicy_list()
                if item == 'snapshot_rule':
                    snaprule = self.get_snaprule_list()
        else:
            self.module.fail_json(msg="No subset specified in gather_subset")

        self.module.exit_json(
            Cluster=clusters,
            Volumes=vol,
            VolumeGroups=vg,
            Hosts=host,
            HostGroups=hg,
            ProtectionPolicies=protectionpolicy,
            SnapshotRules=snaprule,
            Nodes=node)


def get_powerstore_gatherfacts_parameters():
    """This method provide the parameters required for the ansible modules on PowerStore"""
    return dict(

            gather_subset=dict(type='list', required=True,
                               choices=['vol',
                                        'vg',
                                        'host',
                                        'hg',
                                        'node',
                                        'protection_policy',
                                        'snapshot_rule'
                                        ]))

def main():
    """ Create PowerStoreGatherFacts object and perform action on it
        based on user input from playbook """
    obj = PowerstoreGatherFacts()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
