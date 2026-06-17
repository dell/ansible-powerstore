#!/usr/bin/python
# Copyright: (c) 2024, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module for managing Recycle Bin on PowerStore"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: recycle_bin
version_added: '3.9.0'

short_description: Manage Recycle Bin on PowerStore storage systems

description:
- Manage Recycle Bin on PowerStore storage systems includes configuring
  the recycle bin expiration duration, recovering deleted volumes and
  volume groups from the recycle bin, permanently deleting items from
  the recycle bin, and emptying the entire recycle bin.
- This module supports check mode and diff mode.

extends_documentation_fragment:
  - dellemc.powerstore.powerstore

author:
- Saksham Nautiyal (@saksham-nautiyal) <ansible.team@dell.com>

options:
  recycle_bin_id:
    description:
    - The unique identifier of the recycle bin item.
    - Required for recover and delete operations.
    - Mutually exclusive with I(resource_name).
    type: str
  resource_name:
    description:
    - The name of the deleted resource in the recycle bin.
    - Used as an alternative to I(recycle_bin_id) for identifying items.
    - Mutually exclusive with I(recycle_bin_id).
    type: str
  resource_type:
    description:
    - The type of resource to filter when using I(resource_name).
    - Used to disambiguate when multiple items share the same name.
    type: str
    choices: ['volume', 'volume_group']
  expiration_duration:
    description:
    - Duration in days for items to remain in the recycle bin before
      automatic permanent deletion.
    - Valid range is 0 to 30 days. A value of 0 means items expire
      immediately.
    - Used only with I(state=present) to configure the recycle bin
      retention policy.
    type: int
  empty_recycle_bin:
    description:
    - When set to C(true) and I(state=absent), empties the entire
      recycle bin by permanently deleting all items.
    - Cannot be used together with I(recycle_bin_id) or I(resource_name).
    type: bool
    default: false
  state:
    description:
    - Define the operation to perform on the recycle bin.
    - C(present) with I(expiration_duration) configures the retention
      policy.
    - C(present) with I(recycle_bin_id) or I(resource_name) recovers
      items from the recycle bin.
    - C(absent) with I(recycle_bin_id) or I(resource_name) permanently
      deletes items from the recycle bin.
    - C(absent) with I(empty_recycle_bin=true) empties the entire
      recycle bin.
    choices: ['absent', 'present']
    required: true
    type: str
notes:
- The I(check_mode) is supported.
- The I(diff) mode is supported.
- Recycle Bin feature requires PowerStore version 3.5.0.0 or later.
'''

EXAMPLES = r'''
- name: Get recycle bin configuration
  dellemc.powerstore.recycle_bin:
    array_ip: "{{ array_ip }}"
    user: "{{ user }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    state: "present"

- name: Configure recycle bin expiration to 14 days
  dellemc.powerstore.recycle_bin:
    array_ip: "{{ array_ip }}"
    user: "{{ user }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    expiration_duration: 14
    state: "present"

- name: Recover a volume from recycle bin by ID
  dellemc.powerstore.recycle_bin:
    array_ip: "{{ array_ip }}"
    user: "{{ user }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    recycle_bin_id: "e0684b39-0029-4be2-b5bf-67b8c145e1b8"
    state: "present"

- name: Recover a volume from recycle bin by name
  dellemc.powerstore.recycle_bin:
    array_ip: "{{ array_ip }}"
    user: "{{ user }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    resource_name: "my_volume"
    resource_type: "volume"
    state: "present"

- name: Permanently delete a specific item from recycle bin
  dellemc.powerstore.recycle_bin:
    array_ip: "{{ array_ip }}"
    user: "{{ user }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    recycle_bin_id: "e0684b39-0029-4be2-b5bf-67b8c145e1b8"
    state: "absent"

- name: Empty the entire recycle bin
  dellemc.powerstore.recycle_bin:
    array_ip: "{{ array_ip }}"
    user: "{{ user }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    empty_recycle_bin: true
    state: "absent"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "true"
recycle_bin_config:
    description: Details of the recycle bin configuration.
    returned: When I(expiration_duration) is provided or no item
              operation is performed.
    type: complex
    contains:
        id:
            description: Unique identifier for recycle bin configuration
                         (always "0").
            type: str
        expiration_duration:
            description: Duration in days for items to remain in the
                         recycle bin.
            type: int
    sample: {
        "id": "0",
        "expiration_duration": 7
    }
