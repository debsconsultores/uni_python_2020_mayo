from django.urls import path,include
from .api import ApiCategoriaList, crud_categoria

urlpatterns = [
    path('v2/categorias', \
        ApiCategoriaList.as_view(), \
        name='cate'),
    path('v2/categorias/<int:id>',crud_categoria,name="cate_edit")
]