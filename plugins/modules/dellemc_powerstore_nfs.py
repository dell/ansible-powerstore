#!/usr/bin/python
# Copyright: (c) 2020-2021, DellEMC
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Ansible module for managing NFS exports on PowerStore"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r"""
module: dellemc_powerstore_nfs
version_added: '1.1.0'
short_description: Manage NFS exports on Dell EMC PowerStore.
description:
- Managing NFS exports on PowerStore Storage System includes creating new NFS
  Export, getting details of NFS export, modifying attributes of NFS export,
  and deleting NFS export.

author:
- Akash Shendge (@shenda1) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerstore.dellemc_powerstore.powerstore

options:
  nfs_export_name:
    description:
    - The name of the NFS export.
    - Mandatory for create operation.
    - Specify either nfs_export_name or nfs_export_id(but not both) for any
      operation.
    type: str
  nfs_export_id:
    description:
    - The ID of the NFS export.
    type: str
  filesystem:
    description:
    - The ID/Name of the filesystem for which the NFS export will be created.
    - Either filesystem or snapshot is required for creation of the NFS
      Export.
    - If filesystem name is specified, then nas_server is required to uniquely
      identify the filesystem.
    - If filesystem parameter is provided, then snapshot cannot be specified.
    type: str
  snapshot:
    description:
    - The ID/Name of the Snapshot for which NFS export will be created.
    - Either filesystem or snapshot is required for creation of the NFS
      Export.
    - If snapshot name is specified, then nas_server is required to
      uniquely identify the snapshot.
    - If snapshot parameter is provided, then filesystem cannot be specified.
    - NFS export can be created only if access type of snapshot is "protocol".
    type: str
  nas_server:
    description:
    - The NAS server. This could be the name or ID of the NAS server.
    type: str
  path:
    description:
    - Local path to export relative to the NAS server root.
    - With NFS, each export of a file_system or file_snap must have a unique
      local path.
    - Mandatory while creating NFS export.
    type: str
  description:
    description:
    - The description for the NFS export.
    type: str
  default_access:
    description:
    - Default access level for all hosts that can access the Export.
    - For hosts that need different access than the default, they can be
      configured by adding to the list.
    - If default_access is not mentioned during creation, then NFS export will
      be created with No_Access.
    choices: ['NO_ACCESS', 'READ_ONLY', 'READ_WRITE', 'ROOT',
                'READ_ONLY_ROOT']
    type: str
  no_access_hosts:
    description:
    - Hosts with no access to the NFS export.
    type: list
    elements: str
  read_only_hosts:
    description:
    - Hosts with read-only access to the NFS export.
    type: list
    elements: str
  read_only_root_hosts:
    description:
    - Hosts with read-only access for root user to the NFS export.
    type: list
    elements: str
  read_write_hosts:
    description:
    - Hosts with read and write access to the NFS export.
    type: list
    elements: str
  read_write_root_hosts:
    description:
    - Hosts with read and write access for root user to the NFS export.
    type: list
    elements: str
  min_security:
    description:
    - NFS enforced security type for users accessing an NFS export.
    - If not specified at the time of creation, it will be set to SYS.
    choices: ['SYS', 'KERBEROS', 'KERBEROS_WITH_INTEGRITY',
                'KERBEROS_WITH_ENCRYPTION']
    type: str
  anonymous_uid:
    description:
    - Specifies the user ID of the anonymous account.
    - If not specified at the time of creation, it will be set to -2.
    type: int
  anonymous_gid:
    description:
    - Specifies the group ID of the anonymous account.
    - If not specified at the time of creation, it will be set to -2.
    type: int
  is_no_suid:
    description:
    - If set, do not allow access to set SUID. Otherwise, allow access.
    - If not specified at the time of creation, it will be set to False.
    type: bool
  host_state:
    description:
    - Define whether the hosts can access the NFS export.
    - Required when adding or removing host access from the export.
    choices: ['present-in-export', 'absent-in-export']
    type: str
  state:
    description:
    - Define whether the NFS export should exist or not.
    required: true
    choices: ['absent', 'present']
    type: str
