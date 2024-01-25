#!/usr/bin/python
# Copyright: (c) 2024, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
module: storage_container
version_added: '2.0.0'
short_description: Manage storage container for PowerStore
description:
- Managing storage containers on PowerStore Storage System includes creating
  a storage container, getting details of a storage container, modifying a
  storage container and deleting a storage container.
- This module also supports creating and deleting storage container
  destinations.

author:
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>
- Bhavneet Sharma (@Bhavneet-Sharma) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerstore.powerstore

options:
  storage_container_id:
    description:
    - The unique identifier of the storage container.
    type: str
  storage_container_name:
    description:
    - Name for the storage container.
    - This should be unique across all storage containers in the cluster.
    type: str
  quota:
    description:
    - The total number of bytes that can be provisioned/reserved against this
      storage container.
    - A value of C(0) means there is no limit.
    - It is possible to set the quota to a value that overprovisions the amount
      of space available in the system.
    type: int
  quota_unit:
    description:
    - Unit of the quota.
    choices: ['GB', 'TB', 'PB']
    type: str
    default: 'GB'
  storage_protocol:
    description:
    - The type of storage container.
    - C(SCSI) is set when a storage container is dedicated to C(SCSI) usage.
    - C(NVMe) is set when a storage container is dedicated to C(NVMe) usage.
    type: str
    choices: ['SCSI', 'NVMe']
  high_water_mark:
    description:
    - This is the percentage of the quota that can be consumed before an alert
      is raised.
    - This is used only for creating a storage container.
    type: int
  new_name:
    description:
    - The new name of the storage container.
    type: str
  force_delete:
    description:
    - This option overrides the error and allows the deletion to continue in
      case there are any vVols associated with the storage container.
    - Use with great caution.
    type: bool
    default: false
  state:
    description:
    - Define whether the storage container should exist or not.
    - For Delete operation only, it should be set to C(absent).
    required: false
    choices: ['absent', 'present']
    type: str
    default: 'present'
  storage_container_destination_state:
    description:
    - Define whether the storage container destination should exist in the
      storage container.
    - To delete storage container destination, it should be C(absent).
    choices: ['present', 'absent']
    type: str
    default: 'present'
  storage_container_destination:
    description:
    - It contains details of remote system and remote storage container.
    - It is required while creating and deleting storage container
      destinations.
    type: dict
    suboptions:
      remote_system:
        description:
        - Name or ID of the remote system.
        required: true
        type: str
      remote_address:
        description:
        - The IP address of the remote storage system.
        type: str
        required: true
      user:
        description:
        - Username of the remote PowerStore storage system.
        required: true
        type: str
      password:
        description:
        - Password of the remote PowerStore storage system.
        required: true
        type: str
      port:
        description:
        - Port number of the remote PowerStore storage system.
        type: int
        default: 443
      timeout:
        description:
        - Time after which connection will be terminated.
        - It is mentioned in seconds.
        type: int
        default: 120
      validate_certs:
        description:
        - Boolean variable to specify whether to validate SSL certificate or
          not.
        - C(true) - indicates that the SSL certificate should be verified. Set
          the environment variable REQUESTS_CA_BUNDLE to the path of the SSL
          certificate.
        - C(false) - indicates that the SSL certificate should not be verified.
        type: bool
        default: true
        aliases:
          - verifycert
      remote_storage_container:
        description:
        - Name or ID of the remote storage container on the remote storage
          system.
        required: true
        type: str

notes:
- The I(check_mode) is supported.
- Either storage container name or ID required while deleting the storage
  container destination.
- The details of the storage container destination are embedded in the response
  of the storage container.
'''

EXAMPLES = r'''

- name: Create a storage_container
  dellemc.powerstore.storage_container:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    storage_container_name: "Ansible_storage_container_1"
    quota: 0
    storage_protocol: "SCSI"
    high_water_mark: 60

- name: Get the details of the storage container using id
  dellemc.powerstore.storage_container:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    storage_container_id: "storage_container_id"
    state: "present"

