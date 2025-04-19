# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Host module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_host_api import MockHostApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.host import PowerStoreHost, HostHandler


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
        host_module_mock.module.check_mode = False
        return host_module_mock

    def test_get_host_response(self, host_module_mock):
        self.get_module_args.update({
            'host_id': "4d56e60-fc10-4f51-a698-84a664562f0d",
            'state': "present"
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
        assert self.get_module_args['host_name'] == host_module_mock.module.exit_json.call_args[1]['host_details'][
            'name']
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_add_iscsi_initiator_detailed_initiator_with_invalid_name(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_1",
            'detailed_initiators': [{
                'port_name': self.iscsi_initiator_2,
                'port_type': "iSCSI",
                'chap_single_username': "hello world",
                'chap_single_password': None,
                'chap_mutual_username': None,
                'chap_mutual_password': None}],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
        assert MockHostApi.invalid_chap_single_username_failed_msg() in \
               host_module_mock.module.fail_json.call_args[1]['msg']

        self.get_module_args.update({
            'host_name': "Sample_host_1",
            'detailed_initiators': [{
                'port_name': self.iscsi_initiator_2,
                'port_type': "iSCSI",
                'chap_single_username': None,
                'chap_single_password': None,
                'chap_mutual_username': "hello world",
                'chap_mutual_password': None}],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
        assert MockHostApi.invalid_chap_mutual_username_failed_msg() in \
               host_module_mock.module.fail_json.call_args[1]['msg']

    def test_add_iscsi_initiator_detailed_initiator_with_invalid_password(self, host_module_mock):
        self.get_module_args.update({
            'host_name': "Sample_host_1",
            'detailed_initiators': [{
                'port_name': self.iscsi_initiator_2,
                'port_type': "iSCSI",
                'chap_single_username': None,
                'chap_single_password': "hello world hello world",
                'chap_mutual_username': None,
                'chap_mutual_password': None}],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
        assert MockHostApi.invalid_chap_password_failed_msg() in \
               host_module_mock.module.fail_json.call_args[1]['msg']

        self.get_module_args.update({
            'host_name': "Sample_host_1",
            'detailed_initiators': [{
                'port_name': self.iscsi_initiator_2,
                'port_type': "iSCSI",
                'chap_single_username': None,
                'chap_single_password': None,
                'chap_mutual_username': None,
                'chap_mutual_password': "hello world hello world"}],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
        assert MockHostApi.invalid_chap_password_failed_msg() in \
               host_module_mock.module.fail_json.call_args[1]['msg']

        self.get_module_args.update({
            'host_name': "Sample_host_1",
            'detailed_initiators': [{
                'port_name': self.iscsi_initiator_2,
                'port_type': "iSCSI",
                'chap_single_username': None,
                'chap_single_password': "shortpwd",
                'chap_mutual_username': None,
                'chap_mutual_password': None}],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
        assert MockHostApi.invalid_chap_password_failed_msg() in \
               host_module_mock.module.fail_json.call_args[1]['msg']

        self.get_module_args.update({
            'host_name': "Sample_host_1",
            'detailed_initiators': [{
                'port_name': self.iscsi_initiator_2,
                'port_type': "iSCSI",
                'chap_single_username': None,
                'chap_single_password': None,
                'chap_mutual_username': None,
                'chap_mutual_password': "ThisIsAVeryLongPasswordThatExceedsTheMaximumLengthOfSixtyFourCharacters"}],
            'state': 'present',
            'initiator_state': 'present-in-host'
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
        assert MockHostApi.invalid_chap_password_failed_msg() in \
               host_module_mock.module.fail_json.call_args[1]['msg']

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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
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
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_delete_host(self, host_module_mock):
        self.get_module_args.update({
            'host_name': MockHostApi.HOST_NAME_1,
            'state': "absent"
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.conn.provisioning.get_host_details = MagicMock(
            return_value=MockHostApi.HOST_DETAILS)
        HostHandler().handle(host_module_mock, host_module_mock.module.params)
        host_module_mock.conn.provisioning.delete_host.assert_called()
