from django.contrib import admin

from myblog.models import Category
from myblog.models import Post

class PostInline(admin.TabularInline):
    model = 

class CategoryInline(admin.TabularInline):
    model = Category


class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostInline,
    ]

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post, PostAdmin)
