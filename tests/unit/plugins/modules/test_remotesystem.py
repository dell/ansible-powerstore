# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Remote System module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_remotesystem_api import MockRemoteSystemApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.remotesystem import PowerstoreRemoteSystem


class TestPowerstoreRemoteSystem():

    get_module_args = MockRemoteSystemApi.REMOTE_SYSTEM_COMMON_ARGS
    remote_system_sample_address = "xx.xx.xx.xx"
    sample_description = "Adding a new remote system"

    @pytest.fixture
    def remotesystem_module_mock(self, mocker):
        mocker.patch(MockRemoteSystemApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        remotesystem_module_mock = PowerstoreRemoteSystem()
        remotesystem_module_mock.module = MagicMock()
        return remotesystem_module_mock

    def test_get_remotesystem_response(self, remotesystem_module_mock):
        self.get_module_args.update({
            'remote_id': "aaa3cc6b-455b-4bde-aa75-a1edf61bbe0b",
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_details = MagicMock(
            return_value=MockRemoteSystemApi.REMOTE_SYSTEM_DETAILS[0])
        remotesystem_module_mock.perform_module_operation()
        assert self.get_module_args['remote_id'] == remotesystem_module_mock.module.exit_json.call_args[1]['remote_system_details']['id']
        remotesystem_module_mock.conn.protection.get_remote_system_details.assert_called()

    def test_get_remotesystem_remote_address_response(self, remotesystem_module_mock):
        self.get_module_args.update({
            'remote_address': self.remote_system_sample_address,
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            return_value=MockRemoteSystemApi.REMOTE_SYSTEM_DETAILS)
        remotesystem_module_mock.perform_module_operation()
        assert self.get_module_args['remote_address'] == remotesystem_module_mock.module.exit_json.call_args[1]['remote_system_details']['management_address']
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address.assert_called()

    def test_get_remotesystem_remote_address_exception(self, remotesystem_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'remote_address': self.remote_system_sample_address,
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            side_effect=MockApiException)
        remotesystem_module_mock.perform_module_operation()
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address.assert_called()

    def test_get_remote_system_multi_cluster(self, remotesystem_module_mock):
        self.get_module_args.update({
            'remote_id': "aaa3cc6b-455b-4bde-aa75-a1edf61bbe0b",
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_details = MagicMock(
            return_value=MockRemoteSystemApi.REMOTE_SYSTEM_DETAILS[0])
        remotesystem_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockRemoteSystemApi.CLUSTER_DETAILS)
        remotesystem_module_mock.perform_module_operation()
        remotesystem_module_mock.conn.protection.get_remote_system_details.assert_called()

    def test_add_remotesystem_remote_address_response(self, remotesystem_module_mock):
        self.get_module_args.update({
            'remote_address': self.remote_system_sample_address,
            'remote_user': "admin",
            'remote_password': "remote_password",
            'remote_port': 443,
            'network_latency': "Low",
            'decription': self.sample_description,
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            return_value=None)
        remotesystem_module_mock.perform_module_operation()
        remotesystem_module_mock.conn.protection.create_remote_system.assert_called()

    def test_modify_remotesystem_network_latency(self, remotesystem_module_mock):
        self.get_module_args.update({
            'remote_address': self.remote_system_sample_address,
            'remote_user': "admin",
            'remote_password': "remote_password",
            'remote_port': 443,
            'network_latency': "High",
            'decription': self.sample_description,
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            return_value=MockRemoteSystemApi.REMOTE_SYSTEM_DETAILS)
        remotesystem_module_mock.perform_module_operation()
        remotesystem_module_mock.conn.protection.modify_remote_system.assert_called()

    def test_add_remotesystem_remote_address_remote_name_response(self, remotesystem_module_mock):
        self.get_module_args.update({
            'remote_address': self.remote_system_sample_address,
            'remote_name': "Sample_remote_name",
            'remote_user': "admin",
            'remote_password': "remote_password",
            'remote_port': 443,
            'network_latency': "Low",
            'decription': self.sample_description,
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            return_value=None)
        remotesystem_module_mock.perform_module_operation()
        remotesystem_module_mock.conn.protection.create_remote_system.assert_called()
        assert MockRemoteSystemApi.create_remotesystem_with_remote_name_failed_msg() in \
            remotesystem_module_mock.module.fail_json.call_args[1]['msg']

    def test_delete_remotesystem_remote_address_response(self, remotesystem_module_mock):
        self.get_module_args.update({
            'remote_address': self.remote_system_sample_address,
            'state': "absent"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            return_value=MockRemoteSystemApi.REMOTE_SYSTEM_DETAILS)
        remotesystem_module_mock.perform_module_operation()
        remotesystem_module_mock.conn.protection.delete_remote_system.assert_called()

    def test_delete_remotesystem_remote_address_exception(self, remotesystem_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'remote_id': "aaa3cc6b-455b-4bde-aa75-a1edf61bbe0b",
            'wait_for_completion': True,
            'state': "absent"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_details = MagicMock(
            return_value=MockRemoteSystemApi.REMOTE_SYSTEM_DETAILS[0])
        remotesystem_module_mock.protection.delete_remote_system = MagicMock(
            side_effect=MockApiException)
        remotesystem_module_mock.protection.delete_remote_system = MagicMock(
            return_value=(None, None))
        remotesystem_module_mock.perform_module_operation()
        remotesystem_module_mock.protection.delete_remote_system.assert_called()
