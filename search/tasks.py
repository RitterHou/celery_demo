# -*- coding: utf-8 -*-
from . import app


@app.task
def search(keyword, text):
    return keyword in text
