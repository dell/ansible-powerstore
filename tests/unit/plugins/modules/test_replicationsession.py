# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Replication session module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_replicationsession_api import MockReplicationSessionApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKResponse
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_powerstore_connection = MagicMock()
utils.PowerStoreException = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerstore.plugins.modules.replicationsession import PowerstoreReplicationSession


class TestPowerstoreReplicationSession():

    get_module_args = MockReplicationSessionApi.REPLICATION_SESSION_COMMON_ARGS

    @pytest.fixture
    def replicationsession_module_mock(self, mocker):
        mocker.patch(MockReplicationSessionApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        replicationsession_module_mock = PowerstoreReplicationSession()
        replicationsession_module_mock.module = MagicMock()
        return replicationsession_module_mock

    def test_get_replication_session_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS[0])
        replicationsession_module_mock.perform_module_operation()
        assert self.get_module_args['session_id'] == replicationsession_module_mock.module.exit_json.call_args[1]['replication_session_details']['id']
        replicationsession_module_mock.conn.protection.get_replication_session_details.assert_called()

    def test_get_replication_session_using_volume_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'volume': "sample_volume"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS[0])
        replicationsession_module_mock.protection.get_replication_sessions = MagicMock(
            return_value=MockReplicationSessionApi.SESSION_IDS_VOLUME)
        replicationsession_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockReplicationSessionApi.VOLUME_DETAILS)
        replicationsession_module_mock.provisioning.get_volume_details = MagicMock(
            return_value=MockReplicationSessionApi.VOLUME_DETAILS[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.get_replication_session_details.assert_called()

    def test_get_replication_session_using_volume_group_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'volume_group': "sample_volume_group"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_VG[1])
        replicationsession_module_mock.protection.get_replication_sessions = MagicMock(
            return_value=MockReplicationSessionApi.SESSION_IDS_VOLUME_GROUP)
        replicationsession_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            return_value=MockReplicationSessionApi.VOLUME_GROUP_DETAILS)
        replicationsession_module_mock.provisioning.get_volume_group_details = MagicMock(
            return_value=MockReplicationSessionApi.VOLUME_GROUP_DETAILS[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.get_replication_session_details.assert_called()

    def test_modify_from_ok_to_synchronizing_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "synchronizing"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.get_replication_session_details.assert_called()

    def test_modify_from_ok_to_paused_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "paused"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.pause_replication_session.assert_called()

    def test_modify_from_ok_to_failed_over_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "failed_over"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.failover_replication_session.assert_called()

    def test_modify_from_ok_to_failed_over_src_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "failed_over"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_SRC[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.failover_replication_session.assert_called()

    def test_modify_from_ok_to_failed_over_exception(self, replicationsession_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "failed_over"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS[0])
        replicationsession_module_mock.conn.protection.failover_replication_session = MagicMock(
            side_effect=MockApiException)
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.failover_replication_session.assert_called()

    def test_modify_from_sync_to_paused_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "paused"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_SYNC[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.pause_replication_session.assert_called()

    def test_modify_from_sync_to_synchronizing_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "synchronizing"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_SYNC[0])
        replicationsession_module_mock.perform_module_operation()
        assert replicationsession_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_modify_from_sync_to_paused_exception(self, replicationsession_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "paused"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_SYNC[0])
        replicationsession_module_mock.conn.protection.pause_replication_session = MagicMock(
            side_effect=MockApiException)
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.pause_replication_session.assert_called()

    def test_modify_from_sync_to_failed_over_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "failed_over"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_SYNC[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.failover_replication_session.assert_called()

    def test_modify_from_sync_to_failed_over_src_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "failed_over"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_SYNC_SRC[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.failover_replication_session.assert_called()

    def test_modify_from_paused_to_sync_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "synchronizing"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_PAUSED[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.sync_replication_session.assert_called()

    def test_modify_from_paused_to_paused_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "paused"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_PAUSED[0])
        replicationsession_module_mock.perform_module_operation()
        assert replicationsession_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_modify_from_paused_to_sync_dest_error(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "synchronizing"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_PAUSED_DES[0])
        replicationsession_module_mock.perform_module_operation()
        assert MockReplicationSessionApi.paused_to_sync_dest_error_failed_msg() in \
            replicationsession_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_from_paused_to_failed_over_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "failed_over"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_PAUSED[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.failover_replication_session.assert_called()

    def test_modify_from_paused_to_failed_over_des_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "failed_over"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_PAUSED_DES[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.failover_replication_session.assert_called()

    def test_modify_from_paused_to_failed_over_exception(self, replicationsession_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "failed_over"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_PAUSED[0])
        replicationsession_module_mock.conn.protection.failover_replication_session = MagicMock(
            side_effect=MockApiException)
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.failover_replication_session.assert_called()

    def test_modify_from_failing_over_to_sync_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "synchronizing"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILING_OVER[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.sync_replication_session.assert_called()

    def test_modify_from_failing_over_to_sync_exception(self, replicationsession_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "synchronizing"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILING_OVER[0])
        replicationsession_module_mock.conn.protection.sync_replication_session = MagicMock(
            side_effect=MockApiException)
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.sync_replication_session.assert_called()

    def test_modify_from_failing_over_to_paused_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "paused"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILING_OVER[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.pause_replication_session.assert_called()

    def test_modify_from_failing_over_to_failed_over_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "failed_over"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILING_OVER[0])
        replicationsession_module_mock.perform_module_operation()
        assert replicationsession_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_modify_from_failed_over_to_sync_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "synchronizing"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILED_OVER[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.sync_replication_session.assert_called()

    def test_modify_from_failed_over_to_failed_over_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "failed_over"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILED_OVER[0])
        replicationsession_module_mock.perform_module_operation()
        assert replicationsession_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_modify_from_failed_over_to_failed_over_des_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "failed_over"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILED_OVER_DES[0])
        replicationsession_module_mock.perform_module_operation()
        assert replicationsession_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_modify_from_failed_over_to_sync_destination_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "synchronizing"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILED_OVER_DES[0])
        replicationsession_module_mock.perform_module_operation()
        assert MockReplicationSessionApi.failed_over_to_sync_destination_failed_msg() in \
            replicationsession_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_from_failed_over_to_sync_exception(self, replicationsession_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "synchronizing"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILED_OVER[0])
        replicationsession_module_mock.conn.protection.sync_replication_session = MagicMock(
            side_effect=MockApiException)
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.sync_replication_session.assert_called()

    def test_modify_from_failed_over_to_paused_error(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "paused"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILED_OVER[0])
        replicationsession_module_mock.perform_module_operation()
        assert MockReplicationSessionApi.failed_over_to_paused_failed_msg() in \
            replicationsession_module_mock.module.fail_json.call_args[1]['msg']

    def test_change_state_from_transitioning_states_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "paused"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_RESUMING[0])
        replicationsession_module_mock.perform_module_operation()
        assert MockReplicationSessionApi.change_state_from_transitioning_states_failed_msg() in \
            replicationsession_module_mock.module.fail_json.call_args[1]['msg']

    def test_change_state_from_remaining_states_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc",
            'session_state': "paused"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_SYSTEM_PAUSED[0])
        replicationsession_module_mock.perform_module_operation()
        assert MockReplicationSessionApi.change_state_from_remaining_states_failed_msg() in \
            replicationsession_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_replication_session_multi_cluster(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': "b05b5108-26b6-4567-a1d8-1c7795b2e6bc"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS[0])
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.perform_module_operation()
        assert self.get_module_args['session_id'] == replicationsession_module_mock.module.exit_json.call_args[1]['replication_session_details']['id']
        replicationsession_module_mock.conn.protection.get_replication_session_details.assert_called()
