from django.urls import path, re_path
from django1.views import index, index1, index2, index3
urlpatterns = [
 path('', index, name='index'),
 # path('<int:year>/<str:month>/', index1, name='index1'),
 # re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/',index2, name='index2'),
 re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/',index3, name='index3'),

 ]