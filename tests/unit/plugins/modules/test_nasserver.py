# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for NAS server module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import copy
import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_nasserver_api import MockNasServerApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.nasserver import PowerStoreNasServer
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries.\
    fail_json import FailJsonException, fail_json


class TestPowerstoreNasServer():

    get_module_args = MockNasServerApi.NAS_SERVER_COMMON_ARGS

    @pytest.fixture
    def nasserver_module_mock(self, mocker):
        mocker.patch(MockNasServerApi.MODULE_UTILS_PATH +
                     '.PowerStoreException', new=MockApiException)
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "500"
        MockApiException.body = "PyPowerStore Error message"
        self.get_module_args = copy.deepcopy(MockNasServerApi.NAS_SERVER_COMMON_ARGS)
        nasserver_module_mock = PowerStoreNasServer()
        nasserver_module_mock.module = MagicMock()
        nasserver_module_mock.provisioning = MagicMock()
        nasserver_module_mock.protection = MagicMock()
        nasserver_module_mock.configuration = MagicMock()
        nasserver_module_mock.conn = MagicMock()
        nasserver_module_mock.conn.provisioning = nasserver_module_mock.provisioning
        nasserver_module_mock.conn.protection = nasserver_module_mock.protection
        nasserver_module_mock.conn.config_mgmt = nasserver_module_mock.configuration
        nasserver_module_mock.provisioning.get_nodes = MagicMock(
            return_value=MockNasServerApi.NODE_DETAILS)
        nasserver_module_mock.get_clusters = MagicMock(
            return_value=MockNasServerApi.CLUSTERS)
        nasserver_module_mock.module.fail_json = fail_json
        return nasserver_module_mock

    def test_get_nasserver_response(self, nasserver_module_mock):
        self.get_module_args.update({
            'nas_server_id': MockNasServerApi.NAS_SERVER_ID,
            'state': "present"
        })
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_DETAILS[0])
        nasserver_module_mock.provisioning.get_nodes = MagicMock(
            return_value=MockNasServerApi.NODE_DETAILS)
        nasserver_module_mock.perform_module_operation()
        assert self.get_module_args['nas_server_id'] == nasserver_module_mock.module.exit_json.call_args[1]['nasserver_details']['id']
        nasserver_module_mock.provisioning.get_nas_server_details.assert_called()

    def test_get_nasserver_name_response(self, nasserver_module_mock):
        self.get_module_args.update({
            'nas_server_name': "Sample_nas_server_1",
            'state': "present"
        })
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_DETAILS)
        nasserver_module_mock.provisioning.get_nodes = MagicMock(
            return_value=MockNasServerApi.NODE_DETAILS)
        nasserver_module_mock.perform_module_operation()
        assert self.get_module_args['nas_server_name'] == nasserver_module_mock.module.exit_json.call_args[1]['nasserver_details']['name']
        nasserver_module_mock.provisioning.get_nas_server_by_name.assert_called()

    def test_get_nasserver_name_exception(self, nasserver_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'nas_server_name': "Sample_nas_server_1",
            'state': "present"
        })
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.get_node_id = MagicMock()
        nasserver_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            side_effect=MockApiException)
        nasserver_module_mock.perform_module_operation()
        nasserver_module_mock.provisioning.create_nasserver.assert_called()

    def test_modify_nasserver_response(self, nasserver_module_mock):
        self.get_module_args.update({
            'nas_server_name': "Sample_nas_server_1",
            'nas_server_new_name': "Sample_nas_server_new_name_1",
            'description': "New description",
            'current_unix_directory_service': "LOCAL_FILES",
            'default_unix_user': "admin",
            'default_windows_user': "admin",
            'protection_policy': "Sample_protection_policy",
            'state': "present"
        })
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_DETAILS)
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_DETAILS[0])
        nasserver_module_mock.provisioning.get_nodes = MagicMock(
            return_value=MockNasServerApi.NODE_DETAILS)
        nasserver_module_mock.protection.get_protection_policy_by_name = MagicMock(
            return_value=MockNasServerApi.PROTECTION_POLICY_DETAILS)
        nasserver_module_mock.perform_module_operation()
        nasserver_module_mock.provisioning.modify_nasserver.assert_called()

    def test_add_protection_policy_by_id_response(self, nasserver_module_mock):
        self.get_module_args.update({
            'nas_server_name': "Sample_nas_server_1",
            'protection_policy': "bce845ea-78ba-4414-ada1-8130f3a49e74",
            'state': "present"
        })
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_DETAILS)
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_DETAILS[0])
        nasserver_module_mock.provisioning.get_nodes = MagicMock(
            return_value=MockNasServerApi.NODE_DETAILS)
        nasserver_module_mock.protection.get_protection_policy_details = MagicMock(
            return_value=MockNasServerApi.PROTECTION_POLICY_DETAILS[0])
        nasserver_module_mock.perform_module_operation()
        nasserver_module_mock.provisioning.modify_nasserver.assert_called()

    def test_remove_protection_policy_response(self, nasserver_module_mock):
        self.get_module_args.update({
            'nas_server_name': "Sample_nas_server_2",
            'protection_policy': "",
            'state': "present"
        })
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_2_DETAILS)
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_2_DETAILS[0])
        nasserver_module_mock.provisioning.get_nodes = MagicMock(
            return_value=MockNasServerApi.NODE_DETAILS)
        nasserver_module_mock.perform_module_operation()
        nasserver_module_mock.provisioning.modify_nasserver.assert_called()

    def test_modify_nasserver_node_response(self, nasserver_module_mock):
        self.get_module_args.update({
            'nas_server_name': "Sample_nas_server_1",
            'current_node': "Appliance-XXXXXXX-node-A",
            'preferred_node': "Appliance-XXXXXXX-node-A",
            'state': "present"
        })
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_DETAILS[0])
        nasserver_module_mock.provisioning.get_nodes = MagicMock(
            return_value=MockNasServerApi.NODE_DETAILS)
        nasserver_module_mock.perform_module_operation()
        nasserver_module_mock.provisioning.modify_nasserver.assert_called()

    def test_modify_nasserver_exception(self, nasserver_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'nas_server_name': "Sample_nas_server_1",
            'current_node': "Appliance-XXXXXXX-node-A",
            'preferred_node': "Appliance-XXXXXXX-node-A",
            'state': "present"
        })
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_DETAILS[0])
        nasserver_module_mock.provisioning.get_nodes = MagicMock(
            return_value=MockNasServerApi.NODE_DETAILS)
        nasserver_module_mock.provisioning.modify_nasserver = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockNasServerApi.modify_nas_server_failed_msg(), nasserver_module_mock)

    def test_get_nasserver_multi_cluster(self, nasserver_module_mock):
        self.get_module_args.update({
            'nas_server_id': MockNasServerApi.NAS_SERVER_ID,
            'state': "present"
        })
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_DETAILS[0])
        nasserver_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockNasServerApi.CLUSTER_DETAILS)
        nasserver_module_mock.provisioning.get_nodes = MagicMock(
            return_value=MockNasServerApi.NODE_DETAILS)
        nasserver_module_mock.perform_module_operation()
        assert self.get_module_args['nas_server_id'] == nasserver_module_mock.module.exit_json.call_args[1]['nasserver_details']['id']
        nasserver_module_mock.provisioning.get_nas_server_details.assert_called()

    def test_create_nas_server(self, nasserver_module_mock):
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value={})
        self.get_module_args.update({
            "name": "my-nas-server",
            "description": "My NAS Server",
            "current_unix_directory_service": "LDAP",
            "default_unix_user": "nobody",
            "default_windows_user": "Guest",
            "is_username_translation_enabled": True,
            "is_auto_user_mapping_enabled": True,
            "protection_policy_id": "policy-id-123",
            "state": "present"
        })
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.get_node_id = MagicMock()
        nasserver_module_mock.provisioning.create_nasserver = MagicMock(
            return_value={'id': 'nas_server_id'})
        nasserver_module_mock.perform_module_operation()
        nasserver_module_mock.provisioning.create_nasserver.assert_called()

    def test_create_nasserver_exception(self, nasserver_module_mock):
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value={})
        self.get_module_args.update({
            "nas_server_name": MockNasServerApi.NAS_SERVER_NAME_1,
            "description": "My NAS Server",
            "current_unix_directory_service": "LDAP",
            "default_unix_user": "nobody",
            "default_windows_user": "Guest",
            "is_username_translation_enabled": True,
            "is_auto_user_mapping_enabled": True,
            "protection_policy_id": "policy-id-123",
            "state": "present"
        })
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.get_node_id = MagicMock()
        nasserver_module_mock.provisioning.create_nasserver = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockNasServerApi.create_nas_server_failed_msg(), nasserver_module_mock)

    def test_delete_nas_server(self, nasserver_module_mock):
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_DETAILS[0])
        self.get_module_args.update({
            'nas_server_id': MockNasServerApi.NAS_SERVER_ID,
            "state": "absent"
        })
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.delete_nasserver = MagicMock(
            return_value=None)
        nasserver_module_mock.perform_module_operation()
        nasserver_module_mock.provisioning.delete_nasserver.assert_called_once_with(
            MockNasServerApi.NAS_SERVER_ID)

    def test_delete_nas_server_exception(self, nasserver_module_mock):
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_DETAILS[0])
        self.get_module_args.update({
            'nas_server_id': MockNasServerApi.NAS_SERVER_ID,
            "state": "absent"
        })
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.delete_nasserver = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockNasServerApi.delete_nas_server_failed_msg(), nasserver_module_mock)

    def capture_fail_json_call(self, error_msg, nasserver_module_mock):
        try:
            nasserver_module_mock.perform_module_operation()
        except FailJsonException as fj_object:
            assert error_msg in fj_object.message

    # ---- Performance Policy Tests (U-102 to U-111) ----

    PERF_POLICY_NAS = {"id": "9e8g75d3-4567-8901-defg-123456789012",
                       "name": "file_gold_qos", "type": "File_Performance"}
    NAS_WITH_PERF = {"id": "6581683c-61a3-76ab-f107-62b767ad9845", "name": "sample_nas_server",
                     "performance_policy_id": "9e8g75d3-4567-8901-defg-123456789012",
                     "current_node_id": "Appliance-XXXXXXX-node-B",
                     "preferred_node_id": "Appliance-XXXXXXX-node-B"}
    NAS_NO_PERF = {"id": "6581683c-61a3-76ab-f107-62b767ad9845", "name": "sample_nas_server",
                   "performance_policy_id": None,
                   "current_node_id": "Appliance-XXXXXXX-node-B",
                   "preferred_node_id": "Appliance-XXXXXXX-node-B"}

    # U-102
    def test_modify_nasserver_assign_perf_policy(self, nasserver_module_mock):
        self.get_module_args.update({'nas_server_name': 'sample_nas_server',
                                     'performance_policy': 'file_gold_qos', 'state': 'present'})
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=[self.NAS_NO_PERF])
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=self.NAS_NO_PERF)
        nasserver_module_mock.protection.get_policy_by_name = MagicMock(
            return_value=[self.PERF_POLICY_NAS])
        nasserver_module_mock.provisioning.modify_nasserver = MagicMock(
            return_value=None)
        nasserver_module_mock.perform_module_operation()
        assert nasserver_module_mock.module.exit_json.call_args[1]['changed'] is True

    # U-103
    def test_modify_nasserver_remove_perf_policy(self, nasserver_module_mock):
        self.get_module_args.update({'nas_server_name': 'sample_nas_server',
                                     'performance_policy': '', 'state': 'present'})
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=[self.NAS_WITH_PERF])
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=self.NAS_WITH_PERF)
        nasserver_module_mock.provisioning.modify_nasserver = MagicMock(
            return_value=None)
        nasserver_module_mock.perform_module_operation()
        assert nasserver_module_mock.module.exit_json.call_args[1]['changed'] is True

    # U-104
    def test_nasserver_perf_policy_idempotent(self, nasserver_module_mock):
        self.get_module_args.update({'nas_server_name': 'sample_nas_server',
                                     'performance_policy': 'file_gold_qos', 'state': 'present'})
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=[self.NAS_WITH_PERF])
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=self.NAS_WITH_PERF)
        nasserver_module_mock.protection.get_policy_by_name = MagicMock(
            return_value=[self.PERF_POLICY_NAS])
        nasserver_module_mock.perform_module_operation()
        assert nasserver_module_mock.module.exit_json.call_args[1]['changed'] is False

    # U-105
    def test_nasserver_perf_policy_exception(self, nasserver_module_mock):
        self.get_module_args.update({'nas_server_name': 'sample_nas_server',
                                     'performance_policy': 'file_gold_qos', 'state': 'present'})
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=[self.NAS_NO_PERF])
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=self.NAS_NO_PERF)
        nasserver_module_mock.protection.get_policy_by_name = MagicMock(
            return_value=[self.PERF_POLICY_NAS])
        nasserver_module_mock.provisioning.modify_nasserver = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call("Failed to modify nasserver id", nasserver_module_mock)

    # U-106
    def test_nasserver_perf_policy_check_mode(self, nasserver_module_mock):
        self.get_module_args.update({'nas_server_name': 'sample_nas_server',
                                     'performance_policy': 'file_gold_qos', 'state': 'present'})
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.module.check_mode = True
        nasserver_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=[self.NAS_NO_PERF])
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=self.NAS_NO_PERF)
        nasserver_module_mock.protection.get_policy_by_name = MagicMock(
            return_value=[self.PERF_POLICY_NAS])
        nasserver_module_mock.perform_module_operation()
        assert nasserver_module_mock.module.exit_json.call_args[1]['changed'] is True
        nasserver_module_mock.provisioning.modify_nasserver.assert_not_called()

    # U-107
    def test_nasserver_details_include_perf_policy(self, nasserver_module_mock):
        self.get_module_args.update(
            {'nas_server_name': 'sample_nas_server', 'state': 'present'})
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=[self.NAS_WITH_PERF])
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=self.NAS_WITH_PERF)
        nasserver_module_mock.perform_module_operation()
        nas_details = nasserver_module_mock.module.exit_json.call_args[1]['nasserver_details']
        assert 'performance_policy_id' in nas_details

    # U-108
    def test_nasserver_perf_policy_resolve_name(self, nasserver_module_mock):
        self.get_module_args.update({'nas_server_name': 'sample_nas_server',
                                     'performance_policy': 'file_gold_qos', 'state': 'present'})
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=[self.NAS_NO_PERF])
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=self.NAS_NO_PERF)
        nasserver_module_mock.protection.get_policy_by_name = MagicMock(
            return_value=[self.PERF_POLICY_NAS])
        nasserver_module_mock.provisioning.modify_nasserver = MagicMock(
            return_value=None)
        nasserver_module_mock.perform_module_operation()
        nasserver_module_mock.protection.get_policy_by_name.assert_called()

    # U-109
    def test_nasserver_without_perf_policy_compat(self, nasserver_module_mock):
        self.get_module_args.update(
            {'nas_server_name': 'sample_nas_server', 'state': 'present'})
        self.get_module_args.pop('performance_policy', None)
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_DETAILS)
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_DETAILS[0])
        nasserver_module_mock.perform_module_operation()
        assert nasserver_module_mock.module.exit_json.call_args[1]['changed'] is False

    # U-110
    def test_nasserver_perf_policy_diff_mode(self, nasserver_module_mock):
        self.get_module_args.update({'nas_server_name': 'sample_nas_server',
                                     'performance_policy': 'file_gold_qos', 'state': 'present'})
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.module._diff = True
        nasserver_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=[self.NAS_NO_PERF])
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=self.NAS_NO_PERF)
        nasserver_module_mock.protection.get_policy_by_name = MagicMock(
            return_value=[self.PERF_POLICY_NAS])
        nasserver_module_mock.provisioning.modify_nasserver = MagicMock(
            return_value=None)
        nasserver_module_mock.perform_module_operation()
        result = nasserver_module_mock.module.exit_json.call_args[1]
        assert 'diff' in result

    # U-111
    def test_nasserver_invalid_policy_name(self, nasserver_module_mock):
        self.get_module_args.update({'nas_server_name': 'sample_nas_server',
                                     'performance_policy': 'nonexistent', 'state': 'present'})
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=[self.NAS_NO_PERF])
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=self.NAS_NO_PERF)
        nasserver_module_mock.protection.get_policy_by_name = MagicMock(
            return_value=[])
        self.capture_fail_json_call("No performance policy present", nasserver_module_mock)
