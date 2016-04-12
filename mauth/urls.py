from django.conf.urls import url
from . import views
# Auth urls
urlpatterns = [
    url(r'^$', views.index, name='auth_index'),
    url(r'^login/', views.login, name='auth_login')
]
