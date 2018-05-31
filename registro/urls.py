# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from registro import views
from registro.views import *
from django.conf import settings
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    #url(r'^$', Index.as_view(), name='index'),
    url(r'^$', LoginView.as_view(), name = "login"),
    url(r'^buscar$', login_required(buscar), name='buscar'),
    url(r'^lista_imagenes$', login_required(views.Lista_imagenes.as_view()), name='lista_imagenes'),
    url(r'^guardar_imagen$', login_required(views.Guardar_imagen.as_view()), name='guardar_imagen'),
    url(r'^editar_imagen/(?P<pk>\d+)$', login_required(views.Editar_imagen.as_view()), name='editar_imagen'),
    url(r'^borrar_imagen/(?P<pk>\d+)$', login_required(views.Borrar_imagen.as_view()), name='borrar_imagen'),
    # Definiendo la url que va a servir las imagenes para que puedan ser descargadas.
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    # Definiendo la url que va a servir las imagenes para que puedan ser descargadas luego de filtrar.
    url(r'^busqueda/media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^busqueda/$', login_required(busqueda), name='busqueda'),
    url(r'^salir$', login_required(views.Salir.as_view()), name='salir'),
)
