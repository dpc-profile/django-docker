from django.urls import path
from . import views

app_name = 'courses'  # Em urls.py de outras paginas altere o appname para
                      # de acordo com a pasta acima. Ex: 'courses' por causa
                      # do core/courses.py
urlpatterns = [
    path('', views.index, name='index')
]