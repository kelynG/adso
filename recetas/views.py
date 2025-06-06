from rest_framework.views import APIView
from django.http.response import JsonResponse
from .models import Categoria
from .serializers import *
from http import HTTPStatus
from django.http import Http404
from django.utils.text import slugify

# Create your views here.
 
class class1(APIView):

    def get(self, request): 
        data = Receta.objects.order_by('-id').all()
        datos_json = RecetaSerializers(data, many=True)
        return JsonResponse({"data":datos_json.data})
    