from django.urls import path
from blog_app.views import index,project_index,project_detail
from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = [
    path('index/', index ,name="index"),
    path('blog/', project_index ,name="project_index"),
    path('project_detail/<int:pk>/', project_detail ,name="project_detail"),
]

