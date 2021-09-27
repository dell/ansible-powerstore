#!/usr/bin/python
# Copyright: (c) 2019-2021, DellEMC
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r'''
---
module: dellemc_powerstore_gatherfacts
version_added: '1.0.0'
short_description: Gathers information about PowerStore Storage entities
description:
- Gathers the list of specified PowerStore Storage System entities, such as the
  list of cluster nodes, volumes, volume groups, hosts, host groups, snapshot
  rules, protection policies, NAS servers, NFS exports, SMB shares,
  tree quotas, user quotas, file systems etc.
author:
- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
- Vivek Soni (@v-soni11) <ansible.team@dell.com>
extends_documentation_fragment:
  - dellemc.powerstore.dellemc_powerstore.powerstore
options:
  gather_subset:
    description:
    - A list of string variables which specify the PowerStore system entities
      requiring information.information.
    - vol - volumes
    - node - all the nodes
    - vg - volume groups
    - protection_policy - protection policy
    - host - hosts
    - hg -  host groups
    - snapshot_rule - snapshot rule
    - nas_server - NAS servers
    - nfs_export - NFS exports
    - smb_share - SMB shares
    - tree_quota - tree quotas
    - user_quota - user quotas
    - file_system - file systems
    - replication_rule - replication rules
    - replication_session - replication sessions
    - remote_system - remote systems
    - network - various networks
    - role - roles
    - user - local users
    - appliance - appliances
    required: True
    elements: str
    choices: [vol, vg, host, hg, node, protection_policy, snapshot_rule,
              nas_server, nfs_export, smb_share, tree_quota, user_quota,
              file_system, replication_rule, replication_session,
              remote_system, network, role, user, appliance]
    type: list
  filters:
    description:
    - A list of filters to support filtered output for storage entities.
    - Each filter is a list of filter_key, filter_operator, filter_value.
    - Supports passing of multiple filters.
    required: False
    type: list
    elements: dict
    suboptions:
      filter_key:
        description:
        - Name identifier of the filter.
        type: str
        required: True
      filter_operator:
        description:
        - Operation to be performed on the filter key.
        type: str
        choices: [equal, greater, lesser, like, notequal]
        required: True
      filter_value:
        description:
        - Value of the filter key.
        type: str
        required: True
  all_pages:
    description:
    - Indicates whether to return all available entities on the storage system.
    - If set to True, the Gather Facts module will implement pagination and
      return all entities. Otherwise, a maximum of the first 100 entities of any type
      will be returned.
    type: bool
    default: False
notes:
- Pagination is not supported for role and local user. If all_pages is passed,
  it will be ignored.
'''

EXAMPLES = r'''

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

- name: Get list of user, role, network and appliances
  dellemc_powerstore_gatherfacts:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    gather_subset:
      - user
      - role
      - network
      - appliance

- name: Get list of networks whose name contains 'Management'
  dellemc_powerstore_gatherfacts:
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
'''

