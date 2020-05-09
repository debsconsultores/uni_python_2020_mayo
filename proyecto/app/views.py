from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views import generic

# from app.models import Categoria
from .models import Categoria,SubCategoria, Marca
from .forms import CategoriaForm,SubCategoriaForm

# Create your views here.
def hola_mundo(request):
    return HttpResponse("Hola Mundo a los de INATEC")


class CategoriaListar(generic.ListView):
    model=Categoria
    template_name='app/categoria_list.html'
    context_object_name='obj'
    ordering="descripcion"


class CategoriaNueva(generic.CreateView):
    model=Categoria
    template_name='app/categoria_form.html'
    context_object_name='obj'
    form_class=CategoriaForm
    success_url=reverse_lazy('app:categoria_listar')


class CategoriaEditar(generic.UpdateView):
    model=Categoria
    template_name='app/categoria_form.html'
    context_object_name='obj'
    form_class=CategoriaForm
    success_url=reverse_lazy('app:categoria_listar')


class CategoriaBorrar(generic.DeleteView):
    model=Categoria
    template_name='app/borrar.html'
    context_object_name='obj'
    # form_class=CategoriaForm    
    success_url=reverse_lazy('app:categoria_listar')


class SubCategoriaListar(generic.ListView):
    model=SubCategoria
    template_name='app/subcategoria_list.html'
    context_object_name='obj'


class SubCategoriaNueva(generic.CreateView):
    model=SubCategoria
    template_name='app/subcategoria_form.html'
    context_object_name='obj'
    form_class=SubCategoriaForm
    success_url=reverse_lazy('app:subcategoria_listar')


class SubCategoriaEditar(generic.UpdateView):
    model=SubCategoria
    template_name='app/subcategoria_form.html'
    context_object_name='obj'
    form_class=SubCategoriaForm
    success_url=reverse_lazy('app:subcategoria_listar')


class SubCategoriaBorrar(generic.DeleteView):
    model=SubCategoria
    template_name='app/borrar.html'
    context_object_name='obj'
    success_url=reverse_lazy('app:subcategoria_listar')


class MarcaListar(generic.ListView):
    model=Marca
    template_name='app/marca_list.html'
    context_object_name='obj'


def marca(request,id=None):
    template_name = "app/marca_form.html"

    contexto = {}
    if request.method == "GET":
        m = Marca.objects.filter(id=id).first()
        print(m)
        contexto = {"obj":m}



    return render(request,template_name,contexto)
        



