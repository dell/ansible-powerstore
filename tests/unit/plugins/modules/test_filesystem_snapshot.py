# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Filesystem Snapshot module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_filesystem_snapshot_api import MockFilesystemSnapshotApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_powerstore_connection = MagicMock()
utils.PowerStoreException = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerstore.plugins.modules.filesystem_snapshot import PowerStoreFilesystemSnapshot


class TestPowerstoreFilesystemSnapshot():

    get_module_args = MockFilesystemSnapshotApi.FILESYSTEM_SNAPSHOT_COMMON_ARGS

    @pytest.fixture
    def filesystem_snapshot_module_mock(self, mocker):
        mocker.patch(MockFilesystemSnapshotApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        filesystem_snapshot_module_mock = PowerStoreFilesystemSnapshot()
        filesystem_snapshot_module_mock.module = MagicMock()
        return filesystem_snapshot_module_mock

    def test_get_filesystem_snapshot_by_id(self, filesystem_snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_id': "61e49f3f-9b57-e69b-1038-aa02b52a030f",
            'state': "present"
        })
        filesystem_snapshot_module_mock.module.params = self.get_module_args
        filesystem_snapshot_module_mock.protection.get_filesystem_snapshot_details = MagicMock(
            return_value=MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0])
        filesystem_snapshot_module_mock.perform_module_operation()
        assert self.get_module_args['snapshot_id'] == filesystem_snapshot_module_mock.module.exit_json.call_args[1]['filesystem_snap_details']['id']

    def test_get_filesystem_snapshot_by_name(self, filesystem_snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': "Sample_FS_Snapshot",
            'filesystem': 'sample-filesystem',
            'nas_server': 'ansible_nas_server_2',
            'state': "present"
        })
        filesystem_snapshot_module_mock.module.params = self.get_module_args
        filesystem_snapshot_module_mock.protection.get_filesystem_snapshot_details_by_name = MagicMock(
            return_value=MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS)
        filesystem_snapshot_module_mock.protection.get_filesystem_snapshot_details = MagicMock(
            return_value=MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0])
        filesystem_snapshot_module_mock.perform_module_operation()
        assert self.get_module_args['snapshot_name'] == filesystem_snapshot_module_mock.module.exit_json.call_args[1]['filesystem_snap_details']['name']
        filesystem_snapshot_module_mock.protection.get_filesystem_snapshot_details_by_name.assert_called()

    def test_get_filesystem_snapshot_without_nas(self, filesystem_snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': "Sample_FS_Snapshot",
            'state': "present"
        })
        filesystem_snapshot_module_mock.module.params = self.get_module_args
        filesystem_snapshot_module_mock.protection.get_filesystem_snapshot_details_by_name = MagicMock(
            return_value=MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS)
        filesystem_snapshot_module_mock.protection.get_filesystem_snapshot_details = MagicMock(
            return_value=MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0])
        filesystem_snapshot_module_mock.perform_module_operation()
        assert MockFilesystemSnapshotApi.get_fs_snapshot_without_nas_failed_msg() in filesystem_snapshot_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_filesystem_snapshot(self, filesystem_snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': "Sample_FS_Snapshot_1",
            'filesystem': 'sample-filesystem',
            'nas_server': 'ansible_nas_server_2',
            'desired_retention': 20,
            'retention_unit': 'days',
            'access_type': 'PROTOCOL',
            'state': "present"
        })
        filesystem_snapshot_module_mock.module.params = self.get_module_args
        filesystem_snapshot_module_mock.protection.get_filesystem_snapshot_details_by_name = MagicMock(
            return_value=None)
        filesystem_snapshot_module_mock.protection.create_filesystem_snapshot = MagicMock(
            return_value=True)
        filesystem_snapshot_module_mock.get_fs_snapshot = MagicMock(
            return_value=MockFilesystemSnapshotApi.CREATE_FS_SNAPSHOT[0])
        filesystem_snapshot_module_mock.perform_module_operation()
        assert filesystem_snapshot_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_filesystem_snapshot(self, filesystem_snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': "Sample_FS_Snapshot",
            'nas_server': 'ansible_nas_server_2',
            'description': 'Modify',
            'state': "present"
        })
        filesystem_snapshot_module_mock.module.params = self.get_module_args
        filesystem_snapshot_module_mock.protection.get_filesystem_snapshot_details_by_name = MagicMock(
            return_value=MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0])
        filesystem_snapshot_module_mock.protection.modify_filesystem_snapshot = MagicMock(
            return_value=MockFilesystemSnapshotApi.MODIFY_FS_SNAPSHOT[0])
        filesystem_snapshot_module_mock.perform_module_operation()
        assert filesystem_snapshot_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_delete_filesystem_snapshot(self, filesystem_snapshot_module_mock):
        self.get_module_args.update({
            'snapshot_name': "Sample_FS_Snapshot",
            'nas_server': 'ansible_nas_server_2',
            'state': "absent"
        })
        filesystem_snapshot_module_mock.module.params = self.get_module_args
        filesystem_snapshot_module_mock.protection.get_filesystem_snapshot_details_by_name = MagicMock(
            return_value=MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS)
        filesystem_snapshot_module_mock.perform_module_operation()
        filesystem_snapshot_module_mock.protection.delete_filesystem_snapshot.assert_called()
        assert filesystem_snapshot_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_filesystem_snapshot_with_exception(self, filesystem_snapshot_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'snapshot_id': "61e49f3f-9b57-e69b-1038-aa02b52a030f",
            'description': 'Modify',
            'state': "present"
        })
        filesystem_snapshot_module_mock.module.params = self.get_module_args
        filesystem_snapshot_module_mock.protection.get_filesystem_snapshot_details = MagicMock(
            return_value=MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0])
        filesystem_snapshot_module_mock.protection.modify_filesystem_snapshot = MagicMock(
            side_effect=MockApiException)
        filesystem_snapshot_module_mock.perform_module_operation()
        filesystem_snapshot_module_mock.protection.modify_filesystem_snapshot.assert_called()

    def test_delete_filesystem_snapshot_with_exception(self, filesystem_snapshot_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'snapshot_id': "61e49f3f-9b57-e69b-1038-aa02b52a030f",
            'state': "absent"
        })
        filesystem_snapshot_module_mock.module.params = self.get_module_args
        filesystem_snapshot_module_mock.protection.get_filesystem_snapshot_details = MagicMock(
            return_value=MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0])
        filesystem_snapshot_module_mock.protection.delete_filesystem_snapshot = MagicMock(
            side_effect=MockApiException)
        filesystem_snapshot_module_mock.perform_module_operation()
        filesystem_snapshot_module_mock.protection.delete_filesystem_snapshot.assert_called()
