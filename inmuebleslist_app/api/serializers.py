from rest_framework import serializers
from inmuebleslist_app.models import Inmueble

def column_longitude(value):
    if len(value) <2:
        raise serializers.ValidationError('El valor es demasiado corta')

class InmuebleSerializer(serializers.Serializer):
    """Serializer for the Inmueble model, converts data to Python structure for rendering into JSON or other content types."""
    id = serializers.IntegerField(read_only=True)
    direccion = serializers.CharField(validators=[column_longitude])
    pais = serializers.CharField(validators=[column_longitude])
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
    
    def validate(self, data):
        if data['direccion']==data['pais']:
            raise serializers.ValidationError('La dirección y el país no pueden ser el mismo')
        
        else: 
            return data
        
    def validate_imagen(self, data):
        if len(data) < 2:
            raise serializers.ValidationError('La url es muy corta')
        
        else: 
            return data