# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Remote System module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
import copy
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

    def test_add_remotesystem_with_temp_credentials(self, remotesystem_module_mock):
        self.get_module_args.update({
            'remote_address': self.remote_system_sample_address,
            'remote_user': None,
            'remote_password': None,
            'remote_temp_user_id': "temp-id-12345",
            'remote_temp_user_secret': "temp-secret-xyz",
            'remote_port': 443,
            'network_latency': "Low",
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            return_value=None)
        remotesystem_module_mock.perform_module_operation()
        remotesystem_module_mock.conn.protection.create_remote_system.assert_called()

    def test_add_remotesystem_no_auth_method_negative(self, remotesystem_module_mock):
        self.get_module_args.update({
            'remote_address': self.remote_system_sample_address,
            'remote_user': None,
            'remote_password': None,
            'remote_temp_user_id': None,
            'remote_temp_user_secret': None,
            'remote_port': 443,
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            return_value=None)
        remotesystem_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockRemoteSystemApi.CLUSTER_DETAILS)
        remotesystem_module_mock.perform_module_operation()
        assert MockRemoteSystemApi.no_auth_method_for_create_failed_msg() in \
            remotesystem_module_mock.module.fail_json.call_args[1]['msg']

    def test_exchange_cert_uses_temp_keys(self, remotesystem_module_mock):
        self.get_module_args.update({
            'remote_address': self.remote_system_sample_address,
            'remote_user': None,
            'remote_password': None,
            'remote_temp_user_id': "temp-id-12345",
            'remote_temp_user_secret': "temp-secret-xyz",
            'remote_port': 443,
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            return_value=None)
        remotesystem_module_mock.configuration.exchange_certificate = MagicMock()
        remotesystem_module_mock.perform_module_operation()

        call_dict = remotesystem_module_mock.configuration.exchange_certificate.call_args[0][0]
        # Temporary credentials are mapped to username/password for API compatibility
        assert 'username' in call_dict
        assert 'password' in call_dict
        assert call_dict['username'] == "temp-id-12345"
        assert call_dict['password'] == "temp-secret-xyz"
        assert 'temp_user_id' not in call_dict
        assert 'temp_user_secret' not in call_dict

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

    def test_temp_credential_create_flow_explicit(self, remotesystem_module_mock):
        """Test explicit temp credential create flow"""
        self.get_module_args.update({
            'remote_address': self.remote_system_sample_address,
            'remote_user': None,
            'remote_password': None,
            'remote_temp_user_id': "temp-id-12345",
            'remote_temp_user_secret': "temp-secret-xyz",
            'remote_port': 443,
            'network_latency': "Low",
            'description': "Adding remote system via temp credentials",
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            return_value=None)
        remotesystem_module_mock.configuration.exchange_certificate = MagicMock()
        remotesystem_module_mock.perform_module_operation()
        # Verify exchange_certificate is called with temp credentials mapped to username/password
        remotesystem_module_mock.configuration.exchange_certificate.assert_called()
        call_dict = remotesystem_module_mock.configuration.exchange_certificate.call_args[0][0]
        assert call_dict['username'] == "temp-id-12345"
        assert call_dict['password'] == "temp-secret-xyz"
        assert 'temp_user_id' not in call_dict
        assert 'temp_user_secret' not in call_dict
        remotesystem_module_mock.conn.protection.create_remote_system.assert_called()

    def test_legacy_username_password_create_flow_explicit(self, remotesystem_module_mock):
        """Test explicit legacy username/password create flow"""
        self.get_module_args.update({
            'remote_address': self.remote_system_sample_address,
            'remote_user': "admin",
            'remote_password': "remote_password",
            'remote_temp_user_id': None,
            'remote_temp_user_secret': None,
            'remote_port': 443,
            'network_latency': "Low",
            'description': self.sample_description,
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            return_value=None)
        remotesystem_module_mock.configuration.exchange_certificate = MagicMock()
        remotesystem_module_mock.perform_module_operation()
        # Verify exchange_certificate is called with username/password
        remotesystem_module_mock.configuration.exchange_certificate.assert_called()
        call_dict = remotesystem_module_mock.configuration.exchange_certificate.call_args[0][0]
        assert call_dict['username'] == "admin"
        assert call_dict['password'] == "remote_password"
        assert 'temp_user_id' not in call_dict
        assert 'temp_user_secret' not in call_dict
        remotesystem_module_mock.conn.protection.create_remote_system.assert_called()

    # FC Replication - Create tests
    def test_add_remotesystem_with_fc_connection_type(self, remotesystem_module_mock):
        self.get_module_args.update({
            'remote_address': self.remote_system_sample_address,
            'remote_user': "admin",
            'remote_password': "remote_password",
            'remote_port': 443,
            'network_latency': "Low",
            'data_connection_type': "FC",
            'type': "Universal",
            'fc_target_wwns': [
                MockRemoteSystemApi.sample_wwn_1,
                MockRemoteSystemApi.sample_wwn_2
            ],
            'description': "Adding Universal FC remote system",
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            return_value=None)
        remotesystem_module_mock.conn.protection.create_remote_system = MagicMock(
            return_value=MockRemoteSystemApi.FC_REMOTE_SYSTEM_DETAILS[0])
        remotesystem_module_mock.conn.protection.get_remote_system_details = MagicMock(
            return_value=MockRemoteSystemApi.FC_REMOTE_SYSTEM_DETAILS[0])
        remotesystem_module_mock.perform_module_operation()
        remotesystem_module_mock.conn.protection.create_remote_system.assert_called()
        call_args = remotesystem_module_mock.conn.protection.create_remote_system.call_args[0][0]
        assert call_args['data_connection_type'] == 'FC'
        assert call_args['type'] == 'Universal'
        assert 'universal_details' in call_args
        assert call_args['universal_details']['fc_targets'] == [
            MockRemoteSystemApi.sample_wwn_1,
            MockRemoteSystemApi.sample_wwn_2
        ]

    def test_add_remotesystem_with_fc_type_no_wwns(self, remotesystem_module_mock):
        self.get_module_args.update({
            'remote_address': self.remote_system_sample_address,
            'remote_user': "admin",
            'remote_password': "remote_password",
            'remote_port': 443,
            'data_connection_type': "FC",
            'fc_target_wwns': None,
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            return_value=None)
        remotesystem_module_mock.conn.protection.create_remote_system = MagicMock(
            return_value=MockRemoteSystemApi.FC_REMOTE_SYSTEM_DETAILS[0])
        remotesystem_module_mock.conn.protection.get_remote_system_details = MagicMock(
            return_value=MockRemoteSystemApi.FC_REMOTE_SYSTEM_DETAILS[0])
        remotesystem_module_mock.perform_module_operation()
        remotesystem_module_mock.conn.protection.create_remote_system.assert_called()
        call_args = remotesystem_module_mock.conn.protection.create_remote_system.call_args[0][0]
        assert call_args['data_connection_type'] == 'FC'
        assert 'fc_target_wwns' not in call_args

    def test_add_remotesystem_with_iscsi_connection_type(self, remotesystem_module_mock):
        self.get_module_args.update({
            'remote_address': self.remote_system_sample_address,
            'remote_user': "admin",
            'remote_password': "remote_password",
            'remote_port': 443,
            'data_connection_type': "iSCSI",
            'fc_target_wwns': None,
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            return_value=None)
        remotesystem_module_mock.conn.protection.create_remote_system = MagicMock(
            return_value=MockRemoteSystemApi.REMOTE_SYSTEM_DETAILS[0])
        remotesystem_module_mock.conn.protection.get_remote_system_details = MagicMock(
            return_value=MockRemoteSystemApi.REMOTE_SYSTEM_DETAILS[0])
        remotesystem_module_mock.perform_module_operation()
        remotesystem_module_mock.conn.protection.create_remote_system.assert_called()
        call_args = remotesystem_module_mock.conn.protection.create_remote_system.call_args[0][0]
        assert call_args['data_connection_type'] == 'iSCSI'

    # FC Replication - Validation tests (Negative)
    def test_add_remotesystem_fc_wwns_without_fc_type_negative(self, remotesystem_module_mock):
        module_args = copy.deepcopy(MockRemoteSystemApi.REMOTE_SYSTEM_COMMON_ARGS)
        module_args.update({
            'remote_address': self.remote_system_sample_address,
            'remote_name': None,
            'remote_id': None,
            'remote_user': "admin",
            'remote_password': "remote_password",
            'remote_port': 443,
            'data_connection_type': "iSCSI",
            'fc_target_wwns': [MockRemoteSystemApi.sample_wwn_1],
            'state': "present"
        })
        remotesystem_module_mock.module.params = module_args
        remotesystem_module_mock.perform_module_operation()
        assert "fc_target_wwns can only be specified when" \
               " data_connection_type is set to 'FC'." in \
            remotesystem_module_mock.module.fail_json.call_args[1]['msg']

    def test_add_remotesystem_fc_wwns_without_any_type_negative(self, remotesystem_module_mock):
        module_args = copy.deepcopy(MockRemoteSystemApi.REMOTE_SYSTEM_COMMON_ARGS)
        module_args.update({
            'remote_address': self.remote_system_sample_address,
            'remote_name': None,
            'remote_id': None,
            'remote_user': "admin",
            'remote_password': "remote_password",
            'remote_port': 443,
            'data_connection_type': "FC",
            'type': "PowerStore",
            'fc_target_wwns': [MockRemoteSystemApi.sample_wwn_1],
            'state': "present"
        })
        remotesystem_module_mock.module.params = module_args
        remotesystem_module_mock.perform_module_operation()
        assert "fc_target_wwns can only be specified when type is set to 'Universal'." in \
            remotesystem_module_mock.module.fail_json.call_args[1]['msg']

    # FC Replication - Modify tests
    def test_modify_remotesystem_to_fc_connection_type(self, remotesystem_module_mock):
        self.get_module_args.update({
            'remote_address': self.remote_system_sample_address,
            'data_connection_type': "FC",
            'fc_target_wwns': [MockRemoteSystemApi.sample_wwn_1],
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            return_value=MockRemoteSystemApi.REMOTE_SYSTEM_DETAILS)
        remotesystem_module_mock.perform_module_operation()
        remotesystem_module_mock.conn.protection.modify_remote_system.assert_called()

    # FC Replication - Get details tests
    def test_get_remotesystem_fc_details_response(self, remotesystem_module_mock):
        self.get_module_args.update({
            'remote_id': "bbb4dd7c-566c-5cef-99a6-b2feg72ccf1c",
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockRemoteSystemApi.CLUSTER_DETAILS)
        remotesystem_module_mock.conn.protection.get_remote_system_details = MagicMock(
            return_value=MockRemoteSystemApi.FC_REMOTE_SYSTEM_DETAILS[0])
        remotesystem_module_mock.perform_module_operation()
        result = remotesystem_module_mock.module.exit_json.call_args[1]
        assert result['remote_system_details']['data_connection_type'] == 'FC'
        assert result['remote_system_details']['fc_target_wwns'] == [
            MockRemoteSystemApi.sample_wwn_1,
            MockRemoteSystemApi.sample_wwn_2
        ]

    def test_get_remotesystem_iscsi_details_has_connection_type(self, remotesystem_module_mock):
        self.get_module_args.update({
            'remote_id': "aaa3cc6b-455b-4bde-aa75-a1edf61bbe0b",
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockRemoteSystemApi.CLUSTER_DETAILS)
        remotesystem_module_mock.conn.protection.get_remote_system_details = MagicMock(
            return_value=MockRemoteSystemApi.REMOTE_SYSTEM_DETAILS[0])
        remotesystem_module_mock.perform_module_operation()
        result = remotesystem_module_mock.module.exit_json.call_args[1]
        assert result['remote_system_details']['data_connection_type'] == 'iSCSI'
        assert result['remote_system_details']['fc_target_wwns'] == []

    # FC Replication - Idempotency test
    def test_modify_remotesystem_fc_idempotent(self, remotesystem_module_mock):
        self.get_module_args.update({
            'remote_id': "bbb4dd7c-566c-5cef-99a6-b2feg72ccf1c",
            'remote_name': None,
            'remote_address': None,
            'new_remote_address': None,
            'description': None,
            'network_latency': None,
            'data_connection_type': "FC",
            'fc_target_wwns': [
                MockRemoteSystemApi.sample_wwn_1,
                MockRemoteSystemApi.sample_wwn_2
            ],
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockRemoteSystemApi.CLUSTER_DETAILS)
        remotesystem_module_mock.conn.protection.get_remote_system_details = MagicMock(
            return_value=MockRemoteSystemApi.FC_REMOTE_SYSTEM_DETAILS[0])
        remotesystem_module_mock.perform_module_operation()
        result = remotesystem_module_mock.module.exit_json.call_args[1]
        assert result['changed'] is False

    # FC Replication - Create exception test
    def test_add_remotesystem_fc_create_exception(self, remotesystem_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'remote_address': self.remote_system_sample_address,
            'remote_name': None,
            'remote_id': None,
            'remote_user': "admin",
            'remote_password': "remote_password",
            'remote_port': 443,
            'data_connection_type': "FC",
            'type': "Universal",
            'fc_target_wwns': [MockRemoteSystemApi.sample_wwn_1],
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.module.fail_json = MagicMock(
            side_effect=SystemExit(1))
        remotesystem_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockRemoteSystemApi.CLUSTER_DETAILS)
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            return_value=None)
        remotesystem_module_mock.conn.protection.create_remote_system = MagicMock(
            side_effect=MockApiException)
        try:
            remotesystem_module_mock.perform_module_operation()
        except SystemExit:
            pass
        remotesystem_module_mock.module.fail_json.assert_called()
        assert 'create remote system failed' in \
            remotesystem_module_mock.module.fail_json.call_args[1]['msg']

    # FC Replication - Delete FC remote system
    def test_delete_fc_remotesystem(self, remotesystem_module_mock):
        self.get_module_args.update({
            'remote_id': "bbb4dd7c-566c-5cef-99a6-b2feg72ccf1c",
            'state': "absent"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockRemoteSystemApi.CLUSTER_DETAILS)
        remotesystem_module_mock.conn.protection.get_remote_system_details = MagicMock(
            return_value=MockRemoteSystemApi.FC_REMOTE_SYSTEM_DETAILS[0])
        remotesystem_module_mock.perform_module_operation()
        remotesystem_module_mock.conn.protection.delete_remote_system.assert_called()
