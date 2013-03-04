# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.time'
        db.add_column('events_event', 'time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.date.today),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.time'
        db.delete_column('events_event', 'time')


    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'cet': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['events']