# Copyright: (c) 2021, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for SMB Share module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_smbshare_api import MockSMBShareApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.smbshare import PowerStoreSMBShare


class TestPowerStoreSMBShare():

    get_module_args = MockSMBShareApi.SMB_SHARE_COMMON_ARGS

    @pytest.fixture
    def smb_share_module_mock(self, mocker):
        mocker.patch(MockSMBShareApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        smb_share_module_mock = PowerStoreSMBShare()
        smb_share_module_mock.module = MagicMock()
        return smb_share_module_mock

    def test_get_smb_share_response(self, smb_share_module_mock):
        self.get_module_args.update({
            'share_id': "61d68cf6-34d3-7b16-0370-96e8abdcbab0",
            'state': "present"
        })
        smb_share_module_mock.module.params = self.get_module_args
        smb_share_module_mock.provisioning.get_smb_share = MagicMock(
            return_value=MockSMBShareApi.SMB_SHARE_DETAILS[0])
        smb_share_module_mock.perform_module_operation()
        assert self.get_module_args['share_id'] == smb_share_module_mock.module.exit_json.call_args[1]['smb_share_details']['id']
        smb_share_module_mock.provisioning.get_smb_share.assert_called()

    def test_get_smbshare_response_by_name(self, smb_share_module_mock):
        self.get_module_args.update({
            'share_name': MockSMBShareApi.SMB_NAME,
            'nas_server': MockSMBShareApi.NAS_ID,
            'state': "present"
        })
        smb_share_module_mock.module.params = self.get_module_args
        smb_share_module_mock.provisioning.get_smb_share_by_name = MagicMock(
            return_value=MockSMBShareApi.SMB_SHARE_DETAILS)
        smb_share_module_mock.provisioning.get_smb_share = MagicMock(
            return_value=MockSMBShareApi.SMB_SHARE_DETAILS[0])
        smb_share_module_mock.perform_module_operation()
        assert self.get_module_args['share_name'] == smb_share_module_mock.module.exit_json.call_args[1]['smb_share_details']['name']
        smb_share_module_mock.provisioning.get_smb_share_by_name.assert_called()

    def test_get_smbshare_without_nas_server(self, smb_share_module_mock):
        self.get_module_args.update({
            'share_name': MockSMBShareApi.SMB_NAME,
            'state': "present"
        })
        smb_share_module_mock.module.params = self.get_module_args
        smb_share_module_mock.provisioning.get_smb_share_by_name = MagicMock(
            return_value=MockSMBShareApi.SMB_SHARE_DETAILS)
        smb_share_module_mock.provisioning.get_smb_share = MagicMock(
            return_value=MockSMBShareApi.SMB_SHARE_DETAILS[0])
        smb_share_module_mock.perform_module_operation()
        assert MockSMBShareApi.get_smbshare_without_nas_server_failed_msg() in \
               smb_share_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_smb_share(self, smb_share_module_mock):
        self.get_module_args.update({
            'share_name': MockSMBShareApi.SMB_NAME,
            'nas_server': 'ansible_nas_server_2',
            'filesystem': 'sample_file_system',
            'path': '/sample_file_system',
            'state': 'present'
        })
        smb_share_module_mock.module.params = self.get_module_args
        smb_share_module_mock.provisioning.get_smb_share_by_name = MagicMock(
            return_value=None)
        smb_share_module_mock.perform_module_operation()
        assert smb_share_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_smb_share_with_exception(self, smb_share_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'share_name': MockSMBShareApi.SMB_NAME,
            'nas_server': 'ansible_nas_server',
            'filesystem': 'sample_file_system',
            'path': '/sample_file_system',
            'state': 'present'
        })
        smb_share_module_mock.module.params = self.get_module_args
        smb_share_module_mock.provisioning.get_smb_share_by_name = MagicMock(
            return_value=None)
        smb_share_module_mock.provisioning.create_smb_share = MagicMock(
            side_effect=MockApiException)
        smb_share_module_mock.perform_module_operation()
        smb_share_module_mock.provisioning.create_smb_share.assert_called()

    def test_modify_smb_share(self, smb_share_module_mock):
        self.get_module_args.update({
            'share_name': MockSMBShareApi.SMB_NAME,
            'nas_server': 'ansible_nas_server_2',
            'is_branch_cache_enabled': False,
            'is_continuous_availability_enabled': False,
            'offline_availability': 'Programs',
            'umask': '007',
            'state': 'present'
        })
        smb_share_module_mock.module.params = self.get_module_args
        smb_share_module_mock.provisioning.get_smb_share_by_name = MagicMock(
            return_value=MockSMBShareApi.SMB_SHARE_DETAILS)
        smb_share_module_mock.provisioning.get_smb_share = MagicMock(
            return_value=MockSMBShareApi.MODIFY_SMB_SHARE)
        smb_share_module_mock.perform_module_operation()
        assert self.get_module_args['share_name'] == smb_share_module_mock.module.exit_json.call_args[1]['smb_share_details']['name']
        assert smb_share_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_smb_share_with_exception(self, smb_share_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'share_name': MockSMBShareApi.SMB_NAME,
            'nas_server': 'ansible_nas_server_2',
            'is_branch_cache_enabled': False,
            'state': 'present'
        })
        smb_share_module_mock.module.params = self.get_module_args
        smb_share_module_mock.provisioning.get_smb_share_by_name = MagicMock(
            return_value=MockSMBShareApi.SMB_SHARE_DETAILS)
        smb_share_module_mock.provisioning.update_smb_share = MagicMock(
            side_effect=MockApiException)
        smb_share_module_mock.perform_module_operation()
        smb_share_module_mock.provisioning.update_smb_share.assert_called()

    def test_delete_smb_share(self, smb_share_module_mock):
        self.get_module_args.update({
            'share_name': MockSMBShareApi.SMB_NAME,
            'nas_server': 'ansible_nas_server_2',
            'state': 'absent'
        })
        smb_share_module_mock.module.params = self.get_module_args
        smb_share_module_mock.provisioning.get_smb_share_by_name = MagicMock(
            return_value=MockSMBShareApi.SMB_SHARE_DETAILS)
        smb_share_module_mock.perform_module_operation()
        smb_share_module_mock.provisioning.delete_smb_share.assert_called()

    def test_delete_smb_share_with_exception(self, smb_share_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'share_id': MockSMBShareApi.SMB_ID,
            'state': 'absent'
        })
        smb_share_module_mock.module.params = self.get_module_args
        smb_share_module_mock.provisioning.get_smb_share = MagicMock(
            return_value=MockSMBShareApi.SMB_SHARE_DETAILS[0])
        smb_share_module_mock.provisioning.delete_smb_share = MagicMock(
            side_effect=MockApiException)
        smb_share_module_mock.perform_module_operation()
        smb_share_module_mock.provisioning.delete_smb_share.assert_called()

    def test_create_smb_share_without_path(self, smb_share_module_mock):
        self.get_module_args.update({
            'share_name': MockSMBShareApi.SMB_NAME,
            'nas_server': 'ansible_nas_server_2',
            'filesystem': 'sample_file_system',
            'state': 'present'
        })
        smb_share_module_mock.module.params = self.get_module_args
        smb_share_module_mock.provisioning.get_smb_share_by_name = MagicMock(
            return_value=None)
        smb_share_module_mock.perform_module_operation()
        assert MockSMBShareApi.create_smb_share_without_path_failed_msg() in \
               smb_share_module_mock.module.fail_json.call_args[1]['msg']
