from django.urls import path
from AdminApp import views

urlpatterns = [
    # E-commerce section
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


    path('display_booking/', views.display_booking, name="display_booking"),


    # interior design section
    path('add_design_category/', views.add_design_category, name="add_design_category"),
    path('save_design_category/', views.save_design_category, name="save_design_category"),
    path('display_design_category/', views.display_design_category, name="display_design_category"),
    path('add_designs/', views.add_designs, name="add_designs"),
    path('save_designs/', views.save_designs, name="save_designs"),
    path('display_designs/', views.display_designs, name="display_designs"),
    path('edit_designs/<int:d_id>/', views.edit_designs, name="edit_designs"),
    path('update_designs/<int:d_id>/', views.update_designs, name="update_designs"),
    path('delete_designs/<int:d_id>/', views.delete_designs, name="delete_designs"),


]