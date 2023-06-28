# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for NAS server module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_nasserver_api import MockNasServerApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_powerstore_connection = MagicMock()
utils.PowerStoreException = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerstore.plugins.modules.nasserver import PowerStoreNasServer


class TestPowerstoreNasServer():

    get_module_args = MockNasServerApi.NAS_SERVER_COMMON_ARGS

    @pytest.fixture
    def nasserver_module_mock(self, mocker):
        mocker.patch(MockNasServerApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        nasserver_module_mock = PowerStoreNasServer()
        nasserver_module_mock.module = MagicMock()
        return nasserver_module_mock

    def test_get_nasserver_response(self, nasserver_module_mock):
        self.get_module_args.update({
            'nas_server_id': "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
            'state': "present"
        })
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_DETAILS[0])
        nasserver_module_mock.perform_module_operation()
        assert self.get_module_args['nas_server_id'] == nasserver_module_mock.module.exit_json.call_args[1]['nasserver_details']['id']
        nasserver_module_mock.provisioning.get_nas_server_details.assert_called()

    def test_get_nasserver_name_response(self, nasserver_module_mock):
        self.get_module_args.update({
            'nas_server_name': "Sample_nas_server_1",
            'state': "present"
        })
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_DETAILS[0])
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
        nasserver_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            side_effect=MockApiException)
        nasserver_module_mock.perform_module_operation()
        nasserver_module_mock.provisioning.get_nas_server_by_name.assert_called()

    def test_create_nasserver_name(self, nasserver_module_mock):
        self.get_module_args.update({
            'nas_server_name': "Sample_nas_server_1",
            'state': "present"
        })
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=None)
        nasserver_module_mock.perform_module_operation()
        assert MockNasServerApi.create_nas_server_failed_msg() in \
            nasserver_module_mock.module.fail_json.call_args[1]['msg']

    def test_delete_nasserver(self, nasserver_module_mock):
        self.get_module_args.update({
            'nas_server_name': "Sample_nas_server_1",
            'state': "absent"
        })
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_DETAILS[0])
        nasserver_module_mock.perform_module_operation()
        assert MockNasServerApi.delete_nas_server_failed_msg() in \
            nasserver_module_mock.module.fail_json.call_args[1]['msg']

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
        nasserver_module_mock.perform_module_operation()
        nasserver_module_mock.provisioning.modify_nasserver.assert_called()

    def test_get_nasserver_multi_cluster(self, nasserver_module_mock):
        self.get_module_args.update({
            'nas_server_id': "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
            'state': "present"
        })
        nasserver_module_mock.module.params = self.get_module_args
        nasserver_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNasServerApi.NAS_SERVER_DETAILS[0])
        nasserver_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockNasServerApi.CLUSTER_DETAILS)
        nasserver_module_mock.perform_module_operation()
        assert self.get_module_args['nas_server_id'] == nasserver_module_mock.module.exit_json.call_args[1]['nasserver_details']['id']
        nasserver_module_mock.provisioning.get_nas_server_details.assert_called()
