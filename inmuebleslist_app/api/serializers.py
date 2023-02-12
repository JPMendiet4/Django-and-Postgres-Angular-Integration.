from rest_framework import serializers
from inmuebleslist_app.models import Inmueble


class InmuebleSerializer(serializers.Serializer):
    """Serializer for the Inmueble model, converts data to Python structure for rendering into JSON or other content types."""
    id = serializers.IntegerField(read_only=True)
    direccion = serializers.CharField()
    pais = serializers.CharField()
    descripcion = serializers.CharField()
    imagen = serializers.CharField()
    activo = serializers.BooleanField()
    
    def create(self, validated_data):
        """Creates a new Inmueble instance with the validated data from the serializer."""
        return Inmueble.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.pais = validated_data.get('pasi', instance.pais)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.activo = validated_data.get('activo', instance.activo)
        instance.save()
        return instance