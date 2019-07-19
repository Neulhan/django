from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
from django.conf import settings
# Create your views here.

def mysum(request, name, age):
    #request: HttpRequest
    return HttpResponse('안녕하세요.{}.{}살이시네요.'.format(name, age))

def post_list1(request):
    name = "신한결"
    return HttpResponse("""
    <h1>AskDjango</h1>
    <p>{name}</p>
    <p>장고를 배우는 늘한입니다</p>
    """.format(name=name))

def post_list2(request):
    name = "늘한"
    return render(request, 'dojo/post_list.html',{'name':name})

def post_list3(request):
    return JsonResponse(
        {'message': '안녕 파이썬&장고',
         'items': ['파이썬',"장고", "celery", 'azure', 'aws'],
         }
        ,json_dumps_params={'ensure_ascii':False}
    )

def excel_download(request):
    filepath = os.path.join(settings.BASE_DIR, 'm.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
 