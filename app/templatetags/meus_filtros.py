from django import template

register = template.Library()


@register.filter(name="remover_caracter")
def remover_caracter(var, caracter):
    return var.replace(caracter, '')