from django.urls import path
from employee.views import *

urlpatterns = [
    path('add/',employee_add, name="employee_add"),
    path('list/',employee_list, name="employee_list"),
    path('<int:id>/edit/',employee_edit, name="employee_edit"),
    path('<int:id>/delete/',employee_delete, name="employee_delete"),
    path('<int:id>/detail/',employee_detail, name="employee_detail"),
] 
