from django.contrib import admin
from django.urls import path,include
from app import views
from django.contrib.auth import views as auth_view
from .forms import *
from app import admin
from .api_views import *


urlpatterns = [
     path('', views.home, name='home'),
     path('about/', views.about, name='about'),
     path('contact/', views.contact, name='contact'),
  
    path('category/<slug:value>', views.CategoryView.as_view(), name='category'),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    
    path('address/',views.address,name='address'),
    path('update-address/<int:pk>',views.UpdateAddress.as_view(),name='update_address'),
    path('delete-address/<int:pk>',views.delete_address,name='delete_address'),
    
    path('add-to-cart/',views.add_to_cart,name="add_to_cart"),
    path('cart/',views.show_cart,name='show_cart'),
    path('orders/',views.orders,name='orders'),
    path('search/',views.search,name='search'),
    
    path('checkout/',views.checkout.as_view(),name="checkout"),
    path('paymentdone/',views.payment_done,name='payment_done'),
   
    path('plusCart/',views.plus_cart,name='plus_cart'),
    path('minusCart/',views.minus_cart,name='minus_cart'),
    path('removeCart/',views.remove_cart,name='remove_cart'),
    
    path('wishlist/',views.wishlist,name="wishlist"),
    path('plusWishlist/',views.plus_wishlist,name='plus_wishlist'),
    path('minusWishlist/',views.minus_wishlist,name='minus_wishlist'),
    
         
    # login authentication
      path('registration/', views.RegisterView.as_view(),name='registration'),
      path('accounts/login/', auth_view.LoginView.as_view(template_name = "app/login.html"),name = "login-user"),
      path('logout/',auth_view.LogoutView.as_view(next_page='login-user'),name='user_logout'),
      
      path('user-change-password/',auth_view.PasswordChangeView.as_view(template_name='app/change_password.html',success_url='/passChangeDone'),
      name='user_change_password'),
      path('passChangeDone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/passChangeDone.html'),
      name='passChangeDone'),
     
      path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/password_reset.html'
            ,form_class=ResetPasswordForm), name='user_password_reset'),
      path('user-password-reset-done/',auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html')
            ,name='user_password_reset_done'),
      path('user-password-reset-confirm/',auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html'
            ,form_class=SetPasswordForm), name='user_password_reset_confirm'),
      path('user-password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html')
            ,name='user_password_reset_complete'),
      
]


