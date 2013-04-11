# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InfoImage'
        db.create_table('info_infoimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('info', ['InfoImage'])

        # Adding model 'Testimonial'
        db.create_table('info_testimonial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('info', ['Testimonial'])

        # Adding model 'AboutPage'
        db.create_table('info_aboutpage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='name', overwrite=False)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('info', ['AboutPage'])

        # Adding M2M table for field images on 'AboutPage'
        db.create_table('info_aboutpage_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('aboutpage', models.ForeignKey(orm['info.aboutpage'], null=False)),
            ('infoimage', models.ForeignKey(orm['info.infoimage'], null=False))
        ))
        db.create_unique('info_aboutpage_images', ['aboutpage_id', 'infoimage_id'])


    def backwards(self, orm):
        # Deleting model 'InfoImage'
        db.delete_table('info_infoimage')

        # Deleting model 'Testimonial'
        db.delete_table('info_testimonial')

        # Deleting model 'AboutPage'
        db.delete_table('info_aboutpage')

        # Removing M2M table for field images on 'AboutPage'
        db.delete_table('info_aboutpage_images')


    models = {
        'info.aboutpage': {
            'Meta': {'object_name': 'AboutPage'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['info.InfoImage']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'name'", 'overwrite': 'False'})
        },
        'info.infoimage': {
            'Meta': {'object_name': 'InfoImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'info.testimonial': {
            'Meta': {'object_name': 'Testimonial'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['info']