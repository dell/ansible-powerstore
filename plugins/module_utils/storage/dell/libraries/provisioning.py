# Copyright: (c) 2024, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible_collections.dellemc.powerstore.plugins.module_utils.storage.dell \
    import utils

LOG = utils.get_logger('provisioning')


class Provisioning:

    '''Class with shared provisioing operations'''

    def __init__(self, provisioning, module):
        """
        Initialize the provisioing class
        :param provisioing: The provisioing sdk instance
        :param module: Ansible module object
        """
        self.provisioning = provisioning
        self.module = module

    def get_nas_server(self, nas_server_id=None, nas_server_name=None):
        """Get the details of NAS Server of a given Powerstore storage
        system"""
        msg = None

        try:
            log_msg = "Getting NAS Server details id: {0} name " \
                      "{1}".format(nas_server_id, nas_server_name)
            LOG.info(log_msg)
            if nas_server_name:
                nas_details = self.provisioning.get_nas_server_by_name(
                    nas_server_name=nas_server_name)
                if nas_details:
                    nas_details = nas_details[0]
            else:
                nas_details = self.provisioning.get_nas_server_details(
                    nas_server_id=nas_server_id)

            if nas_details:
                log_msg = 'Successfully got NAS Server details {0} '.format(nas_details)
                LOG.info(log_msg)
            else:
                msg = 'Failed to get NAS Server with id {0} or name {1}' \
                      ' from powerstore system'.format(nas_server_id,
                                                       nas_server_name)
            LOG.error(msg)
            return nas_details

        except Exception as e:
            msg = 'Get NAS Server with id {0} or name {1} failed with ' \
                  'error {2} '.format(nas_server_id, nas_server_name, str(e))
            if isinstance(e, utils.PowerStoreException) and \
                    e.err_code == utils.PowerStoreException.HTTP_ERR and \
                    e.status_code == "404":
                LOG.info(msg)
                return None
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))
