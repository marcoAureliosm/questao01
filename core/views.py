from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Olô,Mundo!")
# Create your views here.