- name: Get the details of the storage container by name
  dellemc.powerstore.storage_container:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    storage_container_name: "Ansible_storage_container_1"

- name: Modify a storage container
  dellemc.powerstore.storage_container:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    storage_container_name: "Ansible_storage_container_1"
    quota: 20
    quota_unit: "GB"
    storage_protocol: "NVMe"
    state: "present"

- name: Rename a storage container
  dellemc.powerstore.storage_container:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    storage_container_name: "Ansible_storage_container_1"
    new_name: "Ansible_storage_container_1_new"

- name: Delete a storage container containing vVols
  dellemc.powerstore.storage_container:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    storage_container_name: "Ansible_storage_container_1"
    force_delete: true
    state: "absent"

- name: Delete a storage container using id
  dellemc.powerstore.storage_container:
    array_ip: "{{array_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    storage_container_id: "storage_container_id_1"
    state: "absent"

- name: Create a storage container destination
  dellemc.powerstore.storage_container:
    array_ip: "{{array_ip}}"
    user: "{{user}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_container_name: "local_storage_container"
    storage_container_destination:
      remote_address: "x.x.x.x"
      user: "{{user}}"
      password: "{{password}}"
      validate_certs: "{{validate_certs}}"
      remote_system: "remote_system_name"
      remote_storage_container: "remote_storage_container_name"

- name: Delete a storage container destination
  dellemc.powerstore.storage_container:
    array_ip: "{{array_ip}}"
    user: "{{user}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_container_id: "storage_container_id"
    storage_container_destination_state: "absent"
    storage_container_destination:
      remote_address: "x.x.x.x"
      user: "{{user}}"
      password: "{{password}}"
      validate_certs: "{{validate_certs}}"
      remote_system: "remote_system_name"
      remote_storage_container: "remote_storage_container_name"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"

