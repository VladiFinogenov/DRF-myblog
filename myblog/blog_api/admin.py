from django.contrib import admin
from blog_api.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

