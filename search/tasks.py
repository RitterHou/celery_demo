# -*- coding: utf-8 -*-
import requests

from . import app


@app.task
def search(keyword, text):
    return keyword in text


@app.task
def search_url(url):
    r = requests.get(url)
    return r.text
