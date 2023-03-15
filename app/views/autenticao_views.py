from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

class LoginView(View):
    def get(self, request):
        data = {'form': AuthenticationForm}
        return render(request, 'autenticacao/login_usuario.html', data)
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario:
            login(request, usuario)
            return redirect('lista_usuarios')
        else:
            form_login = AuthenticationForm()
            return render(request, 'autenticacao/login_usuario.html', {
                'form': form_login, 'error': 'Usuário ou senha incorretos'
                })