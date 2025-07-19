"""
URL configuration for project_name project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views  # ✅ app name is 'home'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="home"),  # ✅ root path
    path('menu',views.menu,name="menu"),
    path('orderonline',views.orderonline,name="orderonline"),
    path('aboutus',views.aboutus,name="aboutus"),
     path('contactus',views.contactus,name="contactus"),
     path('deliveron', views.deliveron, name="deliveron"),
     path('menu/', views.menu, name='menu'),
     path('cart/', views.cart, name='cart'),
     # in urls.py
    path('add_to_cart/<str:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<str:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-quantity/<str:item_id>/', views.update_quantity, name='update_quantity'),
    path('checkout/',views.check,name="checkout"),
    path('view/',views.view_menu,name='view'),
     path('clear-cart/', views.clear_cart, name='clear_cart'),

 


    

]
admin.site.site_header = "<3 BrewBaar! Cafeteria"
admin.site.site_title = "BrewBaar! Admin Portal"
admin.site.index_title = "Welcome to BrewBaar! Cafeteria"