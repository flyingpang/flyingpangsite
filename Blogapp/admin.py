from django.contrib import admin
from django.contrib.auth.models import User
from Blogapp.models import Tag, Author, Article


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'website')
    # list_display_links = ('name', 'email', 'website')
    # fields = ('name', 'email', 'website')
    search_fields = ('name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('caption', 'subcaption', 'classification', 'author', 'publish_time', 'update_time')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)
    fields = ('caption', 'author', 'classification')



admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