recycle_bin_items:
    description: List of items currently in the recycle bin.
    returned: When getting recycle bin details without specific item
              operations.
    type: list
    contains:
        id:
            description: Unique identifier of the recycle bin item.
            type: str
        name:
            description: Name of the deleted resource.
            type: str
        resource_type:
            description: Type of resource (volume or volume_group).
            type: str
        logical_provisioned:
            description: Provisioned size of the object in bytes.
            type: int
        logical_used:
            description: Logical space used by the object in bytes.
            type: int
        appliance_id:
            description: The appliance where the resource is located.
            type: str
        deletion_timestamp:
            description: Time when the object was moved to the recycle
                         bin.
            type: str
        expiration_timestamp:
            description: Time when the object will be auto-purged.
            type: str
    sample: [{
        "id": "e0684b39-0029-4be2-b5bf-67b8c145e1b8",
        "name": "test_volume",
        "resource_type": "volume",
        "logical_provisioned": 1073741824,
        "logical_used": 0,
        "appliance_id": "A1",
        "deletion_timestamp": "2024-01-01T00:00:00.000+00:00",
        "expiration_timestamp": "2024-01-08T00:00:00.000+00:00"
    }]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import utils

LOG = utils.get_logger('recycle_bin')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# REST API URL templates
RECYCLE_BIN_CONFIG_URL = 'https://{0}/api/rest/recycle_bin_config/0'
RECYCLE_BIN_LIST_URL = 'https://{0}/api/rest/recycle_bin'
RECYCLE_BIN_ITEM_URL = 'https://{0}/api/rest/recycle_bin/{1}'
RECYCLE_BIN_RECOVER_URL = 'https://{0}/api/rest/recycle_bin/{1}/recover'
RECYCLE_BIN_EMPTY_URL = 'https://{0}/api/rest/recycle_bin/empty'


