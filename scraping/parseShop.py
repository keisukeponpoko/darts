# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json
import glob
import geocoder

fileList = glob.glob('html/tokyo/*.html')

jsonData = []
# fileList = ['html/tokyo/data271.html']
for html in fileList:
    f = open(html, 'r')
    soup = BeautifulSoup(f.read(), "lxml")
    f.close()


    rawDartslive = soup.select(".icn-shop-no")
    if rawDartslive:
        dartslive = rawDartslive[0].text.replace('台', '')
    else:
        dartslive = 0

    name = soup.select(".shop-info dl dd")[0].text

    rawInformation = soup.select(".shopInfo-txt-area p")
    if rawInformation:
        information = rawInformation[0].text
    else:
        information = ''

    address = ''
    tel = ''
    station = ''
    time = ''
    holiday = ''
    url = ''
    tableColumns = soup.select("div.shopAccess table tr")
    for tr in tableColumns:
        th = tr.select("th")[0].text
        td = ' '.join(tr.select("td")[0].text.split())
        if th == '住所':
            address = td
        elif th == '電話':
            tel = td
        elif th == '最寄駅':
            station = td
        elif th == '営業時間':
            time = td
        elif th == '定休日':
            holiday = td
        elif th == 'URL':
            url = td

    ret = geocoder.google(address).latlng
    if ret:
        latitude, longitude = ret
    else:
        latitude, longitude = [0, 0]
        print(name)

    data = {
        'name': name,
        'address': address,
        'tel': tel,
        'station': station,
        'time': time,
        'holiday': holiday,
        'url': url,
        'latitude': latitude,
        'longitude': longitude,
        'dartslive': dartslive,
        'information': information
    }

    jsonData.append(data)

jsonFile = open('json/tokyo_shop.json', 'w')
json.dump(jsonData, jsonFile)
jsonFile.close()
