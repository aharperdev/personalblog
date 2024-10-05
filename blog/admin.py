from django.contrib import admin

# Register your models here.

from django.contrib import admin
from blog.models import Post, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "color")


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date_posted", "last_updated")
    list_filter = ("tags",)


admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
