# Copyright: (c) 2021, DellEMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Email module on PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_email_api import MockEmailApi
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
from ansible_collections.dellemc.powerstore.plugins.modules.email import PowerstoreEmail


class TestPowerstoreEmail():

    get_module_args = MockEmailApi.EMAIL_COMMON_ARGS

    @pytest.fixture
    def email_module_mock(self, mocker):
        mocker.patch(MockEmailApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        email_module_mock = PowerstoreEmail()
        email_module_mock.module = MagicMock()
        return email_module_mock

    def test_get_email_response(self, email_module_mock):
        self.get_module_args.update({
            'email_id': "780b6220-2d0b-4b9f-a485-4ae7f673bd98",
            'state': "present"
        })
        email_module_mock.module.params = self.get_module_args
        email_module_mock.perform_module_operation()
        email_module_mock.configuration.get_destination_email_details.assert_called()

    def test_get_email_response_with_address(self, email_module_mock):
        self.get_module_args.update({
            'email_address': MockEmailApi.EMAIL_ADDRESS_1,
            'state': "present"
        })
        email_module_mock.module.params = self.get_module_args
        email_module_mock.perform_module_operation()
        email_module_mock.configuration.get_destination_email_by_address.assert_called()

    def test_create_email(self, email_module_mock):
        self.get_module_args.update({'email_address': MockEmailApi.EMAIL_ADDRESS_1,
                                     'notify': {'critical': True, 'major': True},
                                     'state': "present"})
        email_module_mock.module.params = self.get_module_args
        email_module_mock.get_email_details = MagicMock(return_value=None)
        email_module_mock.configuration.get_destination_email_details = MagicMock(
            return_value=MockSDKResponse(MockEmailApi.CREATE_EMAIL))
        email_module_mock.perform_module_operation()
        assert email_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_email(self, email_module_mock):
        self.get_module_args.update({'email_address': MockEmailApi.EMAIL_ADDRESS_1,
                                     'new_address': "def_xyz@dell.com",
                                     'notify': {'info': False},
                                     'state': "present"})
        email_module_mock.module.params = self.get_module_args
        email_module_mock.get_email_details = MagicMock(return_value=None)
        email_module_mock.configuration.get_destination_email_details = MagicMock(
            return_value=MockEmailApi.EMAIL_DETAILS)
        email_module_mock.perform_module_operation()
        assert email_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_send_test_email(self, email_module_mock):
        self.get_module_args.update({
            'email_address': MockEmailApi.EMAIL_ADDRESS_1,
            'send_test_email': True,
            'state': "present"
        })
        email_module_mock.module.params = self.get_module_args
        email_module_mock.perform_module_operation()
        email_module_mock.configuration.test_destination_email.assert_called()

    def test_delete_email(self, email_module_mock):
        self.get_module_args.update({
            'email_address': MockEmailApi.EMAIL_ADDRESS_1,
            'state': "absent"
        })
        email_module_mock.module.params = self.get_module_args
        email_module_mock.perform_module_operation()
        email_module_mock.configuration.delete_destination_email.assert_called()
