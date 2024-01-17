# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Snapshot rule module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_snapshotrule_api import MockSnapshotruleApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.snapshotrule import PowerstoreSnapshotrule


class TestPowerstoreSnapshotrule():

    get_module_args = MockSnapshotruleApi.SNAPSHOTRULE_COMMON_ARGS

    @pytest.fixture
    def snapshotrule_module_mock(self, mocker):
        mocker.patch(MockSnapshotruleApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        snapshotrule_module_mock = PowerstoreSnapshotrule()
        snapshotrule_module_mock.module = MagicMock()
        return snapshotrule_module_mock

    def test_get_snapshotrule_response(self, snapshotrule_module_mock):
        self.get_module_args.update({
            'snapshotrule_id': "49830e64-a342-42ae-8f55-2dff084522ca",
            'state': "present"
        })
        snapshotrule_module_mock.module.params = self.get_module_args
        snapshotrule_module_mock.perform_module_operation()
        snapshotrule_module_mock.protection.get_snapshot_rule_details.assert_called()

    def test_get_snapshotrule_response_name(self, snapshotrule_module_mock):
        self.get_module_args.update({
            'name': "snapshot_rule1",
            'state': "present"
        })
        snapshotrule_module_mock.module.params = self.get_module_args
        snapshotrule_module_mock.perform_module_operation()
        snapshotrule_module_mock.protection.get_snapshot_rule_by_name.assert_called()

    def test_create_snapshotrule_interval(self, snapshotrule_module_mock):
        self.get_module_args.update({
            'name': "snapshot_rule1",
            'interval': "One_Day",
            'desired_retention': 168,
            'days_of_week': ['Sunday'],
            'state': "present"
        })
        snapshotrule_module_mock.module.params = self.get_module_args
        snapshotrule_module_mock.get_snapshot_rule_details = MagicMock(return_value=(None, None))
        snapshotrule_module_mock.protection.get_snapshot_rule_details = MagicMock(
            return_value=MockSnapshotruleApi.SNAPSHOTRULE_DETAILS)
        snapshotrule_module_mock.perform_module_operation()
        assert snapshotrule_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_snapshotrule_time_of_day(self, snapshotrule_module_mock):
        self.get_module_args.update({
            'name': "snapshot_rule2",
            "time_of_day": "12:00",
            'desired_retention': 168,
            'days_of_week': ['Sunday'],
            'state': "present"
        })
        snapshotrule_module_mock.module.params = self.get_module_args
        snapshotrule_module_mock.get_snapshot_rule_details = MagicMock(return_value=(None, None))
        snapshotrule_module_mock.protection.get_snapshot_rule_details = MagicMock(
            return_value=MockSnapshotruleApi.SNAPSHOTRULE_DETAILS)
        snapshotrule_module_mock.perform_module_operation()
        assert snapshotrule_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_snapshotrule(self, snapshotrule_module_mock):
        self.get_module_args.update({
            'name': "snapshot_rule1",
            'new_name': "snapshot_rule1_renamed",
            'state': "present"
        })
        snapshotrule_module_mock.module.params = self.get_module_args
        snapshotrule_module_mock.get_snapshot_rule_details = MagicMock(return_value=(True, MockSnapshotruleApi.SNAPSHOTRULE_DETAILS))
        snapshotrule_module_mock.modify_snapshotrule_required = MagicMock(return_value=True)
        snapshotrule_module_mock.perform_module_operation()
        assert snapshotrule_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_delete_snapshotrule(self, snapshotrule_module_mock):
        self.get_module_args.update({
            'id': "46723735-13c1-4bab-bb72-cf3b4c0dcb9b",
            'state': "absent"
        })
        snapshotrule_module_mock.module.params = self.get_module_args
        snapshotrule_module_mock.get_snapshot_rule_details = MagicMock(return_value=(True, MockSnapshotruleApi.SNAPSHOTRULE_DETAILS))
        snapshotrule_module_mock.perform_module_operation()
        assert snapshotrule_module_mock.module.exit_json.call_args[1]['changed'] is True
