from django.contrib import admin
from .models import Likes, Post, Category, Comments




admin.site.register(Likes)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comments)



# Меняем заголовок
admin.site.site_header = 'Flvbyr'

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'date',
                    'category', 'comments', 'likes')
    list_display_links = ('id', 'title')
    search_fields = ('title')


