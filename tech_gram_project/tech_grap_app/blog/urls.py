from django.urls import path,include
from blog.views import blog_home,one_blog_detail

urlpatterns = [
    path("",blog_home, name="blog_home_page"),
 	path("<int:blog_id>",one_blog_detail, name="one_blog_details") 
]
