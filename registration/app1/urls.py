from django.urls import path
from . import views
urlpatterns = [
    path('',views.signupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.homePage,name='home'),
]