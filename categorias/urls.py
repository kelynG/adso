from django.urls import path
from .views import *

urlpatterns = [
    path ('categorias', class1.as_view()),
    path('categorias/<int:id>',class2.as_view())
]