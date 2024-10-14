#!/usr/bin/python
# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module for managing Service Config on PowerStore"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: service_config
version_added: '3.1.0'

short_description: Manage Service config on PowerStore storage systems

description:
- Manage Service config on PowerStore storage systems includes
  retrieving, and updating Service config.

extends_documentation_fragment:
  - dellemc.powerstore.powerstore

author:
- Bhavneet Sharma(@Bhavneet-Sharma) <ansible.team@dell.com>

options:
  service_config:
    description:
    - Specifies the appliance details on which ssh will be enabled/disabled.
    type: list
    elements: dict
    suboptions:
      appliance_name:
        description:
        - Specifies the name of the appliance.
        - Mutually exclusive with appliance_id.
        type: str
      appliance_id:
        description:
        - Specifies the appliance id.
        - Mutually exclusive with appliance_name.
        type: str
      is_ssh_enabled:
        description:
        - Whether ssh will be enabled/disabled on specified appliance.
        type: bool
        required: true
notes:
- The I(check_mode) is supported.
'''

EXAMPLES = r'''
- name: Get Service config
  dellemc.powerstore.service_config:
    array_ip: "{{ array_ip }}"
    user: "{{ user }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"

- name: Update Service config
  dellemc.powerstore.service_config:
    array_ip: "{{ array_ip }}"
    user: "{{ user }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    service_config:
      - appliance_name: "{{ appliance_name }}"
        is_ssh_enabled: true
      - appliance_id: "A2"
        is_ssh_enabled: true
'''

RETURN = r'''
changed:
    description: A Boolean value indicating if task had to make changes.
    returned: always
    type: bool
    sample: "true"
service_configs_details:
    description: The details of Service configurations.
    returned: always
    type: list
    contains:
        id:
            description: Unique identifier of the service configuration.
            type: str
        appliance_name:
            description: Name of the appliance.
            type: str
        appliance_id:
            description: Unique identifier of the appliance.
            type: str
        is_ssh_enabled:
            description: Whether the SSH will be enabled/disabled.
            type: bool
    sample: [{
        "id": "A1",
        "appliance_name": "Appliance-1",
        "appliance_id": "A1",
        "is_ssh_enabled": false
    }]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.libraries.powerstore_base \
    import PowerStoreBase
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.libraries.configuration \
    import ConfigurationSDK
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

LOG = utils.get_logger('service_config')


