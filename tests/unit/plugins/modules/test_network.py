# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Network module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_network_api import MockNetworkApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries.powerstore_unit_base \
    import PowerStoreUnitBase
from ansible_collections.dellemc.powerstore.plugins.modules.network import PowerStoreNetwork


class TestPowerstoreNetwork(PowerStoreUnitBase):

    get_module_args = MockNetworkApi.NETWORK_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerStoreNetwork

    def test_get_network_response(self, powerstore_module_mock):
        self.get_module_args.update({
            'network_id': MockNetworkApi.NW_1,
            'state': MockNetworkApi.STATE_P
        })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS)
        powerstore_module_mock.perform_module_operation()
        assert self.get_module_args['network_id'] == powerstore_module_mock.module.exit_json.call_args[1]['network_details']['id']
        powerstore_module_mock.configuration.get_network_details.assert_called()

    def test_get_network_name_response(self, powerstore_module_mock):
        self.set_module_params(powerstore_module_mock,
                               self.get_module_args,
                               {'network_name': "Default Management Network",
                                'state': MockNetworkApi.STATE_P})
        powerstore_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS)
        powerstore_module_mock.check_array_version = MagicMock()
        powerstore_module_mock.perform_module_operation()
        assert self.get_module_args['network_name'] == powerstore_module_mock.module.exit_json.call_args[1]['network_details']['name']
        powerstore_module_mock.configuration.get_network_by_name.assert_called()

    def test_get_network_exception(self, powerstore_module_mock):
        powerstore_module_mock.configuration.get_network_by_name.return_value = []
        powerstore_module_mock.configuration.get_network_details.return_value = None
        result = powerstore_module_mock.get_network_details(network_id=MockNetworkApi.NW_1)
        assert result is None

    def test_get_vcenter_exception(self, powerstore_module_mock):
        self.get_module_args.update({
            'network_id': MockNetworkApi.NW_1,
            'state': MockNetworkApi.STATE_P
        })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS)
        powerstore_module_mock.configuration.get_vcenter_details = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call("Failed to get the vcenter details with error",
                                    powerstore_module_mock,
                                    invoke_perform_module=True)
        powerstore_module_mock.configuration.get_vcenter_details.assert_called()

    def test_get_member_ips_exception(self, powerstore_module_mock):
        self.get_module_args.update({
            'network_id': MockNetworkApi.NW_1,
            'state': MockNetworkApi.STATE_P
        })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS)
        powerstore_module_mock.configuration.get_ip_pool_address = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call("Failed to get the member IPs of NW_1 with error",
                                    powerstore_module_mock,
                                    invoke_perform_module=True)
        powerstore_module_mock.configuration.get_ip_pool_address.assert_called()

    def test_get_cluster_details_exception(self, powerstore_module_mock):
        powerstore_module_mock.configuration.get_cluster_details = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            "Failed to get the cluster details with error",
            powerstore_module_mock, "get_cluster_details")

    def test_getnetwork_exception(self, powerstore_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "500"
        self.get_module_args.update({
            'network_id': MockNetworkApi.NW_1,
            'state': MockNetworkApi.STATE_P
        })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.configuration.get_network_details = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call("Get details of network NW_1 failed with error",
                                    powerstore_module_mock,
                                    invoke_perform_module=True)

    def test_add_ports(self, powerstore_module_mock):
        network_details = MockNetworkApi.NETWORK_DETAILS
        ports = ['222', '333']

        result = powerstore_module_mock.add_ports_to_network(network_details, ports)

        assert result is True
        powerstore_module_mock.configuration.add_remove_ports.assert_called()

    def test_add_ports_to_network_no_ports_to_add(self, powerstore_module_mock):
        network_details = {'id': '123', 'member_ips': [{'ip_port_id': '456'}, {'ip_port_id': '789'}]}
        ports = ['456', '789']

        result = powerstore_module_mock.add_ports_to_network(network_details, ports)

        assert result is False

    def test_add_ports_to_network_exception(self, powerstore_module_mock):
        powerstore_module_mock.configuration.add_remove_ports.side_effect = MockApiException
        network_details = MockNetworkApi.NETWORK_DETAILS
        ports = ['222', '333']

        self.capture_fail_json_method(
            "Add existing IP ports to storage network NW_1 failed with error",
            powerstore_module_mock, "add_ports_to_network",
            network_details, ports)

    def test_remove_ports(self, powerstore_module_mock):
        network_details = MockNetworkApi.NETWORK_DETAILS
        ports = ['0', '1']

        result = powerstore_module_mock.remove_ports_from_network(network_details, ports)

        assert result is True
        powerstore_module_mock.configuration.add_remove_ports.assert_called()

    def test_remove_ports_to_network_no_ports_to_remove(self, powerstore_module_mock):
        network_details = MockNetworkApi.NETWORK_DETAILS
        ports = ['456', '789']

        result = powerstore_module_mock.remove_ports_from_network(network_details, ports)

        assert result is False

    def test_remove_ports_to_network_exception(self, powerstore_module_mock):
        powerstore_module_mock.configuration.add_remove_ports.side_effect = MockApiException
        network_details = MockNetworkApi.NETWORK_DETAILS
        ports = ['0', '1']

        self.capture_fail_json_method(
            "Remove existing IP ports from storage network NW_1 failed with error",
            powerstore_module_mock, "remove_ports_from_network",
            network_details, ports)

    def test_modify_network(self, powerstore_module_mock):
        # Mock the necessary inputs
        network_id = MockNetworkApi.NW_1
        wait_for_completion = True
        network_modify_dict = {'name': 'new_name', 'description': 'new_description'}
        network_details = MockNetworkApi.NETWORK_DETAILS

        # Mock the necessary return values
        powerstore_module_mock.configuration.modify_network.return_value = {'id': MockNetworkApi.NW_1, 'name': 'new_name', 'description': 'new_description'}

        # Call the function
        result, job_dict = powerstore_module_mock.modify_network(network_id, wait_for_completion, network_modify_dict, network_details)

        # Assert the expected behavior
        assert result is True
        assert job_dict == {'id': MockNetworkApi.NW_1, 'name': 'new_name', 'description': 'new_description'}
        powerstore_module_mock.configuration.modify_network.assert_called()

    def test_modify_network_exception(self, powerstore_module_mock):
        # Mock the necessary inputs
        network_id = MockNetworkApi.NW_1
        wait_for_completion = True
        network_modify_dict = {'name': 'new_name', 'description': 'new_description'}
        network_details = MockNetworkApi.NETWORK_DETAILS

        powerstore_module_mock.configuration.modify_network.side_effect = MockApiException

        self.capture_fail_json_method(
            "Modify operation of network with id: NW_1, failed with error",
            powerstore_module_mock, "modify_network",
            network_id, wait_for_completion, network_modify_dict, network_details)

    def test_register_vasa(self, powerstore_module_mock):
        vcenter_id = MockNetworkApi.VASA_ID
        vasa_provider_credentials = {'username': 'username', 'password': 'password'}
        result = powerstore_module_mock.register_vasa_provider(vcenter_id, vasa_provider_credentials)
        assert result is True
        powerstore_module_mock.configuration.modify_vcenter.assert_called()

    def test_register_vasa_exception(self, powerstore_module_mock):
        vcenter_id = MockNetworkApi.VASA_ID
        vasa_provider_credentials = {'username': 'username', 'password': 'password'}
        powerstore_module_mock.configuration.modify_vcenter.side_effect = MockApiException
        self.capture_fail_json_method(
            "VASA provider registration of vcenter with id: 0d330, failed with error",
            powerstore_module_mock, "register_vasa_provider",
            vcenter_id, vasa_provider_credentials)

    def test_check_array_version(self, powerstore_module_mock):
        network_name = MockNetworkApi.NW_1
        release_version = '2.1.0.0'

        # Mock the necessary return values
        powerstore_module_mock.provisioning.get_array_version.return_value = release_version

        # Call the function
        powerstore_module_mock.check_array_version(network_name)
        powerstore_module_mock.provisioning.get_array_version.assert_called()

    def test_check_array_version_failure(self, powerstore_module_mock):
        network_name = MockNetworkApi.NW_1
        release_version = '1.0.0.0'

        powerstore_module_mock.provisioning.get_array_version.return_value = release_version

        self.capture_fail_json_method(
            "Please provide network_id. Network name can be used with PowerStore release >= 2.0.0.0.",
            powerstore_module_mock, "check_array_version",
            network_name)

    def test_check_array_version_exception(self, powerstore_module_mock):
        network_name = MockNetworkApi.NW_1

        powerstore_module_mock.provisioning.get_array_version.side_effect = Exception('Some error')

        self.capture_fail_json_method(
            "Failed to get the array version with error Some error",
            powerstore_module_mock, "check_array_version",
            network_name)

    @pytest.mark.parametrize("assert_data", [
        {
            "addresses": [{"current_address": "", "new_address": "2.2.2.2"}],
            "expected_err": MockNetworkApi.CURRENT_ADDR_ERR
        },
        {
            "addresses": [{"current_address": "1.1.1.1", "new_address": ""}],
            "expected_err": MockNetworkApi.NEW_ADDR_ERR
        }
    ])
    def test_validate_addresses(self, powerstore_module_mock, assert_data):
        addresses = assert_data["addresses"]
        expected_value = assert_data["expected_err"]
        self.capture_fail_json_method(
            expected_value,
            powerstore_module_mock, "validate_address",
            addresses=addresses)
