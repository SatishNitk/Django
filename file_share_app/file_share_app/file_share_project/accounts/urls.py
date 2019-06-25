from django.urls import path,include
from accounts.views import *

urlpatterns = [
    path('home/', home_view, name="home_view"),
    path('login/', login_view, name="login_view"),
    path('signup/', signup_view, name="signup_view"),
    path('logout/', logout_view, name="logout_view"),
    path('upload/', upload_view, name="upload_view"),

]
