# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for recycle bin module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock

from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries.initial_mock \
    import utils
from ansible_collections.dellemc.powerstore.plugins.modules.recycle_bin import \
    PowerStoreRecycleBin
from ansible_collections.dellemc.powerstore.plugins.modules.recycle_bin import \
    main

from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_recycle_bin_api \
    import MockRecycleBinApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception import \
    MockApiException
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries. \
    fail_json import FailJsonException, fail_json


class TestPowerStoreRecycleBin():

    get_module_args = MockRecycleBinApi.RECYCLE_BIN_COMMON_ARGS

    @pytest.fixture
    def recycle_bin_module_mock(self, mocker):
        mocker.patch(
            MockRecycleBinApi.MODULE_UTILS_PATH + '.PowerStoreException',
            new=MockApiException)
        rb_mock = PowerStoreRecycleBin()
        rb_mock.module = MagicMock()
        rb_mock.module.fail_json = fail_json
        rb_mock.module.check_mode = False
        rb_mock.module._diff = False
        return rb_mock

    def _set_params(self, module_mock, params):
        self.get_module_args.update(params)
        module_mock.module.params = self.get_module_args

    def _capture_fail(self, error_msg, module_mock):
        try:
            module_mock.perform_module_operation()
        except FailJsonException as fj_object:
            if error_msg not in fj_object.message:
                raise AssertionError(fj_object.message)

    # ===== GET CONFIG TESTS =====

    def test_get_recycle_bin_config(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': None,
            'recycle_bin_id': None,
            'resource_name': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=[
                MockRecycleBinApi.RECYCLE_BIN_CONFIG,
                MockRecycleBinApi.RECYCLE_BIN_ITEMS
            ])
        recycle_bin_module_mock.perform_module_operation()
        assert recycle_bin_module_mock.module.exit_json.call_args[1]['changed'] is False
        assert recycle_bin_module_mock.module.exit_json.call_args[1]['recycle_bin_config'] == \
            MockRecycleBinApi.RECYCLE_BIN_CONFIG

    def test_get_recycle_bin_config_exception(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': None,
            'recycle_bin_id': None,
            'resource_name': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=MockApiException)
        self._capture_fail(
            MockRecycleBinApi.get_recycle_bin_exception_response('get_config_exception'),
            recycle_bin_module_mock)

    # ===== MODIFY CONFIG TESTS =====

    def test_modify_recycle_bin_config(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': 14,
            'recycle_bin_id': None,
            'resource_name': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=[
                MockRecycleBinApi.RECYCLE_BIN_CONFIG,  # get config
                None,  # patch config
                MockRecycleBinApi.RECYCLE_BIN_CONFIG_MODIFIED  # get config again
            ])
        recycle_bin_module_mock.perform_module_operation()
        assert recycle_bin_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_recycle_bin_config_idempotent(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': 7,
            'recycle_bin_id': None,
            'resource_name': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=[
                MockRecycleBinApi.RECYCLE_BIN_CONFIG,  # get config (already 7)
                MockRecycleBinApi.RECYCLE_BIN_CONFIG   # get config again
            ])
        recycle_bin_module_mock.perform_module_operation()
        assert recycle_bin_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_modify_recycle_bin_config_check_mode(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': 14,
            'recycle_bin_id': None,
            'resource_name': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.module.check_mode = True
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            return_value=MockRecycleBinApi.RECYCLE_BIN_CONFIG)
        recycle_bin_module_mock.perform_module_operation()
        assert recycle_bin_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_recycle_bin_config_exception(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': 14,
            'recycle_bin_id': None,
            'resource_name': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=[
                MockRecycleBinApi.RECYCLE_BIN_CONFIG,  # get config
                MockApiException  # patch fails
            ])
        self._capture_fail(
            MockRecycleBinApi.get_recycle_bin_exception_response('modify_config_exception'),
            recycle_bin_module_mock)

    def test_modify_recycle_bin_config_diff_mode(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': 14,
            'recycle_bin_id': None,
            'resource_name': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.module._diff = True
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=[
                MockRecycleBinApi.RECYCLE_BIN_CONFIG,
                None,
                MockRecycleBinApi.RECYCLE_BIN_CONFIG_MODIFIED
            ])
        recycle_bin_module_mock.perform_module_operation()
        result = recycle_bin_module_mock.module.exit_json.call_args[1]
        assert result['changed'] is True
        assert 'diff' in result

    def test_invalid_expiration_duration(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': 31,
            'recycle_bin_id': None,
            'resource_name': None,
            'empty_recycle_bin': False
        })
        self._capture_fail(
            MockRecycleBinApi.get_recycle_bin_exception_response('invalid_expiration'),
            recycle_bin_module_mock)

    def test_negative_expiration_duration(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': -1,
            'recycle_bin_id': None,
            'resource_name': None,
            'empty_recycle_bin': False
        })
        self._capture_fail(
            MockRecycleBinApi.get_recycle_bin_exception_response('invalid_expiration'),
            recycle_bin_module_mock)

    # ===== RECOVER TESTS =====

    def test_recover_item_by_id(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': None,
            'recycle_bin_id': 'e0684b39-0029-4be2-b5bf-67b8c145e1b8',
            'resource_name': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=[
                MockRecycleBinApi.RECYCLE_BIN_ITEM_VOLUME,  # get item
                None  # recover
            ])
        recycle_bin_module_mock.perform_module_operation()
        assert recycle_bin_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_recover_item_by_name(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': None,
            'recycle_bin_id': None,
            'resource_name': 'test_volume',
            'resource_type': 'volume',
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=[
                MockRecycleBinApi.RECYCLE_BIN_ITEMS,  # get items for name lookup
                None  # recover
            ])
        recycle_bin_module_mock.perform_module_operation()
        assert recycle_bin_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_recover_item_by_name_no_type(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': None,
            'recycle_bin_id': None,
            'resource_name': 'test_volume',
            'resource_type': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=[
                MockRecycleBinApi.RECYCLE_BIN_ITEMS,  # get items
                None  # recover
            ])
        recycle_bin_module_mock.perform_module_operation()
        assert recycle_bin_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_recover_item_not_found_idempotent(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': None,
            'recycle_bin_id': 'nonexistent-id',
            'resource_name': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            return_value=None)

        # Mock the get_recycle_bin_item to return None for 404
        recycle_bin_module_mock.get_recycle_bin_item = MagicMock(return_value=None)
        recycle_bin_module_mock.perform_module_operation()
        assert recycle_bin_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_recover_item_by_name_not_found_idempotent(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': None,
            'recycle_bin_id': None,
            'resource_name': 'nonexistent',
            'resource_type': 'volume',
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            return_value=MockRecycleBinApi.RECYCLE_BIN_EMPTY)
        recycle_bin_module_mock.perform_module_operation()
        assert recycle_bin_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_recover_item_check_mode(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': None,
            'recycle_bin_id': 'e0684b39-0029-4be2-b5bf-67b8c145e1b8',
            'resource_name': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.module.check_mode = True
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            return_value=MockRecycleBinApi.RECYCLE_BIN_ITEM_VOLUME)
        recycle_bin_module_mock.perform_module_operation()
        assert recycle_bin_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_recover_item_exception(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': None,
            'recycle_bin_id': 'e0684b39-0029-4be2-b5bf-67b8c145e1b8',
            'resource_name': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=[
                MockRecycleBinApi.RECYCLE_BIN_ITEM_VOLUME,
                MockApiException
            ])
        self._capture_fail(
            MockRecycleBinApi.get_recycle_bin_exception_response('recover_exception'),
            recycle_bin_module_mock)

    def test_recover_item_diff_mode(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': None,
            'recycle_bin_id': 'e0684b39-0029-4be2-b5bf-67b8c145e1b8',
            'resource_name': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.module._diff = True
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=[
                MockRecycleBinApi.RECYCLE_BIN_ITEM_VOLUME,
                None
            ])
        recycle_bin_module_mock.perform_module_operation()
        result = recycle_bin_module_mock.module.exit_json.call_args[1]
        assert result['changed'] is True
        assert 'diff' in result

    # ===== DELETE TESTS =====

    def test_delete_item_by_id(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'absent',
            'expiration_duration': None,
            'recycle_bin_id': 'e0684b39-0029-4be2-b5bf-67b8c145e1b8',
            'resource_name': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=[
                MockRecycleBinApi.RECYCLE_BIN_ITEM_VOLUME,  # get item
                None  # delete
            ])
        recycle_bin_module_mock.perform_module_operation()
        assert recycle_bin_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_delete_item_by_name(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'absent',
            'expiration_duration': None,
            'recycle_bin_id': None,
            'resource_name': 'test_vg',
            'resource_type': 'volume_group',
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=[
                MockRecycleBinApi.RECYCLE_BIN_ITEMS,  # get items for name lookup
                None  # delete
            ])
        recycle_bin_module_mock.perform_module_operation()
        assert recycle_bin_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_delete_item_not_found_idempotent(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'absent',
            'expiration_duration': None,
            'recycle_bin_id': 'nonexistent-id',
            'resource_name': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.get_recycle_bin_item = MagicMock(return_value=None)
        recycle_bin_module_mock.perform_module_operation()
        assert recycle_bin_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_delete_item_check_mode(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'absent',
            'expiration_duration': None,
            'recycle_bin_id': 'e0684b39-0029-4be2-b5bf-67b8c145e1b8',
            'resource_name': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.module.check_mode = True
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            return_value=MockRecycleBinApi.RECYCLE_BIN_ITEM_VOLUME)
        recycle_bin_module_mock.perform_module_operation()
        assert recycle_bin_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_delete_item_exception(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'absent',
            'expiration_duration': None,
            'recycle_bin_id': 'e0684b39-0029-4be2-b5bf-67b8c145e1b8',
            'resource_name': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=[
                MockRecycleBinApi.RECYCLE_BIN_ITEM_VOLUME,
                MockApiException
            ])
        self._capture_fail(
            MockRecycleBinApi.get_recycle_bin_exception_response('delete_exception'),
            recycle_bin_module_mock)

    def test_delete_item_diff_mode(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'absent',
            'expiration_duration': None,
            'recycle_bin_id': 'e0684b39-0029-4be2-b5bf-67b8c145e1b8',
            'resource_name': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.module._diff = True
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=[
                MockRecycleBinApi.RECYCLE_BIN_ITEM_VOLUME,
                None
            ])
        recycle_bin_module_mock.perform_module_operation()
        result = recycle_bin_module_mock.module.exit_json.call_args[1]
        assert result['changed'] is True
        assert 'diff' in result

    # ===== EMPTY RECYCLE BIN TESTS =====

    def test_empty_recycle_bin(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'absent',
            'expiration_duration': None,
            'recycle_bin_id': None,
            'resource_name': None,
            'empty_recycle_bin': True
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=[
                MockRecycleBinApi.RECYCLE_BIN_ITEMS,  # get items
                None  # empty
            ])
        recycle_bin_module_mock.perform_module_operation()
        assert recycle_bin_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_empty_recycle_bin_already_empty(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'absent',
            'expiration_duration': None,
            'recycle_bin_id': None,
            'resource_name': None,
            'empty_recycle_bin': True
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            return_value=MockRecycleBinApi.RECYCLE_BIN_EMPTY)
        recycle_bin_module_mock.perform_module_operation()
        assert recycle_bin_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_empty_recycle_bin_check_mode(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'absent',
            'expiration_duration': None,
            'recycle_bin_id': None,
            'resource_name': None,
            'empty_recycle_bin': True
        })
        recycle_bin_module_mock.module.check_mode = True
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            return_value=MockRecycleBinApi.RECYCLE_BIN_ITEMS)
        recycle_bin_module_mock.perform_module_operation()
        assert recycle_bin_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_empty_recycle_bin_exception(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'absent',
            'expiration_duration': None,
            'recycle_bin_id': None,
            'resource_name': None,
            'empty_recycle_bin': True
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=[
                MockRecycleBinApi.RECYCLE_BIN_ITEMS,
                MockApiException
            ])
        self._capture_fail(
            MockRecycleBinApi.get_recycle_bin_exception_response('empty_exception'),
            recycle_bin_module_mock)

    def test_empty_recycle_bin_diff_mode(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'absent',
            'expiration_duration': None,
            'recycle_bin_id': None,
            'resource_name': None,
            'empty_recycle_bin': True
        })
        recycle_bin_module_mock.module._diff = True
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=[
                MockRecycleBinApi.RECYCLE_BIN_ITEMS,
                None
            ])
        recycle_bin_module_mock.perform_module_operation()
        result = recycle_bin_module_mock.module.exit_json.call_args[1]
        assert result['changed'] is True
        assert 'diff' in result

    # ===== ABSENT NO PARAMS TEST =====

    def test_absent_no_params(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'absent',
            'expiration_duration': None,
            'recycle_bin_id': None,
            'resource_name': None,
            'empty_recycle_bin': False
        })
        self._capture_fail(
            MockRecycleBinApi.get_recycle_bin_exception_response('absent_no_params'),
            recycle_bin_module_mock)

    # ===== DUPLICATE NAME TEST =====

    def test_duplicate_name_exception(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': None,
            'recycle_bin_id': None,
            'resource_name': 'dup_name',
            'resource_type': 'volume',
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            return_value=MockRecycleBinApi.DUPLICATE_NAME_ITEMS)
        self._capture_fail(
            MockRecycleBinApi.get_recycle_bin_exception_response('duplicate_name'),
            recycle_bin_module_mock)

    # ===== GET ITEMS EXCEPTION TEST =====

    def test_get_recycle_bin_items_exception(self, recycle_bin_module_mock):
        self._set_params(recycle_bin_module_mock, {
            'state': 'present',
            'expiration_duration': None,
            'recycle_bin_id': None,
            'resource_name': None,
            'empty_recycle_bin': False
        })
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=[
                MockRecycleBinApi.RECYCLE_BIN_CONFIG,  # get config
                MockApiException  # get items fails
            ])
        self._capture_fail(
            MockRecycleBinApi.get_recycle_bin_exception_response('get_items_exception'),
            recycle_bin_module_mock)

    # ===== GET ITEM 404 TEST =====

    def test_get_item_404_returns_none(self, recycle_bin_module_mock):
        """Test that get_recycle_bin_item returns None on 404."""
        mock_exc = MockApiException()
        mock_exc.err_code = "1"
        mock_exc.status_code = "404"
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=mock_exc)
        utils.PowerStoreException = MockApiException
        result = recycle_bin_module_mock.get_recycle_bin_item('nonexistent')
        assert result is None

    def test_get_item_non_404_exception(self, recycle_bin_module_mock):
        """Test that get_recycle_bin_item fails on non-404 errors."""
        mock_exc = MockApiException()
        mock_exc.err_code = "1"
        mock_exc.status_code = "500"
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            side_effect=mock_exc)
        try:
            recycle_bin_module_mock.get_recycle_bin_item('some-id')
        except FailJsonException as fj:
            assert "Failed to get recycle bin item" in fj.message

    def test_get_items_returns_none_response(self, recycle_bin_module_mock):
        """Test that get_recycle_bin_items handles None response."""
        recycle_bin_module_mock.provisioning.client.request = MagicMock(
            return_value=None)
        result = recycle_bin_module_mock.get_recycle_bin_items()
        assert result == []

    def test_resolve_item_returns_none_no_params(self, recycle_bin_module_mock):
        """Test that _resolve_item returns None when no ID or name given."""
        self._set_params(recycle_bin_module_mock, {
            'recycle_bin_id': None,
            'resource_name': None,
            'resource_type': None
        })
        result = recycle_bin_module_mock._resolve_item()
        assert result is None

    def test_get_item_by_name_generic_exception(self, recycle_bin_module_mock):
        """Test get_recycle_bin_item_by_name with generic exception path."""
        recycle_bin_module_mock.get_recycle_bin_items = MagicMock(
            side_effect=Exception())
        try:
            recycle_bin_module_mock.get_recycle_bin_item_by_name('test', 'volume')
        except FailJsonException as fj:
            assert "Failed to find recycle bin item by name" in fj.message

    # ===== MAIN TEST =====

    def test_main(self):
        main()
