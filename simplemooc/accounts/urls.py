#Accounts/urls
from django.urls import path, re_path, include
from django.conf import settings
from . import views as views_accounts
from django.contrib.auth import views as view_auth

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='login'),
    path(r'', views_accounts.dashboard, name='dashboard'),
    path(r'entrar/', include('django.contrib.auth.urls'), name='login'),
    path(r'cadastre-se/', views_accounts.register, name='register'),
    path(r'sair/', view_auth.LogoutView.as_view(next_page = settings.LOGIN_REDIRECT_URL), name='logout'),
    
    
]