from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
]

router = DefaultRouter()
router.register('recetas', views.RecetasViewSet, basename='recetas')
urlpatterns += router.urls