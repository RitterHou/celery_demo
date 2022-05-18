# -*- coding: utf-8 -*-
"""
通过Python启动celery的worker
"""
from search import app

if __name__ == '__main__':
    app.worker_main(('worker', '-Q', 'queue_1,celery', '-n', 'python_host', '-l', 'info'))
