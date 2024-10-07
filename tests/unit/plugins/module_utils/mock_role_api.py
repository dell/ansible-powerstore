# Copyright: (c) 2022, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of Role module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockRoleApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerstore.plugins.modules.role.PowerStoreRole'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    ROLE_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'role_id': None,
        'role_name': None,
        'state': None
    }

    ROLE_DETAILS = {
        "description": "Can view status and performance information",
        "id": "1",
        "is_built_in": True,
        "name": "Administrator"
    }

    @staticmethod
    def get_role_failed_msg():
        return "doesn't exist on the PowerStore storage system"

    @staticmethod
    def delete_role_failed_msg():
        return "Deletion of role is not supported by ansible module"
