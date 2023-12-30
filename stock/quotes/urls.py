from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getTopNews, name="news"),
    path('search_stock', views.search_stock, name="search_stock"),
    path('add_stock', views.add_stock, name="add_stock"),
    path('delete/<stock_id>', views.delete, name="delete"), 
    path('news', views.getTopNews, name="news"),
    path('search_news', views.getNews, name="search_news"),
]