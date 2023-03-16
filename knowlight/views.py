from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import knowPost
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
# Create your views here.
class PostListView(ListView):
    template_name = 'post_list.html'
    model = knowPost

class CreatePostView(CreateView):
    model = knowPost
    template_name = 'post_create.html'
    fields = ['station','text']
    success_url = reverse_lazy('knowlight:post_list')

    def get_success_url(self):
        return resolve_url('knowlight:post_list')