# Copyright: (c) 2021, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Host module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_host_api import MockHostApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_powerstore_connection = MagicMock()
utils.PowerStoreException = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerstore.plugins.modules.host import PowerStoreHost


class TestPowerstoreHost():

    get_module_args = MockHostApi.HOST_COMMON_ARGS
    iscsi_initiator_1 = "iqn.1998-01.com.vmware:lgc198248-5b06fb37"
    iscsi_initiator_2 = "iqn.1998-01.com.vmware:lgc198248-5b06fb38"
    nvme_initiator_1 = "nqn.2014-08.org.nvmexpress:uuid:7936206c-9c51-4bf4-86b6-f4e2803218f4"
    fc_initiator_1 = "21:00:00:XX:XX:XX:XX:XX"

    @pytest.fixture
    def host_module_mock(self, mocker):
        mocker.patch(MockHostApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        host_module_mock = PowerStoreHost()
        host_module_mock.module = MagicMock()
        return host_module_mock

    def test_get_host_response(self, host_module_mock):
        self.get_module_args.update({
            'host_id': "4d56e60-fc10-4f51-a698-84a664562f0d",
            'state': "present"
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        host_module_mock.perform_module_operation()
        assert self.get_module_args['host_id'] == host_module_mock.module.exit_json.call_args[1]['host_details']['id']
        host_module_mock.conn.provisioning.get_host_details.assert_called()

    def test_get_host_response_by_name(self, host_module_mock):
        self.get_module_args.update({
            'host_name': MockHostApi.HOST_NAME_1,
            'state': "present"
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        host_module_mock.perform_module_operation()
        assert self.get_module_args['host_name'] == host_module_mock.module.exit_json.call_args[1]['host_details']['name']
        host_module_mock.conn.provisioning.get_host_by_name.assert_called()

    def test_get_host_details_by_name_more_than_one_host(self, host_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'host_name': "Sample_host",
            'state': "present"
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_by_name = MagicMock(
            return_value=MockHostApi.HOST_DETAILS_TWO)
        host_module_mock.perform_module_operation()
        assert MockHostApi.get_host_more_than_one_failed_msg() in \
            host_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_host(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_2",
            'os_type': 'ESXi',
            'detailed_initiators': [{
                'port_name': self.iscsi_initiator_1,
                'port_type': 'iSCSI',
                'chap_single_username': 'chapuserSingle',
                'chap_single_password': 'chappasswd12345'}],
            'state': 'present',
            'host_connectivity': 'Local_Only',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_by_name = MagicMock(
            return_value=None)
        host_module_mock.perform_module_operation()
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_host_wo_port_type_iscsi(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_2",
            'os_type': 'ESXi',
            'detailed_initiators': [{
                'port_name': self.iscsi_initiator_1,
                'port_type': None,
                'chap_single_username': 'chapuserSingle',
                'chap_single_password': 'chappasswd12345'}],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_by_name = MagicMock(
            return_value=None)
        host_module_mock.perform_module_operation()
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_host_wo_port_type_nvme_wo_port_type(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_2",
            'os_type': 'ESXi',
            'detailed_initiators': [{
                'port_name': self.nvme_initiator_1,
                'port_type': None,
                'chap_single_username': 'chapuserSingle',
                'chap_single_password': 'chappasswd12345'}],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_by_name = MagicMock(
            return_value=None)
        host_module_mock.perform_module_operation()
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_host_wo_port_type_nvme(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_2",
            'os_type': 'ESXi',
            'detailed_initiators': [{
                'port_name': self.nvme_initiator_1,
                'port_type': "NVMe",
                'chap_single_username': 'chapuserSingle',
                'chap_single_password': 'chappasswd12345'}],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_by_name = MagicMock(
            return_value=None)
        host_module_mock.perform_module_operation()
        host_module_mock.conn.provisioning.create_host.assert_called()

    def test_create_host_fc_detailed_initiator_wo_port_type(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_2",
            'os_type': 'ESXi',
            'detailed_initiators': [{
                'port_name': self.fc_initiator_1,
                'port_type': None,
                'chap_single_username': 'chapuserSingle',
                'chap_single_password': 'chappasswd12345'}],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_by_name = MagicMock(
            return_value=None)
        host_module_mock.perform_module_operation()
        host_module_mock.conn.provisioning.create_host.assert_called()

    def test_create_host_fc_detailed_initiator(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_2",
            'os_type': 'ESXi',
            'detailed_initiators': [{
                'port_name': self.fc_initiator_1,
                'port_type': "FC",
                'chap_single_username': 'chapuserSingle',
                'chap_single_password': 'chappasswd12345'}],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_by_name = MagicMock(
            return_value=None)
        host_module_mock.perform_module_operation()
        host_module_mock.conn.provisioning.create_host.assert_called()

    def test_create_host_with_fc_initiators(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_3",
            'os_type': 'ESXi',
            'initiators': [self.fc_initiator_1],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_by_name = MagicMock(
            return_value=None)
        host_module_mock.perform_module_operation()
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_host_wo_initiator_state(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_3",
            'os_type': 'ESXi',
            'initiators': [self.fc_initiator_1],
            'state': 'present'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_by_name = MagicMock(
            return_value=None)
        host_module_mock.perform_module_operation()
        assert MockHostApi.create_host_wo_initiator_state_failed_msg() in \
            host_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_host_with_new_name(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_3",
            'new_name': "Sample_host_3_new",
            'os_type': 'ESXi',
            'initiators': [self.fc_initiator_1],
            'initiator_state': "present-in-host",
            'state': 'present'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_by_name = MagicMock(
            return_value=None)
        host_module_mock.perform_module_operation()
        assert MockHostApi.create_host_with_new_name_failed_msg() in \
            host_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_host_wo_initiator(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_3",
            'os_type': 'ESXi',
            'initiator_state': "present-in-host",
            'state': 'present'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_by_name = MagicMock(
            return_value=None)
        host_module_mock.perform_module_operation()
        assert MockHostApi.create_host_wo_initiator_failed_msg() in \
            host_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_host_with_iscsi_initiators(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_3",
            'os_type': 'ESXi',
            'initiators': [self.iscsi_initiator_1],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_by_name = MagicMock(
            return_value=None)
        host_module_mock.perform_module_operation()
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_host_with_nvme_initiators(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_3",
            'os_type': 'ESXi',
            'initiators': [self.nvme_initiator_1],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_by_name = MagicMock(
            return_value=None)
        host_module_mock.perform_module_operation()
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_host_with_mixed_initiators(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_3",
            'os_type': 'ESXi',
            'initiators': [self.nvme_initiator_1,
                           self.iscsi_initiator_1,
                           self.fc_initiator_1],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_by_name = MagicMock(
            return_value=None)
        host_module_mock.perform_module_operation()
        assert MockHostApi.create_host_mixed_initiators_failed_msg() in \
            host_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_host_without_os_type(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_3",
            'initiators': [self.fc_initiator_1],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_by_name = MagicMock(
            return_value=None)
        host_module_mock.perform_module_operation()
        assert MockHostApi.create_host_without_os_type_failed_msg() in \
            host_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_os_type(self, host_module_mock):
        self.get_module_args.update({
            'host_id': "4d56e60-fc10-4f51-a698-84a664562f0d",
            'os_type': 'Windows',
            "host_connectivity": MockHostApi.HOST_CONN_1,
            'state': 'present'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        host_module_mock.perform_module_operation()
        assert MockHostApi.modify_os_type_failed_msg() in \
            host_module_mock.module.fail_json.call_args[1]['msg']

    def test_add_iscsi_initiator(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_1",
            'initiators': [self.iscsi_initiator_2],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        host_module_mock.perform_module_operation()
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_add_iscsi_initiator_detailed_initiator(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_1",
            'detailed_initiators': [{
                'port_name': self.iscsi_initiator_2,
                'port_type': "iSCSI",
                'chap_single_username': None,
                'chap_single_password': None,
                'chap_mutual_username': None,
                'chap_mutual_password': None}],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        host_module_mock.perform_module_operation()
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_add_nvme_initiator_detailed_initiator(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_1",
            'detailed_initiators': [{
                'port_name': self.nvme_initiator_1,
                'port_type': "NVMe",
                'chap_single_username': None,
                'chap_single_password': None,
                'chap_mutual_username': None,
                'chap_mutual_password': None}],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        host_module_mock.perform_module_operation()
        host_module_mock.conn.provisioning.modify_host.assert_called()

    def test_add_nvme_initiator(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_4",
            'initiators': ["nqn.2014-08.org.nvmexpress:uuid:7936206c-9c51-4bf4-86b6-f4e2803218f5"],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS_4)
        host_module_mock.perform_module_operation()
        host_module_mock.conn.provisioning.modify_host.assert_called()

    def test_add_fc_initiator_detailed_initiator(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_1",
            'detailed_initiators': [{
                'port_name': "21:00:00:XX:XX:XX:XX:YY",
                'port_type': "FC",
                'chap_single_username': None,
                'chap_single_password': None,
                'chap_mutual_username': None,
                'chap_mutual_password': None}],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        host_module_mock.perform_module_operation()
        host_module_mock.conn.provisioning.modify_host.assert_called()

    def test_add_fc_initiator(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_5",
            'initiators': ["21:00:00:XX:XX:XX:XX:YY"],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS_5)
        host_module_mock.perform_module_operation()
        host_module_mock.conn.provisioning.modify_host.assert_called()

    def test_remove_initiator_detailed_initiator(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_1",
            'detailed_initiators': [{
                'port_name': self.iscsi_initiator_2,
                'port_type': "iSCSI",
                'chap_single_username': None,
                'chap_single_password': None,
                'chap_mutual_username': None,
                'chap_mutual_password': None}],
            'state': 'present',
            'initiator_state': 'absent-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS_2)
        host_module_mock.perform_module_operation()
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_remove_non_existing_initiator_detailed_initiator(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_1",
            'detailed_initiators': [{
                'port_name': 'iqn.1998-01.com.vmware:lgc198248-5b06fb30',
                'port_type': "iSCSI",
                'chap_single_username': None,
                'chap_single_password': None,
                'chap_mutual_username': None,
                'chap_mutual_password': None}],
            'state': 'present',
            'initiator_state': 'absent-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS_2)
        host_module_mock.perform_module_operation()
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_add_existing_initiator_detailed_initiator(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_1",
            'detailed_initiators': [{
                'port_name': 'iqn.1998-01.com.vmware:losat106-0eab2afe',
                'port_type': "iSCSI",
                'chap_single_username': None,
                'chap_single_password': None,
                'chap_mutual_username': None,
                'chap_mutual_password': None}],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        host_module_mock.perform_module_operation()
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_add_existing_initiator(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_1",
            'initiators': ['iqn.1998-01.com.vmware:losat106-0eab2afe'],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        host_module_mock.perform_module_operation()
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_remove_initiator(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_1",
            'initiators': [self.iscsi_initiator_2],
            'state': 'present',
            'initiator_state': 'absent-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS_2)
        host_module_mock.perform_module_operation()
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_remove_initiator_no_init(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_3",
            'initiators': [self.iscsi_initiator_2],
            'state': 'present',
            'initiator_state': 'absent-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS_3)
        host_module_mock.perform_module_operation()
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_rename_host(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_1",
            'new_name': "Sample_host_1_new",
            'state': 'present',
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        host_module_mock.perform_module_operation()
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_delete_host(self, host_module_mock):
        self.get_module_args.update({
            'host_name': MockHostApi.HOST_NAME_1,
            'state': "absent"
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        host_module_mock.perform_module_operation()
        host_module_mock.conn.provisioning.delete_host.assert_called()
