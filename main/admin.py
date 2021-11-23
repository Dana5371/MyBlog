from django.contrib import admin

from main.models import Category, Post, PostImage


class PostImageInLine(admin.TabularInline):
    model = PostImage
    max_num = 10
    min_num = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInLine, ]


admin.site.register(Category)


