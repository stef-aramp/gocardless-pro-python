# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources

class PaymentsService(base_service.BaseService):
    RESOURCE_CLASS = resources.Payment
    RESOURCE_NAME = 'payments'

    def create(self, params=None):
        path = '/payments'
        response = self._perform_request('POST', path, params)
        return self._resource_for(response)

    def list(self, params=None):
        path = '/payments'
        response = self._perform_request('GET', path, params)
        return self._resource_for(response)

    def get(self, identity, params=None):
        path = self._sub_url_params('/payments/:identity', {
            'identity': identity,
        })
        response = self._perform_request('GET', path, params)
        return self._resource_for(response)

    def update(self, identity, params=None):
        path = self._sub_url_params('/payments/:identity', {
            'identity': identity,
        })
        response = self._perform_request('PUT', path, params)
        return self._resource_for(response)

    def cancel(self, identity, params=None):
        path = self._sub_url_params('/payments/:identity/actions/cancel', {
            'identity': identity,
        })
        response = self._perform_request('POST', path, params)
        return self._resource_for(response)

    def retry(self, identity, params=None):
        path = self._sub_url_params('/payments/:identity/actions/retry', {
            'identity': identity,
        })
        response = self._perform_request('POST', path, params)
        return self._resource_for(response)

