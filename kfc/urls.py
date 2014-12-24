from django.conf.urls import patterns, include, url
from django.contrib import admin
from delivery.api import *
from kfc import settings
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'pedido', PedidoViewSet)
#router.register(r'detalle_pedido', DetallePedidoViewSet)
router.register(r'restaurantes', RestaurantesViewSet)
router.register(r'clientes',ClienteViewSet)
router.register(r'comentarios',ComentarioViewSet)
#router.register(r'comentarios_Post',ComentarioPOST_ViewSet)

#menu_resource = MenuResource()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kfc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
 #   url(r'^api2/', include(menu_resource.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}),
)
