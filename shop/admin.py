from django.contrib import admin

# Register your models here.
from shop.models import Darts, Pref, City, Station, Line, LineStation


class DartsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'time', 'station', 'holiday', 'tel', 'url', 'dartslive', 'latitude', 'longitude', 'information')  # 一覧に出したい項目
    list_display_links = ('name',)  # 修正リンクでクリックできる項目
admin.site.register(Darts, DartsAdmin)

class PrefAdmin(admin.ModelAdmin):
    list_display = ('pref_id', 'name', 'latitude', 'longitude')  # 一覧に出したい項目
admin.site.register(Pref, PrefAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ('pref_id', 'city_id', 'name', 'latitude', 'longitude')  # 一覧に出したい項目
admin.site.register(City, CityAdmin)
