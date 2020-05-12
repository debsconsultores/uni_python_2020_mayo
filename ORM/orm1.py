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

m = Marca.objects.all().exclude(id=1)
m = Marca.objects.filter(descripcion__startswith='D').exclude(id=1)

# Mostrar ciertos campos
m = Marca.objects.filter(descripcion__startswith='D').values('descripcion')

# Sub Consultas
from django.db.models import Subquery

m = Marca.objects.filter(id__in=Subquery(Categoria.objects.values('id')))



select * from marca where id in (select id from categoria)


# INNER JOIN
sc = Subcategoria.objects.filter(categoria__id=7)















