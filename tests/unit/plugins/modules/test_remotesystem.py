# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Remote System module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import copy
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

    def test_add_remotesystem_fc_wwns(self, remotesystem_module_mock):
        """Test adding Universal remote system with FC WWNs"""
        fc_wwns = [
            MockRemoteSystemApi.sample_wwn_1,
            MockRemoteSystemApi.sample_wwn_2
        ]
        self.get_module_args.update({
            'remote_address': self.remote_system_sample_address,
            'remote_user': "admin",
            'remote_password': "remote_password",
            'remote_port': 443,
            'network_latency': "Low",
            'description': self.sample_description,
            'fc_target_wwns': fc_wwns,
            'data_connection_type': "FC",
            'type': "Universal",
            'state': "present"
        })
        remotesystem_module_mock.module.params = self.get_module_args
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            return_value=None)
        remotesystem_module_mock.configuration.exchange_certificate = MagicMock()
        remotesystem_module_mock.perform_module_operation()
        remotesystem_module_mock.conn.protection.create_remote_system.assert_called()
        call_dict = remotesystem_module_mock.conn.protection.create_remote_system.call_args[0][0]
        # Verify that WWN strings are converted to objects with 'wwn' key
        expected_fc_targets = [{'wwn': wwn} for wwn in fc_wwns]
        assert call_dict['universal_details']['fc_targets'] == expected_fc_targets

    def test_add_remotesystem_fc_wwns_without_fc_type_negative(self, remotesystem_module_mock):
        """Test adding remote system with FC WWNs but without FC connection type should fail"""
        fc_wwns = [
            MockRemoteSystemApi.sample_wwn_1,
            MockRemoteSystemApi.sample_wwn_2
        ]
        module_args = copy.deepcopy(self.get_module_args)
        module_args.update({
            'remote_id': None,
            'remote_name': None,
            'remote_address': self.remote_system_sample_address,
            'remote_user': "admin",
            'remote_password': "remote_password",
            'remote_port': 443,
            'network_latency': "Low",
            'description': self.sample_description,
            'fc_target_wwns': fc_wwns,
            'data_connection_type': "iSCSI",
            'type': "Universal",
            'state': "present"
        })
        remotesystem_module_mock.module.params = module_args
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            return_value=None)
        remotesystem_module_mock.configuration.exchange_certificate = MagicMock()
        remotesystem_module_mock.perform_module_operation()
        assert remotesystem_module_mock.module.fail_json.called
        error_msg = remotesystem_module_mock.module.fail_json.call_args[1]['msg']
        assert "fc_target_wwns can only be specified when data_connection_type is set to 'FC'" in error_msg

    def test_add_remotesystem_fc_wwns_without_any_type_negative(self, remotesystem_module_mock):
        """Test adding remote system with FC WWNs but without Universal type should fail"""
        fc_wwns = [
            MockRemoteSystemApi.sample_wwn_1,
            MockRemoteSystemApi.sample_wwn_2
        ]
        module_args = copy.deepcopy(self.get_module_args)
        module_args.update({
            'remote_id': None,
            'remote_name': None,
            'remote_address': self.remote_system_sample_address,
            'remote_user': "admin",
            'remote_password': "remote_password",
            'remote_port': 443,
            'network_latency': "Low",
            'description': self.sample_description,
            'fc_target_wwns': fc_wwns,
            'data_connection_type': "FC",
            'type': "PowerStore",
            'state': "present"
        })
        remotesystem_module_mock.module.params = module_args
        remotesystem_module_mock.conn.protection.get_remote_system_by_mgmt_address = MagicMock(
            return_value=None)
        remotesystem_module_mock.configuration.exchange_certificate = MagicMock()
        remotesystem_module_mock.perform_module_operation()
        assert remotesystem_module_mock.module.fail_json.called
        error_msg = remotesystem_module_mock.module.fail_json.call_args[1]['msg']
        assert "fc_target_wwns can only be specified when type is set to 'Universal'" in error_msg
