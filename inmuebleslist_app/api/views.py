from django.shortcuts import get_object_or_404
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from inmuebleslist_app.models import Edificacion, Empresa, Comentario
from inmuebleslist_app.api.serializers import EdificacionSerializer, EmpresaSerializer, ComentarioSerializer
from inmuebleslist_app.api.permissions import AdminOrReadOnly


class ComentarioCreate(generics.CreateAPIView):
    serializer_class = ComentarioSerializer
    
    def get_queryset(self):
        return Comentario.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        inmueble = Edificacion.objects.get(pk=pk)
        serializer.save(edificacion=inmueble)
            
            
        user = self.request.user
        comentario_queryset = Comentario.objects.filter(edificacion=inmueble, comentario_user=user)
        
        if comentario_queryset.exists():
            raise ValidationError('El usuario ya escribio un comentario para este inmueble')
        
        serializer.save(edificacion=inmueble, comentario_user=user)
class ComentarioList(generics.ListCreateAPIView):
    #queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comentario.objects.filter(edificacion=pk)
    
class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

# class ComentarioList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Comentario.objects.all()
#     serializer_class = ComentarioSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    

# class ComentarioDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Comentario.objects.all()
#     serializer_class = ComentarioSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

class EmpresaVS(viewsets.ModelViewSet):
    permission_classes = [AdminOrReadOnly] #Autorización para acceder a una api
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

# class EmpresaVS(viewsets.ViewSet):
    
#     def list(self, request):
#         queryset = Empresa.objects.all()
#         serializer = EmpresaSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         queryset = Empresa.objects.all()
#         edificacionlist = get_object_or_404(queryset, pk=pk)
#         serializer = EmpresaSerializer(edificacionlist)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = EmpresaSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def update(self, request, pk):
#         try:
#             empresa = Empresa.objects.get(pk=pk)
#         except Empresa.DoesNotExist:
#             return Response({'Error': 'Empresa no encontrada'}, status=status.HTTP_400_BAD_REQUEST)

#         serializer = EmpresaSerializer(empresa, data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
#     def destroy(self, request, pk):
#         try:
#             empresa = Empresa.objects.get(pk=pk)
#         except Empresa.DoesNotExist:
#             return Response({'Error': 'Empresa no encontrada'}, status=status.HTTP_400_BAD_REQUEST)

#         serializer = EmpresaSerializer(empresa, data=request.data)
        
#         empresa.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# class EmpresaAV(APIView):
    
#     def get(self, request):
#         empresa = Empresa.objects.all()
#         serializer = EmpresaSerializer(empresa, many=True, context={'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = EmpresaSerializer(data=request.data) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        

class EmpresaDetalleAV(APIView):        
    def get(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response ({'Error': 'empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmpresaSerializer(empresa, context={'request': request})
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response ({'Error': 'empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmpresaSerializer(empresa, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response ({'Error': 'empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EdificacionAV(APIView):
    
    def get(self, request):
        inmuebles = Edificacion.objects.all()    
        serializer = EdificacionSerializer(inmuebles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EdificacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EdificacionDetalleAV(APIView):
    
    def get(self, request, pk):
        try:
            inmueble = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'Error': 'Inmueble no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EdificacionSerializer(inmueble)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            inmueble = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'Error': 'Inmueble no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EdificacionSerializer(inmueble, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, pk):
        try:
            inmueble = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'Error': 'Inmueble no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        inmueble.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def inmueble_list(request):
    # """Handles GET and POST requests for the Inmueble model, returning a serialized data response."""
    # if request.method == 'GET':
        # inmuebles = Inmueble.objects.all()
        # serializer = InmuebleSerializer(inmuebles, many=True)
        # return Response(serializer.data)
        # 
        # 
    # 
    # if request.method == 'POST':
        # de_serializer = InmuebleSerializer(data=request.data)
        # if de_serializer.is_valid():
            # de_serializer.save()
            # return Response(de_serializer.data)
        # else:
            # return Response(de_serializer.errors)
        # 
# 
# 
# @api_view(['GET', 'PUT', 'DELETE'])
# def inmueble_detalle(request, pk):
    # """Handles GET request for a single Inmueble instance, returning its serialized data."""
    # if request.method == 'GET':
        # try:
            # inmueble = Inmueble.objects.get(pk=pk)
            # serializer = InmuebleSerializer(inmueble)
            # return Response(serializer.data)
        # except Inmueble.DoesNotExist:
            # return Response({'Error': 'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)
    # 
    # if request.method == 'PUT':
        # inmueble = Inmueble.objects.get(pk=pk)
        # de_serializer = InmuebleSerializer(inmueble, data=request.data)
        # if de_serializer.is_valid():
            # de_serializer.save()
            # return Response(de_serializer.data)
        # else:
            # return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 
    # if request.method == 'DELETE':
        # try:
            # inmueble = Inmueble.objects.get(pk=pk)
            # inmueble.delete()
        # 
        # except Inmueble.DoesNotExist:
            # return Response({'Error': 'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)
        # 
        # return Response(status=status.HTTP_204_NO_CONTENT)