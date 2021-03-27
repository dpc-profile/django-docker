from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'   # Em urls.py de outras paginas altere o appname para
                    # de acordo com a pasta acima. Ex: 'core' por causa
                    # do core/urls.py

urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
