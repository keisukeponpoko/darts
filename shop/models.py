from django.db import models

# Create your models here.
class Darts(models.Model):
    name = models.CharField('書籍名', max_length=255)
    latitude = models.DecimalField('緯度', max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField('経度', max_digits=9, decimal_places=6, default=0)
    holiday = models.CharField('定休日', max_length=255)
    time = models.CharField('営業時間', max_length=255)
    address = models.CharField('住所', max_length=255)
    information = models.TextField('店舗情報')
    dartslive = models.IntegerField('DARTSLIVE2', blank=True, default=0)
    url = models.CharField('URL', max_length=255)
    tel = models.CharField('TEL', max_length=255)
    station = models.CharField('最寄駅', max_length=255)

class Pref(models.Model):
    pref_id = models.IntegerField('都道府県ID', blank=False)
    name = models.CharField('都道府県名', max_length=255)
    latitude = models.DecimalField('緯度', max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField('経度', max_digits=9, decimal_places=6, default=0)

class City(models.Model):
    city_id = models.IntegerField('市区町村ID', blank=False)
    pref_id = models.IntegerField('都道府県ID', blank=False)
    city_part_id = models.IntegerField('市区町村PartID', blank=False)
    name = models.CharField('市区町村名', max_length=255)
    latitude = models.DecimalField('緯度', max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField('経度', max_digits=9, decimal_places=6, default=0)

class Line(models.Model):
    line_id = models.IntegerField('路線ID', blank=False)
    name = models.CharField('路線名', max_length=255)

class LineStation(models.Model):
    line_id = models.IntegerField('路線ID', blank=False)
    station_id = models.IntegerField('駅ID', blank=False)

class Station(models.Model):
    station_id = models.IntegerField('駅ID', blank=False)
    pref_id = models.IntegerField('都道府県ID', blank=False)
    city_id = models.IntegerField('市区町村ID', blank=False)
    name = models.CharField('都道府県名', max_length=255)
    latitude = models.DecimalField('緯度', max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField('経度', max_digits=9, decimal_places=6, default=0)
