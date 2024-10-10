from blog.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["tags", "title", "content", "date_posted", "last_updated"]
