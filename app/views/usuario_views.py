
from django.contrib.auth.forms import UserChangeForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from app.forms.usuario_forms import UsuarioForm, UsuarioUpdateForm
from app.models import User


class UsuarioCreateView(CreateView):
    model = User
    form_class = UsuarioForm
    template_name = "usuarios/form_usuario.html"
    success_url = reverse_lazy("lista_usuarios")


class UsuarioListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "usuarios/lista_usuarios.html"


class UsuarioDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "usuarios/lista_usuario.html"
    context_object_name = "usuario"


class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UsuarioUpdateForm
    template_name = "usuarios/form_usuario.html"
    success_url = reverse_lazy("lista_usuarios")


class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "usuarios/remover_usuario.html"
    context_object_name = "usuario"
    success_url = reverse_lazy("lista_usuarios")
