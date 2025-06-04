from django.urls import path
from .views import class_ejemplo, class_ejemploparametros, class_ejemploUpload

urlpatterns = [
    path('ejemplo', class_ejemplo.as_view()),
    path('ejemplo/<int:id>', class_ejemploparametros.as_view()),
    path('ejemplo-upload', class_ejemploUpload.as_view()),
    
]