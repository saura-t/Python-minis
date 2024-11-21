from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_emp, name='add_emp'),
    path('process-add/', views.process_add_emp, name='process_add_emp'),
    path('delete-emp/<int:idemp>/', views.delete_emp, name='delete_emp'),
    path('update-emp/<int:idemp>/', views.update_emp, name='update_emp'),
]