from django.urls import path
from DesignApp import views

urlpatterns = [
    path('category_page/', views.category_page, name="category_page"),
    path('filter_design/<ct_name>/', views.filter_design, name="filter_design"),
]