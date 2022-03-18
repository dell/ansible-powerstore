#!/usr/bin/python
# Copyright: (c) 2021, Dell EMC
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

""" Ansible module for managing certificates on PowerStore"""
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: certificate
version_added: '1.4.0'
short_description: Certificate operations on PowerStore Storage System
description:
- Supports the provisioning operations on a Certificate such as add/import, modify,
  reset, exchange and get the details of a certificate.

extends_documentation_fragment:
  - dellemc.powerstore.dellemc_powerstore.powerstore

author:
- Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>

options:
  certificate_id:
    description:
    - Unique identifier of the certificate.
    - Mandatory only for modify operation.
    type: str
  certificate_type:
    description:
    - Type of the certificate.
    choices: ['Server', 'Client', 'CA_Client_Validation', 'CA_Server_Validation']
    type: str
  service:
    description:
    - Type of the service for which the certificate is used.
    - Mandatory for reset and exchange operation.
    choices: ['Management_HTTP', 'Replication_HTTP', 'VASA_HTTP', 'Import_HTTP', 'LDAP_HTTP', 'Syslog_HTTP']
    type: str
  scope:
    description:
    - Defines a subset of certificates belonging to one Service.
    type: str
  certificate:
    description:
    - Concatenated PEM encoded x509_certificate string from end-entity
      certificate to root certificate.
    type: str
  remote_address:
    description:
    - IPv4 or DNS name of the remote cluster.
    type: str
  remote_user:
    description:
    - The username of the remote cluster.
    type: str
  remote_password:
    description:
    - The password of the remote cluster.
    type: str
  remote_port:
    description:
    - The port address of the remote cluster.
    type: int
  is_current:
    description:
    - Indicates whether this is the current X509 certificate to be used
      by the service or this X509 Certificate will be used in the future.
    type: bool
  state:
    description:
    - Define whether the certificate should exist or not.
    choices: ['absent', 'present']
    required: True
    type: str

notes:
- Idempotency is not supported for adding/importing certificates, exchange of certificates and the reset of certificates.
- Only is_current parameter is supported for modification of certificate.
- Reset operation can reset more than one certificate at a time.
- Add/import, modify and reset are supported for PowerStore versions 2.0 and above only.
- The check_mode is not supported.
'''

EXAMPLES = r'''
- name: Get details of certificate with certificate_id
  dellemc.powerstore.certificate:
    array_ip: "{{array_ip}}"
    user: "{{user}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    certificate_id: "e940144f-393f-4e9c-8f54-9a4d57b38c48"
    state: "present"

- name: Reset certificates
  dellemc.powerstore.certificate:
    array_ip: "{{array_ip}}"
    user: "{{user}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    service: "VASA_HTTP"
    state: "present"

- name: Exchange certificates
  dellemc.powerstore.certificate:
    array_ip: "{{array_ip}}"
    user: "{{user}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    service: "Replication_HTTP"
    remote_address: "{{remote_array_ip}}"
    remote_port: 443
    remote_user: "{{remote_user}}"
    remote_password: "{{remote_password}}"
    state: "present"

- name: Add/import a certificate
  dellemc.powerstore.certificate:
    array_ip: "{{array_ip}}"
    user: "{{user}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    certificate_type: "CA_Client_Validation"
    service: "VASA_HTTP"
    certificate: "{{certificate_string}}"
    is_current: True
    state: "present"

- name: Modify certificate
  dellemc.powerstore.certificate:
    array_ip: "{{array_ip}}"
    user: "{{user}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    certificate_id: "37b76535-612b-456a-a694-1389f17632c7"
    is_current: True
    state: "present"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"
