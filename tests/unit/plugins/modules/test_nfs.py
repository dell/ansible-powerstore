# Copyright: (c) 2024, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for NFS Export module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_nfs_api import MockNfsApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.nfs import PowerStoreNfsExport


class TestPowerstoreNfs():

    get_module_args = MockNfsApi.NFS_COMMON_ARGS
    filesystem_path = "/sample_file_system"

    @pytest.fixture
    def nfs_module_mock(self, mocker):
        mocker.patch(MockNfsApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        nfs_module_mock = PowerStoreNfsExport()
        nfs_module_mock.module = MagicMock()
        return nfs_module_mock

    def test_get_nfs_response(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_id': "61d6888b-52ed-0d4b-2b35-96e8abdcbab0",
            'state': "present"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.provisioning.get_nfs_export_details = MagicMock(
            return_value=MockNfsApi.NFS_DETAILS)
        nfs_module_mock.perform_module_operation()
        assert self.get_module_args['nfs_export_id'] == nfs_module_mock.module.exit_json.call_args[1]['nfs_export_details']['id']
        nfs_module_mock.provisioning.get_nfs_export_details.assert_called()

    def test_get_nfs_name_response(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_name': "sample_nfs_export",
            'nas_server': "Sample_nas_server_1",
            'state': "present"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.provisioning.get_nfs_export_details_by_name = MagicMock(
            return_value=MockNfsApi.NFS_DETAILS_BY_NAME)
        nfs_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNfsApi.NAS_SERVER_DETAILS)
        nfs_module_mock.perform_module_operation()
        assert self.get_module_args['nfs_export_name'] == nfs_module_mock.module.exit_json.call_args[1]['nfs_export_details']['name']
        nfs_module_mock.provisioning.get_nfs_export_details_by_name.assert_called()

    def test_get_nfs_name_nas_id_response(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_name': "sample_nfs_export",
            'filesystem': "sample_file_system",
            'nas_server': "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
            'state': "present"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.validate_input = MagicMock(
            return_value=MockNfsApi.get_nfs_export_wo_nas_failed_msg())
        nfs_module_mock.provisioning.get_nfs_export_details_by_name = MagicMock(
            return_value=MockNfsApi.NFS_DETAILS_BY_NAME)
        nfs_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNfsApi.NAS_SERVER_DETAILS)
        nfs_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockNfsApi.FILESYSTEM_DETAILS_BY_NAME)
        nfs_module_mock.perform_module_operation()
        nfs_module_mock.provisioning.get_nfs_export_details_by_name.assert_called()

    def test_get_nfs_name_nas_id_exception(self, nfs_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'nfs_export_name': "sample_nfs_export",
            'filesystem': "sample_file_system",
            'nas_server': "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
            'state': "present"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.validate_input = MagicMock(
            return_value=MockNfsApi.get_nfs_export_wo_nas_failed_msg())
        nfs_module_mock.provisioning.get_nfs_export_details_by_name = MagicMock(
            return_value=MockNfsApi.NFS_DETAILS_BY_NAME)
        nfs_module_mock.provisioning.get_nas_server_details = MagicMock(
            side_effect=MockApiException)
        nfs_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockNfsApi.FILESYSTEM_DETAILS_BY_NAME)
        nfs_module_mock.perform_module_operation()
        nfs_module_mock.provisioning.get_nas_server_details.assert_called()

    def test_get_nfs_fiesystem_no_nas(self, nfs_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'nfs_export_name': "sample_nfs_export",
            'filesystem': "sample_file_system",
            'state': "present"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.validate_input = MagicMock(
            return_value=MockNfsApi.get_nfs_export_wo_nas_failed_msg())
        nfs_module_mock.provisioning.get_nfs_export_details_by_name = MagicMock(
            return_value=MockNfsApi.NFS_DETAILS_BY_NAME)
        nfs_module_mock.perform_module_operation()
        assert MockNfsApi.get_nfs_export_wo_nas_failed_msg() in \
            nfs_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_nfs_fiesystem_exception(self, nfs_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'nfs_export_name': "sample_nfs_export",
            'filesystem': "61d68815-1ac2-fc68-7263-96e8abdcbab0",
            'state': "present"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.validate_input = MagicMock(
            return_value=MockNfsApi.get_nfs_export_wo_nas_failed_msg())
        nfs_module_mock.provisioning.get_nfs_export_details_by_name = MagicMock(
            return_value=MockNfsApi.NFS_DETAILS_BY_NAME)
        nfs_module_mock.provisioning.get_filesystem_details = MagicMock(
            side_effect=MockApiException)
        nfs_module_mock.perform_module_operation()
        nfs_module_mock.provisioning.get_filesystem_details.assert_called()

    def test_modify_nfs_empty_description_exception(self, nfs_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'nfs_export_id': "61d6888b-52ed-0d4b-2b35-96e8abdcbab0",
            'description': " ",
            'state': "present"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.provisioning.get_nfs_export_details = MagicMock(
            return_value=MockNfsApi.NFS_DETAILS)
        nfs_module_mock.perform_module_operation()
        assert MockNfsApi.modify_nfs_export_invalid_description_failed_msg() in \
            nfs_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_nfs_exception(self, nfs_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'nfs_export_id': "61d6888b-52ed-0d4b-2b35-96e8abdcbab0",
            'state': "present"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.provisioning.get_nfs_export_details = MagicMock(
            side_effect=MockApiException)
        nfs_module_mock.perform_module_operation()
        nfs_module_mock.provisioning.get_nfs_export_details.assert_called()

    def test_create_nfs_with_filesystem_response(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_name': "sample_nfs_export",
            'filesystem': "sample_file_system",
            'nas_server': "Sample_nas_server_1",
            'description': "This is new description",
            'default_access': "ROOT",
            'no_access_hosts': ["10.10.10.10"],
            'read_only_hosts': ["10.10.10.11"],
            'read_only_root_hosts': ["10.10.10.12"],
            'read_write_root_hosts': ["10.10.10.13"],
            'min_security': "KERBEROS",
            'anonymous_uid': 1000,
            'anonymous_gid': 1000,
            'is_no_suid': True,
            'host_state': "present-in-export",
            'state': "present"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.provisioning.get_nfs_export_details_by_name = MagicMock(
            return_value=None)
        nfs_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockNfsApi.FILESYSTEM_DETAILS_BY_NAME)
        nfs_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNfsApi.NAS_SERVER_DETAILS_2)
        nfs_module_mock.perform_module_operation()
        nfs_module_mock.provisioning.create_nfs_export.assert_called()

    def test_create_nfs_with_filesystem_exception_response(self, nfs_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'nfs_export_name': "sample_nfs_export",
            'filesystem': "sample_file_system",
            'nas_server': "Sample_nas_server_1",
            'state': "present"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.provisioning.get_nfs_export_details_by_name = MagicMock(
            return_value=None)
        nfs_module_mock.provisioning.get_filesystem_by_name = MagicMock(
            return_value=MockNfsApi.FILESYSTEM_DETAILS_BY_NAME)
        nfs_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNfsApi.NAS_SERVER_DETAILS_2)
        nfs_module_mock.provisioning.create_nfs_export = MagicMock(
            side_effect=MockApiException)
        nfs_module_mock.perform_module_operation()
        nfs_module_mock.provisioning.create_nfs_export.assert_called()

    def test_modify_nfs_response(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_name': "sample_nfs_export",
            'nas_server': "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
            'filesystem': "61d68815-1ac2-fc68-7263-96e8abdcbab0",
            'path': self.filesystem_path,
            'description': "This is new description",
            'default_access': "ROOT",
            'no_access_hosts': ["10.10.10.10"],
            'read_only_hosts': ["10.10.10.11"],
            'read_only_root_hosts': ["10.10.10.12"],
            'read_write_root_hosts': ["10.10.10.13"],
            'min_security': "KERBEROS",
            'anonymous_uid': 1000,
            'anonymous_gid': 1000,
            'is_no_suid': True,
            'host_state': "present-in-export",
            'state': "present"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.provisioning.get_nfs_export_details_by_name = MagicMock(
            return_value=MockNfsApi.NFS_DETAILS_BY_NAME)
        nfs_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockNfsApi.FILESYSTEM_DETAILS_BY_NAME[0])
        nfs_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNfsApi.NAS_SERVER_DETAILS)
        nfs_module_mock.perform_module_operation()
        nfs_module_mock.provisioning.modify_nfs_export.assert_called()

    def test_modify_nfs_add_ipv6_hosts_response(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_name': "sample_nfs_export",
            'nas_server': "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
            'filesystem': "61d68815-1ac2-fc68-7263-96e8abdcbab0",
            'path': self.filesystem_path,
            'default_access': "ROOT",
            'no_access_hosts': ["2620:0:170:2858:250:12aa:34aa:aaa3"],
            'read_only_hosts': ["2620:0:170:2858:250:12aa:34aa:aaa4"],
            'read_only_root_hosts': ["2620:0:170:2858:250:12aa:34aa:aaa5"],
            'read_write_root_hosts': ["2620:0:170:2858:250:12aa:34aa:aaa6"],
            'host_state': "present-in-export",
            'state': "present"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.provisioning.get_nfs_export_details_by_name = MagicMock(
            return_value=MockNfsApi.NFS_DETAILS_BY_NAME)
        nfs_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockNfsApi.FILESYSTEM_DETAILS_BY_NAME[0])
        nfs_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNfsApi.NAS_SERVER_DETAILS)
        nfs_module_mock.perform_module_operation()
        nfs_module_mock.provisioning.modify_nfs_export.assert_called()

    def test_modify_nfs_add_ipv6_hosts_exception(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_name': "sample_nfs_export",
            'nas_server': "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
            'filesystem': "61d68815-1ac2-fc68-7263-96e8abdcbab0",
            'path': self.filesystem_path,
            'default_access': "ROOT",
            'no_access_hosts': ["2620:0:170:2858:250:12aa:34aa:a(a3"],
            'host_state': "present-in-export",
            'state': "present"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.provisioning.get_nfs_export_details_by_name = MagicMock(
            return_value=MockNfsApi.NFS_DETAILS_BY_NAME)
        nfs_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockNfsApi.FILESYSTEM_DETAILS_BY_NAME[0])
        nfs_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNfsApi.NAS_SERVER_DETAILS)
        nfs_module_mock.perform_module_operation()
        assert MockNfsApi.add_invalid_ipv6_hosts_failed_msg() in \
            nfs_module_mock.module.fail_json.call_args[1]['msg']

    def test_remove_hosts_nfs_response(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_name': "sample_nfs_export_2",
            'nas_server': "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
            'no_access_hosts': ["10.10.10.10"],
            'read_only_hosts': ["10.10.10.11"],
            'read_only_root_hosts': ["10.10.10.12"],
            'read_write_root_hosts': ["10.10.10.13"],
            'host_state': "absent-in-export",
            'state': "present"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.provisioning.get_nfs_export_details_by_name = MagicMock(
            return_value=MockNfsApi.NFS_DETAILS_2)
        nfs_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockNfsApi.FILESYSTEM_DETAILS_BY_NAME[0])
        nfs_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNfsApi.NAS_SERVER_DETAILS)
        nfs_module_mock.perform_module_operation()
        nfs_module_mock.provisioning.modify_nfs_export.assert_called()

    def test_remove_hosts_wo_host_state_nfs_response(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_name': "sample_nfs_export_2",
            'nas_server': "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
            'no_access_hosts': ["10.10.10.10"],
            'read_only_hosts': ["10.10.10.11"],
            'read_only_root_hosts': ["10.10.10.12"],
            'read_write_root_hosts': ["10.10.10.13"],
            'state': "present"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.provisioning.get_nfs_export_details_by_name = MagicMock(
            return_value=MockNfsApi.NFS_DETAILS_2)
        nfs_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockNfsApi.FILESYSTEM_DETAILS_BY_NAME[0])
        nfs_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNfsApi.NAS_SERVER_DETAILS)
        nfs_module_mock.perform_module_operation()
        assert MockNfsApi.remove_nfs_export_hosts_without_host_state_failed_msg() in \
            nfs_module_mock.module.fail_json.call_args[1]['msg']

    def test_remove_hosts_wo_hosts_nfs_response(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_name': "sample_nfs_export_2",
            'nas_server': "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
            'host_state': "absent-in-export",
            'state': "present"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.provisioning.get_nfs_export_details_by_name = MagicMock(
            return_value=MockNfsApi.NFS_DETAILS_2)
        nfs_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockNfsApi.FILESYSTEM_DETAILS_BY_NAME[0])
        nfs_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNfsApi.NAS_SERVER_DETAILS)
        nfs_module_mock.perform_module_operation()
        assert MockNfsApi.remove_nfs_export_hosts_without_hosts_failed_msg() in \
            nfs_module_mock.module.fail_json.call_args[1]['msg']

    def test_remove_ipv6_hosts_nfs_response(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_name': "sample_nfs_export_3",
            'nas_server': "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
            'no_access_hosts': ["2620:0:170:2858:250:12aa:34aa:aaa3"],
            'read_only_hosts': ["2620:0:170:2858:250:12aa:34aa:aaa4"],
            'read_only_root_hosts': ["2620:0:170:2858:250:12aa:34aa:aaa5"],
            'read_write_root_hosts': ["2620:0:170:2858:250:12aa:34aa:aaa6"],
            'host_state': "absent-in-export",
            'state': "present"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.provisioning.get_nfs_export_details_by_name = MagicMock(
            return_value=MockNfsApi.NFS_DETAILS_3)
        nfs_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockNfsApi.FILESYSTEM_DETAILS_BY_NAME[0])
        nfs_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNfsApi.NAS_SERVER_DETAILS)
        nfs_module_mock.perform_module_operation()
        nfs_module_mock.provisioning.modify_nfs_export.assert_called()

    def test_remove_hosts_nfs_exception(self, nfs_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'nfs_export_name': "sample_nfs_export_2",
            'nas_server': "60c0564a-4a6e-04b6-4d5e-fe8be1eb93c9",
            'no_access_hosts': ["10.10.10.10"],
            'read_only_hosts': ["10.10.10.11"],
            'read_only_root_hosts': ["10.10.10.12"],
            'read_write_root_hosts': ["10.10.10.13"],
            'host_state': "absent-in-export",
            'state': "present"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.provisioning.get_nfs_export_details_by_name = MagicMock(
            return_value=MockNfsApi.NFS_DETAILS_2)
        nfs_module_mock.provisioning.get_filesystem_details = MagicMock(
            return_value=MockNfsApi.FILESYSTEM_DETAILS_BY_NAME[0])
        nfs_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNfsApi.NAS_SERVER_DETAILS)
        nfs_module_mock.provisioning.modify_nfs_export = MagicMock(
            side_effect=MockApiException)
        nfs_module_mock.perform_module_operation()
        nfs_module_mock.provisioning.modify_nfs_export.assert_called()

    def test_delete_nfs_export(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_name': "Sample_nas_server_1",
            'state': "absent"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.provisioning.get_nfs_export_details_by_name = MagicMock(
            return_value=MockNfsApi.NFS_DETAILS_BY_NAME)
        nfs_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNfsApi.NAS_SERVER_DETAILS)
        nfs_module_mock.perform_module_operation()
        nfs_module_mock.provisioning.delete_nfs_export.assert_called()

    def test_delete_nfs_export_exception(self, nfs_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'nfs_export_name': "Sample_nas_server_1",
            'state': "absent"
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.provisioning.get_nfs_export_details_by_name = MagicMock(
            return_value=MockNfsApi.NFS_DETAILS_BY_NAME)
        nfs_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNfsApi.NAS_SERVER_DETAILS)
        nfs_module_mock.provisioning.delete_nfs_export = MagicMock(
            side_effect=MockApiException)
        nfs_module_mock.perform_module_operation()
        nfs_module_mock.provisioning.delete_nfs_export.assert_called()