storage_container_details:
    description: Details of the storage container.
    returned: When storage container exists.
    type: complex
    contains:
        id:
            description: The unique identifier of the storage container.
            type: str
        name:
            description: The name for the storage container.
            type: str
        storage_protocol:
            description: The type of storage container.
            type: str
        quota:
            description: The total number of bytes that can be
                         provisioned/reserved against this storage container.
            type: int
        replication_groups:
            description: Properties of a Replication Group.
            type: list
            contains:
                id:
                    description: Unique identifier of the Replication Group
                                 instance.
                    type: str
                name:
                    description: Name of the Replication Group.
                    type: str
        virtual_volumes:
            description: The virtual volumes associated to the storage
                         container.
            type: list
            contains:
                id:
                    description: The unique identifier of the virtual volume.
                    type: str
                name:
                    description: The name of the virtual volume.
                    type: str
        destinations:
            description: A storage container destination defines replication
                         destination for a local storage container on a
                         remote system.
            type: list
            contains:
                id:
                    description: The unique id of the storage container
                                 destination.
                    type: str
                remote_system_id:
                    description: The unique id of the remote system.
                    type: str
                remote_system_name:
                    description: The name of the remote system.
                    type: str
                remote_storage_container_id:
                    description: The unique id of the destination storage
                                 container on the remote system.
                    type: str
        datastores:
            description: List of associated datstores.
            type: list
            contains:
                id:
                    description: Unique identifier of the datastore instance.
                    type: str
                name:
                    description: User-assigned name of the datastore in vCenter.
                    type: str

    sample: {
        "datastores": [],
        "destinations": [],
        "id": "e0ccd953-5650-41d8-9bce-f36d876d6a2a",
        "name": "Ansible_storage_container_1",
        "quota": 21474836480,
        "replication_groups": [],
        "storage_protocol": "NVMe",
        "storage_protocol_l10n": "NVMe",
        "virtual_volumes": []
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

LOG = utils.get_logger('storage_container')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/3.1.0'


class PowerStoreStorageContainer(object):
    """Class with storage container Operations"""
    cluster_name = None
    cluster_global_id = None

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(
            get_powerstore_storage_container_parameters())

        # initialize the Ansible module
        mut_ex_args = [['storage_container_id', 'storage_container_name']]
        required_one_of = [['storage_container_id', 'storage_container_name']]

        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True,
            mutually_exclusive=mut_ex_args,
            required_one_of=required_one_of
        )
        self.result = dict(
            changed=False,
            storage_container_details={}
        )

        msg = f'HAS_PY4PS = {HAS_PY4PS}, IMPORT_ERROR = {IMPORT_ERROR}'
        LOG.info(msg)
        if HAS_PY4PS is False:
            self.module.fail_json(msg=IMPORT_ERROR)
        msg = (f'IS_SUPPORTED_PY4PS_VERSION = {IS_SUPPORTED_PY4PS_VERSION} , '
               f'VERSION_ERROR = {VERSION_ERROR}')
        LOG.info(msg)
        if IS_SUPPORTED_PY4PS_VERSION is False:
            self.module.fail_json(msg=VERSION_ERROR)

        self.conn = utils.get_powerstore_connection(
            self.module.params,
            application_type=APPLICATION_TYPE)
        self.configuration = self.conn.config_mgmt
        self.protection = self.conn.protection
        msg = 'Got Py4ps instance for configuration {0} and protection {1}' \
              ' on PowerStore'.format(self.configuration, self.protection)
        LOG.info(msg)
        check_mode_msg = f'Check mode flag is {self.module.check_mode}'
        LOG.info(check_mode_msg)

    def create_storage_container(self, storage_container_name, quota,
                                 storage_protocol, high_water_mark):
        """Create a storage container"""
        try:
            msg = f'Attempting to create a storage container with name' \
                  f' {storage_container_name}'
            LOG.info(msg)
            con_details = {}
            if not self.module.check_mode:
                create_params = dict()
                create_params['name'] = storage_container_name
                create_params['quota'] = quota
                create_params['storage_protocol'] = storage_protocol
                create_params['high_water_mark'] = high_water_mark

                resp = self.configuration.create_storage_container(
                    create_parameters=create_params)

                if resp:
                    con_details = self.get_storage_container_details(
                        storage_container_id=resp['id'])

                msg = f'Successfully created storage container with details' \
                      f' {con_details}'
                LOG.info(msg)

            return con_details

        except Exception as e:
            msg = (f'Creation of storage container with name'
                   f' {storage_container_name} on PowerStore array name : '
                   f'{self.cluster_name} , global id : '
                   f'{self.cluster_global_id} failed with error {str(e)} ')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def delete_storage_container(self, storage_container_id, force_delete):
        """ Delete a storage container """

        try:
            msg = f'Deleting storage container with identifier:' \
                  f' {storage_container_id}'
            LOG.info(msg)
            if not self.module.check_mode:
                delete_params = {'force': force_delete}
                self.configuration.delete_storage_container(
                    storage_container_id=storage_container_id,
                    delete_parameters=delete_params)
            return self.get_storage_container_details(
                storage_container_id=storage_container_id)

        except Exception as e:
            msg = (f'Deletion of storage container {storage_container_id}'
                   f' failed with error {str(e)}')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def update_storage_container_details(self, con_details):
        """Update the storage container destination detail"""
        index = 0
        for dest in con_details['destinations']:
            resp = self.get_remote_system(dest['remote_system_id'])['name']
            if resp is not None:
                con_details['destinations'][index]['remote_system_name'] = resp
            index += 1
        return con_details

    def get_remote_storage_container(self, remote_container):
        """Get the remote storage container details with remote connection"""
        try:
            remote_container_name = remote_container_id = None
            if utils.name_or_id(remote_container) == 'NAME':
                remote_container_name = remote_container
            else:
                remote_container_id = remote_container

            remote_params = dict()
            LOG.info("Getting remote storage container details")
            remote_params['array_ip'] = self.module.params[
                'storage_container_destination']['remote_address']
            con_params = ['user', 'password', 'validate_certs', 'port',
                          'timeout']
            for parm in con_params:
                if parm in self.module.params['storage_container_destination']:
                    remote_params[parm] = self.module.params[
                        'storage_container_destination'][parm]

            conn = utils.get_powerstore_connection(
                remote_params, application_type=APPLICATION_TYPE)
            remote_config = conn.config_mgmt
            if remote_container_id:
                con_details = remote_config.get_storage_container_details(
                    remote_container_id)
            else:
                con_details = remote_config.\
                    get_storage_container_details_by_name(remote_container_name)
            msg = f'Successfully got storage container details {con_details}'
            LOG.debug(msg)
            return con_details
        except Exception as e:
            msg = (f'Get remote storage container details for PowerStore array'
                   f' failed with error {str(e)} ')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_storage_container_details(self, storage_container_id=None,
                                      storage_container_name=None):
        """ Get storage container details by name or id """

        try:
            msg = (f'Getting storage container details with '
                   f'storage_container_id {storage_container_id}, '
                   f'storage_container_name {storage_container_name}')
            LOG.info(msg)
            con_details = None
            if storage_container_id:
                con_details = self.configuration.get_storage_container_details(
                    storage_container_id)
            elif storage_container_name:
                con_details = \
                    self.configuration.get_storage_container_details_by_name(
                        storage_container_name)

            # update the storage container details with destination details
            if con_details is not None and \
                    con_details['destinations'] is not None:
                con_details = self.update_storage_container_details(
                    con_details)

            msg = f'Successfully got storage container details {con_details}'
            LOG.info(msg)
            return con_details

        except Exception as e:
            msg = (f'Get storage container details for PowerStore array name '
                   f': {self.cluster_name} , global id : '
                   f'{self.cluster_global_id} failed with error {str(e)} ')
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR \
                    and e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def is_modify_required(self, storage_container_details, quota,
                           storage_protocol, new_name):
        """To get the details of the fields to be modified."""

        msg = f'Storage container details: {storage_container_details}'
        LOG.info(msg)
        modify_dict = dict()

        if self.module.params['quota'] is not None and \
                quota != storage_container_details['quota']:
            modify_dict['quota'] = quota
        if storage_protocol is not None and \
                storage_protocol != storage_container_details['storage_protocol']:
            modify_dict['storage_protocol'] = storage_protocol
        if new_name is not None and \
                new_name != storage_container_details['name']:
            modify_dict['name'] = new_name

        if modify_dict:
            return modify_dict
        else:
            return None

    def modify_storage_container_details(self, storage_container_id,
                                         modify_params):
        """Perform modify operations on a storage container"""

        try:
            if not self.module.check_mode:
                self.configuration.modify_storage_container_details(
                    storage_container_id=storage_container_id,
                    modify_parameters=modify_params)
            return True
        except Exception as e:
            msg = (f'Failed to modify the storage container instance '
                   f'with error {str(e)}')
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_remote_system(self, remote_system, remote_address=None):
        """Get the remote system ID"""
        try:
            LOG.info("Getting remote system details")
            remote_system_name = remote_system_id = None
            if utils.name_or_id(remote_system) == 'ID':
                remote_system_id = remote_system
            else:
                remote_system_name = remote_system

            if remote_system_name is not None:
                resp = self.protection.get_remote_system_by_name(
                    remote_system_name)
                if resp and len(resp) == 1:
                    if resp[0]['management_address'] == remote_address:
                        return resp[0]
                    else:
                        err_msg = f"Enter the valid remote_address for " \
                                  f"remote_system {remote_system}."
                        LOG.error(err_msg)
                        self.module.fail_json(msg=err_msg)
                elif resp and len(resp) > 1:
                    resp = self.protection.get_remote_system_by_name(
                        remote_system_name, remote_address)
                    return resp[0]

            if remote_system_id:
                resp = self.protection.get_remote_system_details(
                    remote_system_id)
                return resp
        except Exception as e:
            msg = f'Failed to get the remote system {remote_system} with ' \
                  f'error: {str(e)}'
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def create_storage_container_destination(self, params, con_details):
        """create the storage container destination"""
        remote_sys_id = remote_con_id = None
        remote_sys = self.get_remote_system(
            params['storage_container_destination']['remote_system'],
            params['storage_container_destination']['remote_address'])
        if remote_sys is not None:
            remote_sys_id = remote_sys['id']
        else:
            msg = f"Unable to find the remote system " \
                  f"{params['storage_container_destination']['remote_system']}"
            self.module.fail_json(msg=msg)

        remote_con = self.get_remote_storage_container(
            params['storage_container_destination']['remote_storage_container'])
        if remote_con is not None:
            remote_con_id = remote_con['id']
        else:
            msg = f"Unable to find the remote storage container " \
                  f"{params['storage_container_destination']['remote_storage_container']}"
            self.module.fail_json(msg=msg)

        if con_details['destinations'] is not None:
            all_dest = con_details['destinations']
            if is_destination_exists(all_dest, remote_sys_id, remote_con_id) \
                    is not None:
                # Destination container already exists, Idempotency
                return False
        try:
            LOG.info("Creating the storage container destination for "
                     "the storage container.}")
            create_params = dict()
            create_params['storage_container_id'] = con_details.get('id')
            create_params['remote_storage_container_id'] = remote_con_id
            create_params['remote_system_id'] = remote_sys_id

            if not self.module.check_mode:
                self.configuration.create_storage_container_destination(
                    create_destination_params=create_params)
            return True
        except Exception as e:
            msg = f"Failed to create a storage container destination with " \
                  f"error: {str(e)}"
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def delete_storage_container_destination(self, params, con_details):
        """Delete the storage container destination"""
        if 'storage_container_destination' not in params or not \
                params['storage_container_destination']:
            msg = "The storage_container_destination dict is required to " \
                  "delete the storage container destination."
            self.module.fail_json(msg=msg)

        remote_sys_id = remote_con_id = None
        remote_sys = self.get_remote_system(
            params['storage_container_destination']['remote_system'],
            params['storage_container_destination']['remote_address'])
        if remote_sys is not None:
            remote_sys_id = remote_sys['id']
        else:
            msg = f"Unable to find the remote system " \
                  f"{params['storage_container_destination']['remote_system']}"
            self.module.fail_json(msg=msg)

        remote_con = self.get_remote_storage_container(
            params['storage_container_destination']['remote_storage_container'])
        if remote_con is not None:
            remote_con_id = remote_con['id']
        else:
            msg = f"Unable to find the remote storage container " \
                  f"{params['storage_container_destination']['remote_storage_container']}"
            self.module.fail_json(msg=msg)

        try:
            if con_details['destinations'] is not None:
                all_dest = con_details['destinations']
                dest_id = is_destination_exists(all_dest, remote_sys_id,
                                                remote_con_id)
                if dest_id:
                    # Destination container exists
                    if not self.module.check_mode:
                        self.configuration.delete_storage_container_destination(
                            storage_container_destination_id=dest_id)
                    return True
        except Exception as e:
            msg = f"Failed to delete a storage container destination with " \
                  f"error: {str(e)}"
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))


