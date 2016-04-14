'''
    Authentication urls for ToDos Users
    Author: Rajmani Arya
'''
from django.conf.urls import url
from . import views

# Authentiction urls

urlpatterns = [
    url(r'^login/', views._login),
    url(r'^signup/', views._register),
    url(r'^change_password', views._changePassword),
    url(r'^logout', views._logout),
    url(r'^upload', views._upload),
    url(r'^profile', views._profile),
]
