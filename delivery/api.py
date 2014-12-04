

__author__ = 'edx'
from .models import *
from rest_framework import viewsets
from tastypie.resources import ModelResource
# Create your views here.
from rest_framework import serializers
from geopy.distance import vincenty
from geopy.geocoders import Nominatim


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    #precio_mas_iva = serializers.SerializerMethodField('get_iva')

    #def get_iva(self, foo):
     #   return foo.precio * 1.15
    class Meta:
        model = Menu
        fields = ('url', 'id', 'nombre', 'descripcion', 'precio', 'imagen')
        read_only_fields = ('imagen',)


class RestauranteSerializer(serializers.HyperlinkedModelSerializer):
    distancia_km = serializers.SerializerMethodField('get_dist')
    direccion = serializers.SerializerMethodField('get_address')

    def get_dist(self, rest):
        request = self.context['request']
        latitud = request.QUERY_PARAMS.get('lat')
        longitud = request.QUERY_PARAMS.get('lon')
        distancia = 0
        if latitud is not None and longitud is not None:
            user_position = (float(latitud), float(longitud))
            rest_position = (float(rest.coordenadas.latitude), float(rest.coordenadas.longitude))
            distancia = vincenty(user_position, rest_position).km
        return round(distancia, 2)

    def get_address(self, rest):
        geolocator = Nominatim()
        ubicacion = geolocator.reverse(str(rest.coordenadas.latitude) + "," + str(rest.coordenadas.longitude))
        return ubicacion.address

    class Meta:
        model = Restaurante
        fields = ('url', 'id', 'distancia_km', 'nombre', 'telefono', 'coordenadas', 'direccion')


class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = ('url', 'id', 'cliente', 'telefono', 'direccion', 'total', 'estado', 'restaurante', 'detallepedido_set', )
        #depth = 1


class DetallePedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetallePedido

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente

class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comentario
        fields = ('url', 'id', 'cliente', 'comentario', )

########################


class MenuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_fields = ('id', 'precio', 'nombre')


class ClienteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_fields = ('id', 'social_id', 'nombre')


class RestaurantesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    filter_fields = ('id', 'cliente', 'telefono', 'estado')


class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

