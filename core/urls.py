from django.urls import path
from .views import employee_list, employee_form, employee_update, employee_delete, contact


urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('employee-form/', employee_form, name='employee_form'),
    path('employee-form/<int:id>/', employee_update, name='employee_update'),
    path('delete/<int:id>/', employee_delete, name='employee_delete'),
    path('contact/', contact, name='contact')
]
