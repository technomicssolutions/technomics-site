# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Testimonials'
        db.delete_table(u'web_testimonials')


        # Changing field 'Candidate.resume'
        db.alter_column(u'web_candidate', 'resume', self.gf('django.db.models.fields.files.FileField')(default='newfile', max_length=100))

        # Changing field 'Candidate.vacancy'
        db.alter_column(u'web_candidate', 'vacancy_id', self.gf('django.db.models.fields.related.ForeignKey')(default=221, to=orm['web.Vacancy']))

        # Changing field 'Candidate.address'
        db.alter_column(u'web_candidate', 'address', self.gf('django.db.models.fields.TextField')(default='address', max_length=500))

        # Changing field 'Contactus.email_id'
        db.alter_column(u'web_contactus', 'email_id', self.gf('django.db.models.fields.EmailField')(max_length=120))

        # Changing field 'Blog.title'
        db.alter_column(u'web_blog', 'title', self.gf('django.db.models.fields.CharField')(default='title', max_length=500))

        # Changing field 'Blog.description'
        db.alter_column(u'web_blog', 'description', self.gf('django.db.models.fields.TextField')(default='desc'))
    def backwards(self, orm):
        # Adding model 'Testimonials'
        db.create_table(u'web_testimonials', (
            (u'dates_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Dates'], unique=True, primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['Testimonials'])


        # Changing field 'Candidate.resume'
        db.alter_column(u'web_candidate', 'resume', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

        # Changing field 'Candidate.vacancy'
        db.alter_column(u'web_candidate', 'vacancy_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Vacancy'], null=True))

        # Changing field 'Candidate.address'
        db.alter_column(u'web_candidate', 'address', self.gf('django.db.models.fields.TextField')(max_length=500, null=True))

        # Changing field 'Contactus.email_id'
        db.alter_column(u'web_contactus', 'email_id', self.gf('django.db.models.fields.EmailField')(max_length=75))

        # Changing field 'Blog.title'
        db.alter_column(u'web_blog', 'title', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'Blog.description'
        db.alter_column(u'web_blog', 'description', self.gf('django.db.models.fields.TextField')(null=True))
    models = {
        u'web.aboutus': {
            'Meta': {'object_name': 'Aboutus', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'web.blog': {
            'Meta': {'ordering': "['-created_date']", 'object_name': 'Blog', '_ormbases': [u'web.Dates']},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'web.candidate': {
            'Meta': {'object_name': 'Candidate', '_ormbases': [u'web.Dates']},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'candidate_type': ('django.db.models.fields.CharField', [], {'default': "'FRESHER'", 'max_length': '50'}),
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '120'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'qualification': ('django.db.models.fields.CharField', [], {'default': "'BSC'", 'max_length': '50'}),
            'resume': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'vacancy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Vacancy']"})
        },
        u'web.comment': {
            'Meta': {'ordering': "['-created_date']", 'object_name': 'Comment', '_ormbases': [u'web.Dates']},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'blog_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Blog']"}),
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'web.contactus': {
            'Meta': {'object_name': 'Contactus', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'email_id': ('django.db.models.fields.EmailField', [], {'max_length': '120'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        u'web.menu': {
            'Meta': {'object_name': 'Menu', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': "'1'", 'max_length': '10'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
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
            'bullet_active': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'bullet_inactive': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'left_arrow': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'max_slide_count': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'right_arrow': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'web.submenu': {
            'Meta': {'object_name': 'Submenu', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Menu']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': "'1'", 'max_length': '10'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'web.vacancy': {
            'Meta': {'object_name': 'Vacancy', '_ormbases': [u'web.Dates']},
            'closing_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'no_of_vacancy': ('django.db.models.fields.IntegerField', [], {'default': "'0'", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'opening_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['web']