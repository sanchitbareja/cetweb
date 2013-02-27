# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CertificateApplication'
        db.create_table('program_certificateapplication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('gpa', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('program', ['CertificateApplication'])


    def backwards(self, orm):
        # Deleting model 'CertificateApplication'
        db.delete_table('program_certificateapplication')


    models = {
        'program.certificateapplication': {
            'Meta': {'object_name': 'CertificateApplication'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'gpa': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'program.course': {
            'Meta': {'object_name': 'Course'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['program.Program']"})
        },
        'program.program': {
            'Meta': {'object_name': 'Program'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'international': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['program']