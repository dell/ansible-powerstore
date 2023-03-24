# Copyright: (c) 2023, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of vCenter module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockVCenterApi:
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'
    SAMPLE_ADDRESS = "xx.xx.xx.xx"
    SAMPLE_ADDRESS1 = "xx.xx.xx.xy"
    USERNAME_1 = "user_1"
    USERNAME_2 = "user_2"
    PASS_STR = "vCenter_pass"
    ID_1 = "434f534e-7009-4e60-8e1e-5cf721ae40df"

    VCENTER_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'vcenter_id': None,
        'address': None,
        'vcenter_username': None,
        'vcenter_password': None,
        'vasa_provider_credentials': None,
        'delete_vasa_provider': None,
        'update_password': None,
        'state': None
    }

    VCENTER_DETAILS_1 = {
        "id": ID_1,
        "instance_uuid": ID_1,
        "address": SAMPLE_ADDRESS,
        "username": USERNAME_1,
        "version": "7.0.3",
        "vendor_provider_status": "Not_Registered",
        "vendor_provider_status_l10n": "Not Registered",
        "virtual_machines": [],
        "datastores": [],
        "vsphere_hosts": []
    }

    VCENTER_DETAILS_2 = [{
        "id": ID_1,
        "instance_uuid": ID_1,
        "address": SAMPLE_ADDRESS1,
        "username": USERNAME_2,
        "version": "7.0.3",
        "vendor_provider_status": "Online",
        "vendor_provider_status_l10n": "Online",
        "virtual_machines": [],
        "datastores": [],
        "vsphere_hosts": []
    }]

    @staticmethod
    def invalid_param_failed_msg():
        return "Provide the valid address"

    @staticmethod
    def add_vcenter_without_param_failed_msg():
        return "address, vcenter_username and vcenter_password must be " \
               "passed to add a vCenter"

    @staticmethod
    def get_vcenter_exception_failed_msg():
        return "Get details of vCenter: %s failed with " \
               "error" % MockVCenterApi.ID_1

    @staticmethod
    def modify_vcenter_exception_failed_msg():
        return "Modification of vCenter %s failed with error" % \
               MockVCenterApi.ID_1

    @staticmethod
    def remove_vcenter_exception_failed_msg():
        return "Deletion of vCenter %s failed with error" % MockVCenterApi.ID_1
