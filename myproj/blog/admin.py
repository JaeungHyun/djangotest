from django.contrib import admin
from .models import Post


# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    list_filter = ["update_at"]
    search_fields = ['title']
