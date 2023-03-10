from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from app.forms.usuario_forms import UsuarioForm, UsuarioUpdateForm


class UsuarioCreateView(CreateView):
    model = User
    form_class = UsuarioForm
    template_name = "usuarios/form_usuario.html"
    success_url = reverse_lazy("lista_usuarios")


class UsuarioListView(ListView):
    model = User
    template_name = "usuarios/lista_usuarios.html"


class UsuarioDetailView(DetailView):
    model = User
    template_name = "usuarios/lista_usuario.html"
    context_object_name = "usuario"


class UsuarioUpdateView(UpdateView):
    model = User
    form_class = UsuarioUpdateForm
    template_name = "usuarios/form_usuario.html"
    success_url = reverse_lazy("lista_usuarios")


class UsuarioDeleteView(DeleteView):
    model = User
    template_name = "usuarios/remover_usuario.html"
    context_object_name = "usuario"
    success_url = reverse_lazy("lista_usuarios")
