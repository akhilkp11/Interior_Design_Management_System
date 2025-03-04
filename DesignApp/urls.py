from django.urls import path
from DesignApp import views

urlpatterns = [
    path('category_page/', views.category_page, name="category_page"),
    path('filter_design/<ct_name>/', views.filter_design, name="filter_design"),
    path('design_single/<int:d_id>/', views.design_single, name="design_single"),
    path('consultation_submit/', views.consultation_submit, name="consultation_submit"),
    path('booked_design_page/', views.booked_design_page, name="booked_design_page"),
    path('daily_progress/<int:c_id>/', views.daily_progress, name="daily_progress"),

    path('estimate_page/', views.estimate_page, name="estimate_page"),
    path('calculate_estimate/', views.calculate_estimate, name="calculate_estimate"),

    # path for download button to download design as pdf
    # path('download_pdf/<int:d_id>/', views.download_pdf, name='download_pdf'),
    path('design/<int:d_id>/download/', views.download_design_pdf, name='download_design_pdf'),
]