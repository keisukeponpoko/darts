from django.shortcuts import render
from shop.models import Shop
from django_user_agents.utils import get_user_agent
from django.http import HttpResponse,Http404

def index(request):
    if get_user_agent(request).is_mobile:
        templatePath = 'sp/index.html'
    else:
        templatePath = 'sp/index.html'
    return render(request, templatePath)

def map(request):
    return render(request, 'sp/map.html')

def Arealist(request, param):
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    from shop.models import Pref, City
    import re

    pref_id, city_id, category_id, page = 13, None, None, 1

    r = re.compile("(pref|city|category|page)=([0-9_]+)")
    for ids in r.findall(param):
        if ids[0] == 'pref':
            pref_id = ids[1]
        elif ids[0] == 'city':
            city_id = ids[1]
        elif ids[0] == 'category':
            category_id = ids[1]
        elif ids[0] == 'page':
            page = ids[1]

    where = {}
    where['pref_id'] = pref_id

    if city_id is not None:
        cities = city_id.split('_')
        where['city_id__in'] = cities
        if len(cities) == 1:
            AreaModel = City.objects.filter(city_id__in = cities).values('name').first()

    try:
        areaName = AreaModel['name']
    except:
        AreaModel = Pref.objects.filter(pref_id = pref_id).values('name').first()
        areaName = AreaModel['name']

    listData = Shop.objects.filter(**where).values('id', 'name', 'address', 'holiday', 'time', 'dartslive', 'phoenix', 'station')


    paginator = Paginator(listData, 20)
    try:
        shopList = paginator.page(page)
    except PageNotAnInteger:
        shopList = paginator.page(1)
    except EmptyPage:
        shopList = paginator.page(paginator.num_pages)

    # 将来的にはreact-pythonを使いたい
    return render(request, 'sp/list.html', {
        'shopList': shopList,
        'areaName': areaName,
        'pref': pref_id,
        'city': city_id,
        'category': category_id,
    })

def shop(request, shop_id):
    shopData = Shop.objects.filter(id = shop_id).first()
    return render(request, 'sp/detail.html', {'shopData' : shopData})

def ajaxDetail(request):
    import json

    data = json.dumps(list(Shop.objects.values_list('latitude', 'longitude', 'name', 'id')), default=decimal_default)
    return HttpResponse(data)

def decimal_default(obj):
    import decimal

    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError
