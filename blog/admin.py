from seivanheidari.blog.models import Post
from seivanheidari.picture.models import *
from django.contrib.contenttypes import generic
from django.contrib import admin




class PhotoInline(generic.GenericTabularInline):
    """docstring for PhotoInline"""
    model = Photo
    extra = 1
    
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('title', 'created', 'updated', 'commentable', 'visible')
    list_filter = ('created', 'updated', 'commentable', 'visible')
    list_editable = ('visible', 'commentable')
    actions = ['visible_true', 'visible_false']
    inlines = [PhotoInline]
    class Media:
            js = ['javascript/lib/jquery-1.3.2.min.js', 'javascript/lib/ui.core.js',
                'javascript/lib/ui.sortable.js', 'javascript/lib/dynamic_inlines_with_sort.js',]
            css = { 'all' : ['javascript/lib/css/dynamic_inlines_with_sort.css'], }
    
    def visible_true(self, request, queryset):
        queryset.update(visible=True)
    visible_true.short_description = "Mark selected stories as published"

    def visible_false(self, request, queryset):
        queryset.update(visible=False)
    visible_false.short_description = "Mark selected stories as draft"
    
admin.site.register(Post, PostAdmin)

from django.contrib.comments.moderation import CommentModerator, moderator

class PostModerator(CommentModerator):
    #email_notification = True
    enable_field = 'commentable'

moderator.register(Post, PostModerator)
        