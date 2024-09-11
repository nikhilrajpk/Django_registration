from django.urls import path
from . import views
urlpatterns = [
    path('',views.signupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.homePage,name='home'),
    path('logout/',views.logoutPage,name='logout'),
    path('user/',views.user_list,name='user_list'),
    path('user/new/',views.user_create,name='user_create'),
    path('user/update/',views.user_update,name='user_update'),
    path('user/delete/',views.user_delete,name='user_delete'),
]