RETURN = r'''
changed:
    description: Shows whether or not the resource has changed.
    returned: always
    type: bool
subset_result:
    description: Provides details of all given subsets.
    returned: always
    type: complex
    contains:
      Appliance:
        description: Provides details of all appliances.
        type: list
        contains:
          id:
            description: appliance id
            type: str
          name:
            description: appliance name
            type: str
          model:
            description: Model type of the PowerStore
            type: str
      Cluster:
        description: Provides details of all clusters.
        type: list
        returned: always
        contains:
          id:
            description: cluster id
            type: str
            returned: always
          name:
            description: cluster name
            type: str
            returned: always
      FileSystems:
        description: Provides details of all filesystems.
        type: list
        returned: When file_system is in a given gather_subset
        contains:
          id:
            description: filesystem id
            type: str
          name:
            description: filesystem name
            type: str
      HostGroups:
        description: Provides details of all hostgroups.
        type: list
        returned: When hg is in a given gather_subset
        contains:
          id:
            description: hostgroup id
            type: str
          name:
            description: hostgroup name
            type: str
      Hosts:
        description: Provides details of all hosts.
        type: list
        returned: When host is in a given gather_subset
        contains:
          id:
            description: host id
            type: str
          name:
            description: host name
            type: str
      LocalUsers:
        description: Provides details of all local users.
        type: list
        returned: When user is in a given gather_subset
        contains:
          id:
            description: user id
            type: str
          name:
            description: user name
            type: str
      NASServers:
        description: Provides details of all nas servers.
        type: list
        returned: When nas_server is in a given gather_subset
        contains:
          id:
            description: nas server id
            type: str
          name:
            description: nas server name
            type: str
      Networks:
        description: Provides details of all networks.
        type: list
        returned: When network is in a given gather_subset
        contains:
          id:
            description: network id
            type: str
          name:
            description: network name
            type: str
      NFSExports:
        description: Provides details of all nfs exports.
        type: list
        returned: When nfs_export is in a given gather_subset
        contains:
          id:
            description: nfs export id
            type: str
          name:
            description: nfs export name
            type: str
      Nodes:
        description: Provides details of all nodes.
        type: list
        returned: When a node is in a given gather_subset
        contains:
          id:
            description: node id
            type: str
          name:
            description: node name
            type: str
      ProtectionPolicies:
        description: Provides details of all protectionpolicies.
        type: list
        returned: When protection_policy is in a given gather_subset
        contains:
          id:
            description: protectionpolicy id
            type: str
          name:
            description: protectionpolicy name
            type: str
      ReplicationRules:
        description: Provides details of all replication rules.
        type: list
        returned: When replication_rule is in a given gather_subset
        contains:
          id:
            description: replication rule id
            type: str
          name:
            description: replication rule name
            type: str
      ReplicationSession:
        description: details of all replication sessions.
        type: list
        returned: when replication_session given in gather_subset
        contains:
          id:
            description: replication session id
            type: str
      RemoteSystems:
        description: Provides details of all remote systems.
        type: list
        returned: When remote_system is in a given gather_subset
        contains:
          id:
            description: remote system id
            type: str
          name:
            description: remote system name
            type: str
      Roles:
        description: Provides details of all roles.
        type: list
        returned: When role is in a given gather_subset
        contains:
          id:
            description: role id
            type: str
          name:
            description: role name
            type: str
      SMBShares:
        description: Provides details of all smb shares.
        type: list
        returned: When smb_share are in a given gather_subset
        contains:
          id:
            description: smb share id
            type: str
          name:
            description: smb share name
            type: str
      SnapshotRules:
        description: Provides details of all snapshot rules.
        type: list
        returned: When snapshot_rule is in a given gather_subset
        contains:
          id:
            description: snapshot rule id
            type: str
          name:
            description: snapshot rule name
            type: str
      VolumeGroups:
        description: Provides details of all volumegroups.
        type: list
        returned: When vg is in a given gather_subset
        contains:
          id:
            description: volumegroup id
            type: str
          name:
            description: volumegroup name
            type: str
      Volumes:
        description: Provides details of all volumes.
        type: list
        returned: When vol is in a given gather_subset
        contains:
          id:
            description: volume id
            type: str
          name:
            description: volume name
            type: str
      TreeQuotas:
        description: Provides details of all tree quotas.
        type: list
        returned: When tree_quota is in a given gather_subset
        contains:
          id:
            description: tree quota id
            type: str
          path:
            description: tree quota path
            type: str
      UserQuotas:
        description: Provides details of all user quotas.
        type: list
        returned: When user_quota is in a given gather_subset
        contains:
          id:
            description: user quota id
            type: str
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import dellemc_ansible_powerstore_utils as utils
import logging

LOG = utils.get_logger('dellemc_powerstore_gatherfacts')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.3.0'


class PowerstoreGatherFacts(object):
    """Gather Facts operations"""
    cluster_name = ' '
    cluster_global_id = ' '
    filter_mapping = {'equal': 'eq.', 'greater': 'gt.', 'notequal': 'neq.',
                      'lesser': 'lt.', 'like': 'ilike.'}

    def __init__(self):
        self.result = {}
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_gatherfacts_parameters())

        self.filter_keys = sorted(
            [k for k in self.module_params['filters']['options'].keys()
             if 'filter' in k])

        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False
        )

        LOG.info('HAS_PY4PS = %s, IMPORT_ERROR = %s', HAS_PY4PS, IMPORT_ERROR)
        if HAS_PY4PS is False:
            self.module.fail_json(msg=IMPORT_ERROR)
        LOG.info('IS_SUPPORTED_PY4PS_VERSION = %s , '
                 'VERSION_ERROR = %s', IS_SUPPORTED_PY4PS_VERSION,
                 VERSION_ERROR)
        if IS_SUPPORTED_PY4PS_VERSION is False:
            self.module.fail_json(msg=VERSION_ERROR)

        self.conn = utils.get_powerstore_connection(
            self.module.params,
            application_type=APPLICATION_TYPE)
        self.provisioning = self.conn.provisioning
        self.protection = self.conn.protection
        self.configuration = self.conn.config_mgmt

        self.subset_mapping = {
            'vol': {
                'func': self.provisioning.get_volumes,
                'display_as': 'Volumes'
            },
            'vg': {
                'func': self.provisioning.get_volume_group_list,
                'display_as': 'VolumeGroups'
            },
            'host': {
                'func': self.provisioning.get_hosts,
                'display_as': 'Hosts'
            },
            'hg': {
                'func': self.provisioning.get_host_group_list,
                'display_as': 'HostGroups'
            },
            'node': {
                'func': self.provisioning.get_nodes,
                'display_as': 'Nodes'
            },
            'protection_policy': {
                'func': self.protection.get_protection_policies,
                'display_as': 'ProtectionPolicies'
            },
            'snapshot_rule': {
                'func': self.protection.get_snapshot_rules,
                'display_as': 'SnapshotRules'
            },
            'replication_rule': {
                'func': self.protection.get_replication_rules,
                'display_as': 'ReplicationRules'
            },
            'replication_session': {
                'func': self.protection.get_replication_sessions,
                'display_as': 'ReplicationSessions'
            },
            'remote_system': {
                'func': self.protection.get_remote_systems,
                'display_as': 'RemoteSystems'
            },
            'nas_server': {
                'func': self.provisioning.get_nas_servers,
                'display_as': 'NASServers'
            },
            'nfs_export': {
                'func': self.provisioning.get_nfs_exports,
                'display_as': 'NFSExports'
            },
            'smb_share': {
                'func': self.provisioning.get_smb_shares,
                'display_as': 'SMBShares'
            },
            'tree_quota': {
                'func': self.provisioning.get_file_tree_quotas,
                'display_as': 'TreeQuotas'
            },
            'user_quota': {
                'func': self.provisioning.get_file_user_quotas,
                'display_as': 'UserQuotas'
            },
            'file_system': {
                'func': self.provisioning.get_file_systems,
                'display_as': 'FileSystems'
            },
            'network': {
                'func': self.configuration.get_networks,
                'display_as': 'Networks'
            },
            'role': {
                'func': self.configuration.get_roles,
                'display_as': 'Roles'
            },
            'user': {
                'func': self.configuration.get_local_users,
                'display_as': 'LocalUsers'
            },
            'appliance': {
                'func': self.configuration.get_appliances,
                'display_as': 'Appliance'
            }
        }

        LOG.info('Got Py4ps connection object %s',
                 self.conn)

    def update_result_with_item_list(self, item, filter_dict=None,
                                     all_pages=False):
        """Update the result json with list of item of a given PowerStore
           storage system"""

        try:
            LOG.info('Getting %s list', item)
            if item not in ['role', 'user']:
                item_list = self.subset_mapping[item]['func'](
                    filter_dict=filter_dict, all_pages=all_pages)
            else:
                item_list = self.subset_mapping[item]['func'](
                    filter_dict=filter_dict)
            LOG.info('Successfully listed %s %s from powerstore array name: '
                     '%s , global id : %s', len(item_list), self.
                     subset_mapping[item]['display_as'], self.cluster_name,
                     self.cluster_global_id)
            d = {
                self.subset_mapping[item]['display_as']: item_list,
            }
            self.result.update(d)
        except Exception as e:
            msg = 'Get {0} for powerstore array name : {1} , global id : {2}'\
                  ' failed with error {3} '\
                .format(self.subset_mapping[item]['display_as'], self.
                        cluster_name, self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def validate_filter(self, filter_dict):
        """ Validate given filter_dict """

        is_invalid_filter = self.filter_keys != sorted(list(filter_dict))
        if is_invalid_filter:
            msg = "Filter should have all keys: '{0}'".format(
                ", ".join(self.filter_keys))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        is_invalid_filter = any([filter_dict[i] is None for i in filter_dict])
        if is_invalid_filter:
            msg = "Filter keys: '{0}' cannot be None".format(self.filter_keys)
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_filters(self, filters):
        """Get the filters to be applied"""

        filter_dict = {}
        for item in filters:
            self.validate_filter(item)
            f_op = item['filter_operator']
            if self.filter_mapping.get(f_op):
                f_key = item['filter_key']
                f_val = self.filter_mapping[f_op] + item['filter_value']
                if f_key in filter_dict:
                    # multiple filters on same key
                    if isinstance(filter_dict[f_key], list):
                        # prev_val is list, so append new f_val
                        filter_dict[f_key].append(f_val)
                    else:
                        # prev_val is not list,
                        # so create list with prev_val & f_val
                        filter_dict[f_key] = [filter_dict[f_key], f_val]
                else:
                    filter_dict[f_key] = f_val
            else:
                msg = "Given filter operator '{0}' is not supported." \
                    "supported operators are : '{1}'".format(
                        f_op,
                        list(self.filter_mapping.keys()))
                LOG.error(msg)
                self.module.fail_json(msg=msg)
        return filter_dict

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

    def get_array_software_version(self):
        """Get array software version"""
        try:
            soft_ver = self.provisioning.get_array_version()
            msg = 'Got array software version as {0}'.format(soft_ver)
            LOG.info(msg)
            return soft_ver

        except Exception as e:
            msg = 'Failed to get the array software version with ' \
                  'error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def perform_module_operation(self):
        clusters = self.get_clusters()
        if len(clusters) > 0:
            self.cluster_name = clusters[0]['name']
            self.cluster_global_id = clusters[0]['id']
        else:
            self.module.fail_json(msg="Unable to find any active cluster on"
                                      " this array ")

        array_soft_ver = self.get_array_software_version()

        self.result.update(Cluster=clusters,
                           Array_Software_Version=array_soft_ver)
        subset = self.module.params['gather_subset']
        filters = self.module.params['filters']
        all_pages = self.module.params['all_pages']

        filter_dict = {}
        if filters:
            filter_dict = self.get_filters(filters)
            LOG.info('filters: %s', filter_dict)
        if subset is not None:
            for item in subset:
                if item in self.subset_mapping:
                    self.update_result_with_item_list(
                        item, filter_dict=filter_dict, all_pages=all_pages)
                else:
                    self.module.fail_json(
                        msg="subset_mapping do not have details for '{0}'"
                            .format(item))
        else:
            self.module.fail_json(msg="No subset specified in gather_subset")

        self.module.exit_json(**self.result)


def get_powerstore_gatherfacts_parameters():
    """This method provides the parameters required for the ansible modules on
       PowerStore"""
    return dict(
        all_pages=dict(type='bool', required=False, default=False),
        gather_subset=dict(type='list', required=True, elements='str',
                           choices=['vol', 'vg', 'host', 'hg', 'node',
                                    'protection_policy', 'snapshot_rule',
                                    'nas_server', 'nfs_export', 'smb_share',
                                    'tree_quota', 'user_quota', 'file_system',
                                    'replication_rule', 'replication_session',
                                    'remote_system', 'network', 'role',
                                    'user', 'appliance'
                                    ]),
        filters=dict(type='list', required=False, elements='dict',
                     options=dict(filter_key=dict(type='str', required=True,
                                                  no_log=False),
                                  filter_operator=dict(
                                      type='str',
                                      required=True,
                                      choices=['equal', 'greater',
                                               'notequal', 'lesser',
                                               'like']),
                                  filter_value=dict(type='str',
                                                    required=True))
                     )
    )


def main():
    """ Create PowerStore gather facts object and perform action on it
        based on user input from playbook """
    obj = PowerstoreGatherFacts()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
