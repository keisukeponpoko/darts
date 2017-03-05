# -*- coding:utf-8 -*-

from django.core.management.base import BaseCommand
from shop.models import Shop, Pref, City, Station, Line, LineStation


# BaseCommandを継承して作成
class Command(BaseCommand):
    # python manage.py help insertSqlで表示されるメッセージ
    help = 'Insert Data to MySql. 0 = all data insert. 1 = only darts shop. 2 = only area info. 3 = only station info.'

    # コマンドライン引数を指定します。(argparseモジュール https://docs.python.org/2.7/library/argparse.html)
    def add_arguments(self, parser):
        parser.add_argument('type', nargs='?', type=int)

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):
        if options['type'] == 1:
            self.insertShop()
        elif options['type'] == 2:
            self.insertPref()
            self.insertCity()

    def insertShop(self):
        import random

        for shopData in self.getJson('format'):
            shop = Shop()
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
            shop.phoenix = shopData['dartslive']
            shop.information = shopData['information']
            shop.pref_id = 13
            shop.city_id = random.uniform(13101, 13123)

            try:
                shop.save()
            except:
                shop.information = ''
                shop.save()
                print(shopData['name'] + 'は環境依存文字が使われています。')

        print('shop data insert')

    def insertPref(self):
        for data in self.getJson('pref'):
            box = Pref()
            box.pref_id = data['id']
            box.name = data['name']
            box.latitude = data['geo']['office']['lat'] if data['geo']['office']['lat'] else 0
            box.longitude = data['geo']['office']['lng'] if data['geo']['office']['lng'] else 0
            box.save()

        print('pref data insert')

    def insertCity(self):
        for data in self.getJson('city'):
            box = City()
            box.pref_id = data['pref_id']
            box.city_id = data['id']
            box.city_part_id = data['city_part_id']
            box.name = data['name']
            box.latitude = data['lat'] if data['lat'] else 0
            box.longitude = data['lng'] if data['lng'] else 0
            box.save()

        print('city data insert')

    def getJson(self, filename):
        import json
        import os.path

        base = os.path.dirname(os.path.abspath(__file__))
        name = os.path.normpath(os.path.join(base, '../../json/' + filename + '.json'))
        data = open(name, 'r')
        jsonData = json.load(data)
        data.close()
        return jsonData
