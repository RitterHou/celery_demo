#!/usr/bin/env bash

celery -A search worker -l info

# -A, --app
# 表示使用的应用实例，设置后会按顺序自动寻找：search.app、search.celery、search.celery.app、search.celery.celery，作为celery的对象
# https://docs.celeryq.dev/en/v4.4.7/getting-started/next-steps.html#about-the-app-argument

# worker
# 启动一个worker