"""

EXAMPLES = r"""
- name: Create NFS export (filesystem)
  dellemc_powerstore_nfs:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    nfs_export_name: "{{export_name1}}"
    filesystem: "{{filesystem}}"
    nas_server: "{{nas_server}}"
    path: "{{path1}}"
    description: "sample description"
    default_access: "NO_ACCESS"
    no_access_hosts:
      - "{{host5}}"
    read_only_hosts:
      - "{{host1}}"
    read_only_root_hosts:
      - "{{host2}}"
    read_write_hosts:
      - "{{host3}}"
    read_write_root_hosts:
      - "{{host4}}"
    min_security: "SYS"
    anonymous_uid: 1000
    anonymous_gid: 1000
    is_no_suid: True
    host_state: "present-in-export"
    state: "present"

- name: Create NFS export Create NFS export for filesystem snapshot with mandatory parameters
  dellemc_powerstore_nfs:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    nfs_export_name: "{{export_name2}}"
    snapshot: "{{snapshot}}"
    nas_server: "{{nas_server}}"
    path: "{{path2}}"
    state: "present"

- name: Get NFS export details using ID
  dellemc_powerstore_nfs:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    nfs_export_id: "{{export_id}}"
    state: "present"

- name: Add Read-Only and Read-Write hosts to NFS export
  dellemc_powerstore_nfs:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    nfs_export_id: "{{export_id}}"
    read_only_hosts:
      - "{{host5}}"
    read_write_hosts:
      - "{{host6}}"
    host_state: "present-in-export"
    state: "present"

- name: Remove Read-Only and Read-Write hosts from NFS export
  dellemc_powerstore_nfs:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    nfs_export_id: "{{export_id}}"
    read_only_hosts:
      - "{{host1}}"
    read_write_hosts:
      - "{{host3}}"
    host_state: "absent-in-export"
    state: "present"

- name: Modify the attributes of NFS export
  dellemc_powerstore_nfs:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    nfs_export_id: "{{export_id}}"
    description: "modify description"
    default_access: "ROOT"
    state: "present"

- name: Delete NFS export using name
  dellemc_powerstore_nfs:
    array_ip: "{{array_ip}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    nfs_export_name: "{{export_name}}"
    nas_server: "{{nas_server}}"
    state: "absent"
"""

RETURN = r"""
changed:
    description: Whether or not the resource has changed
    returned: always
    type: bool

nfs_export_details:
    description: The NFS export details.
    type: complex
    returned: When NFS export exists.
    contains:
        anonymous_GID:
            description: The group ID of the anonymous account.
            type: int
        anonymous_UID:
            description: The user ID of the anonymous account.
            type: int
        default_access:
            description: Default access level for all hosts that can access
                         the export.
            type: str
        description:
            description: The description for the NFS export.
            type: str
        file_system:
            description: Details of filesystem and NAS server on which NFS
                         export is present.
            type: complex
            contains:
                id:
                    description: The ID of the filesystem.
                    type: str
                name:
                    description: The name of the filesystem.
                    type: str
                filesystem_type:
                    description: The type of the filesystem.
                    type: str
                nas_server:
                    description: Details of NAS server.
                    type: complex
                    contains:
                        id:
                            description: The ID of the NAS server.
                            type: str
                        name:
                            description: The name of the NAS server.
                            type: str
        id:
            description: The ID of the NFS export.
            type: str
        is_no_SUID:
            description: If set, do not allow access to set SUID. Otherwise,
                         allow access.
            type: bool
        min_security:
            description: NFS enforced security type for users accessing an NFS
                         export.
            type: str
        name:
            description: The name of the NFS export.
            type: str
        no_access_hosts:
            description: Hosts with no access to the NFS export.
            type: list
        path:
            description: Local path to a location within the file system.
            type: str
        read_only_hosts:
            description: Hosts with read-only access to the NFS export.
            type: list
        read_only_root_hosts:
            description: Hosts with read-only for root user access to the NFS
                         export.
            type: list
        read_write_hosts:
            description: Hosts with read and write access to the NFS export.
            type: list
        read_write_root_hosts:
            description: Hosts with read and write for root user access to the
                         NFS export.
            type: list
