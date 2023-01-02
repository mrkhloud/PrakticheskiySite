from django.contrib import admin

from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_image', 'title', 'date_add', 'category')
    list_display_links = ('title',)
    readonly_fields = ('get_image',)
    fields = ('get_image', 'image', 'user', 'title', 'content', 'category')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
