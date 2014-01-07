# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Alumni.email'
        db.alter_column(u'alumni_search_alumni', 'email', self.gf('django.db.models.fields.EmailField')(max_length='200'))

    def backwards(self, orm):

        # Changing field 'Alumni.email'
        db.alter_column(u'alumni_search_alumni', 'email', self.gf('django.db.models.fields.EmailField')(max_length=75))

    models = {
        u'alumni_search.alumni': {
            'Meta': {'object_name': 'Alumni'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': "'150'"}),
            'branch': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': "'200'"}),
            'fName': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lName': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'landmark': ('django.db.models.fields.CharField', [], {'max_length': "'150'"}),
            'phCell': ('django.db.models.fields.CharField', [], {'max_length': "'80'"}),
            'phOffice': ('django.db.models.fields.CharField', [], {'max_length': "'80'"}),
            'phRes': ('django.db.models.fields.CharField', [], {'max_length': "'80'"}),
            'pincode': ('django.db.models.fields.CharField', [], {'max_length': "'10'"}),
            'posHeld': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'resAddress': ('django.db.models.fields.CharField', [], {'max_length': "'150'"}),
            'resCity': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'resCountry': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'resLandmark': ('django.db.models.fields.CharField', [], {'max_length': "'150'"}),
            'resPincode': ('django.db.models.fields.CharField', [], {'max_length': "'10'"}),
            'resState': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': "'150'"}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': "'15'"}),
            'yop': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['alumni_search']