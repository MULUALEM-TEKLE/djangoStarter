from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import TemplateView
from djangoStarter.models import Post

# Create your views here.

class post_feed(TemplateView):
    template_name = 'index.html'

def get_context_data(self, *args , **kwargs):
    context = super().get_context_data(**kwargs)
    context["posts"] = Post.objects.all() 
    return context

