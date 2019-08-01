from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostForm
from .models import Post

def mysum(request, name, age):

    return HttpResponse('안녕하세요.{}.{}살이시네요.'.format(name, age))


def post_new(request):
    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('http://127.0.0.1:8000/dojo/new/')
    else:
        form = PostForm()
        pass
    return render(request, 'dojo/post_form.html', {'form': form})
