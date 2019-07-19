from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mysum(request, x,y):
    #request: HttpRequest
    print(int(x)+y)
    return HttpResponse(int(x)+100+y)
