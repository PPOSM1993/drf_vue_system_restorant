from django.urls import path
from .views import *

urlpatterns = [
    path('recetas', RecetasView.as_view(), name='recetas'),
    path('recetas/<int:id>', EdicionRecetas.as_view(), name='edicion_recetas'),
]