# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class Helper(object):
    """A thin wrapper around a helper, providing easy access to its
    attributes.

    Example:
      helper = client.helpers.get()
      helper.id
    """

    def __init__(self, attributes, response):
        self.attributes = attributes
        self.response = response


# TODO: handle links properly, and double check how response is exposed

