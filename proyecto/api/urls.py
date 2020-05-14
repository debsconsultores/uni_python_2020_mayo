from django.urls import path,include
from .api import ApiCategoriaList

urlpatterns = [
    path('v2/categorias', \
        ApiCategoriaList.as_view(), \
        name='cate')
]