#!/usr/bin/python
# Copyright: (c) 2021, DellEMC
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)
""" Ansible module for managing cluster related operations on PowerStore"""
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: dellemc_powerstore_cluster

version_added: '1.3.0'

short_description: Manage cluster related opeartions on PowerStore.

description:
- Managing cluster on PowerStore storage system includes getting details and
  modifying cluster configuration parameters.

extends_documentation_fragment:
  - dellemc.powerstore.dellemc_powerstore.powerstore

author:
- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

options:
  cluster_name:
    description:
    - The Name of cluster.
    type: str
  chap_mode:
    description:
    - The mode that describes or sets the iSCSI CHAP mode for the cluster.
    type: str
    choices: ['Disabled', 'Single', 'Mutual']
  cluster_id:
    description:
    - Id of the cluster.
    type: str
  new_name:
    description:
    - The new name for the cluster.
    type: str
  service_password:
    description:
    - The password for the service user.
    type: str
  appliance_id:
    description:
    - ID of the appliance.
    - appliance_id and appliance_name are mutually exclusive.
    - is_ssh_enabled has to be passed along with appliance_id.
    type: str
  appliance_name:
    description:
    - Name of the appliance.
    - appliance_id and appliance_name are mutually exclusive.
    - is_ssh_enabled has to be passed along with appliance_name.
    type: str
  is_ssh_enabled:
    description:
    - Whether SSH access is enabled for the cluster.
    - Either appliance_id or appliance_name is to be passed along with
      is_ssh_enabled.
    type: bool
  physical_mtu:
    description:
    - MTU for ethernet ports in the cluster.
    - The MTU can be set between 1500 to 9000.
    type: int
  state:
    description:
    - Define whether the cluster should exist or not.
    - present  indicates that the cluster should exist on the system.
    - absent  indicates that the cluster should not exist on the system.
    type: str
    required: true
    choices: ['absent', 'present']

notes:
- Creation and deletion of cluster is not supported by ansible modules.

'''
EXAMPLES = r'''
- name: get the details of cluster using id
  dellemc_powerstore_cluster:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    cluster_id: "0"
    state: "present"

- name: Modify details of cluster using the name
  dellemc_powerstore_cluster:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    cluster_name: "RT-D1320"
    appliance_id: "A1"
    is_ssh_enabled: True
    service_password: "S@mple_password"
    chap_mode: "Disabled"
    new_name: "new_RT-D1320"
    state: "present"

'''
RETURN = r'''
changed:
    description: Whether or not the resource has changed
    returned: always
    type: bool
    sample: True
cluster_details:
    description: The cluster details.
    type: complex
    returned: When Cluster exists.
    contains:
        id:
            description: The ID of the cluster.
            type: str
        name:
            description: Name of the cluster.
            type: str
        is_ssh_enabled:
            description: Whether or not the ssh is enabled.
            type: bool
        physical_mtu:
            description: MTU for the cluster.
            type: int
        global_id:
            description: The global unique identifier of the cluster.
            type: str
        management_address:
            description: The floating management IP address for the cluster in
                         IPv4 or IPv6 format.
            type: str
        storage_discovery_address:
            description: The floating storage discovery IP address for the
                         cluster in IPv4 or IPv6 format.
            type: str
        master_appliance_id:
            description: The unique identifier of the appliance acting as
                         primary. This parameter is deprecated in version
                         2.0.0.0.
            type: str
        primary_appliance_id:
            description: The unique identifier of the appliance acting as
                         primary. This parameter was added in version 2.0.0.0.
            type: str
        appliance_count:
            description: Number of appliances configured in this cluster.
            type: int
        is_encryption_enabled:
            description: Whether or not Data at Rest Encryption is enabled on
                         the cluster.
            type: bool
        compatibility_level:
            description: The behavioral version of the software version API,
                         It is used to ensure the compatibility across
                         potentially different software versions.
            type: int
        state:
            description: Possible cluster states.
            type: str
        system_time:
            description: Current clock time for the system. System time and
                         all the system reported times are in UTC (GMT+0:00)
                         format.
            type: str
        service_config_details:
            description: Details of the service config for the entered
                         appliance.
            type: complex
            returned: When is_ssh_enabled is passed in the playbook task
            contains:
                id:
                    description: Id of the service configuration.
                    type: str
                appliance_id:
                    description: Id of the appliance for which the service
                                 configuration exists.
                    type: str
                is_ssh_enabled:
                    description: Whether the ssh is enabled for the appliance
                                 or not.
                    type: bool
        service_user_details:
            description: Details of the service user for which the password
                         can be updated.
            type: complex
            returned: when the cluster exists.
            contains:
                id:
                    description: Id of the service user.
                    type: str
                name:
                    description: Name of the service user.
                    type: str
                is_default_password:
                    description: Whether the service user has default password
                                 or not.
                    type: bool
                is_built_in:
                    description: Whether the service user is built in or not.
                    type: bool
        appliance_details:
            description: Name and Id of the appliance for which is_ssh_enabled
                         parameter is used.
            type: complex
            returned: When appliance name or id is passed in the playbook
                      task.
            contains:
                id:
                    description: Id of the appliance.
                    type: str
                name:
                    description: Name of the appliance.
                    type: str

