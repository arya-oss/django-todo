from django.conf.urls import url
from . import views
# ToDos urls
urlpatterns = [
    url(r'^$', views.index, name='todo_index'),
    url(r'^list/', views.list, name='todo_list')
]
