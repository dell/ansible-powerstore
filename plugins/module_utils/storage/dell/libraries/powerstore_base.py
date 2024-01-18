# Copyright: (c) 2024, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

LOG = utils.get_logger('powerstore_base')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']


class PowerStoreBase:

    '''Powerstore Base Class'''

    def __init__(self, ansible_module, ansible_module_params):
        """
        Initialize the powerstore base class
        :param ansible_module: Ansible module class
        :type ansible_module: AnsibleModule
        :param ansible_module_params: Parameters for ansible module class
        :type ansible_module_params: dict
        """
        self.module_params = utils.get_powerstore_management_host_parameters()
        ansible_module_params['argument_spec'].update(self.module_params)

        # Initialize the ansible module
        self.module = ansible_module(
            **ansible_module_params
        )

        self.result = {"changed": False}

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
        self.provisioning = self.conn.provisioning

        msg = 'Got Py4ps instance for configuration {0} and protection {1}' \
              ' on PowerStore'.format(self.configuration, self.protection)
        LOG.info(msg)

        check_mode_msg = f'Check mode flag is {self.module.check_mode}'
        LOG.info(check_mode_msg)
