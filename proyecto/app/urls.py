from django.urls import path,include
from .views import hola_mundo, CategoriaListar, \
    CategoriaNueva, CategoriaEditar, CategoriaBorrar, \
    SubCategoriaListar,SubCategoriaNueva,SubCategoriaEditar, SubCategoriaBorrar, \
    MarcaListar, marca, \
    ProductoListar,ProductoNueva

urlpatterns = [
    path('hola-mundo',hola_mundo,name="home1"),
    path('categorias/',CategoriaListar.as_view(),name='categoria_listar'),
    path('categorias/nueva',CategoriaNueva.as_view(),name='categoria_nueva'),
    path('categorias/editar/<int:pk>',CategoriaEditar.as_view(),name='categoria_editar'),
    path('categorias/borrar/<int:pk>',CategoriaBorrar.as_view(),name='categoria_borrar'),

    path('sub-categorias/',SubCategoriaListar.as_view(),name='subcategoria_listar'),
    path('sub-categorias/nueva',SubCategoriaNueva.as_view(),name='subcategoria_nueva'),
    path('sub-categorias/editar/<int:pk>',SubCategoriaEditar.as_view(),name='subcategoria_editar'),
    path('sub-categorias/borrar/<int:pk>',SubCategoriaBorrar.as_view(),name='subcategoria_borrar'),

    path('marcas/',MarcaListar.as_view(),name='marca_listar'),
    path('marcas/nueva',marca,name='marca_nueva'),
    path('marcas/editar/<int:id_marca>',marca,name='marca_editar'),

    path('productos/',ProductoListar.as_view(),name="producto_listar"),
    path('productos/nuevo',ProductoNueva.as_view(),name="producto_nuevo"),

]