# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for NAS server module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

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
        mocker.patch(MockNasServerApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        nasserver_module_mock = PowerStoreNasServer()
        nasserver_module_mock.module = MagicMock()
        nasserver_module_mock.get_clusters = MagicMock(return_value=MockNasServerApi.CLUSTERS)
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
        nasserver_module_mock.provisioning.get_nodes = MagicMock(return_value=MockNasServerApi.NODE_DETAILS)
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
        nasserver_module_mock.provisioning.get_nodes = MagicMock(return_value=MockNasServerApi.NODE_DETAILS)
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
        nasserver_module_mock.provisioning.delete_nasserver = MagicMock(return_value=None)
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
