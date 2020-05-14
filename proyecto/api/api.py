from rest_framework import generics

from .serializer import CategoriaSerializer
from app.models import Categoria

class ApiCategoriaList(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    