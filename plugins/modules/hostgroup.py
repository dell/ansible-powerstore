#!/usr/bin/python
# Copyright: (c) 2019-2021, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: hostgroup
version_added: '1.0.0'
short_description:  Manage host group on PowerStore Storage System
description:
- Managing host group on PowerStore storage system includes create
  host group with a set of hosts, add/remove hosts from host group, rename
  host group, and delete host group.
- Deletion of a host group results in deletion of the containing hosts as
  well. Remove hosts from the host group first to retain them.
author:
- Manisha Agrawal (@agrawm3) <ansible.team@dell.com>
extends_documentation_fragment:
  - dellemc.powerstore.powerstore
options:
  hostgroup_name:
    description:
    - The host group name. This value must contain 128 or fewer printable
      Unicode characters.
    - Creation of an empty host group is not allowed.
    - Required when creating a host group.
    - Use either hostgroup_id or hostgroup_name for modify and delete tasks.
    type: str
  hostgroup_id:
    description:
    - The 36-character long host group id, automatically generated when a
      host group is created.
    - Use either hostgroup_id or hostgroup_name for modify and delete tasks.
    - The hostgroup_id cannot be used while creating host group, as it is
      generated by the array after creation of host group.
    type: str
  hosts:
    description:
    - List of hosts to be added or removed from the host group.
    - Subordinate hosts in a host group can only be of one type, either FC or iSCSI.
    - Required when creating a host group.
    - To represent host, both name or ID can be used interchangeably. The
      module will detect both.
    type: list
    elements: str
  state:
    description:
    - Define whether the host group should exist or not.
    - Value present - indicates that the host group should exist on the
      system.
    - Value absent - indicates that the host group should not exist on the
      system.
    - Deletion of a host group results in deletion of the containing hosts as
      well. Remove hosts from the host group first to retain them.
    required: True
    choices: [absent, present]
    type: str
  host_state:
    description:
    - Define whether the hosts should be present or absent in host group.
    - Value present-in-group - indicates that the hosts should exist on the
      host group.
    - Value absent-in-group - indicates that the hosts should not exist on the
      host group.
    - Required when creating a host group with hosts or adding/removing hosts
      from existing host group.
    choices: [present-in-group, absent-in-group]
    type: str
  new_name:
    description:
    - The new name for host group renaming function. This value must contain
      128 or fewer printable Unicode characters.
    type: str

notes:
- The check_mode is not supported.
'''


EXAMPLES = r'''
  - name: Create host group with hosts using host name
    dellemc.powerstore.hostgroup:
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
    dellemc.powerstore.hostgroup:
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
    dellemc.powerstore.hostgroup:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      hostgroup_name: "{{hostgroup_name}}"
      state: 'present'

  - name: Get host group details using ID
    dellemc.powerstore.hostgroup:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      hostgroup_id: "{{host group_id}}"
      state: 'present'

  - name: Add hosts to host group
    dellemc.powerstore.hostgroup:
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
    dellemc.powerstore.hostgroup:
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
    dellemc.powerstore.hostgroup:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      hostgroup_name: "{{hostgroup_name}}"
      new_name: "{{new_hostgroup_name}}"
      state: 'present'

  - name: Delete host group
    dellemc.powerstore.hostgroup:
      array_ip: "{{array_ip}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      hostgroup_name: "{{hostgroup_name}}"
      state: 'absent'
'''

RETURN = r'''

changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"

