from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)


def detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'blogs/detail.html', context)


@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            obj = Post()
            obj.user = User.objects.get(id=request.user.id)
            obj.post_name = form.cleaned_data['post_name']
            obj.post_detail = form.cleaned_data['post_detail']
            obj.save()
            return redirect('/blogs/')
    else:
        form = PostForm()
        context = {'form': form}
        return render(request, 'blogs/form.html', context)

# def update_post(request, pk):
#     if request.method == "POST":
#         postupdate = Post.objects.get(id=pk)
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             return HttpResponse("NotValid")
#     else:
#         post = Post.objects.get(id=pk)
#         postupdate = Post.objects.get(id=pk)
#         form = PostForm(instance=postupdate)
#         context = {'post':post, 'form':form}
#         return render(request, 'blogs/post_update.html', context)


@login_required
def update(request, pk):
    if request.method == "POST":
        postupdate = Post.objects.get(id=pk)
        form = PostForm(request.POST, instance=postupdate)
        if form.is_valid():
            obj = form
            obj.post_name = form.cleaned_data['post_name']
            obj.post_detail = form.cleaned_data['post_detail']
            obj.save()
            return HttpResponseRedirect("/blogs/")
    else:
        post = Post.objects.get(id=pk)
        postupdate = Post.objects.get(id=pk)
        form = PostForm(instance=postupdate)
        context = {'post': post, 'form': form}
        return render(request, 'blogs/update.html', context)


@login_required
def delete(request, pk):
    if request.method == "POST":
        obj = Post.objects.get(id=pk)
        obj.delete()
        return HttpResponseRedirect("/blogs/")
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'blogs/delete.html', context)
