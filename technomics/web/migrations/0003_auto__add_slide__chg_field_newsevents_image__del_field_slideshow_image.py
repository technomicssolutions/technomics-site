# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slide'
        db.create_table(u'web_slide', (
            (u'dates_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Dates'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('slideshow_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Slideshow'])),
        ))
        db.send_create_signal(u'web', ['Slide'])


        # Changing field 'Newsevents.image'
        db.alter_column(u'web_newsevents', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))
        # Deleting field 'Slideshow.image'
        db.delete_column(u'web_slideshow', 'image')

        # Deleting field 'Slideshow.slogan'
        db.delete_column(u'web_slideshow', 'slogan')

        # Deleting field 'Slideshow.description'
        db.delete_column(u'web_slideshow', 'description')

        # Adding field 'Slideshow.left_arrow'
        db.add_column(u'web_slideshow', 'left_arrow',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Slideshow.right_arrow'
        db.add_column(u'web_slideshow', 'right_arrow',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Slideshow.max_slide_count'
        db.add_column(u'web_slideshow', 'max_slide_count',
                      self.gf('django.db.models.fields.IntegerField')(default=3),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting model 'Slide'
        db.delete_table(u'web_slide')


        # Changing field 'Newsevents.image'
        db.alter_column(u'web_newsevents', 'image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100))

        # User chose to not deal with backwards NULL issues for 'Slideshow.image'
        raise RuntimeError("Cannot reverse this migration. 'Slideshow.image' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Slideshow.slogan'
        raise RuntimeError("Cannot reverse this migration. 'Slideshow.slogan' and its values cannot be restored.")
        # Adding field 'Slideshow.description'
        db.add_column(u'web_slideshow', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Slideshow.left_arrow'
        db.delete_column(u'web_slideshow', 'left_arrow')

        # Deleting field 'Slideshow.right_arrow'
        db.delete_column(u'web_slideshow', 'right_arrow')

        # Deleting field 'Slideshow.max_slide_count'
        db.delete_column(u'web_slideshow', 'max_slide_count')

    models = {
        u'web.aboutus': {
            'Meta': {'object_name': 'Aboutus', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'web.blog': {
            'Meta': {'object_name': 'Blog', '_ormbases': [u'web.Dates']},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        u'web.comment': {
            'Meta': {'object_name': 'Comment', '_ormbases': [u'web.Dates']},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'blog_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Blog']"}),
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'web.contactus': {
            'Meta': {'object_name': 'Contactus', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'email_id': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'web.dates': {
            'Meta': {'object_name': 'Dates'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'web.feature': {
            'Meta': {'object_name': 'Feature', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'web.homepage': {
            'Meta': {'object_name': 'Homepage', '_ormbases': [u'web.Dates']},
            'customer_care': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'web.newsevents': {
            'Meta': {'object_name': 'Newsevents', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'event_date': ('django.db.models.fields.DateTimeField', [], {}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'web.services': {
            'Meta': {'object_name': 'Services', '_ormbases': [u'web.Dates']},
            'banner_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'content_subhead': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'web.services_section': {
            'Meta': {'object_name': 'Services_section', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'section_head': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'section_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'web.slide': {
            'Meta': {'object_name': 'Slide', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slideshow_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Slideshow']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'web.slideshow': {
            'Meta': {'object_name': 'Slideshow', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'left_arrow': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'max_slide_count': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'right_arrow': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'web.testimonials': {
            'Meta': {'object_name': 'Testimonials', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['web']