from django.urls import path, re_path
from . import views

app_name = 'courses'  # Em urls.py de outras paginas altere o appname para
                      # de acordo com a pasta acima. Ex: 'courses' por causa
                      # do core/courses.py
urlpatterns = [
    path('', views.index, name='index'),
    #re_path(r'^(?P<pk>\d+)/$', views.details, name='details'),
    re_path(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'),
]
#Sobre o re_path:
#pk = pega a partir da primary key do banco de dados. Comentada por ter sido substituido pelo metodo slug.
#
#?P = cria um grupo.
#slug = é um 'atalho' criado com base no nome do curso. Duvida acessa o admin do sistema
#\w_- = caracteres alfanumericos, que podem ter na sua composição _ e -
#+ = pode ocorrer 1 ou mais vezes.