from django.urls import path
from WebApp import views

urlpatterns = [
    path('', views.display_home, name="home"),
    path('save_contact_homepage/', views.save_contact_homepage, name="save_contact_homepage"),
    path('shop/', views.display_shop, name="shop"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('save_contact/', views.save_contact, name="save_contact"),

    path('products/', views.all_products, name="products"),
    path('filtered_products/<cat>/', views.filtered_products, name="filtered_products"),
    path('single_product/<int:pr_id>/', views.single_product, name="single_product"),
    path('save_cart/', views.save_cart, name="save_cart"),
    path('delete_cart_item/<int:c_id>/', views.delete_cart_item, name="delete_cart_item"),
    path('cart_page/', views.cart_page, name="cart_page"),
    path('return_policy/', views.return_policy, name="return_policy"),
    path('checkout/', views.checkout, name="checkout"),
    path('save_order/', views.save_order, name="save_order"),
    path('payment/', views.payment, name="payment"),

    path('signup_page', views.signup_page, name="signup_page"),
    # path('signup_page/', views.signup_page, name="signup_page"),
    path('user_signup/', views.user_signup, name="user_signup"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_sign_out/', views.user_sign_out, name="user_sign_out"),
    path('edit_profile_page/', views.edit_profile_page, name="edit_profile_page"),
    path('update_user/', views.update_user, name="update_user"),

    # design section
    path('homepage/', views.homepage, name="homepage")
]
