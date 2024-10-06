from django.shortcuts import render
from django.views import View, generic

from .models import Post

# Create your views here.
class Index(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)

class PostListViews(generic.ListView):
    model = Post
    context_object_name = "posts"
    template_name = "index.html"