from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start_vm', views.start_vm, name='start_vm'),
    path('req_vm', views.req_vm, name='req_vm'),
    path('show_vm', views.show_vm, name='show_vm'),
]