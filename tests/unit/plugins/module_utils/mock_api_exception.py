# Copyright: (c) 2021, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock ApiException for PowerStore Test modules"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockApiException(Exception):
    HTTP_ERR = "1"
    err_code = "1"
    status_code = "500"
    body = "PyPowerStore Error message"
