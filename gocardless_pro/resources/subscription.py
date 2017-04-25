# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class Subscription(object):
    """A thin wrapper around a subscription, providing easy access to its
    attributes.

    Example:
      subscription = client.subscriptions.get()
      subscription.id
    """

    def __init__(self, attributes, api_response):
        self.attributes = attributes
        self.api_response = api_response

    @property
    def amount(self):
        return self.attributes.get('amount')
  

    @property
    def created_at(self):
        return self.attributes.get('created_at')
  

    @property
    def currency(self):
        return self.attributes.get('currency')
  

    @property
    def day_of_month(self):
        return self.attributes.get('day_of_month')
  

    @property
    def end_date(self):
        return self.attributes.get('end_date')
  

    @property
    def id(self):
        return self.attributes.get('id')
  

    @property
    def interval(self):
        return self.attributes.get('interval')
  

    @property
    def interval_unit(self):
        return self.attributes.get('interval_unit')
  

    @property
    def links(self):
        return self.Links(self.attributes.get('links'))
  

    @property
    def metadata(self):
        return self.attributes.get('metadata')
  

    @property
    def month(self):
        return self.attributes.get('month')
  

    @property
    def name(self):
        return self.attributes.get('name')
  

    @property
    def payment_reference(self):
        return self.attributes.get('payment_reference')
  

    @property
    def start_date(self):
        return self.attributes.get('start_date')
  

    @property
    def status(self):
        return self.attributes.get('status')
  

    @property
    def upcoming_payments(self):
        return self.attributes.get('upcoming_payments')
  


  

  

  

  

  

  

  

  

  
    class Links(object):
        """Wrapper for the response's 'links' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def mandate(self):
            return self.attributes.get('mandate')
    
  

  

  

  

  

  

  

  

