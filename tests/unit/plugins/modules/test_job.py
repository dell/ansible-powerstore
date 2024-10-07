# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for job module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_job_api import MockJobApi
from ansible_collections.dellemc.powerstore.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerstore.plugins.modules.job import PowerStoreJob


class TestPowerstoreJob():

    get_module_args = MockJobApi.JOB_COMMON_ARGS

    @pytest.fixture
    def job_module_mock(self, mocker):
        mocker.patch(MockJobApi.MODULE_UTILS_PATH + '.PowerStoreException', new=MockApiException)
        job_module_mock = PowerStoreJob()
        job_module_mock.module = MagicMock()
        return job_module_mock

    def test_get_job_response(self, job_module_mock):
        self.get_module_args.update({
            'job_id': "be0d099c-a6cf-44e8-88d7-9be80ccae369"
        })
        job_module_mock.module.params = self.get_module_args
        job_module_mock.provisioning.get_job_details = MagicMock(
            return_value=MockJobApi.JOB_DETAILS)
        job_module_mock.perform_module_operation()
        assert self.get_module_args['job_id'] == job_module_mock.module.exit_json.call_args[1]['job_details']['id']
        job_module_mock.provisioning.get_job_details.assert_called()

    def test_get_non_existing_job_details(self, job_module_mock):
        MockApiException.HTTP_ERR = "1"
        MockApiException.err_code = "1"
        MockApiException.status_code = "404"
        self.get_module_args.update({
            'job_id': "non_existing_job",
        })
        job_module_mock.module.params = self.get_module_args
        job_module_mock.provisioning.get_job_details = MagicMock(
            side_effect=MockApiException)
        job_module_mock.perform_module_operation()
        assert MockJobApi.get_non_existing_job_details_failed_msg() in \
            job_module_mock.module.fail_json.call_args[1]['msg']
