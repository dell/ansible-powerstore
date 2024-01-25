# Copyright: (c) 2024, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for remote support module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_remote_support_api \
    import MockRemoteSupportApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.remote_support \
    import PowerstoreRemoteSupport


class TestPowerstoreRemoteSupport():

    get_module_args = MockRemoteSupportApi.REMOTE_SUPPORT_COMMON_ARGS

    @pytest.fixture
    def remote_support_module_mock(self, mocker):
        mocker.patch(MockRemoteSupportApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        remote_support_module_mock = PowerstoreRemoteSupport()
        remote_support_module_mock.module = MagicMock()
        return remote_support_module_mock

    def test_get_remote_support_response(self, remote_support_module_mock):
        self.get_module_args.update({
            'remote_support_id': 0,
            'state': "present"
        })
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.
                                                                module.exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.get_remote_support_details.assert_called()

    def test_modify_remote_support_details(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Integrated_Tier2",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_modify_disabled_to_one_primary(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier2",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.X",
                                         'port': 9443,
                                         'is_primary': True}],
                                     'server_state': "present-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_modify_disabled_to_one_backup(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier2",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.X",
                                         'port': 9443,
                                         'is_primary': False}],
                                     'server_state': "present-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_modify_disabled_to_two_servers(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier2",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.X",
                                         'port': 9443,
                                         'is_primary': True},
                                      {
                                         'address': "10.X.X.Y",
                                         'port': 9443,
                                         'is_primary': False}],
                                     'server_state': "present-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_modify_gateway1_to_same_address_backup(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier3",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.X",
                                         'port': 9443,
                                         'is_primary': False}],
                                     'server_state': "present-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_GATEWAY1_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_modify_gateway1_to_two_servers(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier3",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.Y",
                                         'port': 9443,
                                         'is_primary': True},
                                      {
                                         'address': "10.X.X.Z",
                                         'port': 9443,
                                         'is_primary': False}],
                                     'server_state': "present-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_GATEWAY1_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_modify_gateway1_to_two_servers_primary(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier3",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.Y",
                                         'port': 9443,
                                         'is_primary': True}],
                                     'server_state': "present-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_GATEWAY1_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_modify_gateway1_to_two_servers_backup(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier3",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.Y",
                                         'port': 9443,
                                         'is_primary': False}],
                                     'server_state': "present-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_GATEWAY1_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_modify_gateway1_to_two_servers_2new(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier3",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.Y",
                                         'port': 9443,
                                         'is_primary': True},
                                      {
                                         'address': "10.X.X.X",
                                         'port': 9443,
                                         'is_primary': False}],
                                     'server_state': "present-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_GATEWAY1_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_modify_gateway2_to_two_servers_2same(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier3",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.Y",
                                         'port': 9443,
                                         'is_primary': True},
                                      {
                                         'address': "10.X.X.X",
                                         'port': 9443,
                                         'is_primary': False}],
                                     'server_state': "present-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_GATEWAY2_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_modify_gateway2_to_two_servers_2new(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier3",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.Z",
                                         'port': 9443,
                                         'is_primary': True},
                                      {
                                         'address': "10.X.X.X",
                                         'port': 9443,
                                         'is_primary': False}],
                                     'server_state': "present-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_GATEWAY2_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_modify_gateway2_to_two_servers_1new(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier3",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.X",
                                         'port': 9442,
                                         'is_primary': False}],
                                     'server_state': "present-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_GATEWAY2_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_modify_gateway2_to_two_servers_backup(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier3",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.Y",
                                         'port': 9442,
                                         'is_primary': False}],
                                     'server_state': "present-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_GATEWAY2_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_modify_gateway2_to_two_servers_same_backup(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier3",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.X",
                                         'port': 9443,
                                         'is_primary': False}],
                                     'server_state': "present-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_GATEWAY2SAME_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_modify_gateway2_to_two_servers_same_primary(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier3",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.X",
                                         'port': 9444,
                                         'is_primary': True}],
                                     'server_state': "present-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_GATEWAY2SAME_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_modify_gateway2_to_two_servers_same_primary_same_as_backup(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier3",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.X",
                                         'port': 9444,
                                         'is_primary': False}],
                                     'server_state': "present-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_GATEWAY2SAME_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_remove_primary_gateway_address(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier3",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.X",
                                         'port': 9443,
                                         'is_primary': True}],
                                     'server_state': "absent-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_GATEWAY2_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_remove_primary_gateway_address_only_is_primary(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier3",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.X",
                                         'port': None,
                                         'is_primary': True}],
                                     'server_state': "absent-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_GATEWAY2_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_remove_primary_gateway_address_only_port(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier3",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.X",
                                         'port': 9443,
                                         'is_primary': None}],
                                     'server_state': "absent-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_GATEWAY2_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_remove_primary_gateway_address_neither(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier3",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.X",
                                         'port': None,
                                         'is_primary': None}],
                                     'server_state': "absent-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_GATEWAY2_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_remove_primary_gateway_address_neither_same_address(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier3",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.X",
                                         'port': None,
                                         'is_primary': None}],
                                     'server_state': "absent-in-server",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_GATEWAY2SAME_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.modify_remote_support_details.assert_called()

    def test_verify_remote_support_details(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Integrated_Tier2",
                                     'verify_connection': True,
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.verify_remote_support_config.assert_called()

    def test_verify_remote_support_details_gateway(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier2",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.X",
                                         'port': 9443,
                                         'is_primary': True}],
                                     'verify_connection': True,
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.verify_remote_support_config.assert_called()

    def test_verify_remote_support_details_two_gateway(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier2",
                                     'remote_support_servers':
                                     [{
                                         'address': "10.X.X.X",
                                         'port': 9443,
                                         'is_primary': True},
                                      {
                                         'address': "10.X.X.X",
                                         'port': 9444,
                                         'is_primary': False}],
                                     'verify_connection': True,
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.verify_remote_support_config.assert_called()

    def test_send_test_alert_remote_support(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'send_test_alert': True,
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        remote_support_module_mock.configuration.test_remote_support_config.assert_called()

    def test_get_non_existing_remote_support_details(self, remote_support_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        invalid_remote_support_id = 2
        self.get_module_args.update({
            'remote_support_id': invalid_remote_support_id,
            'state': "present"
        })
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            side_effect=MockApiException)
        remote_support_module_mock.perform_module_operation()
        assert MockRemoteSupportApi.get_remote_support_failed_msg() in \
            remote_support_module_mock.module.fail_json.call_args[1]['msg']

    def test_delete_remote_support(self, remote_support_module_mock):
        remote_support_id = 0
        self.get_module_args.update({'remote_support_id': remote_support_id,
                                     'state': "absent"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert MockRemoteSupportApi.delete_remote_support_failed_msg() in \
            remote_support_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_remote_support_disabled_idempotency(self, remote_support_module_mock):
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "Disabled",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_DISABLED_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert self.get_module_args['remote_support_id'] == int(remote_support_module_mock.module.
                                                                exit_json.call_args[1]['remote_support_details']['id'])
        assert remote_support_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_send_test_alert_remote_support_disabled(self, remote_support_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({'remote_support_id': 0,
                                     'send_test_alert': True,
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_DISABLED_DETAILS)
        remote_support_module_mock.configuration.test_remote_support_config = MagicMock(
            side_effect=MockApiException)
        remote_support_module_mock.perform_module_operation()
        assert MockRemoteSupportApi.send_test_alert_remote_support_failed_msg() in \
            remote_support_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_remote_support_without_support_type(self, remote_support_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({'remote_support_id': 0,
                                     'proxy_address': '10.X.X.W',
                                     'proxy_port': 3128,
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_DISABLED_DETAILS)
        remote_support_module_mock.configuration.modify_remote_support_details = MagicMock(
            side_effect=MockApiException)
        remote_support_module_mock.perform_module_operation()
        assert MockRemoteSupportApi.modify_remote_support_without_support_type_failed_msg() in \
            remote_support_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_remote_support_without_remote_support_servers(self, remote_support_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({'remote_support_id': 0,
                                     'support_type': "SRS_Gateway_Tier3",
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_DISABLED_DETAILS)
        remote_support_module_mock.perform_module_operation()
        assert MockRemoteSupportApi.modify_remote_support_without_remote_support_servers_failed_msg() in \
            remote_support_module_mock.module.fail_json.call_args[1]['msg']

    def test_verify_remote_support_without_support_type(self, remote_support_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({'remote_support_id': 0,
                                     'verify_connection': True,
                                     'state': "present"})
        remote_support_module_mock.module.params = self.get_module_args
        remote_support_module_mock.configuration.get_remote_support_details = MagicMock(
            return_value=MockRemoteSupportApi.REMOTE_SUPPORT_INTEGRATED_DETAILS)
        remote_support_module_mock.configuration.modify_remote_support_details = MagicMock(
            side_effect=MockApiException)
        remote_support_module_mock.perform_module_operation()
        print(remote_support_module_mock.module.fail_json.call_args)
        assert MockRemoteSupportApi.verify_remote_support_without_support_type_failed_msg() in \
            remote_support_module_mock.module.fail_json.call_args[1]['msg']
