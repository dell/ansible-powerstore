# Copyright: (c) 2022, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of Replication Rule module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockReplicationRuleApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.replicationrule.PowerstoreReplicationRule'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    REPLICATION_RULE_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'replication_rule_id': None,
        'replication_rule_name': None,
        'new_name': None,
        'state': None,
        'alert_threshold': None,
        'rpo': None,
        'remote_system': None,
        'remote_system_address': None
    }

    REPLICATION_RULE_DETAILS = [
        {
            "alert_threshold": 15,
            "id": "0a9dc368-3085-4f4b-b7a4-23ec0166542f",
            "is_replica": False,
            "name": "sample_replication_rule_1",
            "policies": [],
            "remote_system_id": "677f64ff-955a-49ce-9a06-7d5af0ec4929",
            "remote_system_name": "RT-D0101",
            "rpo": "Thirty_Minutes"},
        {
            "alert_threshold": 15,
            "id": "0a9dc368-3085-4f4b-b7a4-23ec0166542g",
            "is_replica": False,
            "name": "sample_replication_rule_1",
            "policies": [],
            "remote_system_id": "677f64ff-955a-49ce-9a06-7d5af0ec4929",
            "remote_system_name": "RT-D0102",
            "rpo": "Thirty_Minutes"}
    ]

    CLUSTER_DETAILS = [
        {
            "id": "0",
            "name": "WN-ABCD"},
        {
            "id": "1",
            "name": "WN-WXYZ"}
    ]
