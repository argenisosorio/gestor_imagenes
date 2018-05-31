# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,ListView, View
from django.views.generic import FormView, RedirectView, CreateView, DeleteView, UpdateView, ListView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from registro.models import Imagen
from registro.forms import ImagenForm
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import forms, login, logout, authenticate
from django.views.generic import View
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import LoginForm


class LoginView(FormView):
    template_name = 'registro/login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('registro:buscar')

    def form_valid(self, form):
        usuario = form.cleaned_data['username']
        contrasena = form.cleaned_data['password']
        usuario = authenticate(username=usuario, password=contrasena)
        login(self.request, usuario)
        return super(LoginView, self).form_valid(form)


class Guardar_imagen(SuccessMessageMixin, CreateView):
    """
    Clase que permite guardar las imagenes, se guardan en /media en
    la raíz del proyecto.
    """
    model = Imagen
    form_class = ImagenForm
    template_name = "registro/guardar_imagen.html"
    success_url = reverse_lazy('registro:buscar')
    success_message = "Se guardó la imagen con éxito"


class Lista_imagenes(ListView):
    """
    Clase que permite listar las imagenes registradas.
    """
    model = Imagen
    template_name = "registro/lista_imagenes.html"


class Editar_imagen(SuccessMessageMixin, UpdateView):
    """
    Clase que permite editar las imagenes registradas.
    """
    template_name = "registro/guardar_imagen.html"
    form_class = ImagenForm
    model = Imagen
    success_message = "Se actualizó la información con éxito"
    success_url = reverse_lazy('registro:buscar')


class Borrar_imagen(SuccessMessageMixin, DeleteView):
    """
    Clase que permite borrar las imagenes.
    """
    form_class = ImagenForm
    model = Imagen
    success_message = "Se eliminó la información con éxito"
    success_url = reverse_lazy('registro:lista_imagenes')


def buscar(request):
    """
    Función que muestra la plantilla con el formulario de búsqueda.
    """
    return render(request, 'registro/buscar.html')


def busqueda(request):
    """
    Función que permite hacer el query con las imagenes ya filtrados.
    """
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        #imagenes = imagen.objects.filter(cedula__icontains=q)
        imagenes = Imagen.objects.filter(tag__icontains=q)
        if imagenes:
            return render(request, 'registro/buscar.html',  {'imagenes': imagenes, 'query': q})
        else:
            messages = ['No se encontró ningúna imagen.']
            return render_to_response('registro/buscar.html', {'messages': messages}, context_instance=RequestContext(request))
    else:
        messages = ['Por favor introduce una etiqueta.']
        return render_to_response('registro/buscar.html', {'messages': messages}, context_instance=RequestContext(request))


class Salir(View):
    """
    Clase que permite cerrar la sesión de usuario.
    """

    def get(self, request):
        """
        Método que redireccíona cuando se cierra la sesión.
        """
        logout(request)
        return redirect('/')
