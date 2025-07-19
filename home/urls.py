from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.menu, name='menu'),
    path('orderonline/', views.orderonline, name='orderonline'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('deliveron/', views.deliveron, name='deliveron'),  # ✅ Add this
    path('cart/',views.cart,name="cart"),
]
