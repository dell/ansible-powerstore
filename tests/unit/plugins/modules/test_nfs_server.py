# Copyright: (c) 2024, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)
"""Unit Tests for NFS server module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
# pylint: disable=unused-import

from ansible_collections.dellemc.powerstore.plugins.modules.nfs_server import \
    PowerStoreNFSServer
from ansible_collections.dellemc.powerstore.plugins.modules.nfs_server import \
    NFSServerHandler
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_nfs_server_api \
    import MockNFSServerApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception import \
    MockApiException
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries.powerstore_unit_base \
    import PowerStoreUnitBase


class TestPowerStoreNFSServer(PowerStoreUnitBase):

    get_module_args = MockNFSServerApi.NFS_SERVER_COMMON_ARGS
    nas_id = "6581683c-61a3-76ab-f107-62b767ad9845"

    @pytest.fixture
    def module_object(self):
        return PowerStoreNFSServer

    def test_get_nfs_server_response(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nfs_server_id': MockNFSServerApi.NFS_SERVER_DETAILS[0]['id'],
                'state': "present"}
        )
        NFSServerHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.nfs_server.get_nfs_server_details.assert_called()

    def test_get_nfs_server_nas_response(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nas_server': self.nas_id,
                'state': "present"
            })
        powerstore_module_mock.provisioning.get_nas_server_details = MagicMock(
            return_value=MockNFSServerApi.NAS_SERVER_DETAILS)
        powerstore_module_mock.nfs_server.get_nfs_server_by_nas_server_id = MagicMock(
            return_value=MockNFSServerApi.NFS_SERVER_DETAILS)
        NFSServerHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.nfs_server.get_nfs_server_by_nas_server_id.assert_called()

    def test_get_nfs_server_exception(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nfs_server_id': MockNFSServerApi.NFS_SERVER_DETAILS[0]['id'],
                'state': "present"
            })
        powerstore_module_mock.nfs_server.get_nfs_server_details = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockNFSServerApi.get_nfs_server_exception_response(
                'get_nfs_server_exception'), powerstore_module_mock, NFSServerHandler)

    def test_create_nfs_server_response(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nas_server': "sample_nas_server",
                'host_name': "sample_host",
                'credentials_cache_TTL': 60,
                'is_extended_credentials_enabled': False,
                'is_nfsv3_enabled': True,
                'is_nfsv4_enabled': True,
                'is_secure_enabled': False,
                'state': "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.nfs_server.get_nfs_server_details_by_nas_server_id = MagicMock(
            return_value=None)
        NFSServerHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.nfs_server.create_nfs_server.assert_called()

    def test_create_nfs_server_wo_nas_server_exception(self, powerstore_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'host_name': "sample_host",
                'credentials_cache_TTL': 60,
                'is_extended_credentials_enabled': False,
                'is_nfsv3_enabled': True,
                'is_nfsv4_enabled': True,
                'is_secure_enabled': False,
                'state': "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.configuration.get_nfs_server_details_by_nas_server_id = MagicMock(
            return_value=None)
        self.capture_fail_json_call(
            MockNFSServerApi.get_nfs_server_exception_response(
                'create_nfs_server_wo_nas_server_exception'), powerstore_module_mock, NFSServerHandler)

    def test_create_nfs_server_exception(self, powerstore_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nas_server': "sample_nas_server",
                'host_name': "sample_host",
                'credentials_cache_TTL': 60,
                'is_extended_credentials_enabled': False,
                'is_nfsv3_enabled': True,
                'is_nfsv4_enabled': True,
                'is_secure_enabled': False,
                'state': "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.configuration.get_nfs_server_details_by_nas_server_id = MagicMock(
            return_value=None)
        powerstore_module_mock.nfs_server.create_nfs_server = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockNFSServerApi.get_nfs_server_exception_response(
                'create_nfs_server_exception'), powerstore_module_mock, NFSServerHandler)

    def test_modify_nfs_server(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nfs_server_id': MockNFSServerApi.NFS_SERVER_DETAILS[0]['id'],
                'credentials_cache_TTL': 60,
                'is_extended_credentials_enabled': False,
                'is_nfsv3_enabled': False,
                'is_skip_unjoin': True,
                'state': "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.nfs_server.get_nfs_server_details = MagicMock(
            return_value=MockNFSServerApi.NFS_SERVER_DETAILS[0])
        NFSServerHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.nfs_server.modify_nfs_server.assert_called()

    def test_modify_nfs_server_exception(self, powerstore_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nfs_server_id': MockNFSServerApi.NFS_SERVER_DETAILS[0]['id'],
                'credentials_cache_TTL': 60,
                'is_extended_credentials_enabled': False,
                'is_nfsv3_enabled': False,
                'is_skip_unjoin': True,
                'state': "present"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.nfs_server.get_nfs_server_details = MagicMock(
            return_value=MockNFSServerApi.NFS_SERVER_DETAILS[0])
        powerstore_module_mock.nfs_server.modify_nfs_server = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockNFSServerApi.get_nfs_server_exception_response(
                'modify_nfs_server_exception'), powerstore_module_mock, NFSServerHandler)

    def test_delete_nfs_server(self, powerstore_module_mock):
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nfs_server_id': MockNFSServerApi.NFS_SERVER_DETAILS[0]['id'],
                'state': "absent"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.nfs_server.get_nfs_server_details = MagicMock(
            return_value=MockNFSServerApi.NFS_SERVER_DETAILS[0])
        NFSServerHandler().handle(powerstore_module_mock, powerstore_module_mock.module.params)
        powerstore_module_mock.nfs_server.delete_nfs_server.assert_called()

    def test_delete_nfs_server_exception(self, powerstore_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.set_module_params(
            powerstore_module_mock,
            self.get_module_args,
            {
                'nfs_server_id': MockNFSServerApi.NFS_SERVER_DETAILS[0]['id'],
                'state': "absent"
            })
        powerstore_module_mock.module.params = self.get_module_args
        powerstore_module_mock.nfs_server.get_nfs_server_details = MagicMock(
            return_value=MockNFSServerApi.NFS_SERVER_DETAILS[0])
        powerstore_module_mock.nfs_server.delete_nfs_server = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockNFSServerApi.get_nfs_server_exception_response(
                'delete_nfs_server_exception'), powerstore_module_mock, NFSServerHandler)
