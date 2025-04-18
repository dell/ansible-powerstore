# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries. \
    fail_json import FailJsonException, fail_json


class PowerStoreUnitBase:

    '''Powerstore Unit Test Base Class'''

    @pytest.fixture
    def powerstore_module_mock(self, mocker, module_object):
        exception_class_path = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils.PowerStoreException'
        mocker.patch(exception_class_path, new=MockApiException)
        powerstore_module_mock = module_object()
        powerstore_module_mock.module = MagicMock()
        powerstore_module_mock.module.fail_json = fail_json
        powerstore_module_mock.module.check_mode = False
        return powerstore_module_mock

    def capture_fail_json_call(self, error_msg, module_mock, module_handler=None, invoke_perform_module=False):
        try:
            if not invoke_perform_module:
                module_handler().handle(module_mock, module_mock.module.params)
            else:
                module_mock.perform_module_operation()
        except FailJsonException as fj_object:
            if error_msg not in fj_object.message:
                raise AssertionError(fj_object.message)

    def capture_fail_json_method(self, error_msg, module_mock, function_name, *args, **kwargs):
        try:
            func = getattr(module_mock, function_name)
            func(*args, **kwargs)
        except FailJsonException as fj_object:
            if error_msg not in fj_object.message:
                raise AssertionError(fj_object.message)

    def set_module_params(self, module_mock, get_module_args, params):
        get_module_args.update(params)
        module_mock.module.params = get_module_args
