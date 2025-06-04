from rest_framework import serializers
from .models import *

class CategoriasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ("id","nombre", "slug")