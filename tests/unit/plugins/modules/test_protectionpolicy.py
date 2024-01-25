# Copyright: (c) 2024, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Protection policy module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_protectionpolicy_api import MockProtectionpolicyApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.protectionpolicy import PowerstoreProtectionpolicy


class TestPowerstoreProtectionpolicy():

    get_module_args = MockProtectionpolicyApi.PROTECTIONPOLICY_COMMON_ARGS

    @pytest.fixture
    def protectionpolicy_module_mock(self, mocker):
        mocker.patch(MockProtectionpolicyApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        protectionpolicy_module_mock = PowerstoreProtectionpolicy()
        protectionpolicy_module_mock.module = MagicMock()
        return protectionpolicy_module_mock

    def test_get_protectionpolicy_response(self, protectionpolicy_module_mock):
        self.get_module_args.update({
            'protectionpolicy_id': "d8712ddc-2e89-4b9a-827e-37ef75ac9a36",
            'state': "present"
        })
        protectionpolicy_module_mock.module.params = self.get_module_args
        protectionpolicy_module_mock.perform_module_operation()
        protectionpolicy_module_mock.protection.get_protection_policy_details.assert_called()

    def test_get_protectionpolicy_response_name(self, protectionpolicy_module_mock):
        self.get_module_args.update({
            'name': "protection_policy1",
            'state': "present"
        })
        protectionpolicy_module_mock.module.params = self.get_module_args
        protectionpolicy_module_mock.protection.get_protection_policy_by_name = MagicMock(return_value=MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS)
        protectionpolicy_module_mock.perform_module_operation()
        protectionpolicy_module_mock.protection.get_protection_policy_by_name.assert_called()

    def test_create_protection_policy_with_snaprule_name(self, protectionpolicy_module_mock):
        self.get_module_args.update({
            'name': "protection_policy1",
            'snapshotrules': ["Ansible_test_snap_rule_1"],
            'snapshotrule_state': "present-in-policy",
            'state': "present"
        })
        protectionpolicy_module_mock.module.params = self.get_module_args
        protectionpolicy_module_mock.protection.get_protection_policy_by_name = MagicMock(return_value=None)
        protectionpolicy_module_mock.get_snapshot_rule_details = MagicMock(return_value=(True, MockProtectionpolicyApi.SNAPSHOTRULE_DETAILS[0]['id']))
        protectionpolicy_module_mock.module.create_protection_policy = MagicMock(return_value=(True, MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS[0]))
        protectionpolicy_module_mock.perform_module_operation()
        print(protectionpolicy_module_mock.module.exit_json.call_args[1])
        protectionpolicy_module_mock.protection.create_protection_policy.assert_called()

    def test_create_protection_policy_with_reprule_name(self, protectionpolicy_module_mock):
        self.get_module_args.update({
            'name': "protection_policy1",
            'replicationrule': "Test-Ans",
            'state': "present"
        })
        protectionpolicy_module_mock.module.params = self.get_module_args
        protectionpolicy_module_mock.protection.get_protection_policy_by_name = MagicMock(return_value=None)
        protectionpolicy_module_mock.protection.get_replication_rule_by_name = MagicMock(
            return_value=MockProtectionpolicyApi.REPLICATIONRULE_DETAILS)
        protectionpolicy_module_mock.module.create_protection_policy = MagicMock(
            return_value=(True, MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS[0]))
        protectionpolicy_module_mock.perform_module_operation()
        print(protectionpolicy_module_mock.module.exit_json.call_args[1])
        protectionpolicy_module_mock.protection.create_protection_policy.assert_called()

    def test_create_protection_policy_with_snaprule_id(self, protectionpolicy_module_mock):
        self.get_module_args.update({
            'name': "protection_policy1",
            'snapshotrules': ["49830e64-a342-42ae-8f55-2dff084522ca"],
            'snapshotrule_state': "present-in-policy",
            'state': "present"
        })
        protectionpolicy_module_mock.module.params = self.get_module_args
        protectionpolicy_module_mock.protection.get_protection_policy_by_name = MagicMock(return_value=None)
        protectionpolicy_module_mock.protection.get_snapshot_rule_details = MagicMock(return_value=(MockProtectionpolicyApi.SNAPSHOTRULE_DETAILS[0]))
        protectionpolicy_module_mock.module.create_protection_policy = MagicMock(return_value=(True, MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS[0]))
        protectionpolicy_module_mock.perform_module_operation()
        print(protectionpolicy_module_mock.module.exit_json.call_args[1])
        protectionpolicy_module_mock.protection.create_protection_policy.assert_called()

    def test_create_protection_policy_with_reprule_id(self, protectionpolicy_module_mock):
        self.get_module_args.update({
            'name': "protection_policy1",
            'replicationrule': "ffda77a6-a429-4a09-b630-7dd611f81926",
            'state': "present"
        })
        protectionpolicy_module_mock.module.params = self.get_module_args
        protectionpolicy_module_mock.protection.get_protection_policy_by_name = MagicMock(return_value=None)
        protectionpolicy_module_mock.protection.get_replication_rule_details = MagicMock(return_value=(MockProtectionpolicyApi.REPLICATIONRULE_DETAILS[0]))
        protectionpolicy_module_mock.module.create_protection_policy = MagicMock(return_value=(True, MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS[0]))
        protectionpolicy_module_mock.perform_module_operation()
        print(protectionpolicy_module_mock.module.exit_json.call_args[1])
        protectionpolicy_module_mock.protection.create_protection_policy.assert_called()

    def test_modify_desc_protection_policy(self, protectionpolicy_module_mock):
        self.get_module_args.update({
            'protectionpolicy_id': "d8712ddc-2e89-4b9a-827e-37ef75ac9a36",
            'description': "modify_description",
            'state': "present"
        })
        protectionpolicy_module_mock.module.params = self.get_module_args
        protectionpolicy_module_mock.protection.get_protection_policy_details = MagicMock(return_value=MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS1)
        protectionpolicy_module_mock.protection.modify_protection_policy = MagicMock(return_value=MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS2)
        protectionpolicy_module_mock.perform_module_operation()
        print(protectionpolicy_module_mock.module.exit_json.call_args[1])
        protectionpolicy_module_mock.protection.modify_protection_policy.assert_called()

    def test_rename_protection_policy(self, protectionpolicy_module_mock):
        self.get_module_args.update({
            'protectionpolicy_id': "d8712ddc-2e89-4b9a-827e-37ef75ac9a36",
            'new_name': "protection_policy2",
            'state': "present"
        })
        protectionpolicy_module_mock.module.params = self.get_module_args
        protectionpolicy_module_mock.protection.get_protection_policy_details = MagicMock(return_value=MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS1)
        protectionpolicy_module_mock.protection.modify_protection_policy = MagicMock(return_value=MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS3)
        protectionpolicy_module_mock.perform_module_operation()
        print(protectionpolicy_module_mock.module.exit_json.call_args[1])
        protectionpolicy_module_mock.protection.modify_protection_policy.assert_called()

    def test_add_snaprule_protection_policy(self, protectionpolicy_module_mock):
        self.get_module_args.update({
            'protectionpolicy_id': "d8712ddc-2e89-4b9a-827e-37ef75ac9a36",
            'snapshotrules': ["Ansible_test_snap_rule_2"],
            'snapshotrule_state': "present-in-policy",
            'state': "present"
        })
        protectionpolicy_module_mock.module.params = self.get_module_args
        protectionpolicy_module_mock.protection.get_protection_policy_details = MagicMock(
            return_value=MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS[0])
        protectionpolicy_module_mock.get_snapshot_rule_details = MagicMock(return_value=(True, MockProtectionpolicyApi.SNAPSHOTRULE_DETAILS1.get('id')))
        protectionpolicy_module_mock.protection.modify_protection_policy = MagicMock(
            return_value=MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS3)
        protectionpolicy_module_mock.perform_module_operation()
        print(protectionpolicy_module_mock.module.exit_json.call_args[1])
        protectionpolicy_module_mock.protection.modify_protection_policy.assert_called()

    def test_remove_snaprule_protection_policy(self, protectionpolicy_module_mock):
        self.get_module_args.update({
            'protectionpolicy_id': "d8712ddc-2e89-4b9a-827e-37ef75ac9a36",
            'snapshotrules': ["Ansible_test_snap_rule_2"],
            'snapshotrule_state': "absent-in-policy",
            'state': "present"
        })
        protectionpolicy_module_mock.module.params = self.get_module_args
        protectionpolicy_module_mock.protection.get_protection_policy_details = MagicMock(
            return_value=MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS3)
        protectionpolicy_module_mock.get_snapshot_rule_details = MagicMock(return_value=(True, MockProtectionpolicyApi.SNAPSHOTRULE_DETAILS1.get('id')))
        protectionpolicy_module_mock.protection.modify_protection_policy = MagicMock(
            return_value=MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS[0])
        protectionpolicy_module_mock.perform_module_operation()
        print(protectionpolicy_module_mock.module.exit_json.call_args[1])
        protectionpolicy_module_mock.protection.modify_protection_policy.assert_called()

    def test_remove_reprule_protection_policy(self, protectionpolicy_module_mock):
        self.get_module_args.update({
            'protectionpolicy_id': "d8712ddc-2e89-4b9a-827e-37ef75ac9a36",
            'replicationrule': "",
            'state': "present"
        })
        protectionpolicy_module_mock.module.params = self.get_module_args
        protectionpolicy_module_mock.protection.get_protection_policy_details = MagicMock(
            return_value=MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS[0])
        protectionpolicy_module_mock.protection.modify_protection_policy = MagicMock(return_value=MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS_WO_REPRULE)
        protectionpolicy_module_mock.perform_module_operation()
        protectionpolicy_module_mock.protection.modify_protection_policy.assert_called()

    def test_add_reprule_protection_policy(self, protectionpolicy_module_mock):
        self.get_module_args.update({
            'protectionpolicy_id': "d8712ddc-2e89-4b9a-827e-37ef75ac9a36",
            'replicationrule': "ffda77a6-a429-4a09-b630-7dd611f81926",
            'state': "present"
        })
        protectionpolicy_module_mock.module.params = self.get_module_args
        protectionpolicy_module_mock.protection.get_protection_policy_details = MagicMock(
            return_value=MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS_WO_REPRULE)
        protectionpolicy_module_mock.protection.modify_protection_policy = MagicMock(return_value=MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS[0])
        protectionpolicy_module_mock.perform_module_operation()
        protectionpolicy_module_mock.protection.modify_protection_policy.assert_called()

    def test_delete_protection_policy(self, protectionpolicy_module_mock):
        self.get_module_args.update({
            'protectionpolicy_id': "d8712ddc-2e89-4b9a-827e-37ef75ac9a36",
            'state': "absent"
        })
        protectionpolicy_module_mock.module.params = self.get_module_args
        protectionpolicy_module_mock.protection.get_protection_policy_details = MagicMock(return_value=MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS1)
        protectionpolicy_module_mock.perform_module_operation()
        protectionpolicy_module_mock.protection.delete_protection_policy.assert_called()

    def test_add_nonexisting_snaprule_prot_policy(self, protectionpolicy_module_mock):
        self.get_module_args.update({
            'protectionpolicy_id': "d8712ddc-2e89-4b9a-827e-37ef75ac9a36",
            'snapshotrules': ["ansible_snapshotrule"],
            'snapshotrule_state': "present-in-policy",
            'state': "present"
        })
        protectionpolicy_module_mock.module.params = self.get_module_args
        protectionpolicy_module_mock.get_clusters = MagicMock(return_value=MockProtectionpolicyApi.CLUSTER_LIST)
        protectionpolicy_module_mock.protection.get_protection_policy_details = MagicMock(
            return_value=MockProtectionpolicyApi.PROTECTION_POLICY_DETAILS[0])
        protectionpolicy_module_mock.get_snapshot_rule_details = MagicMock(
            return_value=(None, None))
        protectionpolicy_module_mock.perform_module_operation()
        assert MockProtectionpolicyApi.add_nonexisting_snaprule() in protectionpolicy_module_mock.module.fail_json.call_args[1]['msg']
