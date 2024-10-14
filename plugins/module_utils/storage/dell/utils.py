# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Copyright: (c) 2024, Dell Technologies
"""
import PyPowerStore library for PowerStore Storage
"""
from __future__ import (absolute_import, division, print_function)
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell.logging_handler \
    import CustomRotatingFileHandler

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
    PKG_RSRC_IMPORTED = True
except ImportError:
    PKG_RSRC_IMPORTED = False

import logging
import math
from decimal import Decimal
from uuid import UUID
from datetime import datetime

# Application type
APPLICATION_TYPE = 'Ansible/3.4.0'

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
        supported_version = False
        if not PKG_RSRC_IMPORTED:
            unsupported_version_message = "Unable to import 'pkg_resources'," \
                                          " please install the required" \
                                          " package"
        else:
            min_ver = '3.3.0'
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
        port=dict(type='int', required=False),
        timeout=dict(type='int', required=False, default=120),
        validate_certs=dict(type='bool', required=False,
                            aliases=['verifycert'], default=True)
    )


def get_powerstore_connection(module_params, application_type=APPLICATION_TYPE,
                              enable_log=False):
    if HAS_Py4PS:
        conn = powerstore_conn.PowerStoreConn(
            server_ip=module_params['array_ip'],
            username=module_params['user'],
            password=module_params['password'],
            verify=module_params['validate_certs'],
            timeout=module_params['timeout'],
            application_type=application_type,
            port_no=module_params['port'],
            enable_log=enable_log)
        return conn


def name_or_id(val):
    """Determines if the input value is a name or id"""
    try:
        UUID(str(val))
        return "ID"
    except ValueError:
        return "NAME"


def get_logger(module_name, log_file_name='ansible_powerstore.log', log_devel=logging.INFO):
    FORMAT = '%(asctime)-15s %(filename)s %(levelname)s : %(message)s'
    max_bytes = 5 * 1024 * 1024
    logging.basicConfig(filename=log_file_name, format=FORMAT)
    LOG = logging.getLogger(module_name)
    LOG.setLevel(log_devel)
    handler = CustomRotatingFileHandler(log_file_name, maxBytes=max_bytes, backupCount=5)
    formatter = logging.Formatter(FORMAT)
    handler.setFormatter(formatter)
    LOG.addHandler(handler)
    LOG.propagate = False
    return LOG


'''
Convert the given size to bytes
'''
KB_IN_BYTES = 1024
MB_IN_BYTES = 1024 * 1024
GB_IN_BYTES = 1024 * 1024 * 1024
TB_IN_BYTES = 1024 * 1024 * 1024 * 1024
PB_IN_BYTES = 1024 * 1024 * 1024 * 1024 * 1024


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
        elif cap_units in ('Pb', 'PB'):
            return size * PB_IN_BYTES
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


'''
returns a dictionary of error_code and status_code if the exception is of PowerstoreExcpetion type
'''


def failure_codes(exception):
    codes = {}
    if isinstance(exception, PowerStoreException):
        codes = dict({'error_code': exception.err_code, 'status_code': exception.status_code})
    return codes


def validate_timestamp(expiration_timestamp):
    """Validates whether the timestamp is valid"""
    try:
        datetime.strptime(expiration_timestamp,
                          '%Y-%m-%dT%H:%M:%SZ')
        return True
    except ValueError:
        return False


'''
Validate whether param is empty or not
'''


def is_param_empty(param):
    if param is not None and (param.count(" ") > 0 or len(param.strip()) == 0):
        return True
