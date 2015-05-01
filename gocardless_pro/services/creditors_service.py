# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import base_service
from .. import resources

class CreditorsService(base_service.BaseService):
    RESOURCE_CLASS = resources.Creditor
    RESOURCE_NAME = 'creditors'

    def create(self, params=None):
        path = '/creditors'
        response = self._perform_request('POST', path, params)
        return self._resource_for(response)

    def list(self, params=None):
        path = '/creditors'
        response = self._perform_request('GET', path, params)
        return self._resource_for(response)

    def get(self, identity, params=None):
        path = self._sub_url_params('/creditors/:identity', {
            'identity': identity,
        })
        response = self._perform_request('GET', path, params)
        return self._resource_for(response)

    def update(self, identity, params=None):
        path = self._sub_url_params('/creditors/:identity', {
            'identity': identity,
        })
        response = self._perform_request('PUT', path, params)
        return self._resource_for(response)

