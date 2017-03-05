# coding: utf-8

from django import template

register = template.Library()

@register.simple_tag(name='areaUrl')
def areaUrl(pref=13, city=None, category=None, page=None):
    urlParam = '/list/pref=' + str(pref) + '/'
    if city is not None:
        urlParam = urlParam + 'city=' + str(city) + '/'
    if category is not None:
        urlParam = urlParam + 'category=' + str(category) + '/'
    if page is not None:
        urlParam = urlParam + 'page=' + str(page) + '/'

    return urlParam
