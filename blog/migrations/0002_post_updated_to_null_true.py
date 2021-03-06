
from south.db import db
from django.db import models
from seivanheidari.blog.models import *
from seivanheidari.picture.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'Post.updated'
        # (to signature: django.db.models.fields.DateTimeField(null=True, blank=True))
        db.alter_column('blog_post', 'updated', orm['blog.post:updated'])
        
    
    
    def backwards(self, orm):
        
        # Changing field 'Post.updated'
        # (to signature: django.db.models.fields.DateTimeField(blank=True))
        db.alter_column('blog_post', 'updated', orm['blog.post:updated'])
        
    
    
    models = {
        'blog.post': {
            'commentable': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pictures': ('django.contrib.contenttypes.generic.GenericRelation', [], {'to': "orm['picture.Photo']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'tags': ('TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'picture.photo': {
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'picture': ('ImageWithThumbsField', [], {'sizes': '((200,200),(1024,800))'})
        }
    }
    
    complete_apps = ['blog']
