# Copyright: (c) 2024, Dell Technologies

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
from ansible_collections.dellemc.powerstore.plugins.modules.smbshare import PowerStoreSMBShare, is_match_smb_parent, \
    is_match_path


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
            return_value={})
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
            return_value={})
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

    def test_create_smb_share_with_aces(self, smb_share_module_mock):
        self.get_module_args.update({
            'share_name': MockSMBShareApi.SMB_NAME,
            'nas_server': 'ansible_nas_server_2',
            'filesystem': 'sample_file_system',
            'description': 'test update SMB share',
            'state': 'present',
            'acl': [
                {"state": "present",
                 "trustee_name": "Everyone",
                 "trustee_type": "WellKnown",
                 "access_level": "Read",
                 "access_type": "Allow"},
                {"state": "absent",
                 "trustee_name": "S-1-5-21-8-5-1-32",
                 "trustee_type": "SID",
                 "access_level": "Read",
                 "access_type": "Allow"}
            ],
        })
        smb_share_module_mock.module.params = self.get_module_args
        smb_share_module_mock.get_smb_share = MagicMock(
            return_value={"smb_share_details": {"id": "61d68cf6-34d3-7b16-0370-96e8abdcbab0",
                                                "description": "share details"},
                          "id": "61d68cf6-34d3-7b16-0370-96e8abdcbab0", "description": "share details"})
        smb_share_module_mock.provisioning.get_smb_share_by_name = MagicMock(
            return_value={"smb_share_details": {"id": "61d68cf6-34d3-7b16-0370-96e8abdcbab0",
                                                "description": "share details"},
                          "id": "61d68cf6-34d3-7b16-0370-96e8abdcbab0", "description": "share details"})
        smb_share_module_mock.perform_module_operation()
        assert smb_share_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_is_match_smb_parent(self, smb_share_module_mock):
        smb_parent = 'test_fs'
        smb_share_details = {"file_system": {"id": "61d68c36-7c59-f5d9-65f0-96e8abdcbab0", "name": "file_system"}}
        result = is_match_smb_parent(smb_parent, smb_share_details)
        assert not result
        smb_parent = "61d68c36-7c59-f5d9-65f0-96e8abdcbab0"
        result = is_match_smb_parent(smb_parent, smb_share_details)
        assert result
        smb_parent = "61d68c36-7c59"
        result = is_match_smb_parent(smb_parent, smb_share_details)
        assert not result

    def test_is_match_path(self, smb_share_module_mock):
        input_path = "\file_system"
        smb_share_details = {"path": "/file_system"}
        result = is_match_path(input_path, smb_share_details)
        assert not result
        input_path = "/file_system"
        result = is_match_path(input_path, smb_share_details)
        assert result

    def test_validate_unmask_share(self, smb_share_module_mock):
        with pytest.raises(Exception) as exc_info:
            smb_share_module_mock.validate_umask('te')
        assert exc_info.value.args[0] == MockSMBShareApi.smb_error_messages()['umask_error']
        nas_server_name = 'ansible_nas_server_2'
        smb_share_module_mock.provisioning.get_nas_server_by_name = MagicMock(side_effect=MockApiException)
        result = smb_share_module_mock.get_nas_server_id(nas_server_name)
        assert result == nas_server_name
        smb_share_module_mock.provisioning.get_smb_share = MagicMock(side_effect=MockApiException)
        args = ("61d68c36-7c59-f5d9-65f0-96e8abdcbab0", "smb_share", None, None, None)
        result = smb_share_module_mock.get_smb_share(*args)
        assert result is None
        smb_share_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=[{"filesystem_type": "Primary"}])
        smb_share_module_mock.get_nas_server_id = MagicMock(return_value=None)
        args = ("smb_parent", "new_snapshot", "nas_server")
        result = smb_share_module_mock.get_filesystem_id(*args)
        assert result == "smb_parent"
