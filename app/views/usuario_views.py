
from django.contrib.auth.forms import UserChangeForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy
from app.forms.usuario_forms import UsuarioForm, UsuarioUpdateForm
from app.models import User
from app.mixins import AdminPermissionMixin


class UsuarioCreateView(AdminPermissionMixin, CreateView):
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


class UsuarioUpdateView(UserPassesTestMixin, UpdateView):
    model = User
    form_class = UsuarioUpdateForm
    template_name = "usuarios/form_usuario.html"
    success_url = reverse_lazy("lista_usuarios")

    def test_func(self):
        return self.request.user.is_superuser


class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "usuarios/remover_usuario.html"
    context_object_name = "usuario"
    success_url = reverse_lazy("lista_usuarios")
