from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from seivanheidari.picture.models import Photo
from seivanheidari.content_util import parse_content
from django.contrib.contenttypes import generic
from django.db.models.signals import pre_save
import datetime

class FlatPage(models.Model):
    url = models.CharField(_('URL'), max_length=100, db_index=True)
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'), blank=True)
    content_html = models.TextField(blank=True, null=True)
    created = models.DateTimeField(default=datetime.datetime.now)
    updated = models.DateTimeField(blank=True, null=True)
    visible = models.BooleanField(default=True)
    pictures = generic.GenericRelation(Photo)
    enable_comments = models.BooleanField(_('enable comments'))
    template_name = models.CharField(_('template name'), max_length=70, blank=True,
    help_text=_("Example: 'flatpages/contact_page.html'. If this isn't provided, the system will use 'flatpages/default.html'."))
    registration_required = models.BooleanField(_('registration required'), help_text=_("If this is checked, only logged-in users will be able to view the page."))
    sites = models.ManyToManyField(Site)

    # def save(self):
    #     import pdb; pdb.set_trace()
    #     markup_embed = parse_content.find_markup(self.content)
    #     function_embed = parse_content.find_function(markup_embed)
    #     syntax_embed = parse_content.find_syntax(function_embed)
    #     self.content_html = syntax_embed
    #     super(FlatPage, self).save()
    
    def get_created(self):
        """docstring for get_created"""
        return "Created: %s" % (self.created.strftime("%Y-%B-%d, %H:%M"))
    
    def get_updated(self):
        """docstring for get_updated"""
        if not self.updated is False:
          return "Updated: %s" % (self.updated.strftime("%Y-%B-%d, %H:%M"))

    def __unicode__(self):
        return u"%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        return self.url
        
def add_updated(sender, instance, **kwargs):
    if (instance.created.date() < datetime.datetime.now().date()) & (instance.visible is True):
        instance.updated = datetime.datetime.now()

def embed_with_content_util(sender, instance, **kwargs):
    markup_embed = parse_content.find_markup(instance.content)
    function_embed = parse_content.find_function(markup_embed)
    syntax_embed = parse_content.find_syntax(function_embed)
    instance.content_html = syntax_embed

pre_save.connect(embed_with_content_util, sender=FlatPage)   
pre_save.connect(add_updated, sender=FlatPage)