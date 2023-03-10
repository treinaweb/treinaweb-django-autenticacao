from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class UsuarioCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "usuarios/form_usuario.html"
    success_url = reverse_lazy("lista_usuarios")
