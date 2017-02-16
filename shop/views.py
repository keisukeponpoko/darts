from django.shortcuts import render
from shop.models import Darts
from django.http import HttpResponse
import json
import os.path

# Create your views here.
def insert(self):
    BASE = os.path.dirname(os.path.abspath(__file__))
    data = open(BASE + "/json/format.json", 'r')
    jsonData = json.load(data)
    data.close()

    for shopData in jsonData:
        shop = Darts()
        shop.name = shopData['name']
        shop.latitude = shopData['latitude'] if shopData['latitude'] else 0
        shop.longitude = shopData['longitude'] if shopData['longitude'] else 0
        shop.holiday = shopData['holiday']
        shop.station = shopData['station']
        shop.time = shopData['time']
        shop.address = shopData['address']
        shop.tel = shopData['tel']
        shop.url = shopData['url']
        shop.dartslive = shopData['dartslive']
        shop.information = shopData['information']
        shop.save()

    return HttpResponse('ok')
