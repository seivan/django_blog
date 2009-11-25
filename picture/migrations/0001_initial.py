
from south.db import db
from django.db import models
from seivanheidari.picture.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Photo'
        db.create_table('picture_photo', (
            ('id', orm['picture.Photo:id']),
            ('name', orm['picture.Photo:name']),
            ('content_type', orm['picture.Photo:content_type']),
            ('object_id', orm['picture.Photo:object_id']),
            ('picture', orm['picture.Photo:picture']),
        ))
        db.send_create_signal('picture', ['Photo'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Photo'
        db.delete_table('picture_photo')
        
    
    
    models = {
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
    
    complete_apps = ['picture']
