# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for info module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_info_api import MockInfoApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException

from ansible_collections.dellemc.powerstore.plugins.modules.info import PowerstoreInfo


class TestPowerstoreInfo():

    get_module_args = MockInfoApi.INFO_COMMON_ARGS

    @pytest.fixture
    def info_module_mock(self, mocker):
        mocker.patch(MockInfoApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        info_module_mock = PowerstoreInfo()
        return info_module_mock

    def test_get_security_config_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['security_config'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_security_configs.assert_called()

    def test_get_certificate_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['certificate'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_certificates.assert_called()

    def test_get_ad_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['ad'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.provisioning.get_file_ads.assert_called()

    def test_get_ldap_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['ldap'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.provisioning.get_file_ldaps.assert_called()

    def test_get_dns_response(self, info_module_mock):
        MockInfoApi.get_dns_response('api')
        self.get_module_args.update({
            'gather_subset': ['dns'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_dns_list.assert_called()

    def test_get_ntp_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['ntp'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_ntp_list.assert_called()

    def test_get_smtp_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['smtp_config'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_smtp_configs.assert_called()

    def test_get_email_destination_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['email_notification'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_destination_emails.assert_called()

    def test_get_remote_support_contact_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['remote_support_contact'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_remote_support_contact_list.assert_called()

    def test_get_remote_support_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['remote_support'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_remote_support_list.assert_called()

    def test_get_filesystem_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['file_system'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.conn.provisioning.get_file_systems.assert_called()

    def test_get_role_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['role'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_roles.assert_called()

    def test_get_response_invalid_gather_subset(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['roles'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_invalid_gather_subset_failed_msg() in \
            info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_role_multiple_cluster_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['role'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockInfoApi.CLUSTER_DETAILS_TWO)
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_roles.assert_called()

    def test_get_role_get_array_version_exception(self, info_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        MockInfoApi.get_one_id_response('api')
        self.get_module_args.update({
            'gather_subset': ['role'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockInfoApi.CLUSTER_DETAILS_TWO)
        info_module_mock.provisioning.get_array_version = MagicMock(
            side_effect=MockApiException)
        info_module_mock.perform_module_operation()
        info_module_mock.provisioning.get_array_version.assert_called()

    def test_get_role_get_empty_subset_exception(self, info_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        MockInfoApi.get_one_id_response('api')
        self.get_module_args.update({
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_no_gather_subset_failed_msg() in \
            info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_filesystem_snapshot_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['file_system'],
            'filters': [{
                'filter_key': 'access_type',
                'filter_operator': 'equal',
                'filter_value': 'Snapshot'
            }],
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.conn.provisioning.get_file_systems.assert_called()

    def test_get_filesystem_invalid_filter_key_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['file_system'],
            'filters': [{
                'filter_key': 'access_type',
                'filter_operator': 'equal',
                'filter_value': 'Snapshot',
                'filter_subset': 'file_system'
            }],
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_subset_invalid_filter() in \
            info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_volume_multiple_filter_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['vol'],
            'filters': [
                {
                    'filter_key': 'size',
                    'filter_operator': 'greater',
                    'filter_value': '1073741824'},
                {
                    'filter_key': 'size',
                    'filter_operator': 'lesser',
                    'filter_value': '5368706371'}
            ],
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.conn.provisioning.get_volumes.assert_called()

    def test_get_volume_invalid_valid_filter_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['vol'],
            'filters': [
                {
                    'filter_key': 'size',
                    'filter_operator': 'greater',
                    'filter_value': '1073741824'},
                {
                    'filter_key': 'size',
                    'filter_operator': None,
                    'filter_value': '5368706371'}
            ],
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_volumes_failed_msg() in \
            info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_vcenter_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['vcenter'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_vcenters.assert_called()

    def test_get_virtual_volume_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['virtual_volume'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_virtual_volume_list.assert_called()

    def test_get_storage_container_response(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['storage_container'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_storage_container_list.assert_called()

    def test_get_replication_groups(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['replication_group'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.protection.get_replication_groups.assert_called()

    def test_get_discovered_appliances(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['discovered_appliance'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_discovered_appliances.assert_called()

    def test_get_filesystem_invalid_filter_key(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['file_system'],
            'filters': [{
                'filter_key': 'access_type',
                'filter_operator': "equal",
                'filter_value': 'Snapshot',
                'filter_subset': None
            }],
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_invalid_filter_key() in \
            info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_file_interfaces(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['file_interface'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.file_interface.get_file_interface_list.assert_called()

    def test_get_smb_servers(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['smb_server'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.smb_server.get_smb_server_list.assert_called()

    def test_get_nfs_servers(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['nfs_server'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.nfs_server.get_nfs_server_list.assert_called()

    def test_get_file_dnses(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['file_dns'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.file_dns.get_file_dns_list.assert_called()

    def test_get_file_nises(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['file_nis'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.file_nis.get_file_nis_list.assert_called()

    def test_get_service_configs(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['service_config'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_service_configs.assert_called()

    def test_get_snmp_servers(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['snmp_manager'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        info_module_mock.snmp_manager.get_snmp_server_list.assert_called()

    # ---- QoS Gather Subset Tests (U-122 to U-136) ----

    IO_LIMIT_RULES_LIST = [
        {"id": "rule-1", "name": "rule_a", "max_bw": 102400, "max_iops": 5000, "burst_percentage": 20, "type": "Absolute", "policies": []},
        {"id": "rule-2", "name": "rule_b", "max_bw": 204800, "max_iops": 10000, "burst_percentage": 50, "type": "Density", "policies": []},
        {"id": "rule-3", "name": "rule_c", "max_bw": 51200, "max_iops": 2000, "burst_percentage": 0, "type": "Absolute",
         "policies": [{"id": "pol-1", "name": "gold_qos"}]}
    ]

    FILE_IO_LIMIT_RULES_LIST = [
        {"id": "frule-1", "name": "file_rule_a", "max_bw": 500, "policies": []},
        {"id": "frule-2", "name": "file_rule_b", "max_bw": 1000, "policies": []}
    ]

    # U-122
    def test_get_io_limit_rules(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['io_limit_rule'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_io_limit_rules = MagicMock(return_value=self.IO_LIMIT_RULES_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.provisioning.get_io_limit_rules.assert_called()
        assert 'io_limit_rules' in info_module_mock.module.exit_json.call_args[1]

    # U-123
    def test_get_io_limit_rules_empty(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['io_limit_rule'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_io_limit_rules = MagicMock(return_value=[])
        info_module_mock.perform_module_operation()
        result = info_module_mock.module.exit_json.call_args[1]
        assert result.get('io_limit_rules', None) == [] or 'io_limit_rules' in result

    # U-124
    def test_get_io_limit_rules_exception(self, info_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "500"
        self.get_module_args.update({
            'gather_subset': ['io_limit_rule'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_io_limit_rules = MagicMock(side_effect=MockApiException)
        info_module_mock.perform_module_operation()
        info_module_mock.module.fail_json.assert_called()

    # U-125
    def test_get_file_io_limit_rules(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['file_io_limit_rule'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.configuration.get_file_io_limit_rules = MagicMock(return_value=self.FILE_IO_LIMIT_RULES_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_file_io_limit_rules.assert_called()
        assert 'file_io_limit_rules' in info_module_mock.module.exit_json.call_args[1]

    # U-126
    def test_get_file_io_limit_rules_empty(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['file_io_limit_rule'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.configuration.get_file_io_limit_rules = MagicMock(return_value=[])
        info_module_mock.perform_module_operation()
        result = info_module_mock.module.exit_json.call_args[1]
        assert result.get('file_io_limit_rules', None) == [] or 'file_io_limit_rules' in result

    # U-127
    def test_get_file_io_limit_rules_exception(self, info_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "500"
        self.get_module_args.update({
            'gather_subset': ['file_io_limit_rule'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.configuration.get_file_io_limit_rules = MagicMock(side_effect=MockApiException)
        info_module_mock.perform_module_operation()
        info_module_mock.module.fail_json.assert_called()

    # U-128
    def test_get_io_limit_rules_with_filter(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['io_limit_rule'],
            'filters': [{'filter_key': 'name', 'filter_operator': 'equal', 'filter_value': 'rule_a'}],
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_io_limit_rules = MagicMock(return_value=[self.IO_LIMIT_RULES_LIST[0]])
        info_module_mock.perform_module_operation()
        info_module_mock.provisioning.get_io_limit_rules.assert_called()

    # U-129
    def test_get_file_io_limit_rules_with_filter(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['file_io_limit_rule'],
            'filters': [{'filter_key': 'name', 'filter_operator': 'equal', 'filter_value': 'file_rule_a'}],
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.configuration.get_file_io_limit_rules = MagicMock(return_value=[self.FILE_IO_LIMIT_RULES_LIST[0]])
        info_module_mock.perform_module_operation()
        info_module_mock.configuration.get_file_io_limit_rules.assert_called()

    # U-130
    def test_io_limit_rule_details_complete(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['io_limit_rule'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_io_limit_rules = MagicMock(return_value=self.IO_LIMIT_RULES_LIST)
        info_module_mock.perform_module_operation()
        rules = info_module_mock.module.exit_json.call_args[1].get('io_limit_rules', [])
        if rules:
            rule = rules[0]
            for field in ['id', 'name', 'max_bw', 'max_iops', 'burst_percentage', 'type']:
                assert field in rule

    # U-131
    def test_file_io_limit_rule_details_complete(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['file_io_limit_rule'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.configuration.get_file_io_limit_rules = MagicMock(return_value=self.FILE_IO_LIMIT_RULES_LIST)
        info_module_mock.perform_module_operation()
        rules = info_module_mock.module.exit_json.call_args[1].get('file_io_limit_rules', [])
        if rules:
            rule = rules[0]
            for field in ['id', 'name', 'max_bw']:
                assert field in rule

    # U-132
    def test_existing_subsets_still_work(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['vol'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_volumes = MagicMock(return_value=[])
        info_module_mock.perform_module_operation()
        info_module_mock.provisioning.get_volumes.assert_called()

    # U-133
    def test_io_limit_rule_multiple_rules(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['io_limit_rule'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_io_limit_rules = MagicMock(return_value=self.IO_LIMIT_RULES_LIST)
        info_module_mock.perform_module_operation()
        rules = info_module_mock.module.exit_json.call_args[1].get('io_limit_rules', [])
        assert len(rules) == 3

    # U-134
    def test_combined_subsets(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['io_limit_rule', 'file_io_limit_rule'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_io_limit_rules = MagicMock(return_value=self.IO_LIMIT_RULES_LIST)
        info_module_mock.configuration.get_file_io_limit_rules = MagicMock(return_value=self.FILE_IO_LIMIT_RULES_LIST)
        info_module_mock.perform_module_operation()
        result = info_module_mock.module.exit_json.call_args[1]
        assert 'io_limit_rules' in result
        assert 'file_io_limit_rules' in result

    # U-135
    def test_io_limit_rule_with_policies(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['io_limit_rule'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_io_limit_rules = MagicMock(return_value=self.IO_LIMIT_RULES_LIST)
        info_module_mock.perform_module_operation()
        rules = info_module_mock.module.exit_json.call_args[1].get('io_limit_rules', [])
        rule_with_policy = [r for r in rules if r.get('policies')]
        assert len(rule_with_policy) >= 1

    # U-136
    def test_info_check_mode(self, info_module_mock):
        self.get_module_args.update({
            'gather_subset': ['io_limit_rule'],
            'filters': None,
            'all_pages': None
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.module.check_mode = True
        info_module_mock.provisioning.get_io_limit_rules = MagicMock(return_value=self.IO_LIMIT_RULES_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.provisioning.get_io_limit_rules.assert_called()
