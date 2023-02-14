from django.urls import path

# from inmuebleslist_app.api.views import inmueble_list, inmueble_detalle
from inmuebleslist_app.api.views import EmpresaAV, EdificacionAV, EdificacionDetalleAV

urlpatterns = [
    path('list/', EdificacionAV.as_view(), name='edificacion'),
    path('<int:pk>', EdificacionDetalleAV.as_view(), name='edificacion-detalle'),
    path('empresa/', EmpresaAV.as_view(), name='empresa'),
]
