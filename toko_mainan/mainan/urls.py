from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainan_list, name='mainan_list'),
    path('tambah/', views.mainan_create, name='mainan_create'),   # ⬅️ INI YANG HILANG
    path('edit/<int:id>/', views.mainan_update, name='mainan_update'),
    path('hapus/<int:id>/', views.mainan_delete, name='mainan_delete'),
]
