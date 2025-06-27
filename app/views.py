from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("<h1> Ysa <h1/>")
    return render(request, "teste.html")
