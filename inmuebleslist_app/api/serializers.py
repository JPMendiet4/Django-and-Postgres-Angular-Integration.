from rest_framework import serializers
from inmuebleslist_app.models import Edificacion, Empresa, Comentario


class ComentarioSerializer(serializers.ModelSerializer):
    comentario_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comentario
        exclude = ['edificacion']
        #fields = '__all__'


class EdificacionSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)
    class Meta:
        model = Edificacion
        fields = '__all__'
        #fields = ['id', 'pais', 'activo', 'imagen']
        #exclude = ['id']
        
class EmpresaSerializer(serializers.ModelSerializer):
    edificacionlist = EdificacionSerializer(many=True, read_only=True)
    # edificacionlist = serializers.StringRelatedField(many=True)
    # edificacionlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # edificacionlist = serializers.HyperlinkedRelatedField(
    #     many=True, 
    #     read_only=True,
    #     view_name='edificacion-detalle')
    class Meta:
        model = Empresa
        fields = '__all__'


        
        
        
        
        
        
        
        
        
        
        
        
        
    # def get_longitud_direccion(self, object):
    #     cantidad_caracteres = len(object.direccion)
    #     return cantidad_caracteres
        
    # def validate(self, data):
    #     if data['direccion']==data['pais']:
    #         raise serializers.ValidationError('La dirección y el país no pueden ser el mismo')
        
    #     else: 
    #         return data
        
    # def validate_imagen(self, data):
    #     if len(data) < 2:
    #         raise serializers.ValidationError('La url es muy corta')
        
    #     else: 
    #         return data

# def column_longitude(value):
#     if len(value) <2:
#         raise serializers.ValidationError('El valor es demasiado corta')

# class InmuebleSerializer(serializers.Serializer):
#     """Serializer for the Inmueble model, converts data to Python structure for rendering into JSON or other content types."""
#     id = serializers.IntegerField(read_only=True)
#     direccion = serializers.CharField(validators=[column_longitude])
#     pais = serializers.CharField(validators=[column_longitude])
#     descripcion = serializers.CharField()
#     imagen = serializers.CharField()
#     activo = serializers.BooleanField()
    
#     def create(self, validated_data):
#         """Creates a new Inmueble instance with the validated data from the serializer."""
#         return Inmueble.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.direccion = validated_data.get('direccion', instance.direccion)
#         instance.pais = validated_data.get('pasi', instance.pais)
#         instance.descripcion = validated_data.get('descripcion', instance.descripcion)
#         instance.imagen = validated_data.get('imagen', instance.imagen)
#         instance.activo = validated_data.get('activo', instance.activo)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['direccion']==data['pais']:
#             raise serializers.ValidationError('La dirección y el país no pueden ser el mismo')
        
#         else: 
#             return data
        
#     def validate_imagen(self, data):
#         if len(data) < 2:
#             raise serializers.ValidationError('La url es muy corta')
        
#         else: 
#             return data