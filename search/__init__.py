# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging
import sys

from celery import Celery

from . import config

app = Celery('search', broker='redis://127.0.0.1:6379/1', backend='redis://127.0.0.1:6379/1')
app.config_from_object(config)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(filename)10s:%(lineno)-5d: %(message)s',
                    stream=sys.stdout)
