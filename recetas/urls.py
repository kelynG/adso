from django.urls import path
from .views import *

urlpatterns = [
    path ('recetas/', class1.as_view()),
    #path('recetas/<int:id>',class2.as_view())
]