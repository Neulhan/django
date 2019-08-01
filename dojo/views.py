from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm


def mysum(request, name, age):

    return HttpResponse('안녕하세요.{}.{}살이시네요.'.format(name, age))


def post_new(request):
    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)

    else:
        form = PostForm()
        pass
    return render(request, 'dojo/post_form.html', {'form': form})
