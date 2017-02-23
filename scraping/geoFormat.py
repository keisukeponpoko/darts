# -*- coding: utf-8 -*-
import geocoder
import json

f = open('json/tokyo_shop.json', 'r')
jsonData = json.load(f)
f.close()

for k, j in enumerate(jsonData):
    if j['latitude'] == "" or j['longitude'] == "":
        print(j['address'])
        ret = geocoder.google(j['address']).latlng
        if ret:
            jsonData[k]['latitude'], jsonData[k]['longitude'] = ret
        else:
            ret = geocoder.google(j['address']).latlng
            if ret:
                jsonData[k]['latitude'], jsonData[k]['longitude'] = ret
            else:
                ret = geocoder.google(j['address'].replace('\u3000', '')).latlng
                if ret:
                    jsonData[k]['latitude'], jsonData[k]['longitude'] = ret
                else:
                    for i in range(1, 20):
                        address = j['address'][:-i]
                        ret = geocoder.google(address).latlng
                        print(ret)
                        print(i)
                        if ret:
                            jsonData[k]['latitude'], jsonData[k]['longitude'] = ret
                            break

    if jsonData[k]['latitude'] == "" or jsonData[k]['longitude'] == "":
        print(jsonData[k])

f2 = open('json/format.json', 'w')
json.dump(jsonData, f2)
f.close()
