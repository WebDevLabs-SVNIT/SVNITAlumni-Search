# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Alumni.phOffice'
        db.alter_column(u'alumni_search_alumni', 'phOffice', self.gf('django.db.models.fields.CharField')(max_length='30'))

        # Changing field 'Alumni.phRes'
        db.alter_column(u'alumni_search_alumni', 'phRes', self.gf('django.db.models.fields.CharField')(max_length='30'))

        # Changing field 'Alumni.phCell'
        db.alter_column(u'alumni_search_alumni', 'phCell', self.gf('django.db.models.fields.CharField')(max_length='30'))

    def backwards(self, orm):

        # Changing field 'Alumni.phOffice'
        db.alter_column(u'alumni_search_alumni', 'phOffice', self.gf('django.db.models.fields.CharField')(max_length='20'))

        # Changing field 'Alumni.phRes'
        db.alter_column(u'alumni_search_alumni', 'phRes', self.gf('django.db.models.fields.CharField')(max_length='20'))

        # Changing field 'Alumni.phCell'
        db.alter_column(u'alumni_search_alumni', 'phCell', self.gf('django.db.models.fields.CharField')(max_length='20'))

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
            'phCell': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'phOffice': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'phRes': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
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