def is_destination_exists(destinations, remote_sys_id, remote_con_id):
    """Check whether storage container exists or not"""
    for dest in destinations:
        if dest['remote_storage_container_id'] == remote_con_id and \
                dest['remote_system_id'] == remote_sys_id:
            return dest['id']
    return None


def get_powerstore_storage_container_parameters():
    """This method provide the parameters required for the storage container
       operations for PowerStore"""
    return dict(
        storage_container_id=dict(), storage_container_name=dict(),
        new_name=dict(), quota=dict(type='int'),
        quota_unit=dict(choices=['GB', 'TB', 'PB'], default='GB'),
        high_water_mark=dict(type='int'),
        storage_protocol=dict(choices=['SCSI', 'NVMe']),
        force_delete=dict(type='bool', default=False),
        state=dict(type='str', choices=['present', 'absent'],
                   default='present'),
        storage_container_destination_state=dict(
            choices=['present', 'absent'], default='present', type='str'),
        storage_container_destination=dict(type='dict', options=dict(
            remote_address=dict(required=True, type='str'),
            user=dict(required=True, type='str'),
            password=dict(required=True, no_log=True),
            validate_certs=dict(type='bool', aliases=['verifycert'],
                                default=True),
            port=dict(type='int', default=443),
            timeout=dict(type='int', default=120),
            remote_storage_container=dict(type='str', required=True),
            remote_system=dict(type='str', required=True)))
    )


