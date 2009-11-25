from django.conf.urls.defaults import *
from seivanheidari.blog.models import Post
from seivanheidari.picture.models import Photo
from seivanheidari.flatpage_extended.models import FlatPage
import datetime

def visible_flatpages():
    """docstring for visible_flatpages"""
    return FlatPage.objects.filter(visible=True)
    
def latest_10_posts():
    return Post.objects.filter(visible=True, created__lte=datetime.datetime.now)[:10]

def list_of_dates():
    return Post.objects.dates('created', 'month').filter(created__lte=datetime.datetime.now)

def visible_posts():
   return Post.objects.filter(visible=True, created__lte=datetime.datetime.now)

info_dict = {
    'queryset': visible_posts(),
    'extra_context': {
                    'dates_list' : list_of_dates,
                    'latest_object_list' : latest_10_posts,
                    'flatpages' : visible_flatpages,
                    }
    }

urlpatterns = patterns('django.views.generic',
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'date_based.object_detail', dict(info_dict, slug_field='slug', date_field="created"), name="blog_detail"),
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$','date_based.archive_day',dict(info_dict,template_name='blog/post_list.html', date_field="created")),
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$','date_based.archive_month', dict(info_dict, template_name='blog/post_list.html', date_field="created"), name="blog_month"),
	url(r'^(?P<year>\d{4})/$','date_based.archive_year', dict(info_dict, date_field="created", template_name='blog/post_archive_year.html'),),
	url(r'^$', 'list_detail.object_list', dict(info_dict, paginate_by=5, template_name='blog/post_list.html'), name="blog_list")
)
  
