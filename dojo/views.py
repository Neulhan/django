from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mysum(request, name, age):
    #request: HttpRequest
    return HttpResponse('안녕하세요.{}.{}살이시네요.'.format(name, age))


