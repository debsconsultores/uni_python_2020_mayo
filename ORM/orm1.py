from app.models import Categoria,SubCategoria,Marca
from django.db.models import Q

# AND
Modelo.objects.filter(condicion1,codicion2,condicion3)
Modelo.objects.filter(condicion1) & Modelo.objects.filter(condicion2)
Modelo.objects.filter(Q(condicion1) & Q(condicion2))


m = Marca.objects.filter(id=1,descripcion__startswith='D')
m = Marca.objects.filter(Q(id=1) & Q(descripcion__startswith='D'))

m = Marca(descripcion="Daniel")

# NOT

m = Marca.objects.filter(~Q(descripcion__startswith='D'))

m = Marca.objects.filter(~Q(descripcion__startswith='D') & ~Q(descripcion__startswith='d'))

