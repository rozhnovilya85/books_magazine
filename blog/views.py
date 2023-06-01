from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'blog_list'
    extra_context = {'title': 'Блог'}

