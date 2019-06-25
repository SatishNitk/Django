from django.urls import path
from accounts.views import *


urlpatterns = [
    path('', account_home_page,name="account_home"),
	path('login/', account_login_page,name="account_login"),
    path('logout/', account_logout_page,name="account_logout"),
    path('signup/', account_signup_page,name="account_signup"),
]
