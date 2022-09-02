from multiprocessing import context
from django.shortcuts import render
from django.views.generic.list import ListView

from app_ventas.models import categoria


class CategoriaListView(ListView):
    model = categoria
    template_name = 'categoria/categoria_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado Categorias'

        return context
