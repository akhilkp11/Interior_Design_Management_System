from django.urls import path
from AdminApp import views

urlpatterns = [
    # E-commerce section
    path('admin_login_page/', views.admin_login_page, name="admin_login_page"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('index/', views.display_index, name="index"),


    path('display_users/', views.display_users, name="display_users"),
    path('edit_users/<int:u_id>/', views.edit_users, name="edit_users"),
    path('update_user/<int:u_id>/', views.update_user, name="update_user"),
    path('delete_user/<int:u_id>/', views.delete_user, name="delete_user"),

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
    path('delete_product/<int:pr_id>/', views.delete_product, name="delete_product"),


    path('display_booking/', views.display_booking, name="display_booking"),


    # interior design section
    path('add_design_category/', views.add_design_category, name="add_design_category"),
    path('save_design_category/', views.save_design_category, name="save_design_category"),
    path('display_design_category/', views.display_design_category, name="display_design_category"),
    path('edit_design_category/<int:d_id>/', views.edit_design_category, name="edit_design_category"),
    path('update_design_category/<int:d_id>/', views.update_design_category, name="update_design_category"),
    path('delete_design_category/<int:d_id>/', views.delete_design_category, name="delete_design_category"),

    path('add_designs/', views.add_designs, name="add_designs"),
    path('save_designs/', views.save_designs, name="save_designs"),
    path('display_designs/', views.display_designs, name="display_designs"),
    path('edit_designs/<int:d_id>/', views.edit_designs, name="edit_designs"),
    path('update_designs/<int:d_id>/', views.update_designs, name="update_designs"),
    path('delete_designs/<int:d_id>/', views.delete_designs, name="delete_designs"),


    path('display_consultation/', views.display_consultation, name="display_consultation"),
    path('book_consult_status/<int:c_id>/', views.book_consult_status, name="book_consult_status"),
    path('work_progress/<int:c_id>/', views.work_progress, name="work_progress"),
    path('save_daily_progress/<int:c_id>/', views.save_daily_progress, name="save_daily_progress"),
    path('work_progress_edit_page/<int:w_id>/', views.work_progress_edit_page, name="work_progress_edit_page"),
    path('update_work_progress/<int:w_id>/', views.update_work_progress, name="update_work_progress"),
    path('delete_work_progress/<int:w_id>/', views.delete_work_progress, name="delete_work_progress"),


]