class StorageContainerCreateHandler():
    def handle(self, con_object, con_params, storage_container_details, quota):
        if con_params['state'] == 'present' and not storage_container_details:
            storage_container_details = con_object.create_storage_container(
                storage_container_name=con_params['storage_container_name'],
                quota=quota, storage_protocol=con_params['storage_protocol'],
                high_water_mark=con_params['high_water_mark'])
            con_object.result['changed'] = True

        StorageContainerModifyHandler().handle(
            con_object, con_params, storage_container_details, quota)


class StorageContainerModifyHandler():
    def handle(self, con_object, con_params, storage_container_details, quota):
        if con_params['state'] == 'present' and storage_container_details:
            modify_params = con_object.is_modify_required(
                storage_container_details=storage_container_details,
                quota=quota, storage_protocol=con_params['storage_protocol'],
                new_name=con_params['new_name'])
            if modify_params:
                msg = (f'Attempting to modify the storage container with id '
                       f'{storage_container_details.get("id")}')
                LOG.info(msg)
                changed = con_object.modify_storage_container_details(
                    storage_container_id=storage_container_details.get("id"),
                    modify_params=modify_params)
                storage_container_details = con_object.\
                    get_storage_container_details(storage_container_details.get("id"))
                con_object.result['changed'] = changed

        StorageContainerDestinationCreateHandler().handle(
            con_object, con_params, storage_container_details)


