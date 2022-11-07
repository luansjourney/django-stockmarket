from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('about/', views.About, name="about"),
    path('add_stock/', views.AddStock, name="add_stock"),
    path('delete_stock/', views.DeleteStock, name="delete_stock"),
    path('delete/<stock_id>', views.Delete, name="delete")
]
