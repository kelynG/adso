
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.response import Response
from http import HTTPStatus
from django.core.files.storage import FileSystemStorage
import os
from datetime import datetime



class class_ejemplo(APIView):

    # def get(self,request):
        # return HttpResponse(f"METODO GET | id={request.GET.get('id', None)} | slug={request.GET.get
            #('slug')}")

        #    return JsonResponse({"estado":"ok", "mensaje": f"METODO GET | id={request.GET.get('id',
        #       None)} | slug={request.GET.get('slug')}"})
    
    def post(self, request):
         if request.data.get("correo")== None or request.data.get ("password")==None:
              raise Http404
         return JsonResponse({"estado":"ok", "mensaje":f"Metodo GET | correo={request.data.get('correo')} | password={request.data.get('password')}"}, status=HTTPStatus.CREATED)
    


    #  def get(self, request):
    #      return JsonResponse({"estado":"ok", "mensaje": f"METODO GET | id={request.GET.get('id',
    #         None)} | slug={request.GET.get('slug')}"})
    




class class_ejemploparametros(APIView):


    def get (self, request, id):
         return HttpResponse(f"METODO GET| parametro={id}")
    
    def put (self, request, id):
         return HttpResponse(f"METODO PUT| parametro={id}")
    
    def delete (self, request, id):
         return HttpResponse(f"METODO DELETE| parametro={id}")
    

class class_ejemploUpload(APIView):

     def post(self, request):
          fs= FileSystemStorage()
          #fs.save(f"ejemplo/foto.jpg", request.FILES['file'])
          fecha= datetime.now()
          foto=f"{datetime.timestamp(fecha)}{os.path.splitext(str(request.FILES['file']))[1]}"
          fs.save(f"ejemplo/{foto}", request.FILES['file'])
          fs.url(request.FILES['file'])
          return JsonResponse({"estado":"ok", "mensaje":"el archivo se subio"})
    



    
    


    
   