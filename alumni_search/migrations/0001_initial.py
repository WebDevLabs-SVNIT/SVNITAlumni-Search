# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Alumni'
        db.create_table(u'alumni_search_alumni', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lName', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('fName', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('yop', self.gf('django.db.models.fields.IntegerField')()),
            ('branch', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length='15')),
            ('phOffice', self.gf('django.db.models.fields.CharField')(max_length='20')),
            ('phCell', self.gf('django.db.models.fields.CharField')(max_length='20')),
            ('phRes', self.gf('django.db.models.fields.CharField')(max_length='20')),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('posHeld', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('address', self.gf('django.db.models.fields.CharField')(max_length='120')),
            ('landmark', self.gf('django.db.models.fields.CharField')(max_length='120')),
            ('street', self.gf('django.db.models.fields.CharField')(max_length='120')),
            ('city', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('pincode', self.gf('django.db.models.fields.CharField')(max_length='10')),
            ('state', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('country', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('resAddress', self.gf('django.db.models.fields.CharField')(max_length='120')),
            ('resLandmark', self.gf('django.db.models.fields.CharField')(max_length='120')),
            ('resCity', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('resPincode', self.gf('django.db.models.fields.CharField')(max_length='10')),
            ('resState', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('resCountry', self.gf('django.db.models.fields.CharField')(max_length='30')),
        ))
        db.send_create_signal(u'alumni_search', ['Alumni'])


    def backwards(self, orm):
        # Deleting model 'Alumni'
        db.delete_table(u'alumni_search_alumni')


    models = {
        u'alumni_search.alumni': {
            'Meta': {'object_name': 'Alumni'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': "'120'"}),
            'branch': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fName': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lName': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'landmark': ('django.db.models.fields.CharField', [], {'max_length': "'120'"}),
            'phCell': ('django.db.models.fields.CharField', [], {'max_length': "'20'"}),
            'phOffice': ('django.db.models.fields.CharField', [], {'max_length': "'20'"}),
            'phRes': ('django.db.models.fields.CharField', [], {'max_length': "'20'"}),
            'pincode': ('django.db.models.fields.CharField', [], {'max_length': "'10'"}),
            'posHeld': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'resAddress': ('django.db.models.fields.CharField', [], {'max_length': "'120'"}),
            'resCity': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'resCountry': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'resLandmark': ('django.db.models.fields.CharField', [], {'max_length': "'120'"}),
            'resPincode': ('django.db.models.fields.CharField', [], {'max_length': "'10'"}),
            'resState': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': "'120'"}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': "'15'"}),
            'yop': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['alumni_search']