certificate_details:
    description: Details of the certificate.
    returned: When certificate exists
    type: complex
    contains:
        id:
            description: The system generated ID given to the certificate.
            type: str
        type:
            description: Type of the certificate.
            type: str
        service:
            description: Type of the service for which the certificate is used.
            type: str
        is_valid:
            description: Indicates whether this is a valid X509 certificate.
            type: bool
        is_current:
            description: Whether the certificate can be used now or not.
            type: bool
        type_l10n:
            description: Localized message string corresponding to type.
            type: str
        service_l10n:
            description: Localized message string corresponding to service.
            type: str
        members:
            description: Member certificates included in this x509_certificate.
            type: complex
            contains:
                subject:
                    description: Certificate subject or so called distinguished name.
                    type: str
                serial_number:
                    description: Certificate serial number.
                    type: str
                signature_algorithm:
                    description: Certificate signature algorithm.
                    type: str
                issuer:
                    description: Distinguished name of the certificate issuer.
                    type: str
                valid_from:
                    description: Date and time when the certificate becomes valid.
                    type: str
                valid_to:
                    description: Date and time when the certificate will expire.
                    type: str
                subject_alternative_names:
                    description: Additional DNS names or IP addresses in the x509_certificate.
                    type: list
                public_key_algorithm:
                    description: Public key algorithm used to generate the key pair.
                    type: str
                key_length:
                    description: Private key length.
                    type: int
                thumbprint_algorithm:
                    description: The thumbprint algorithm.
                    type: str
                thumbprint:
                    description: CeHash value of the certificate.
                    type: str
                certificate:
                    description: Base64 encoded certificate without any line breaks.
                    type: str
                depth:
                    description: Depth indicates the position of this member certificate
                                 in the X509 Certificate chain.
                    type: str
                thumbprint_algorithm_l10n:
                    description: Localized message string corresponding to thumbprint_algorithm.
                    type: str
    sample: {
        "id": "1f0fd938-f122-482a-97b3-72ab1500d007",
        "is_current": true,
        "is_valid": true,
        "members": [
            {
                "certificate": "MIIFejCCA2KgAwIBAgIJAPru9o7dBIwFMA0GCSqGSIb3D
                                QEBCwUAMFcxCzAJBgNVBAYTAlVTMQswCQ",
                "depth": 1,
                "issuer": "CN=Dell EMC PowerStore CA LBSD548W,O=Dell EMC,ST=MA,C=US",
                "key_length": 4096,
                "public_key_algorithm": "SHA256withRSA",
                "subject": "CN=Dell EMC PowerStore CA LBSD548W,O=Dell EMC,ST=MA,C=US",
                "subject_alternative_names": [],
                "thumbprint": "5ff9bc0108dffb0374189d08bc11a6a97eaedac5add511e8a30e7ce283a0ced6",
                "thumbprint_algorithm": "SHA-256",
                "thumbprint_algorithm_l10n": "SHA-256",
                "valid_from": "2021-02-02T17:35:29.0Z",
                "valid_to": "2026-01-16T17:35:29.0Z"
            }
        ],
        "scope": "1.2.3.4",
        "service": "Management_HTTP",
        "service_l10n": "Management_HTTP",
        "type": "Server",
        "type_l10n": "Server"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell\
    import dellemc_ansible_powerstore_utils as utils

LOG = utils.get_logger('certificate')

py4ps_sdk = utils.has_pyu4ps_sdk()
HAS_PY4PS = py4ps_sdk['HAS_Py4PS']
IMPORT_ERROR = py4ps_sdk['Error_message']

py4ps_version = utils.py4ps_version_check()
IS_SUPPORTED_PY4PS_VERSION = py4ps_version['supported_version']
VERSION_ERROR = py4ps_version['unsupported_version_message']

# Application type
APPLICATION_TYPE = 'Ansible/1.5.0'


class PowerStoreCertificate(object):
    """Certificate operations"""
    cluster_name = None
    cluster_global_id = None

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powerstore_management_host_parameters()
        self.module_params.update(get_powerstore_certificate_parameters())

        required_together = [['remote_user', 'remote_password', 'remote_address', 'remote_port']]
        required_one_of = [['service', 'certificate_id']]
        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            required_together=required_together,
            required_one_of=required_one_of
        )
        msg = 'HAS_PY4PS = {0} , IMPORT_ERROR = ' \
              '{1}'.format(HAS_PY4PS, IMPORT_ERROR)
        LOG.info(msg)
        if HAS_PY4PS is False:
            self.module.fail_json(msg=IMPORT_ERROR)
        msg = 'IS_SUPPORTED_PY4PS_VERSION = {0} , ' \
              'VERSION_ERROR = {1}'.format(IS_SUPPORTED_PY4PS_VERSION,
                                           VERSION_ERROR)
        LOG.info(msg)
        if IS_SUPPORTED_PY4PS_VERSION is False:
            self.module.fail_json(msg=VERSION_ERROR)

        self.conn = utils.get_powerstore_connection(
            self.module.params,
            application_type=APPLICATION_TYPE)
        self.configuration = self.conn.config_mgmt
        msg = 'Got Py4ps instance for configuration on' \
              ' PowerStore {0}'.format(self.configuration)
        LOG.info(msg)

    def get_certificate_details(self, certificate_id):
        """Get the details of a certificate on a PowerStore storage system"""

        try:
            msg = 'Getting Certificate Details with certificate_id {0}, ' \
                ''.format(certificate_id)
            LOG.info(msg)
            certi_details = None
            certi_details = self.configuration.get_certificate_details(certificate_id)

            msg = 'Successfully Got Certificate Details {0}'.format(certi_details)

            LOG.info(msg)
            return certi_details
        except Exception as e:
            msg = 'Get certificate details for PowerStore array name : ' \
                  '{0} , global id : {1} failed with error' \
                  ' {2} '.format(self.cluster_name, self.cluster_global_id,
                                 str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR \
                    and e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def reset_certificates(self, service):
        """Resets certificate of a service"""
        try:
            LOG.info("Attempting to reset certificates with service %s", service)
            reset_cert_dict = dict()
            reset_cert_dict['service'] = service
            self.configuration.reset_certificates(reset_cert_dict=reset_cert_dict)
            LOG.info("Successfully reset certificates with service: %s", service)

        except Exception as e:
            msg = 'Resetting certificates with service {0} on PowerStore array ' \
                  'name : {1} , global id : {2} failed with ' \
                  'error {3} '.format(service, self.cluster_name,
                                      self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def exchange_certificate(self, service, remote_address, remote_port, remote_user, remote_password):
        """Exchange certificate of a service"""
        try:
            LOG.info("Attempting to exchange certificates with service %s", service)
            exchange_cert_dict = dict()
            exchange_cert_dict['service'] = service
            exchange_cert_dict['address'] = remote_address
            exchange_cert_dict['port'] = remote_port
            exchange_cert_dict['username'] = remote_user
            exchange_cert_dict['password'] = remote_password
            self.configuration.exchange_certificate(exchange_cert_dict=exchange_cert_dict)

            LOG.info("Successfully exchanged certificates with service: %s", service)

        except Exception as e:
            msg = 'Exchanging certificates with remote array {0} on PowerStore array ' \
                  'name : {1} , global id : {2} failed with ' \
                  'error {3} '.format(service, self.cluster_name, self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def create_certificate(self, certificate_type, service, certificate, is_current=None, scope=None):
        """Create a certificate."""
        try:
            LOG.info("Attempting to create certificate")
            create_cert_dict = dict()
            create_cert_dict['type'] = certificate_type
            create_cert_dict['service'] = service
            create_cert_dict['scope'] = scope
            create_cert_dict['certificate'] = certificate
            create_cert_dict['is_current'] = is_current

            resp = self.configuration.create_certificate(create_cert_dict=create_cert_dict)
            LOG.info(resp)
            crt_details = None

            if resp:
                crt_details = self.get_certificate_details(certificate_id=resp['id'])
                LOG.info("Successfully Created certificate with details : %s", crt_details)
                return crt_details

        except Exception as e:
            msg = 'Create certificate on PowerStore array ' \
                  'name : {0} , global id : {1} failed with ' \
                  'error {2} '.format(self.cluster_name, self.cluster_global_id, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def is_modify_required(self, cert_details):
        """To get the details of the field to be modified."""

        try:
            LOG.info("Certificate details: %s", cert_details)
            modify_dict = dict()
            is_current = self.module.params['is_current']
            if is_current is not None\
                    and cert_details['is_current'] != is_current:
                modify_dict['is_current'] = is_current

            if modify_dict:
                return modify_dict
            else:
                return None

        except Exception as e:
            msg = 'Failed to determine if certificate instance needs ' \
                  'to be modified with error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def modify_certificate(self, certificate_id, modify_params, cert_details):
        """Perform modify operations on a certificate"""

        try:
            self.configuration.modify_certificate(certificate_id=certificate_id,
                                                  modify_cert_dict=modify_params)
            return True
        except Exception as e:
            msg = 'Failed to modify certificate instance ' \
                  'with error {0}'.format(str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))

    def perform_module_operation(self):
        """ Perform various module operations"""

        certificate_id = self.module.params['certificate_id']
        certificate_type = self.module.params['certificate_type']
        service = self.module.params['service']
        scope = self.module.params['scope']
        certificate = self.module.params['certificate']
        is_current = self.module.params['is_current']
        remote_address = self.module.params['remote_address']
        remote_port = self.module.params['remote_port']
        remote_user = self.module.params['remote_user']
        remote_password = self.module.params['remote_password']
        state = self.module.params['state']

        # result is a dictionary to contain end state and certificate details
        changed = False
        result = dict(
            changed=False,
            certificate_details=None
        )

        modify_params = None
        certi_details = self.get_certificate_details(certificate_id=certificate_id)
        if certi_details:
            modify_params = self.is_modify_required(cert_details=certi_details)

        if state == 'absent' and certi_details:
            msg = 'Deletion of certificate is not supported through Ansible Module'
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        if not certi_details and state == 'present':
            if service:
                if certificate_type and certificate:
                    certi_details = self.create_certificate(certificate_type=certificate_type,
                                                            service=service,
                                                            certificate=certificate,
                                                            is_current=is_current, scope=scope)
                    changed = True

                if remote_address and remote_port and remote_user and remote_password:
                    self.exchange_certificate(service=service,
                                              remote_address=remote_address,
                                              remote_port=remote_port,
                                              remote_user=remote_user,
                                              remote_password=remote_password)
                    changed = True
                elif (not certificate_type and not scope and not certificate and not is_current
                      and not remote_address and not remote_port and not remote_user and not remote_password):
                    self.reset_certificates(service=service)
                    changed = True
                elif not certificate_type or not certificate:
                    msg = "certificate_type, service, and certificate are required to create a certificate"
                    LOG.error(msg)
                    self.module.fail_json(msg=msg)

            if not service:
                msg = " Please provide valid/existing certificate_id "
                LOG.error(msg)
                self.module.fail_json(msg=msg)

        if state == 'present' and certi_details:
            if certificate:
                msg = 'Modification of certificate string is not supported through Ansible Module'
                LOG.error(msg)
                self.module.fail_json(msg=msg)
            elif modify_params:
                LOG.info('attempting to modify certificate with id %s', certi_details.get("id"))
                changed = self.modify_certificate(certificate_id=certi_details.get("id"),
                                                  modify_params=modify_params, cert_details=certi_details)
                certi_details = self.get_certificate_details(certi_details.get("id"))
            else:
                result['certificate_details'] = certi_details
        result['changed'] = changed
        self.module.exit_json(**result)


def get_powerstore_certificate_parameters():
    """This method provides the parameters required for the ansible
    certificate modules on PowerStore"""
    return dict(
        certificate_id=dict(),
        certificate_type=dict(choices=['Server', 'Client', 'CA_Client_Validation', 'CA_Server_Validation']),
        service=dict(choices=['Management_HTTP', 'Replication_HTTP', 'VASA_HTTP', 'Import_HTTP', 'LDAP_HTTP', 'Syslog_HTTP']),
        scope=dict(),
        certificate=dict(),
        is_current=dict(type='bool'),
        remote_address=dict(),
        remote_port=dict(type='int'),
        remote_user=dict(no_log=True),
        remote_password=dict(no_log=True),
        state=dict(required=True, choices=['present', 'absent'])
    )


def main():
    """ Create PowerStore certificate object and perform action on it
        based on user input from playbook """
    obj = PowerStoreCertificate()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
