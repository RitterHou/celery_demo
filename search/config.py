# -*- coding: utf-8 -*-

include = ['search.tasks']

# https://docs.celeryq.dev/en/v4.4.7/userguide/routing.html#automatic-routing
# 对该任务（task）使用一个特定的队列进行路由
task_routes = {
    'search.tasks.sort_list': {'queue': 'sort'}
}

timezone = 'Asia/Shanghai'
