from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('curso/<int:id>', views.curso, name='curso'),
    path('aula/<int:id>', views.aula, name = 'aula'),
    path('comentarios/', views.comentarios, name='comentarios'),
    path('processa_avaliacao/', views.processa_avaliacao, name = 'processa_avaliacao')
]
