.. _certificate_module:


certificate -- Certificate operations for PowerStore Storage System
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Supports the provisioning operations on a certificate such as add/import, modify, reset, exchange and get the details of a certificate.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.13 or later.
- PyPowerStore 3.0.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  certificate_id (optional, str, None)
    Unique identifier of the certificate.

    Mandatory only for modify operation.


  certificate_type (optional, str, None)
    Type of the certificate.


  service (optional, str, None)
    Type of the service for which the certificate is used.

    Mandatory for reset and exchange operation.


  scope (optional, str, None)
    Defines a subset of certificates belonging to one service.


  certificate (optional, str, None)
    Concatenated PEM encoded x509_certificate string from end-entity certificate to root certificate.


  remote_address (optional, str, None)
    IPv4 or DNS name of the remote cluster.


  remote_user (optional, str, None)
    The username of the remote cluster.


  remote_password (optional, str, None)
    The password of the remote cluster.


  remote_port (optional, int, None)
    The port address of the remote cluster.


  is_current (optional, bool, None)
    Indicates whether this is the current X509 certificate to be used by the service or this X509 Certificate will be used in the future.


  state (True, str, None)
    Define whether the certificate should exist or not.


  array_ip (True, str, None)
    IP or FQDN of the PowerStore management system.


  validate_certs (optional, bool, True)
    Boolean variable to specify whether to validate SSL certificate or not.

    ``true`` - indicates that the SSL certificate should be verified. Set the environment variable REQUESTS_CA_BUNDLE to the path of the SSL certificate.

    ``false`` - indicates that the SSL certificate should not be verified.


  user (True, str, None)
    The username of the PowerStore host.


  password (True, str, None)
    The password of the PowerStore host.


  timeout (optional, int, 120)
    Time after which the connection will get terminated.

    It is to be mentioned in seconds.


  port (optional, int, None)
    Port number for the PowerStore array.

    If not passed, it will take 443 as default.





Notes
-----

.. note::
   - Idempotency is not supported for adding/importing certificates, exchange of certificates and the reset of certificates.
   - Only *is_current* parameter is supported for modification of certificate.
   - Reset operation can reset more than one certificate at a time.
   - Add/import, modify and reset are supported for PowerStore versions 2.0 and above only.
   - The *check_mode* is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get details of certificate with certificate_id
      dellemc.powerstore.certificate:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        certificate_id: "e940144f-393f-4e9c-8f54-9a4d57b38c48"
        state: "present"

    - name: Reset certificates
      dellemc.powerstore.certificate:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        service: "VASA_HTTP"
        state: "present"

    - name: Exchange certificates
      dellemc.powerstore.certificate:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
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
        validate_certs: "{{validate_certs}}"
        certificate_type: "CA_Client_Validation"
        service: "VASA_HTTP"
        certificate: "{{certificate_string}}"
        is_current: true
        state: "present"

    - name: Modify certificate
      dellemc.powerstore.certificate:
        array_ip: "{{array_ip}}"
        user: "{{user}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        certificate_id: "37b76535-612b-456a-a694-1389f17632c7"
        is_current: true
        state: "present"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


certificate_details (When certificate exists, complex, {'id': '1f0fd938-f122-482a-97b3-72ab1500d007', 'is_current': True, 'is_valid': True, 'members': [{'certificate': 'MIIFejCCA2KgAwIBAgIJAPru9o7dBIwFMA0GCSqGSIb3D QEBCwUAMFcxCzAJBgNVBAYTAlVTMQswCQ', 'depth': 1, 'issuer': 'CN=Dell Technologies PowerStore CA LBSD548W,O=Dell Technologies,ST=MA,C=US', 'key_length': 4096, 'public_key_algorithm': 'SHA256withRSA', 'subject': 'CN=Dell Technologies PowerStore CA LBSD548W,O=Dell Technologies,ST=MA,C=US', 'subject_alternative_names': [], 'thumbprint': '5ff9bc0108dffb0374189d08bc11a6a97eaedac5add511e8a30e7ce283a0ced6', 'thumbprint_algorithm': 'SHA-256', 'thumbprint_algorithm_l10n': 'SHA-256', 'valid_from': '2021-02-02T17:35:29.0Z', 'valid_to': '2026-01-16T17:35:29.0Z'}], 'scope': '1.2.3.4', 'service': 'Management_HTTP', 'service_l10n': 'Management_HTTP', 'type': 'Server', 'type_l10n': 'Server'})
  Details of the certificate.


  id (, str, )
    The system generated ID given to the certificate.


  type (, str, )
    Type of the certificate.


  service (, str, )
    Type of the service for which the certificate is used.


  is_valid (, bool, )
    Indicates whether this is a valid X509 certificate.


  is_current (, bool, )
    Whether the certificate can be used now or not.


  type_l10n (, str, )
    Localized message string corresponding to type.


  service_l10n (, str, )
    Localized message string corresponding to service.


  members (, complex, )
    Member certificates included in this x509_certificate.


    subject (, str, )
      Certificate subject or so called distinguished name.


    serial_number (, str, )
      Certificate serial number.


    signature_algorithm (, str, )
      Certificate signature algorithm.


    issuer (, str, )
      Distinguished name of the certificate issuer.


    valid_from (, str, )
      Date and time when the certificate becomes valid.


    valid_to (, str, )
      Date and time when the certificate will expire.


    subject_alternative_names (, list, )
      Additional DNS names or IP addresses in the x509_certificate.


    public_key_algorithm (, str, )
      Public key algorithm used to generate the key pair.


    key_length (, int, )
      Private key length.


    thumbprint_algorithm (, str, )
      The thumbprint algorithm.


    thumbprint (, str, )
      CeHash value of the certificate.


    certificate (, str, )
      Base64 encoded certificate without any line breaks.


    depth (, str, )
      Depth indicates the position of this member certificate in the X509 Certificate chain.


    thumbprint_algorithm_l10n (, str, )
      Localized message string corresponding to thumbprint_algorithm.







Status
------





Authors
~~~~~~~

- Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>