class StorageContainerDestinationCreateHandler():
    def handle(self, con_object, con_params, storage_container_details):
        if con_params['state'] == 'present' and storage_container_details and \
                con_params['storage_container_destination'] and \
                con_params['storage_container_destination_state'] == 'present':
            changed = con_object.create_storage_container_destination(
                params=con_params, con_details=storage_container_details)

            storage_container_details = \
                con_object.get_storage_container_details(
                    storage_container_details.get("id"))
            con_object.result['changed'] = changed

        StorageContainerDestinationDeleteHandler().handle(
            con_object, con_params, storage_container_details)


class StorageContainerDestinationDeleteHandler:
    def handle(self, con_object, con_params, storage_container_details):
        if con_params['state'] == 'present' and storage_container_details and \
                con_params['storage_container_destination_state'] == 'absent':
            changed = con_object.delete_storage_container_destination(
                params=con_params, con_details=storage_container_details)

            storage_container_details = con_object.\
                get_storage_container_details(storage_container_details.get("id"))
            con_object.result['changed'] = changed

        StorageContainerDeleteHandler().handle(
            con_object, con_params, storage_container_details)


class StorageContainerDeleteHandler():
    def handle(self, con_object, con_params, storage_container_details):
        if con_params['state'] == 'absent' and storage_container_details:
            storage_container_details = con_object.delete_storage_container(
                storage_container_id=storage_container_details.get("id"),
                force_delete=con_params['force_delete'])
            con_object.result['changed'] = True
        StorageContainerExitHandler().handle(con_object,
                                             storage_container_details)


class StorageContainerExitHandler():
    def handle(self, con_object, storage_container_details):
        con_object.result['storage_container_details'] = storage_container_details
        con_object.module.exit_json(**con_object.result)


class StorageContainerHandler():
    def handle(self, con_object, con_params):
        quota = utils.get_size_bytes(con_params['quota'],
                                     con_params['quota_unit'])
        storage_container_details = con_object.get_storage_container_details(
            storage_container_id=con_params['storage_container_id'],
            storage_container_name=con_params['storage_container_name'])
        StorageContainerCreateHandler().handle(
            con_object, con_params, storage_container_details, quota)


def main():
    """ Create PowerStore storage container object and perform action on it
        based on user input from playbook"""
    obj = PowerStoreStorageContainer()
    StorageContainerHandler().handle(obj, obj.module.params)


if __name__ == '__main__':
    main()
