
'''import PyU4V library for Powermax Storage'''
try:
    import PyU4V
    HAS_PYU4V = True
except ImportError:
    HAS_PYU4V = False

'''import ISI library for Isilon Storage'''
try:
    import isi_sdk_8_1_1 as isi_sdk
    from isi_sdk_8_1_1.rest import ApiException
    HAS_ISILON_SDK = True
except ImportError:
    HAS_ISILON_SDK = False

'''import PyPowerStore library for PowerStore Storage'''
try:
    import PyPowerStore
    from PyPowerStore import powerstore_conn
    HAS_Py4PS = True
except ImportError:
    HAS_Py4PS = False

'''import pkg_resources'''
try:
    from pkg_resources import parse_version
    import pkg_resources
    PKG_RSRC_IMPORTED = True
except ImportError:
    PKG_RSRC_IMPORTED = False

import logging
import urllib3
urllib3.disable_warnings()
from decimal import Decimal

'''
Check required libraries
'''


def has_pyu4v_sdk():
    return HAS_PYU4V

def has_isilon_sdk():
    return HAS_ISILON_SDK

def get_isilon_sdk():
    return isi_sdk


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
            min_ver = '1.1.0'
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


'''
Check if required PyU4V version installed
'''


def pyu4v_version_check():
    try:
        if not PKG_RSRC_IMPORTED:
            err_msg = "Unable to import 'pkg_resources', please install " \
                      "the required package"
            return err_msg
        min_ver = '3.0.0.14'
        curr_version = PyU4V.__version__
        unsupported_version_message = "PyU4V {0} is not supported by this module.Minimum supported version is : " \
                                      "{1} ".format(curr_version, min_ver)
        supported_version = parse_version(curr_version) >= parse_version(min_ver)
        if supported_version is False:
            return unsupported_version_message
        else:
            return None
    except Exception as e:
        unsupported_version_message = "Unable to get the PyU4V version, failed with Error {0} ".format(
            str(e))
        return unsupported_version_message


'''Check if valid Unisphere Version'''


def universion_check(universion):
    is_valid_universion = False
    user_message = ""

    try:
        if universion == 91:
            user_message = "Specify universion as \"90\" even" \
                           " if the Unisphere version is 9.1"

        elif universion == 90:
            is_valid_universion = True

        else:
            user_message = "Unsupported unisphere version , please " \
                           "specify universion as \"90\""

        universion_details = {"is_valid_universion": is_valid_universion,
                              "user_message": user_message}
        return universion_details

    except Exception as e:
        is_valid_universion = False
        user_message = "Failed to validate the Unisphere version " \
                       "with error {0}".format(str(e))

        universion_details = {"is_valid_universion": is_valid_universion,
                              "user_message": user_message}
        return universion_details



'''
This method provide parameter required for the ansible modules on PowerMax
options:
  unispherehost:
    description:
    - IP/FQDN of unisphere host.
    required: true
  universion:
    description:
    - Version of univmax SDK.
  verifycert:
    description:
    - Boolean value to inform system whether to verify client certificate or not.
  user:
    description:
    - User name to access on to unispherehost
  password:
    description:
    - password to access on to unispherehost
  serial_no:
    description:
    - Serial number of Powermax system    
    
'''


def get_powermax_management_host_parameters():
    return dict(
        unispherehost=dict(type='str', required=True),
        universion=dict(type='int', required=True),
        verifycert=dict(type='bool', required=True),
        user=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        serial_no=dict(type='str', required=True)
    )


def get_powerstore_management_host_parameters():
    return dict(
        user=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        array_ip=dict(type='str', required=True),
        verifycert=dict(type='bool', required=True)
    )


def get_powerstore_connection(module_params, application_type=None,
                              timeout=None):
    if HAS_Py4PS:
        conn = PyPowerStore.powerstore_conn.PowerStoreConn(server_ip=module_params['array_ip'],
                                              username=module_params['user'],
                                              password=module_params['password'],
                                              verify=module_params['verifycert'],
                                              application_type=application_type,
                                              timeout=timeout)
        return conn

    

'''
This method is to establish connection to PowerMax
using PyU4v SDK.

parameters:
  module_params - Ansible module parameters which contain below unisphere details
                 to establish connection on to Unisphere
     - unispherehost: IP/FQDN of unisphere host.
     - universion:Version of univmax SDK.
     - verifycert: Boolean value to inform system whether to verify client certificate or not.
     - user:  User name to access on to unispherehost
     - password: Password to access on to unispherehost
     - serial_no: Serial number of Powermax system
returns connection object to access provisioning and protection sdks
'''


