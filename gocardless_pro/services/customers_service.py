# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class CustomersService(base_service.BaseService):
    """Service class that provides access to the customers
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.Customer
    RESOURCE_NAME = 'customers'


    def create(self,params=None, headers=None):
        """Create a customer.

        Creates a new customer object.

        Args:
              params (dict, optional): Request body.

        Returns:
              ListResponse of Customer instances
        """
        path = '/customers'
        
        if params is not None:
            params = {self._envelope_key(): params}

        try:
          response = self._perform_request('POST', path, params, headers,
                                            retry_failures=True)
        except errors.IdempotentCreationConflictError as err:
          return self.get(identity=err.conflicting_resource_id,
                          params=params,
                          headers=headers)
        return self._resource_for(response)
  

    def list(self,params=None, headers=None):
        """List customers.

        Returns a [cursor-paginated](#api-usage-cursor-pagination) list of your
        customers.

        Args:
              params (dict, optional): Query string parameters.

        Returns:
              Customer
        """
        path = '/customers'
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)

    def all(self, params=None):
        if params is None:
            params = {}
        return Paginator(self, params)
    
  

    def get(self,identity,params=None, headers=None):
        """Get a single customer.

        Retrieves the details of an existing customer.

        Args:
              identity (string): Unique identifier, beginning with "CU".
              params (dict, optional): Query string parameters.

        Returns:
              ListResponse of Customer instances
        """
        path = self._sub_url_params('/customers/:identity', {
          
            'identity': identity,
          })
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  

    def update(self,identity,params=None, headers=None):
        """Update a customer.

        Updates a customer object. Supports all of the fields supported when
        creating a customer.

        Args:
              identity (string): Unique identifier, beginning with "CU".
              params (dict, optional): Request body.

        Returns:
              ListResponse of Customer instances
        """
        path = self._sub_url_params('/customers/:identity', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {self._envelope_key(): params}

        response = self._perform_request('PUT', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  

    def remove(self,identity,params=None, headers=None):
        """Remove a customer.

        Removed customers will not appear in search results or lists of
        customers (in our API
        or exports), and it will not be possible to load an individually
        removed customer by
        ID.
        
        <p class="restricted-notice"><strong>The action of removing a customer
        cannot be
        reversed, so please use with care.</strong></p>

        Args:
              identity (string): Unique identifier, beginning with "CU".
              params (dict, optional): Request body.

        Returns:
              ListResponse of Customer instances
        """
        path = self._sub_url_params('/customers/:identity', {
          
            'identity': identity,
          })
        
        response = self._perform_request('DELETE', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  
