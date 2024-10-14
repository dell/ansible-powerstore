# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Filesystem module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_filesystem_api import MockFilesystemApi
from ansible_collections.dellemc.powerstore.plugins.modules.filesystem import PowerStoreFileSystem
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries.powerstore_unit_base \
    import PowerStoreUnitBase


class TestPowerStoreFileSystem(PowerStoreUnitBase):

    get_module_args = MockFilesystemApi.FILESYSTEM_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerStoreFileSystem

    def set_cluster(self, powerstore_module_mock):
        powerstore_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockFilesystemApi.CLUSTER_DETAILS)
        return powerstore_module_mock

    def test_get_filesystem_by_id(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_id": MockFilesystemApi.FS_ID,
                                "state": "present"})
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        powerstore_module_mock.perform_module_operation()
        assert self.get_module_args['filesystem_id'] == powerstore_module_mock.module.exit_json.call_args[1]["filesystem_details"]["id"]
        powerstore_module_mock.provisioning.get_filesystem_details.assert_called()

    def test_get_filesystem_by_name(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_name": MockFilesystemApi.FS_NAME,
                                "nas_server": MockFilesystemApi.NAS_NAME,
                                "state": "present"})
        powerstore_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS)
        powerstore_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1)
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        powerstore_module_mock.perform_module_operation()
        assert self.get_module_args["filesystem_name"] == powerstore_module_mock.module.exit_json.call_args[1]["filesystem_details"]["name"]
        powerstore_module_mock.provisioning.get_filesystem_by_name.assert_called()

    def test_get_filesystem_with_exception(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_name": 'sample_filesystem',
                                "nas_server": MockFilesystemApi.NAS_ID,
                                "state": 'present'})
        powerstore_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS[0])
        powerstore_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            side_effect=MockApiException)
        powerstore_module_mock.perform_module_operation()
        powerstore_module_mock.provisioning.get_filesystem_by_name.assert_called()

    def test_get_filesystem_no_nas_exception(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_name": 'sample_filesystem',
                                "nas_server": MockFilesystemApi.NAS_ID,
                                "state": 'present'})
        powerstore_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=None)
        powerstore_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockFilesystemApi.exception_messages("get_filesystem_no_nas"),
                                    powerstore_module_mock,
                                    invoke_perform_module=True)

    def test_get_nas_for_filesystem_with_exception(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_name": 'sample_filesystem',
                                "nas_server": MockFilesystemApi.NAS_ID,
                                "state": 'present'})
        powerstore_module_mock.provisioning.get_nas_server_details = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockFilesystemApi.exception_messages("get_nas_server"),
                                    powerstore_module_mock,
                                    invoke_perform_module=True)

    def test_create_filesystem(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_name": MockFilesystemApi.FS_NAME,
                                "nas_server": MockFilesystemApi.NAS_NAME,
                                'description': MockFilesystemApi.DESCRIPTION1,
                                "size": 10,
                                "cap_unit": "GB",
                                "access_policy": "UNIX",
                                "locking_policy": "ADVISORY",
                                "config_type": "GENERAL",
                                "folder_rename_policy": "ALL_FORBIDDEN",
                                "protection_policy": "sample_protection_policy",
                                "smb_properties": {"is_smb_notify_on_write_enabled": True,
                                                   "is_smb_notify_on_access_enabled": True,
                                                   "is_smb_op_locks_enabled": True,
                                                   "is_smb_no_notify_enabled": True,
                                                   "smb_notify_on_change_dir_depth": 1,
                                                   "is_smb_sync_writes_enabled": True},
                                "quota_defaults": {"grace_period": 1, "grace_period_unit": "months",
                                                   "default_hard_limit": 10,
                                                   "default_soft_limit": 8, "cap_unit": None},
                                "is_async_mtime_enabled": True,
                                "flr_attributes": {"mode": "Enterprise",
                                                   "minimum_retention": "5D",
                                                   "maximum_retention": "10D",
                                                   "default_retention": "7D"},
                                "file_events_publishing_mode": "ALL",
                                "state": 'present'})
        powerstore_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS)
        powerstore_module_mock.protection.get_protection_policy_by_name = MagicMock(
            return_value=MockFilesystemApi.PROTECTION_POLICY_DETAILS)
        powerstore_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=None)
        powerstore_module_mock.provisioning.create_filesystem = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        powerstore_module_mock.perform_module_operation()
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is True
        powerstore_module_mock.provisioning.create_filesystem.assert_called()

    def test_create_filesystem_with_pp_id(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_name": MockFilesystemApi.FS_NAME,
                                "nas_server": MockFilesystemApi.NAS_NAME,
                                'description': MockFilesystemApi.DESCRIPTION1,
                                "size": 10,
                                "cap_unit": "GB",
                                "access_policy": "UNIX",
                                "protection_policy": "4db27abe-08cf-427d-a95b-e7a51216b0cf",
                                "state": 'present'})
        powerstore_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS)
        powerstore_module_mock.protection.get_protection_policy_details = MagicMock(
            return_value=MockFilesystemApi.PROTECTION_POLICY_DETAILS[0])
        powerstore_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=None)
        powerstore_module_mock.provisioning.create_filesystem = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        powerstore_module_mock.perform_module_operation()
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is True
        powerstore_module_mock.provisioning.create_filesystem.assert_called()

    def test_get_pp_to_create_filesystem_with_exception(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_name": MockFilesystemApi.FS_NAME,
                                "nas_server": MockFilesystemApi.NAS_NAME,
                                "size": 10,
                                "cap_unit": "GB",
                                "protection_policy": "4db27abe-08cf-427d-a95b-e7a51216b0cf",
                                "state": 'present'})
        powerstore_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS)
        powerstore_module_mock.protection.get_protection_policy_details = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockFilesystemApi.exception_messages("get_protection_policy"),
                                    powerstore_module_mock,
                                    invoke_perform_module=True)

    def test_create_filesystem_with_exception(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_name": MockFilesystemApi.FS_NAME,
                                "nas_server": MockFilesystemApi.NAS_NAME,
                                "size": 10,
                                "cap_unit": "GB",
                                "protection_policy": "4db27abe-08cf-427d-a95b-e7a51216b0cf",
                                "state": 'present'})
        powerstore_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS)
        powerstore_module_mock.protection.get_protection_policy_details = MagicMock(
            return_value=MockFilesystemApi.PROTECTION_POLICY_DETAILS[0])
        powerstore_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=None)
        powerstore_module_mock.provisioning.create_filesystem = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockFilesystemApi.exception_messages("create_filesystem"),
                                    powerstore_module_mock,
                                    invoke_perform_module=True)

    def test_create_volume_with_size_less_than_3gb(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_name": MockFilesystemApi.FS_NAME,
                                "nas_server": MockFilesystemApi.NAS_NAME,
                                "size": 1,
                                "cap_unit": "GB",
                                "protection_policy": "4db27abe-08cf-427d-a95b-e7a51216b0cf",
                                "state": 'present'})
        self.capture_fail_json_call(MockFilesystemApi.create_filesystem_with_size_less_than_3_failed_msg(),
                                    powerstore_module_mock,
                                    invoke_perform_module=True)

    def test_create_volume_without_size(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_name": MockFilesystemApi.FS_NAME,
                                "nas_server": MockFilesystemApi.NAS_NAME,
                                "cap_unit": "GB",
                                "protection_policy": "4db27abe-08cf-427d-a95b-e7a51216b0cf",
                                "state": 'present'})
        self.capture_fail_json_call(MockFilesystemApi.create_filesystem_without_size_failed_msg(),
                                    powerstore_module_mock,
                                    invoke_perform_module=True)

    def test_modify_filesystem(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_name": MockFilesystemApi.FS_NAME,
                                "nas_server": MockFilesystemApi.NAS_NAME,
                                'description': "",
                                "size": 4,
                                "cap_unit": "TB",
                                "config_type": "GENERAL",
                                "access_policy": "NATIVE",
                                "locking_policy": "MANDATORY",
                                "folder_rename_policy": "SMB_FORBIDDEN",
                                "protection_policy": "",
                                "smb_properties": {"is_smb_notify_on_write_enabled": False,
                                                   "is_smb_notify_on_access_enabled": False,
                                                   "is_smb_op_locks_enabled": False,
                                                   "is_smb_no_notify_enabled": False,
                                                   "smb_notify_on_change_dir_depth": 3,
                                                   "is_smb_sync_writes_enabled": False},
                                "quota_defaults": {"grace_period": 2,
                                                   "grace_period_unit": "weeks",
                                                   "default_hard_limit": 3,
                                                   "default_soft_limit": 2,
                                                   "cap_unit": "TB"},
                                "is_async_mtime_enabled": True,
                                "flr_attributes": {"minimum_retention": "10D",
                                                   "maximum_retention": "30D",
                                                   "default_retention": "15D"},
                                "file_events_publishing_mode": "ALL",
                                "state": 'present'})
        powerstore_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS)
        powerstore_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1)
        powerstore_module_mock.provisioning.modify_filesystem = MagicMock(
            return_value=None)
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.MODIFY_FS_DETAILS[0])
        powerstore_module_mock.perform_module_operation()
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is True
        powerstore_module_mock.provisioning.modify_filesystem.assert_called()

    def test_modify_grace_period_to_days_filesystem(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_name": MockFilesystemApi.FS_NAME,
                                "nas_server": MockFilesystemApi.NAS_ID,
                                "size": 4,
                                "quota_defaults": {"grace_period": 2,
                                                   "grace_period_unit": "days",
                                                   "default_hard_limit": 3,
                                                   "default_soft_limit": 2,
                                                   "cap_unit": "GB"},
                                "state": 'present'})
        powerstore_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS[0])
        powerstore_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockFilesystemApi.MODIFY_FS_DETAILS)
        powerstore_module_mock.provisioning.modify_filesystem = MagicMock(
            return_value=None)
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        powerstore_module_mock.perform_module_operation()
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is True
        powerstore_module_mock.provisioning.modify_filesystem.assert_called()

    def test_modify_grace_period_to_months_filesystem(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_name": MockFilesystemApi.FS_NAME,
                                "nas_server": MockFilesystemApi.NAS_ID,
                                "quota_defaults": {"grace_period": 5,
                                                   "grace_period_unit": "months",
                                                   "default_hard_limit": 3,
                                                   "default_soft_limit": 2,
                                                   "cap_unit": "GB"},
                                "state": 'present'})
        powerstore_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS[0])
        powerstore_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockFilesystemApi.MODIFY_FS_DETAILS)
        powerstore_module_mock.provisioning.modify_filesystem = MagicMock(
            return_value=None)
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        powerstore_module_mock.perform_module_operation()
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is True
        powerstore_module_mock.provisioning.modify_filesystem.assert_called()

    def test_modify_filesystem_wo_grace_period_unit_wo_cap_unit(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_name": MockFilesystemApi.FS_NAME,
                                "nas_server": MockFilesystemApi.NAS_ID,
                                "quota_defaults": {"grace_period": 5,
                                                   "grace_period_unit": None,
                                                   "default_hard_limit": 3,
                                                   "default_soft_limit": 2,
                                                   "cap_unit": None},
                                "state": 'present'})
        powerstore_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS[0])
        powerstore_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockFilesystemApi.MODIFY_FS_DETAILS)
        powerstore_module_mock.provisioning.modify_filesystem = MagicMock(
            return_value=None)
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        powerstore_module_mock.perform_module_operation()
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is True
        powerstore_module_mock.provisioning.modify_filesystem.assert_called()

    def test_modify_filesystem_with_exception(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_name": MockFilesystemApi.FS_NAME,
                                "nas_server": MockFilesystemApi.NAS_ID,
                                "size": 4,
                                "quota_defaults": {"grace_period": 2,
                                                   "grace_period_unit": "days",
                                                   "default_hard_limit": 3,
                                                   "default_soft_limit": 2,
                                                   "cap_unit": "GB"},
                                "state": 'present'})
        powerstore_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS[0])
        powerstore_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockFilesystemApi.MODIFY_FS_DETAILS)
        powerstore_module_mock.provisioning.modify_filesystem = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockFilesystemApi.exception_messages("modify_filesystem"),
                                    powerstore_module_mock,
                                    invoke_perform_module=True)

    def test_modify_filesystem_with_invalid_default_hard_limit(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_name": MockFilesystemApi.FS_NAME,
                                "nas_server": MockFilesystemApi.NAS_ID,
                                "size": 4,
                                "quota_defaults": {"grace_period": 2,
                                                   "grace_period_unit": "days",
                                                   "default_hard_limit": -1,
                                                   "default_soft_limit": 2,
                                                   "cap_unit": "GB"},
                                "state": 'present'})
        powerstore_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockFilesystemApi.NAS_SERVER_DETAILS[0])
        powerstore_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockFilesystemApi.MODIFY_FS_DETAILS)
        powerstore_module_mock.provisioning.modify_filesystem = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockFilesystemApi.filesystem_with_invalid_default_hard_limit(),
                                    powerstore_module_mock,
                                    invoke_perform_module=True)

    def test_delete_filesystem(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_id": MockFilesystemApi.FS_ID,
                                "state": "absent"})
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        powerstore_module_mock.perform_module_operation()
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is True
        powerstore_module_mock.provisioning.delete_filesystem.assert_called()

    def test_delete_filesystem_with_exception(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_id": MockFilesystemApi.FS_ID,
                                "state": "absent"})
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        powerstore_module_mock.provisioning.delete_filesystem = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockFilesystemApi.exception_messages("delete_filesystem"),
                                    powerstore_module_mock,
                                    invoke_perform_module=True)

    def test_get_filesystem_snapshot(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {'snapshot_id': "61e49f3f-9b57-e69b-1038-aa02b52a030f",
                                'refresh_filesystem': True,
                                'state': "present"})
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.protection.get_filesystem_snapshot_details = MagicMock(
            return_value=MockFilesystemApi.FILESYSTEM_SNAP_DETAILS[0])
        assert powerstore_module_mock.provisioning.get_filesystem_snapshot_details()
        powerstore_module_mock.provisioning.get_filesystem_snapshot_details.assert_called()

    def test_get_filesystem_snapshot_with_exception(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {'snapshot_id': "61e49f3f-9b57-e69b-1038-aa02b52a030f",
                                'refresh_filesystem': True,
                                'state': "present"})
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.protection.get_filesystem_snapshot_details = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_call(MockFilesystemApi.exception_messages("fs_snapshot"),
                                    powerstore_module_mock,
                                    invoke_perform_module=True)

    def test_clone_filesystem(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_id": MockFilesystemApi.FS_ID,
                                "clone_filesystem": {"name": "Test"},
                                "state": 'present'})
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.set_parms = MagicMock(side_effect=[None, None, MockFilesystemApi.FS_DETAILS_1[0]])
        powerstore_module_mock.get_filesystem_details = MagicMock()
        powerstore_module_mock.get_clone = MagicMock(return_value=None)
        powerstore_module_mock.clone_filesystem_dict_params = MagicMock(return_value={"name": "Test"})
        powerstore_module_mock.provisioning.clone_filesystem = MagicMock()
        powerstore_module_mock.perform_module_operation()
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is True
        powerstore_module_mock.provisioning.clone_filesystem.assert_called()

    def test_clone_filesystem_with_exception(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"filesystem_id": MockFilesystemApi.FS_ID,
                                "clone_filesystem": {"name": "Test"},
                                "state": 'present'})
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.set_parms = MagicMock(side_effect=[None, None, MockFilesystemApi.FS_DETAILS_1[0]])
        powerstore_module_mock.get_filesystem_details = MagicMock()
        powerstore_module_mock.get_clone = MagicMock(return_value=None)
        powerstore_module_mock.clone_filesystem_dict_params = MagicMock(return_value={"name": "Test"})
        powerstore_module_mock.provisioning.clone_filesystem = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_call(MockFilesystemApi.exception_messages("clone_filesystem"),
                                    powerstore_module_mock,
                                    invoke_perform_module=True)

    def test_refresh_filesystem(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"snapshot_id": MockFilesystemApi.SNAP_ID,
                                "refresh_filesystem": True,
                                "state": 'present'})
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.provisioning.refresh_filesystem = MagicMock(
            return_value=None)
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        powerstore_module_mock.perform_module_operation()
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is True
        powerstore_module_mock.provisioning.refresh_filesystem.assert_called()

    def test_refresh_filesystem_with_exception(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"snapshot_id": MockFilesystemApi.SNAP_ID,
                                "refresh_filesystem": True,
                                "state": 'present'})
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.provisioning.refresh_filesystem = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_call(MockFilesystemApi.exception_messages("refresh_filesystem"),
                                    powerstore_module_mock,
                                    invoke_perform_module=True)

    def test_restore_filesystem(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"snapshot_id": MockFilesystemApi.SNAP_ID,
                                "restore_filesystem": True,
                                "state": 'present'})
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.provisioning.restore_filesystem = MagicMock(
            return_value=None)
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemApi.FS_DETAILS_1[0])
        powerstore_module_mock.perform_module_operation()
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is True
        powerstore_module_mock.provisioning.restore_filesystem.assert_called()

    def test_restore_filesystem_with_exception(self, powerstore_module_mock):
        powerstore_module_mock = self.set_cluster(powerstore_module_mock)
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {"snapshot_id": MockFilesystemApi.SNAP_ID,
                                "restore_filesystem": True,
                                "state": 'present'})
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.provisioning.restore_filesystem = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_call(MockFilesystemApi.exception_messages("restore_filesystem"),
                                    powerstore_module_mock,
                                    invoke_perform_module=True)
