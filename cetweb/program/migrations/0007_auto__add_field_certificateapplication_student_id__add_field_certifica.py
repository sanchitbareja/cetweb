# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CertificateApplication.student_id'
        db.add_column('program_certificateapplication', 'student_id',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'CertificateApplication.phone_number'
        db.add_column('program_certificateapplication', 'phone_number',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'CertificateApplication.major'
        db.add_column('program_certificateapplication', 'major',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=200),
                      keep_default=False)

        # Adding field 'CertificateApplication.address'
        db.add_column('program_certificateapplication', 'address',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=200),
                      keep_default=False)

        # Adding field 'CertificateApplication.comments'
        db.add_column('program_certificateapplication', 'comments',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CertificateApplication.student_id'
        db.delete_column('program_certificateapplication', 'student_id')

        # Deleting field 'CertificateApplication.phone_number'
        db.delete_column('program_certificateapplication', 'phone_number')

        # Deleting field 'CertificateApplication.major'
        db.delete_column('program_certificateapplication', 'major')

        # Deleting field 'CertificateApplication.address'
        db.delete_column('program_certificateapplication', 'address')

        # Deleting field 'CertificateApplication.comments'
        db.delete_column('program_certificateapplication', 'comments')


    models = {
        'program.certificateapplication': {
            'GPA': ('django.db.models.fields.FloatField', [], {}),
            'Meta': {'object_name': 'CertificateApplication'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['program.CETCourse']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'student_id': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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