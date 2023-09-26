# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for remote support contact module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.shared_library import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_remote_support_contact_api \
    import MockRemoteSupportContactApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.remote_support_contact \
    import PowerstoreRemoteSupportContact


class TestPowerstoreRemoteSupportContact():

    get_module_args = MockRemoteSupportContactApi.REMOTE_SUPPORT_CONTACT_COMMON_ARGS

    @pytest.fixture
    def remote_support_contact_module_mock(self, mocker):
        mocker.patch(MockRemoteSupportContactApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        remote_support_contact_module_mock = PowerstoreRemoteSupportContact()
        remote_support_contact_module_mock.module = MagicMock()
        return remote_support_contact_module_mock

    def test_get_remote_support_contact_response(self, remote_support_contact_module_mock):
        self.get_module_args.update({
            'contact_id': 0,
            'state': "present"
        })
        remote_support_contact_module_mock.module.params = self.get_module_args
        remote_support_contact_module_mock.configuration.get_remote_support_contact_details = MagicMock(
            return_value=MockRemoteSupportContactApi.REMOTE_SUPPORT_CONTACT_DETAILS)
        remote_support_contact_module_mock.perform_module_operation()
        assert self.get_module_args['contact_id'] == int(remote_support_contact_module_mock.
                                                         module.exit_json.call_args[1]['remote_support_contact_details']['id'])
        remote_support_contact_module_mock.configuration.get_remote_support_contact_details.assert_called()

    def test_modify_remote_support_contact_details(self, remote_support_contact_module_mock):
        self.get_module_args.update({'contact_id': 0,
                                     'first_name': "abc",
                                     'source_email': "remote_support@dell.com",
                                     'state': "present"})
        remote_support_contact_module_mock.module.params = self.get_module_args
        remote_support_contact_module_mock.configuration.get_remote_support_contact_details = MagicMock(
            return_value=MockRemoteSupportContactApi.REMOTE_SUPPORT_CONTACT_DETAILS)
        remote_support_contact_module_mock.perform_module_operation()
        assert self.get_module_args['contact_id'] == int(remote_support_contact_module_mock.module.
                                                         exit_json.call_args[1]['remote_support_contact_details']['id'])
        remote_support_contact_module_mock.configuration.modify_remote_support_contact_details.assert_called()

    def test_get_non_existing_remote_support_contact_details(self, remote_support_contact_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        invalid_contact_id = 2
        self.get_module_args.update({
            'contact_id': invalid_contact_id,
            'state': "present"
        })
        remote_support_contact_module_mock.module.params = self.get_module_args
        remote_support_contact_module_mock.configuration.get_remote_support_contact_details = MagicMock(
            side_effect=MockApiException)
        remote_support_contact_module_mock.perform_module_operation()
        assert MockRemoteSupportContactApi.get_remote_support_contact_failed_msg() in \
            remote_support_contact_module_mock.module.fail_json.call_args[1]['msg']

    def test_delete_remote_support_contact(self, remote_support_contact_module_mock):
        contact_id = 0
        self.get_module_args.update({'contact_id': contact_id,
                                     'state': "absent"})
        remote_support_contact_module_mock.module.params = self.get_module_args
        remote_support_contact_module_mock.configuration.get_remote_support_contact_details = MagicMock(
            return_value=MockRemoteSupportContactApi.REMOTE_SUPPORT_CONTACT_DETAILS)
        remote_support_contact_module_mock.perform_module_operation()
        assert MockRemoteSupportContactApi.delete_remote_support_contact_failed_msg() in \
            remote_support_contact_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_invalid_first_name(self, remote_support_contact_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        contact_id = 0
        invalid_first_name = "This_is_the_first_name_and_contains_more_than_one_hundred_and_twenty_eight_characters_making_this_first_name_to_be_an_invalid_one"
        self.get_module_args.update({'contact_id': contact_id,
                                     'first_name': invalid_first_name,
                                     'state': "present"})
        remote_support_contact_module_mock.module.params = self.get_module_args
        remote_support_contact_module_mock.configuration.get_remote_support_contact_details = MagicMock(
            return_value=MockRemoteSupportContactApi.REMOTE_SUPPORT_CONTACT_DETAILS)
        remote_support_contact_module_mock.configuration.modify_remote_support_contact_details = MagicMock(
            side_effect=MockApiException)
        remote_support_contact_module_mock.perform_module_operation()
        assert MockRemoteSupportContactApi.modify_remote_support_contact_failed_msg() in \
            remote_support_contact_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_invalid_email(self, remote_support_contact_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        contact_id = 0
        self.get_module_args.update({'contact_id': contact_id,
                                     'email': "abc",
                                     'state': "present"})
        remote_support_contact_module_mock.module.params = self.get_module_args
        remote_support_contact_module_mock.configuration.get_remote_support_contact_details = MagicMock(
            return_value=MockRemoteSupportContactApi.REMOTE_SUPPORT_CONTACT_DETAILS)
        remote_support_contact_module_mock.configuration.modify_remote_support_contact_details = MagicMock(
            side_effect=MockApiException)
        remote_support_contact_module_mock.perform_module_operation()
        assert MockRemoteSupportContactApi.modify_remote_support_contact_failed_msg() in \
            remote_support_contact_module_mock.module.fail_json.call_args[1]['msg']
