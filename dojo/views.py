from django.shortcuts import render
from django.http import HttpResponse


def mysum(request, name, age):

    return HttpResponse('안녕하세요.{}.{}살이시네요.'.format(name, age))

