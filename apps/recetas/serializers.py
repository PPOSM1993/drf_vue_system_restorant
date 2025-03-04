from rest_framework import serializers
from .models import Recetas
from dotenv import load_dotenv
import os


class RecetasSerializer(serializers.ModelSerializer):
    #categoria = serializers.CharField(source='categoria.nombre')
    #categoria = serializers.ReadOnlyField(source='categorias.nombre')
    #foto = serializers.SerializerMethodField()
    #foto = serializers.ImageField(use_url=True)
    fecha = serializers.DateTimeField(format="%d/%m/%Y")#13/10/2025
    
    class Meta:
        model = Recetas
        fields = ("id", "nombre", "slug", "tiempo", "descripcion", "fecha", "categoria", "categoria_id", "foto")
        
    
    def get_imagen(self, obj):
        return f"{os.getenv("BASE_URL")}uploads/recetas/{obj.foto}"