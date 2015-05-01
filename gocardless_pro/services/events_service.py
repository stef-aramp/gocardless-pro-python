# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources

class EventsService(base_service.BaseService):
    RESOURCE_CLASS = resources.Event
    RESOURCE_NAME = 'events'

    def list(self, params=None):
        path = '/events'
        response = self._perform_request('GET', path, params)
        return self._resource_for(response)

    def get(self, identity, params=None):
        path = self._sub_url_params('/events/:identity', {
            'identity': identity,
        })
        response = self._perform_request('GET', path, params)
        return self._resource_for(response)

