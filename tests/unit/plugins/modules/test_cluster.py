# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for cluster module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_cluster_api import MockClusterApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKResponse
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_powerstore_connection = MagicMock()
utils.PowerStoreException = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
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

    def test_get_non_existing_cluster_details(self, cluster_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        invalid_cluster_id = 2
        self.get_module_args.update({
            'cluster_id': invalid_cluster_id,
            'state': "present"
        })
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.configuration.get_cluster_details = MagicMock(
            side_effect=MockApiException)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.get_cluster_failed_msg() in \
            cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_invalid_physical_mtu(self, cluster_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'cluster_id': "0",
            'physical_mtu': 100,
            'state': "present"
        })
        cluster_module_mock.module.params = self.get_module_args
        cluster_module_mock.configuration.get_cluster_details = MagicMock(
            return_value=MockClusterApi.CLUSTER_DETAILS)
        cluster_module_mock.configuration.modify_cluster = MagicMock(
            side_effect=MockApiException)
        cluster_module_mock.perform_module_operation()
        assert MockClusterApi.modify_cluster_failed_msg() in \
            cluster_module_mock.module.fail_json.call_args[1]['msg']
