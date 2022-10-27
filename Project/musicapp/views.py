from django.shortcuts import render
from django.https import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('Hey World')
