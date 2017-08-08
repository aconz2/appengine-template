import logging

import requests
import requests_toolbelt.adapters.appengine

from flask import Flask

requests_toolbelt.adapters.appengine.monkeypatch()

app = Flask(__name__)

@app.route('/')
def hello():
    res = requests.get('https://google.com')
    res.raise_for_status()
    return res.text

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
