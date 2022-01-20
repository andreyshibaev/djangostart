from django.contrib import admin
from blog.models import Blog


class AdminBlog(admin.ModelAdmin):
    list_display = ['id', 'title', 'datearticle', 'publish',]
    list_display_links = ['title',]
    list_editable = ['publish',]


admin.site.register(Blog, AdminBlog)


