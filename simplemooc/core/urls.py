from django.urls import path
from . import views

app_name = 'core'   # Em urls.py de outras paginas altere o appname para
                    # de acordo com a pasta acima. Ex: 'core' por causa
                    # do core/urls.py

urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contact'),
]