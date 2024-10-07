# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Replication rule module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_replicationrule_api import MockReplicationRuleApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.replicationrule import PowerstoreReplicationRule


class TestPowerstoreReplicationRule():

    get_module_args = MockReplicationRuleApi.REPLICATION_RULE_COMMON_ARGS

    @pytest.fixture
    def replicationrule_module_mock(self, mocker):
        mocker.patch(MockReplicationRuleApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        replicationrule_module_mock = PowerstoreReplicationRule()
        replicationrule_module_mock.module = MagicMock()
        return replicationrule_module_mock

    def test_get_replication_rule_response(self, replicationrule_module_mock):
        self.get_module_args.update({
            'replication_rule_id': "0a9dc368-3085-4f4b-b7a4-23ec0166542f",
            'state': "present"
        })
        replicationrule_module_mock.module.params = self.get_module_args
        replicationrule_module_mock.conn.protection.get_replication_rule_details = MagicMock(
            return_value=MockReplicationRuleApi.REPLICATION_RULE_DETAILS[0])
        replicationrule_module_mock.perform_module_operation()
        assert self.get_module_args['replication_rule_id'] == replicationrule_module_mock.module.exit_json.call_args[1]['replication_rule_details']['id']
        replicationrule_module_mock.conn.protection.get_replication_rule_details.assert_called()

    def test_get_replication_rule_name_response(self, replicationrule_module_mock):
        self.get_module_args.update({
            'replication_rule_name': "sample_replication_rule_1",
            'state': "present"
        })
        replicationrule_module_mock.module.params = self.get_module_args
        replicationrule_module_mock.conn.protection.get_replication_rule_by_name = MagicMock(
            return_value=MockReplicationRuleApi.REPLICATION_RULE_DETAILS)
        replicationrule_module_mock.conn.protection.get_replication_rule_details = MagicMock(
            return_value=MockReplicationRuleApi.REPLICATION_RULE_DETAILS[0])
        replicationrule_module_mock.perform_module_operation()
        assert self.get_module_args['replication_rule_name'] == replicationrule_module_mock.module.exit_json.call_args[1]['replication_rule_details']['name']
        replicationrule_module_mock.conn.protection.get_replication_rule_by_name.assert_called()

    def test_get_replicationrule_replication_rule_name_exception(self, replicationrule_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'replication_rule_name': "sample_replication_rule_1",
            'state': "present"
        })
        replicationrule_module_mock.module.params = self.get_module_args
        replicationrule_module_mock.protection.get_replication_rule_by_name = MagicMock(
            side_effect=MockApiException)
        replicationrule_module_mock.conn.protection.get_replication_rule_details = MagicMock(
            return_value=MockReplicationRuleApi.REPLICATION_RULE_DETAILS[0])
        replicationrule_module_mock.perform_module_operation()
        replicationrule_module_mock.protection.get_replication_rule_by_name.assert_called()

    def test_get_replicationrule_multi_cluster(self, replicationrule_module_mock):
        self.get_module_args.update({
            'replication_rule_id': "0a9dc368-3085-4f4b-b7a4-23ec0166542f",
            'state': "present"
        })
        replicationrule_module_mock.module.params = self.get_module_args
        replicationrule_module_mock.conn.protection.get_replication_rule_details = MagicMock(
            return_value=MockReplicationRuleApi.REPLICATION_RULE_DETAILS[0])
        replicationrule_module_mock.provisioning.get_cluster_list = MagicMock(
            return_value=MockReplicationRuleApi.CLUSTER_DETAILS)
        replicationrule_module_mock.perform_module_operation()
        replicationrule_module_mock.conn.protection.get_replication_rule_details.assert_called()

    def test_create_replication_rule_response(self, replicationrule_module_mock):
        self.get_module_args.update({
            'replication_rule_name': "sample_replication_rule_1",
            'rpo': "Thirty_Minutes",
            'alert_threshold': "15",
            'remote_system': "RT-D0102",
            'state': "present"
        })
        replicationrule_module_mock.module.params = self.get_module_args
        replicationrule_module_mock.conn.protection.get_replication_rule_by_name = MagicMock(
            return_value=None)
        replicationrule_module_mock.conn.protection.get_replication_rule_details = MagicMock(
            return_value=MockReplicationRuleApi.REPLICATION_RULE_DETAILS[1])
        replicationrule_module_mock.perform_module_operation()
        replicationrule_module_mock.conn.protection.create_replication_rule.assert_called()

    def test_modify_replication_rule_response(self, replicationrule_module_mock):
        self.get_module_args.update({
            'replication_rule_name': "sample_replication_rule_1",
            'new_name': "new_replication_rule_name",
            'rpo': "One_Hour",
            'alert_threshold': "60",
            'remote_system': "RT-D0102",
            'state': "present"
        })
        replicationrule_module_mock.module.params = self.get_module_args
        replicationrule_module_mock.conn.protection.get_replication_rule_by_name = MagicMock(
            return_value=MockReplicationRuleApi.REPLICATION_RULE_DETAILS)
        replicationrule_module_mock.conn.protection.get_replication_rule_details = MagicMock(
            return_value=MockReplicationRuleApi.REPLICATION_RULE_DETAILS[0])
        replicationrule_module_mock.perform_module_operation()
        replicationrule_module_mock.conn.protection.modify_replication_rule.assert_called()

    def test_delete_replication_rule_response(self, replicationrule_module_mock):
        self.get_module_args.update({
            'replication_rule_id': "0a9dc368-3085-4f4b-b7a4-23ec0166542f",
            'state': "absent"
        })
        replicationrule_module_mock.module.params = self.get_module_args
        replicationrule_module_mock.conn.protection.get_replication_rule_details = MagicMock(
            return_value=MockReplicationRuleApi.REPLICATION_RULE_DETAILS[0])
        replicationrule_module_mock.perform_module_operation()
        replicationrule_module_mock.conn.protection.delete_replication_rule.assert_called()

    def test_delete_replication_rule_exception(self, replicationrule_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'replication_rule_id': "0a9dc368-3085-4f4b-b7a4-23ec0166542f",
            'state': "absent"
        })
        replicationrule_module_mock.module.params = self.get_module_args
        replicationrule_module_mock.conn.protection.get_replication_rule_details = MagicMock(
            return_value=MockReplicationRuleApi.REPLICATION_RULE_DETAILS[0])
        replicationrule_module_mock.conn.protection.delete_replication_rule = MagicMock(
            side_effect=MockApiException)
        replicationrule_module_mock.perform_module_operation()
        replicationrule_module_mock.conn.protection.delete_replication_rule.assert_called()
