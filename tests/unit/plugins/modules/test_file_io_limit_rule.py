# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for File IO Limit Rule module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_file_io_limit_rule_api \
    import MockFileIoLimitRuleApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.file_io_limit_rule import \
    PowerStoreFileIoLimitRule, FileIoLimitRuleHandler


class TestPowerstoreFileIoLimitRule():

    get_module_args = MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_COMMON_ARGS

    @pytest.fixture
    def file_io_limit_rule_module_mock(self, mocker):
        mocker.patch(MockFileIoLimitRuleApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        module_mock = PowerStoreFileIoLimitRule()
        module_mock.module = MagicMock()
        module_mock.module.check_mode = False
        module_mock.module._diff = False
        module_mock.result = {"changed": False}
        return module_mock

    # U-027: test_get_file_io_limit_rule_by_name
    def test_get_file_io_limit_rule_by_name(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_NAME_1,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(
            return_value=[MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1])
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_details = MagicMock(
            return_value=MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1)
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        assert MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_NAME_1 == \
            file_io_limit_rule_module_mock.module.exit_json.call_args[1]['file_io_limit_rule_details']['name']

    # U-028: test_get_file_io_limit_rule_by_id
    def test_get_file_io_limit_rule_by_id(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_id': MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_ID_1,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_details = MagicMock(
            return_value=MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1)
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        assert MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_ID_1 == \
            file_io_limit_rule_module_mock.module.exit_json.call_args[1]['file_io_limit_rule_details']['id']

    # U-029: test_create_file_io_limit_rule
    def test_create_file_io_limit_rule(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': 'file_bw_500mb',
            'max_bw': 500,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(return_value=[])
        file_io_limit_rule_module_mock.configuration.create_file_io_limit_rule = MagicMock(
            return_value=MockFileIoLimitRuleApi.CREATE_RESPONSE)
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_details = MagicMock(
            return_value=MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1)
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        assert file_io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is True
        file_io_limit_rule_module_mock.configuration.create_file_io_limit_rule.assert_called()

    # U-030: test_create_file_io_limit_rule_max
    def test_create_file_io_limit_rule_max(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': 'file_bw_max',
            'max_bw': 1000000,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(return_value=[])
        file_io_limit_rule_module_mock.configuration.create_file_io_limit_rule = MagicMock(
            return_value=MockFileIoLimitRuleApi.CREATE_RESPONSE)
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_details = MagicMock(
            return_value=MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1)
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        assert file_io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is True

    # U-031: test_modify_file_io_limit_rule_bw
    def test_modify_file_io_limit_rule_bw(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_NAME_1,
            'max_bw': 1000,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(
            return_value=[MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1])
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_details = MagicMock(
            return_value=MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1)
        file_io_limit_rule_module_mock.configuration.modify_file_io_limit_rule = MagicMock(return_value=None)
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        assert file_io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is True
        file_io_limit_rule_module_mock.configuration.modify_file_io_limit_rule.assert_called()

    # U-032: test_modify_file_io_limit_rule_name
    def test_modify_file_io_limit_rule_name(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_NAME_1,
            'new_name': 'renamed_rule',
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(
            return_value=[MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1])
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_details = MagicMock(
            return_value=MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1)
        file_io_limit_rule_module_mock.configuration.modify_file_io_limit_rule = MagicMock(return_value=None)
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        assert file_io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is True

    # U-033: test_delete_file_io_limit_rule
    def test_delete_file_io_limit_rule(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_NAME_1,
            'state': 'absent'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(
            return_value=[MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1])
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_details = MagicMock(
            return_value=MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1)
        file_io_limit_rule_module_mock.configuration.delete_file_io_limit_rule = MagicMock(return_value=None)
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        assert file_io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is True
        file_io_limit_rule_module_mock.configuration.delete_file_io_limit_rule.assert_called()

    # U-034: test_get_exception
    def test_get_exception(self, file_io_limit_rule_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'file_io_limit_rule_name': MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_NAME_1,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(
            side_effect=MockApiException)
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        file_io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-035: test_create_exception
    def test_create_exception(self, file_io_limit_rule_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'file_io_limit_rule_name': 'new_rule',
            'max_bw': 500,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(return_value=[])
        file_io_limit_rule_module_mock.configuration.create_file_io_limit_rule = MagicMock(
            side_effect=MockApiException)
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        file_io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-036: test_modify_exception
    def test_modify_exception(self, file_io_limit_rule_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'file_io_limit_rule_name': MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_NAME_1,
            'max_bw': 1000,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(
            return_value=[MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1])
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_details = MagicMock(
            return_value=MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1)
        file_io_limit_rule_module_mock.configuration.modify_file_io_limit_rule = MagicMock(
            side_effect=MockApiException)
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        file_io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-037: test_delete_exception
    def test_delete_exception(self, file_io_limit_rule_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "500"
        self.get_module_args.update({
            'file_io_limit_rule_name': MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_NAME_1,
            'state': 'absent'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(
            return_value=[MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1])
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_details = MagicMock(
            return_value=MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1)
        file_io_limit_rule_module_mock.configuration.delete_file_io_limit_rule = MagicMock(
            side_effect=MockApiException)
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        file_io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-038: test_idempotency_no_change
    def test_idempotency_no_change(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_NAME_1,
            'max_bw': 500,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(
            return_value=[MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1])
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_details = MagicMock(
            return_value=MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1)
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        assert file_io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is False
        file_io_limit_rule_module_mock.configuration.modify_file_io_limit_rule.assert_not_called()

    # U-039: test_check_mode_create
    def test_check_mode_create(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': 'new_rule',
            'max_bw': 500,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.module.check_mode = True
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(return_value=[])
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        assert file_io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is True
        file_io_limit_rule_module_mock.configuration.create_file_io_limit_rule.assert_not_called()

    # U-040: test_check_mode_modify
    def test_check_mode_modify(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_NAME_1,
            'max_bw': 1000,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.module.check_mode = True
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(
            return_value=[MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1])
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_details = MagicMock(
            return_value=MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1)
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        assert file_io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is True
        file_io_limit_rule_module_mock.configuration.modify_file_io_limit_rule.assert_not_called()

    # U-041: test_diff_mode_modify
    def test_diff_mode_modify(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_NAME_1,
            'max_bw': 1000,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.module._diff = True
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(
            return_value=[MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1])
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_details = MagicMock(
            return_value=MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1)
        file_io_limit_rule_module_mock.configuration.modify_file_io_limit_rule = MagicMock(return_value=None)
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        result = file_io_limit_rule_module_mock.module.exit_json.call_args[1]
        assert 'diff' in result
        assert 'before' in result['diff']
        assert 'after' in result['diff']

    # U-042: test_invalid_max_bw_zero
    def test_invalid_max_bw_zero(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': 'new_rule',
            'max_bw': 0,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(return_value=[])
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        file_io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-043: test_invalid_max_bw_negative
    def test_invalid_max_bw_negative(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': 'new_rule',
            'max_bw': -1,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(return_value=[])
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        file_io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-044: test_invalid_max_bw_above_max
    def test_invalid_max_bw_above_max(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': 'new_rule',
            'max_bw': 1000001,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(return_value=[])
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        file_io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-045: test_missing_name_and_id
    def test_missing_name_and_id(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': None,
            'file_io_limit_rule_id': None,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        file_io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-046: test_create_without_max_bw
    def test_create_without_max_bw(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': 'new_rule',
            'max_bw': None,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(return_value=[])
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        file_io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-047: test_delete_nonexistent_rule
    def test_delete_nonexistent_rule(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': 'nonexistent_rule',
            'state': 'absent'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(return_value=[])
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        assert file_io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is False
        file_io_limit_rule_module_mock.configuration.delete_file_io_limit_rule.assert_not_called()

    # U-048: test_delete_rule_in_use
    def test_delete_rule_in_use(self, file_io_limit_rule_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "422"
        self.get_module_args.update({
            'file_io_limit_rule_name': MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_NAME_1,
            'state': 'absent'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(
            return_value=[MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_WITH_POLICY])
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_details = MagicMock(
            return_value=MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_WITH_POLICY)
        file_io_limit_rule_module_mock.configuration.delete_file_io_limit_rule = MagicMock(
            side_effect=MockApiException)
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        file_io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-049: test_get_multiple_rules_same_name
    def test_get_multiple_rules_same_name(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_NAME_1,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(
            return_value=MockFileIoLimitRuleApi.TWO_RULE_LIST)
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        file_io_limit_rule_module_mock.module.fail_json.assert_called()

    # U-050: test_check_mode_delete
    def test_check_mode_delete(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_NAME_1,
            'state': 'absent'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.module.check_mode = True
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(
            return_value=[MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1])
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_details = MagicMock(
            return_value=MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1)
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        assert file_io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is True
        file_io_limit_rule_module_mock.configuration.delete_file_io_limit_rule.assert_not_called()

    # U-051: test_modify_only_name
    def test_modify_only_name(self, file_io_limit_rule_module_mock):
        self.get_module_args.update({
            'file_io_limit_rule_name': MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_NAME_1,
            'new_name': 'renamed_only',
            'max_bw': None,
            'state': 'present'
        })
        file_io_limit_rule_module_mock.module.params = self.get_module_args
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_by_name = MagicMock(
            return_value=[MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1])
        file_io_limit_rule_module_mock.configuration.get_file_io_limit_rule_details = MagicMock(
            return_value=MockFileIoLimitRuleApi.FILE_IO_LIMIT_RULE_DETAILS_1)
        file_io_limit_rule_module_mock.configuration.modify_file_io_limit_rule = MagicMock(return_value=None)
        FileIoLimitRuleHandler().handle(file_io_limit_rule_module_mock, file_io_limit_rule_module_mock.module.params)
        assert file_io_limit_rule_module_mock.module.exit_json.call_args[1]['changed'] is True
