.. _remote_support_module:


remote_support -- Remote Support operations on a PowerStore storage system
==========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Performs all Remote Support operations on a PowerStore Storage System. This module supports getting details of an existing Remote Support configuration.

This module also supports modifying an existing Remote Support configuration. Verify a remote support configuration. You can send a test alert through the remote support configuration.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.13 or later.
- PyPowerStore 2.0.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  remote_support_id (True, int, None)
    Unique identifier of the remote support configuration.


  support_type (optional, str, None)
    The type of remote support that is configured.

    Mandatory for modify and verify operation.

    ``SRS_Gateway``, *support_type* is only supported for verify operation.


  remote_support_servers (optional, list, None)
    One or two remote support servers.


    address (True, str, None)
      Gateway server IP address (IPv4).

      The address is a mandatory key.


    port (optional, int, None)
      Gateway server port.


    is_primary (optional, bool, None)
      Indicates whether the server is acting as the primary.

      One server must be set to ``false`` when two servers are configured.



  server_state (optional, str, None)
    Indicates the state of the remote_support_servers.

    Required with *remote_support_servers*.


  is_support_assist_license_accepted (optional, bool, None)
    Indicates whether user has accepted remote support license agreement before enabling the Support Assist on the system for the first time.


  is_cloudiq_enabled (optional, bool, None)
    Indicates whether support for CloudIQ is enabled.


  is_rsc_enabled (optional, bool, None)
    Indicates whether support for Remote Service Credentials is enabled.


  proxy_address (optional, str, None)
    Proxy server IP address (IPv4).


  proxy_port (optional, int, None)
    Proxy server port number.


  proxy_username (optional, str, None)
    User name for proxy server access.


  proxy_password (optional, str, None)
    Password for proxy server access.


  is_icw_configured (optional, bool, None)
    Client already configured ICW.


  verify_connection (optional, bool, False)
    Indicates whether to perform the verify call or not.


  send_test_alert (optional, bool, False)
    Indicates whether to send a test alert or not.


  wait_for_completion (optional, bool, False)
    Flag to indicate if the operation should be run synchronously or asynchronously. ``true`` signifies synchronous execution. By default, modify operation will run asynchronously.


  return_support_license_text (optional, bool, False)
    Indicates whether to return support license agreement text or not.


  state (True, str, None)
    The state of the remote support configuration after the task is performed.

    For Delete operation only, it should be set to ``absent``.

    For get/modify operation it should be set to ``present``.


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
   - Creation and deletion of remote support configuration is not supported.
   - Support for *check_mode* is not available for this module.
   - Verify and send test alert operations do not support idempotency.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    

      - name: Get details of remote support configuration
        dellemc.powerstore.remote_support:
           array_ip: "{{array_ip}}"
           user: "{{user}}"
           password: "{{password}}"
           validate_certs: "{{validate_certs}}"
           remote_support_id: 0
           state: "present"

      - name: Modify remote support configuration - SRS_Gateway_Tier2
        dellemc.powerstore.remote_support:
          array_ip: "{{array_ip}}"
          user: "{{user}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          remote_support_id: 0
          support_type: "SRS_Gateway_Tier2"
          remote_support_servers:
          - address: "10.XX.XX.XX"
            port: 9443
            is_primary: true
          - address: "10.XX.XX.YY"
            port: 9443
            is_primary: false
          server_state: "present-in-server"
          is_rsc_enabled: true
          is_cloudiq_enabled: false
          timeout: 300
          state: "present"

      - name: Modify remote support configuration - SRS_Integrated_Tier2
        dellemc.powerstore.remote_support:
          array_ip: "{{array_ip}}"
          user: "{{user}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          remote_support_id: 0
          support_type: "SRS_Integrated_Tier2"
          proxy_address: "10.XX.XX.ZZ"
          proxy_port: 3128
          proxy_username: "user"
          proxy_password: "password"
          timeout: 300
          state: "present"

      - name: Verify remote support configuration
        dellemc.powerstore.remote_support:
          array_ip: "{{array_ip}}"
          user: "{{user}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          remote_support_id: 0
          support_type: "SRS_Integrated_Tier3"
          timeout: 300
          verify_connection: true
          state: "present"

      - name: Send a test alert
        dellemc.powerstore.remote_support:
           array_ip: "{{array_ip}}"
           user: "{{user}}"
           password: "{{password}}"
           validate_certs: "{{validate_certs}}"
           remote_support_id: 0
           send_test_alert: true
           state: "present"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


