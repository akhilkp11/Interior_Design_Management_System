from django.urls import path
from AdminApp import views

urlpatterns = [
    path('index/', views.display_index, name="index"),
    path('add_category/', views.add_category, name="add_category"),
    path('display_category/', views.display_category, name="display_category"),
    path('save_category/', views.save_category, name="save_category"),
    path('edit_category/<int:ct_id>/', views.edit_category, name="edit_category"),
    path('update_category/<int:ct_id>/', views.update_category, name="update_category"),
    path('delete_category/<int:ct_id>/', views.delete_category, name="delete_category"),

    path('add_product/', views.add_product, name="add_product"),
    path('display_product/', views.display_product, name="display_product"),
    path('save_product/', views.save_product, name="save_product"),
    path('edit_product/<int:pr_id>/', views.edit_product, name="edit_product"),
    path('update_product/<int:pr_id>/', views.update_product, name="update_product"),
]