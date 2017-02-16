from django.contrib import admin

# Register your models here.
from shop.models import Darts


class DartsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'time', 'station', 'holiday', 'tel', 'url', 'dartslive', 'latitude', 'longitude', 'information')  # 一覧に出したい項目
    list_display_links = ('name',)  # 修正リンクでクリックできる項目
admin.site.register(Darts, DartsAdmin)
