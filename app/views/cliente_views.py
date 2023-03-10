from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from ..models import Cliente
from ..forms.cliente_forms import ClienteForm, EnderecoForm

# Create your views here.


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/form_cliente.html"
    success_url = "lista_clientes"

    def get_context_data(self, **kwargs):
        context = super(ClienteCreateView, self).get_context_data(**kwargs)
        context["form"] = ClienteForm()
        context["endereco_form"] = EnderecoForm()
        return context

    def post(self, request, *args, **kwargs):
        cliente_form = ClienteForm(data=request.POST)
        endereco_form = EnderecoForm(data=request.POST)
        if cliente_form.is_valid() and endereco_form.is_valid():
            endereco = endereco_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.endereco = endereco
            cliente.save()
            return HttpResponseRedirect(reverse("lista_clientes"))


class ClienteListView(ListView):
    model = Cliente
    template_name = "clientes/lista_clientes.html"
    queryset = Cliente.objects.filter(profissao="Programador").order_by('-data_nascimento')

# Adicionar um comentário
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "clientes/lista_cliente.html"
    context_object_name = "cliente"

    def get_context_data(self, **kwargs):
        context = super(ClienteDetailView, self).get_context_data(**kwargs)
        context["cliente"] = Cliente.objects.select_related("endereco").prefetch_related("dependente").get(id=self.kwargs["pk"])
        return context



class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/form_cliente.html"
    success_url = reverse_lazy("lista_clientes")

    def get_context_data(self, **kwargs):
        context = super(ClienteUpdateView, self).get_context_data(**kwargs)
        context["form"] = ClienteForm(instance=self.object)
        context["endereco_form"] = EnderecoForm(instance=self.object.endereco)
        return context

    def post(self, request, *args, **kwargs):
        cliente = Cliente.objects.get(id=kwargs["pk"])
        cliente_form = ClienteForm(data=request.POST or None, instance=cliente)
        endereco_form = EnderecoForm(data=request.POST or None, instance=cliente.endereco)
        if cliente_form.is_valid() and endereco_form.is_valid():
            endereco = endereco_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.endereco = endereco
            cliente.save()
            return HttpResponseRedirect(reverse("lista_clientes"))


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "clientes/remover_cliente.html"
    success_url = reverse_lazy("lista_clientes")

    def post(self, request, *args, **kwargs):
        cliente = Cliente.objects.get(id=kwargs["pk"])
        cliente.endereco.delete()
        cliente.delete()
        return HttpResponseRedirect(reverse("lista_clientes"))
