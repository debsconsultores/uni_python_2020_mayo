from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import CategoriaSerializer
from app.models import Categoria

class ApiCategoriaList(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    

@api_view(["POST","GET"])
def crud_categoria(request,id):
    cat = None
    resp = {}
    estado = status.HTTP_200_OK
    if request.method=="GET":
        cat = Categoria.objects.filter(id=id).first()
        if cat:
            resp = {"id":cat.id,"descripcion":cat.descripcion}
        else:
            estado = status.HTTP_404_NOT_FOUND
            resp = {"msg":"Categoría {} no existe".format(id)}
    else:
        print("POST")
        d_id = None
        try:
            d_id = request.data["id"]
        except:
            d_id = None
        
        print("d_id",d_id)
        d_des= request.data["desc"]

        if not d_id:
            estado = status.HTTP_404_NOT_FOUND
            resp = {"msg":"Id es Requerido" }
            return Response(resp,estado)

        if d_id!= id:
            estado = status.HTTP_404_NOT_FOUND
            resp = {"msg":"NO coinciden los id" }
            return Response(resp,estado)  

        cat = Categoria.objects.filter(id=id).first()
        if not cat:
            estado = status.HTTP_404_NOT_FOUND
            resp = {"msg":"Categoría {} no existe".format(id)}
            return Response(resp,estado)  
        
        cat.descripcion = d_des
        cat.save()
        resp = {"id":cat.id,"descripcion":cat.descripcion}

    return Response(resp,estado)
    
