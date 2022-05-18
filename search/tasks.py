# -*- coding: utf-8 -*-
"""
创建celery的tasks
"""
import logging

import requests
from redis.client import Redis

from . import app

redis_cli = Redis('127.0.0.1', db=1)


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


@app.task
def get_redis_keys():
    keys = redis_cli.keys()
    logging.info('redis keys: {}'.format(keys))
    return keys
