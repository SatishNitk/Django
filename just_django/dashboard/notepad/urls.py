from django.conf.urls import url,include
from notepad.views import *


urlpatterns = [
    url(r'^create/', create_view, name="create"),
    url(r'^list/', list_view, name="list"),
    url(r'^(?P<note_id>\d+)/delete/', delete_view, name="delete"),
    url(r'^(?P<note_id>\d+)/update/', update_view, name="update"),

 	 
]
