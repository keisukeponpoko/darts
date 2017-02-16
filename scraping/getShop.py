# -*- coding: utf-8 -*-

from urllib.request import urlretrieve
import json

jsonFile = open('json/tokyo_list.json', 'r')
jsonData = json.load(jsonFile)
jsonFile.close()

url = 'http://search.dartslive.jp/'

print('count:' + str(len(jsonData)))

for i, lists in enumerate(jsonData):
    urlretrieve(url + lists[0], 'html/tokyo/data' + str(i) + '.html')
