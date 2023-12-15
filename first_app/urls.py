from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home_page'),
    path('signup/',views.user_signup,name='signup_page'),
    path('profile/',views.user_profile,name='profile'),
    path('login/',views.user_login,name='login_page'),
    path('logout/',views.user_logout,name='logout_page'),
    path('profile/Password_change/',views.password_change,name='Password_change'),
]