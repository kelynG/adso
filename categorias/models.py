from django.db import models
from autoslug import AutoSlugField


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    slug = AutoSlugField(populate_from='nombre')