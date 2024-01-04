# Copyright: (c) 2022-24, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Quota module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.shared_library import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_quota_api import MockQuotaApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.quota import PowerStoreQuota, main
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.shared_library.powerstore_unit_base \
    import PowerStoreUnitBase


class TestPowerStoreQuota(PowerStoreUnitBase):

    get_module_args = MockQuotaApi.QUOTA_COMMON_ARGS

    path_1 = "/ansible_tree_quota_FS1_path2"
    filesystem_1 = "629494e2-f86e-63ef-3d95-827ee627f9b1"
    quota_id_1 = "61d68a87-6000-3cc3-f816-96e8abdcbab0"
    unix_name_1 = "ldap_test_user_1"

    @pytest.fixture
    def module_object(self):
        return PowerStoreQuota

    @pytest.mark.parametrize("assert_data", [
        {
            "expected_value": MockQuotaApi.MODULE_OPERATION_ERROR1,
            "quota": None,
            "q_type": None,
            "windows_name": None,
            "description": None
        },
        {
            "expected_value": MockQuotaApi.MODULE_OPERATION_ERROR2,
            "quota": MockQuotaApi.QUOTA_DETAILS[0],
            "q_type": "user",
            "windows_name": None,
            "description": "Error Description"
        },
        {
            "expected_value": MockQuotaApi.MODULE_OPERATION_ERROR3,
            "quota": MockQuotaApi.QUOTA_DETAILS[0],
            "q_type": "tree",
            "windows_name": None,
            "description": None
        },
        {
            "expected_value": MockQuotaApi.MODULE_OPERATION_ERROR4,
            "quota": None,
            "q_type": None,
            "windows_name": "domainuser",
            "description": None
        },
        {
            "expected_value": MockQuotaApi.MODULE_OPERATION_ERROR5,
            "quota": None,
            "q_type": None,
            "windows_name": None,
            "description": ""
        },
        {
            "expected_value": MockQuotaApi.MODULE_OPERATION_ERROR6,
            "quota": None,
            "q_type": None,
            "windows_name": None,
            "description": " Description with Space "
        }
    ])
    def test_perform_module_operation_errors(self, powerstore_module_mock, assert_data):

        self.get_module_args.update({
            'quota_id': self.quota_id_1,
            'filesystem': self.filesystem_1,
            'quota': {
                'soft_limit': 200,
                'hard_limit': 500,
                'cap_unit': "GB"
            },
            'state': "present",
            'unix_name': self.unix_name_1,
            'windows_name': assert_data.get("windows_name"),
            'description': assert_data.get("description")
        })
        expected_value = assert_data.get("expected_value")
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.get_quota_details = MagicMock(
            return_value=(assert_data.get("quota"), assert_data.get("q_type")))
        self.capture_fail_json_call(expected_value,
                                    powerstore_module_mock,
                                    invoke_perform_module=True)

    @pytest.mark.parametrize("assert_data", [
        {
            "description": None,
            "hard_limit": None,
            "soft_limit": None,
            "changed": False
        },
        {
            "description": MockQuotaApi.MODULE_OPERATION_DESCRIPTION1,
            "hard_limit": None,
            "soft_limit": None,
            "changed": True
        },
        {
            "description": MockQuotaApi.MODULE_OPERATION_DESCRIPTION2,
            "hard_limit": 200,
            "soft_limit": None,
            "changed": True
        },
        {
            "description": MockQuotaApi.MODULE_OPERATION_DESCRIPTION2,
            "hard_limit": None,
            "soft_limit": 200,
            "changed": True
        }
    ])
    def test_perform_module_operation_modify(self, powerstore_module_mock, assert_data):
        self.get_module_args.update({
            'quota_id': self.quota_id_1,
            'filesystem': self.filesystem_1,
            'description': assert_data.get("description"),
            'quota': {
                'soft_limit': assert_data.get("soft_limit"),
                'hard_limit': assert_data.get("hard_limit"),
                'cap_unit': "GB"
            },
            'state': "present",
        })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.get_quota_details = MagicMock(
            return_value=(MockQuotaApi.QUOTA_DETAILS[0], None))
        powerstore_module_mock.show_quota_details = MagicMock(
            return_value=(MockQuotaApi.QUOTA_DETAILS[0]))
        powerstore_module_mock.update_quota = MagicMock(
            return_value=True
        )
        powerstore_module_mock.perform_module_operation()
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is assert_data.get(
            "changed")
        assert powerstore_module_mock.module.exit_json.call_args[
            1]['quota_details'] == MockQuotaApi.QUOTA_DETAILS[0]

    def test_perform_module_operation_create(self, powerstore_module_mock):
        self.get_module_args.update({
            'filesystem': self.filesystem_1,
            'description': "Test Quota description",
            'quota': {
                'soft_limit': 200,
                'hard_limit': 200,
                'cap_unit': "GB"
            },
            'state': "present",
        })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.get_quota_details = MagicMock(
            return_value=(None, None))
        powerstore_module_mock.show_quota_details = MagicMock(
            return_value=(MockQuotaApi.QUOTA_DETAILS[0]))
        powerstore_module_mock.create_quota = MagicMock(
            return_value=self.quota_id_1
        )
        powerstore_module_mock.perform_module_operation()
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is True
        assert powerstore_module_mock.module.exit_json.call_args[
            1]['quota_details'] == MockQuotaApi.QUOTA_DETAILS[0]

    def test_perform_module_operation_absent(self, powerstore_module_mock):
        self.get_module_args.update({
            'description': MockQuotaApi.MODULE_OPERATION_DESCRIPTION3,
            'state': "absent",
        })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.get_quota_details = MagicMock(
            return_value=(MockQuotaApi.QUOTA_DETAILS[0], None))
        powerstore_module_mock.show_quota_details = MagicMock(
            return_value=(None))
        powerstore_module_mock.delete_quota = MagicMock(
            return_value=True
        )
        powerstore_module_mock.perform_module_operation()
        assert powerstore_module_mock.module.exit_json.call_args[1]['changed'] is True
        assert powerstore_module_mock.module.exit_json.call_args[1]['quota_details'] is None

    def test_update_quota_tree(self, powerstore_module_mock):
        powerstore_module_mock.enable_quotas = MagicMock(
            return_value=None
        )
        powerstore_module_mock.provisioning.update_tree_quota = MagicMock(
            return_value=None
        )
        quota_details = {
            'file_system': {'id': self.filesystem_1},
            'id': self.quota_id_1
        }
        quota_type, description = "tree", None
        hard_limit, soft_limit = None, None
        result = powerstore_module_mock.update_quota(quota_type, quota_details, description,
                                                     hard_limit, soft_limit)
        powerstore_module_mock.provisioning.update_tree_quota.assert_called()
        assert result is True

    def test_update_quota_user(self, powerstore_module_mock):
        powerstore_module_mock.enable_quotas = MagicMock(
            return_value=None
        )
        powerstore_module_mock.provisioning.update_user_quota = MagicMock(
            return_value=None
        )
        quota_details = {
            'file_system': {'id': self.filesystem_1},
            'id': self.quota_id_1
        }
        quota_type, description = "user", None
        hard_limit, soft_limit = None, None
        result = powerstore_module_mock.update_quota(quota_type, quota_details, description,
                                                     hard_limit, soft_limit)
        powerstore_module_mock.provisioning.update_user_quota.assert_called()
        assert result is True

    def test_update_quota_empty(self, powerstore_module_mock):
        powerstore_module_mock.enable_quotas = MagicMock(
            return_value=None
        )
        quota_details = {
            'file_system': {'id': self.filesystem_1},
            'id': self.quota_id_1
        }
        quota_type, description = None, None
        hard_limit, soft_limit = None, None
        result = powerstore_module_mock.update_quota(quota_type, quota_details, description,
                                                     hard_limit, soft_limit)
        powerstore_module_mock.provisioning.update_user_quota.assert_not_called()
        powerstore_module_mock.provisioning.update_tree_quota.assert_not_called()
        assert result is None

    def test_update_quota_exception(self, powerstore_module_mock):
        powerstore_module_mock.enable_quotas = MagicMock(
            side_effect=MockApiException
        )
        quota_details = {
            'file_system': {'id': self.filesystem_1},
            'id': self.quota_id_1
        }
        quota_type, description = None, None
        hard_limit, soft_limit = None, None
        expected_value = MockQuotaApi.UPDATE_QUOTA_ERROR1
        self.capture_fail_json_method(expected_value, powerstore_module_mock,
                                      "update_quota", quota_type, quota_details, description,
                                      hard_limit, soft_limit)

    def test_create_quota_tree(self, powerstore_module_mock):
        quota_type = "tree"
        path = self.path_1
        filesystem = self.filesystem_1
        description = None
        windows_name = None
        windows_sid = None
        unix_name = None
        uid = None
        hard_limit = None
        soft_limit = None
        powerstore_module_mock.enable_quotas = MagicMock(
            return_value=None
        )
        powerstore_module_mock.provisioning.create_tree_quota = MagicMock(
            return_value={'id': self.quota_id_1}
        )
        result = powerstore_module_mock.create_quota(quota_type, path, filesystem,
                                                     description, windows_name, windows_sid,
                                                     unix_name, uid, hard_limit, soft_limit)
        powerstore_module_mock.provisioning.create_tree_quota.assert_called()
        assert result is self.quota_id_1

    def test_create_quota_tree_error(self, powerstore_module_mock):
        quota_type = "tree"
        path = None
        filesystem = None
        unix_name = None
        expected_value = MockQuotaApi.CREATE_QUOTA_ERROR1
        self.capture_fail_json_method(expected_value, powerstore_module_mock, "create_quota",
                                      quota_type=quota_type, unix_name=unix_name,
                                      path=path, filesystem=filesystem)

    def test_create_quota_tree_exception(self, powerstore_module_mock):
        quota_type = "tree"
        path = self.path_1
        filesystem = self.filesystem_1
        unix_name = None
        self.get_module_args.update({
            'filesystem': self.filesystem_1,
        })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.enable_quotas = MagicMock(
            return_value=None
        )
        powerstore_module_mock.provisioning.create_tree_quota = MagicMock(
            side_effect=MockApiException
        )
        expected_value = MockQuotaApi.CREATE_QUOTA_ERROR2
        self.capture_fail_json_method(expected_value, powerstore_module_mock, "create_quota",
                                      quota_type=quota_type, unix_name=unix_name,
                                      path=path, filesystem=filesystem)

    def test_create_quota_user(self, powerstore_module_mock):
        quota_type = "user"
        path = self.path_1
        filesystem = self.filesystem_1
        unix_name = self.unix_name_1
        powerstore_module_mock.enable_quotas = MagicMock(
            return_value=None
        )
        powerstore_module_mock.provisioning.get_tree_quota_id = MagicMock(
            return_value=self.quota_id_1
        )
        powerstore_module_mock.provisioning.enforce_user_quota_on_tree_quota = MagicMock(
            return_value=None
        )
        powerstore_module_mock.provisioning.create_user_quota = MagicMock(
            return_value={'id': self.quota_id_1}
        )
        result = powerstore_module_mock.create_quota(quota_type=quota_type, unix_name=unix_name,
                                                     path=path, filesystem=filesystem)
        powerstore_module_mock.provisioning.create_user_quota.assert_called()
        assert result is self.quota_id_1

    def test_create_quota_user_error(self, powerstore_module_mock):
        quota_type = "user"
        path = None
        filesystem = self.filesystem_1
        unix_name = None
        powerstore_module_mock.enable_quotas = MagicMock(
            return_value=None
        )
        powerstore_module_mock.provisioning.get_tree_quota_id = MagicMock(
            return_value=self.quota_id_1
        )
        powerstore_module_mock.provisioning.enforce_user_quota_on_tree_quota = MagicMock(
            return_value=None
        )
        powerstore_module_mock.provisioning.create_user_quota = MagicMock(
            return_value={'id': self.quota_id_1}
        )
        expected_value = MockQuotaApi.CREATE_QUOTA_ERROR3
        self.capture_fail_json_method(expected_value, powerstore_module_mock, "create_quota",
                                      quota_type=quota_type, unix_name=unix_name,
                                      path=path, filesystem=filesystem)

    @pytest.mark.parametrize("assert_data", [
        {
            'uid': 'uid-123-unique-id',
            'unix_name': None,
            'windows_name': None,
            'windows_sid': None,
            'expected_value': MockQuotaApi.CREATE_QUOTA_ERROR4,
        },
        {
            'uid': None,
            'unix_name': 'unix_name',
            'windows_name': None,
            'windows_sid': None,
            'expected_value': MockQuotaApi.CREATE_QUOTA_ERROR5,
        },
        {
            'uid': None,
            'unix_name': None,
            'windows_name': 'windows_name',
            'windows_sid': None,
            'expected_value': MockQuotaApi.CREATE_QUOTA_ERROR6,
        },
        {
            'uid': None,
            'unix_name': None,
            'windows_name': None,
            'windows_sid': 'windows_sid',
            'expected_value': MockQuotaApi.CREATE_QUOTA_ERROR7,
        },
    ])
    def test_create_quota_user_fail_exception(self, powerstore_module_mock, assert_data):
        quota_type = "user"
        path = None
        filesystem = self.filesystem_1

        unix_name = assert_data.get('unix_name')
        uid = assert_data.get('uid')
        windows_name = assert_data.get('windows_name')
        windows_sid = assert_data.get('windows_sid')

        powerstore_module_mock.enable_quotas = MagicMock(
            return_value=None
        )
        powerstore_module_mock.provisioning.get_tree_quota_id = MagicMock(
            return_value=self.quota_id_1
        )
        powerstore_module_mock.provisioning.enforce_user_quota_on_tree_quota = MagicMock(
            return_value=None
        )
        powerstore_module_mock.provisioning.create_user_quota = MagicMock(
            side_effect=MockApiException
        )
        expected_value = assert_data.get('expected_value')
        self.capture_fail_json_method(expected_value, powerstore_module_mock, "create_quota",
                                      quota_type=quota_type, unix_name=unix_name,
                                      path=path, filesystem=filesystem, uid=uid,
                                      windows_name=windows_name, windows_sid=windows_sid)

    def test_delete_quota_success(self, powerstore_module_mock):
        powerstore_module_mock.provisioning.delete_tree_quota = MagicMock(
            return_value=None
        )
        result = powerstore_module_mock.delete_quota("tree", "")
        assert result is True

    def test_delete_quota_not_supported(self, powerstore_module_mock):
        expected_value = MockQuotaApi.DELETE_QUOTA_ERROR1.format(
            self.quota_id_1)
        self.capture_fail_json_method(expected_value, powerstore_module_mock, "delete_quota",
                                      "user", self.quota_id_1)

    def test_enforce_user_quota_on_tree_quota(self, powerstore_module_mock):
        powerstore_module_mock.get_tree_quota_details = MagicMock(
            return_value={
                'is_user_quotas_enforced': False,
                'id': self.quota_id_1}
        )
        powerstore_module_mock.provisioning.update_tree_quota = MagicMock(
            return_value=None
        )
        powerstore_module_mock.enforce_user_quota_on_tree_quota(
            self.path_1, self.filesystem_1)
        powerstore_module_mock.provisioning.update_tree_quota.assert_called()

    def test_enforce_user_quota_on_tree_quota_exception(self, powerstore_module_mock):
        powerstore_module_mock.get_tree_quota_details = MagicMock(
            side_effect=MockApiException
        )
        expected_value = MockQuotaApi.QUOTA_ERROR1
        self.capture_fail_json_method(expected_value, powerstore_module_mock,
                                      "enforce_user_quota_on_tree_quota",
                                      self.path_1, self.filesystem_1)

    def test_enable_quotas(self, powerstore_module_mock):
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value={
                'is_quota_enabled': False
            }
        )
        powerstore_module_mock.provisioning.modify_filesystem = MagicMock(
            return_value=None
        )
        powerstore_module_mock.enable_quotas(self.filesystem_1)
        powerstore_module_mock.provisioning.modify_filesystem.assert_called()

    def test_enable_quotas(self, powerstore_module_mock):
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value={
                'is_quota_enabled': True
            }
        )
        powerstore_module_mock.enable_quotas(self.filesystem_1)
        powerstore_module_mock.provisioning.modify_filesystem.assert_not_called()

    def test_enable_quotas_execption(self, powerstore_module_mock):
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value={
                'is_quota_enabled': False
            }
        )
        powerstore_module_mock.provisioning.modify_filesystem = MagicMock(
            side_effect=MockApiException
        )
        expected_value = MockQuotaApi.QUOTA_ERROR2
        self.capture_fail_json_method(expected_value, powerstore_module_mock,
                                      "enable_quotas",
                                      self.filesystem_1)

    def test_convert_quota_thresholds_error(self, powerstore_module_mock):
        quota = {
            'soft_limit': -1,
            'hard_limit': 100
        }
        expected_value = MockQuotaApi.QUOTA_ERROR3
        self.capture_fail_json_method(expected_value, powerstore_module_mock,
                                      "convert_quota_thresholds",
                                      quota)

    @pytest.mark.parametrize("assert_data", [
        {
            'quota_details': MockQuotaApi.QUOTA_DETAILS[0],
            'quota_type': 'user',
            'assert_quota_type': 'user'
        },
        {
            'quota_details': None,
            'quota_type': 'user',
            'assert_quota_type': None
        },
        {
            'quota_details': MockQuotaApi.QUOTA_DETAILS[0],
            'quota_type': 'tree',
            'assert_quota_type': 'tree'
        },
        {
            'quota_details': None,
            'quota_type': 'tree',
            'assert_quota_type': None
        },
        {
            'quota_details': None,
            'quota_type': None,
            'assert_quota_type': None
        }
    ])
    def test_get_quota_details_user(self, powerstore_module_mock, assert_data):
        quota_id = None
        quota_type = assert_data.get('quota_type')
        powerstore_module_mock.get_user_quota_details = MagicMock(
            return_value=assert_data.get('quota_details')
        )
        powerstore_module_mock.get_tree_quota_details = MagicMock(
            return_value=assert_data.get('quota_details')
        )
        quota_details, q_type = powerstore_module_mock.get_quota_details(
            quota_id, quota_type=quota_type)
        assert quota_details == assert_data.get('quota_details')
        assert q_type == assert_data.get('assert_quota_type')

    def test_get_tree_quota_id(self, powerstore_module_mock):
        powerstore_module_mock.get_tree_quota_details = MagicMock(
            return_value=MockQuotaApi.QUOTA_DETAILS[0]
        )
        quota_detail_id = powerstore_module_mock.get_tree_quota_id(
            self.path_1, self.filesystem_1)
        assert quota_detail_id == MockQuotaApi.QUOTA_DETAILS[0]['id']

    def test_get_tree_quota_error(self, powerstore_module_mock):
        powerstore_module_mock.get_tree_quota_details = MagicMock(
            return_value=None
        )
        expected_value = MockQuotaApi.QUOTA_EXPECTED1
        self.capture_fail_json_method(expected_value, powerstore_module_mock,
                                      "get_tree_quota_id",
                                      self.path_1, self.filesystem_1)

    def test_get_user_quota_details_quota_id(self, powerstore_module_mock):
        powerstore_module_mock.provisioning.get_user_quota = MagicMock(
            return_value=MockQuotaApi.QUOTA_DETAILS[0]
        )
        quota_details = powerstore_module_mock.get_user_quota_details(
            self.quota_id_1)
        assert quota_details == MockQuotaApi.QUOTA_DETAILS[0]

    @pytest.mark.parametrize("assert_data", [
        {
            'tree_quota_id': None,
            'path': '/path',
            'assert_quota_details': MockQuotaApi.QUOTA_DETAILS[0]
        },
        {
            'tree_quota_id': None,
            'path': None,
            'assert_quota_details': MockQuotaApi.QUOTA_DETAILS[0]
        },
        {
            'tree_quota_id': "0000-ffff-0000-0000-000000000000",
            'path': None,
            'assert_quota_details': None
        }
    ])
    def test_get_user_quota_details_quota_details(self, powerstore_module_mock, assert_data):
        mock_data = MockQuotaApi.QUOTA_DETAILS[0]
        mock_data.update({'tree_quota_id': assert_data.get('tree_quota_id')})
        unix_name = self.unix_name_1
        path = assert_data.get('path')
        powerstore_module_mock.provisioning.get_user_quota = MagicMock(
            return_value=MockQuotaApi.QUOTA_DETAILS
        )
        quota_details = powerstore_module_mock.get_user_quota_details(None, path=path,
                                                                      filesystem_id=self.filesystem_1,
                                                                      unix_name=unix_name)
        assert quota_details == assert_data.get('assert_quota_details')

    def test_get_user_quota_details_quota_details_error(self, powerstore_module_mock):
        unix_name = None
        powerstore_module_mock.provisioning.get_user_quota = MagicMock(
            return_value=MockQuotaApi.QUOTA_DETAILS
        )
        expected_value = MockQuotaApi.QUOTA_EXPECTED2
        self.capture_fail_json_method(expected_value, powerstore_module_mock,
                                      "get_user_quota_details",
                                      None, path=None, filesystem_id=self.filesystem_1,
                                      unix_name=unix_name)

    @pytest.mark.parametrize("assert_data", [
        {
            'uid': 'uid-123-unique-id',
            'unix_name': None,
            'windows_name': None,
            'windows_sid': None,
            'expected_value': MockQuotaApi.QUOTA_EXPECTED3,
        },
        {
            'uid': None,
            'unix_name': 'unix_name',
            'windows_name': None,
            'windows_sid': None,
            'expected_value': MockQuotaApi.QUOTA_EXPECTED4,
        },
        {
            'uid': None,
            'unix_name': None,
            'windows_name': 'windows_name',
            'windows_sid': None,
            'expected_value': MockQuotaApi.QUOTA_EXPECTED5,
        },
        {
            'uid': None,
            'unix_name': None,
            'windows_name': None,
            'windows_sid': 'windows_sid',
            'expected_value': MockQuotaApi.QUOTA_EXPECTED6,
        },
    ])
    def test_get_user_quota_details_quota_details_exception(self, powerstore_module_mock, assert_data):
        powerstore_module_mock.provisioning.get_user_quota = MagicMock(
            side_effect=MockApiException
        )
        unix_name = assert_data.get('unix_name')
        expected_value = assert_data.get('expected_value')
        uid = assert_data.get('uid')
        win_name = assert_data.get('windows_name')
        win_sid = assert_data.get('windows_sid')
        self.capture_fail_json_method(expected_value, powerstore_module_mock,
                                      "get_user_quota_details",
                                      None, path=self.path_1, filesystem_id=self.filesystem_1,
                                      unix_name=unix_name, uid=uid, win_name=win_name,
                                      win_sid=win_sid)

    @pytest.mark.parametrize("assert_data", [
        {
            'nas_server': 'nas-server',
            'nas_id': 'nas_id',
        },
        {
            'nas_server': None,
            'nas_id': 'nas_id',
        }
    ])
    def test_get_nas_server_id(self, powerstore_module_mock, assert_data):
        nas_server = assert_data.get('nas_server')
        nas_id = assert_data.get('nas_id')
        powerstore_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=[{'id': nas_id}]
        )
        powerstore_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value={'id': nas_id}
        )
        nas_server_id = powerstore_module_mock.get_nas_server_id(nas_server)
        assert nas_server_id == nas_id

    @pytest.mark.parametrize("assert_data", [
        {
            'nas_server': 'nas-server',
            'expected_value': MockQuotaApi.QUOTA_EXPECTED7
        },
        {
            'nas_server': None,
            'expected_value': MockQuotaApi.QUOTA_EXPECTED8
        }
    ])
    def test_get_nas_server_id_exception(self, powerstore_module_mock, assert_data):
        nas_server = assert_data.get('nas_server')
        expected_value = assert_data.get('expected_value')
        powerstore_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            side_effect=MockApiException
        )
        powerstore_module_mock.provisioning.get_nas_server_details = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(expected_value, powerstore_module_mock,
                                      "get_nas_server_id",
                                      nas_server)

    def test_get_filesystem_id(self, powerstore_module_mock):
        filesystem, nas_server = "filesystem", "nas-server"
        powerstore_module_mock.provisioning.get_nas_server_id = MagicMock(
            return_value=[{'id': self.filesystem_1}]
        )
        powerstore_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=[{'id': self.filesystem_1}]
        )
        filesystem_id = powerstore_module_mock.get_filesystem_id(
            filesystem, nas_server)
        assert filesystem_id == self.filesystem_1

    @pytest.mark.parametrize("assert_data", [
        {
            "nas_server": None,
            "expected_value": MockQuotaApi.QUOTA_EXPECTED9
        },
        {
            "nas_server": "nas-server",
            "expected_value": "No File System found with"
        }
    ])
    def test_get_filesystem_id_error(self, powerstore_module_mock, assert_data):
        filesystem, nas_server = "filesystem", assert_data.get('nas_server')
        powerstore_module_mock.provisioning.get_nas_server_id = MagicMock(
            return_value=[{'id': self.filesystem_1}]
        )
        powerstore_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=None
        )
        expected_value = assert_data.get('expected_value')
        self.capture_fail_json_method(expected_value, powerstore_module_mock,
                                      "get_filesystem_id",
                                      filesystem, nas_server)

    def test_get_filesystem_id_exception(self, powerstore_module_mock):
        filesystem, nas_server = self.filesystem_1, "nas-server"
        powerstore_module_mock.provisioning.get_filesystem_details = MagicMock(
            side_effect=MockApiException
        )
        expected_value = MockQuotaApi.QUOTA_EXPECTED10.format(
            self.filesystem_1)
        self.capture_fail_json_method(expected_value, powerstore_module_mock,
                                      "get_filesystem_id",
                                      filesystem, nas_server)

    @pytest.mark.parametrize("assert_data", [
        {
            'quota_id': "quota_id",
            'quota_details': MockQuotaApi.QUOTA_DETAILS[0],
            'assert_quota_details': MockQuotaApi.QUOTA_DETAILS[0]
        },
        {
            'quota_id': None,
            'quota_details': MockQuotaApi.QUOTA_DETAILS,
            'assert_quota_details': MockQuotaApi.QUOTA_DETAILS[0]
        },
        {
            'quota_id': None,
            'quota_details': None,
            'assert_quota_details': None
        }
    ])
    def test_get_tree_quota_details(self, powerstore_module_mock, assert_data):
        quota_id = assert_data.get('quota_id')
        path = self.path_1
        filesystem_id = self.filesystem_1
        powerstore_module_mock.provisioning.get_tree_quota = MagicMock(
            return_value=assert_data.get('quota_details')
        )
        quota_details = powerstore_module_mock.get_tree_quota_details(quota_id=quota_id,
                                                                      path=path,
                                                                      filesystem_id=filesystem_id)
        assert quota_details == assert_data.get('assert_quota_details')

    def test_get_tree_quota_details_error(self, powerstore_module_mock):
        quota_id = None
        path = self.path_1
        filesystem_id = None
        expected_value = MockQuotaApi.QUOTA_EXPECTED11
        self.capture_fail_json_method(expected_value, powerstore_module_mock, "get_tree_quota_details",
                                      quota_id=quota_id, path=path, filesystem_id=filesystem_id)

    def test_show_quota_details_tree(self, powerstore_module_mock):
        quota_id = None
        quota_type = "tree"
        path = self.path_1
        filesystem_id = self.filesystem_1
        uid = None
        unix_name = None
        windows_name = None
        windows_sid = None
        state = "present"
        powerstore_module_mock.get_quota_details = MagicMock(
            return_value=(MockQuotaApi.QUOTA_DETAILS[0], None)
        )
        quota_details = powerstore_module_mock.show_quota_details(quota_id, quota_type,
                                                                  path, filesystem_id, uid,
                                                                  unix_name, windows_name,
                                                                  windows_sid, state)
        assert quota_details == MockQuotaApi.QUOTA_DETAILS[0]

    def test_show_quota_details_user(self, powerstore_module_mock):
        quota_id = None
        quota_type = "user"
        path = self.path_1
        filesystem_id = self.filesystem_1
        uid = None
        unix_name = None
        windows_name = None
        windows_sid = None
        state = "present"
        powerstore_module_mock.get_quota_details = MagicMock(
            return_value=(MockQuotaApi.QUOTA_DETAILS[0], None)
        )
        quota_details = powerstore_module_mock.show_quota_details(quota_id, quota_type,
                                                                  path, filesystem_id, uid,
                                                                  unix_name, windows_name,
                                                                  windows_sid, state)
        assert "tree_quota_for_user_quota" in quota_details

    def test_show_quota_details_empty(self, powerstore_module_mock):
        quota_id = None
        quota_type = None
        path = self.path_1
        filesystem_id = self.filesystem_1
        uid = None
        unix_name = None
        windows_name = None
        windows_sid = None
        state = None
        quota_details = powerstore_module_mock.show_quota_details(quota_id, quota_type,
                                                                  path, filesystem_id, uid,
                                                                  unix_name, windows_name,
                                                                  windows_sid, state)
        assert quota_details == {}

    def test_main(self):
        main()
