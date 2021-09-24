# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)
"""
import PyPowerStore library for PowerStore Storage
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

try:
    import PyPowerStore
    from PyPowerStore import powerstore_conn
    from PyPowerStore.utils.exception import PowerStoreException
    HAS_Py4PS = True
except ImportError:
    HAS_Py4PS = False

'''
check if pkg_resources can be imported or not
'''
try:
    from pkg_resources import parse_version
    import pkg_resources
    PKG_RSRC_IMPORTED = True
except ImportError:
    PKG_RSRC_IMPORTED = False

import logging
import math
from decimal import Decimal
from uuid import UUID

'''
Check required libraries
'''


def has_pyu4ps_sdk():
    error_message = "Ansible modules for Powerstore require the " \
                    "PyPowerStore python library to be installed. " \
                    "Please install the library before using these modules."
    if HAS_Py4PS:
        pyu4ps_sdk = dict(HAS_Py4PS=True, Error_message='')
        return pyu4ps_sdk
    else:
        pyu4ps_sdk = dict(HAS_Py4PS=False, Error_message=error_message)
        return pyu4ps_sdk


'''
Check if required PyPowerStore version installed
'''


def py4ps_version_check():
    try:
        supported_version = False,
        if not PKG_RSRC_IMPORTED:
            unsupported_version_message = "Unable to import " \
                                          "'pkg_resources', please install" \
                                          " the required package"
        else:
            min_ver = '1.3.0'
            curr_version = PyPowerStore.__version__
            unsupported_version_message = "PyPowerStore {0} is not supported " \
                                          "by this module. Minimum supported" \
                                          " version is : {1} " \
                                          "".format(curr_version, min_ver)
            supported_version = parse_version(curr_version) >= parse_version(min_ver)

        if supported_version:
            py4ps_version = dict(supported_version=supported_version,
                                 unsupported_version_message='')
        else:
            py4ps_version = dict(
                supported_version=supported_version,
                unsupported_version_message=unsupported_version_message)

        return py4ps_version

    except Exception as e:
        unsupported_version_message = "Unable to get the PyPowerStore" \
                                      " version, failed with Error {0} "\
            .format(str(e))
        py4ps_version = dict(
            supported_version=False,
            unsupported_version_message=unsupported_version_message)
        return py4ps_version


def get_powerstore_management_host_parameters():
    return dict(
        user=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        array_ip=dict(type='str', required=True),
        verifycert=dict(type='bool', required=True, choices=[True, False])
    )


def get_powerstore_connection(module_params, application_type=None,
                              timeout=None, enable_log=False):
    if HAS_Py4PS:
        conn = PyPowerStore.powerstore_conn.PowerStoreConn(
            server_ip=module_params['array_ip'],
            username=module_params['user'],
            password=module_params['password'],
            verify=module_params['verifycert'],
            application_type=application_type,
            timeout=timeout, enable_log=enable_log)
        return conn


def name_or_id(val):
    """Determines if the input value is a name or id"""
    try:
        UUID(str(val))
        return "ID"
    except ValueError:
        return "NAME"


def get_logger(module_name, log_file_name='dellemc_ansible_provisioning.log',
               log_devel=logging.INFO):
    FORMAT = '%(asctime)-15s %(filename)s %(levelname)s : %(message)s'
    logging.basicConfig(filename=log_file_name, format=FORMAT)
    LOG = logging.getLogger(module_name)
    LOG.setLevel(log_devel)
    return LOG


'''
Convert the given size to bytes
'''
KB_IN_BYTES = 1024
MB_IN_BYTES = 1024 * 1024
GB_IN_BYTES = 1024 * 1024 * 1024
TB_IN_BYTES = 1024 * 1024 * 1024 * 1024


def get_size_bytes(size, cap_units):
    if size is not None and size > 0:
        if cap_units in ('kb', 'KB'):
            return size * KB_IN_BYTES
        elif cap_units in ('mb', 'MB'):
            return size * MB_IN_BYTES
        elif cap_units in ('gb', 'GB'):
            return size * GB_IN_BYTES
        elif cap_units in ('tb', 'TB'):
            return size * TB_IN_BYTES
        else:
            return size
    else:
        return 0


'''
Convert size in byte with actual unit like KB,MB,GB,TB,PB etc.
'''


def convert_size_with_unit(size_bytes):
    if not isinstance(size_bytes, int):
        raise ValueError('This method takes Integer type argument only')
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


'''
Convert the given size to size in GB, size is restricted to 2 decimal places
'''


def get_size_in_gb(size, cap_units):
    size_in_bytes = get_size_bytes(size, cap_units)
    size = Decimal(size_in_bytes / GB_IN_BYTES)
    size_in_gb = round(size, 2)
    return size_in_gb
