from django.shortcuts import render
from shop.models import Darts
from django.http import HttpResponse
from django.core import serializers
import json, decimal
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

def map(request):
    return render(request, 'map.html')

def getShop(request):
    from django.http import HttpResponse,Http404

    data = json.dumps(list(Darts.objects.values_list('latitude', 'longitude', 'name', 'id')), default=decimal_default)
    return HttpResponse(data)

def showShop(request, shop_id):
    shopData = Darts.objects.filter(id = shop_id).first()
    return render(request, 'detail.html', {'shopData' : shopData})

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError
