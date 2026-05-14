# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for QoS Policy module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_qos_policy_api \
    import MockQosPolicyApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.qos_policy import \
    PowerStoreQosPolicy, QosPolicyHandler


class TestPowerstoreQosPolicy():

    get_module_args = MockQosPolicyApi.QOS_POLICY_COMMON_ARGS

    @pytest.fixture
    def qos_policy_module_mock(self, mocker):
        mocker.patch(MockQosPolicyApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        module_mock = PowerStoreQosPolicy()
        module_mock.module = MagicMock()
        module_mock.module.check_mode = False
        module_mock.module._diff = False
        module_mock.result = {"changed": False}
        return module_mock

    # U-052: test_get_qos_policy_by_name
    def test_get_qos_policy_by_name(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': MockQosPolicyApi.QOS_POLICY_NAME_1,
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(
            return_value=[MockQosPolicyApi.QOS_POLICY_DETAILS_QOS])
        qos_policy_module_mock.protection.get_policy_details = MagicMock(
            return_value=MockQosPolicyApi.QOS_POLICY_DETAILS_QOS)
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        assert MockQosPolicyApi.QOS_POLICY_NAME_1 == \
            qos_policy_module_mock.module.exit_json.call_args[1]['qos_policy_details']['name']

    # U-053: test_get_qos_policy_by_id
    def test_get_qos_policy_by_id(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_id': MockQosPolicyApi.QOS_POLICY_ID_1,
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_details = MagicMock(
            return_value=MockQosPolicyApi.QOS_POLICY_DETAILS_QOS)
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        assert MockQosPolicyApi.QOS_POLICY_ID_1 == \
            qos_policy_module_mock.module.exit_json.call_args[1]['qos_policy_details']['id']

    # U-054: test_create_qos_policy
    def test_create_qos_policy(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': 'gold_qos',
            'policy_type': 'QoS',
            'io_limit_rule': 'tenant_a_limits',
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(return_value=[])
        qos_policy_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            return_value=[MockQosPolicyApi.IO_LIMIT_RULE_DETAILS])
        qos_policy_module_mock.protection.create_policy = MagicMock(
            return_value=MockQosPolicyApi.CREATE_RESPONSE)
        qos_policy_module_mock.protection.get_policy_details = MagicMock(
            return_value=MockQosPolicyApi.QOS_POLICY_DETAILS_QOS)
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        assert qos_policy_module_mock.module.exit_json.call_args[1]['changed'] is True
        qos_policy_module_mock.protection.create_policy.assert_called()

    # U-055: test_create_file_performance_policy
    def test_create_file_performance_policy(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': 'file_gold_qos',
            'policy_type': 'File_Performance',
            'file_io_limit_rule': 'file_bw_500mb',
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(return_value=[])
        qos_policy_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(
            return_value=[MockQosPolicyApi.FILE_IO_LIMIT_RULE_DETAILS])
        qos_policy_module_mock.protection.create_policy = MagicMock(
            return_value=MockQosPolicyApi.CREATE_RESPONSE)
        qos_policy_module_mock.protection.get_policy_details = MagicMock(
            return_value=MockQosPolicyApi.QOS_POLICY_DETAILS_FILE_PERF)
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        assert qos_policy_module_mock.module.exit_json.call_args[1]['changed'] is True

    # U-056: test_create_qos_policy_with_description
    def test_create_qos_policy_with_description(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': 'gold_qos',
            'description': 'Gold tier QoS policy',
            'policy_type': 'QoS',
            'io_limit_rule': 'tenant_a_limits',
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(return_value=[])
        qos_policy_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            return_value=[MockQosPolicyApi.IO_LIMIT_RULE_DETAILS])
        qos_policy_module_mock.protection.create_policy = MagicMock(
            return_value=MockQosPolicyApi.CREATE_RESPONSE)
        qos_policy_module_mock.protection.get_policy_details = MagicMock(
            return_value=MockQosPolicyApi.QOS_POLICY_DETAILS_QOS)
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        assert qos_policy_module_mock.module.exit_json.call_args[1]['changed'] is True

    # U-057: test_modify_qos_policy_rule
    def test_modify_qos_policy_rule(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': MockQosPolicyApi.QOS_POLICY_NAME_1,
            'io_limit_rule': 'tenant_b_limits',
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(
            return_value=[MockQosPolicyApi.QOS_POLICY_DETAILS_QOS])
        qos_policy_module_mock.protection.get_policy_details = MagicMock(
            return_value=MockQosPolicyApi.QOS_POLICY_DETAILS_QOS)
        qos_policy_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            return_value=[MockQosPolicyApi.IO_LIMIT_RULE_DETAILS_2])
        qos_policy_module_mock.protection.modify_policy = MagicMock(return_value=None)
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        assert qos_policy_module_mock.module.exit_json.call_args[1]['changed'] is True

    # U-058: test_modify_qos_policy_name
    def test_modify_qos_policy_name(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': MockQosPolicyApi.QOS_POLICY_NAME_1,
            'new_name': 'silver_qos',
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(
            return_value=[MockQosPolicyApi.QOS_POLICY_DETAILS_QOS])
        qos_policy_module_mock.protection.get_policy_details = MagicMock(
            return_value=MockQosPolicyApi.QOS_POLICY_DETAILS_QOS)
        qos_policy_module_mock.protection.modify_policy = MagicMock(return_value=None)
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        assert qos_policy_module_mock.module.exit_json.call_args[1]['changed'] is True

    # U-059: test_modify_file_performance_policy_rule
    def test_modify_file_performance_policy_rule(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': 'file_gold_qos',
            'file_io_limit_rule': 'file_bw_1000mb',
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(
            return_value=[MockQosPolicyApi.QOS_POLICY_DETAILS_FILE_PERF])
        qos_policy_module_mock.protection.get_policy_details = MagicMock(
            return_value=MockQosPolicyApi.QOS_POLICY_DETAILS_FILE_PERF)
        qos_policy_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(
            return_value=[{"id": "new-rule-id", "name": "file_bw_1000mb"}])
        qos_policy_module_mock.protection.modify_policy = MagicMock(return_value=None)
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        assert qos_policy_module_mock.module.exit_json.call_args[1]['changed'] is True

    # U-060: test_delete_qos_policy
    def test_delete_qos_policy(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': MockQosPolicyApi.QOS_POLICY_NAME_1,
            'state': 'absent'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(
            return_value=[MockQosPolicyApi.QOS_POLICY_DETAILS_QOS])
        qos_policy_module_mock.protection.get_policy_details = MagicMock(
            return_value=MockQosPolicyApi.QOS_POLICY_DETAILS_QOS)
        qos_policy_module_mock.protection.delete_policy = MagicMock(return_value=None)
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        assert qos_policy_module_mock.module.exit_json.call_args[1]['changed'] is True
        qos_policy_module_mock.protection.delete_policy.assert_called()

    # U-061: test_delete_policy_with_assigned_resources
    def test_delete_policy_with_assigned_resources(self, qos_policy_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "422"
        self.get_module_args.update({
            'qos_policy_name': MockQosPolicyApi.QOS_POLICY_NAME_1,
            'state': 'absent'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(
            return_value=[MockQosPolicyApi.QOS_POLICY_DETAILS_WITH_RESOURCES])
        qos_policy_module_mock.protection.get_policy_details = MagicMock(
            return_value=MockQosPolicyApi.QOS_POLICY_DETAILS_WITH_RESOURCES)
        qos_policy_module_mock.protection.delete_policy = MagicMock(side_effect=MockApiException)
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        qos_policy_module_mock.module.fail_json.assert_called()

    # U-062: test_get_exception
    def test_get_exception(self, qos_policy_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'qos_policy_name': MockQosPolicyApi.QOS_POLICY_NAME_1,
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(side_effect=MockApiException)
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        qos_policy_module_mock.module.fail_json.assert_called()

    # U-063: test_create_exception
    def test_create_exception(self, qos_policy_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'qos_policy_name': 'new_policy',
            'policy_type': 'QoS',
            'io_limit_rule': 'tenant_a_limits',
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(return_value=[])
        qos_policy_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            return_value=[MockQosPolicyApi.IO_LIMIT_RULE_DETAILS])
        qos_policy_module_mock.protection.create_policy = MagicMock(side_effect=MockApiException)
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        qos_policy_module_mock.module.fail_json.assert_called()

    # U-064: test_modify_exception
    def test_modify_exception(self, qos_policy_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'qos_policy_name': MockQosPolicyApi.QOS_POLICY_NAME_1,
            'new_name': 'updated_name',
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(
            return_value=[MockQosPolicyApi.QOS_POLICY_DETAILS_QOS])
        qos_policy_module_mock.protection.get_policy_details = MagicMock(
            return_value=MockQosPolicyApi.QOS_POLICY_DETAILS_QOS)
        qos_policy_module_mock.protection.modify_policy = MagicMock(side_effect=MockApiException)
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        qos_policy_module_mock.module.fail_json.assert_called()

    # U-065: test_delete_exception
    def test_delete_exception(self, qos_policy_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "500"
        self.get_module_args.update({
            'qos_policy_name': MockQosPolicyApi.QOS_POLICY_NAME_1,
            'state': 'absent'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(
            return_value=[MockQosPolicyApi.QOS_POLICY_DETAILS_QOS])
        qos_policy_module_mock.protection.get_policy_details = MagicMock(
            return_value=MockQosPolicyApi.QOS_POLICY_DETAILS_QOS)
        qos_policy_module_mock.protection.delete_policy = MagicMock(side_effect=MockApiException)
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        qos_policy_module_mock.module.fail_json.assert_called()

    # U-066: test_idempotency_no_change
    def test_idempotency_no_change(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': MockQosPolicyApi.QOS_POLICY_NAME_1,
            'io_limit_rule': 'tenant_a_limits',
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(
            return_value=[MockQosPolicyApi.QOS_POLICY_DETAILS_QOS])
        qos_policy_module_mock.protection.get_policy_details = MagicMock(
            return_value=MockQosPolicyApi.QOS_POLICY_DETAILS_QOS)
        qos_policy_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            return_value=[MockQosPolicyApi.IO_LIMIT_RULE_DETAILS])
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        assert qos_policy_module_mock.module.exit_json.call_args[1]['changed'] is False

    # U-067: test_check_mode_create
    def test_check_mode_create(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': 'new_policy',
            'policy_type': 'QoS',
            'io_limit_rule': 'tenant_a_limits',
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.module.check_mode = True
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(return_value=[])
        qos_policy_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            return_value=[MockQosPolicyApi.IO_LIMIT_RULE_DETAILS])
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        assert qos_policy_module_mock.module.exit_json.call_args[1]['changed'] is True
        qos_policy_module_mock.protection.create_policy.assert_not_called()

    # U-068: test_check_mode_delete
    def test_check_mode_delete(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': MockQosPolicyApi.QOS_POLICY_NAME_1,
            'state': 'absent'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.module.check_mode = True
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(
            return_value=[MockQosPolicyApi.QOS_POLICY_DETAILS_QOS])
        qos_policy_module_mock.protection.get_policy_details = MagicMock(
            return_value=MockQosPolicyApi.QOS_POLICY_DETAILS_QOS)
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        assert qos_policy_module_mock.module.exit_json.call_args[1]['changed'] is True
        qos_policy_module_mock.protection.delete_policy.assert_not_called()

    # U-069: test_diff_mode_modify
    def test_diff_mode_modify(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': MockQosPolicyApi.QOS_POLICY_NAME_1,
            'io_limit_rule': 'tenant_b_limits',
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.module._diff = True
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(
            return_value=[MockQosPolicyApi.QOS_POLICY_DETAILS_QOS])
        qos_policy_module_mock.protection.get_policy_details = MagicMock(
            return_value=MockQosPolicyApi.QOS_POLICY_DETAILS_QOS)
        qos_policy_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            return_value=[MockQosPolicyApi.IO_LIMIT_RULE_DETAILS_2])
        qos_policy_module_mock.protection.modify_policy = MagicMock(return_value=None)
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        result = qos_policy_module_mock.module.exit_json.call_args[1]
        assert 'diff' in result

    # U-070: test_missing_name_and_id
    def test_missing_name_and_id(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': None,
            'qos_policy_id': None,
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        qos_policy_module_mock.module.fail_json.assert_called()

    # U-071: test_create_without_policy_type
    def test_create_without_policy_type(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': 'new_policy',
            'policy_type': None,
            'io_limit_rule': 'tenant_a_limits',
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(return_value=[])
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        qos_policy_module_mock.module.fail_json.assert_called()

    # U-072: test_create_qos_without_io_limit_rule
    def test_create_qos_without_io_limit_rule(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': 'new_policy',
            'policy_type': 'QoS',
            'io_limit_rule': None,
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(return_value=[])
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        qos_policy_module_mock.module.fail_json.assert_called()

    # U-073: test_create_file_perf_without_file_rule
    def test_create_file_perf_without_file_rule(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': 'new_policy',
            'policy_type': 'File_Performance',
            'file_io_limit_rule': None,
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(return_value=[])
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        qos_policy_module_mock.module.fail_json.assert_called()

    # U-074: test_create_qos_with_file_rule_conflict
    def test_create_qos_with_file_rule_conflict(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': 'new_policy',
            'policy_type': 'QoS',
            'file_io_limit_rule': 'file_bw_500mb',
            'io_limit_rule': None,
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(return_value=[])
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        qos_policy_module_mock.module.fail_json.assert_called()

    # U-075: test_delete_nonexistent_policy
    def test_delete_nonexistent_policy(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': 'nonexistent',
            'state': 'absent'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(return_value=[])
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        assert qos_policy_module_mock.module.exit_json.call_args[1]['changed'] is False

    # U-076: test_resolve_io_limit_rule_by_name
    def test_resolve_io_limit_rule_by_name(self, qos_policy_module_mock):
        self.get_module_args.update({
            'qos_policy_name': 'new_policy',
            'policy_type': 'QoS',
            'io_limit_rule': 'tenant_a_limits',
            'state': 'present'
        })
        qos_policy_module_mock.module.params = self.get_module_args
        qos_policy_module_mock.protection.get_policy_by_name = MagicMock(return_value=[])
        qos_policy_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            return_value=[MockQosPolicyApi.IO_LIMIT_RULE_DETAILS])
        qos_policy_module_mock.protection.create_policy = MagicMock(
            return_value=MockQosPolicyApi.CREATE_RESPONSE)
        qos_policy_module_mock.protection.get_policy_details = MagicMock(
            return_value=MockQosPolicyApi.QOS_POLICY_DETAILS_QOS)
        QosPolicyHandler().handle(qos_policy_module_mock, qos_policy_module_mock.module.params)
        qos_policy_module_mock.provisioning.get_io_limit_rule_by_name.assert_called()