hostgroup_details:
    description: Details of the host group.
    returned: When host group exists
    type: complex
    contains:
        id:
            description: The system generated ID given to the host group.
            type: str
        name:
            description: Name of the host group.
            type: str
        description:
            description: Description about the host group.
            type: str
        hosts:
            description: The hosts details which are part of this host group.
            type: complex
            contains:
                id:
                    description: The ID of the host.
                    type: str
                name:
                    description: The name of the host.
                    type: str
    sample: {
        "description": null,
        "hosts": [
            {
                "id": "1ff90201-a576-482c-b7fe-0d4dc901da67",
                "name": "sample_host"
            }
        ],
        "id": "80fc96fa-227e-4796-84b8-c6452c5b8f64",
        "name": "sample_host_group"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import utils
import logging

LOG = utils.get_logger('hostgroup', log_devel=logging.INFO)

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.6.0'


class PowerStoreHostgroup(object):
    '''Class with host group operations'''

    VALID_ID = "ID"

    def __init__(self):
        # Define all parameters required by this module
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(self.get_powerstore_hostgroup_parameters())

        mutually_exclusive = [['hostgroup_name', 'hostgroup_id']]
        required_one_of = [['hostgroup_name', 'hostgroup_id']]

        # Initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mutually_exclusive,
            required_one_of=required_one_of
        )

        LOG.info('HAS_PY4PS = %s , IMPORT_ERROR = %s', HAS_PY4PS,
                 IMPORT_ERROR)
        if HAS_PY4PS is False:
            self.module.fail_json(msg=IMPORT_ERROR)
        LOG.info('IS_SUPPORTED_PY4PS_VERSION = %s , VERSION_ERROR = %s',
                 IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR)
        if IS_SUPPORTED_PY4PS_VERSION is False:
            self.module.fail_json(msg=VERSION_ERROR)

        # result is a dictionary that contains changed status and host group
        # details
        self.result = {"changed": False, "hostgroup_details": {}}

        self.conn = utils.get_powerstore_connection(
            self.module.params, application_type=APPLICATION_TYPE)
        LOG.info('Got Python library connection instance for provisioning on'
                 ' PowerStore %s', self.conn)

    def get_powerstore_hostgroup_parameters(self):
        return dict(
            hostgroup_name=dict(required=False, type='str'),
            hostgroup_id=dict(required=False, type='str'),
            hosts=dict(required=False, type='list', elements='str'),
            state=dict(required=True, choices=['present', 'absent'],
                       type='str'),
            host_state=dict(required=False,
                            choices=['absent-in-group', 'present-in-group'],
                            type='str'),
            new_name=dict(required=False, type='str')
        )

    def get_hostgroup(self, hostgroup_id):
        '''
        Get details of a given host group
        '''
        try:
            LOG.info('Getting host group %s details', hostgroup_id)
            return self.conn.provisioning.get_host_group_details(hostgroup_id)
        except Exception as e:
            msg = 'Unable to get details of host group ID: {0} -- error: {1}' \
                .format(hostgroup_id, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR \
                    and e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_hostgroup_id_by_name(self, hostgroup_name):
        try:
            host_group_info = self.conn.provisioning.get_host_group_by_name(
                hostgroup_name)
            if host_group_info:
                if len(host_group_info) > 1:
                    error_msg = 'Multiple host groups by the same name found'
                    LOG.error(error_msg)
                    self.module.fail_json(msg=error_msg)
                return host_group_info[0]['id']
            return None
        except Exception as e:
            error_msg = "Get hostgroup: {0} failed with " \
                        "error: {1}".format(hostgroup_name, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def get_host(self, host_id):
        '''
        Get details of a given host
        '''
        try:
            LOG.info('Getting host %s details', host_id)
            return self.conn.provisioning.get_host_details(host_id)
        except Exception as e:
            LOG.error('Unable to get details of host ID: %s -- error: %s',
                      host_id, str(e))

    def create_host_list(self, hosts):
        '''
        A function which takes the hosts list given by the user (which could be
        either name or ID of each host), and converts it to a list of IDs.
        '''
        host_list = []
        try:
            for host in hosts:
                # Since the ID format of PowerStore is UUID
                # check if host is host_id
                id_or_name = utils.name_or_id(val=host)
                if id_or_name == self.VALID_ID and self.get_host(host):
                    host_list.append(host)
                else:
                    # check if host is host_name
                    host_id = self.get_host_id_by_name(host)
                    if host_id:
                        host_list.append(host_id)
                    else:
                        error_msg = ("Host {0} not found".format(host))
                        LOG.error(error_msg)
                        self.module.fail_json(msg=error_msg)
            return host_list

        except Exception as e:
            error_msg = ("Host {0} not found, error={1}".format(
                host, str(e)))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def get_host_id_by_name(self, host_name):
        try:
            host_info = self.conn.provisioning.get_host_by_name(host_name)
            if host_info:
                if len(host_info) > 1:
                    error_msg = 'Multiple hosts by the same name found'
                    LOG.error(error_msg)
                    self.module.fail_json(msg=error_msg)
                return host_info[0]['id']
            return None
        except Exception as e:
            error_msg = ("Host {0} not found, with error= {1}".format(
                host_name, str(e)))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def create_hostgroup(self, hostgroup_name, hosts):
        '''
        Create host group with given hosts
        '''
        try:

            if hosts is None or not len(hosts):
                error_msg = ("Create host group {0} failed as no hosts or "
                             "invalid hosts specified".format(hostgroup_name))
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)

            host_state = self.module.params['host_state']
            if host_state != 'present-in-group':
                error_msg = ("Please provide correct host_state while trying"
                             " to create a host group. Empty host group"
                             " creation not allowed")
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)

            LOG.info("Creating host group %s with hosts %s", hostgroup_name,
                     hosts)
            resp = self.conn.provisioning.create_host_group(hostgroup_name,
                                                            hosts)
            LOG.info("the response is %s", resp)
            return True

        except Exception as e:
            error_msg = 'Create host group {0} failed with error {1}'.format(
                hostgroup_name, e)
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def _get_add_hosts(self, existing, requested):
        all_hosts = existing + requested
        add_hosts = list(set(all_hosts) - set(existing))
        return add_hosts

    def _get_remove_hosts(self, existing, requested):
        rem_hosts = list(set(existing).intersection(set(requested)))
        return rem_hosts

    def add_hostgroup_hosts(self, hostgroup, hosts):

        add_list = None
        try:
            existing_hosts = []
            if 'hosts' in hostgroup:
                current_hosts = hostgroup['hosts']
                for host in current_hosts:
                    existing_hosts.append(host['id'])

            LOG.info('existing hosts %s', existing_hosts)
            if hosts and (set(hosts).issubset(set(existing_hosts))):
                LOG.info('Hosts are already present in host group %s',
                         hostgroup['name'])
                return False
            add_list = self._get_add_hosts(existing_hosts, hosts)
            if len(add_list) > 0:
                LOG.info('Adding hosts %s to host group %s', add_list,
                         hostgroup['name'])
                self.conn.provisioning.add_hosts_to_host_group(
                    hostgroup['id'], add_list)
                return True
            else:
                LOG.info('No hosts to add to host group %s',
                         hostgroup['name'])
                return False

        except Exception as e:
            error_msg = (
                ("Adding hosts {0} to host group {1} failed with"
                 "error {2}").format(
                    add_list, hostgroup['name'], str(e)))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def remove_hostgroup_hosts(self, hostgroup, hosts):
        remove_list = None
        try:
            existing_hosts = []
            if 'hosts' in hostgroup:
                current_hosts = hostgroup['hosts']
                for host in current_hosts:
                    existing_hosts.append(host['id'])

            if len(existing_hosts) == 0:
                LOG.info('No hosts are present in host group %s',
                         hostgroup['name'])
                return False

            remove_list = self._get_remove_hosts(existing_hosts, hosts)

            if len(remove_list) > 0:
                LOG.info('Removing hosts %s from host group %s', remove_list,
                         hostgroup['name'])
                self.conn.provisioning.remove_hosts_from_host_group(
                    hostgroup['id'], remove_list)
                return True
            else:
                LOG.info('No hosts to remove from host group %s',
                         hostgroup['name'])
                return False

        except Exception as e:
            error_msg = (("Removing hosts {0} from host group {1} failed"
                          "with error {2}").format(
                remove_list,
                hostgroup['name'],
                str(e)))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def rename_hostgroup(self, hostgroup, new_name):
        try:
            self.conn.provisioning.modify_host_group(
                hostgroup['id'], name=new_name)
            return True
        except Exception as e:
            error_msg = 'Renaming of host group {0} failed with error {1}'.format(
                hostgroup['name'], str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def delete_hostgroup(self, hostgroup):
        '''
        Delete host group from system
        '''
        try:
            self.conn.provisioning.delete_host_group(hostgroup['id'])
            return True
        except Exception as e:
            error_msg = (
                'Deleting host group {0} failed with error {1}'.format(
                    hostgroup['name'], str(e)))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg, **utils.failure_codes(e))

    def _create_result_dict(self, changed, hostgroup_id):
        self.result['changed'] = changed
        if self.module.params['state'] == 'absent':
            self.result['hostgroup_details'] = {}
        else:
            self.result['hostgroup_details'] = self.get_hostgroup(
                hostgroup_id)

    def perform_module_operation(self):
        '''
        Perform different actions on host group based on user parameters
        chosen in playbook
        '''
        state = self.module.params['state']
        host_state = self.module.params['host_state']
        hostgroup_name = self.module.params['hostgroup_name']
        hostgroup_id = self.module.params['hostgroup_id']
        hosts = self.module.params['hosts']
        new_name = self.module.params['new_name']

        if hostgroup_name:
            hostgroup_id = self.get_hostgroup_id_by_name(hostgroup_name)
        if hostgroup_id:
            hostgroup = self.get_hostgroup(hostgroup_id)
        else:
            hostgroup = None
        changed = False
        host_ids_list = []
        if hosts:
            host_ids_list = self.create_host_list(hosts)

        if state == 'present' and not hostgroup and hostgroup_name:
            LOG.info('Creating host group %s', hostgroup_name)
            changed = self.create_hostgroup(hostgroup_name, host_ids_list)
            if changed:
                hostgroup_id = self.get_hostgroup_id_by_name(hostgroup_name)

        if (state == 'present' and hostgroup and host_state ==
                'present-in-group' and host_ids_list and
                len(host_ids_list) > 0):
            LOG.info('Adding hosts to host group %s', hostgroup['name'])
            changed = (
                self.add_hostgroup_hosts(
                    hostgroup,
                    hosts=host_ids_list) or changed)

        if (state == 'present' and hostgroup and host_state ==
                'absent-in-group' and host_ids_list and
                len(host_ids_list) > 0):
            LOG.info('Removing hosts from host group %s', hostgroup['name'])
            changed = (
                self.remove_hostgroup_hosts(
                    hostgroup,
                    hosts=host_ids_list) or changed)

        if state == 'present' and hostgroup and new_name and \
                hostgroup['name'] != new_name:
            LOG.info('Renaming host group %s to %s', hostgroup['name'],
                     new_name)
            changed = self.rename_hostgroup(hostgroup, new_name)

        if state == 'absent' and hostgroup:
            LOG.info('Deleting host group %s ', hostgroup['name'])
            changed = self.delete_hostgroup(hostgroup) or changed

        self._create_result_dict(changed, hostgroup_id)
        # Update the module's final state
        LOG.info('changed %s', changed)
        self.module.exit_json(**self.result)


def main():
    ''' Create PowerStore host group object and perform action on it
        based on user input from playbook'''
    obj = PowerStoreHostgroup()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
