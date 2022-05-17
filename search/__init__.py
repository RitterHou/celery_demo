# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery import Celery

from . import config

app = Celery('search', broker='redis://127.0.0.1:6379/6', backend='redis://127.0.0.1:6379/8')
app.config_from_object(config)
