# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Host Group module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_hostgroup_api import MockHostGroupApi
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
from ansible_collections.dellemc.powerstore.plugins.modules.hostgroup import PowerStoreHostgroup


class TestPowerstoreHostGroup():

    get_module_args = MockHostGroupApi.HOSTGROUP_COMMON_ARGS
    iscsi_initiator_1 = "iqn.1998-01.com.vmware:xxxxxxxxx-xxxxfb37"
    iscsi_initiator_2 = "iqn.1998-01.com.vmware:xxxxxxxxx-xxxxfb38"
    nvme_initiator_1 = "nqn.2014-08.org.nvmexpress:uuid:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx18f4"
    fc_initiator_1 = "21:00:00:XX:XX:XX:XX:XX"

    @pytest.fixture
    def hostgroup_module_mock(self, mocker):
        mocker.patch(MockHostGroupApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        hostgroup_module_mock = PowerStoreHostgroup()
        hostgroup_module_mock.module = MagicMock()
        return hostgroup_module_mock

    def test_get_hostgroup_response(self, hostgroup_module_mock):
        self.get_module_args.update({
            'hostgroup_id': "d21beab9-15fa-4cee-9651-e3b740ceaa7c",
            'state': "present"
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_details = MagicMock(
            return_value=MockHostGroupApi.HOSTGROUP_DETAILS)
        hostgroup_module_mock.perform_module_operation()
        assert self.get_module_args['hostgroup_id'] == hostgroup_module_mock.module.exit_json.call_args[1]['hostgroup_details']['id']
        hostgroup_module_mock.conn.provisioning.get_host_group_details.assert_called()

    def test_get_hostgroup_response_by_name(self, hostgroup_module_mock):
        self.get_module_args.update({
            'hostgroup_name': MockHostGroupApi.HOSTGROUP_NAME_1,
            'state': "present"
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_details = MagicMock(
            return_value=MockHostGroupApi.HOSTGROUP_DETAILS)
        hostgroup_module_mock.perform_module_operation()
        assert self.get_module_args['hostgroup_name'] == hostgroup_module_mock.module.exit_json.call_args[1]['hostgroup_details']['name']
        hostgroup_module_mock.conn.provisioning.get_host_group_by_name.assert_called()

    def test_get_non_existing_hostgroup_by_id(self, hostgroup_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'hostgroup_id': "Non_existng_hostgroup",
            'state': "present"
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_details = MagicMock(
            side_effect=MockApiException)
        hostgroup_module_mock.perform_module_operation()
        hostgroup_module_mock.conn.provisioning.get_host_group_details.assert_called()

    def test_get_non_existing_hostgroup_by_name(self, hostgroup_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'hostgroup_name': "Non_existng_hostgroup",
            'state': "present"
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_by_name = MagicMock(
            side_effect=MockApiException)
        hostgroup_module_mock.perform_module_operation()
        hostgroup_module_mock.conn.provisioning.get_host_group_by_name.assert_called()

    def test_get_hostgroup_details_by_name_more_than_one_hostgroup(self, hostgroup_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'hostgroup_name': "Sample_hostgroup_1",
            'state': "present"
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_by_name = MagicMock(
            return_value=MockHostGroupApi.HOSTGROUP_DETAILS_TWO)
        hostgroup_module_mock.perform_module_operation()
        print(hostgroup_module_mock.module.fail_json.call_args[1]['msg'])
        assert MockHostGroupApi.get_hostgroup_more_than_one_failed_msg() in \
            hostgroup_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_hostgroup(self, hostgroup_module_mock):
        self.get_module_args.update({
            'hostgroup_name': "Sample_hostgroup_2",
            'hosts': ['host1', 'host2'],
            'host_state': 'present-in-group',
            'state': 'present'
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_by_name = MagicMock(
            return_value=None)
        hostgroup_module_mock.perform_module_operation()
        assert hostgroup_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_hostgroup_exception(self, hostgroup_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'hostgroup_name': "Sample_hostgroup_2",
            'hosts': ['host1', 'host2'],
            'host_state': 'present-in-group',
            'state': 'present'
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_by_name = MagicMock(
            return_value=None)
        hostgroup_module_mock.conn.provisioning.create_host_group = MagicMock(
            side_effect=MockApiException)
        hostgroup_module_mock.perform_module_operation()
        hostgroup_module_mock.conn.provisioning.create_host_group.assert_called()

    def test_create_hostgroup_wo_host(self, hostgroup_module_mock):
        self.get_module_args.update({
            'hostgroup_name': "Sample_hostgroup_2",
            'hosts': [],
            'host_state': 'present-in-group',
            'state': 'present'
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_by_name = MagicMock(
            return_value=None)
        hostgroup_module_mock.perform_module_operation()
        assert MockHostGroupApi.create_hostgroup_wo_host_failed_msg() in \
            hostgroup_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_hostgroup_two_hosts_same_name(self, hostgroup_module_mock):
        self.get_module_args.update({
            'hostgroup_name': "Sample_hostgroup_2",
            'hosts': ['Sample_host_1'],
            'host_state': 'present-in-group',
            'state': 'present'
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_by_name = MagicMock(
            return_value=None)
        hostgroup_module_mock.conn.provisioning.get_host_by_name = MagicMock(
            return_value=MockHostGroupApi.HOST_DETAILS_TWO)
        hostgroup_module_mock.perform_module_operation()
        hostgroup_module_mock.conn.provisioning.get_host_by_name.assert_called()

    def test_create_hostgroup_non_existing_host(self, hostgroup_module_mock):
        self.get_module_args.update({
            'hostgroup_name': "Sample_host_2",
            'hosts': ['non_existing_host'],
            'host_state': 'present-in-group',
            'state': 'present'
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_by_name = MagicMock(
            return_value=None)
        hostgroup_module_mock.conn.provisioning.get_host_by_name = MagicMock(
            side_effect=MockApiException)
        hostgroup_module_mock.perform_module_operation()
        hostgroup_module_mock.conn.provisioning.get_host_by_name.assert_called()

    def test_create_hostgroup_absent_host(self, hostgroup_module_mock):
        self.get_module_args.update({
            'hostgroup_name': "Sample_host_2",
            'hosts': ['host1', 'host2'],
            'host_state': 'absent-in-group',
            'state': 'present'
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_by_name = MagicMock(
            return_value=None)
        hostgroup_module_mock.perform_module_operation()
        assert MockHostGroupApi.create_hostgroup_absent_host_failed_msg() in \
            hostgroup_module_mock.module.fail_json.call_args[1]['msg']

    def test_add_host(self, hostgroup_module_mock):
        self.get_module_args.update({
            'hostgroup_id': "d21beab9-15fa-4cee-9651-e3b740ceaa7c",
            'hosts': ['bdd5e201-153c-4b86-b35e-394db0c4851e'],
            'host_state': 'present-in-group',
            'state': 'present'
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_details = MagicMock(
            return_value=MockHostGroupApi.HOSTGROUP_DETAILS_2)
        hostgroup_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostGroupApi.HOST_DETAILS_2)
        hostgroup_module_mock.perform_module_operation()
        hostgroup_module_mock.conn.provisioning.add_hosts_to_host_group.assert_called()

    def test_add_host_exception(self, hostgroup_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'hostgroup_id': "d21beab9-15fa-4cee-9651-e3b740ceaa7c",
            'hosts': ['bdd5e201-153c-4b86-b35e-394db0c4851e'],
            'host_state': 'present-in-group',
            'state': 'present'
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_details = MagicMock(
            return_value=MockHostGroupApi.HOSTGROUP_DETAILS_2)
        hostgroup_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostGroupApi.HOST_DETAILS_2)
        hostgroup_module_mock.conn.provisioning.add_hosts_to_host_group = MagicMock(
            side_effect=MockApiException)
        hostgroup_module_mock.perform_module_operation()
        hostgroup_module_mock.conn.provisioning.add_hosts_to_host_group.assert_called()

    def test_add_non_existing_host(self, hostgroup_module_mock):
        self.get_module_args.update({
            'hostgroup_id': "d21beab9-15fa-4cee-9651-e3b740ceaa7c",
            'hosts': ['Host3'],
            'host_state': 'present-in-group',
            'state': 'present'
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_details = MagicMock(
            return_value=MockHostGroupApi.HOSTGROUP_DETAILS_2)
        hostgroup_module_mock.conn.provisioning.get_host_by_name = MagicMock(
            side_effect=MockApiException)
        hostgroup_module_mock.perform_module_operation()
        hostgroup_module_mock.conn.provisioning.get_host_by_name.assert_called()

    def test_remove_host(self, hostgroup_module_mock):
        self.get_module_args.update({
            'hostgroup_id': "d21beab9-15fa-4cee-9651-e3b740ceaa7c",
            'hosts': ['bdd5e201-153c-4b86-b35e-394db0c4851e'],
            'host_state': 'absent-in-group',
            'state': 'present'
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_details = MagicMock(
            return_value=MockHostGroupApi.HOSTGROUP_DETAILS)
        hostgroup_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostGroupApi.HOST_DETAILS_2)
        hostgroup_module_mock.perform_module_operation()
        hostgroup_module_mock.conn.provisioning.remove_hosts_from_host_group.assert_called()

    def test_remove_host_exception(self, hostgroup_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'hostgroup_id': "d21beab9-15fa-4cee-9651-e3b740ceaa7c",
            'hosts': ['bdd5e201-153c-4b86-b35e-394db0c4851e'],
            'host_state': 'absent-in-group',
            'state': 'present'
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_details = MagicMock(
            return_value=MockHostGroupApi.HOSTGROUP_DETAILS)
        hostgroup_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostGroupApi.HOST_DETAILS_2)
        hostgroup_module_mock.conn.provisioning.remove_hosts_from_host_group = MagicMock(
            side_effect=MockApiException)
        hostgroup_module_mock.perform_module_operation()
        hostgroup_module_mock.conn.provisioning.remove_hosts_from_host_group.assert_called()

    def test_remove_host_hostgroup_no_hosts(self, hostgroup_module_mock):
        self.get_module_args.update({
            'hostgroup_id': "d21beab9-15fa-4cee-9651-e3b740ceaa7e",
            'hosts': ['bdd5e201-153c-4b86-b35e-394db0c4851e'],
            'host_state': 'absent-in-group',
            'state': 'present'
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_details = MagicMock(
            return_value=MockHostGroupApi.HOSTGROUP_DETAILS_NO_HOSTS)
        hostgroup_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostGroupApi.HOST_DETAILS_2)
        hostgroup_module_mock.perform_module_operation()
        hostgroup_module_mock.conn.provisioning.get_host_group_details.assert_called()

    def test_modify_hostgroup(self, hostgroup_module_mock):
        self.get_module_args.update({
            'hostgroup_id': "d21beab9-15fa-4cee-9651-e3b740ceaa7c",
            'new_name': "Hostgroup_new_name",
            'host_connectivity': MockHostGroupApi.HOST_CONNECTIVITY,
            'state': 'present'
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_details = MagicMock(
            return_value=MockHostGroupApi.HOSTGROUP_DETAILS)
        hostgroup_module_mock.perform_module_operation()
        hostgroup_module_mock.conn.provisioning.modify_host_group.assert_called()

    def test_rename_hostgroup_exception(self, hostgroup_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'hostgroup_id': "d21beab9-15fa-4cee-9651-e3b740ceaa7c",
            'new_name': "Hostgroup_new_name",
            'state': 'present'
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_details = MagicMock(
            return_value=MockHostGroupApi.HOSTGROUP_DETAILS)
        hostgroup_module_mock.conn.provisioning.modify_host_group = MagicMock(
            side_effect=MockApiException)
        hostgroup_module_mock.perform_module_operation()
        hostgroup_module_mock.conn.provisioning.modify_host_group.assert_called()

    def test_delete_hostgroup(self, hostgroup_module_mock):
        self.get_module_args.update({
            'hostgroup_name': MockHostGroupApi.HOSTGROUP_NAME_1,
            'state': "absent"
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_details = MagicMock(
            return_value=MockHostGroupApi.HOSTGROUP_DETAILS)
        hostgroup_module_mock.perform_module_operation()
        hostgroup_module_mock.conn.provisioning.delete_host_group.assert_called()

    def test_delete_hostgroup_exception(self, hostgroup_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'hostgroup_name': MockHostGroupApi.HOSTGROUP_NAME_1,
            'state': "absent"
        })
        hostgroup_module_mock.module.params = self.get_module_args
        hostgroup_module_mock.conn.provisioning.get_host_group_details = MagicMock(
            return_value=MockHostGroupApi.HOSTGROUP_DETAILS)
        hostgroup_module_mock.conn.provisioning.delete_host_group = MagicMock(
            side_effect=MockApiException)
        hostgroup_module_mock.perform_module_operation()
        hostgroup_module_mock.conn.provisioning.delete_host_group.assert_called()
