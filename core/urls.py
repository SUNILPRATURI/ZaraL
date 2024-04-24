from django.urls import path
from . import views

urlpatterns = [
    path('auth/instructor/register/', views.register, name='register'),
    
    
    path('accounts/login/', views.user_login, name='login'),
    
    
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('change_password/', views.change_password_no_auth, name='change_password'),
    path('auth/change_password/', views.change_password_auth, name='change_password_auth'),
    path('redirect/login/',views.redirect_login,name='redirect-login'),
    path('',views.index,name = 'index'),
    
    
    
    path('register/', views.register_student, name='register_student'),
    
    
]