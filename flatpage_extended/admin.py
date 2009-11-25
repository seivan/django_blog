from django import forms
from django.contrib import admin
from seivanheidari.flatpage_extended.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from seivanheidari.picture.models import *
from django.contrib.contenttypes import generic

class FlatpageForm(forms.ModelForm):
    url = forms.RegexField(label=_("URL"), max_length=100, regex=r'^[-\w/]+$',
        help_text = _("Example: '/aboasdasdut/contact/'. Make sure to have leading"
                      " and trailing slashes."),
        error_message = _("This value must contain only letters, numbers,"
                          " underscores, dashes or slashes."))

    class Meta:
        model = FlatPage

class PhotoInline(generic.GenericTabularInline):
    """docstring for PhotoInline"""
    model = Photo
    extra = 1

class FlatPageAdmin(admin.ModelAdmin):
    form = FlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'created', 'updated',  'content', 'visible', 'sites')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'enable_comments', 'registration_required')
    search_fields = ('url', 'title')
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

admin.site.register(FlatPage, FlatPageAdmin)
