from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_create', 'date_update')
    list_display_links = ('title', 'content')

admin.site.register(Post, PostAdmin)

