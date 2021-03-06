from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# from app.models import Categoria
from .models import Categoria,SubCategoria, Marca, \
    Producto
from .forms import CategoriaForm,SubCategoriaForm, \
    ProductoForm

from home.views import ClaseBase,VistaAlta


# Create your views here.
def hola_mundo(request):
    return HttpResponse("Hola Mundo a los de INATEC")


class CategoriaListar(ClaseBase,generic.ListView):
    model=Categoria
    template_name='app/categoria_list.html'
    context_object_name='obj'
    ordering="descripcion"
    permission_required = "app.view_categoria"


class CategoriaNueva(VistaAlta):
    model=Categoria
    template_name='app/categoria_form.html'
    # context_object_name='obj'
    form_class=CategoriaForm
    success_url=reverse_lazy('app:categoria_listar')
    permission_required = "app.add_categoria"
    # success_message="Creado Satisfactoriamente"

    # def form_valid(self, form):
    #     if form.instance.pk:
    #         form.instance.um = self.request.user.id
    #     else:
    #         form.instance.uc = self.request.user
    #     return super().form_valid(form)


class CategoriaEditar(ClaseBase,generic.UpdateView):
    model=Categoria
    template_name='app/categoria_form.html'
    context_object_name='obj'
    form_class=CategoriaForm
    permission_required = "app.change_categoria"
    success_url=reverse_lazy('app:categoria_listar')
    success_message="Actualizado Satisfactoriamente"

    def form_valid(self, form):
        if form.instance.pk:
            form.instance.um = self.request.user.id
        else:
            form.instance.uc = self.request.user
        return super().form_valid(form)


class CategoriaBorrar(generic.DeleteView):
    model=Categoria
    template_name='app/borrar.html'
    context_object_name='obj'
    # form_class=CategoriaForm    
    success_url=reverse_lazy('app:categoria_listar')


class SubCategoriaListar(ClaseBase,generic.ListView):
    model=SubCategoria
    template_name='app/subcategoria_list.html'
    context_object_name='obj'
    login_url='home:login'
    permission_required = "app.view_subcategoria"


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

    if request.method == "POST":
        desc = request.POST["id_descripcion"]
        if not id:
            m = Marca(
                descripcion=desc
            )
            m.save()
        else:
            m = Marca.objects.filter(id=id).first()
            m.descripcion = desc
            m.save()
        
        # return reverse("app:marca_listar")
        return redirect("app:marca_listar")

    return render(request,template_name,contexto)
        

class ProductoListar(generic.ListView):
    model=Producto
    template_name='app/producto_list.html'
    context_object_name='obj'


class ProductoNueva(generic.CreateView):
    model=Producto
    template_name='app/producto_form.html'
    context_object_name='obj'
    form_class=ProductoForm
    success_url=reverse_lazy('app:producto_listar')

