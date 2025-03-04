from http import HTTPStatus
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Recetas
from .serializers import RecetasSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse
import os
from datetime import datetime
from django.core.files.storage import FileSystemStorage

# Create your views here.
class RecetasViewSet(viewsets.ModelViewSet):
    queryset = Recetas.objects.order_by('-id').all()
    serializer_class = RecetasSerializer
    permission_classes = [AllowAny]
    
    def list(self, request):
        queryset = Recetas.objects.order_by('-id').all()
        serializer = RecetasSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = RecetasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            data = Recetas.objects.filter(id=id).get()
        except Recetas.DoesNotExist:
            return JsonResponse({"estado":"error", "mensaje":"Recurso no disponible"}, status=HTTPStatus.NOT_FOUND)
        #borrar la foto de la carpeta
        os.remove(f"./uploads/recetas/{data.foto}")
        #borrar el registro de la bd
        Recetas.objects.filter(id=id).delete()
        return JsonResponse({"estado":"ok", "mensaje":"Se elimina el registro exitosamente"}, status=HTTPStatus.OK)
"""        queryset = Recetas.objects.all()
        receta = get_object_or_404(queryset, pk=pk)
        
        receta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""