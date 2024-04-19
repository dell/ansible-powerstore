# Copyright: (c) 2024, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Filesystem Snapshot module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_filesystem_snapshot_api import MockFilesystemSnapshotApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.filesystem_snapshot import PowerStoreFilesystemSnapshot, main
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries.powerstore_unit_base \
    import PowerStoreUnitBase


class TestPowerstoreFilesystemSnapshot(PowerStoreUnitBase):

    get_module_args = MockFilesystemSnapshotApi.FILESYSTEM_SNAPSHOT_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerStoreFilesystemSnapshot

    def test_validate_expiration_timestamp(self, powerstore_module_mock):
        expiration_timestamp = "2022-02-02T02:02:02Z"
        ret = powerstore_module_mock.validate_expiration_timestamp(
            expiration_timestamp)
        assert ret is None

    def test_validate_expiration_timestamp_error(self, powerstore_module_mock):
        expiration_timestamp = "2-02-02T02:02:02Z"
        self.capture_fail_json_method(
            MockFilesystemSnapshotApi.get_error_message("vet"),
            powerstore_module_mock, "validate_expiration_timestamp",
            expiration_timestamp)

    def test_validate_desired_retention(self, powerstore_module_mock):
        desired_retention = 740
        retention_unit = "hours"
        ret = powerstore_module_mock.validate_desired_retention(
            desired_retention, retention_unit)
        assert ret is None

    @pytest.mark.parametrize("params", [
        {"error_key": "vdr_err1", "retention_unit": "hours"},
        {"error_key": "vdr_err2", "retention_unit": "days"}
    ])
    def test_validate_desired_retention_exception(self, powerstore_module_mock, params):
        desired_retention = 750
        retention_unit = params.get("retention_unit", None)
        self.capture_fail_json_method(
            MockFilesystemSnapshotApi.get_error_message(
                params.get("error_key", None)
            ),
            powerstore_module_mock, "validate_desired_retention",
            desired_retention, retention_unit)

    @pytest.mark.parametrize("params", [
        {"nas_server_name": "nas_server_name"},
        {"nas_server_id": "nas_server_id"}
    ])
    def test_get_nas_server(self, powerstore_module_mock, params):
        nas_server_name = params.get("nas_server_name", None)
        nas_server_id = params.get("nas_server_id", None)
        ret_val = MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS
        if nas_server_id:
            ret_val = MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0]
        powerstore_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=ret_val)
        powerstore_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=ret_val)
        ret = powerstore_module_mock.get_nas_server(
            nas_server_name, nas_server_id)
        assert ret == MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0]['id']

    def test_get_nas_server_exp(self, powerstore_module_mock):
        ret_val = None
        powerstore_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=ret_val)
        self.capture_fail_json_method(
            MockFilesystemSnapshotApi.get_error_message("nse_err1"),
            powerstore_module_mock, "get_nas_server",
            "nas_server_name")

    @pytest.mark.parametrize("params", [
        {"nas_server": "sample_nas_server"},
        {"nas_server": "61e4947b-8992-3db7-2859-aa02b52a0308"},
    ])
    def test_get_fs_id_from_filesystem_name(self, powerstore_module_mock, params):
        filesystem = "sample_filesystem"
        nas_server = params.get("nas_server", None)
        powerstore_module_mock.get_nas_server = MagicMock(
            return_value=MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0]['id']
        )
        powerstore_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=[
                {"id": MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0]['id']}]
        )
        ret = powerstore_module_mock.get_fs_id_from_filesystem(
            filesystem, nas_server)
        assert ret == MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0]['id']

    def test_get_fs_id_from_filesystem_uid(self, powerstore_module_mock):
        filesystem = "61e4947b-8992-3db7-2859-aa02b52a0308"
        nas_server = "61e4947b-8992-3db7-2859-aa02b52a0308"
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value={
                "id": MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0]['id']}
        )
        ret = powerstore_module_mock.get_fs_id_from_filesystem(
            filesystem, nas_server)
        assert ret == MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0]['id']

    @pytest.mark.parametrize("params", [
        {"nas_server": "sample_nas_server", "error_key": "nfe_err1"},
        {"nas_server": None, "error_key": "nfe_err2"}
    ])
    def test_get_fs_id_from_filesystem_name_exp(self, powerstore_module_mock, params):
        filesystem = "sample_filesystem"
        nas_server = params.get("nas_server", None)
        powerstore_module_mock.get_nas_server = MagicMock(
            return_value=MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0]['id']
        )
        powerstore_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=None
        )
        self.capture_fail_json_method(
            MockFilesystemSnapshotApi.get_error_message(
                params.get("error_key")),
            powerstore_module_mock, "get_fs_id_from_filesystem",
            filesystem, nas_server
        )

    def test_get_fs_name(self, powerstore_module_mock):
        filesystem_id = "61e4947b-8992-3db7-2859-aa02b52a0308"
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0]
        )
        ret = powerstore_module_mock.get_fs_name(filesystem_id)
        assert ret == MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0]['name']

    def test_get_fs_name_exp(self, powerstore_module_mock):
        filesystem_id = "61e4947b-8992-3db7-2859-aa02b52a0308"
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockApiException()
        )
        self.capture_fail_json_method(
            MockFilesystemSnapshotApi.get_error_message("fs_name_exp"),
            powerstore_module_mock, "get_fs_name",
            filesystem_id
        )

    @pytest.mark.parametrize("params", [
        {"snapshot_name": "sample_snapshot",
         "nas_server": "nas_server",
         "sn_details": MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS,
         "nas_server_id": "nas_server_id",
         "ret_val": MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0]},
        {"snapshot_name": "sample_snapshot",
         "nas_server": "61e4947b-8992-3db7-2859-aa02b52a0308"},
        {"filesystem_id": "61e4947b-8992-3db7-2859-aa02b52a0308",
         "nas_server": "nas_server",
         "sn_details": MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS,
         "nas_server_id": "nas_server_id",
         "ret_val": MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0]},
    ])
    def test_get_fs_snapshot(self, powerstore_module_mock, params):
        snapshot_name = params.get("snapshot_name", None)
        snapshot_id = "61e4947b-8992-3db7-2859-aa02b52a0302"
        filesystem_id = "61e4947b-8992-3db7-2859-aa02b52a0308"
        nas_server = params.get("nas_server", None)
        powerstore_module_mock.get_nas_server = MagicMock(
            return_value=params.get("nas_server_id")
        )
        powerstore_module_mock.protection.get_filesystem_snapshot_details_by_name = MagicMock(
            return_value=params.get("sn_details")
        )
        powerstore_module_mock.protection.get_filesystem_snapshot_details = MagicMock(
            return_value=MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0]
        )
        powerstore_module_mock.get_fs_name = MagicMock(
            return_value=MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS[0]['parent_name']
        )
        ret = powerstore_module_mock.get_fs_snapshot(snapshot_name, snapshot_id,
                                                     filesystem_id, nas_server)
        assert ret == params.get("ret_val")

    def test_get_fs_snapshot_exp1(self, powerstore_module_mock):
        snapshot_name = "sample_snapshot"
        snapshot_id = None
        filesystem_id = None
        nas_server = None
        self.capture_fail_json_method(
            MockFilesystemSnapshotApi.get_error_message("fs_snap_exp1"),
            powerstore_module_mock, "get_fs_snapshot",
            snapshot_name, snapshot_id, filesystem_id, nas_server
        )

    def test_get_fs_snapshot_exp2(self, powerstore_module_mock):
        snapshot_name = "sample_snapshot"
        snapshot_id = None
        filesystem_id = "61e4947b-8992-3db7-2859-aa02b52a0318"
        nas_server = "nas_server"
        powerstore_module_mock.get_nas_server = MagicMock(
            return_value="nas_server_id"
        )
        powerstore_module_mock.protection.get_filesystem_snapshot_details_by_name = MagicMock(
            return_value=MockFilesystemSnapshotApi.FILESYSTEM_SNAP_DETAILS
        )
        self.capture_fail_json_method(
            MockFilesystemSnapshotApi.get_error_message("fs_snap_exp2"),
            powerstore_module_mock, "get_fs_snapshot",
            snapshot_name, snapshot_id, filesystem_id, nas_server
        )

    def test_get_fs_snapshot_exp3(self, powerstore_module_mock):
        snapshot_name = None
        snapshot_id = "61e4947b-8992-3db7-2859-aa02b52a0302"
        filesystem_id = "61e4947b-8992-3db7-2859-aa02b52a0318"
        nas_server = "nas_server"
        powerstore_module_mock.get_nas_server = MagicMock(
            return_value="nas_server_id"
        )
        powerstore_module_mock.protection.get_filesystem_snapshot_details = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockFilesystemSnapshotApi.get_error_message("fs_snap_exp3"),
            powerstore_module_mock, "get_fs_snapshot",
            snapshot_name, snapshot_id, filesystem_id, nas_server
        )

    def test_create_filesystem_snapshot(self, powerstore_module_mock):
        filesystem_id = "61e4947b-8992-3db7-2859-aa02b52a0308"
        snapshot_name = "sample_snapshot"
        description = "sample_description"
        expiration_timestamp = 0
        access_type = "SNAPSHOT"
        nas_server = "nas_server"
        powerstore_module_mock.protection.create_filesystem_snapshot = MagicMock(
            return_value=None
        )
        ret = powerstore_module_mock.create_filesystem_snapshot(
            filesystem_id, snapshot_name, description, expiration_timestamp,
            access_type, nas_server
        )
        assert ret is True

    @pytest.mark.parametrize("params", [
        {"filesystem_id": "61e4947b-8992-3db7-2859-aa02b52a0308",
         "ret_value": "create_exp1",
         "access_type": "SNAPSHOT", },
        {"snapshot_name": "sample_snapshot",
         "ret_value": "create_exp2",
         "access_type": "SNAPSHOT"},
        {"filesystem_id": "61e4947b-8992-3db7-2859-aa02b52a0308",
         "snapshot_name": "sample_snapshot",
         "ret_value": "create_exp3"},

    ])
    def test_create_filesystem_snapshot_exp(self, powerstore_module_mock, params):
        filesystem_id = params.get("filesystem_id", None)
        snapshot_name = params.get("snapshot_name", None)
        description = "sample_description"
        expiration_timestamp = 0
        access_type = params.get("access_type", None)
        nas_server = "nas_server"
        powerstore_module_mock.protection.create_filesystem_snapshot = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockFilesystemSnapshotApi.get_error_message(
                params.get("ret_value")),
            powerstore_module_mock, "create_filesystem_snapshot",
            filesystem_id, snapshot_name, description, expiration_timestamp,
            access_type, nas_server
        )

    @pytest.mark.parametrize("params", [
        {"creation_timestamp": "2021-10-26T10:01:33.000Z",
         "expiration_timestamp": "2021-11-26T10:01:33.000Z",
         "retention_unit": "days",
         "desired_retention": 1,
         "ret_value": {
             'description': 'sample_description',
             'expiration_timestamp': '2021-10-27T10:01:00Z'}
         },
        {"creation_timestamp": "2021-09-26T10:01:33.000Z",
         "expiration_timestamp": "2021-08-26T10:01:33.000Z",
         "retention_unit": "hours",
         "desired_retention": 1,
         "ret_value": {
             'description': 'sample_description',
             'expiration_timestamp': '2021-09-26T11:01:00Z'}
         },
        {
            "retention_unit": "hours",
            "expiration_timestamp_param": "2021-07-26T10:01:33.000Z",
            "ret_value": {
                'description': 'sample_description',
                'expiration_timestamp': '2021-07-26T10:01:33.000Z'}
        },
        {
            "retention_unit": "hours",
            "expiration_timestamp": "2021-07-26T10:01:33.000Z",
            "expiration_timestamp_param": "",
            "ret_value": {
                'description': 'sample_description',
                'expiration_timestamp': '1970-01-01T00:00:00.000Z'}
        },
    ])
    def test_check_fs_snapshot_modified(self, powerstore_module_mock, params):
        snapshot = {
            "expiration_timestamp": params.get("expiration_timestamp", None),
            "access_type": "Snapshot",
            "description": "sample_description1",
        }
        if params.get("creation_timestamp", None):
            snapshot["creation_timestamp"] = params.get("creation_timestamp")
        filesystem_id = "61e4947b-8992-3db7-2859-aa02b52a0308"
        description = "sample_description"
        desired_retention = params.get("desired_retention", None)
        retention_unit = params.get("retention_unit", None)
        expiration_timestamp = params.get("expiration_timestamp_param", None)
        access_type = "SNAPSHOT"
        nas_server = "nas_server"
        ret = powerstore_module_mock.check_fs_snapshot_modified(
            snapshot, filesystem_id, description, desired_retention,
            retention_unit, expiration_timestamp, access_type, nas_server
        )
        assert ret == params.get("ret_value")

    def test_check_fs_snapshot_modified_exp(self, powerstore_module_mock):
        snapshot = {
            "access_type": "SNAPSHOT",
        }
        filesystem_id = None
        description = None
        desired_retention = None
        retention_unit = None
        expiration_timestamp = None
        access_type = "SNAPSHOT"
        nas_server = None
        self.capture_fail_json_method(
            MockFilesystemSnapshotApi.get_error_message("fs_snap_mod_exp1"),
            powerstore_module_mock, "check_fs_snapshot_modified",
            snapshot, filesystem_id, description, desired_retention,
            retention_unit, expiration_timestamp, access_type, nas_server
        )

    def test_modify_filesystem_snapshot(self, powerstore_module_mock):
        snapshot = {"id": "61e4947b-8992-3db7-2859-aa02b52a0308"}
        fs_snapshot_dict = {}
        powerstore_module_mock.protection.modify_filesystem_snapshot = MagicMock(
            return_value=None
        )
        ret = powerstore_module_mock.modify_filesystem_snapshot(
            snapshot, fs_snapshot_dict)
        assert ret is True

    def test_modify_filesystem_snapsho_exp(self, powerstore_module_mock):
        snapshot = {
            "id": "61e4947b-8992-3db7-2859-aa02b52a0308", "name": "Name"}
        fs_snapshot_dict = {}
        powerstore_module_mock.protection.modify_filesystem_snapshot = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockFilesystemSnapshotApi.get_error_message("mod_fs_snapshot"),
            powerstore_module_mock, "modify_filesystem_snapshot",
            snapshot, fs_snapshot_dict
        )

    def test_delete_filesystem_snapshot(self, powerstore_module_mock):
        snapshot = {"id": "61e4947b-8992-3db7-2859-aa02b52a0308"}
        powerstore_module_mock.protection.delete_filesystem_snapshot = MagicMock(
            return_value=None
        )
        ret = powerstore_module_mock.delete_filesystem_snapshot(snapshot)
        assert ret is True

    def test_delete_filesystem_snapshot_exp(self, powerstore_module_mock):
        snapshot = {
            "id": "61e4947b-8992-3db7-2859-aa02b52a0308", "name": "Name"}
        powerstore_module_mock.protection.delete_filesystem_snapshot = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockFilesystemSnapshotApi.get_error_message("del_fs_snapshot"),
            powerstore_module_mock, "delete_filesystem_snapshot",
            snapshot
        )

    @pytest.mark.parametrize("params", [
        {
            "expiration_timestamp": "2021-07-26T10:01:33.000Z",
            "desired_retention": "1",
            "filesystem": "fileSystem",
            "state": "present",
            "get_fs_snapshot": {"id": "61e4947b-8992-3db7-2859-aa02b52a0308"},
            "ret_val": {'changed': True, 'create_fs_snap': '',
                        'modify_fs_snap': True, 'delete_fs_snap': '',
                        'filesystem_snap_details':
                        {'id': '61e4947b-8992-3db7-2859-aa02b52a0308'}}
        },
        {
            "expiration_timestamp": "2021-07-26T10:01:33.000Z",
            "desired_retention": "1",
            "filesystem": "fileSystem",
            "state": "present",
            "ret_val": {'changed': True,
                        'create_fs_snap':
                        {"id": "61e4947b-8992-3db7-2859-aa02b52a0308"},
                        'modify_fs_snap': '', 'delete_fs_snap': '',
                        'filesystem_snap_details': None}
        },
        {
            "state": "absent",
            "get_fs_snapshot": {"id": "61e4947b-8992-3db7-2859-aa02b52a0308"},
            "ret_val": {'changed': True, 'create_fs_snap': '',
                        'modify_fs_snap': '', 'delete_fs_snap': True,
                        'filesystem_snap_details': ''}
        },
    ])
    def test_perform_module_operation(self, powerstore_module_mock, params):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {"expiration_timestamp": params.get("expiration_timestamp", None),
             "desired_retention": params.get("desired_retention", None),
             "filesystem": params.get("filesystem", None),
             "state": params.get("state", None),
             }
        )
        powerstore_module_mock.validate_expiration_timestamp = MagicMock(
            return_value=None
        )
        powerstore_module_mock.validate_desired_retention = MagicMock(
            return_value=None
        )
        powerstore_module_mock.get_fs_id_from_filesystem = MagicMock(
            return_value="61e4947b-8992-3db7-2859-aa02b52a0308"
        )
        powerstore_module_mock.get_fs_snapshot = MagicMock(
            return_value=params.get("get_fs_snapshot", None)
        )
        powerstore_module_mock.check_fs_snapshot_modified = MagicMock(
            return_value=params.get("get_fs_snapshot", None)
        )
        powerstore_module_mock.create_filesystem_snapshot = MagicMock(
            return_value={"id": "61e4947b-8992-3db7-2859-aa02b52a0308"}
        )
        powerstore_module_mock.delete_filesystem_snapshot = MagicMock(
            return_value=True
        )
        powerstore_module_mock.perform_module_operation()
        assert powerstore_module_mock.module.exit_json.call_args[1] == params.get("ret_val")

    def test_main(self, powerstore_module_mock, mocker):

        mock_obj = mocker.patch(MockFilesystemSnapshotApi.MODULE_PATH,
                                new=PowerStoreFilesystemSnapshot)
        mock_obj.perform_module_operation = MagicMock(
            return_value=None)
        main()
