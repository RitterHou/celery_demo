# -*- coding: utf-8 -*-
"""
通过Python启动celery的worker
"""
import logging

from search import app

if __name__ == '__main__':
    logging.info(app.conf.timezone)

    app.conf.update(timezone='Europe/London')
    logging.info(app.conf.timezone)

    app.conf.timezone = 'Asia/Shanghai'
    logging.info(app.conf.timezone)

    logging.info(app.conf.humanize(with_defaults=False, censored=True))

    app.worker_main(('worker', '-Q', 'queue_1,celery', '-n', 'python_host', '-l', 'info'))
