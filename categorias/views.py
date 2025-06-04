from rest_framework.views import APIView
from django.http.response import JsonResponse
from .models import Categoria
from .serializers import *

# Create your views here.
 
class class1(APIView):

    def get(self, request): 
        data = Categoria.objects.order_by('-id').all()
        datos_json = CategoriasSerializers(data, many=True)
        return response(datos_json.data)