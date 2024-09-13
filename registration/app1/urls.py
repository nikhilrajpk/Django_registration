from django.urls import path
from . import views
urlpatterns = [
    path('',views.signupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.homePage,name='home'),
    path('logout/',views.logoutPage,name='logout'),
    path('adminPage/',views.adminPage,name='adminPage'),
    path('create/',views.create,name='create'),
    path('edit/',views.edit,name='edit'),
]