from seivanheidari.picture.models import Photo
from django.contrib import admin

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'picture')#, 'content_type', 'content_id', 'content_object', 'id')
    #list_editable = ('name', 'picture')
    
admin.site.register(Photo, PhotoAdmin)

