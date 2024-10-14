# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for cluster module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_cluster_api import MockClusterApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.cluster import PowerStoreCluster


class TestPowerstoreCluster():

    get_module_args = MockClusterApi.CLUSTER_COMMON_ARGS

    @pytest.fixture
    def cluster_module_mock(self, mocker):
        mocker.patch(MockClusterApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        cluster_module_mock = PowerStoreCluster()
        cluster_module_mock.module = MagicMock()
        return cluster_module_mock

    def test_get_cluster_response(self, cluster_module_mock):
        self.get_module_args.update({
            'cluster_id': "0",
            'state': "present"
        })
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.configuration.get_cluster_details = MagicMock(
            return_value=MockClusterApi.CLUSTER_DETAILS)
        cluster_module_mock.perform_module_operation()
        assert self.get_module_args['cluster_id'] == cluster_module_mock.module.exit_json.call_args[1]['cluster_details']['id']
        cluster_module_mock.configuration.get_cluster_details.assert_called()

    def test_get_cluster_response_cluster_name(self, cluster_module_mock):
        self.get_module_args.update({
            'cluster_name': "WX-D9023",
            'validate_create': False,
            'state': "present"
        })
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.configuration.get_cluster_details = MagicMock(
            return_value=MockClusterApi.CLUSTER_DETAILS)
        cluster_module_mock.perform_module_operation()
        assert self.get_module_args['cluster_name'] == cluster_module_mock.module.exit_json.call_args[1]['cluster_details']['name']
        cluster_module_mock.configuration.get_cluster_by_name.assert_called()

    def test_modify_cluster(self, cluster_module_mock):
        self.get_module_args.update({'cluster_id': "0",
                                     'appliance_name': "A1",
                                     'is_ssh_enabled': False,
                                     'physical_mtu': 3000,
                                     'chap_mode': "Single",
                                     'new_name': "cluster_new_name",
                                     'service_password': "sample_pass",
                                     'state': "present"})
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.perform_module_operation()
        cluster_module_mock.configuration.modify_cluster.assert_called()

    def test_modify_cluster_appliance_id_cluster_name(self, cluster_module_mock):
        self.get_module_args.update({'cluster_name': "WX-D9023",
                                     'appliance_id': "A1",
                                     'is_ssh_enabled': True,
                                     'physical_mtu': 3000,
                                     'chap_mode': "Single",
                                     'new_name': "cluster_new_name",
                                     'service_password': "sample_pass",
                                     'state': "present"})
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.configuration.get_cluster_by_name = MagicMock(
            return_value=MockClusterApi.CLUSTER_DETAILS)
        cluster_module_mock.perform_module_operation()
        assert cluster_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_cluster_is_ssh_enabled_wo_appliance_id(self, cluster_module_mock):
        self.get_module_args.update({'cluster_id': "0",
                                     'is_ssh_enabled': True,
                                     'state': "present"})
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.configuration.get_cluster_details = MagicMock(
            return_value=MockClusterApi.CLUSTER_DETAILS)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.modify_cluster_wo_appliance_failed_msg() in \
            cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_cluster_with_is_ssh_enabled_wo_appliance_negative(self, cluster_module_mock):
        self.get_module_args.update({'cluster_id': "0",
                                     'appliance_id': "A1",
                                     'state': "present"})
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.configuration.get_cluster_details = MagicMock(
            return_value=MockClusterApi.CLUSTER_DETAILS)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.modify_cluster_with_is_ssh_enabled_wo_appliance_failed_msg() in \
            cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_delete_cluster(self, cluster_module_mock):
        cluster_id = "cluster1"
        self.get_module_args.update({'cluster_id': cluster_id,
                                     'state': "absent"})
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.configuration.get_cluster_details = MagicMock(
            return_value=MockClusterApi.CLUSTER_DETAILS)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.delete_cluster_failed_msg() in \
            cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_cluster_list_exception(self, cluster_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'cluster_id': 0,
            'create_validate': False,
            'state': "present"
        })
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            side_effect=MockApiException)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.get_cluster_list_failed_msg() in \
            cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_invalid_physical_mtu(self, cluster_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'cluster_id': "0",
            'physical_mtu': 100,
            'validate_create': False,
            'state': "present"
        })
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST)
        cluster_module_mock.configuration.get_cluster_details = MagicMock(
            return_value=MockClusterApi.CLUSTER_DETAILS)
        cluster_module_mock.configuration.modify_cluster = MagicMock(
            side_effect=MockApiException)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.modify_cluster_failed_msg() in \
            cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_validate_create_cluster(self, cluster_module_mock):
        self.get_module_args.update(MockClusterApi.MODIFIED_PARAMS)
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST_1)
        cluster_module_mock.perform_module_operation()
        cluster_module_mock.configuration.cluster_create_validate.assert_called()

    def test_create_cluster(self, cluster_module_mock):
        MockClusterApi.MODIFIED_PARAMS['validate_create'] = False
        MockClusterApi.MODIFIED_PARAMS['wait_for_completion'] = True
        self.get_module_args.update(MockClusterApi.MODIFIED_PARAMS)
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST_1)
        cluster_module_mock.perform_module_operation()
        cluster_module_mock.configuration.cluster_create.assert_called()

    def test_cluster_less_than_3_network_address(self, cluster_module_mock):
        self.get_module_args.update(MockClusterApi.MODIFIED_PARAMS)
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST_1)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.cluster_addr_less_3_failed_msg() in \
               cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_cluster_more_than_3_dns(self, cluster_module_mock):
        MockClusterApi.MODIFIED_PARAMS['dns_servers'] = [
            MockClusterApi.address_1, MockClusterApi.address_1,
            MockClusterApi.address_1, MockClusterApi.address_1]
        MockClusterApi.MODIFIED_PARAMS['networks'][0]['addresses'] = [
            MockClusterApi.address_1, MockClusterApi.address_1,
            MockClusterApi.address_1]
        self.get_module_args.update(MockClusterApi.MODIFIED_PARAMS)
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST_1)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.dns_ntp_more_than_3_failed_msg() in \
               cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_cluster_more_than_3_ntp(self, cluster_module_mock):
        MockClusterApi.MODIFIED_PARAMS['ntp_servers'] = [
            MockClusterApi.address_1, MockClusterApi.address_1,
            MockClusterApi.address_1, MockClusterApi.address_1]
        MockClusterApi.MODIFIED_PARAMS['networks'][0]['addresses'] = [
            MockClusterApi.address_1, MockClusterApi.address_1,
            MockClusterApi.address_1]
        self.get_module_args.update(MockClusterApi.MODIFIED_PARAMS)
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST_1)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.dns_ntp_more_than_3_failed_msg() in \
               cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_cluster_invalid_link_local_address(self, cluster_module_mock):
        MockClusterApi.MODIFIED_PARAMS['appliances'][
            0]['link_local_address'] = MockClusterApi.invalid_address_1
        MockClusterApi.MODIFIED_PARAMS['networks'][0]['addresses'] = [
            MockClusterApi.address_1, MockClusterApi.address_1,
            MockClusterApi.address_1]
        self.get_module_args.update(MockClusterApi.MODIFIED_PARAMS)
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST_1)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.link_local_address_failed_msg() in \
               cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_cluster_invalid_appliance_name(self, cluster_module_mock):
        MockClusterApi.MODIFIED_PARAMS['appliances'][0]['name'] = MockClusterApi.invalid_name
        MockClusterApi.MODIFIED_PARAMS['networks'][0]['addresses'] = [
            MockClusterApi.address_1, MockClusterApi.address_1,
            MockClusterApi.address_1]
        self.get_module_args.update(MockClusterApi.MODIFIED_PARAMS)
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST_1)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.appliance_name_failed_msg() in \
               cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_cluster_with_invalid_address_for_switch(self, cluster_module_mock):
        MockClusterApi.MODIFIED_PARAMS['physical_switches'] = [{
            'name': 'test-appliance',
            'purpose': 'Management_Only',
            'connections': [{
                'address': ' ',
                'connect_method': 'SSH',
                'username': 'user',
                'ssh_password': 'xxxx'
            }]
        }]
        MockClusterApi.MODIFIED_PARAMS['networks'][0]['addresses'] = [
            MockClusterApi.address_1, MockClusterApi.address_1,
            MockClusterApi.address_1]
        self.get_module_args.update(MockClusterApi.MODIFIED_PARAMS)
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST_1)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.not_address_failed_msg() in \
               cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_cluster_response_empty_cluster_name(self, cluster_module_mock):
        self.get_module_args.update({
            'cluster_name': " ",
            'state': "present"
        })
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST_1)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.invalid_cluster_name_failed_msg() in \
               cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_cluster_with_invalid_vcenter_address(self, cluster_module_mock):
        MockClusterApi.MODIFIED_PARAMS['vcenters'] = [{
            'address': '  ',
            'username': 'user',
            'password': 'xxxx',
            'is_verify_server_cert': True,
            'vasa_provider_credentials': {
                'username': 'user',
                'password': 'xxxx'
            }
        }]
        MockClusterApi.MODIFIED_PARAMS['networks'][0]['addresses'] = [
            MockClusterApi.address_1, MockClusterApi.address_1,
            MockClusterApi.address_1]
        self.get_module_args.update(MockClusterApi.MODIFIED_PARAMS)
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST_1)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.invalid_vcenter_address_failed_msg() in \
               cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_cluster_with_invalid_switch_name(self, cluster_module_mock):
        MockClusterApi.MODIFIED_PARAMS['physical_switches'] = [{
            'name': MockClusterApi.invalid_name,
            'purpose': 'Management_Only',
            'connections': [{
                'address': MockClusterApi.address_1,
                'connect_method': 'SSH',
                'username': 'user',
                'ssh_password': 'xxxx'
            }]
        }]
        MockClusterApi.MODIFIED_PARAMS['networks'][0]['addresses'] = [
            MockClusterApi.address_1, MockClusterApi.address_1,
            MockClusterApi.address_1]
        self.get_module_args.update(MockClusterApi.MODIFIED_PARAMS)
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST_1)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.invalid_switch_name_failed_msg() in \
               cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_cluster_without_connections(self, cluster_module_mock):
        MockClusterApi.MODIFIED_PARAMS['physical_switches'] = [{
            'name': 'phy_switch_name',
            'purpose': 'Management_Only',
            'connections': []
        }]
        MockClusterApi.MODIFIED_PARAMS['networks'][0]['addresses'] = [
            MockClusterApi.address_1, MockClusterApi.address_1,
            MockClusterApi.address_1]
        self.get_module_args.update(MockClusterApi.MODIFIED_PARAMS)
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST_1)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.invalid_empty_connections_failed_msg() in \
               cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_cluster_without_mgmt_cluster_address(self, cluster_module_mock):
        MockClusterApi.MODIFIED_PARAMS['networks'][
            0]['cluster_mgmt_address'] = None
        MockClusterApi.MODIFIED_PARAMS['networks'][0]['addresses'] = [
            MockClusterApi.address_1, MockClusterApi.address_1,
            MockClusterApi.address_1]
        self.get_module_args.update(MockClusterApi.MODIFIED_PARAMS)
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST_1)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.without_mgmt_cluster_address_failed_msg() in \
               cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_cluster_with_invalid_cluster_mgmt(self, cluster_module_mock):
        MockClusterApi.MODIFIED_PARAMS['networks'][
            0]['cluster_mgmt_address'] = MockClusterApi.invalid_address_1
        MockClusterApi.MODIFIED_PARAMS['networks'][0]['addresses'] = [
            MockClusterApi.address_1, MockClusterApi.address_1,
            MockClusterApi.address_1]
        self.get_module_args.update(MockClusterApi.MODIFIED_PARAMS)
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST_1)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.invalid_cluster_address_failed_msg() in \
               cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_cluster_with_invalid_storage_discovery(self, cluster_module_mock):
        MockClusterApi.MODIFIED_PARAMS['networks'][0]['addresses'] = [
            MockClusterApi.address_1, MockClusterApi.address_1,
            MockClusterApi.address_1]
        MockClusterApi.MODIFIED_PARAMS['networks'].append(MockClusterApi.NET_DICT)
        self.get_module_args.update(MockClusterApi.MODIFIED_PARAMS)
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST_1)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.invalid_storage_address_failed_msg() in \
               cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_cluster_with_storage_discovery_in_mgmt_network(self, cluster_module_mock):
        MockClusterApi.MODIFIED_PARAMS['networks'][
            0]['storage_discovery_address'] = MockClusterApi.invalid_address_1
        MockClusterApi.MODIFIED_PARAMS['networks'][0]['addresses'] = [
            MockClusterApi.address_1, MockClusterApi.address_1,
            MockClusterApi.address_1]
        self.get_module_args.update(MockClusterApi.MODIFIED_PARAMS)
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST_1)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.storage_address_in_mgmt_network_failed_msg() in \
               cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_appliance_exception(self, cluster_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({'cluster_name': MockClusterApi.cluster_name,
                                     'appliance_id': "A1",
                                     'is_ssh_enabled': True,
                                     'physical_mtu': 3000,
                                     'state': "present"})
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST_1)
        cluster_module_mock.configuration.get_cluster_by_name = MagicMock(
            return_value=MockClusterApi.CLUSTER_DETAILS)
        cluster_module_mock.configuration.get_appliance_details = MagicMock(
            side_effect=MockApiException)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.appliance_failed_msg() in \
               cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_service_user_exception(self, cluster_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({'cluster_name': MockClusterApi.cluster_name,
                                     'appliance_id': "A1",
                                     'is_ssh_enabled': True,
                                     'physical_mtu': 3000,
                                     'state': "present"})
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST)
        cluster_module_mock.get_appliance_details = MagicMock(
            return_values=MockClusterApi.APPLIANCE_DETAILS)
        cluster_module_mock.get_cluster_details = MagicMock(
            return_value=MockClusterApi.CLUSTER_DETAILS)
        cluster_module_mock.configuration.get_service_user_details = MagicMock(
            side_effect=MockApiException)
        cluster_module_mock.get_appliance_details = MagicMock(
            return_values=MockClusterApi.APPLIANCE_DETAILS)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.service_user_failed_msg() in \
               cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_cluster_with_data_center_name_id(self, cluster_module_mock):
        MockClusterApi.MODIFIED_PARAMS['vcenters'] = [{
            'address': MockClusterApi.address_1,
            'username': 'user',
            'password': 'xxxx',
            'data_center_name': 'center_name',
            'data_center_id': 'center_id',
            'is_verify_server_cert': True,
            'vasa_provider_credentials': {
                'username': 'user',
                'password': 'xxxx'
            }
        }]
        MockClusterApi.MODIFIED_PARAMS['networks'][0]['addresses'] = [
            MockClusterApi.address_1, MockClusterApi.address_1,
            MockClusterApi.address_1]
        self.get_module_args.update(MockClusterApi.MODIFIED_PARAMS)
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockClusterApi.CLUSTER_LIST_1)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.data_center_name_id_failed_msg() in \
               cluster_module_mock.module.fail_json.call_args[1]['msg']
