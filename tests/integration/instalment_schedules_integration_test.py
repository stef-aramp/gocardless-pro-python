# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import json

import requests
import responses
from nose.tools import (
  assert_equal,
  assert_is_instance,
  assert_is_none,
  assert_is_not_none,
  assert_not_equal,
  assert_raises
)

from gocardless_pro.errors import MalformedResponseError
from gocardless_pro import resources
from gocardless_pro import list_response

from .. import helpers
  

@responses.activate
def test_instalment_schedules_create_with_dates():
    fixture = helpers.load_fixture('instalment_schedules')['create_with_dates']
    helpers.stub_response(fixture)
    response = helpers.client.instalment_schedules.create_with_dates(*fixture['url_params'])
    body = fixture['body']['instalment_schedules']

    assert_is_instance(response, resources.InstalmentSchedule)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.payment_errors, body.get('payment_errors'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.total_amount, body.get('total_amount'))
    assert_equal(response.links.customer,
                 body.get('links')['customer'])
    assert_equal(response.links.mandate,
                 body.get('links')['mandate'])
    assert_equal(response.links.payments,
                 body.get('links')['payments'])

@responses.activate
def test_instalment_schedules_create_with_dates_new_idempotency_key_for_each_call():
    fixture = helpers.load_fixture('instalment_schedules')['create_with_dates']
    helpers.stub_response(fixture)
    helpers.client.instalment_schedules.create_with_dates(*fixture['url_params'])
    helpers.client.instalment_schedules.create_with_dates(*fixture['url_params'])
    assert_not_equal(responses.calls[0].request.headers.get('Idempotency-Key'),
                     responses.calls[1].request.headers.get('Idempotency-Key'))

def test_timeout_instalment_schedules_create_with_dates_idempotency_conflict():
    create_fixture = helpers.load_fixture('instalment_schedules')['create_with_dates']
    get_fixture = helpers.load_fixture('instalment_schedules')['get']
    with helpers.stub_timeout_then_idempotency_conflict(create_fixture, get_fixture) as rsps:
      response = helpers.client.instalment_schedules.create_with_dates(*create_fixture['url_params'])
      assert_equal(2, len(rsps.calls))

    assert_is_instance(response, resources.InstalmentSchedule)

