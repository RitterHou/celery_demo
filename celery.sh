#!/bin/bash

if [[ "$1" == "-q" ]]; then
  celery -A search worker -Q sort,celery -l info
else
  celery -A search worker -l info
fi

# -A, --app
# 表示使用的应用实例，设置后会按顺序自动寻找：search.app、search.celery、search.celery.app、search.celery.celery，作为celery的对象
# https://docs.celeryq.dev/en/v4.4.7/getting-started/next-steps.html#about-the-app-argument

# worker 启动一个worker

# -Q 使用特定的队列，实现路由功能
# https://docs.celeryq.dev/en/v4.4.7/userguide/routing.html#automatic-routing