'''

from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import dellemc_ansible_powerstore_utils as utils
from ansible.module_utils.basic import AnsibleModule

LOG = utils.get_logger('dellemc_powerstore_cluster')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.3.0'


class PowerStoreCluster(object):
    """Class with cluster configuration operations"""

    def __init__(self):
        """ Define all parameters required by this module"""

        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_cluster_parameters())

        # initialize the ansible module
        mut_ex_args = [
            ['cluster_name', 'cluster_id'],
            ['appliance_name', 'appliance_id']
        ]
        required_one_of = [['cluster_name', 'cluster_id']]
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mut_ex_args,
            required_one_of=required_one_of
        )

        msg = 'HAS_PY4PS = {0} , IMPORT_ERROR = {1}'.format(HAS_PY4PS,
                                                            IMPORT_ERROR)
        LOG.info(msg)

        if not HAS_PY4PS:
            self.module.fail_json(msg=IMPORT_ERROR)
        msg = 'IS_SUPPORTED_PY4PS_VERSION = {0} , VERSION_ERROR = {1}' \
            .format(IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR)
        LOG.info(msg)

        if not IS_SUPPORTED_PY4PS_VERSION:
            self.module.fail_json(msg=VERSION_ERROR)

        # result is a dictionary that contains changed status and
        # cluster details
        self.result = {"changed": False, "cluster_details": {}}

        self.conn = utils.get_powerstore_connection(
            self.module.params, application_type=APPLICATION_TYPE)
        self.configuration = self.conn.config_mgmt
        msg = 'Got Py4Ps instance for configuring cluster on' \
              ' PowerStore {0}'.format(self.conn)
        LOG.info(msg)

    def get_cluster_details(self, cluster_name=None, cluster_id=None):
        """
        Get the cluster details
        """
        try:
            cluster_details = None
            if cluster_name:
                cluster_details = \
                    self.configuration.get_cluster_by_name(cluster_name)
                if cluster_details:
                    cluster_details = cluster_details[0]

            if cluster_id:
                cluster_details =\
                    self.configuration.get_cluster_details(
                        cluster_id=cluster_id)
            return cluster_details
        except Exception as e:
            name_or_id = cluster_name if cluster_name else cluster_id
            msg = 'Get details of cluster {0} failed' \
                  ' with error: {1}'.format(name_or_id, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def show_cluster_details(self, cluster_id, appliance_id):
        """
        Show the details of the cluster.
        """
        cluster_details = self.get_cluster_details(
            cluster_id=cluster_id)
        chap_config_details = self.get_chap_config_details()
        if cluster_details:
            cluster_details['chap_mode'] = chap_config_details['mode']
            cluster_details['service_config_details'] = None
            if appliance_id:
                cluster_details['service_config_details'] = \
                    self.configuration.get_service_config_details(appliance_id)
                cluster_details['service_user_details'] = \
                    self.get_service_user_details()
                appliance_details = self.get_appliance_details(
                    appliance_id, None)
                cluster_details['appliance_details'] = {}
                cluster_details['appliance_details']['id'] =\
                    appliance_details['id']
                cluster_details['appliance_details']['name'] =\
                    appliance_details['name']

        return cluster_details

    def modify_cluster(self, cluster_id, service_config_id,
                       modify_dict=None):
        """
        Update the parameters for clusters.
        """
        try:
            if 'name' in modify_dict.keys():
                self.configuration.modify_cluster(cluster_id,
                                                  name=modify_dict['name'])
            if 'physical_mtu' in modify_dict.keys():
                self.configuration.modify_cluster(
                    cluster_id, physical_mtu=modify_dict['physical_mtu'])
            if 'service_password' in modify_dict.keys():
                self.configuration.modify_service_user(
                    '1', password=modify_dict['service_password'])
            if 'is_ssh_enabled' in modify_dict.keys() and service_config_id:
                self.configuration.modify_service_config(
                    service_config_id,
                    is_ssh_enabled=modify_dict['is_ssh_enabled'])
            if 'chap_mode' in modify_dict.keys():
                self.configuration.modify_chap_config(
                    '0', mode=modify_dict['chap_mode'])
        except Exception as e:
            msg = 'Modify operation failed' \
                  ' with error: {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_chap_config_details(self):
        """
        Get the details of chap config.
        """
        try:
            # The ID of the CHAP config will always be 0
            return \
                self.configuration.get_chap_config_details(chap_config_id='0')

        except Exception as e:
            msg = 'Get details of chap config with id = 0 failed' \
                  ' with error: {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_service_user_details(self):
        """
        Get the details of the service user
        """
        try:
            # There can be only one service user with name as
            # 'service' and id as '1'. This can't be changed or updated.
            return self.configuration.get_service_user_details(
                service_user_id='1')
        except Exception as e:
            msg = 'Get details of service user with id: 1 and name: service' \
                  ' failed with error: {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_service_config_details(self, appliance_id):
        """
        Get the service config details
        """
        try:
            return self.configuration.get_service_config_by_appliance_id(
                appliance_id)[0]
        except Exception as e:
            msg = 'Get details of service config for appliance with id: {0}' \
                  ' failed with error: {1}'.format(appliance_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_appliance_details(self, appliance_id, appliance_name):
        """
        Get the appliance details
        """
        try:
            if appliance_name:
                appliance_details = self.configuration.get_appliance_by_name(
                    appliance_name)
                if appliance_details:
                    return appliance_details[0]
            if appliance_id:
                return self.configuration.get_appliance_details(appliance_id)
            return None

        except Exception as e:
            msg = 'Get appliance details failed with error: {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def perform_module_operation(self):
        """
        Perform different actions on cluster module based on parameters
        chosen in playbook
        """

        cluster_id = self.module.params['cluster_id']
        cluster_name = self.module.params['cluster_name']
        is_ssh_enabled = self.module.params['is_ssh_enabled']
        chap_mode = self.module.params['chap_mode']
        service_password = self.module.params['service_password']
        physical_mtu = self.module.params['physical_mtu']
        new_name = self.module.params['new_name']
        state = self.module.params['state']
        appliance_name = self.module.params['appliance_name']
        appliance_id = self.module.params['appliance_id']

        changed = False
        # if is_ssh_enabled is passed and appliance name/id is not passed.
        if not (appliance_id or appliance_name) and is_ssh_enabled is not None:
            self.module.fail_json(
                msg='Either appliance id or appliance name is needed along'
                    ' with is_ssh_enabled parameter. Please enter a valid'
                    ' appliance id/name')
        # if appliance name/id is passed and is_ssh_enabled is not passed.
        if is_ssh_enabled is None and (appliance_id or appliance_name):
            self.module.fail_json(
                msg='is_ssh_enabled parameter is also needed along with '
                    'appliance id/name. Please enter a valid is_ssh_enabled '
                    'value.')
        # Getting the service_config_id from the appliance details
        # for updating is_ssh_enabled.
        service_config_id = None
        if appliance_id or appliance_name:
            appliance_details = self.get_appliance_details(
                appliance_id, appliance_name)
            if not appliance_details:
                self.module.fail_json(
                    msg="Unable to fetch the appliance details. Please provide"
                        " a valid appliance_name.")
            service_config_id = appliance_details['id']
            appliance_id = appliance_details['id']

        cluster_details = self.get_cluster_details(cluster_name, cluster_id)
        if cluster_details and cluster_name:
            cluster_id = cluster_details['id']

        if state == 'present' and not cluster_details:
            self.module.fail_json(
                msg="Creation of cluster is currently not supported by the "
                    "module. Please enter the cluster_name/cluster_id of the "
                    "existing cluster.")

        if state == 'absent' and cluster_details:
            self.module.fail_json(
                msg="Invalid operation. Deletion of the existing cluster is "
                    "currently not supported by the module.")

        # cluster details with all the parameters needed for modify
        cluster_details = self.show_cluster_details(cluster_id, appliance_id)

        if state == 'present' and cluster_details:
            update_params_dict = modify_payload(
                cluster_details, new_name, physical_mtu, service_password,
                chap_mode, is_ssh_enabled)
            if update_params_dict:
                self.modify_cluster(cluster_id, service_config_id,
                                    update_params_dict)
                changed = True

        cluster_details = self.show_cluster_details(cluster_id, appliance_id)
        self.result["changed"] = changed
        self.result["cluster_details"] = cluster_details
        self.module.exit_json(**self.result)


def modify_payload(cluster_details, new_name=None, physical_mtu=None,
                   service_password=None, chap_mode=None, is_ssh_enabled=None):
    """
    Dictionary containing all the parameters which are to be updated
    :param cluster_details: The details of the cluster
    :param physical_mtu: MTU for the cluster
    :param new_name: New name for the cluster
    :param service_password: new password for the service user
    :param chap_mode: CHAP mode
    :param is_ssh_enabled: To enable ssh for the service users or not
    :return: Returns payload_dict, includes parameters which are to be updated
    """
    payload = {}
    if service_password is not None:
        payload['service_password'] = service_password
    if physical_mtu is not None and\
            physical_mtu != int(cluster_details['physical_mtu']):
        payload['physical_mtu'] = physical_mtu
    if new_name is not None and new_name != "" and\
            cluster_details['name'].lower() != new_name.lower():
        payload['name'] = new_name
    if chap_mode and \
            (not cluster_details['chap_mode'] or
             (chap_mode.lower() != cluster_details['chap_mode'].lower())):
        payload['chap_mode'] = chap_mode
    if cluster_details['service_config_details'] is not None:
        service_config_ssh = \
            cluster_details['service_config_details']['is_ssh_enabled']
        if is_ssh_enabled is not None and service_config_ssh != is_ssh_enabled:
            payload['is_ssh_enabled'] = is_ssh_enabled

    return payload


def get_powerstore_cluster_parameters():
    """This method provides parameters required for the ansible cluster
    module on PowerStore"""
    return dict(
        cluster_name=dict(), cluster_id=dict(),
        appliance_name=dict(), appliance_id=dict(),
        service_password=dict(no_log=True),
        chap_mode=dict(choices=['Disabled', 'Single', 'Mutual']),
        is_ssh_enabled=dict(type='bool'), new_name=dict(),
        physical_mtu=dict(type='int'),
        state=dict(required=True, choices=['present', 'absent'])
    )


def main():
    """ Create cluster config object and perform actions on it
    based on user input from playbook"""

    obj = PowerStoreCluster()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
