# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Replication session module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_replicationsession_api import MockReplicationSessionApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.replicationsession\
    import PowerstoreReplicationSession
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries.\
    fail_json import FailJsonException, fail_json


class TestPowerstoreReplicationSession():

    get_module_args = MockReplicationSessionApi.REPLICATION_SESSION_COMMON_ARGS

    @pytest.fixture
    def replicationsession_module_mock(self, mocker):
        mocker.patch(MockReplicationSessionApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        replicationsession_module_mock = PowerstoreReplicationSession()
        replicationsession_module_mock.module = MagicMock()
        replicationsession_module_mock.module.fail_json = fail_json
        return replicationsession_module_mock

    def capture_fail_json_call(self, error_msg, replicationsession_module_mock):
        try:
            replicationsession_module_mock.perform_module_operation()
        except FailJsonException as fj_object:
            assert error_msg in fj_object.message

    def test_get_replication_session_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS[0])
        replicationsession_module_mock.perform_module_operation()
        assert self.get_module_args['session_id'] == \
               replicationsession_module_mock.module.exit_json.call_args[1][
                   'replication_session_details']['id']
        replicationsession_module_mock.conn.protection.get_replication_session_details.assert_called()

    def test_get_replication_session_using_volume_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'volume': "sample_volume"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
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

    def test_get_replication_session_using_volume_id_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'volume': "634e4b95-e7bd-49e7-957b-6dc932642464"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS[0])
        replicationsession_module_mock.protection.get_replication_sessions = MagicMock(
            return_value=MockReplicationSessionApi.SESSION_IDS_VOLUME)
        replicationsession_module_mock.provisioning.get_volume_details = MagicMock(
            return_value=MockReplicationSessionApi.VOLUME_DETAILS[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.get_replication_session_details.assert_called()

    def test_get_replication_session_using_volume_not_found_response(self, replicationsession_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'volume': "634e4b95-e7bd-49e7-957b-6dc932642464"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS[0])
        replicationsession_module_mock.protection.get_replication_sessions = MagicMock(
            return_value=MockReplicationSessionApi.SESSION_IDS_VOLUME)
        replicationsession_module_mock.provisioning.get_volume_details = MagicMock(
            side_effect=MockApiException)
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.provisioning.get_volume_details.assert_called()

    def test_get_replication_session_using_volume_group_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'volume_group': "sample_volume_group"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
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

    def test_get_replication_session_using_nas_server_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'nas_server': "sample_nas_server"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_NAS_SERVER[0])
        replicationsession_module_mock.protection.get_replication_sessions = MagicMock(
            return_value=MockReplicationSessionApi.SESSION_IDS_NAS_SERVER)
        replicationsession_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockReplicationSessionApi.NAS_SERVER_DETAILS)
        replicationsession_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockReplicationSessionApi.NAS_SERVER_DETAILS[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.get_replication_session_details.assert_called()

    def test_get_replication_session_using_filesystem_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'filesystem': MockReplicationSessionApi.FS_NAME
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockReplicationSessionApi.FILESYSTEM_DETAILS)
        replicationsession_module_mock.protection.get_replication_sessions = MagicMock(
            return_value=MockReplicationSessionApi.SESSION_IDS_FILESYSTEM)
        replicationsession_module_mock.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FILESYSTEM[0])
        replicationsession_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockReplicationSessionApi.FILESYSTEM_DETAILS[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.get_replication_session_details.assert_called()

    def test_modify_from_ok_to_synchronizing_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.SYNCING_STATE
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.get_replication_session_details.assert_called()

    def test_modify_from_ok_to_paused_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.PAUSE_STATE
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.pause_replication_session.assert_called()

    def test_modify_from_ok_to_failed_over_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.FAIL_OVER
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.failover_replication_session.assert_called()

    def test_modify_from_ok_to_failed_over_src_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.FAIL_OVER
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_SRC[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.failover_replication_session.assert_called()

    def test_modify_from_ok_to_failed_over_exception(self, replicationsession_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.FAIL_OVER
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS[0])
        replicationsession_module_mock.conn.protection.failover_replication_session = MagicMock(
            side_effect=MockApiException)
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.failover_replication_session.assert_called()

    def test_modify_from_sync_to_paused_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.PAUSE_STATE
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_SYNC[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.pause_replication_session.assert_called()

    def test_modify_from_sync_to_synchronizing_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.SYNCING_STATE
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_SYNC[0])
        replicationsession_module_mock.perform_module_operation()
        assert replicationsession_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_modify_from_sync_to_paused_exception(self, replicationsession_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.PAUSE_STATE
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_SYNC[0])
        replicationsession_module_mock.conn.protection.pause_replication_session = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockReplicationSessionApi.get_rep_session_exception_response(
                'get_rep_session_exception'), replicationsession_module_mock)

    def test_modify_from_sync_to_failed_over_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.FAIL_OVER
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_SYNC[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.failover_replication_session.assert_called()

    def test_modify_from_sync_to_failed_over_src_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.FAIL_OVER
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_SYNC_SRC[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.failover_replication_session.assert_called()

    def test_modify_from_paused_to_sync_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.SYNCING_STATE
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_PAUSED[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.sync_replication_session.assert_called()

    def test_modify_from_paused_to_paused_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.PAUSE_STATE
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_PAUSED[0])
        replicationsession_module_mock.perform_module_operation()
        assert replicationsession_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_modify_from_paused_to_sync_dest_error(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.SYNCING_STATE
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_PAUSED_DES[0])
        self.capture_fail_json_call(
            MockReplicationSessionApi.get_rep_session_exception_response(
                'pause_to_sync_dest_error'), replicationsession_module_mock)

    def test_modify_from_paused_to_failed_over_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.FAIL_OVER
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_PAUSED[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.failover_replication_session.assert_called()

    def test_modify_from_paused_to_failed_over_des_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.FAIL_OVER
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_PAUSED_DES[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.failover_replication_session.assert_called()

    def test_modify_from_paused_to_failed_over_exception(self, replicationsession_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.FAIL_OVER
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_PAUSED[0])
        replicationsession_module_mock.conn.protection.failover_replication_session = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockReplicationSessionApi.get_rep_session_exception_response(
                'get_rep_session_exception'), replicationsession_module_mock)

    def test_modify_from_failing_over_to_sync_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.SYNCING_STATE
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILING_OVER[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.sync_replication_session.assert_called()

    def test_modify_from_failing_over_to_sync_exception(self, replicationsession_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.SYNCING_STATE
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILING_OVER[0])
        replicationsession_module_mock.conn.protection.sync_replication_session = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockReplicationSessionApi.get_rep_session_exception_response(
                'get_rep_session_exception'), replicationsession_module_mock)

    def test_modify_from_failing_over_to_paused_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.PAUSE_STATE
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILING_OVER[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.pause_replication_session.assert_called()

    def test_modify_from_failing_over_to_failed_over_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.FAIL_OVER
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILING_OVER[0])
        replicationsession_module_mock.perform_module_operation()
        assert replicationsession_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_modify_from_failed_over_to_sync_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.SYNCING_STATE
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILED_OVER[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.sync_replication_session.assert_called()

    def test_modify_from_failed_over_to_failed_over_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.FAIL_OVER
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILED_OVER[0])
        replicationsession_module_mock.perform_module_operation()
        assert replicationsession_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_modify_from_failed_over_to_failed_over_des_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.FAIL_OVER
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILED_OVER_DES[0])
        replicationsession_module_mock.perform_module_operation()
        assert replicationsession_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_modify_from_failed_over_to_sync_destination_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.SYNCING_STATE
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILED_OVER_DES[0])
        self.capture_fail_json_call(
            MockReplicationSessionApi.get_rep_session_exception_response(
                'failover_to_sync_destination_error'), replicationsession_module_mock)

    def test_modify_from_failed_over_to_sync_exception(self, replicationsession_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.SYNCING_STATE
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILED_OVER[0])
        replicationsession_module_mock.conn.protection.sync_replication_session = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockReplicationSessionApi.get_rep_session_exception_response(
            'get_rep_session_exception'), replicationsession_module_mock)

    def test_modify_from_failed_over_to_paused_error(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.PAUSE_STATE
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FAILED_OVER[0])
        self.capture_fail_json_call(
            MockReplicationSessionApi.get_rep_session_exception_response(
                'failOver_to_paused_error'), replicationsession_module_mock)

    def test_change_state_from_transitioning_states_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.PAUSE_STATE
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_RESUMING[0])
        self.capture_fail_json_call(
            MockReplicationSessionApi.get_rep_session_exception_response(
                'state_from_transition_state'), replicationsession_module_mock)

    def test_change_state_from_remaining_states_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.PAUSE_STATE
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_SYSTEM_PAUSED[0])
        self.capture_fail_json_call(
            MockReplicationSessionApi.get_rep_session_exception_response(
                'any_to_remaining_state'), replicationsession_module_mock)

    def test_modify_role_replication_session(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'role': "Metro_Preferred"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS[0])
        replicationsession_module_mock.perform_module_operation()
        assert replicationsession_module_mock.module.exit_json.call_args[1]['changed'] is True
        replicationsession_module_mock.conn.protection.modify_replication_session.assert_called()

    def test_modify_metro_paused_to_sync_response(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.SYNCING_STATE
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.METRO_SESSION_DETAILS_PAUSED[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.resume_replication_session.assert_called()

    def test_modify_role_replication_session_exception(self, replicationsession_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'role': "Metro_Preferred"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS[0])
        replicationsession_module_mock.conn.protection.modify_replication_session = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockReplicationSessionApi.get_rep_session_exception_response(
            'get_rep_session_exception'), replicationsession_module_mock)

    def test_replication_session_with_repl_group(self, replicationsession_module_mock):
        self.get_module_args.update({
            'replication_group': MockReplicationSessionApi.REP_GROUP})
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.protection.get_replication_group_details_by_name = MagicMock(
            return_value=MockReplicationSessionApi.REP_GROUP_DETAILS)
        replicationsession_module_mock.protection.get_replication_sessions = MagicMock(
            return_value=MockReplicationSessionApi.SESSION_IDS_REP_GROUP)
        replicationsession_module_mock.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_REP_GROUP[0])
        replicationsession_module_mock.protection.get_replication_group_details = MagicMock(
            return_value=MockReplicationSessionApi.REP_GROUP_DETAILS[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.get_replication_session_details.assert_called()

    def test_replication_session_with_repl_group_id(self, replicationsession_module_mock):
        self.get_module_args.update({
            'replication_group': MockReplicationSessionApi.REP_GROUP})
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.protection.get_replication_sessions = MagicMock(
            return_value=MockReplicationSessionApi.SESSION_IDS_REP_GROUP)
        replicationsession_module_mock.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_REP_GROUP[0])
        replicationsession_module_mock.protection.get_replication_group_details = MagicMock(
            return_value=MockReplicationSessionApi.REP_GROUP_DETAILS[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.get_replication_session_details.assert_called()

    def test_get_replication_session_exception(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockReplicationSessionApi.get_rep_session_exception_response(
            'get_rep_session_error'), replicationsession_module_mock)

    def test_get_replication_session_rep_group_exception(self, replicationsession_module_mock):
        self.get_module_args.update({
            'replication_group': MockReplicationSessionApi.REP_GROUP,
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.protection.get_replication_group_details_by_name = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockReplicationSessionApi.get_rep_session_error(
            'get_rep_group_error'), replicationsession_module_mock)

    def test_cluster_exception(self, replicationsession_module_mock):
        self.get_module_args.update({
            'replication_group': MockReplicationSessionApi.REP_GROUP,
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockReplicationSessionApi.get_rep_session_error(
            'get_cluster_error'), replicationsession_module_mock)

    def test_get_replication_session_nas_exception(self, replicationsession_module_mock):
        self.get_module_args.update({
            'nas_server': "sample_nas_server"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockReplicationSessionApi.get_rep_session_error(
            'nas_error'), replicationsession_module_mock)

    def test_get_replication_session_filesystem_exception(self, replicationsession_module_mock):
        self.get_module_args.update({
            'filesystem': MockReplicationSessionApi.FS_NAME
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockReplicationSessionApi.get_rep_session_error(
            'fs_error'), replicationsession_module_mock)

    def test_get_replication_session_vg_exception(self, replicationsession_module_mock):
        self.get_module_args.update({
            'volume_group': "sample_vg"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockReplicationSessionApi.get_rep_session_error(
            'vg_error'), replicationsession_module_mock)

    def test_get_replication_session_vol_exception(self, replicationsession_module_mock):
        self.get_module_args.update({
            'volume': "sample_vol"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockReplicationSessionApi.get_rep_session_error(
            'vol_error'), replicationsession_module_mock)

    def test_modify_from_failed_over_to_sync_destination(self, replicationsession_module_mock):
        self.get_module_args.update({
            'session_id': MockReplicationSessionApi.ID,
            'session_state': MockReplicationSessionApi.FAIL_OVER
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.conn.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_SYNC[1])
        replicationsession_module_mock.protection.failover_replication_session = MagicMock(return_value=True)
        replicationsession_module_mock.perform_module_operation()
        assert replicationsession_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_get_replication_session_filesystem_nas(self, replicationsession_module_mock):
        self.get_module_args.update({
            'filesystem': MockReplicationSessionApi.FS_NAME,
            'nas_server': "6299d83a-37dc-340b-788f-4ad525462806"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.provisioning.get_nas_server_details = MagicMock(
            MockReplicationSessionApi.NAS_SERVER_DETAILS[0])
        replicationsession_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockReplicationSessionApi.FILESYSTEM_DETAILS)
        replicationsession_module_mock.protection.get_replication_sessions = MagicMock(
            return_value=MockReplicationSessionApi.SESSION_IDS_FILESYSTEM)
        replicationsession_module_mock.protection.get_replication_session_details = MagicMock(
            return_value=MockReplicationSessionApi.REPLICATION_SESSION_DETAILS_FILESYSTEM[0])
        replicationsession_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockReplicationSessionApi.FILESYSTEM_DETAILS[0])
        replicationsession_module_mock.perform_module_operation()
        replicationsession_module_mock.conn.protection.get_replication_session_details.assert_called()

    def test_get_replication_session_filesystem_nas_exception(self, replicationsession_module_mock):
        self.get_module_args.update({
            'filesystem': MockReplicationSessionApi.FS_NAME,
            'nas_server': "6299d83a-37dc-340b-788f-4ad525462806"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.provisioning.get_nas_server_details = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockReplicationSessionApi.get_rep_session_error(
            'fs_nas_error'), replicationsession_module_mock)

    def test_get_replication_session_filesystem_nas_none_exception(self, replicationsession_module_mock):
        self.get_module_args.update({
            'filesystem': MockReplicationSessionApi.FS_NAME,
            'nas_server': "6299d83a-37dc-340b-788f-4ad525462806"
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockReplicationSessionApi.get_rep_session_error(
            'fs_nas_error'), replicationsession_module_mock)

    def test_empty_cluster(self, replicationsession_module_mock):
        self.get_module_args.update({
            'replication_group': MockReplicationSessionApi.REP_GROUP,
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.get_clusters = MagicMock(
            return_value=[])
        self.capture_fail_json_call(MockReplicationSessionApi.get_rep_session_error(
            'empty_cluster'), replicationsession_module_mock)

    def test_rep_session_none(self, replicationsession_module_mock):
        self.get_module_args.update({
            'replication_group': MockReplicationSessionApi.REP_GROUP,
        })
        replicationsession_module_mock.module.params = self.get_module_args
        replicationsession_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationSessionApi.CLUSTER_DETAILS)
        replicationsession_module_mock.get_replication_session_details = MagicMock(return_value=[])
        self.capture_fail_json_call(MockReplicationSessionApi.get_rep_session_error(
            'non_existing_session'), replicationsession_module_mock)
