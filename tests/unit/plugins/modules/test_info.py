# Copyright: (c) 2021, DellEMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for info module on PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_info_api import MockInfoApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKResponse
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import dellemc_ansible_powerstore_utils as utils

utils.get_logger = MagicMock()
utils.get_powerstore_connection = MagicMock()
utils.PowerStoreException = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerstore.plugins.modules.info import PowerstoreInfo


class TestPowerstoreInfo():

    get_module_args = MockInfoApi.INFO_COMMON_ARGS

    @pytest.fixture
    def info_module_mock(self, mocker):
        mocker.patch(MockInfoApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        info_module_mock = PowerstoreInfo()
        return info_module_mock

    def test_get_security_config_response(self, info_module_mock):
        MockInfoApi.get_security_config_response('api')
        self.get_module_args.update({
            'gather_subset': ['security_config'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_security_configs.assert_called()

    def test_get_certificate_response(self, info_module_mock):
        MockInfoApi.get_certificate_response('api')
        self.get_module_args.update({
            'gather_subset': ['certificate'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_certificates.assert_called()

    def test_get_ad_response(self, info_module_mock):
        MockInfoApi.get_certificate_response('api')
        self.get_module_args.update({
            'gather_subset': ['ad'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.provisioning.get_file_ads.assert_called()

    def test_get_ldap_response(self, info_module_mock):
        MockInfoApi.get_certificate_response('api')
        self.get_module_args.update({
            'gather_subset': ['ldap'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.provisioning.get_file_ldaps.assert_called()
