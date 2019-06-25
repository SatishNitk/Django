from django.urls import path
from products.views import *

urlpatterns = [
    path('', product_home_page,name="product_home"),
    path('create/', product_create,name="product_create"),
    path('<int:product_id>/', product_display,name="product_display"),
    path('<int:product_id>/upvote', product_upvote,name="product_upvote"),

]
