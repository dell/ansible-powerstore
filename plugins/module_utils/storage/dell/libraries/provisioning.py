# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

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

    def get_nas_server(self, nas_server=None):
        """Get the details of NAS Server of a given Powerstore storage
        system"""

        try:
            msg = 'Getting NAS Server details {0}'.format(nas_server)
            LOG.info(msg)
            id_or_name = utils.name_or_id(val=nas_server)
            LOG.info(id_or_name)
            if id_or_name == "NAME":
                nas_details = self.provisioning.get_nas_server_by_name(
                    nas_server_name=nas_server)
                if nas_details:  # implement in sdk , workaround
                    nas_details = nas_details[0]
            else:
                nas_details = self.provisioning.get_nas_server_details(
                    nas_server_id=nas_server)

            if nas_details:
                msg = f'Successfully got NAS Server details {nas_details}'
                LOG.info(msg)

                return nas_details
            else:
                msg = 'Failed to get NAS Server with id or name {0} from ' \
                      'powerstore system'.format(nas_server)

            self.module.fail_json(msg=msg)

        except Exception as e:
            msg = f'Get NAS Server {nas_server} failed with error {str(e)} '
            LOG.error(msg)
            self.module.fail_json(msg=msg, **utils.failure_codes(e))
