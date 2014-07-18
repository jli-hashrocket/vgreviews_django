# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Review'
        db.create_table(u'reviews_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('pros', self.gf('django.db.models.fields.TextField')()),
            ('cons', self.gf('django.db.models.fields.TextField')()),
            ('score', self.gf('django.db.models.fields.FloatField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
        ))
        db.send_create_signal(u'reviews', ['Review'])

        # Adding M2M table for field categories on 'Review'
        m2m_table_name = db.shorten_name(u'reviews_review_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('review', models.ForeignKey(orm[u'reviews.review'], null=False)),
            ('category', models.ForeignKey(orm[u'reviews.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['review_id', 'category_id'])

        # Adding model 'Like'
        db.create_table(u'reviews_like', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('review', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reviews.Review'])),
            ('total_likes', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'reviews', ['Like'])

        # Adding M2M table for field user on 'Like'
        m2m_table_name = db.shorten_name(u'reviews_like_user')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('like', models.ForeignKey(orm[u'reviews.like'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['like_id', 'user_id'])

        # Adding model 'Category'
        db.create_table(u'reviews_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'reviews', ['Category'])


    def backwards(self, orm):
        # Deleting model 'Review'
        db.delete_table(u'reviews_review')

        # Removing M2M table for field categories on 'Review'
        db.delete_table(db.shorten_name(u'reviews_review_categories'))

        # Deleting model 'Like'
        db.delete_table(u'reviews_like')

        # Removing M2M table for field user on 'Like'
        db.delete_table(db.shorten_name(u'reviews_like_user'))

        # Deleting model 'Category'
        db.delete_table(u'reviews_category')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'registration.registrationprofile':{
            'Meta': {'object_name': 'RegistrationProfile'},
             u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
             'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
             'activation_key': ('django.db.models.fields.CharField',[], {'max_length': '200'})
        },
        u'reviews.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'reviews.like': {
            'Meta': {'object_name': 'Like'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'review': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.Review']"}),
            'total_likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'likes'", 'symmetrical': 'False', 'to': u"orm['auth.User']"})
        },
        u'reviews.review': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Review'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'reviews'", 'symmetrical': 'False', 'to': u"orm['reviews.Category']"}),
            'cons': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pros': ('django.db.models.fields.TextField', [], {}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'score': ('django.db.models.fields.FloatField', [], {}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['reviews']
