from django.contrib import admin

# Register your models here.
from shop.models import Shop, Pref, City, Station, Line, LineStation


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'pref_id', 'city_id', 'name', 'address', 'time', 'station', 'holiday', 'tel', 'url', 'dartslive', 'phoenix', 'latitude', 'longitude', 'information')  # 一覧に出したい項目
    list_display_links = ('name',)  # 修正リンクでクリックできる項目
admin.site.register(Shop, ShopAdmin)

class PrefAdmin(admin.ModelAdmin):
    list_display = ('pref_id', 'name', 'latitude', 'longitude')  # 一覧に出したい項目
admin.site.register(Pref, PrefAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ('pref_id', 'city_id', 'name', 'latitude', 'longitude')  # 一覧に出したい項目
admin.site.register(City, CityAdmin)
