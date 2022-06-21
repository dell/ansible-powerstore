# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of SnapshotRule module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockSnapshotruleApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.snapshotrule.PowerstoreSnapshotrule'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    SNAPSHOTRULE_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        "days_of_week": None,
        "desired_retention": None,
        "id": None,
        "interval": None,
        "name": None,
        "policies": None,
        "time_of_day": None,
        "new_name": None,
        "delete_snaps": None,
        "snapshotrule_id": None
    }

    SNAPSHOTRULE_DETAILS = {
        "days_of_week": ["Sunday"],
        "desired_retention": 168,
        "id": "46723735-13c1-4bab-bb72-cf3b4c0dcb9b",
        "interval": "One_Day",
        "name": "snapshot_rule1",
        "policies": [],
        "time_of_day": None
    }
