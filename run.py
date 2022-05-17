# -*- coding: utf-8 -*-
from search.tasks import search

if __name__ == '__main__':
    print search('hello', 'nice to meet you')
    print search.delay('hello', 'nice to meet you').get()
