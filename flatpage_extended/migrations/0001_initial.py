from seivanheidari.picture.models import *
from south.db import db
from django.db import models
from seivanheidari.flatpage_extended.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'FlatPage'
        db.create_table('flatpage_extended_flatpage', (
            ('id', orm['flatpage_extended.FlatPage:id']),
            ('url', orm['flatpage_extended.FlatPage:url']),
            ('title', orm['flatpage_extended.FlatPage:title']),
            ('content', orm['flatpage_extended.FlatPage:content']),
            ('content_html', orm['flatpage_extended.FlatPage:content_html']),
            ('created', orm['flatpage_extended.FlatPage:created']),
            ('updated', orm['flatpage_extended.FlatPage:updated']),
            ('visible', orm['flatpage_extended.FlatPage:visible']),
            ('enable_comments', orm['flatpage_extended.FlatPage:enable_comments']),
            ('template_name', orm['flatpage_extended.FlatPage:template_name']),
            ('registration_required', orm['flatpage_extended.FlatPage:registration_required']),
        ))
        db.send_create_signal('flatpage_extended', ['FlatPage'])
        
        # Adding ManyToManyField 'FlatPage.sites'
        db.create_table('flatpage_extended_flatpage_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('flatpage', models.ForeignKey(orm.FlatPage, null=False)),
            ('site', models.ForeignKey(orm['sites.Site'], null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'FlatPage'
        db.delete_table('flatpage_extended_flatpage')
        
        # Dropping ManyToManyField 'FlatPage.sites'
        db.delete_table('flatpage_extended_flatpage_sites')
        
    
    
    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'flatpage_extended.flatpage': {
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pictures': ('django.contrib.contenttypes.generic.GenericRelation', [], {'to': "orm['picture.Photo']"}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']"}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'})
        },
        'picture.photo': {
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'picture': ('ImageWithThumbsField', [], {'sizes': '((200,200),(1024,800))'})
        },
        'sites.site': {
            'Meta': {'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['flatpage_extended']
