# -*- coding: utf-8 -*-
from search.tasks import search, search_url

if __name__ == '__main__':
    print search('hello', 'nice to meet you')
    print search.delay('hello', 'nice to meet you').get()

    print search_url('https://www.jd.com')
    print search_url.delay('https://www.jd.com').get()
