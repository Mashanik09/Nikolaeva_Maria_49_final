import configuration
import requests

def post_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=body)

def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.RECIVE_ORDER_BY_TRACK, {'t':track})
     