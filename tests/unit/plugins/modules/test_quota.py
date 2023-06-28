# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Quota module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_quota_api import MockQuotaApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_powerstore_connection = MagicMock()
utils.PowerStoreException = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerstore.plugins.modules.quota import PowerStoreQuota


class TestPowerStoreQuota():

    get_module_args = MockQuotaApi.QUOTA_COMMON_ARGS
    path_1 = "/ansible_tree_quota_FS1_path2"
    filesystem_1 = "629494e2-f86e-63ef-3d95-827ee627f9b1"
    quota_id_1 = "61d68a87-6000-3cc3-f816-96e8abdcbab0"
    unix_name_1 = "ldap_test_user_1"

    @pytest.fixture
    def quota_module_mock(self, mocker):
        mocker.patch(MockQuotaApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        quota_module_mock = PowerStoreQuota()
        quota_module_mock.module = MagicMock()
        return quota_module_mock

    def test_get_tree_quota_response(self, quota_module_mock):
        self.get_module_args.update({
            'quota_id': self.quota_id_1,
            'state': "present"
        })
        quota_module_mock.module.params = self.get_module_args
        quota_module_mock.provisioning.get_tree_quota = MagicMock(
            return_value=MockQuotaApi.QUOTA_DETAILS[0])
        quota_module_mock.perform_module_operation()
        quota_module_mock.provisioning.get_tree_quota.assert_called()

    def test_get_tree_quota_exception(self, quota_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'quota_id': self.quota_id_1,
            'state': "present"
        })
        quota_module_mock.module.params = self.get_module_args
        quota_module_mock.provisioning.get_tree_quota = MagicMock(
            return_value=MockQuotaApi.QUOTA_DETAILS[0])
        quota_module_mock.provisioning.get_tree_quota = MagicMock(
            side_effect=MockApiException)
        quota_module_mock.perform_module_operation()
        quota_module_mock.provisioning.get_tree_quota.assert_called()

    def test_get_user_quota_response(self, quota_module_mock):
        self.get_module_args.update({
            'quota_type': "user",
            'uid': 19,
            'path': self.path_1,
            'filesystem': self.filesystem_1,
            'state': "present"
        })
        quota_module_mock.module.params = self.get_module_args
        quota_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockQuotaApi.FILESYSTEM_DETAILS1[0])
        quota_module_mock.provisioning.get_user_quota = MagicMock(
            return_value=MockQuotaApi.QUOTA_DETAILS[0])
        quota_module_mock.perform_module_operation()
        quota_module_mock.provisioning.get_user_quota.assert_called()

    def test_create_user_quota_response(self, quota_module_mock):
        self.get_module_args.update({
            'quota_type': "user",
            'unix_name': "ldap_test_user_1",
            'path': self.path_1,
            'filesystem': self.filesystem_1,
            'quota': {
                'soft_limit': 200,
                'hard_limit': 500,
                'cap_unit': "GB"
            },
            'state': "present"
        })
        quota_module_mock.module.params = self.get_module_args
        quota_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockQuotaApi.FILESYSTEM_DETAILS1[0])
        quota_module_mock.provisioning.get_user_quota = MagicMock(
            return_value=None)
        quota_module_mock.perform_module_operation()
        quota_module_mock.provisioning.create_user_quota.assert_called()

    def test_create_tree_quota_response(self, quota_module_mock):
        self.get_module_args.update({
            'quota_type': "tree",
            'unix_name': self.unix_name_1,
            'path': self.path_1,
            'filesystem': self.filesystem_1,
            'quota': {
                'soft_limit': 50,
                'hard_limit': 90,
                'cap_unit': "GB"
            },
            'description': "Tree quota created on filesystem FS1.",
            'state': "present"
        })
        quota_module_mock.module.params = self.get_module_args
        quota_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockQuotaApi.FILESYSTEM_DETAILS1[0])
        quota_module_mock.provisioning.get_tree_quota = MagicMock(
            return_value=None)
        quota_module_mock.perform_module_operation()
        quota_module_mock.provisioning.create_tree_quota.assert_called()

    def test_create_tree_quota_exception(self, quota_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'quota_type': "tree",
            'unix_name': self.unix_name_1,
            'path': self.path_1,
            'filesystem': self.filesystem_1,
            'quota': {
                'soft_limit': 200,
                'hard_limit': 500,
                'cap_unit': "GB"
            },
            'description': "Tree quota created on filesystem FS1.",
            'state': "present"
        })
        quota_module_mock.module.params = self.get_module_args
        quota_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockQuotaApi.FILESYSTEM_DETAILS1[0])
        quota_module_mock.provisioning.get_tree_quota = MagicMock(
            return_value=None)
        quota_module_mock.provisioning.create_tree_quota = MagicMock(
            side_effect=MockApiException)
        quota_module_mock.perform_module_operation()
        quota_module_mock.provisioning.create_tree_quota.assert_called()

    def test_modify_tree_quota_response(self, quota_module_mock):
        self.get_module_args.update({
            'quota_type': "tree",
            'unix_name': self.unix_name_1,
            'path': self.path_1,
            'filesystem': "ansible_PS_SMB_quota_FS1",
            'nas_server': "ansible_nas_server_2",
            'quota': {
                'soft_limit': 70,
                'hard_limit': 98,
                'cap_unit': "GB"
            },
            'description': "Modifed Tree quota.",
            'state': "present"
        })
        quota_module_mock.module.params = self.get_module_args
        quota_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockQuotaApi.FILESYSTEM_DETAILS1)
        quota_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockQuotaApi.NAS_SERVER_DETAILS1)
        quota_module_mock.provisioning.get_tree_quota = MagicMock(
            return_value=MockQuotaApi.QUOTA_DETAILS2)
        quota_module_mock.perform_module_operation()
        quota_module_mock.provisioning.update_tree_quota.assert_called()

    def test_modify_tree_quota_exception(self, quota_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'quota_type': "tree",
            'unix_name': self.unix_name_1,
            'path': self.path_1,
            'filesystem': "ansible_PS_SMB_quota_FS1",
            'nas_server': "ansible_nas_server_2",
            'quota': {
                'soft_limit': 70,
                'hard_limit': 98,
                'cap_unit': "GB"
            },
            'description': "Modifed Tree quota.",
            'state': "present"
        })
        quota_module_mock.module.params = self.get_module_args
        quota_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockQuotaApi.FILESYSTEM_DETAILS1)
        quota_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockQuotaApi.NAS_SERVER_DETAILS1)
        quota_module_mock.provisioning.get_tree_quota = MagicMock(
            return_value=MockQuotaApi.QUOTA_DETAILS2)
        quota_module_mock.provisioning.update_tree_quota = MagicMock(
            rside_effect=MockApiException)
        quota_module_mock.perform_module_operation()
        quota_module_mock.provisioning.update_tree_quota.assert_called()

    def test_delete_tree_quota_response(self, quota_module_mock):
        self.get_module_args.update({
            'quota_type': "tree",
            'unix_name': self.unix_name_1,
            'path': self.path_1,
            'filesystem': "ansible_PS_SMB_quota_FS1",
            'nas_server': "ansible_nas_server_2",
            'state': "absent"
        })
        quota_module_mock.module.params = self.get_module_args
        quota_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockQuotaApi.FILESYSTEM_DETAILS1)
        quota_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockQuotaApi.NAS_SERVER_DETAILS1)
        quota_module_mock.provisioning.get_tree_quota = MagicMock(
            return_value=MockQuotaApi.QUOTA_DETAILS2)
        quota_module_mock.perform_module_operation()
        quota_module_mock.provisioning.delete_tree_quota.assert_called()

    def test_delete_tree_quota_exception(self, quota_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'quota_type': "tree",
            'unix_name': self.unix_name_1,
            'path': self.path_1,
            'filesystem': "ansible_PS_SMB_quota_FS1",
            'nas_server': "ansible_nas_server_2",
            'state': "absent"
        })
        quota_module_mock.module.params = self.get_module_args
        quota_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockQuotaApi.FILESYSTEM_DETAILS1)
        quota_module_mock.provisioning.get_nas_server_by_name = MagicMock(
            return_value=MockQuotaApi.NAS_SERVER_DETAILS1)
        quota_module_mock.provisioning.get_tree_quota = MagicMock(
            return_value=MockQuotaApi.QUOTA_DETAILS2)
        quota_module_mock.provisioning.delete_tree_quota = MagicMock(
            side_effect=MockApiException)
        quota_module_mock.perform_module_operation()
        quota_module_mock.provisioning.delete_tree_quota.assert_called()
