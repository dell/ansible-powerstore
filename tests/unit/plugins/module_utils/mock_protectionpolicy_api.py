# Copyright: (c) 2022, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of ProtectionPolicy module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockProtectionpolicyApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.protectionpolicy.PowerstoreProtectionpolicy'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    PROTECTIONPOLICY_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        "name": None,
        "protectionpolicy_id": None,
        "new_name": None,
        "description": None,
        "replicationrule": None,
        "snapshotrules": None,
        "snapshotrule_state": None,
        "state": None
    }

    PROTECTION_POLICY_DETAILS = [{
        "description": "",
        "id": "d8712ddc-2e89-4b9a-827e-37ef75ac9a36",
        "name": "protection_policy1",
        "replication_rules": [
            {
                "id": "ffda77a6-a429-4a09-b630-7dd611f81926",
                "name": "Test-Ans"
            }
        ],
        "snapshot_rules": [
            {
                "id": "49830e64-a342-42ae-8f55-2dff084522ca",
                "name": "Ansible_test_snap_rule_1"
            }
        ],
        "type": "Protection"
    }]

    PROTECTION_POLICY_DETAILS_WO_REPRULE = {
        "description": "",
        "id": "d8712ddc-2e89-4b9a-827e-37ef75ac9a36",
        "name": "protection_policy1",
        "replication_rules": [],
        "snapshot_rules": [
            {
                "id": "49830e64-a342-42ae-8f55-2dff084522ca",
                "name": "Ansible_test_snap_rule_1"
            }
        ],
        "type": "Protection"
    }

    PROTECTION_POLICY_DETAILS1 = {
        "description": "",
        "id": "d8712ddc-2e89-4b9a-827e-37ef75ac9a36",
        "name": "protection_policy1",
        "replication_rules": [],
        "snapshot_rules": [],
        "type": "Protection"
    }

    PROTECTION_POLICY_DETAILS2 = {
        "description": "modify_description",
        "id": "d8712ddc-2e89-4b9a-827e-37ef75ac9a36",
        "name": "protection_policy1",
        "replication_rules": [],
        "snapshot_rules": [],
        "type": "Protection"
    }

    PROTECTION_POLICY_DETAILS3 = {
        "description": "modify_description",
        "id": "d8712ddc-2e89-4b9a-827e-37ef75ac9a36",
        "name": "protection_policy2",
        "replication_rules": [],
        "snapshot_rules": [
            {
                "id": "49830e64-a342-42ae-8f55-2dff084522ca",
                "name": "Ansible_test_snap_rule_1"
            },
            {
                "id": "49830e64-a342-42ae-8f55-2dff084522cb",
                "name": "Ansible_test_snap_rule_2"
            }
        ],
        "type": "Protection"
    }

    SNAPSHOTRULE_DETAILS = [{
        "days_of_week": [
            "Sunday",
            "Friday"
        ],
        "desired_retention": 72,
        "id": "49830e64-a342-42ae-8f55-2dff084522ca",
        "interval": None,
        "name": "Ansible_test_snap_rule_1",
        "policies": [
            {
                "id": "d8712ddc-2e89-4b9a-827e-37ef75ac9a36",
                "name": "protection_policy1"
            }
        ],
        "time_of_day": "01:00:00"
    }]

    SNAPSHOTRULE_DETAILS1 = {
        "days_of_week": [
            "Sunday",
            "Friday"
        ],
        "desired_retention": 72,
        "id": "49830e64-a342-42ae-8f55-2dff084522cb",
        "interval": None,
        "name": "Ansible_test_snap_rule_2",
        "policies": [
            {
                "id": "d8712ddc-2e89-4b9a-827e-37ef75ac9a36",
                "name": "protection_policy1"
            }
        ],
        "time_of_day": "01:00:00"
    }

    REPLICATIONRULE_DETAILS = [{
        "alert_threshold": 30,
        "id": "ffda77a6-a429-4a09-b630-7dd611f81926",
        "is_replica": False,
        "name": "Test-Ans",
        "policies": [
            {
                "id": "7d2f1466-c757-42c4-8345-7e886b7cdd0c",
                "name": "Test-Ans"
            }
        ],
        "remote_system_id": "f07be373-dafd-4a46-8b21-f7cf790c287f",
        "remote_system_name": "WN-DXXXX",
        "rpo": "One_Hour"
    }]

    CLUSTER_LIST = [
        {
            'id': 0,
            'name': "RT-D0335"
        }
    ]

    @staticmethod
    def add_nonexisting_snaprule():
        return "snapshot rule name: ansible_snapshotrule is not found on the array"
