from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostForm
from .models import Post


def mysum(request, name, age):

    return HttpResponse('안녕하세요.{}.{}살이시네요.'.format(name, age))


def post_new(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.ip = request.META['REMOTE_ADDR']
        post.save()
        return redirect('/dojo/new')
    return render(request, 'dojo/post_form.html', {'form': form})
