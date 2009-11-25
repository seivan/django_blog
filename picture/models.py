from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from thumbs import ImageWithThumbsField
import datetime
import os
from django.template.defaultfilters import slugify
#ROOT_PATH = os.path.dirname(__file__)
#TEMPLATES_PATH = os.path.join(ROOT_PATH, 'templates')

class Photo(models.Model):
    """(photo description)"""
    def get_content_type(instance, filename):
        """docstring for get_content_type"""
        return os.path.join("pictures", slugify(instance.content_type.name), datetime.datetime.now().strftime("%Y-%b"), filename)
        #return os.path.join("pictures", "stuff", datetime.datetime.now().strftime("%Y-%b"), filename)
        
    name = models.CharField(max_length=100, unique=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    picture = ImageWithThumbsField(upload_to=get_content_type, sizes=((200,200),(1024,800)))

    def __unicode__(self):
        return self.name
    

