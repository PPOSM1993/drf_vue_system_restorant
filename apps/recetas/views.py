from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RecetaSerializer
from .models import Receta
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.order_by('-id').all()
    serializer_class = RecetaSerializer
    permission_classes = [AllowAny]
    

    
    
    