job_details (When asynchronous task is performed., complex, {'description_l10n': 'Modify SupportAssist configuration.', 'end_time': '2022-02-24T04:41:56.852+00:00', 'estimated_completion_time': None, 'id': '24e3f881-87f1-49f6-8764-13df4906eb2f', 'parent_id': None, 'phase': 'Completed', 'phase_l10n': 'Completed', 'progress_percentage': 100, 'resource_action': 'modify', 'resource_action_l10n': 'modify', 'resource_id': '0', 'resource_name': None, 'resource_type': 'remote_support', 'resource_type_l10n': 'remote support', 'response_body': None, 'response_status': '204', 'response_status_l10n': '204', 'root_id': '24e3f881-87f1-49f6-8764-13df4906eb2f', 'start_time': '2022-02-24T04:41:38.146+00:00', 'state': 'COMPLETED', 'state_l10n': 'Completed', 'step_order': 64871764, 'user': 'admin'})
  The job details.


  id (, str, )
    The ID of the job.



remote_support_details (When remote support configuration exists., complex, {'connectivity_status': 'Unavailable', 'connectivity_status_l10n': 'Unavailable', 'id': '0', 'is_cloudiq_enabled': True, 'is_rsc_enabled': False, 'is_support_assist_license_accepted': True, 'last_update': '2022-02-11T11:16:39.134+00:00', 'policy_manager_address': None, 'policy_manager_port': None, 'proxy_address': None, 'proxy_port': None, 'proxy_username': None, 'remote_support_servers': [{'address': 'localhost', 'connectivity_qos': [{'appliance_id': 'A1', 'connectivity_qos': 'connectivity_qos', 'connectivity_qos_priority': 2, 'connectivity_qos_value': -1.0, 'id': 'dc326198-2d92-4ff4-a774-324b00ca8818', 'last_update': '2022-02-11T11:16:39.888+00:00', 'remote_support_servers_id': '0'}], 'id': '0', 'is_primary': True, 'port': '9443', 'remote_support_id': '0'}, {'address': 'localhost', 'connectivity_qos': [], 'id': '1', 'is_primary': False, 'port': 'null', 'remote_support_id': '0'}], 'support_assist_license_agreement_text': 'license string', 'type': 'SRS_Integrated_Tier3', 'type_l10n': 'SRS Integrated with Remote Access'})
  Details of the remote support configuration.


  id (, int, )
    Unique identifier of remote support configuration.


  type (, str, )
    The type of remote support that is configured.


  is_cloudiq_enabled (, bool, )
    Indicates whether support for CloudIQ is enabled.


  is_support_assist_license_accepted (, bool, )
    Indicates whether user has accepted remote support license agreement before enabling the Support Assist on the system for the first time.


  support_assist_license_agreement_text (, str, )
    The support assist license agreement text.


  is_rsc_enabled (, bool, )
    Indicates whether support for Remote Service Credentials is enabled.


  proxy_address (, str, )
    Proxy server IP address (IPv4).


  proxy_port (, int, )
    Proxy server port number.


  proxy_username (, str, )
    User name for proxy server access.


  proxy_password (, str, )
    Password for proxy server access.


  remote_support_servers (, complex, )
    Details of two remote support servers.


    id (, str, )
      Unique identifier of the remote support server.


    address (, str, )
      Gateway server IP address (IPv4).


    port (, int, )
      Gateway server port.


    is_primary (, bool, )
      Indicates whether the server is acting as the primary.







Status
------





Authors
~~~~~~~

- Trisha Datta (@Trisha_Datta) <ansible.team@dell.com>

