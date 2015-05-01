# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse
import json

import requests

class HttpClient(object):
    """HTTP Client for interacting with a JSON API, using OAuth2-style auth.

    Args:
      base_url (string): The prefix that's prepended to all request paths.
      access_token (string): Token used in the Authorization header.
    """

    def __init__(self, base_url, access_token):
        self.base_url = base_url
        self.access_token = access_token

    def get(self, path, params=None):
        """Perform a GET request, optionally providing query-string params.

        Args:
          path (str): A path that gets appended to ``base_url``.
          params (dict, optional): Dictionary of param names to values.

        Example:
          http_client.get('/users', params={'active': True})

        Returns:
          A requests ``Response`` object.
        """
        return requests.get(
            self._url_for(path),
            params=params,
            headers=self._default_headers()
        )

    def post(self, path, body):
        """Perform a POST request, providing a body, which will be JSON-encoded.

        Args:
          path (str): A path that gets appended to ``base_url``.
          body (dict): Dictionary that will be JSON-encoded and sent as the body.

        Example:
          http_client.post('/users', body={'name': 'Billy Jean'})

        Returns:
          A requests ``Response`` object.
        """
        return requests.post(
            self._url_for(path),
            data=json.dumps(body),
            headers=self._default_headers()
        )

    def put(self, path, body):
        """Perform a PUT request, providing a body, which will be JSON-encoded.

        Args:
          path (str): A path that gets appended to ``base_url``.
          body (dict): Dictionary that will be JSON-encoded and sent as the body.

        Example:
          http_client.put('/users', body={'name': 'Billy Jean'})

        Returns:
          A requests ``Response`` object.
        """
        return requests.put(
            self._url_for(path),
            data=json.dumps(body),
            headers=self._default_headers()
        )

    def _url_for(self, path):
        return urlparse.urljoin(self.base_url, path)

    def _default_headers(self):
        return {
            'Accept': 'application/json',
            'Authorization': 'Bearer {0}'.format(self.access_token),
            'Content-Type': 'application/json',
            'User-Agent': 'gocardless-pro-python',  # TODO: add detail!
            
            'GoCardless-Version': '2015-04-29',
        }