"""

import re
import logging
try:
    import ipaddress
    from ipaddress import ip_network, IPv4Network, IPv6Network
    HAS_IPADDRESS = True
except ImportError:
    HAS_IPADDRESS = False
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import dellemc_ansible_powerstore_utils as utils

LOG = utils.get_logger('dellemc_powerstore_nfs', log_devel=logging.INFO)

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.3.0'


class PowerStoreNfsExport(object):
    """Class with NFS export operations"""

    def __init__(self):
        """Define all the parameters required by this module"""

        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_nfs_export_parameters())

        mutually_exclusive = [['nfs_export_name', 'nfs_export_id'],
                              ['filesystem', 'snapshot'],
                              ['nfs_export_id', 'nas_server'],
                              ['nfs_export_id', 'filesystem'],
                              ['nfs_export_id', 'snapshot'],
                              ['nfs_export_id', 'path']]

        required_one_of = [['nfs_export_name', 'nfs_export_id']]

        # Initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mutually_exclusive,
            required_one_of=required_one_of
        )

        if not HAS_IPADDRESS:
            error_msg = "Please install the ipaddress python library " \
                        "before using NFS Export Ansible module."
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

        LOG.info('HAS_PY4PS = %s , IMPORT_ERROR = %s', HAS_PY4PS,
                 IMPORT_ERROR)

        if not HAS_PY4PS:
            self.module.fail_json(msg=IMPORT_ERROR)

        LOG.info('IS_SUPPORTED_PY4PS_VERSION = %s , VERSION_ERROR = %s',
                 IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR)

        if not IS_SUPPORTED_PY4PS_VERSION:
            self.module.fail_json(msg=VERSION_ERROR)

        self.py4ps_conn = utils.get_powerstore_connection(
            self.module.params, application_type=APPLICATION_TYPE)
        self.provisioning = self.py4ps_conn.provisioning
        LOG.info('Got Py4ps instance for PowerStore')

    def get_nas_server_id(self, nas_server_name=None, nas_server_id=None):
        """Get the id of the NAS server."""

        nas_server_id_or_name = nas_server_id if nas_server_id else \
            nas_server_name
        try:
            if nas_server_name is not None:
                nas_server_details = self.provisioning.get_nas_server_by_name(
                    nas_server_name=nas_server_name)
            else:
                nas_server_details = self.provisioning.get_nas_server_details(
                    nas_server_id=nas_server_id)

            if not nas_server_details:
                self.module.fail_json(msg="Please provide valid NAS server "
                                          "details")

            if isinstance(nas_server_details, list):
                return nas_server_details[0]['id']
            else:
                return nas_server_details['id']

        except Exception as e:
            error_msg = "Failed to get details of NAS server {0} with error" \
                        " {1}".format(nas_server_id_or_name, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def get_fs_id_from_filesystem(self, filesystem, nas_server):
        """Get the id of the filesystem."""

        is_valid_uuid = utils.name_or_id(filesystem)
        try:
            if is_valid_uuid == "NAME":
                # Get the filesystem details using name
                nas_server_id = nas_server
                if nas_server is not None:
                    is_valid_uuid = utils.name_or_id(nas_server)
                    if is_valid_uuid == "ID":
                        nas_server_id = self.get_nas_server_id(
                            nas_server_id=nas_server)
                    else:
                        nas_server_id = self.get_nas_server_id(
                            nas_server_name=nas_server)
                else:
                    error_msg = "Please provide NAS Server details along " \
                                "with filesystem"
                    LOG.error(error_msg)
                    self.module.fail_json(msg=error_msg)

                fs = self.provisioning.get_filesystem_by_name(
                    filesystem_name=filesystem, nas_server_id=nas_server_id)
                if fs:
                    return fs[0]['id']
            else:
                # Get the filesystem details using id
                fs = self.provisioning.get_filesystem_details(filesystem)
                return fs['id']

            error_msg = "Filesystem {0} not found on the array.".format(
                filesystem)
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)
        except Exception as e:
            error_msg = "Failed to get the filesystem {0} by name with " \
                        "error {1}".format(filesystem, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def get_nfs_export(self, nfs_export_name, nfs_export_id, export_parent,
                       nas_server, path):
        """Get NFS export details."""

        name_or_id = nfs_export_name if nfs_export_name else nfs_export_id
        try:
            if nfs_export_id:
                export_details = self.provisioning.\
                    get_nfs_export_details(nfs_export_id)
            else:
                exports_list = self.provisioning.\
                    get_nfs_export_details_by_name(nfs_export_name)

                # Match the NAS server, filesystem/snapshot, path details
                export_details = match_nfs_export(exports_list,
                                                  export_parent, nas_server,
                                                  path)

                if exports_list and not export_details:
                    error_msg = "Entered filesystem/snapshot/nas_server/" \
                                "path do not match with the corresponding " \
                                "NFS Export details. Please provide valid " \
                                "parameters."
                    self.module.fail_json(msg=error_msg)

            # Add the export path
            if export_details:
                nas_details = self.provisioning.get_nas_server_details(
                    export_details['file_system']['nas_server']['id'])
                export_path = \
                    nas_details['file_interfaces'][0]['ip_address'] + ":/" + \
                    export_details['name']
                export_details['export_path'] = export_path
            return export_details

        except Exception as e:
            msg = "Get details of NFS export {0} failed with error {1}". \
                format(name_or_id, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_enum_keys(self, user_input):
        """Get the ENUM key for for user input"""

        try:
            enum_dict = {
                "NO_ACCESS": "No_Access",
                "READ_ONLY": "Read_Only",
                "READ_WRITE": "Read_Write",
                "ROOT": "Root",
                "READ_ONLY_ROOT": "Read_Only_Root",
                "SYS": "Sys",
                "KERBEROS": "Kerberos",
                "KERBEROS_WITH_INTEGRITY": "Kerberos_With_Integrity",
                "KERBEROS_WITH_ENCRYPTION": "Kerberos_With_Encryption"
            }
            return enum_dict[user_input]

        except Exception as e:
            msg = 'Failed to get the enum value for user_input : {0} ' \
                  'with error {1}'.format(user_input, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def delete_nfs_export(self, nfs_export_details):
        """Delete NFS export"""

        msg = "Deleting NFS export with name {0} ".format(
            nfs_export_details['name'])
        LOG.info(msg)

        try:
            self.provisioning.delete_nfs_export(nfs_export_details['id'])
            return True
        except Exception as e:
            errormsg = "Delete operation of NFS export with name: {0}, " \
                       "id: {1} failed with error {2}".\
                format(nfs_export_details['name'], nfs_export_details['id'],
                       str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def create_nfs_export(self, export_parent, nfs_export_name,
                          export_parent_id, path):
        """Create NFS export"""

        if not path:
            self.module.fail_json(msg="Path is required for creation of NFS "
                                      "export.")

        msg = "Creating NFS export with name {0} ".format(nfs_export_name)
        LOG.info(msg)

        optional_param = dict()
        param_list = ['description', 'no_access_hosts', 'read_only_hosts',
                      'read_only_root_hosts', 'read_write_hosts',
                      'read_write_root_hosts']

        if self.module.params['default_access']:
            optional_param['default_access'] = self.get_enum_keys(
                self.module.params['default_access'])

        if self.module.params['min_security']:
            optional_param['min_security'] = self.get_enum_keys(
                self.module.params['min_security'])

        if self.module.params['is_no_suid'] is not None:
            optional_param['is_no_SUID'] = self.module.params['is_no_suid']

        if self.module.params['anonymous_uid'] is not None:
            optional_param['anonymous_UID'] = self.module.params[
                'anonymous_uid']

        if self.module.params['anonymous_gid'] is not None:
            optional_param['anonymous_GID'] = self.module.params[
                'anonymous_gid']

        for param in param_list:
            if self.module.params[param]:
                optional_param[param] = self.module.params[param]

        try:
            self.provisioning.create_nfs_export(
                name=nfs_export_name, file_system_id=export_parent_id,
                path=path, nfs_other_params=optional_param)
            return True
        except Exception as e:
            error_message = 'Failed to create NFS export: {0} for ' \
                            'filesystem {1} with error: {2}'.format(
                                nfs_export_name, export_parent, str(e))
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def create_current_host_dict_playbook(self):
        """Create dict from the playbook host parameters"""

        host_dict = {
            'no_access_hosts': self.module.params['no_access_hosts'],
            'read_only_hosts': self.module.params['read_only_hosts'],
            'read_only_root_hosts': self.module.params[
                'read_only_root_hosts'],
            'read_write_hosts': self.module.params['read_write_hosts'],
            'read_write_root_hosts': self.module.params[
                'read_write_root_hosts']
        }
        return host_dict

    def get_export_hosts(self, host_details):
        """Classify the hosts based on IPv4, IPv6 and FQDN"""
        ipv4_hosts = list()
        ipv6_hosts = list()
        fqdn_hosts = list()

        for host in host_details:
            version = check_ipv4_ipv6_fqdn(host)
            if version == 4:
                ipv4_hosts.append(self.get_ipv4_host(host))
            elif version == 6:
                ipv6_hosts.append(self.get_ipv6_host(host))
            else:
                fqdn_hosts.append(host)

        return ipv4_hosts, ipv6_hosts, fqdn_hosts

    def get_ipv4_host(self, host):
        """Convert the host to IPv4Network"""

        try:
            host = u'{0}'.format(host)
            return IPv4Network(host, strict=False)
        except ValueError as e:
            error_msg = "Given host {0} is an invalid IPv4 format -- " \
                        "error {1}".format(host, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def get_ipv6_host(self, host):
        """Convert the host to IPv6Network"""

        try:
            host = u'{0}'.format(host)
            return IPv6Network(host, strict=False)
        except ValueError as e:
            error_msg = "Given host {0} is an invalid IPv6 format -- " \
                        "error {1}".format(host, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def check_add_hosts(self, export_details):
        """Check if hosts are to be added to NFS export"""

        playbook_host_dict = self.create_current_host_dict_playbook()
        add_host_dict = dict()
        host_type_list = ['no_access_hosts', 'read_only_hosts',
                          'read_write_hosts', 'read_only_root_hosts',
                          'read_write_root_hosts']

        for host_type in host_type_list:
            if playbook_host_dict[host_type]:
                hosts_to_add = list()
                ipv4_hosts, ipv6_hosts, fqdn_hosts = \
                    self.get_export_hosts(export_details[host_type])
                for host in playbook_host_dict[host_type]:
                    version = check_ipv4_ipv6_fqdn(host)

                    # Check if host is FQDN/Netgroup or IP
                    if version:
                        if version == 4:
                            # IPv4 host is provided
                            ipv4_host = self.get_ipv4_host(host)
                            # Check if given host is member of already added
                            # network
                            if ipv4_host not in ipv4_hosts and \
                                    str(ipv4_host) not in hosts_to_add:
                                hosts_to_add.append(str(ipv4_host))
                        else:
                            # IPv6 host is provided
                            ipv6_host = self.get_ipv6_host(host)
                            # Check if given host is member of already added
                            # network
                            if ipv6_host not in ipv6_hosts and \
                                    str(ipv6_host) not in hosts_to_add:
                                hosts_to_add.append(str(ipv6_host))
                    else:
                        # FQDN/Netgroup is provided
                        if host not in fqdn_hosts and \
                                host not in hosts_to_add:
                            hosts_to_add.append(host)
                if hosts_to_add:
                    if host_type == "read_only_root_hosts":
                        export_details[host_type].extend(hosts_to_add)
                        add_host_dict['read_only_root_hosts'] = \
                            export_details[host_type]
                    else:
                        add_host_dict['add_' + host_type] = hosts_to_add

        LOG.info("Host list to add: %s", add_host_dict)
        return add_host_dict

    def check_remove_hosts(self, export_details):
        """Check if hosts are to be removed from NFS export"""

        playbook_host_dict = self.create_current_host_dict_playbook()
        remove_host_dict = dict()
        host_type_list = ['no_access_hosts', 'read_only_hosts',
                          'read_write_hosts', 'read_only_root_hosts',
                          'read_write_root_hosts']

        for host_type in host_type_list:
            if playbook_host_dict[host_type]:
                hosts_to_remove = list()
                ipv4_hosts, ipv6_hosts, fqdn_hosts = \
                    self.get_export_hosts(export_details[host_type])
                for host in playbook_host_dict[host_type]:
                    version = check_ipv4_ipv6_fqdn(host)

                    # Check if host is FQDN/Netgroup or IP
                    if version:
                        if version == 4:
                            # IPv4 host is provided
                            ipv4_host = self.get_ipv4_host(host)
                            # Check if given host is member of already added
                            # network
                            if ipv4_host in ipv4_hosts and \
                                    str(ipv4_host.with_netmask) not in \
                                    hosts_to_remove:
                                hosts_to_remove.append(str(ipv4_host.with_netmask))
                        else:
                            # IPv6 host is provided
                            ipv6_host = self.get_ipv6_host(host)
                            # Check if given host is member of already added
                            # network
                            if ipv6_host in ipv6_hosts and \
                                    str(ipv6_host.with_prefixlen) not in \
                                    hosts_to_remove:
                                hosts_to_remove.append(
                                    str(ipv6_host.with_prefixlen))
                    else:
                        # FQDN/Netgroup is provided
                        if host in fqdn_hosts and host not in hosts_to_remove:
                            hosts_to_remove.append(host)

                if hosts_to_remove:
                    remove_host_dict['remove_' + host_type] = hosts_to_remove

        LOG.info("Host list to remove: %s", remove_host_dict)
        return remove_host_dict

    def check_nfs_export_modified(self, export_details, description,
                                  default_access, min_security, anonymous_uid,
                                  anonymous_gid, is_no_suid):
        """Check if modification is required for NFS export"""

        LOG.info("Checking if modification is required for NFS export")
        modify_param = dict()

        if self.module.params['host_state'] == 'present-in-export':
            modify_param = self.check_add_hosts(export_details)
        elif self.module.params['host_state'] == 'absent-in-export':
            modify_param = self.check_remove_hosts(export_details)

        if (description is not None and export_details['description']
            != description) and \
                ((export_details['description'] is None
                  and description != "") or (export_details['description']
                                             is not None)):
            modify_param['description'] = description

        if default_access:
            access = self.get_enum_keys(default_access)
            if export_details['default_access'] != access:
                modify_param['default_access'] = access

        if min_security:
            security = self.get_enum_keys(min_security)
            if export_details['min_security'] != security:
                modify_param['min_security'] = security

        if anonymous_uid is not None and \
                anonymous_uid != export_details['anonymous_UID']:
            modify_param['anonymous_UID'] = anonymous_uid

        if anonymous_gid is not None and \
                anonymous_gid != export_details['anonymous_GID']:
            modify_param['anonymous_GID'] = anonymous_gid

        if is_no_suid is not None and \
                is_no_suid != export_details['is_no_SUID']:
            modify_param['is_no_SUID'] = is_no_suid

        LOG.info("NFS modification details: %s", modify_param)
        return modify_param

    def modify_nfs_export(self, export_details, nfs_modify_dict):
        """Modify NFS export"""

        LOG.info("Modifying NFS export")

        try:
            self.provisioning.modify_nfs_export(export_details['id'],
                                                nfs_modify_dict)
            return True
        except Exception as e:
            errormsg = "Modify operation of NFS export with name: {0}, " \
                       "id: {1} failed with error {2}".\
                format(export_details['name'], export_details['id'], str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def validate_input(self, export_parent):
        """Validate the input parameters"""

        host_type_list = ['no_access_hosts', 'read_only_hosts',
                          'read_write_hosts', 'read_only_root_hosts',
                          'read_write_root_hosts']

        param_list = ['nfs_export_name', 'filesystem', 'snapshot',
                      'nas_server']

        # Check if sufficient parameters are provided along with
        # nfs_export_name
        if self.module.params['nfs_export_name']:
            if export_parent and (utils.name_or_id(export_parent) == "NAME"
                                  and not self.module.params['nas_server']):
                self.module.fail_json(msg="Please provide NAS server details "
                                          "to uniquely identify NFS export.")
            if not export_parent and not self.module.params['nas_server']:
                self.module.fail_json(msg="Please provide "
                                          "filesystem/snapshot/NAS server "
                                          "details to uniquely identify NFS "
                                          "Export.")

        for param in param_list:
            if self.module.params[param] and len(
                    self.module.params[param].strip()) == 0:
                error_msg = "Please provide valid {0}".format(param)
                self.module.fail_json(msg=error_msg)

        # Check if valid FQDN/IP is provided
        regex = re.compile(r'[a-zA-Z0-9_/.-:@]+$')
        for host_type in host_type_list:
            if self.module.params[host_type]:
                for host in self.module.params[host_type]:
                    if regex.match(host) is None:
                        error_msg = "Along with alphanumeric characters, " \
                                    "only special characters allowed are" \
                                    " ., _, -, /, :, @"
                        self.module.fail_json(msg=error_msg)

        if self.module.params['host_state'] and all(
                self.module.params[host_type] is None for host_type in
                host_type_list):
            error_msg = 'Host state is given but hosts are not specified.'
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

        if not self.module.params['host_state'] and any(
                self.module.params[host_type] is not None for host_type in
                host_type_list):
            error_msg = 'Hosts are given but host state is not specified.'
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

        # Check if valid description is provided
        if self.module.params['description'] is not None:
            if self.module.params['description'].strip() == "":
                self.module.fail_json(msg="Empty description or white spaced"
                                          " description is not allowed. "
                                          "Please enter a valid description")
            if self.module.params['description'] != \
                    self.module.params['description'].strip():
                self.module.fail_json(msg="Description starting or ending "
                                          "with white spaces is not allowed. "
                                          "Please enter a valid description.")

    def perform_module_operation(self):
        """
        Perform different actions on NFS export based on user parameter chosen
        in playbook
        """

        nfs_export_name = self.module.params['nfs_export_name']
        nfs_export_id = self.module.params['nfs_export_id']
        filesystem = self.module.params['filesystem']
        snapshot = self.module.params['snapshot']
        nas_server = self.module.params['nas_server']
        path = self.module.params['path']
        description = self.module.params['description']
        default_access = self.module.params['default_access']
        min_security = self.module.params['min_security']
        anonymous_uid = self.module.params['anonymous_uid']
        anonymous_gid = self.module.params['anonymous_gid']
        is_no_suid = self.module.params['is_no_suid']
        state = self.module.params['state']

        result = dict(
            changed=False,
            nfs_export_details=''
        )

        export_parent = filesystem if filesystem else snapshot
        changed = False
        nfs_modify_dict = dict()

        # Validate the input parameters
        self.validate_input(export_parent)

        # Get the ID of the filesystem/snapshot if name is provided
        export_parent_id = None
        if export_parent is not None:
            export_parent_id = self.get_fs_id_from_filesystem(
                export_parent, nas_server)

        # Get the details of NFS export
        nfs_export_details = self.get_nfs_export(
            nfs_export_name, nfs_export_id, export_parent, nas_server, path)

        # Check if modification to the NFS export is required
        if state == 'present' and nfs_export_details:
            nfs_modify_dict = self.check_nfs_export_modified(
                nfs_export_details, description, default_access, min_security,
                anonymous_uid, anonymous_gid, is_no_suid)

        # Create NFS export
        if state == 'present' and not nfs_export_details:
            if nfs_export_id:
                error_msg = "NFS export with nfs_export_id {0} not found.".\
                    format(nfs_export_id)
                self.module.fail_json(msg=error_msg)

            if nfs_export_name and not export_parent:
                self.module.fail_json(msg="filesystem/snapshot is required to"
                                          " create NFS export.")

            changed = self.create_nfs_export(export_parent, nfs_export_name,
                                             export_parent_id, path)

        # Modify NFS export
        if state == 'present' and nfs_export_details and nfs_modify_dict:
            changed = self.modify_nfs_export(nfs_export_details,
                                             nfs_modify_dict)

        # Delete NFS export
        elif state == 'absent' and nfs_export_details:
            changed = self.delete_nfs_export(nfs_export_details)

        # Finally update the module result!
        result['changed'] = changed
        if state == 'present':
            result['nfs_export_details'] = self.get_nfs_export(
                nfs_export_name, nfs_export_id, export_parent, nas_server,
                path)

        self.module.exit_json(**result)


def match_nfs_export(exports_list, export_parent, nas_server, path):
    """Match the parameters provided in the playbook with the details
    retrieved from the array
    """

    for export in exports_list:
        flag = True
        if (nas_server and not is_nas_server_matched(nas_server, export)) or \
                (export_parent and not is_export_parent_matched(
                    export_parent, export)) or \
                (path and not is_path_matched(path, export)):
            flag = False
        if flag:
            return export
    return False


def is_nas_server_matched(nas_server, nfs_export_details):
    """Match the entered NAS server details with the NAS server details
    retrieved from the array
    """

    nas_id_from_details = \
        nfs_export_details['file_system']['nas_server']['id']
    nas_name_from_details = \
        nfs_export_details['file_system']['nas_server']['name']

    if nfs_export_details and nas_server:
        if utils.name_or_id(nas_server) == "ID" and \
                nas_id_from_details != nas_server:
            return False
        if utils.name_or_id(nas_server) == "NAME" and \
                nas_name_from_details != nas_server:
            return False
    return True


def is_export_parent_matched(export_parent, nfs_export_details):
    """Match the entered filesystem/snapshot details with the
    filesystem/snapshot retrieved from the array
    """

    fs_id_from_details = nfs_export_details['file_system']['id']
    fs_name_from_details = nfs_export_details['file_system']['name']

    if nfs_export_details and export_parent:
        if utils.name_or_id(export_parent) == "ID" and \
                fs_id_from_details != export_parent:
            return False
        if utils.name_or_id(export_parent) == "NAME" and \
                fs_name_from_details != export_parent:
            return False
    return True


def is_path_matched(input_path, nfs_export_details):
    """Match the entered path with the path retrieved from the array"""

    input_path = input_path[:-1] if input_path[-1] == "/" else input_path
    if nfs_export_details['path'] != input_path:
        return False
    return True


def check_ipv4_ipv6_fqdn(val):
    """Determines if the string is IPv4 or IPv6 or FQDN/Netgroup"""

    try:
        val = u'{0}'.format(val)
        ip = ip_network(val, strict=False)
        return ip.version
    except ValueError:
        return 0


def get_powerstore_nfs_export_parameters():
    """This method provides parameters required for the Ansible NFS export
       module on PowerStore"""

    return dict(
        nfs_export_name=dict(), nfs_export_id=dict(), filesystem=dict(),
        snapshot=dict(), nas_server=dict(), path=dict(), description=dict(),
        default_access=dict(choices=['NO_ACCESS', 'READ_ONLY', 'READ_WRITE',
                                     'ROOT', 'READ_ONLY_ROOT']),
        no_access_hosts=dict(type='list', elements='str'),
        read_only_hosts=dict(type='list', elements='str'),
        read_only_root_hosts=dict(type='list', elements='str'),
        read_write_hosts=dict(type='list', elements='str'),
        read_write_root_hosts=dict(type='list', elements='str'),
        min_security=dict(choices=['SYS', 'KERBEROS',
                                   'KERBEROS_WITH_INTEGRITY',
                                   'KERBEROS_WITH_ENCRYPTION']),
        anonymous_uid=dict(type='int'),
        anonymous_gid=dict(type='int'),
        is_no_suid=dict(type='bool'),
        host_state=dict(choices=['present-in-export', 'absent-in-export']),
        state=dict(required=True, choices=['present', 'absent'])
    )


def main():
    """ Create PowerStore NFS export object and perform action on it based on
        user input from playbook"""

    obj = PowerStoreNfsExport()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
