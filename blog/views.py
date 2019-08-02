#blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib.messages import constants as messages_constants
# Create your views here.
MESSAGE_TAGS = {messages_constants.ERROR: 'danger'}


def post_list(request):
    qs = Post.objects.all()
    return render(request, "blog/post_list.html",{
        'post_list': qs,
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request, '새 포스팅을 저장했습니다')

            return redirect(post)
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})

