#!/usr/bin/python
# Copyright: (c) 2024, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
module: job
version_added: '1.3.0'
short_description: Manage jobs for PowerStore
description:
- Managing jobs on PowerStore Storage System includes getting details of job.

author:
- Akash Shendge (@shenda1) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerstore.powerstore

options:
  job_id:
    description:
    - The ID of the job.
    type: str
    required: true

notes:
- The I(check_mode) is not supported.
'''

EXAMPLES = r'''
- name: Get Job Details
  dellemc.powerstore.job:
    array_ip: "{{mgmt_ip}}"
    validate_certs: "{{validate_certs}}"
    user: "{{user}}"
    password: "{{password}}"
    job_id: "a544981c-e94a-40ab-9eae-e578e182d2bb"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"

job_details:
    description: The job details.
    type: complex
    returned: When job exists.
    contains:
        id:
            description: Unique identifier of the job.
            type: str
        resource_action:
            description: User-specified action to be performed on the
                         given resource.
            type: str
        resource_type:
            description: Resource Type for the given resource.
            type: str
        resource_id:
            description: Unique identifier of the resource on which the job
                         is operating.
            type: str
        resource_name:
            description: Name of the resource on which the job is operating.
            type: str
        description_l10n:
            description: Description of the job.
            type: str
        state:
            description: Current status of the job.
            type: str
        start_time:
            description: Date and time when the job execution started.
            type: str
        phase:
            description: Current status of the job.
            type: str
        end_time:
            description: Date and time when the job execution completed.
            type: str
        estimated_completion_time:
            description: Estimated completion date and time.
            type: str
        progress_percentage:
            description: Percent complete of the job.
            type: int
        parent_id:
            description: Unique identifier of the parent job, if applicable.
            type: str
        root_id:
            description: Unique identifier of the root job, if applicable.
                         The root job is the job at the top of the parent
                         hierarchy.
            type: str
        response_body:
            description: Base response object.
            type: complex
            contains:
                response_type:
                    description: Job error response.
                    type: str
                messages:
                    description: The details of the error response.
                    type: complex
                    contains:
                        code:
                            description: Hexadecimal code of the error.
                            type: str
                        severity:
                            description: Type of the severity.
                            type: str
                        arguments:
                            description: Values involved in the error.
                            type: list
                        message_l10n:
                            description: The description of the error.
                            type: str
        user:
            description: Name of the user associated with the job.
            type: str
        response_status:
            description: Possible HTTP status values of completed or failed
                         jobs.
            type: str
        step_order:
            description: Order of a given job step with respect to its
                         siblings within the job hierarchy.
            type: int
    sample: {
        "description_l10n": "Modify network parameters.",
        "end_time": "2022-01-06T07:39:05.846+00:00",
        "estimated_completion_time": null,
        "id": "be0d099c-a6cf-44e8-88d7-9be80ccae369",
        "parent_id": null,
        "phase": "Completed",
        "phase_l10n": "Completed",
        "progress_percentage": 100,
        "resource_action": "modify",
        "resource_action_l10n": "modify",
        "resource_id": "nw6",
        "resource_name": null,
        "resource_type": "network",
        "resource_type_l10n": "network",
        "response_body": null,
        "response_status": null,
        "response_status_l10n": null,
        "root_id": "be0d099c-a6cf-44e8-88d7-9be80ccae369",
        "start_time": "2022-01-06T07:39:05.47+00:00",
        "state": "COMPLETED",
        "state_l10n": "Completed",
        "step_order": 23792565,
        "user": "admin"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import utils

LOG = utils.get_logger('job')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']


class PowerStoreJob(object):
    """Class with job operations"""

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_job_parameters())

        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False
        )

        LOG.info('HAS_PY4PS = %s , IMPORT_ERROR = %s', HAS_PY4PS,
                 IMPORT_ERROR)
        if HAS_PY4PS is False:
            self.module.fail_json(msg=IMPORT_ERROR)
        LOG.info('IS_SUPPORTED_PY4PS_VERSION = %s , VERSION_ERROR = '
                 '%s', IS_SUPPORTED_PY4PS_VERSION, VERSION_ERROR)
        if IS_SUPPORTED_PY4PS_VERSION is False:
            self.module.fail_json(msg=VERSION_ERROR)

        self.conn = utils.get_powerstore_connection(self.module.params)
        self.provisioning = self.conn.provisioning
        LOG.info('Got Py4ps instance for provisioning on PowerStore %s',
                 self.provisioning)

    def get_job_details(self, job_id):
        """Get job details"""

        try:
            LOG.info('Getting the details of job ID: %s', job_id)
            return self.provisioning.get_job_details(job_id)

        except Exception as e:
            msg = "Get details of job {0} failed with error {1}".format(
                job_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def perform_module_operation(self):
        """ Accept the parameters and get the job details """

        job_id = self.module.params['job_id']

        # Check for valid UUID
        is_valid_uuid = utils.name_or_id(job_id)
        if is_valid_uuid != "ID":
            error_msg = "Please provide valid job id."
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

        job_details = self.get_job_details(job_id)

        self.module.exit_json(
            changed=False,
            job_details=job_details
        )


def get_powerstore_job_parameters():
    """This method provides the parameters required for the ansible job module
    of PowerStore. """
    return dict(
        job_id=dict(type='str', required=True)
    )


def main():
    """ Create PowerStore Job object and perform action on it
        based on user input from playbook """
    obj = PowerStoreJob()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
