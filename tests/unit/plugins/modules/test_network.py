# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Network module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_network_api import MockNetworkApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_powerstore_connection = MagicMock()
utils.PowerStoreException = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerstore.plugins.modules.network import PowerStoreNetwork


class TestPowerstoreNetwork():

    get_module_args = MockNetworkApi.NETWORK_COMMON_ARGS

    @pytest.fixture
    def network_module_mock(self, mocker):
        mocker.patch(MockNetworkApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        network_module_mock = PowerStoreNetwork()
        network_module_mock.module = MagicMock()
        return network_module_mock

    def test_get_network_response(self, network_module_mock):
        self.get_module_args.update({
            'network_id': "NW1",
            'state': "present"
        })
        network_module_mock.module.params = self.get_module_args
        network_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS)
        network_module_mock.perform_module_operation()
        assert self.get_module_args['network_id'] == network_module_mock.module.exit_json.call_args[1]['network_details']['id']
        network_module_mock.configuration.get_network_details.assert_called()

    def test_get_network_name_response(self, network_module_mock):
        self.get_module_args.update({
            'network_name': "Default Management Network",
            'state': "present"
        })
        network_module_mock.module.params = self.get_module_args
        network_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS)
        network_module_mock.perform_module_operation()
        assert self.get_module_args['network_name'] == network_module_mock.module.exit_json.call_args[1]['network_details']['name']
        network_module_mock.configuration.get_network_by_name.assert_called()

    def test_delete_network(self, network_module_mock):
        self.get_module_args.update({
            'network_id': "NW1",
            'state': "absent"
        })
        network_module_mock.module.params = self.get_module_args
        network_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS)
        network_module_mock.perform_module_operation()
        assert MockNetworkApi.delete_network_failed_msg() in \
            network_module_mock.module.fail_json.call_args[1]['msg']

    def test_map_ports_network_response(self, network_module_mock):
        self.get_module_args.update({
            'network_id': "NW1",
            'ports': ["3"],
            'port_state': "present-in-network",
            'state': "present"
        })
        network_module_mock.module.params = self.get_module_args
        network_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS)
        network_module_mock.configuration.get_ip_pool_address = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS['member_ips'])
        network_module_mock.perform_module_operation()
        network_module_mock.configuration.add_remove_ports.assert_called()

    def test_map_ports_network_exception(self, network_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'network_id': "NW1",
            'ports': ["3"],
            'port_state': "present-in-network",
            'state': "present"
        })
        network_module_mock.module.params = self.get_module_args
        network_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS)
        network_module_mock.configuration.get_ip_pool_address = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS['member_ips'])
        network_module_mock.configuration.add_remove_ports = MagicMock(
            side_effect=MockApiException)
        network_module_mock.perform_module_operation()
        network_module_mock.configuration.add_remove_ports.assert_called()

    def test_unmap_ports_network_response(self, network_module_mock):
        self.get_module_args.update({
            'network_id': "NW1",
            'ports': ["1"],
            'port_state': "absent-in-network",
            'state': "present"
        })
        network_module_mock.module.params = self.get_module_args
        network_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS)
        network_module_mock.configuration.get_ip_pool_address = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS['member_ips'])
        network_module_mock.perform_module_operation()
        network_module_mock.configuration.add_remove_ports.assert_called()

    def test_unmap_ports_network_exception(self, network_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'network_id': "NW1",
            'ports': ["1"],
            'port_state': "absent-in-network",
            'state': "present"
        })
        network_module_mock.module.params = self.get_module_args
        network_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS)
        network_module_mock.configuration.get_ip_pool_address = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS['member_ips'])
        network_module_mock.configuration.add_remove_ports = MagicMock(
            side_effect=MockApiException)
        network_module_mock.perform_module_operation()
        network_module_mock.configuration.add_remove_ports.assert_called()

    def test_modify_network_response(self, network_module_mock):
        self.get_module_args.update({
            'network_id': "NW1",
            'vlan_id': "vlan_1",
            'gateway': "gateway_1",
            'prefix_length': "100",
            'mtu': "1200",
            'addresses': [
                {
                    'current_address': "10.xx.xx.xy",
                    'new_address': "10.xx.xx.xz"},
                {
                    'current_address': "10.xx.xx.yy",
                    'new_address': None},
                {
                    'current_address': None,
                    'new_address': "10.xx.xx.zz"}
            ],
            'new_cluster_mgmt_address': "array_ip",
            'vasa_provider_credentials': {
                'username': "vasa_user",
                'password': "vasa_password"},
            'esxi_credentials': [
                {
                    'node_id': "esxi_node1",
                    'password': "esxi_passwd"}
            ],
            'state': "present"
        })
        network_module_mock.module.params = self.get_module_args
        network_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS)
        network_module_mock.configuration.get_ip_pool_address = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS['member_ips'])
        network_module_mock.configuration.get_vcenter_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS['vcenter_details'])
        network_module_mock.perform_module_operation()
        network_module_mock.configuration.modify_network.assert_called()

    def test_register_vcenter_response(self, network_module_mock):
        self.get_module_args.update({
            'network_id': "NW1",
            'vlan_id': "vlan_1",
            'vasa_provider_credentials': {
                'username': "vasa_user",
                'password': "vasa_password"},
            'state': "present"
        })
        network_module_mock.module.params = self.get_module_args
        network_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS_UNREGISTERED_VCENTER)
        network_module_mock.configuration.get_vcenter_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS_UNREGISTERED_VCENTER['vcenter_details'])
        network_module_mock.perform_module_operation()
        network_module_mock.configuration.modify_network.assert_called()

    def test_register_vasa_provider_exception(self, network_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'network_id': "NW1",
            'vlan_id': "vlan_1",
            'vasa_provider_credentials': {
                'username': "vasa_user",
                'password': "vasa_password"},
            'state': "present"
        })
        network_module_mock.module.params = self.get_module_args
        network_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS_UNREGISTERED_VCENTER)
        network_module_mock.configuration.get_vcenter_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS_UNREGISTERED_VCENTER['vcenter_details'])
        network_module_mock.configuration.modify_vcenter = MagicMock(
            side_effect=MockApiException)
        network_module_mock.perform_module_operation()
        network_module_mock.configuration.modify_vcenter.assert_called()

    def test_no_vcenter_response(self, network_module_mock):
        self.get_module_args.update({
            'network_id': "NW1",
            'vlan_id': "vlan_1",
            'vasa_provider_credentials': {
                'username': "vasa_user",
                'password': "vasa_password"},
            'state': "present"
        })
        network_module_mock.module.params = self.get_module_args
        network_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS_NO_VCENTER)
        network_module_mock.configuration.get_vcenter_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS_NO_VCENTER['vcenter_details'])
        network_module_mock.perform_module_operation()
        assert MockNetworkApi.no_vcenter_failed_msg() in \
            network_module_mock.module.fail_json.call_args[1]['msg']

    def test_invalid_name_response(self, network_module_mock):
        self.get_module_args.update({
            'network_id': "NW1",
            'new_name': " ",
            'state': "present"
        })
        network_module_mock.module.params = self.get_module_args
        network_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS_NO_VCENTER)
        network_module_mock.perform_module_operation()
        assert MockNetworkApi.invalid_new_name_failed_msg() in \
            network_module_mock.module.fail_json.call_args[1]['msg']

    def test_invalid_storage_discovery_address_response(self, network_module_mock):
        self.get_module_args.update({
            'network_id': "NW1",
            'storage_discovery_address': "10.xx. xx.xx",
            'wait_for_completion': True,
            'state': "present"
        })
        network_module_mock.module.params = self.get_module_args
        network_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS_NO_VCENTER)
        network_module_mock.perform_module_operation()
        assert MockNetworkApi.invalid_storage_discovery_address_failed_msg() in \
            network_module_mock.module.fail_json.call_args[1]['msg']

    def test_invalid_current_address_response(self, network_module_mock):
        self.get_module_args.update({
            'network_id': "NW1",
            'addresses': [
                {
                    'current_address': " ",
                    'new_address': None}
            ],
            'state': "present"
        })
        network_module_mock.module.params = self.get_module_args
        network_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS_NO_VCENTER)
        network_module_mock.perform_module_operation()
        assert MockNetworkApi.invalid_current_address_failed_msg() in \
            network_module_mock.module.fail_json.call_args[1]['msg']

    def test_invalid_new_address_response(self, network_module_mock):
        self.get_module_args.update({
            'network_id': "NW1",
            'addresses': [
                {
                    'current_address': None,
                    'new_address': " "}
            ],
            'state': "present"
        })
        network_module_mock.module.params = self.get_module_args
        network_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS_NO_VCENTER)
        network_module_mock.perform_module_operation()
        assert MockNetworkApi.invalid_new_address_failed_msg() in \
            network_module_mock.module.fail_json.call_args[1]['msg']
