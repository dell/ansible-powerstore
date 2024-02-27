# Copyright: (c) 2024, Dell Technologies.
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class ModuleDocFragment(object):
    # Documentation fragment for PowerStore (powerstore)
    DOCUMENTATION = r'''
    options:
      array_ip:
          description:
              - IP or FQDN of the PowerStore management system.
          type: str
          required: true
      validate_certs:
          description:
              - Boolean variable to specify whether to validate SSL
                certificate or not.
              - C(true) - indicates that the SSL certificate should be
                       verified. Set the environment variable REQUESTS_CA_BUNDLE
                       to the path of the SSL certificate.
              - C(false) - indicates that the SSL certificate should not be
                        verified.
          type: bool
          default: true
          aliases:
              - verifycert
      user:
          description:
              - The username of the PowerStore host.
          type: str
          required: true
      password:
          description:
              - The password of the PowerStore host.
          type: str
          required: true
      timeout:
          description:
              - Time after which the connection will get terminated.
              - It is to be mentioned in seconds.
          type: int
          default: 120
      port:
          description:
              - Port number for the PowerStore array.
              - If not passed, it will take 443 as default.
          type: int
    requirements:
      - A Dell PowerStore storage system version 3.0.0.0 or later.
      - Ansible-core 2.13 or later.
      - PyPowerStore 3.2.0.
      - Python 3.9, 3.10 or 3.11.
    notes:
      - The modules present in this collection named as 'dellemc.powerstore'
        are built to support the Dell PowerStore storage platform.
'''
