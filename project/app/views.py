from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Post, Likes, Comments, Category


class GetPost(ListView):
    model = Post
    template_name = 'app/index.html'
    context_object_name = 'posts'



class GetDetail(DetailView):
    model = Post
    template_name = 'app/post_list.html'


class CreatePost(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'app/post_form.html'
    success_url = '/app'


class UpdatePost(UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'app/post_form.html'
    success_url = '/app'


class DeletePost(DeleteView):
    model = Post
    success_url = '/app'



def index(request):
    posts = Post.objects.all()
    likes = Likes.objects.all()
    com = Comments.objects.all()
    cats = Category.objects.all()
    return render(request, 'app/bebr.html', context={'posts': posts, 'likes':likes,
        'com': com, 'cats': cats})
