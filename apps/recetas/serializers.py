from rest_framework import serializers
from .models import Receta

class RecetaSerializer(serializers.ModelSerializer):
    
    categoria = serializers.ReadOnlyField(source='categoria.nombre')
    fecha = serializers.DateTimeField(format="%d-%m-%Y")
    class Meta:
        model = Receta
        fields = ('id', 'nombre', 'slug', 'tiempo', 'descripcion', 'fecha', 'categoria','categoria_id')
    