def get_U4V_connection(module_params, application_type=None):
    if HAS_PYU4V:
        conn = PyU4V.U4VConn(server_ip=module_params['unispherehost'],
                             port=8443,
                             array_id=module_params['serial_no'],
                             verify=module_params['verifycert'],
                             username=module_params['user'],
                             password=module_params['password'],
                             u4v_version=module_params['universion'],
                             application_type=application_type)
        return conn


'''
This method is to establish connection to PowerMax Unisphere
using PyU4v SDK.

parameters:
  module_params - Ansible module parameters which contain below unisphere 
                  details to establish connection on to Unisphere
     - unispherehost: IP/FQDN of unisphere host.
     - universion:Version of univmax SDK.
     - verifycert: Boolean value to inform system whether to verify client 
                   certificate or not.
     - user:  User name to access on to unispherehost
     - password: Password to access on to unispherehost     
  application_type - application tagging header
returns connection object to access U4V Unisphere Common sdks
'''


def get_u4v_unisphere_connection(module_params, application_type=None):

    if HAS_PYU4V:

        conn = PyU4V.U4VConn(server_ip=module_params['unispherehost'],
                             port=8443,
                             verify=module_params['verifycert'],
                             username=module_params['user'],
                             password=module_params['password'],
                             u4v_version=module_params['universion'],
                             application_type=application_type)
        return conn

'''
Check if required Isilon SDK version is installed
'''


def isilon_sdk_version_check():
    try:
        if not PKG_RSRC_IMPORTED:
            err_msg = "Unable to import 'pkg_resources', please install " \
                      "the required package"
            return err_msg
        supported_version = False
        min_ver = '0.2.7'
        curr_version = pkg_resources.require("isi-sdk-8-1-1")[0].version
        unsupported_version_message = "isilon sdk {0} is not supported by this module.Minimum supported version is : " \
                                      "{1} ".format(curr_version, min_ver)
        supported_version = parse_version(curr_version) >= parse_version(
            min_ver)
        if supported_version is False:
            return unsupported_version_message
        else:
            return None
    except Exception as e:
        unsupported_version_message = "Unable to get the isilon sdk version, failed with Error {0} ".format(
            str(e))
        return unsupported_version_message

'''
This method provides common access parameters required for the Ansible Modules on Isilon
options:
  onefshost:
    description:
    - IP of the Isilon OneFS host
    required: true
  port_no:
    decription:
    - The port number through which all the requests will be addressed by the OneFS host.
  verifyssl:
    description:
    - Boolean value to inform system whether to verify ssl certificate or not.
  api_user:
    description:
    - User name to access OneFS
  api_password:
    description:
    - password to access OneFS
'''


def get_isilon_management_host_parameters():
    return dict(
        onefs_host=dict(type='str', required=True),
        verify_ssl=dict(type='bool', required=True),
        port_no=dict(type='str'),
        api_user=dict(type='str', required=True),
        api_password=dict(type='str', required=True, no_log=True)
    )


'''
This method is to establish connection to Isilon
using its SDK.
parameters:
  module_params - Ansible module parameters which contain below OneFS details
                 to establish connection on to OneFS
     - onefshost: IP of OneFS host.
     - verifyssl: Boolean value to inform system whether to verify ssl certificate or not.
     - port_no: The port no of the OneFS host.
     - username:  Username to access OneFS
     - password: Password to access OneFS
returns configuration object 
'''


def get_isilon_connection(module_params):
    if HAS_ISILON_SDK:
        conn = isi_sdk.Configuration()
        if module_params['port_no'] is not None:
            conn.host = module_params['onefs_host'] + ":" + module_params[
                'port_no']
        else:
            conn.host = module_params['onefs_host']
        conn.verify_ssl = module_params['verify_ssl']
        conn.username = module_params['api_user']
        conn.password = module_params['api_password']
        api_client = isi_sdk.ApiClient(conn)
        return api_client


'''
This method is to initialize logger and return the logger object 

parameters:
     - module_name: Name of module to be part of log message.
     - log_file_name: name of the file in which the log meessages get appended.
     - log_devel: log level.
returns logger object 
'''


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
MB_IN_BYTES = 1024*1024
GB_IN_BYTES = 1024*1024*1024
TB_IN_BYTES = 1024*1024*1024*1024


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
Convert the given size to size in GB, size is restricted to 2 decimal places
'''


def get_size_in_gb(size, cap_units):
    size_in_bytes = get_size_bytes(size, cap_units)
    size = Decimal(size_in_bytes / GB_IN_BYTES)
    size_in_gb = round(size, 2)
    return size_in_gb
