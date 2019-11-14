#!/usr/bin/python
#-*-coding:utf-8-*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# copyright 2019 Zhao, Inc.
# All Rights Reserved.

# @File: baiduMyself.py
# @Author: Zhao, Zhao, Inc.
# @Time: 2019/11/14 14:51

import sys
import urllib
import argparse
from pyquery import PyQuery

class Spider(object):
    def __init__(self, header, url):
        self.url = url
        self.context = PyQuery(headers = header, url=url)
        return

    def search(self):
        content = self.context.find('#content_left')
        for item in content('h3.t a').items():
            print('{0}: {1}'.format(item.text(), item.attr('href')))
        return



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="name", type=str, required=True)
    args = parser.parse_args()

    url = 'https://www.baidu.com/s?wd={0}'.format(urllib.request.quote(args.name))
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
    }

    spider = Spider(header, url)
    spider.search()

    sys.exit(0)