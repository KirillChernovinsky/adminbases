from django.contrib import admin

from .models import Tovars, Zakaz, Maker, Categories

# Register your models here.
admin.site.register(Tovars)
admin.site.register(Zakaz)
admin.site.register(Maker)
admin.site.register(Categories)


# Меняем заголовок
admin.site.site_header = 'Internet_magazin'

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'date',
                    'category', 'comments', 'likes')
    list_display_links = ('id', 'title')
    search_fields = ('title')


