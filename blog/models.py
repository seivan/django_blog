from django.db import models
from seivanheidari.picture.models import Photo
from seivanheidari.content_util import parse_content
from django.contrib.contenttypes import generic
from django.db.models.signals import pre_save
from tagging.models import Tag
from tagging.fields import TagField
from django.template.defaultfilters import slugify
import datetime

class Post(models.Model):
    """(Post description)"""
    title = models.CharField(blank=True, max_length=100)
    created = models.DateTimeField(default=datetime.datetime.now)
    updated = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True)
    content_html = models.TextField(blank=True)
    visible = models.BooleanField(default=True)
    commentable = models.BooleanField(default=True)
    tags = TagField()
    pictures = generic.GenericRelation(Photo)
    slug = models.SlugField(blank=True, unique_for_date="created")
    
    def __unicode__(self):
        return u'%s' %(self.title)
    
    def get_created(self):
        """docstring for get_created"""
        return "Created: %s" % (self.created.strftime("%Y-%B-%d, %H:%M"))
    
    def get_updated(self):
        """docstring for get_updated"""
        if not self.updated is False:
          return "Updated: %s" % (self.updated.strftime("%Y-%B-%d, %H:%M"))
    
    def get_model_name(self):
        return self.__class__.__name__

    
    @models.permalink
    def get_absolute_url(self):
        return ('blog_detail', (), {
            'year': self.created.year,
            'month': self.created.strftime("%h").lower(),
            'day': self.created.day,
            'slug': self.slug
                })
    
    
    class Meta:
        get_latest_by = "created"
        ordering = ('-created',)
            

def add_updated(sender, instance, **kwargs):
    """docstring for fname"""
    if (instance.created.date() < datetime.datetime.now().date()) & (instance.visible is True):
        instance.updated = datetime.datetime.now()

def create_slug(sender, instance, **kwargs):
    """docstring for create_slug"""
    instance.slug = slugify(instance.title)
  
def embed_with_content_util(sender, instance, **kwargs):
    markup_embed = parse_content.find_markup(instance.content)
    function_embed = parse_content.find_function(markup_embed)
    syntax_embed = parse_content.find_syntax(function_embed)
    instance.content_html = syntax_embed

def fix_time(sender, instance, **kwargs):
	instance.created = instance.created - datetime.timedelta(minutes=3)
	
      
pre_save.connect(embed_with_content_util, sender=Post)   
pre_save.connect(add_updated, sender=Post)
pre_save.connect(create_slug, sender=Post)
pre_save.connect(fix_time, sender=Post)