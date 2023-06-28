# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Filesystem module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_filesystem_api import MockFilesystemApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_powerstore_connection = MagicMock()
utils.PowerStoreException = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerstore.plugins.modules.filesystem import PowerStoreFileSystem


class TestPowerStoreFileSystem():

    get_module_args = MockFilesystemApi.FILESYSTEM_COMMON_ARGS

    @pytest.fixture
    def filesystem_module_mock(self, mocker):
        mocker.patch(MockFilesystemApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        filesystem_module_mock = PowerStoreFileSystem()
        filesystem_module_mock.module = MagicMock()
        return filesystem_module_mock

    def test_get_filesystem_by_id(self, filesystem_module_mock):
        self.get_module_args.update({
            "filesystem_id": MockFilesystemApi.FS_ID,
            "state": "present"
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockFilesystemApi.CLUSTER_DETAILS)
        filesystem_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        filesystem_module_mock.perform_module_operation()
        assert self.get_module_args['filesystem_id'] == filesystem_module_mock.module.exit_json.call_args[1]["filesystem_details"]["id"]
        filesystem_module_mock.provisioning.get_filesystem_details.assert_called()

    def test_get_filesystem_by_name(self, filesystem_module_mock):
        self.get_module_args.update({
            "filesystem_name": MockFilesystemApi.FS_NAME,
            "nas_server": MockFilesystemApi.NAS_NAME,
            "state": "present"
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS)
        filesystem_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1)
        filesystem_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        filesystem_module_mock.perform_module_operation()
        assert self.get_module_args["filesystem_name"] == filesystem_module_mock.module.exit_json.call_args[1]["filesystem_details"]["name"]
        filesystem_module_mock.provisioning.get_filesystem_by_name.assert_called()

    def test_get_filesystem_with_exception(self, filesystem_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            "filesystem_name": 'sample_filesystem',
            "nas_server": MockFilesystemApi.NAS_ID,
            "state": 'present'
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS[0])
        filesystem_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            side_effect=MockApiException)
        filesystem_module_mock.perform_module_operation()
        filesystem_module_mock.provisioning.get_filesystem_by_name.assert_called()

    def test_get_filesystem_no_nas_exception(self, filesystem_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            "filesystem_name": 'sample_filesystem',
            "nas_server": MockFilesystemApi.NAS_ID,
            "state": 'present'
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=None)
        filesystem_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            side_effect=MockApiException)
        filesystem_module_mock.perform_module_operation()
        filesystem_module_mock.provisioning.get_nas_server_details.assert_called()

    def test_get_nas_for_filesystem_with_exception(self, filesystem_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            "filesystem_name": 'sample_filesystem',
            "nas_server": MockFilesystemApi.NAS_ID,
            "state": 'present'
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.provisioning.get_nas_server_details = MagicMock(
            side_effect=MockApiException)
        filesystem_module_mock.perform_module_operation()
        filesystem_module_mock.provisioning.get_nas_server_details.assert_called()

    def test_create_filesystem(self, filesystem_module_mock):
        self.get_module_args.update({
            "filesystem_name": MockFilesystemApi.FS_NAME,
            "nas_server": MockFilesystemApi.NAS_NAME,
            'description': MockFilesystemApi.DESCRIPTION1,
            "size": 10,
            "cap_unit": "GB",
            "access_policy": "UNIX",
            "locking_policy": "ADVISORY",
            "folder_rename_policy": "ALL_FORBIDDEN",
            "protection_policy": "sample_protection_policy",
            "smb_properties": {"is_smb_notify_on_write_enabled": True, "is_smb_notify_on_access_enabled": True,
                               "is_smb_op_locks_enabled": True, "is_smb_no_notify_enabled": True,
                               "smb_notify_on_change_dir_depth": 1, "is_smb_sync_writes_enabled": True},
            "quota_defaults": {"grace_period": 1, "grace_period_unit": "months",
                               "default_hard_limit": 10, "default_soft_limit": 8, "cap_unit": None},
            "config_type": "General",
            "is_async_mtime_enabled": True,
            "flr_attributes": {"mode": "Enterprise", "minimum_retention": "5D", "maximum_retention": "10D", "default_retention": "7D"},
            "file_events_publishing_mode": True,
            "state": 'present'
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS)
        filesystem_module_mock.protection.get_protection_policy_by_name = MagicMock(
            return_value=MockFilesystemApi.PROTECTION_POLICY_DETAILS)
        filesystem_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=None)
        filesystem_module_mock.provisioning.create_filesystem = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        filesystem_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        filesystem_module_mock.perform_module_operation()
        assert filesystem_module_mock.module.exit_json.call_args[1]['changed'] is True
        filesystem_module_mock.provisioning.create_filesystem.assert_called()

    def test_create_filesystem_with_pp_id(self, filesystem_module_mock):
        self.get_module_args.update({
            "filesystem_name": MockFilesystemApi.FS_NAME,
            "nas_server": MockFilesystemApi.NAS_NAME,
            'description': MockFilesystemApi.DESCRIPTION1,
            "size": 10,
            "cap_unit": "GB",
            "access_policy": "UNIX",
            "protection_policy": "4db27abe-08cf-427d-a95b-e7a51216b0cf",
            "state": 'present'
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS)
        filesystem_module_mock.protection.get_protection_policy_details = MagicMock(
            return_value=MockFilesystemApi.PROTECTION_POLICY_DETAILS[0])
        filesystem_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=None)
        filesystem_module_mock.provisioning.create_filesystem = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        filesystem_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        filesystem_module_mock.perform_module_operation()
        assert filesystem_module_mock.module.exit_json.call_args[1]['changed'] is True
        filesystem_module_mock.provisioning.create_filesystem.assert_called()

    def test_get_pp_to_create_filesystem_with_exception(self, filesystem_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            "filesystem_name": MockFilesystemApi.FS_NAME,
            "nas_server": MockFilesystemApi.NAS_NAME,
            "size": 10,
            "cap_unit": "GB",
            "protection_policy": "4db27abe-08cf-427d-a95b-e7a51216b0cf",
            "state": 'present'
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS)
        filesystem_module_mock.protection.get_protection_policy_details = MagicMock(
            side_effect=MockApiException)
        filesystem_module_mock.perform_module_operation()
        filesystem_module_mock.protection.get_protection_policy_details.assert_called()

    def test_create_filesystem_with_exception(self, filesystem_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            "filesystem_name": MockFilesystemApi.FS_NAME,
            "nas_server": MockFilesystemApi.NAS_NAME,
            "size": 10,
            "cap_unit": "GB",
            "protection_policy": "4db27abe-08cf-427d-a95b-e7a51216b0cf",
            "state": 'present'
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS)
        filesystem_module_mock.protection.get_protection_policy_details = MagicMock(
            return_value=MockFilesystemApi.PROTECTION_POLICY_DETAILS[0])
        filesystem_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=None)
        filesystem_module_mock.provisioning.create_filesystem = MagicMock(
            side_effect=MockApiException)
        filesystem_module_mock.perform_module_operation()
        filesystem_module_mock.provisioning.create_filesystem.assert_called()

    def test_create_volume_with_size_less_than_3gb(self, filesystem_module_mock):
        self.get_module_args.update({
            "filesystem_name": MockFilesystemApi.FS_NAME,
            "nas_server": MockFilesystemApi.NAS_NAME,
            "size": 1,
            "cap_unit": "GB",
            "protection_policy": "4db27abe-08cf-427d-a95b-e7a51216b0cf",
            "state": 'present'
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.perform_module_operation()
        assert MockFilesystemApi.create_filesystem_with_size_less_than_3_failed_msg() in \
               filesystem_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_volume_without_size(self, filesystem_module_mock):
        self.get_module_args.update({
            "filesystem_name": MockFilesystemApi.FS_NAME,
            "nas_server": MockFilesystemApi.NAS_NAME,
            "cap_unit": "GB",
            "protection_policy": "4db27abe-08cf-427d-a95b-e7a51216b0cf",
            "state": 'present'
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.perform_module_operation()
        assert MockFilesystemApi.create_filesystem_without_size_failed_msg() in \
               filesystem_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_filesystem(self, filesystem_module_mock):
        self.get_module_args.update({
            "filesystem_name": MockFilesystemApi.FS_NAME,
            "nas_server": MockFilesystemApi.NAS_NAME,
            'description': "",
            "size": 4,
            "cap_unit": "TB",
            "access_policy": "NATIVE",
            "locking_policy": "MANDATORY",
            "folder_rename_policy": "SMB_FORBIDDEN",
            "protection_policy": "",
            "smb_properties": {"is_smb_notify_on_write_enabled": False, "is_smb_notify_on_access_enabled": False,
                               "is_smb_op_locks_enabled": False, "is_smb_no_notify_enabled": False,
                               "smb_notify_on_change_dir_depth": 3, "is_smb_sync_writes_enabled": False},
            "quota_defaults": {"grace_period": 2, "grace_period_unit": "weeks",
                               "default_hard_limit": 3, "default_soft_limit": 2, "cap_unit": "TB"},
            "is_async_mtime_enabled": True,
            "flr_attributes": {"minimum_retention": "10D", "maximum_retention": "30D", "default_retention": "15D"},
            "file_events_publishing_mode": True,
            "state": 'present'
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS)
        filesystem_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1)
        filesystem_module_mock.provisioning.modify_filesystem = MagicMock(
            return_value=None)
        filesystem_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.MODIFY_FS_DETAILS[0])
        filesystem_module_mock.perform_module_operation()
        assert filesystem_module_mock.module.exit_json.call_args[1]['changed'] is True
        filesystem_module_mock.provisioning.modify_filesystem.assert_called()

    def test_modify_grace_period_to_days_filesystem(self, filesystem_module_mock):
        self.get_module_args.update({
            "filesystem_name": MockFilesystemApi.FS_NAME,
            "nas_server": MockFilesystemApi.NAS_ID,
            "size": 4,
            "quota_defaults": {"grace_period": 2, "grace_period_unit": "days",
                               "default_hard_limit": 3, "default_soft_limit": 2, "cap_unit": "GB"},
            "state": 'present'
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS[0])
        filesystem_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockFilesystemApi.MODIFY_FS_DETAILS)
        filesystem_module_mock.provisioning.modify_filesystem = MagicMock(
            return_value=None)
        filesystem_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        filesystem_module_mock.perform_module_operation()
        assert filesystem_module_mock.module.exit_json.call_args[1]['changed'] is True
        filesystem_module_mock.provisioning.modify_filesystem.assert_called()

    def test_modify_grace_period_to_months_filesystem(self, filesystem_module_mock):
        self.get_module_args.update({
            "filesystem_name": MockFilesystemApi.FS_NAME,
            "nas_server": MockFilesystemApi.NAS_ID,
            "quota_defaults": {"grace_period": 5, "grace_period_unit": "months",
                               "default_hard_limit": 3, "default_soft_limit": 2, "cap_unit": "GB"},
            "state": 'present'
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS[0])
        filesystem_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockFilesystemApi.MODIFY_FS_DETAILS)
        filesystem_module_mock.provisioning.modify_filesystem = MagicMock(
            return_value=None)
        filesystem_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        filesystem_module_mock.perform_module_operation()
        assert filesystem_module_mock.module.exit_json.call_args[1]['changed'] is True
        filesystem_module_mock.provisioning.modify_filesystem.assert_called()

    def test_modify_filesystem_wo_grace_period_unit_wo_cap_unit(self, filesystem_module_mock):
        self.get_module_args.update({
            "filesystem_name": MockFilesystemApi.FS_NAME,
            "nas_server": MockFilesystemApi.NAS_ID,
            "quota_defaults": {"grace_period": 5, "grace_period_unit": None,
                               "default_hard_limit": 3, "default_soft_limit": 2, "cap_unit": None},
            "state": 'present'
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS[0])
        filesystem_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockFilesystemApi.MODIFY_FS_DETAILS)
        filesystem_module_mock.provisioning.modify_filesystem = MagicMock(
            return_value=None)
        filesystem_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        filesystem_module_mock.perform_module_operation()
        assert filesystem_module_mock.module.exit_json.call_args[1]['changed'] is True
        filesystem_module_mock.provisioning.modify_filesystem.assert_called()

    def test_modify_filesystem_with_exception(self, filesystem_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            "filesystem_name": MockFilesystemApi.FS_NAME,
            "nas_server": MockFilesystemApi.NAS_ID,
            "size": 4,
            "quota_defaults": {"grace_period": 2, "grace_period_unit": "days",
                               "default_hard_limit": 3, "default_soft_limit": 2, "cap_unit": "GB"},
            "state": 'present'
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS[0])
        filesystem_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockFilesystemApi.MODIFY_FS_DETAILS)
        filesystem_module_mock.provisioning.modify_filesystem = MagicMock(
            side_effect=MockApiException)
        filesystem_module_mock.perform_module_operation()
        filesystem_module_mock.provisioning.modify_filesystem.assert_called()

    def test_modify_filesystem_with_invalid_default_hard_limit(self, filesystem_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            "filesystem_name": MockFilesystemApi.FS_NAME,
            "nas_server": MockFilesystemApi.NAS_ID,
            "size": 4,
            "quota_defaults": {"grace_period": 2, "grace_period_unit": "days",
                               "default_hard_limit": -1, "default_soft_limit": 2, "cap_unit": "GB"},
            "state": 'present'
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS[0])
        filesystem_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockFilesystemApi.MODIFY_FS_DETAILS)
        filesystem_module_mock.provisioning.modify_filesystem = MagicMock(
            side_effect=MockApiException)
        filesystem_module_mock.perform_module_operation()
        filesystem_module_mock.provisioning.modify_filesystem.assert_called()

    def test_delete_filesystem(self, filesystem_module_mock):
        self.get_module_args.update({
            "filesystem_id": MockFilesystemApi.FS_ID,
            "state": "absent"
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        filesystem_module_mock.perform_module_operation()
        assert filesystem_module_mock.module.exit_json.call_args[1]['changed'] is True
        filesystem_module_mock.provisioning.delete_filesystem.assert_called()

    def test_delete_filesystem_with_exception(self, filesystem_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            "filesystem_id": MockFilesystemApi.FS_ID,
            "state": "absent"
        })
        filesystem_module_mock.module.params = self.get_module_args
        filesystem_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        filesystem_module_mock.provisioning.delete_filesystem = MagicMock(
            side_effect=MockApiException)
        filesystem_module_mock.perform_module_operation()
        filesystem_module_mock.provisioning.delete_filesystem.assert_called()
