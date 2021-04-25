from django.urls import path, re_path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='login'),
    re_path(r'^entrar/', include('django.contrib.auth.urls'), name='login'),
    path(r'cadastre-se/', views.register,name='register'),
    
]