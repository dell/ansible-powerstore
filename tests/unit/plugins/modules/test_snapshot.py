# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Snapshot module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.\
    mock_snapshot_api import MockSnapshotApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.\
    mock_api_exception import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.snapshot import PowerStoreSnapshot


class TestPowerStoreSnapshot():

    get_module_args = MockSnapshotApi.SNAPSHOT_COMMON_ARGS

    @pytest.fixture
    def snapshot_module_mock(self, mocker):
        mocker.patch(MockSnapshotApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        snapshot_module_mock = PowerStoreSnapshot()
        snapshot_module_mock.module = MagicMock()
        snapshot_module_mock.module.check_mode = False
        return snapshot_module_mock

    def test_get_vol_snap_response(self, snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_id': '83314020-31b7-4e2d-98d4-535a733f35e8',
            'volume': '3fa9cb4c-4943-4baf-a420-83019ed7f6dd',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.get_vol_id_from_volume = MagicMock(return_value=MockSnapshotApi.SOURCE_VOL_DETAILS[0]['id'])
        snapshot_module_mock.protection.get_volume_snapshots = MagicMock(return_value=MockSnapshotApi.VOL_SNAPS)
        snapshot_module_mock.perform_module_operation()
        snapshot_module_mock.protection.get_volume_snapshot_details.assert_called()

    def test_get_vol_snap_response_exception(self, snapshot_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'snapshot_id': '83314020-31b7-4e2d-98d4-535a733f35e8',
            'volume': '3fa9cb4c-4943-4baf-a420-83019ed7f6dd',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.get_vol_id_from_volume = MagicMock(return_value=MockSnapshotApi.SOURCE_VOL_DETAILS[0]['id'])
        snapshot_module_mock.protection.get_volume_snapshots = MagicMock(return_value=MockSnapshotApi.VOL_SNAPS)
        snapshot_module_mock.protection.get_volume_snapshot_details = MagicMock(
            side_effect=MockApiException)
        snapshot_module_mock.perform_module_operation()
        snapshot_module_mock.protection.get_volume_snapshot_details.assert_called()

    def test_get_vg_snap_response(self, snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_id': 'f3baa2c7-bdef-4b83-8f71-b67c904683ab',
            'volume_group': '1a18566b-31d4-4c00-bfce-30deeeb08acb',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.get_vol_group_id_from_vg = MagicMock(return_value=MockSnapshotApi.SOURCE_VG_DETAILS[0]['id'])
        snapshot_module_mock.protection.get_volume_group_snapshots = MagicMock(return_value=MockSnapshotApi.VG_SNAPS)
        snapshot_module_mock.perform_module_operation()
        snapshot_module_mock.protection.get_volume_group_snapshot_details.assert_called()

    def test_get_vg_snap_response_exception(self, snapshot_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'snapshot_id': 'f3baa2c7-bdef-4b83-8f71-b67c904683ab',
            'volume_group': '1a18566b-31d4-4c00-bfce-30deeeb08acb',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.get_vol_group_id_from_vg = MagicMock(return_value=MockSnapshotApi.SOURCE_VG_DETAILS[0]['id'])
        snapshot_module_mock.protection.get_volume_group_snapshots = MagicMock(return_value=MockSnapshotApi.VG_SNAPS)
        snapshot_module_mock.protection.get_volume_group_snapshot_details = MagicMock(side_effect=MockApiException)
        snapshot_module_mock.perform_module_operation()
        snapshot_module_mock.protection.get_volume_group_snapshot_details.assert_called()

    def test_create_vol_snap(self, snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': 'ansible_vol_snap',
            'volume': 'ansible_vol',
            'desired_retention': '2',
            'retention_unit': 'days',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.get_vol_id_from_volume = MagicMock(
            return_value=MockSnapshotApi.SOURCE_VOL_DETAILS[0]['id'])
        snapshot_module_mock.get_vol_snapshot = MagicMock(return_value=None)
        snapshot_module_mock.get_vol_snap_details = MagicMock(return_value=None)
        snapshot_module_mock.perform_module_operation()
        snapshot_module_mock.protection.create_volume_snapshot.assert_called()

    def test_invalid_create_vol_snap_rename(self, snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': 'ansible_vol_snap',
            'new_snapshot_name': 'ansible_vol_snap_renamed',
            'volume': 'ansible_vol',
            'desired_retention': '2',
            'retention_unit': 'days',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.get_vol_id_from_volume = MagicMock(
            return_value=MockSnapshotApi.SOURCE_VOL_DETAILS[0]['id'])
        snapshot_module_mock.get_vol_snapshot = MagicMock(return_value=None)
        snapshot_module_mock.get_vol_snap_details = MagicMock(return_value=None)
        snapshot_module_mock.perform_module_operation()
        assert MockSnapshotApi.get_rename_create_failed_msg() in \
               snapshot_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_vg_snap(self, snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': 'ansible_vg_snap',
            'volume_group': 'ansible_vg',
            'desired_retention': '2',
            'retention_unit': 'days',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.get_vol_group_id_from_vg = MagicMock(return_value=MockSnapshotApi.SOURCE_VG_DETAILS[0]['id'])
        snapshot_module_mock.get_vol_group_snapshot = MagicMock(return_value=None)
        snapshot_module_mock.get_vol_group_snap_details = MagicMock(return_value=None)
        snapshot_module_mock.perform_module_operation()
        snapshot_module_mock.protection.create_volume_group_snapshot.assert_called()

    def test_invalid_create_vg_snap_rename(self, snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': 'ansible_vg_snap',
            'new_snapshot_name': 'ansible_vg_snap_renamed',
            'volume_group': 'ansible_vg',
            'desired_retention': '2',
            'retention_unit': 'days',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.get_vol_group_id_from_vg = MagicMock(return_value=MockSnapshotApi.SOURCE_VG_DETAILS[0]['id'])
        snapshot_module_mock.get_vol_group_snapshot = MagicMock(return_value=None)
        snapshot_module_mock.get_vol_group_snap_details = MagicMock(return_value=None)
        snapshot_module_mock.perform_module_operation()
        assert MockSnapshotApi.get_rename_create_failed_msg() in \
               snapshot_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_vol_snap(self, snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': 'ansible_vol_snap',
            'volume': 'ansible_vol',
            'description': 'description_modified',
            'desired_retention': '700',
            'retention_unit': 'hours',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.get_vol_id_from_volume = MagicMock(
            return_value=MockSnapshotApi.SOURCE_VOL_DETAILS[0]['id'])
        snapshot_module_mock.protection.get_volume_snapshots = MagicMock(
            return_value=MockSnapshotApi.VOL_SNAPS)
        snapshot_module_mock.get_vol_snap_details = MagicMock(
            return_value=MockSnapshotApi.VOL_SNAP_DETAILS)
        snapshot_module_mock.perform_module_operation()
        snapshot_module_mock.protection.modify_volume_snapshot.assert_called()

    def test_modify_vg_snap(self, snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': 'ansible_vg_snap',
            'volume_group': 'ansible_vg',
            'description': 'description_modified',
            'desired_retention': '4',
            'retention_unit': 'days',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.get_vol_group_id_from_vg = MagicMock(
            return_value=MockSnapshotApi.SOURCE_VG_DETAILS[0]['id'])
        snapshot_module_mock.protection.get_volume_group_snapshots = MagicMock(
            return_value=MockSnapshotApi.VG_SNAPS)
        snapshot_module_mock.get_vol_group_snap_details = MagicMock(
            return_value=MockSnapshotApi.VG_SNAP_DETAILS)
        snapshot_module_mock.perform_module_operation()
        snapshot_module_mock.protection.modify_volume_group_snapshot.assert_called()

    def test_rename_vol_snap(self, snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': 'ansible_vol_snap',
            'new_snapshot_name': 'ansible_vol_snap_renamed',
            'volume': 'ansible_vol',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_Value=MockSnapshotApi.SOURCE_VOL_DETAILS)
        snapshot_module_mock.get_vol_snap_details = MagicMock(
            return_value=MockSnapshotApi.VOL_SNAP_DETAILS)
        snapshot_module_mock.protection.get_volume_snapshots = MagicMock(
            return_value=MockSnapshotApi.VOL_SNAPS)
        snapshot_module_mock.perform_module_operation()
        snapshot_module_mock.protection.modify_volume_snapshot.assert_called()

    def test_rename_same_vol_snap(self, snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': 'ansible_vol_snap',
            'new_snapshot_name': 'ansible_vol_snap',
            'volume': 'ansible_vol',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_Value=MockSnapshotApi.SOURCE_VOL_DETAILS)
        snapshot_module_mock.get_vol_snap_details = MagicMock(
            return_value=MockSnapshotApi.VOL_SNAP_DETAILS)
        snapshot_module_mock.protection.get_volume_snapshots = MagicMock(
            return_value=MockSnapshotApi.VOL_SNAPS)
        snapshot_module_mock.perform_module_operation()
        assert snapshot_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_rename_vg_snap(self, snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': 'ansible_vg_snap',
            'new_snapshot_name': 'ansible_vg_snap_renamed',
            'volume_group': 'ansible_vg',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            return_Value=MockSnapshotApi.SOURCE_VG_DETAILS)
        snapshot_module_mock.get_vol_group_snap_details = MagicMock(
            return_value=MockSnapshotApi.VG_SNAP_DETAILS)
        snapshot_module_mock.protection.get_volume_group_snapshots = MagicMock(
            return_value=MockSnapshotApi.VG_SNAPS)
        snapshot_module_mock.perform_module_operation()
        snapshot_module_mock.protection.modify_volume_group_snapshot.assert_called()

    def test_rename_same_vg_snap(self, snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': 'ansible_vg_snap',
            'new_snapshot_name': 'ansible_vg_snap',
            'volume_group': 'ansible_vg',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            return_Value=MockSnapshotApi.SOURCE_VG_DETAILS)
        snapshot_module_mock.get_vol_group_snap_details = MagicMock(
            return_value=MockSnapshotApi.VG_SNAP_DETAILS)
        snapshot_module_mock.protection.get_volume_group_snapshots = MagicMock(
            return_value=MockSnapshotApi.VG_SNAPS)
        snapshot_module_mock.perform_module_operation()
        assert snapshot_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_delete_vol_snap(self, snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': 'ansible_vol_snap',
            'volume': 'ansible_vol',
            'state': "absent"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_Value=MockSnapshotApi.SOURCE_VOL_DETAILS)
        snapshot_module_mock.get_vol_snap_details = MagicMock(
            return_value=MockSnapshotApi.VOL_SNAP_DETAILS)
        snapshot_module_mock.protection.get_volume_snapshots = MagicMock(
            return_value=MockSnapshotApi.VOL_SNAPS)
        snapshot_module_mock.perform_module_operation()
        snapshot_module_mock.protection.delete_volume_snapshot.assert_called()

    def test_delete_vol_snap_exception(self, snapshot_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'snapshot_name': 'ansible_vol_snap',
            'volume': 'ansible_vol',
            'state': "absent"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_Value=MockSnapshotApi.SOURCE_VOL_DETAILS)
        snapshot_module_mock.get_vol_snap_details = MagicMock(
            return_value=MockSnapshotApi.VOL_SNAP_DETAILS)
        snapshot_module_mock.protection.get_volume_snapshots = MagicMock(
            return_value=MockSnapshotApi.VOL_SNAPS)
        snapshot_module_mock.protection.delete_volume_snapshot = MagicMock(
            side_effect=MockApiException)
        snapshot_module_mock.perform_module_operation()
        snapshot_module_mock.protection.delete_volume_snapshot.assert_called()

    def test_delete_vg_snap(self, snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': 'ansible_vg_snap',
            'volume_group': 'ansible_vg',
            'state': "absent"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            return_Value=MockSnapshotApi.SOURCE_VG_DETAILS)
        snapshot_module_mock.get_vol_group_snap_details = MagicMock(
            return_value=MockSnapshotApi.VG_SNAP_DETAILS)
        snapshot_module_mock.protection.get_volume_group_snapshots = MagicMock(
            return_value=MockSnapshotApi.VG_SNAPS)
        snapshot_module_mock.perform_module_operation()
        snapshot_module_mock.protection.delete_volume_group_snapshot.assert_called()

    def test_delete_vg_exception(self, snapshot_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'snapshot_name': 'ansible_vg_snap',
            'volume_group': 'ansible_vg',
            'state': "absent"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            return_Value=MockSnapshotApi.SOURCE_VG_DETAILS)
        snapshot_module_mock.get_vol_group_snap_details = MagicMock(
            return_value=MockSnapshotApi.VG_SNAP_DETAILS)
        snapshot_module_mock.protection.get_volume_group_snapshots = MagicMock(
            return_value=MockSnapshotApi.VG_SNAPS)
        snapshot_module_mock.protection.delete_volume_group_snapshot = MagicMock(
            side_effect=MockApiException)
        snapshot_module_mock.perform_module_operation()
        snapshot_module_mock.protection.delete_volume_group_snapshot.assert_called()

    def test_invalid_desired_retention_days(self, snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': 'ansible_vg_snap',
            'volume_group': 'ansible_vg',
            'desired_retention': '32',
            'retention_unit': 'days',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.perform_module_operation()
        assert MockSnapshotApi.get_invalid_desired_retention_days_failed_msg() in \
               snapshot_module_mock.module.fail_json.call_args[1]['msg']

    def test_invalid_desired_retention_hours(self, snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': 'ansible_vg_snap',
            'volume_group': 'ansible_vg',
            'desired_retention': '745',
            'retention_unit': 'hours',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.perform_module_operation()
        assert MockSnapshotApi.get_invalid_desired_retention_hours_failed_msg() in \
               snapshot_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_nonexisting_vol_details(self, snapshot_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'snapshot_name': 'ansible_vg_snap',
            'volume': 'ansible_vol1',
            'desired_retention': '10',
            'retention_unit': 'days',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.provisioning.get_volume_by_name = MagicMock(
            side_effect=MockApiException)
        snapshot_module_mock.perform_module_operation()
        snapshot_module_mock.provisioning.get_volume_by_name.assert_called()

    def test_get_nonexisting_vol_details_id(self, snapshot_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'snapshot_name': 'ansible_vg_snap',
            'volume': '3fa9cb4c-4943-4baf-a420-83019ed7f6de',
            'desired_retention': '10',
            'retention_unit': 'days',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.provisioning.get_volume_details = MagicMock(
            side_effect=MockApiException)
        snapshot_module_mock.perform_module_operation()
        snapshot_module_mock.provisioning.get_volume_details.assert_called()

    def test_get_nonexisting_vg_details_id(self, snapshot_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'snapshot_name': 'ansible_vg_snap',
            'volume_group': '3fa9cb4c-4943-4baf-a420-83019ed7f6df',
            'desired_retention': '10',
            'retention_unit': 'days',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.provisioning.get_volume_group_details = MagicMock(
            side_effect=MockApiException)
        snapshot_module_mock.perform_module_operation()
        snapshot_module_mock.provisioning.get_volume_group_details.assert_called()

    def test_get_nonexisting_vg_details(self, snapshot_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'snapshot_name': 'ansible_vg_snap',
            'volume_group': 'ansible_vg1',
            'desired_retention': '10',
            'retention_unit': 'days',
            'state': "present"
        })
        snapshot_module_mock.module.params = self.get_module_args
        snapshot_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            side_effect=MockApiException)
        snapshot_module_mock.perform_module_operation()
        snapshot_module_mock.provisioning.get_volume_group_by_name.assert_called()
