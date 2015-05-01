# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import base_service
from .. import resources

class CustomerBankAccountsService(base_service.BaseService):
    RESOURCE_CLASS = resources.CustomerBankAccount
    RESOURCE_NAME = 'customer_bank_accounts'

    def create(self, params=None):
        path = '/customer_bank_accounts'
        response = self._perform_request('POST', path, params)
        return self._resource_for(response)

    def list(self, params=None):
        path = '/customer_bank_accounts'
        response = self._perform_request('GET', path, params)
        return self._resource_for(response)

    def get(self, identity, params=None):
        path = self._sub_url_params('/customer_bank_accounts/:identity', {
            'identity': identity,
        })
        response = self._perform_request('GET', path, params)
        return self._resource_for(response)

    def update(self, identity, params=None):
        path = self._sub_url_params('/customer_bank_accounts/:identity', {
            'identity': identity,
        })
        response = self._perform_request('PUT', path, params)
        return self._resource_for(response)

    def disable(self, identity, params=None):
        path = self._sub_url_params('/customer_bank_accounts/:identity/actions/disable', {
            'identity': identity,
        })
        response = self._perform_request('POST', path, params)
        return self._resource_for(response)

