# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import requests
import responses
from nose.tools import assert_equal, assert_is_instance

from gocardless_pro import resources
from gocardless_pro import list_response

from .. import helpers

@responses.activate
def test_payments_create():
    fixture = helpers.load_fixture('payments')['create']
    helpers.stub_response(fixture)
    response = helpers.client.payments.create(*fixture['url_params'])
    body = fixture['body']['payments']

    assert_is_instance(response, resources.Payment)

    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.amount_refunded, body.get('amount_refunded'))
    assert_equal(response.charge_date, body.get('charge_date'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.description, body.get('description'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.status, body.get('status'))

@responses.activate
def test_payments_list():
    fixture = helpers.load_fixture('payments')['list']
    helpers.stub_response(fixture)
    response = helpers.client.payments.list(*fixture['url_params'])
    body = fixture['body']['payments']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(next(iter(response)), resources.Payment)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

    assert_equal([r.amount for r in response],
                  [b.get('amount') for b in body])
    assert_equal([r.amount_refunded for r in response],
                  [b.get('amount_refunded') for b in body])
    assert_equal([r.charge_date for r in response],
                  [b.get('charge_date') for b in body])
    assert_equal([r.created_at for r in response],
                  [b.get('created_at') for b in body])
    assert_equal([r.currency for r in response],
                  [b.get('currency') for b in body])
    assert_equal([r.description for r in response],
                  [b.get('description') for b in body])
    assert_equal([r.id for r in response],
                  [b.get('id') for b in body])
    assert_equal([r.links for r in response],
                  [b.get('links') for b in body])
    assert_equal([r.metadata for r in response],
                  [b.get('metadata') for b in body])
    assert_equal([r.reference for r in response],
                  [b.get('reference') for b in body])
    assert_equal([r.status for r in response],
                  [b.get('status') for b in body])

@responses.activate
def test_payments_get():
    fixture = helpers.load_fixture('payments')['get']
    helpers.stub_response(fixture)
    response = helpers.client.payments.get(*fixture['url_params'])
    body = fixture['body']['payments']

    assert_is_instance(response, resources.Payment)

    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.amount_refunded, body.get('amount_refunded'))
    assert_equal(response.charge_date, body.get('charge_date'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.description, body.get('description'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.status, body.get('status'))

@responses.activate
def test_payments_update():
    fixture = helpers.load_fixture('payments')['update']
    helpers.stub_response(fixture)
    response = helpers.client.payments.update(*fixture['url_params'])
    body = fixture['body']['payments']

    assert_is_instance(response, resources.Payment)

    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.amount_refunded, body.get('amount_refunded'))
    assert_equal(response.charge_date, body.get('charge_date'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.description, body.get('description'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.status, body.get('status'))

@responses.activate
def test_payments_cancel():
    fixture = helpers.load_fixture('payments')['cancel']
    helpers.stub_response(fixture)
    response = helpers.client.payments.cancel(*fixture['url_params'])
    body = fixture['body']['payments']

    assert_is_instance(response, resources.Payment)

    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.amount_refunded, body.get('amount_refunded'))
    assert_equal(response.charge_date, body.get('charge_date'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.description, body.get('description'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.status, body.get('status'))

@responses.activate
def test_payments_retry():
    fixture = helpers.load_fixture('payments')['retry']
    helpers.stub_response(fixture)
    response = helpers.client.payments.retry(*fixture['url_params'])
    body = fixture['body']['payments']

    assert_is_instance(response, resources.Payment)

    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.amount_refunded, body.get('amount_refunded'))
    assert_equal(response.charge_date, body.get('charge_date'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.description, body.get('description'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.links, body.get('links'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.status, body.get('status'))

