from django.urls import path,include
from accounts.views import *

urlpatterns = [
    path('home/', home_view, name="home_view"),
    path('login/', login_view, name="login_view"),
    path('signup/', signup_view, name="signup_view"),
    path('logout/', logout_view, name="logout_view"),
    path('upload/', upload_view, name="upload_view"),
    path('delete/<int:pk>/', delete_view, name="delete_view"),
    path('demo/', my_image, name="demo_view"),
    path('book_list/', book_list_view, name='book_list_view'),
    path('book_listu/', book_list_view_by_u, name='book_list_view_by_u'),
    path('book_listother/', book_list_view_by_other, name='book_list_view_by_other'),
    path('downloader/', downloader_view, name='downloader_view'),



]
