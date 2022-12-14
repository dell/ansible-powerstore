# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dell Technologies.

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
          required: True
      verifycert:
          description:
              - Boolean variable to specify whether to validate SSL
                certificate or not.
              - True - indicates that the SSL certificate should be
                       verified. Set the environment variable REQUESTS_CA_BUNDLE
                       to the path of the SSL certificate.
              - False - indicates that the SSL certificate should not be
                        verified.
          type: bool
          required: True
          choices: [True, False]
      user:
          description:
              - The username of the PowerStore host.
          type: str
          required: True
      password:
          description:
              - The password of the PowerStore host.
          type: str
          required: True
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
      - A Dell PowerStore Storage System. Ansible 2.12, 2.13 or 2.14
    notes:
      - The modules present in this collection named as 'dellemc.powerstore'
        are built to support the Dell PowerStore storage platform.
'''
