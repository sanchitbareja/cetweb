# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Event.time'
        db.delete_column('events_event', 'time')

        # Adding field 'Event.start_time'
        db.add_column('events_event', 'start_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 3, 3, 0, 0)),
                      keep_default=False)

        # Adding field 'Event.end_time'
        db.add_column('events_event', 'end_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 3, 3, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Event.time'
        db.add_column('events_event', 'time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 3, 3, 0, 0)),
                      keep_default=False)

        # Deleting field 'Event.start_time'
        db.delete_column('events_event', 'start_time')

        # Deleting field 'Event.end_time'
        db.delete_column('events_event', 'end_time')


    models = {
        'events.event': {
            'Meta': {'ordering': "['-start_time']", 'object_name': 'Event'},
            'cet': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'CET Berkeley'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['events']