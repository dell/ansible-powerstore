# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Volume Group module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_volumegroup_api import MockVolumeGroupApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKResponse
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_powerstore_connection = MagicMock()
utils.PowerStoreException = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerstore.plugins.modules.volumegroup import PowerStoreVolumeGroup


class TestPowerstoreVolumeGroup():

    get_module_args = MockVolumeGroupApi.VOLUME_GROUP_COMMON_ARGS

    @pytest.fixture
    def volume_group_module_mock(self, mocker):
        mocker.patch(MockVolumeGroupApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        volume_group_module_mock = PowerStoreVolumeGroup()
        volume_group_module_mock.module = MagicMock()
        return volume_group_module_mock

    def test_get_volume_group_by_id(self, volume_group_module_mock):
        self.get_module_args.update({
            'vg_id': "634e4b95-e7bd-49e7-957b-6dc932642464",
            'state': "present"
        })
        volume_group_module_mock.module.params = self.get_module_args
        volume_group_module_mock.provisioning.get_volume_group_details = MagicMock(
            return_value=MockVolumeGroupApi.VG_DETAILS[0])
        volume_group_module_mock.perform_module_operation()
        assert self.get_module_args['vg_id'] == volume_group_module_mock.module.exit_json.call_args[1]['volume_group_details']['id']

    def test_get_volume_group_by_name(self, volume_group_module_mock):
        self.get_module_args.update({
            'vg_name': "sample_volume_group",
            'state': "present"
        })
        volume_group_module_mock.module.params = self.get_module_args
        volume_group_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            return_value=MockVolumeGroupApi.VG_DETAILS)
        volume_group_module_mock.provisioning.get_volume_group_details = MagicMock(
            return_value=MockVolumeGroupApi.VG_DETAILS[0])
        volume_group_module_mock.perform_module_operation()
        assert self.get_module_args['vg_name'] == volume_group_module_mock.module.exit_json.call_args[1]['volume_group_details']['name']
        volume_group_module_mock.provisioning.get_volume_group_by_name.assert_called()

    def test_create_volume_group(self, volume_group_module_mock):
        self.get_module_args.update({
            'vg_name': "sample_volume_group_1",
            'description': MockVolumeGroupApi.DESCRIPTION1,
            'protection_policy': 'sample_protection_policy',
            'is_write_order_consistent': True,
            'state': "present"
        })
        volume_group_module_mock.module.params = self.get_module_args
        volume_group_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            return_value=None)
        volume_group_module_mock.protection.get_protection_policy_by_name = MagicMock(
            return_value=MockVolumeGroupApi.PROTECTION_POLICY_DETAILS[0])
        volume_group_module_mock.provisioning.create_volume_group = MagicMock(
            return_value=MockVolumeGroupApi.CREATE_VG[0])
        volume_group_module_mock.provisioning.get_volume_group_details = MagicMock(
            return_value=MockVolumeGroupApi.CREATE_VG[0])
        volume_group_module_mock.perform_module_operation()
        assert volume_group_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_group_module_mock.provisioning.create_volume_group.assert_called()

    def test_create_volume_group_with_pp_id(self, volume_group_module_mock):
        self.get_module_args.update({
            'vg_name': "sample_volume_group",
            'description': MockVolumeGroupApi.DESCRIPTION1,
            'protection_policy': '4bbb6333-59e4-489c-9015-c618d3e8384b',
            'is_write_order_consistent': False,
            'state': "present"
        })
        volume_group_module_mock.module.params = self.get_module_args
        volume_group_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            return_value=None)
        volume_group_module_mock.protection.get_protection_policy_details = MagicMock(
            return_value=MockVolumeGroupApi.PROTECTION_POLICY_DETAILS[0])
        volume_group_module_mock.provisioning.create_volume_group = MagicMock(
            return_value=MockVolumeGroupApi.VG_DETAILS[0])
        volume_group_module_mock.provisioning.get_volume_group_details = MagicMock(
            return_value=MockVolumeGroupApi.VG_DETAILS[0])
        volume_group_module_mock.perform_module_operation()
        assert volume_group_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_group_module_mock.provisioning.create_volume_group.assert_called()

    def test_modify_volume_group(self, volume_group_module_mock):
        self.get_module_args.update({
            'vg_name': "sample_volume_group_1",
            'description': MockVolumeGroupApi.DESCRIPTION1,
            'new_vg_name': 'sample_volume_group',
            'protection_policy': '',
            'is_write_order_consistent': False,
            'state': "present"
        })
        volume_group_module_mock.module.params = self.get_module_args
        volume_group_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            return_value=MockVolumeGroupApi.CREATE_VG)
        volume_group_module_mock.provisioning.modify_volume_group = MagicMock(
            return_value=MockVolumeGroupApi.MODIFY_VG[0])
        volume_group_module_mock.perform_module_operation()
        assert volume_group_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_group_module_mock.provisioning.modify_volume_group.assert_called()

    def test_delete_volume_group(self, volume_group_module_mock):
        self.get_module_args.update({
            'vg_id': "634e4b95-e7bd-49e7-957b-6dc932642464",
            'state': "absent"
        })
        volume_group_module_mock.module.params = self.get_module_args
        volume_group_module_mock.provisioning.get_volume_group_details = MagicMock(
            return_value=MockVolumeGroupApi.CREATE_VG[0])
        volume_group_module_mock.perform_module_operation()
        assert volume_group_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_group_module_mock.provisioning.delete_volume_group.assert_called()

    def test_delete_volume_group_with_exception(self, volume_group_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vg_id': "634e4b95-e7bd-49e7-957b-6dc932642464",
            'state': "absent"
        })
        volume_group_module_mock.module.params = self.get_module_args
        volume_group_module_mock.provisioning.get_volume_group_details = MagicMock(
            return_value=MockVolumeGroupApi.CREATE_VG[0])
        volume_group_module_mock.provisioning.delete_volume_group = MagicMock(
            side_effect=MockApiException)
        volume_group_module_mock.perform_module_operation()
        volume_group_module_mock.provisioning.delete_volume_group.assert_called()

    def test_modify_volume_group_with_exception(self, volume_group_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vg_id': "634e4b95-e7bd-49e7-957b-6dc932642464",
            'is_write_order_consistent': False,
            'state': "present"
        })
        volume_group_module_mock.module.params = self.get_module_args
        volume_group_module_mock.provisioning.get_volume_group_details = MagicMock(
            return_value=MockVolumeGroupApi.CREATE_VG[0])
        volume_group_module_mock.provisioning.modify_volume_group = MagicMock(
            side_effect=MockApiException)
        volume_group_module_mock.perform_module_operation()
        volume_group_module_mock.provisioning.modify_volume_group.assert_called()

    def test_add_volume_to_volume_group(self, volume_group_module_mock):
        self.get_module_args.update({
            'vg_name': "sample_volume_group",
            'description': MockVolumeGroupApi.DESCRIPTION2,
            'volumes': ['sample_volume_1', '6b730a66-494a-4aea-88d2-45552bb4adfc'],
            'vol_state': 'present-in-group',
            'state': "present"
        })
        volume_group_module_mock.module.params = self.get_module_args
        volume_group_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            return_value=MockVolumeGroupApi.VG_DETAILS)
        volume_group_module_mock.get_volume_group_details = MagicMock(
            return_value=MockVolumeGroupApi.VG_DETAILS[0])
        volume_group_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeGroupApi.VOL_DETAILS1[0])
        volume_group_module_mock.provisioning.get_volume_details = MagicMock(
            return_value=MockVolumeGroupApi.VOL_DETAILS2[0])
        volume_group_module_mock.provisioning.add_members_to_volume_group = MagicMock(
            return_value=MockVolumeGroupApi.MODIFY_VG[0])
        volume_group_module_mock.perform_module_operation()
        assert volume_group_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_group_module_mock.provisioning.add_members_to_volume_group.assert_called()

    def test_remove_volume_from_volume_group(self, volume_group_module_mock):
        self.get_module_args.update({
            'vg_name': "sample_volume_group",
            'volumes': ['sample_volume_1', '6b730a66-494a-4aea-88d2-45552bb4adfc'],
            'vol_state': 'absent-in-group',
            'state': "present"
        })
        volume_group_module_mock.module.params = self.get_module_args
        volume_group_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            return_value=MockVolumeGroupApi.MODIFY_VG)
        volume_group_module_mock.get_volume_group_details = MagicMock(
            return_value=MockVolumeGroupApi.MODIFY_VG[0])
        volume_group_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeGroupApi.VOL_DETAILS1[0])
        volume_group_module_mock.provisioning.get_volume_details = MagicMock(
            return_value=MockVolumeGroupApi.VOL_DETAILS2[0])
        volume_group_module_mock.provisioning.remove_members_from_volume_group = MagicMock(
            return_value=MockVolumeGroupApi.VG_DETAILS[0])
        volume_group_module_mock.perform_module_operation()
        assert volume_group_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_group_module_mock.provisioning.remove_members_from_volume_group.assert_called()

    def test_remove_volume_from_volume_group_with_exception(self, volume_group_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vg_name': "sample_volume_group",
            'volumes': ['sample_volume_1', '6b730a66-494a-4aea-88d2-45552bb4adfc'],
            'vol_state': 'absent-in-group',
            'state': "present"
        })
        volume_group_module_mock.module.params = self.get_module_args
        volume_group_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            return_value=MockVolumeGroupApi.MODIFY_VG)
        volume_group_module_mock.get_volume_group_details = MagicMock(
            return_value=MockVolumeGroupApi.MODIFY_VG[0])
        volume_group_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeGroupApi.VOL_DETAILS1[0])
        volume_group_module_mock.provisioning.get_volume_details = MagicMock(
            return_value=MockVolumeGroupApi.VOL_DETAILS2[0])
        volume_group_module_mock.provisioning.remove_members_from_volume_group = MagicMock(
            side_effect=MockApiException)
        volume_group_module_mock.perform_module_operation()
        volume_group_module_mock.provisioning.remove_members_from_volume_group.assert_called()

    def test_add_volume_to_volume_group_with_exception(self, volume_group_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vg_name': "sample_volume_group",
            'description': MockVolumeGroupApi.DESCRIPTION2,
            'volumes': ['sample_volume_1', '6b730a66-494a-4aea-88d2-45552bb4adfc'],
            'vol_state': 'present-in-group',
            'state': "present"
        })
        volume_group_module_mock.module.params = self.get_module_args
        volume_group_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            return_value=MockVolumeGroupApi.VG_DETAILS)
        volume_group_module_mock.get_volume_group_details = MagicMock(
            return_value=MockVolumeGroupApi.VG_DETAILS[0])
        volume_group_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeGroupApi.VOL_DETAILS1[0])
        volume_group_module_mock.provisioning.get_volume_details = MagicMock(
            return_value=MockVolumeGroupApi.VOL_DETAILS2[0])
        volume_group_module_mock.provisioning.add_members_to_volume_group = MagicMock(
            side_effect=MockApiException)
        volume_group_module_mock.perform_module_operation()
        volume_group_module_mock.provisioning.add_members_to_volume_group.assert_called()

    def test_get_volume_group_with_exception(self, volume_group_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vg_id': "634e4b95-e7bd-49e7-957b-6dc932642464",
            'state': "absent"
        })
        volume_group_module_mock.module.params = self.get_module_args
        volume_group_module_mock.provisioning.get_volume_group_details = MagicMock(
            side_effect=MockApiException)
        volume_group_module_mock.perform_module_operation()
        volume_group_module_mock.provisioning.get_volume_group_details.assert_called()

    def test_get_volume_id_to_remove_volume_group_with_exception(self, volume_group_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vg_name': "sample_volume_group",
            'volumes': ['6b730a66-494a-4aea-88d2-45552bb4adfc'],
            'vol_state': 'absent-in-group',
            'state': "present"
        })
        volume_group_module_mock.module.params = self.get_module_args
        volume_group_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            return_value=MockVolumeGroupApi.MODIFY_VG)
        volume_group_module_mock.get_volume_group_details = MagicMock(
            return_value=MockVolumeGroupApi.MODIFY_VG[0])
        volume_group_module_mock.provisioning.get_volume_details = MagicMock(
            side_effect=MockApiException)
        volume_group_module_mock.perform_module_operation()
        volume_group_module_mock.provisioning.get_volume_details.assert_called()

    def test_get_non_existing_volume_to_remove_volume_group_with_exception(self, volume_group_module_mock):
        self.get_module_args.update({
            'vg_name': "sample_volume_group",
            'volumes': ['6b730a66-494a-4aea-88d2-45552bb4adfc'],
            'vol_state': 'absent-in-group',
            'state': "present"
        })
        volume_group_module_mock.module.params = self.get_module_args
        volume_group_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            return_value=MockVolumeGroupApi.MODIFY_VG)
        volume_group_module_mock.get_volume_group_details = MagicMock(
            return_value=MockVolumeGroupApi.MODIFY_VG[0])
        volume_group_module_mock.provisioning.get_volume_details = MagicMock(
            side_effect=MockApiException)
        volume_group_module_mock.perform_module_operation()
        assert MockVolumeGroupApi.get_non_existing_volume_failed_msg() in \
               volume_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_non_existing_volume_to_add_volume_group(self, volume_group_module_mock):
        self.get_module_args.update({
            'vg_name': "sample_volume_group",
            'description': MockVolumeGroupApi.DESCRIPTION2,
            'volumes': ['6b730a66-494a-4aea-88d2-45552bb4adfc'],
            'vol_state': 'present-in-group',
            'state': "present"
        })
        volume_group_module_mock.module.params = self.get_module_args
        volume_group_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            return_value=MockVolumeGroupApi.VG_DETAILS)
        volume_group_module_mock.get_volume_group_details = MagicMock(
            return_value=MockVolumeGroupApi.VG_DETAILS[0])
        volume_group_module_mock.provisioning.get_volume_details = MagicMock(
            side_effect=MockApiException)
        volume_group_module_mock.perform_module_operation()
        assert MockVolumeGroupApi.get_non_existing_volume_failed_msg() in \
               volume_group_module_mock.module.fail_json.call_args[1]['msg']
