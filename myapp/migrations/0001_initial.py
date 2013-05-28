# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Habit'
        db.create_table(u'myapp_habit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('track_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('del_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ip_address', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'myapp', ['Habit'])


    def backwards(self, orm):
        # Deleting model 'Habit'
        db.delete_table(u'myapp_habit')


    models = {
        u'myapp.habit': {
            'Meta': {'object_name': 'Habit'},
            'del_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'track_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['myapp']