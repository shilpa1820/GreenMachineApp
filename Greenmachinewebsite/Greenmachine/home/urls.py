from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name="home"),
    path('aboutus',views.aboutus, name="aboutus"),
    path('contactus',views.contactus, name="contactus"),
    path('gardeningtools',views.gardeningtools,name="gardeningtools"),
    path('plants',views.plants,name="plants"),
    path('seeds',views.seeds,name="seeds"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('register',views.register,name="register"),
    path('userlogout',views.userlogout,name="userlogout"),
    path('logingout',views.logingout,name="logingout")
]