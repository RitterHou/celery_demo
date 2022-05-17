#!/bin/bash

operation='worker'
queue_flag=''
log_level='info'
hostname=''

while getopts 'fql:n:' flag; do
  case "${flag}" in
  f) operation='flower --port=5555' ;;  # 启动flower，而不是worker
  q) queue_flag='-Q sort,celery' ;;     # 使用自定义队列
  l) log_level="${OPTARG}" ;;           # 设置日志级别
  n) hostname="--hostname ${OPTARG}" ;; # 指定worker的主机名，可选参数：%p，%h，%n，%d
  *) echo "Unknown flag: ${flag}" ;;
  esac
done

celery -A search $operation $queue_flag -l $log_level $hostname

# -A, --app
# 表示使用的应用实例，设置后会按顺序自动寻找：search.app、search.celery、search.celery.app、search.celery.celery，作为celery的对象
# https://docs.celeryq.dev/en/v4.4.7/getting-started/next-steps.html#about-the-app-argument

# worker 启动一个worker

# -Q 使用特定的队列，实现路由功能
# https://docs.celeryq.dev/en/v4.4.7/userguide/routing.html#automatic-routing
