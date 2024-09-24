from django.db import models

# Create your models here.
class Noticia(models.Model): #mayusculas la primera letra en singular
    title = models.CharField(max_length=200)
    description = models.TextField()
    detail=models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta: ##modificacion de la metainformacion
        verbose_name="New"
        verbose_name_plural="News"


    def __str__(self): #para que el titulo de la notica salga el nombre del tuitulo que yo puse
        return self.title