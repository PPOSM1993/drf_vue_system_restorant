from django.urls import path
from .views import *

urlpatterns = [
    path('recetas/editar/foto', EditarFoto.as_view(), name='editar_foto'),
    path('recetas/slug/<str:slug>', Clase2.as_view()),
    path('recetas_home', Clase3.as_view(), name='recetas_home'),
    path('recetas_panel/<int:id>', Clase4.as_view()),
    path('recetas_buscador', Clase5.as_view()),

]