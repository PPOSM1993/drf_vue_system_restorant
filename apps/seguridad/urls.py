from django.urls import path
from .views import *

urlpatterns = [
    path('seguridad/registro', RegistroUsuario.as_view(), name='registro'),
    path('seguridad/verificacion/<str:token>', VerificacionUsurio.as_view(), name='verificacion'),
    path('seguridad/login', LoginView.as_view(), name='login'),
]