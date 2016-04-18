from django.conf.urls import url
from . import views
# ToDos urls
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/', views._add),
    url(r'^list/', views.list),
]
