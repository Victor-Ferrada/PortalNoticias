









from django.shortcuts import render
from .models import Noticia

# Create your views here.
def noticia(request):
    minoticia=Noticia.objects.all() ##select * from
    return render(request,"foro/foro.html",
                  {'minoticia':minoticia})