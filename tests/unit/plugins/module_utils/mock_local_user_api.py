# Copyright: (c) 2022, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of Local User module for PowerStore"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockLocalUserApi:
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.utils'

    LOCAL_USER_COMMON_ARGS = {
        'array_ip': '**.***.**.***',
        'user_id': None,
        'user_name': None,
        'user_password': None,
        'new_password': None,
        'role_name': None,
        'role_id': None,
        'is_locked': False,
        'state': None
    }

    LOCAL_USER_1 = "Sample_user"
    LOCAL_USER_DETAILS = {
        "id": "272",
        "is_built_in": False,
        "is_default_password": False,
        "is_locked": False,
        "name": "Sample_user",
        "role_id": "1",
        "role_name": "Administrator"
    }

    CREATE_LOCAL_USER = {
        "id": "272",
        "is_built_in": False,
        "is_default_password": False,
        "is_locked": True,
        "name": "Sample_user",
        "role_id": "1",
        "role_name": "Administrator"
    }

    MODIFY_LOCAL_USER = {
        "id": "272",
        "is_built_in": False,
        "is_default_password": False,
        "is_locked": False,
        "name": "Sample_user",
        "role_id": "4",
        "role_name": "Operator"
    }

    @staticmethod
    def create_local_user_without_role_failed_msg():
        return "user_name and user_password and role details are required to create a local user"

    @staticmethod
    def create_local_user_with_new_password_failed_msg():
        return "new_password is not allowed during creation."

    @staticmethod
    def modify_new_pass_without_user_pass_failed_msg():
        return "user_password along with new_password is required to update password."
