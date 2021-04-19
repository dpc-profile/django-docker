from django.urls import path, re_path, include
from . import views

app_name = 'accounts'                     
                      

'''
urlpatterns = [
    path('entrar/', include('django.contrib.auth.urls'),
    {'template_name': 'accounts/login.html'},
    name='login'
    )
]
'''
urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='login'),
    path('register/', views.register, name='register'),
    re_path(r'^entrar/', include('django.contrib.auth.urls'), name='login'),
]