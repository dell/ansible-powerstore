.. _job_module:


job -- Manage jobs for PowerStore
=================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing jobs on PowerStore Storage System includes getting details of job.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerStore storage system version 3.0.0.0 or later.
- Ansible-core 2.14 or later.
- PyPowerStore 3.2.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  job_id (True, str, None)
    The ID of the job.


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
   - The *check_mode* is not supported.
   - The modules present in this collection named as 'dellemc.powerstore' are built to support the Dell PowerStore storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get Job Details
      dellemc.powerstore.job:
        array_ip: "{{mgmt_ip}}"
        validate_certs: "{{validate_certs}}"
        user: "{{user}}"
        password: "{{password}}"
        job_id: "a544981c-e94a-40ab-9eae-e578e182d2bb"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


job_details (When job exists., complex, {'description_l10n': 'Modify network parameters.', 'end_time': '2022-01-06T07:39:05.846+00:00', 'estimated_completion_time': None, 'id': 'be0d099c-a6cf-44e8-88d7-9be80ccae369', 'parent_id': None, 'phase': 'Completed', 'phase_l10n': 'Completed', 'progress_percentage': 100, 'resource_action': 'modify', 'resource_action_l10n': 'modify', 'resource_id': 'nw6', 'resource_name': None, 'resource_type': 'network', 'resource_type_l10n': 'network', 'response_body': None, 'response_status': None, 'response_status_l10n': None, 'root_id': 'be0d099c-a6cf-44e8-88d7-9be80ccae369', 'start_time': '2022-01-06T07:39:05.47+00:00', 'state': 'COMPLETED', 'state_l10n': 'Completed', 'step_order': 23792565, 'user': 'admin'})
  The job details.


  id (, str, )
    Unique identifier of the job.


  resource_action (, str, )
    User-specified action to be performed on the given resource.


  resource_type (, str, )
    Resource Type for the given resource.


  resource_id (, str, )
    Unique identifier of the resource on which the job is operating.


  resource_name (, str, )
    Name of the resource on which the job is operating.


  description_l10n (, str, )
    Description of the job.


  state (, str, )
    Current status of the job.


  start_time (, str, )
    Date and time when the job execution started.


  phase (, str, )
    Current status of the job.


  end_time (, str, )
    Date and time when the job execution completed.


  estimated_completion_time (, str, )
    Estimated completion date and time.


  progress_percentage (, int, )
    Percent complete of the job.


  parent_id (, str, )
    Unique identifier of the parent job, if applicable.


  root_id (, str, )
    Unique identifier of the root job, if applicable. The root job is the job at the top of the parent hierarchy.


  response_body (, complex, )
    Base response object.


    response_type (, str, )
      Job error response.


    messages (, complex, )
      The details of the error response.


      code (, str, )
        Hexadecimal code of the error.


      severity (, str, )
        Type of the severity.


      arguments (, list, )
        Values involved in the error.


      message_l10n (, str, )
        The description of the error.




  user (, str, )
    Name of the user associated with the job.


  response_status (, str, )
    Possible HTTP status values of completed or failed jobs.


  step_order (, int, )
    Order of a given job step with respect to its siblings within the job hierarchy.






Status
------





Authors
~~~~~~~

- Akash Shendge (@shenda1) <ansible.team@dell.com>

