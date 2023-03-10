from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from app.forms.usuario_forms import UsuarioForm


class UsuarioCreateView(CreateView):
    model = User
    form_class = UsuarioForm
    template_name = "usuarios/form_usuario.html"
    success_url = reverse_lazy("lista_usuarios")


class UsuarioListView(ListView):
    model = User
    template_name = "usuarios/lista_usuarios.html"
