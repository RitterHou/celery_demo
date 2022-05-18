# -*- coding: utf-8 -*-
"""
发送celery的tasks
"""
import logging

from search.tasks import search_url, add, sort_list, get_redis_keys

if __name__ == '__main__':
    # logging.info(' local: {}'.format(search_url('https://www.jd.com')))
    # logging.info('remote: {}'.format(search_url.delay('https://www.jd.com').get(5)))
    #
    # logging.info(' local: {}'.format(add(1.5, 3.5)))
    # logging.info('remote: {}'.format(add.delay(1.5, 3.5).get(5)))
    #
    # data = [5, 86, 59, 17, 24, 92, 38, 95, 13, 89, 63, 3, 4, 60, 6]
    # logging.info(' local: {}'.format(sort_list(data)))
    # logging.info('remote: {}'.format(sort_list.delay(data).get(5)))

    logging.info(get_redis_keys.apply_async((), queue='queue_1').get(5))
