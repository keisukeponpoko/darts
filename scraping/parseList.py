# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json

jsonData = []
for i in range(0, 29):
    f = open('html/list' + str(i) + '.html', 'r')
    soup = BeautifulSoup(f.read(), "lxml")
    f.close()

    links = soup.select(".info-txt a")
    for link in links:
        jsonData.append([link.get("href"), link.text])

jsonFile = open('json/tokyo_list.json', 'w')
json.dump(jsonData, jsonFile)
jsonFile.close()
