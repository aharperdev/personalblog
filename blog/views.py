from django.shortcuts import render
from django.views import View, generic
from .serializers import PostSerializer
from rest_framework import viewsets

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


class PostDetailViews(generic.DetailView):
    model = Post
    template_name = "post.html"


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = []
