from django.contrib import admin
from .models import (
    Resource,
    Content,
    Category
)


class AudioFileUploadInline(admin.StackedInline):
    model = Resource
    extra = 1
    fields = ["resource_name","resource", 'resource_type']



@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    inlines = (
        AudioFileUploadInline,
    )

    list_filter = [ 'title']
    search_fields = ['title']





@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['category_name']
    list_filter = ['category_name']