class ServiceConfigs(PowerStoreBase):

    """Service configurations operations."""

    def __init__(self):
        """Define all parameters for this module."""

        ansible_module_params = {
            'argument_spec': self.get_service_configs_parameters(),
            'supports_check_mode': True
        }

        super().__init__(AnsibleModule, ansible_module_params)

        self.result = {
            "changed": False,
            "service_configs_details": []
        }

    def update_appliance_details(self, configs_details):
        """Update appliance details in service config."""
        updated_details = []
        for config in configs_details:
            if config.get('appliance_id'):
                appliance_details = ConfigurationSDK(self.configuration,
                                                     self.module).\
                    get_appliance_details(appliance_id=config['appliance_id'])
                config['appliance_name'] = appliance_details.get('name')
            updated_details.append(config)

        return updated_details

    def get_service_configs(self):
        """
        Get Service config.
        returns: Details of Service config
        rtype: dict
        """
        updated_details = []
        try:
            LOG.info("Getting Service configs.")
            configs_details = self.configuration.get_service_configs()
            if configs_details:
                updated_details = self.update_appliance_details(configs_details)
                return updated_details
        except Exception as e:
            msg = f"Failed to get the service configs with error {str(e)}"
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def get_service_configs_parameters(self):
        """
        Returns a dictionary containing the Service config parameters.
        :rtype: dict
        """
        return dict(
            service_config=dict(
                type='list', elements='dict', options=dict(
                    appliance_name=dict(type='str'),
                    appliance_id=dict(type='str'),
                    is_ssh_enabled=dict(type='bool', required=True))))

    def is_app_exists(self, access, configs):
        """Check if an appliance exists in the config details."""
        value1 = access.get('appliance_id')
        value2 = access.get('appliance_name')
        msg = f"Appliance id: {value1} or name: {value2} not found. Specify " \
              f"valid appliance_id or appliance_name."
        if (value1 and not any(value1 in dict_item.values() for dict_item in configs)) or \
                (value2 and not any(value2 in dict_item.values() for dict_item in configs)):
            self.module.fail_json(msg=msg)

    def update_ssh(self, access, configs):
        """Update SSH access for an appliance
        :param access: Service details of an appliance.
        :type access: dict
        :param configs: Service configurations details.
        :type configs: list
        :rtype: bool
        """
        try:
            LOG.info("Updating SSH Service of an appliance.")
            app_id = access.get('appliance_id')
            app_name = access.get('appliance_name')
            is_ssh = access.get('is_ssh_enabled')

            for config in configs:
                if (config.get('appliance_id') == app_id or config.get('appliance_name') == app_name) and \
                        config.get('is_ssh_enabled') != is_ssh:
                    if not self.module.check_mode:
                        self.configuration.modify_service_config(
                            service_config_id=config['appliance_id'],
                            is_ssh_enabled=is_ssh)
                    return True
                # Mentioned appliance not found in config details
            self.is_app_exists(access, configs)
            return False
        except Exception as e:
            msg = f"Failed to update the service config with error: {str(e)}"
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def update_service_config(self, config_params, configs_details):
        """Update Service config.
        :param config_params: Params passed by playbook.
        :param configs_details: service config details
        :rtype: bool
        """
        ssh_access = config_params.get('service_config')
        ssh_enabled = False

        LOG.info("Modifying Service configs.")
        if ssh_access:
            for access in ssh_access:
                ssh_enabled = self.update_ssh(access, configs_details)
        return ssh_enabled

    def is_param_empty(self, app_name=None, app_id=None):
        """Check if a parameter is empty.
        :param param_name: Appliance name.
        :type app_name: str
        :param app_id: Appliance id.
        :type param_value: str
        :rtype: None
        """
        # Check for empty appliance name
        if app_name and utils.is_param_empty(app_name):
            err_msg = "Provide valid value of appliance_name."
            self.module.fail_json(msg=err_msg)

        # Check for empty appliance id
        if app_id and utils.is_param_empty(app_id):
            err_msg = "Provide valid value of appliance_id."
            self.module.fail_json(msg=err_msg)

    def validate_service_config_params(self, module_params):
        """Validate Service parameters.
        :param module_params: Service config parameters.
        :type module_params: dict
        :rtype: bool
        """
        ssh_access = module_params.get('service_config')
        if ssh_access:
            for access in ssh_access:
                app_id = access.get('appliance_id')
                app_name = access.get('appliance_name')

                # check for mutually exclusive parameters
                if app_name and app_id:
                    err_msg = "parameters are mutually exclusive: " \
                              "appliance_name|appliance_id."
                    self.module.fail_json(msg=err_msg)

                # Check for required parameters
                if not app_name and not app_id:
                    err_msg = "one of the following is required: " \
                              "appliance_name, appliance_id."
                    self.module.fail_json(msg=err_msg)

                self.is_param_empty(app_name=app_name, app_id=app_id)


class ServiceConfigsExitHandler:
    def handle(self, config_obj):
        config_obj.result['service_configs_details'] = config_obj.get_service_configs()
        config_obj.module.exit_json(**config_obj.result)


class ServiceConfigsUpdateHandler:
    def handle(self, config_obj, module_params, configs_details):
        config_obj.validate_service_config_params(module_params)

        changed = config_obj.update_service_config(
            config_params=module_params,
            configs_details=configs_details)
        config_obj.result['changed'] = changed
        ServiceConfigsExitHandler().handle(config_obj)


class ServiceConfigsHandler:
    def handle(self, config_obj, module_params):
        service_configs_details = config_obj.get_service_configs()
        ServiceConfigsUpdateHandler().handle(
            config_obj=config_obj, module_params=module_params,
            configs_details=service_configs_details)


def main():
    """ Create the PowerStore Service config object and perform
    action on it based on the user input from playbook.
    """
    obj = ServiceConfigs()
    ServiceConfigsHandler().handle(obj, obj.module.params)


if __name__ == '__main__':
    main()
