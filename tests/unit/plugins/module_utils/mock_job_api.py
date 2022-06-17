# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Job module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockJobApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.job.PowerStoreJob.'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    JOB_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'job_id': None
    }

    JOB_DETAILS = {
        "description_l10n": "Modify network parameters.",
        "end_time": "2022-01-06T07:39:05.846+00:00",
        "estimated_completion_time": None,
        "id": "be0d099c-a6cf-44e8-88d7-9be80ccae369",
        "parent_id": None,
        "phase": "Completed",
        "phase_l10n": "Completed",
        "progress_percentage": 100,
        "resource_action": "modify",
        "resource_action_l10n": "modify",
        "resource_id": "nw6",
        "resource_name": None,
        "resource_type": "network",
        "resource_type_l10n": "network",
        "response_body": None,
        "response_status": None,
        "response_status_l10n": None,
        "root_id": "be0d099c-a6cf-44e8-88d7-9be80ccae369",
        "start_time": "2022-01-06T07:39:05.47+00:00",
        "state": "COMPLETED",
        "state_l10n": "Completed",
        "step_order": 23792565,
        "user": "admin"
    }

    @staticmethod
    def get_non_existing_job_details_failed_msg():
        return "Get details of job"