@responses.activate
def test_timeout_instalment_schedules_create_with_dates_retries():
    fixture = helpers.load_fixture('instalment_schedules')['create_with_dates']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.instalment_schedules.create_with_dates(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['instalment_schedules']

    assert_is_instance(response, resources.InstalmentSchedule)

def test_502_instalment_schedules_create_with_dates_retries():
    fixture = helpers.load_fixture('instalment_schedules')['create_with_dates']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.instalment_schedules.create_with_dates(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['instalment_schedules']

    assert_is_instance(response, resources.InstalmentSchedule)
  

@responses.activate
def test_instalment_schedules_create_with_schedule():
    fixture = helpers.load_fixture('instalment_schedules')['create_with_schedule']
    helpers.stub_response(fixture)
    response = helpers.client.instalment_schedules.create_with_schedule(*fixture['url_params'])
    body = fixture['body']['instalment_schedules']

    assert_is_instance(response, resources.InstalmentSchedule)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.payment_errors, body.get('payment_errors'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.total_amount, body.get('total_amount'))
    assert_equal(response.links.customer,
                 body.get('links')['customer'])
    assert_equal(response.links.mandate,
                 body.get('links')['mandate'])
    assert_equal(response.links.payments,
                 body.get('links')['payments'])

@responses.activate
def test_instalment_schedules_create_with_schedule_new_idempotency_key_for_each_call():
    fixture = helpers.load_fixture('instalment_schedules')['create_with_schedule']
    helpers.stub_response(fixture)
    helpers.client.instalment_schedules.create_with_schedule(*fixture['url_params'])
    helpers.client.instalment_schedules.create_with_schedule(*fixture['url_params'])
    assert_not_equal(responses.calls[0].request.headers.get('Idempotency-Key'),
                     responses.calls[1].request.headers.get('Idempotency-Key'))

def test_timeout_instalment_schedules_create_with_schedule_idempotency_conflict():
    create_fixture = helpers.load_fixture('instalment_schedules')['create_with_schedule']
    get_fixture = helpers.load_fixture('instalment_schedules')['get']
    with helpers.stub_timeout_then_idempotency_conflict(create_fixture, get_fixture) as rsps:
      response = helpers.client.instalment_schedules.create_with_schedule(*create_fixture['url_params'])
      assert_equal(2, len(rsps.calls))

    assert_is_instance(response, resources.InstalmentSchedule)

@responses.activate
def test_timeout_instalment_schedules_create_with_schedule_retries():
    fixture = helpers.load_fixture('instalment_schedules')['create_with_schedule']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.instalment_schedules.create_with_schedule(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['instalment_schedules']

    assert_is_instance(response, resources.InstalmentSchedule)

def test_502_instalment_schedules_create_with_schedule_retries():
    fixture = helpers.load_fixture('instalment_schedules')['create_with_schedule']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.instalment_schedules.create_with_schedule(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['instalment_schedules']

    assert_is_instance(response, resources.InstalmentSchedule)
  

@responses.activate
def test_instalment_schedules_list():
    fixture = helpers.load_fixture('instalment_schedules')['list']
    helpers.stub_response(fixture)
    response = helpers.client.instalment_schedules.list(*fixture['url_params'])
    body = fixture['body']['instalment_schedules']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.InstalmentSchedule)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal([r.created_at for r in response.records],
                 [b.get('created_at') for b in body])
    assert_equal([r.currency for r in response.records],
                 [b.get('currency') for b in body])
    assert_equal([r.id for r in response.records],
                 [b.get('id') for b in body])
    assert_equal([r.metadata for r in response.records],
                 [b.get('metadata') for b in body])
    assert_equal([r.name for r in response.records],
                 [b.get('name') for b in body])
    assert_equal([r.payment_errors for r in response.records],
                 [b.get('payment_errors') for b in body])
    assert_equal([r.status for r in response.records],
                 [b.get('status') for b in body])
    assert_equal([r.total_amount for r in response.records],
                 [b.get('total_amount') for b in body])

@responses.activate
def test_timeout_instalment_schedules_list_retries():
    fixture = helpers.load_fixture('instalment_schedules')['list']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.instalment_schedules.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['instalment_schedules']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.InstalmentSchedule)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

def test_502_instalment_schedules_list_retries():
    fixture = helpers.load_fixture('instalment_schedules')['list']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.instalment_schedules.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['instalment_schedules']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.InstalmentSchedule)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

@responses.activate
def test_instalment_schedules_all():
    fixture = helpers.load_fixture('instalment_schedules')['list']

    def callback(request):
        if 'after=123' in request.url:
          fixture['body']['meta']['cursors']['after'] = None
        else:
          fixture['body']['meta']['cursors']['after'] = '123'
        return [200, {}, json.dumps(fixture['body'])]

    url = 'http://example.com' + fixture['path_template']
    responses.add_callback(fixture['method'], url, callback)

    all_records = list(helpers.client.instalment_schedules.all())
    assert_equal(len(all_records), len(fixture['body']['instalment_schedules']) * 2)
    for record in all_records:
      assert_is_instance(record, resources.InstalmentSchedule)
    
  

@responses.activate
def test_instalment_schedules_get():
    fixture = helpers.load_fixture('instalment_schedules')['get']
    helpers.stub_response(fixture)
    response = helpers.client.instalment_schedules.get(*fixture['url_params'])
    body = fixture['body']['instalment_schedules']

    assert_is_instance(response, resources.InstalmentSchedule)
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.payment_errors, body.get('payment_errors'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.total_amount, body.get('total_amount'))
    assert_equal(response.links.customer,
                 body.get('links')['customer'])
    assert_equal(response.links.mandate,
                 body.get('links')['mandate'])
    assert_equal(response.links.payments,
                 body.get('links')['payments'])

@responses.activate
def test_timeout_instalment_schedules_get_retries():
    fixture = helpers.load_fixture('instalment_schedules')['get']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.instalment_schedules.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['instalment_schedules']

    assert_is_instance(response, resources.InstalmentSchedule)

def test_502_instalment_schedules_get_retries():
    fixture = helpers.load_fixture('instalment_schedules')['get']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.instalment_schedules.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['instalment_schedules']

    assert_is_instance(response, resources.InstalmentSchedule)
  

@responses.activate
def test_instalment_schedules_cancel():
    fixture = helpers.load_fixture('instalment_schedules')['cancel']
    helpers.stub_response(fixture)
    response = helpers.client.instalment_schedules.cancel(*fixture['url_params'])
    body = fixture['body']['instalment_schedules']

    assert_is_instance(response, resources.InstalmentSchedule)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.name, body.get('name'))
    assert_equal(response.payment_errors, body.get('payment_errors'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.total_amount, body.get('total_amount'))
    assert_equal(response.links.customer,
                 body.get('links')['customer'])
    assert_equal(response.links.mandate,
                 body.get('links')['mandate'])
    assert_equal(response.links.payments,
                 body.get('links')['payments'])

def test_timeout_instalment_schedules_cancel_doesnt_retry():
    fixture = helpers.load_fixture('instalment_schedules')['cancel']
    with helpers.stub_timeout(fixture) as rsps:
      with assert_raises(requests.ConnectTimeout):
        response = helpers.client.instalment_schedules.cancel(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))

def test_502_instalment_schedules_cancel_doesnt_retry():
    fixture = helpers.load_fixture('instalment_schedules')['cancel']
    with helpers.stub_502(fixture) as rsps:
      with assert_raises(MalformedResponseError):
        response = helpers.client.instalment_schedules.cancel(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))
  