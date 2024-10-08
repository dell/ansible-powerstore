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
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries. \
    fail_json import FailJsonException
from ansible_collections.dellemc.powerstore.plugins.modules.network import PowerStoreNetwork


class TestPowerstoreNetwork():

    get_module_args = MockNetworkApi.NETWORK_COMMON_ARGS

    @pytest.fixture
    def network_module_mock(self, mocker):
        mocker.patch(MockNetworkApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        network_module_mock = PowerStoreNetwork()
        network_module_mock.module = MagicMock()
        network_module_mock.check_mode = False
        return network_module_mock

    def test_get_network_response(self, network_module_mock):
        self.get_module_args.update({
            'network_id': MockNetworkApi.NW_1,
            'state': MockNetworkApi.STATE_P
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
            'state': MockNetworkApi.STATE_P
        })
        network_module_mock.module.params = self.get_module_args
        network_module_mock.configuration.get_network_details = MagicMock(
            return_value=MockNetworkApi.NETWORK_DETAILS)
        network_module_mock.perform_module_operation()
        assert self.get_module_args['network_name'] == network_module_mock.module.exit_json.call_args[1]['network_details']['name']
        network_module_mock.configuration.get_network_by_name.assert_called()

    def test_get_network_exception(self, network_module_mock):
        network_module_mock.configuration.get_network_by_name.return_value = []
        network_module_mock.configuration.get_network_details.return_value = None
        result = network_module_mock.get_network_details(network_id=MockNetworkApi.NW_1)
        assert result is None