class PowerStoreRecycleBin(object):
    """Recycle Bin operations"""

    def __init__(self):
        """Define all parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_recycle_bin_parameters())

        mutually_exclusive = [['recycle_bin_id', 'resource_name'],
                              ['recycle_bin_id', 'empty_recycle_bin'],
                              ['resource_name', 'empty_recycle_bin']]

        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True,
            mutually_exclusive=mutually_exclusive
        )

        msg = 'HAS_PY4PS = {0} , IMPORT_ERROR = {1}'.format(
            HAS_PY4PS, IMPORT_ERROR)
        LOG.info(msg)
        if HAS_PY4PS is False:
            self.module.fail_json(msg=IMPORT_ERROR)

        msg = 'IS_SUPPORTED_PY4PS_VERSION = {0} , VERSION_ERROR = {1}'.format(
            IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR)
        LOG.info(msg)
        if IS_SUPPORTED_PY4PS_VERSION is False:
            self.module.fail_json(msg=VERSION_ERROR)

        self.conn = utils.get_powerstore_connection(self.module.params)
        self.provisioning = self.conn.provisioning
        LOG.info('Got Py4ps instance for provisioning on PowerStore %s',
                 self.provisioning)

    def _api_request(self, method, url, payload=None, querystring=None):
        """Make a REST API request using the SDK client."""
        return self.provisioning.client.request(
            method, url, payload=payload, querystring=querystring)

    def get_recycle_bin_config(self):
        """Get the recycle bin configuration."""
        try:
            LOG.info("Getting recycle bin configuration.")
            url = RECYCLE_BIN_CONFIG_URL.format(self.provisioning.server_ip)
            resp = self._api_request('GET', url,
                                     querystring={'select': '*'})
            LOG.info("Recycle bin config: %s", resp)
            return resp
        except Exception as e:
            msg = "Failed to get recycle bin configuration with " \
                  "error {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_recycle_bin_items(self):
        """Get all items in the recycle bin."""
        try:
            LOG.info("Getting recycle bin items.")
            url = RECYCLE_BIN_LIST_URL.format(self.provisioning.server_ip)
            resp = self._api_request('GET', url,
                                     querystring={'select': '*'})
            if resp is None:
                resp = []
            LOG.info("Recycle bin items count: %s", len(resp))
            return resp
        except Exception as e:
            msg = "Failed to get recycle bin items with " \
                  "error {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_recycle_bin_item(self, item_id):
        """Get a specific recycle bin item by ID."""
        try:
            LOG.info("Getting recycle bin item with ID: %s", item_id)
            url = RECYCLE_BIN_ITEM_URL.format(
                self.provisioning.server_ip, item_id)
            resp = self._api_request('GET', url,
                                     querystring={'select': '*'})
            LOG.info("Recycle bin item: %s", resp)
            return resp
        except Exception as e:
            msg = "Failed to get recycle bin item {0} with " \
                  "error {1}".format(item_id, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_recycle_bin_item_by_name(self, name, resource_type=None):
        """Find a recycle bin item by name and optional resource type."""
        try:
            LOG.info("Getting recycle bin item by name: %s, type: %s",
                     name, resource_type)
            items = self.get_recycle_bin_items()
            matches = []
            for item in items:
                if item.get('name') == name:
                    if resource_type is None or \
                            item.get('resource_type') == resource_type:
                        matches.append(item)
            if len(matches) == 1:
                return matches[0]
            elif len(matches) > 1:
                msg = "Multiple recycle bin items found with name '{0}'. " \
                      "Please specify resource_type to narrow the " \
                      "search or use recycle_bin_id.".format(name)
                self.module.fail_json(msg=msg)
            return None
        except Exception as e:
            if hasattr(e, 'args') and e.args:
                raise
            msg = "Failed to find recycle bin item by name {0} with " \
                  "error {1}".format(name, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def modify_recycle_bin_config(self, expiration_duration):
        """Modify the recycle bin configuration."""
        try:
            LOG.info("Modifying recycle bin config: expiration_duration=%s",
                     expiration_duration)
            url = RECYCLE_BIN_CONFIG_URL.format(self.provisioning.server_ip)
            self._api_request('PATCH', url,
                              payload={'expiration_duration':
                                       expiration_duration})
            return True
        except Exception as e:
            msg = "Failed to modify recycle bin configuration with " \
                  "error {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def recover_recycle_bin_item(self, item_id):
        """Recover an item from the recycle bin."""
        try:
            LOG.info("Recovering recycle bin item: %s", item_id)
            url = RECYCLE_BIN_RECOVER_URL.format(
                self.provisioning.server_ip, item_id)
            self._api_request('POST', url, payload={})
            return True
        except Exception as e:
            msg = "Failed to recover recycle bin item {0} with " \
                  "error {1}".format(item_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def delete_recycle_bin_item(self, item_id):
        """Permanently delete an item from the recycle bin."""
        try:
            LOG.info("Deleting recycle bin item: %s", item_id)
            url = RECYCLE_BIN_ITEM_URL.format(
                self.provisioning.server_ip, item_id)
            self._api_request('DELETE', url)
            return True
        except Exception as e:
            msg = "Failed to delete recycle bin item {0} with " \
                  "error {1}".format(item_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def empty_recycle_bin(self):
        """Empty the entire recycle bin."""
        try:
            LOG.info("Emptying recycle bin.")
            url = RECYCLE_BIN_EMPTY_URL.format(self.provisioning.server_ip)
            self._api_request('POST', url, payload={})
            return True
        except Exception as e:
            msg = "Failed to empty recycle bin with " \
                  "error {0}".format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def _resolve_item(self):
        """Resolve recycle bin item from ID or name parameters."""
        recycle_bin_id = self.module.params.get('recycle_bin_id')
        resource_name = self.module.params.get('resource_name')
        resource_type = self.module.params.get('resource_type')

        if recycle_bin_id:
            return self.get_recycle_bin_item(recycle_bin_id)
        elif resource_name:
            return self.get_recycle_bin_item_by_name(
                resource_name, resource_type)
        return None

    def _validate_params(self):
        """Validate module parameters."""
        expiration_duration = self.module.params.get('expiration_duration')
        if expiration_duration is not None and \
                isinstance(expiration_duration, int):
            if expiration_duration < 0 or expiration_duration > 30:
                self.module.fail_json(
                    msg="expiration_duration must be between 0 and 30 days. "
                        "Got {0}.".format(expiration_duration))

    def _handle_present_state(self, result, diff):
        """Handle present state operations."""
        recycle_bin_id = self.module.params.get('recycle_bin_id')
        resource_name = self.module.params.get('resource_name')
        expiration_duration = self.module.params.get('expiration_duration')

        if expiration_duration is not None:
            self._handle_configure(result, diff, expiration_duration)
        elif recycle_bin_id or resource_name:
            self._handle_recover(result, diff)
        else:
            result['recycle_bin_config'] = self.get_recycle_bin_config()
            result['recycle_bin_items'] = self.get_recycle_bin_items()

    def _handle_configure(self, result, diff, expiration_duration):
        """Configure recycle bin expiration duration."""
        current_config = self.get_recycle_bin_config()
        if current_config and \
                current_config.get('expiration_duration') != \
                expiration_duration:
            diff['before'] = {
                'expiration_duration':
                    current_config.get('expiration_duration')}
            diff['after'] = {
                'expiration_duration': expiration_duration}
            if not self.module.check_mode:
                self.modify_recycle_bin_config(expiration_duration)
            result['changed'] = True

        if not self.module.check_mode:
            result['recycle_bin_config'] = \
                self.get_recycle_bin_config()
        else:
            result['recycle_bin_config'] = current_config

    def _handle_recover(self, result, diff):
        """Recover item from recycle bin."""
        item = self._resolve_item()
        if item:
            diff['before'] = {'state': 'in_recycle_bin',
                              'id': item.get('id'),
                              'name': item.get('name')}
            diff['after'] = {'state': 'recovered',
                             'id': item.get('id'),
                             'name': item.get('name')}
            if not self.module.check_mode:
                self.recover_recycle_bin_item(item['id'])
            result['changed'] = True

    def _handle_absent_state(self, result, diff):
        """Handle absent state operations."""
        recycle_bin_id = self.module.params.get('recycle_bin_id')
        resource_name = self.module.params.get('resource_name')
        empty_rb = self.module.params.get('empty_recycle_bin')

        if empty_rb:
            self._handle_empty(result, diff)
        elif recycle_bin_id or resource_name:
            self._handle_delete(result, diff)
        else:
            self.module.fail_json(
                msg="state is absent but none of the following are "
                    "set: recycle_bin_id, resource_name, "
                    "empty_recycle_bin")

    def _handle_empty(self, result, diff):
        """Empty entire recycle bin."""
        items = self.get_recycle_bin_items()
        if items:
            diff['before'] = {'items_count': len(items)}
            diff['after'] = {'items_count': 0}
            if not self.module.check_mode:
                self.empty_recycle_bin()
            result['changed'] = True

    def _handle_delete(self, result, diff):
        """Permanently delete specific item from recycle bin."""
        item = self._resolve_item()
        if item:
            diff['before'] = {'state': 'in_recycle_bin',
                              'id': item.get('id'),
                              'name': item.get('name')}
            diff['after'] = {'state': 'permanently_deleted',
                             'id': item.get('id'),
                             'name': item.get('name')}
            if not self.module.check_mode:
                self.delete_recycle_bin_item(item['id'])
            result['changed'] = True

    def perform_module_operation(self):
        """Perform recycle bin operations based on parameters."""

        state = self.module.params['state']
        self._validate_params()

        result = dict(
            changed=False,
            recycle_bin_config=None,
            recycle_bin_items=None
        )
        diff = dict(before={}, after={})

        if state == 'present':
            self._handle_present_state(result, diff)
        elif state == 'absent':
            self._handle_absent_state(result, diff)

        if self.module._diff:
            result['diff'] = diff

        self.module.exit_json(**result)


def get_powerstore_recycle_bin_parameters():
    """Provide the parameters required for the recycle bin module."""
    return dict(
        recycle_bin_id=dict(required=False, type='str'),
        resource_name=dict(required=False, type='str'),
        resource_type=dict(required=False, type='str',
                           choices=['volume', 'volume_group']),
        expiration_duration=dict(required=False, type='int'),
        empty_recycle_bin=dict(required=False, type='bool', default=False),
        state=dict(required=True, type='str',
                   choices=['present', 'absent'])
    )


def main():
    """Create PowerStore Recycle Bin object and perform action on it
       based on user input from playbook."""
    obj = PowerStoreRecycleBin()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
