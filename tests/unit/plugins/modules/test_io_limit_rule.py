# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for IO Limit Rule module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_io_limit_rule_api \
    import MockIoLimitRuleApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.io_limit_rule import \
    PowerStoreIoLimitRule, IoLimitRuleHandler


class TestPowerstoreIoLimitRule():

    get_module_args = MockIoLimitRuleApi.IO_LIMIT_RULE_COMMON_ARGS

    @pytest.fixture
    def io_limit_rule_module_mock(self, mocker):
        mocker.patch(MockIoLimitRuleApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        io_limit_rule_module_mock = PowerStoreIoLimitRule()
        io_limit_rule_module_mock.module = MagicMock()
        io_limit_rule_module_mock.module.check_mode = False
        io_limit_rule_module_mock.module._diff = False
        io_limit_rule_module_mock.result = {"changed": False}
        return io_limit_rule_module_mock

    # U-001: test_get_io_limit_rule_by_name
    def test_get_io_limit_rule_by_name(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': MockIoLimitRuleApi.IO_LIMIT_RULE_NAME_1,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            return_value=[MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1])
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_details = MagicMock(
            return_value=MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1)
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        assert MockIoLimitRuleApi.IO_LIMIT_RULE_NAME_1 == \
            io_limit_rule_module_mock.module.exit_json.call_args[1]['io_limit_rule_details']['name']

    # U-002: test_get_io_limit_rule_by_id
    def test_get_io_limit_rule_by_id(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_id': MockIoLimitRuleApi.IO_LIMIT_RULE_ID_1,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_details = MagicMock(
            return_value=MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1)
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        assert MockIoLimitRuleApi.IO_LIMIT_RULE_ID_1 == \
            io_limit_rule_module_mock.module.exit_json.call_args[1]['io_limit_rule_details']['id']

    # U-003: test_create_io_limit_rule
    def test_create_io_limit_rule(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': 'new_rule',
            'limit_type': 'absolute',
            'max_iops': 5000,
            'max_bw': 102400,
            'max_bw_unit': 'KB/s',
            'burst_percentage': 20,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(return_value=[])
        io_limit_rule_module_mock.provisioning.create_io_limit_rule = MagicMock(
            return_value=MockIoLimitRuleApi.CREATE_RESPONSE)
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_details = MagicMock(
            return_value=MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1)
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        assert io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is True
        io_limit_rule_module_mock.provisioning.create_io_limit_rule.assert_called()

    # U-004: test_create_io_limit_rule_minimal
    def test_create_io_limit_rule_minimal(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': 'minimal_rule',
            'limit_type': 'absolute',
            'max_iops': 1000,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(return_value=[])
        io_limit_rule_module_mock.provisioning.create_io_limit_rule = MagicMock(
            return_value=MockIoLimitRuleApi.CREATE_RESPONSE)
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_details = MagicMock(
            return_value=MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1)
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        assert io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is True

    # U-005: test_modify_io_limit_rule_max_bw
    def test_modify_io_limit_rule_max_bw(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': MockIoLimitRuleApi.IO_LIMIT_RULE_NAME_1,
            'max_bw': 204800,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            return_value=[MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1])
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_details = MagicMock(
            return_value=MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1)
        io_limit_rule_module_mock.provisioning.modify_io_limit_rule = MagicMock(return_value=None)
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        assert io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is True
        io_limit_rule_module_mock.provisioning.modify_io_limit_rule.assert_called()

    # U-006: test_modify_io_limit_rule_max_iops
    def test_modify_io_limit_rule_max_iops(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': MockIoLimitRuleApi.IO_LIMIT_RULE_NAME_1,
            'max_iops': 10000,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            return_value=[MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1])
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_details = MagicMock(
            return_value=MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1)
        io_limit_rule_module_mock.provisioning.modify_io_limit_rule = MagicMock(return_value=None)
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        assert io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is True

    # U-007: test_delete_io_limit_rule
    def test_delete_io_limit_rule(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': MockIoLimitRuleApi.IO_LIMIT_RULE_NAME_1,
            'state': 'absent'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            return_value=[MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1])
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_details = MagicMock(
            return_value=MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1)
        io_limit_rule_module_mock.provisioning.delete_io_limit_rule = MagicMock(return_value=None)
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        assert io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is True
        io_limit_rule_module_mock.provisioning.delete_io_limit_rule.assert_called()

    # U-008: test_get_io_limit_rule_exception
    def test_get_io_limit_rule_exception(self, io_limit_rule_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'io_limit_rule_name': MockIoLimitRuleApi.IO_LIMIT_RULE_NAME_1,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            side_effect=MockApiException)
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-009: test_create_io_limit_rule_exception
    def test_create_io_limit_rule_exception(self, io_limit_rule_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'io_limit_rule_name': 'new_rule',
            'limit_type': 'absolute',
            'max_iops': 5000,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(return_value=[])
        io_limit_rule_module_mock.provisioning.create_io_limit_rule = MagicMock(
            side_effect=MockApiException)
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-010: test_modify_io_limit_rule_exception
    def test_modify_io_limit_rule_exception(self, io_limit_rule_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'io_limit_rule_name': MockIoLimitRuleApi.IO_LIMIT_RULE_NAME_1,
            'max_bw': 204800,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            return_value=[MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1])
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_details = MagicMock(
            return_value=MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1)
        io_limit_rule_module_mock.provisioning.modify_io_limit_rule = MagicMock(
            side_effect=MockApiException)
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-011: test_delete_io_limit_rule_exception
    def test_delete_io_limit_rule_exception(self, io_limit_rule_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "500"
        self.get_module_args.update({
            'io_limit_rule_name': MockIoLimitRuleApi.IO_LIMIT_RULE_NAME_1,
            'state': 'absent'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            return_value=[MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1])
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_details = MagicMock(
            return_value=MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1)
        io_limit_rule_module_mock.provisioning.delete_io_limit_rule = MagicMock(
            side_effect=MockApiException)
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-012: test_delete_rule_in_use
    def test_delete_rule_in_use(self, io_limit_rule_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "422"
        self.get_module_args.update({
            'io_limit_rule_name': MockIoLimitRuleApi.IO_LIMIT_RULE_NAME_1,
            'state': 'absent'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            return_value=[MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_WITH_POLICY])
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_details = MagicMock(
            return_value=MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_WITH_POLICY)
        io_limit_rule_module_mock.provisioning.delete_io_limit_rule = MagicMock(
            side_effect=MockApiException)
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-013: test_idempotency_no_change
    def test_idempotency_no_change(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': MockIoLimitRuleApi.IO_LIMIT_RULE_NAME_1,
            'max_bw': 102400,
            'max_iops': 5000,
            'burst_percentage': 20,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            return_value=[MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1])
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_details = MagicMock(
            return_value=MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1)
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        assert io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is False
        io_limit_rule_module_mock.provisioning.modify_io_limit_rule.assert_not_called()

    # U-014: test_check_mode_create
    def test_check_mode_create(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': 'new_rule',
            'limit_type': 'absolute',
            'max_iops': 5000,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.module.check_mode = True
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(return_value=[])
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        assert io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is True
        io_limit_rule_module_mock.provisioning.create_io_limit_rule.assert_not_called()

    # U-015: test_check_mode_modify
    def test_check_mode_modify(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': MockIoLimitRuleApi.IO_LIMIT_RULE_NAME_1,
            'max_bw': 204800,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.module.check_mode = True
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            return_value=[MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1])
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_details = MagicMock(
            return_value=MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1)
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        assert io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is True
        io_limit_rule_module_mock.provisioning.modify_io_limit_rule.assert_not_called()

    # U-016: test_diff_mode_modify
    def test_diff_mode_modify(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': MockIoLimitRuleApi.IO_LIMIT_RULE_NAME_1,
            'max_bw': 204800,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.module._diff = True
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(
            return_value=[MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1])
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_details = MagicMock(
            return_value=MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1)
        io_limit_rule_module_mock.provisioning.modify_io_limit_rule = MagicMock(return_value=None)
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        result = io_limit_rule_module_mock.module.exit_json.call_args[1]
        assert 'diff' in result
        assert 'before' in result['diff']
        assert 'after' in result['diff']

    # U-017: test_invalid_max_bw_below_min
    def test_invalid_max_bw_below_min(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': 'new_rule',
            'limit_type': 'absolute',
            'max_bw': 1000,
            'max_bw_unit': 'KB/s',
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(return_value=[])
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-018: test_invalid_max_iops_zero
    def test_invalid_max_iops_zero(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': 'new_rule',
            'limit_type': 'absolute',
            'max_iops': 0,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(return_value=[])
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-019: test_invalid_burst_above_100
    def test_invalid_burst_above_100(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': 'new_rule',
            'limit_type': 'absolute',
            'max_iops': 5000,
            'burst_percentage': 101,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(return_value=[])
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-020: test_invalid_limit_type
    def test_invalid_limit_type(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': 'new_rule',
            'limit_type': 'invalid',
            'max_iops': 5000,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(return_value=[])
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-021: test_missing_name_and_id
    def test_missing_name_and_id(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': None,
            'io_limit_rule_id': None,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-022: test_create_without_limit_type
    def test_create_without_limit_type(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': 'new_rule',
            'limit_type': None,
            'max_iops': 5000,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(return_value=[])
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-023: test_create_without_any_limit
    def test_create_without_any_limit(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': 'new_rule',
            'limit_type': 'absolute',
            'max_bw': None,
            'max_iops': None,
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(return_value=[])
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-024: test_bw_unit_conversion_mb
    def test_bw_unit_conversion_mb(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': 'conv_rule',
            'limit_type': 'absolute',
            'max_bw': 100,
            'max_bw_unit': 'MB/s',
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(return_value=[])
        io_limit_rule_module_mock.provisioning.create_io_limit_rule = MagicMock(
            return_value=MockIoLimitRuleApi.CREATE_RESPONSE)
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_details = MagicMock(
            return_value=MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1)
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        create_call_args = io_limit_rule_module_mock.provisioning.create_io_limit_rule.call_args
        assert create_call_args is not None
        # Verify the max_bw was converted: 100 MB/s = 102400 KB/s
        payload = create_call_args[0][0] if create_call_args[0] else create_call_args[1]
        assert payload.get('max_bw', 0) == 102400

    # U-025: test_bw_unit_conversion_gb
    def test_bw_unit_conversion_gb(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': 'conv_rule_gb',
            'limit_type': 'absolute',
            'max_bw': 1,
            'max_bw_unit': 'GB/s',
            'state': 'present'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(return_value=[])
        io_limit_rule_module_mock.provisioning.create_io_limit_rule = MagicMock(
            return_value=MockIoLimitRuleApi.CREATE_RESPONSE)
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_details = MagicMock(
            return_value=MockIoLimitRuleApi.IO_LIMIT_RULE_DETAILS_1)
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        create_call_args = io_limit_rule_module_mock.provisioning.create_io_limit_rule.call_args
        assert create_call_args is not None
        # Verify the max_bw was converted: 1 GB/s = 1048576 KB/s
        payload = create_call_args[0][0] if create_call_args[0] else create_call_args[1]
        assert payload.get('max_bw', 0) == 1048576

    # U-026: test_delete_nonexistent_rule
    def test_delete_nonexistent_rule(self, io_limit_rule_module_mock):
        self.get_module_args.update({
            'io_limit_rule_name': 'nonexistent_rule',
            'state': 'absent'
        })
        io_limit_rule_module_mock.module.params = self.get_module_args
        io_limit_rule_module_mock.provisioning.get_io_limit_rule_by_name = MagicMock(return_value=[])
        IoLimitRuleHandler().handle(io_limit_rule_module_mock, io_limit_rule_module_mock.module.params)
        assert io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is False
        io_limit_rule_module_mock.provisioning.delete_io_limit_rule.assert_not_called()
