# -*- coding: utf-8 -*-
import logging

import requests

from . import app


@app.task
def search_url(url):
    logging.info('GET url: {}'.format(url))
    r = requests.get(url)
    return r.status_code


@app.task
def add(x, y):
    logging.info('calculate add: {} + {}'.format(x, y))
    return x + y


@app.task
def sort_list(data):
    logging.info('Sort list: {}'.format(data))
    return sorted(data)
