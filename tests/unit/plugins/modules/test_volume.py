# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Volume module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_volume_api import MockVolumeApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.volume import PowerStoreVolume


class TestPowerstoreVolume():

    get_module_args = MockVolumeApi.VOLUME_COMMON_ARGS

    @pytest.fixture
    def volume_module_mock(self, mocker):
        mocker.patch(MockVolumeApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        volume_module_mock = PowerStoreVolume()
        volume_module_mock.module = MagicMock()
        return volume_module_mock

    def test_get_volume_by_id(self, volume_module_mock):
        self.get_module_args.update({
            'vol_id': "ae20eb9a-a482-416e-aaf7-2a3fe7203630",
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_volume_details = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1[0])
        volume_module_mock.perform_module_operation()
        assert self.get_module_args['vol_id'] == volume_module_mock.module.exit_json.call_args[1]['volume_details']['id']

    def test_get_volume_by_name(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1)
        volume_module_mock.provisioning.get_volume_details = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1[0])
        volume_module_mock.perform_module_operation()
        assert self.get_module_args['vol_name'] == volume_module_mock.module.exit_json.call_args[1]['volume_details']['name']
        volume_module_mock.provisioning.get_volume_by_name.assert_called()

    def test_get_volume_details_by_name_more_than_one_vol(self, volume_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'vol_name': "sample_volume",
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.TWO_VOL_LIST)
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.get_volume_more_than_one_failed_msg() in \
               volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_volume_with_exception(self, volume_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'vol_name': 'sample_volume_1',
            'state': 'present'
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            side_effect=MockApiException)
        volume_module_mock.perform_module_operation()
        volume_module_mock.provisioning.get_volume_by_name.assert_called()

    def test_create_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': 'sample_volume_1',
            'description': MockVolumeApi.DESCRIPTION1,
            'size': 1,
            'cap_unit': 'GB',
            'performance_policy': 'medium',
            'vg_name': 'sample_VG',
            'protection_policy': 'sample_protection_policy',
            'state': 'present',
            'app_type': 'Relational_Databases_Other',
            'app_type_other': 'Max_DB',
            'appliance_id': 'A1'
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=None)
        volume_module_mock.provisioning.get_volume_group_by_name = MagicMock(
            return_value=MockVolumeApi.VG_1[0])
        volume_module_mock.conn.protection.get_protection_policy_by_name = MagicMock(
            return_value=MockVolumeApi.PROTECTION_POLICY_DETAILS[0])
        volume_module_mock.provisioning.create_volume = MagicMock(
            return_value=True)
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1[0])
        volume_module_mock.provisioning.get_volume_details = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1[0])
        volume_module_mock.perform_module_operation()
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_module_mock.provisioning.create_volume.assert_called()

    def test_create_volume_with_pp_id(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': 'sample_volume_1',
            'description': MockVolumeApi.DESCRIPTION1,
            'size': 1,
            'vg_id': 'fd156da5-d579-43b2-a377-e98af0c6962f',
            'performance_policy': 'medium',
            'protection_policy': '4bbb6333-59e4-489c-9015-c618d3e8384b',
            'state': 'present'
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=None)
        volume_module_mock.provisioning.get_volume_group_details = MagicMock(
            return_value=MockVolumeApi.VG_1[0])
        volume_module_mock.conn.protection.get_protection_policy_details = MagicMock(
            return_value=MockVolumeApi.PROTECTION_POLICY_DETAILS[0])
        volume_module_mock.provisioning.create_volume = MagicMock(
            return_value=True)
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1[0])
        volume_module_mock.provisioning.get_volume_details = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1[0])
        volume_module_mock.perform_module_operation()
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_module_mock.provisioning.create_volume.assert_called()

    def test_create_volume_without_size(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': 'sample_volume_1',
            'description': MockVolumeApi.DESCRIPTION1,
            'performance_policy': 'medium',
            'protection_policy': '4bbb6333-59e4-489c-9015-c618d3e8384b',
            'state': 'present'
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=None)
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.create_volume_without_size_failed_msg() in \
               volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_volume_with_new_name(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': 'sample_volume_1',
            'description': MockVolumeApi.DESCRIPTION1,
            'performance_policy': 'medium',
            'new_name': 'new_vol',
            'size': 1,
            'protection_policy': '4bbb6333-59e4-489c-9015-c618d3e8384b',
            'state': 'present'
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=None)
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.create_volume_with_new_name_failed_msg() in \
               volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'description': 'Volume 2 created',
            'new_vol_name': 'sample_volume_2',
            'protection_policy': '',
            'size': 2,
            'performance_policy': 'high',
            'state': "present",
            'app_type': 'Business_Applications_CRM'
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1)
        volume_module_mock.provisioning.modify_volume = MagicMock(
            return_value=True)
        volume_module_mock.provisioning.get_volume_details = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS2[0])
        volume_module_mock.perform_module_operation()
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_module_mock.provisioning.modify_volume.assert_called()

    def test_delete_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_id': "6b730a66-494a-4aea-88d2-45552bb4adfc",
            'state': "absent"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_volume_details = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS2[0])
        volume_module_mock.perform_module_operation()
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_module_mock.provisioning.delete_volume.assert_called()

    def test_delete_volume_with_exception(self, volume_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vol_id': "6b730a66-494a-4aea-88d2-45552bb4adfc",
            'state': "absent"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_volume_details = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS2[0])
        volume_module_mock.provisioning.delete_volume = MagicMock(
            side_effect=MockApiException)
        volume_module_mock.perform_module_operation()
        volume_module_mock.provisioning.delete_volume.assert_called()

    def test_modify_volume_with_exception(self, volume_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'cap_unit': 'TB',
            'size': 2,
            'performance_policy': 'high',
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1)
        volume_module_mock.provisioning.modify_volume = MagicMock(
            side_effect=MockApiException)
        volume_module_mock.perform_module_operation()
        volume_module_mock.provisioning.modify_volume.assert_called()

    def test_map_host_to_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'host': 'sample_host',
            'mapping_state': 'mapped',
            'hlu': 123,
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_host_by_name = MagicMock(
            return_value=MockVolumeApi.HOST_DETAILS1)
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1)
        volume_module_mock.provisioning.map_volume_to_host = MagicMock(
            return_value=[])
        volume_module_mock.perform_module_operation()
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_module_mock.provisioning.map_volume_to_host.assert_called()

    def test_unmap_host_from_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'host': 'ced80318-b14a-461d-93a7-11b10afaf349',
            'mapping_state': 'unmapped',
            'hlu': 123,
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_host_details = MagicMock(
            return_value=MockVolumeApi.HOST_DETAILS1[0])
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.MODIFY_VOL_DETAILS1)
        volume_module_mock.provisioning.unmap_volume_from_host = MagicMock(
            return_value=[])
        volume_module_mock.perform_module_operation()
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_module_mock.provisioning.unmap_volume_from_host.assert_called()

    def test_map_host_group_to_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'hostgroup': 'sample_host_group',
            'mapping_state': 'mapped',
            'hlu': 123,
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_host_group_by_name = MagicMock(
            return_value=MockVolumeApi.HG_DETAILS1)
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1)
        volume_module_mock.provisioning.map_volume_to_host_group = MagicMock(
            return_value=[])
        volume_module_mock.perform_module_operation()
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_module_mock.provisioning.map_volume_to_host_group.assert_called()

    def test_unmap_host_group_from_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_id': "ae20eb9a-a482-416e-aaf7-2a3fe7203630",
            'hostgroup': "sample_host_group_2",
            'mapping_state': 'unmapped',
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_host_group_by_name = MagicMock(
            return_value=MockVolumeApi.HG_DETAILS2)
        volume_module_mock.provisioning.get_volume_details = MagicMock(
            return_value=MockVolumeApi.MODIFY_VOL_DETAILS1[0])
        volume_module_mock.perform_module_operation()
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_module_mock.provisioning.unmap_volume_from_host_group.assert_called()

    def test_map_host_to_volume_with_exception(self, volume_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'host': 'sample_host',
            'mapping_state': 'mapped',
            'hlu': 123,
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_host_by_name = MagicMock(
            return_value=MockVolumeApi.HOST_DETAILS1)
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1)
        volume_module_mock.provisioning.map_volume_to_host = MagicMock(
            side_effect=MockApiException)
        volume_module_mock.perform_module_operation()
        volume_module_mock.provisioning.map_volume_to_host.assert_called()

    def test_unmap_host_from_volume_with_exception(self, volume_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'host': 'ced80318-b14a-461d-93a7-11b10afaf349',
            'mapping_state': 'unmapped',
            'hlu': 123,
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_host_details = MagicMock(
            return_value=MockVolumeApi.HOST_DETAILS1[0])
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.MODIFY_VOL_DETAILS1)
        volume_module_mock.provisioning.unmap_volume_from_host = MagicMock(
            side_effect=MockApiException)
        volume_module_mock.perform_module_operation()
        volume_module_mock.provisioning.unmap_volume_from_host.assert_called()

    def test_map_host_group_to_volume_with_exception(self, volume_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'hostgroup': 'sample_host_group',
            'mapping_state': 'mapped',
            'hlu': 123,
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_host_group_by_name = MagicMock(
            return_value=MockVolumeApi.HG_DETAILS1)
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1)
        volume_module_mock.provisioning.map_volume_to_host_group = MagicMock(
            side_effect=MockApiException)
        volume_module_mock.perform_module_operation()
        volume_module_mock.provisioning.map_volume_to_host_group.assert_called()

    def test_unmap_host_group_from_volume_with_exception(self, volume_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vol_id': "ae20eb9a-a482-416e-aaf7-2a3fe7203630",
            'hostgroup': "sample_host_group_2",
            'mapping_state': 'unmapped',
            'hlu': 123,
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_host_group_by_name = MagicMock(
            return_value=MockVolumeApi.HG_DETAILS2)
        volume_module_mock.provisioning.get_volume_details = MagicMock(
            return_value=MockVolumeApi.MODIFY_VOL_DETAILS1[0])
        volume_module_mock.provisioning.unmap_volume_from_host_group = MagicMock(
            side_effect=MockApiException)
        volume_module_mock.perform_module_operation()
        volume_module_mock.provisioning.unmap_volume_from_host_group.assert_called()

    def test_create_volume_with_pp_id_with_exception(self, volume_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vol_name': 'sample_volume_1',
            'description': MockVolumeApi.DESCRIPTION1,
            'size': 1,
            'vg_id': 'fd156da5-d579-43b2-a377-e98af0c6962f',
            'performance_policy': 'medium',
            'protection_policy': '4bbb6333-59e4-489c-9015-c618d3e8384b',
            'state': 'present'
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=None)
        volume_module_mock.provisioning.get_volume_group_details = MagicMock(
            return_value=MockVolumeApi.VG_1[0])
        volume_module_mock.conn.protection.get_protection_policy_details = MagicMock(
            return_value=MockVolumeApi.PROTECTION_POLICY_DETAILS[0])
        volume_module_mock.provisioning.create_volume = MagicMock(
            side_effect=MockApiException)
        volume_module_mock.perform_module_operation()
        volume_module_mock.provisioning.create_volume.assert_called()

    def test_map_host_and_hg_to_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'host': 'sample_host',
            'hostgroup': 'sample_host_group',
            'mapping_state': 'mapped',
            'hlu': 123,
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_host_by_name = MagicMock(
            return_value=MockVolumeApi.HOST_DETAILS1)
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1)
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.add_host_and_hg_volume_failed_msg() in \
               volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_hlu_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'host': 'sample_host',
            'mapping_state': 'mapped',
            'hlu': 1213,
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_host_by_name = MagicMock(
            return_value=MockVolumeApi.HOST_DETAILS1)
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.MODIFY_VOL_DETAILS1)
        volume_module_mock.check_for_hlu_modification = MagicMock(
            return_value=(False, 'Modification of HLU from'))
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.modify_hlu_volume_failed_msg() in \
               volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_shrink_of_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': 'sample_volume_2',
            'size': 1,
            'state': 'present'
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS2)
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.shrink_volume_failed_msg() in \
               volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_host_to_map_volume_exception(self, volume_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'host': 'sample_host',
            'mapping_state': 'mapped',
            'hlu': 123,
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_host_by_name = MagicMock(
            side_effect=MockApiException)
        volume_module_mock.perform_module_operation()
        volume_module_mock.provisioning.get_host_by_name.assert_called()

    def test_get_host_group_to_map_volume_with_exception(self, volume_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'hostgroup': 'sample_host_group',
            'mapping_state': 'mapped',
            'hlu': 123,
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_host_group_by_name = MagicMock(
            side_effect=MockApiException)
        volume_module_mock.perform_module_operation()
        volume_module_mock.provisioning.get_host_group_by_name.assert_called()

    def test_map_host_to_volume_without_mapping_state(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'host': 'sample_host',
            'hlu': 123,
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_host_by_name = MagicMock(
            return_value=MockVolumeApi.HOST_DETAILS1)
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1)
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.map_without_mapping_state_failed_msg() in \
               volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_map_existing_host_group_to_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'hostgroup': 'sample_host_group2',
            'mapping_state': 'mapped',
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_host_group_by_name = MagicMock(
            return_value=MockVolumeApi.HG_DETAILS2)
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.MODIFY_VOL_DETAILS1)
        volume_module_mock.perform_module_operation()
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_map_existing_host_to_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'host': 'sample_host',
            'mapping_state': 'mapped',
            'hlu': 123,
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_host_by_name = MagicMock(
            return_value=MockVolumeApi.HOST_DETAILS1)
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.MODIFY_VOL_DETAILS1)
        volume_module_mock.perform_module_operation()
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_unmap_non_existing_host_from_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'host': 'ced80318-b14a-461d-93a7-11b10afaf349',
            'mapping_state': 'unmapped',
            'hlu': 123,
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_host_details = MagicMock(
            return_value=MockVolumeApi.HOST_DETAILS1[0])
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1)
        volume_module_mock.perform_module_operation()
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_unmap_non_existing_host_group_from_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_id': "ae20eb9a-a482-416e-aaf7-2a3fe7203630",
            'hostgroup': 'd0a61806-0992-4e8b-9419-d47ac1ed563f',
            'mapping_state': 'unmapped',
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_host_group_details = MagicMock(
            return_value=MockVolumeApi.HG_DETAILS1[0])
        volume_module_mock.provisioning.get_volume_details = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1[0])
        volume_module_mock.perform_module_operation()
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is False

    def perform_operation(self, volume_module_mock):
        volume_module_mock.provisioning.get_volume_details = MagicMock(return_value=MockVolumeApi.VOL_DETAILS1[0])
        volume_module_mock.perform_module_operation()

    def operation_before_clone_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'clone_volume': {
                'name': 'test_name_3',
                'description': 'test description 1',
                'host': 'hst_nm_1',
                'host_group': "sample_host_group_2",
                'logical_unit_number': 13,
                'protection_policy': 'PP1',
                'performance_policy': 'low'
            },
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(return_value=MockVolumeApi.VOL_DETAILS1)
        volume_module_mock.get_volume = MagicMock(side_effect=[MockVolumeApi.VOL_DETAILS1[0], None, MockVolumeApi.VOL_DETAILS1[0]])
        volume_module_mock.get_performance_policy = MagicMock(return_value=MockVolumeApi.PERFORMANCE_POLICY_LOW)
        volume_module_mock.get_protection_policy_id_by_name = MagicMock(return_value='PP_ID_1')
        volume_module_mock.get_host_id_by_name = MagicMock(return_value='HD_ID_1')
        volume_module_mock.provisioning.get_host_group_details = MagicMock(return_value=MockVolumeApi.HG_DETAILS2)

    def test_clone_volume(self, volume_module_mock):
        self.operation_before_clone_volume(volume_module_mock)
        volume_module_mock.provisioning.clone_volume = MagicMock(return_value='vol_id_3')
        self.perform_operation(volume_module_mock)
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_module_mock.provisioning.clone_volume.assert_called()

    def test_clone_volume_log_unit_error(self, volume_module_mock):
        self.operation_before_clone_volume(volume_module_mock)
        self.get_module_args['clone_volume']['host'] = None
        self.get_module_args['clone_volume']['host_group'] = None
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.clone_volume = MagicMock(return_value='vol_id_3')
        self.perform_operation(volume_module_mock)
        assert volume_module_mock.module.fail_json.call_args[1]['msg'] == MockVolumeApi.get_fail_msg_for_clone_volume('log_unit_error')

    def test_clone_volume_exception(self, volume_module_mock):
        self.operation_before_clone_volume(volume_module_mock)
        volume_module_mock.provisioning.clone_volume = MagicMock(side_effect=MockApiException)
        self.perform_operation(volume_module_mock)
        assert volume_module_mock.module.fail_json.call_args[1]['msg'] == MockVolumeApi.get_fail_msg_for_clone_volume('exception')

    def operation_before_refresh_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'source_volume': 'test_name_1',
            'create_backup_snap': True,
            'backup_snap_profile': {
                'name': 'refresh_backup_snap_2',
                'description': 'test refresh_backup_snap',
                'expiration_timestamp': MockVolumeApi.EXPIRATION_TIMESTAMP,
                'performance_policy': 'low'
            },
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(return_value=MockVolumeApi.VOL_DETAILS1)
        volume_module_mock.provisioning.get_volumes = MagicMock(return_value=MockVolumeApi.VOL1_SNAPSHOT_LIST)
        volume_module_mock.get_volume = MagicMock(return_value=MockVolumeApi.VOL_DETAILS1[0])
        volume_module_mock.get_performance_policy = MagicMock(return_value=MockVolumeApi.PERFORMANCE_POLICY_LOW)

    def test_refresh_volume(self, volume_module_mock):
        self.operation_before_refresh_volume(volume_module_mock)
        volume_module_mock.provisioning.refresh_volume = MagicMock(return_value='snap_id_3')
        self.perform_operation(volume_module_mock)
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_module_mock.provisioning.refresh_volume.assert_called()

    def test_refresh_volume_exception(self, volume_module_mock):
        self.operation_before_refresh_volume(volume_module_mock)
        volume_module_mock.provisioning.refresh_volume = MagicMock(side_effect=MockApiException)
        self.perform_operation(volume_module_mock)
        assert volume_module_mock.module.fail_json.call_args[1]['msg'] == MockVolumeApi.get_fail_msg_for_refresh_volume('exception')

    def test_refresh_volume_backup_snap_error(self, volume_module_mock):
        self.operation_before_refresh_volume(volume_module_mock)
        self.get_module_args['create_backup_snap'] = None
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.refresh_volume = MagicMock(return_value='snap_id_3')
        self.perform_operation(volume_module_mock)
        assert volume_module_mock.module.fail_json.call_args[1]['msg'] == MockVolumeApi.get_fail_msg_for_refresh_volume('backup_snap_error')

    def test_refresh_volume_expiration_timestamp_error(self, volume_module_mock):
        self.operation_before_refresh_volume(volume_module_mock)
        self.get_module_args['backup_snap_profile']['expiration_timestamp'] = '2024-23T01:20:00Z'
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.refresh_volume = MagicMock(return_value='snap_id_3')
        self.perform_operation(volume_module_mock)
        assert volume_module_mock.module.fail_json.call_args[1]['msg'] == MockVolumeApi.get_fail_msg_for_refresh_volume('expiration_timestamp_error')

    def operation_before_restore_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'source_snap': 'refresh_backup_snap_1',
            'create_backup_snap': True,
            'backup_snap_profile': {
                'name': 'restore_snap_2',
                'description': 'test backup snap',
                'expiration_timestamp': MockVolumeApi.EXPIRATION_TIMESTAMP,
                'performance_policy': 'low'
            },
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.get_volume = MagicMock(return_value=MockVolumeApi.VOL_DETAILS1[0])
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(return_value=MockVolumeApi.VOL_DETAILS1)
        volume_module_mock.provisioning.get_volumes = MagicMock(return_value=MockVolumeApi.VOL1_SNAPSHOT_LIST)
        volume_module_mock.get_performance_policy = MagicMock(return_value=MockVolumeApi.PERFORMANCE_POLICY_LOW)

    def test_restore_volume(self, volume_module_mock):
        self.operation_before_restore_volume(volume_module_mock)
        volume_module_mock.provisioning.restore_volume = MagicMock(return_value='snap_id_4')
        self.perform_operation(volume_module_mock)
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_module_mock.provisioning.restore_volume.assert_called()

    def test_restore_volume_exception(self, volume_module_mock):
        self.operation_before_restore_volume(volume_module_mock)
        volume_module_mock.provisioning.restore_volume = MagicMock(side_effect=MockApiException)
        self.perform_operation(volume_module_mock)
        assert volume_module_mock.module.fail_json.call_args[1]['msg'] == MockVolumeApi.get_fail_msg_for_restore_volume('exception')

    def test_restore_volume_snap_exception(self, volume_module_mock):
        self.operation_before_restore_volume(volume_module_mock)
        volume_module_mock.provisioning.get_volumes = MagicMock(side_effect=[MockApiException, MockVolumeApi.VOL1_SNAPSHOT_LIST])
        volume_module_mock.provisioning.restore_volume = MagicMock(return_value='snap_id_3')
        self.perform_operation(volume_module_mock)
        assert volume_module_mock.module.fail_json.call_args[1]['msg'] == MockVolumeApi.get_fail_msg_for_restore_volume('snap_exception')

    def operation_before_configure_metro(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'remote_system': 'remote-system',
            'remote_appliance_id': 'A2',
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.protection.get_remote_system_by_name = MagicMock(
            return_value=MockVolumeApi.REMOTE_SYSTEM_DETAILS)
        volume_module_mock.protection.get_remote_system_details = MagicMock(
            return_value=MockVolumeApi.REMOTE_SYSTEM_DETAILS[0])

    def test_configure_metro_volume(self, volume_module_mock):
        self.operation_before_configure_metro(volume_module_mock)
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1)
        volume_module_mock.provisioning.configure_metro_volume = MagicMock(
            return_value=True)
        volume_module_mock.perform_module_operation()
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_module_mock.provisioning.configure_metro_volume.assert_called()

    def test_configure_metro_volume_exception(self, volume_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.operation_before_configure_metro(volume_module_mock)
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS1)
        volume_module_mock.provisioning.configure_metro_volume = MagicMock(
            side_effect=MockApiException)
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.configure_metro_fail_msg() in \
               volume_module_mock.module.fail_json.call_args[1]['msg']
        volume_module_mock.provisioning.configure_metro_volume.assert_called()

    def test_rep_session_exception(self, volume_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.operation_before_configure_metro(volume_module_mock)
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.MODIFY_VOL_DETAILS1)
        volume_module_mock.protection.get_replication_session_details = MagicMock(
            side_effect=MockApiException)
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.rep_session_fail_msg() in \
               volume_module_mock.module.fail_json.call_args[1]['msg']
        volume_module_mock.protection.get_replication_session_details.assert_called()

    def test_existing_metro_exception(self, volume_module_mock):
        self.operation_before_configure_metro(volume_module_mock)
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS2)
        volume_module_mock.protection.get_replication_session_details = MagicMock(
            return_values=MockVolumeApi.REP_SESSION_DETAILS[0])
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.exisiting_metro_session_fail_msg() in \
               volume_module_mock.module.fail_json.call_args[1]['msg']
        volume_module_mock.protection.get_replication_session_details.assert_called()

    def test_multiple_remote_system_exception(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'remote_system': 'remote-system',
            'remote_appliance_id': 'A2',
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.protection.get_remote_system_by_name = MagicMock(
            return_value=MockVolumeApi.REMOTE_SYSTEM_DETAILS_1)
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.no_appliance_fail_msg() in \
               volume_module_mock.module.fail_json.call_args[1]['msg']
        volume_module_mock.protection.get_remote_system_by_name.assert_called()

    def test_remote_system_exception(self, volume_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'remote_system': MockVolumeApi.ID_1,
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.protection.get_remote_system_details = MagicMock(
            side_effect=MockApiException)
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.remote_system_fail_msg() in \
               volume_module_mock.module.fail_json.call_args[1]['msg']
        volume_module_mock.protection.get_remote_system_details.assert_called()

    def test_remote_system_app_exception(self, volume_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'remote_system': MockVolumeApi.REMOTE_SYSTEM_ID,
            'remote_appliance_id': 'A2',
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.protection.get_remote_system_details = MagicMock(
            return_value=MockVolumeApi.REMOTE_SYSTEM_DETAILS[0])
        volume_module_mock.protection.get_remote_system_appliance_details = MagicMock(
            side_effect=MockApiException)
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.remote_app_fail_msg() in \
               volume_module_mock.module.fail_json.call_args[1]['msg']
        volume_module_mock.protection.get_remote_system_appliance_details.assert_called()

    def test_end_metro(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'end_metro_config': True,
            'delete_remote_volume': True,
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS2)
        volume_module_mock.provisioning.end_volume_metro_config = MagicMock(
            return_value=True)
        volume_module_mock.perform_module_operation()
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is True
        volume_module_mock.provisioning.end_volume_metro_config.assert_called()

    def test_end_metro_exception(self, volume_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "400"
        self.get_module_args.update({
            'vol_name': "sample_volume_1",
            'end_metro_config': True,
            'delete_remote_volume': True,
            'state': "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.provisioning.get_volume_by_name = MagicMock(
            return_value=MockVolumeApi.VOL_DETAILS2)
        volume_module_mock.provisioning.end_volume_metro_config = MagicMock(
            side_effect=MockApiException)
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.end_metro_fail_msg() in \
               volume_module_mock.module.fail_json.call_args[1]['msg']
        volume_module_mock.provisioning.end_volume_metro_config.assert_called()
