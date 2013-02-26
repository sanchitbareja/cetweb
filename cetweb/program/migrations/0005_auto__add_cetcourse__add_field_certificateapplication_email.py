# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CETCourse'
        db.create_table('program_cetcourse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('program', ['CETCourse'])

        # Adding field 'CertificateApplication.email'
        db.add_column('program_certificateapplication', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75),
                      keep_default=False)

        # Adding M2M table for field courses on 'CertificateApplication'
        db.create_table('program_certificateapplication_courses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('certificateapplication', models.ForeignKey(orm['program.certificateapplication'], null=False)),
            ('cetcourse', models.ForeignKey(orm['program.cetcourse'], null=False))
        ))
        db.create_unique('program_certificateapplication_courses', ['certificateapplication_id', 'cetcourse_id'])


    def backwards(self, orm):
        # Deleting model 'CETCourse'
        db.delete_table('program_cetcourse')

        # Deleting field 'CertificateApplication.email'
        db.delete_column('program_certificateapplication', 'email')

        # Removing M2M table for field courses on 'CertificateApplication'
        db.delete_table('program_certificateapplication_courses')


    models = {
        'program.certificateapplication': {
            'Meta': {'object_name': 'CertificateApplication'},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['program.CETCourse']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'gpa': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'program.cetcourse': {
            'Meta': {'object_name': 'CETCourse'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
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