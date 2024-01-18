# Copyright: (c) 2024, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

LOG = utils.get_logger('configuration')

# Application type
APPLICATION_TYPE = 'Ansible/3.1.0'


class ConfigurationSDK:

    """
    The configuration sdk class with shared configuration operations.
    """

    def __init__(self, configuration, module):
        """
        Initialize the configuration class
        :param configuration: The configuration sdk instance
        :param module: Ansible module object
        """
        self.configuration = configuration
        self.module = module

    def get_appliance_details(self, appliance_id=None, appliance_name=None):
        """
        Get the details of Appliance of a given Powerstore storage system.

        Args:
            appliance_id (str): The ID of the appliance.
            appliance_name (str): The name of the appliance.
        Returns:
            dict: The details of the appliance.
        Raises:
            Exception: If an error occurs while getting the appliance details.
        """

        try:
            # Log the appliance details being retrieved
            log_msg = f"Getting Appliance details id: {appliance_id} or " \
                      f"name {appliance_name}"
            LOG.info(log_msg)

            # Get appliance details based on the provided ID or name
            if appliance_name:
                appliance_details = self.configuration.get_appliance_by_name(
                    appliance_name=appliance_name)
                if appliance_details:
                    appliance_details = appliance_details[0]
            else:
                appliance_details = self.configuration.get_appliance_details(
                    appliance_id=appliance_id)

            # Log the retrieved appliance details
            if appliance_details:
                log_msg = f"Successfully got Appliance details" \
                          f" {appliance_details}"
                LOG.info(log_msg)
            return appliance_details

        except Exception as e:
            # Set error message if an exception occurs
            msg = f"Get Appliance with id {appliance_id} or name" \
                  f" {appliance_name} failed with error {str(e)}"
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))
