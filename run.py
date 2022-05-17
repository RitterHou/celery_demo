# -*- coding: utf-8 -*-
import logging

from search.tasks import search_url, add, sort_list

if __name__ == '__main__':
    logging.info(search_url('https://www.jd.com'))
    logging.info(search_url.delay('https://www.jd.com').get(5))

    logging.info(add(1.5, 3.5))
    logging.info(add.delay(1.5, 3.5).get(5))

    data = [5, 86, 59, 17, 24, 92, 38, 95, 13, 89, 63, 3, 4, 60, 6]
    logging.info(sort_list(data))
    logging.info(sort_list.delay(data).get(5))
