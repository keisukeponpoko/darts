# -*- coding: utf-8 -*-

from urllib.request import urlretrieve

url = 'http://search.dartslive.jp/list/%E6%9D%B1%E4%BA%AC%E9%83%BD?p='

for i in range(0, 29):
    urlretrieve(url + str(i), 'html/list' + str(i) + '.html')
