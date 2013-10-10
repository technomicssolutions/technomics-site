# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Freshers'
        db.delete_table(u'web_freshers')

        # Deleting model 'Experienced'
        db.delete_table(u'web_experienced')

        # Adding field 'Candidate.name'
        db.add_column(u'web_candidate', 'name',
                      self.gf('django.db.models.fields.CharField')(default='test', max_length=100),
                      keep_default=False)

        # Adding field 'Candidate.candidate_type'
        db.add_column(u'web_candidate', 'candidate_type',
                      self.gf('django.db.models.fields.CharField')(default='FRESHER', max_length=50),
                      keep_default=False)

        # Adding field 'Candidate.email'
        db.add_column(u'web_candidate', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='test@gmail.com', max_length=100),
                      keep_default=False)

        # Adding field 'Candidate.phone'
        db.add_column(u'web_candidate', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='123456789', max_length=15),
                      keep_default=False)

        # Adding field 'Candidate.address'
        db.add_column(u'web_candidate', 'address',
                      self.gf('django.db.models.fields.TextField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Candidate.qualification'
        db.add_column(u'web_candidate', 'qualification',
                      self.gf('django.db.models.fields.CharField')(default='BSC', max_length=50),
                      keep_default=False)


        # Changing field 'Candidate.resume'
        db.alter_column(u'web_candidate', 'resume', self.gf('django.db.models.fields.files.FileField')(max_length=100))

        # Changing field 'Submenu.slug'
        db.alter_column(u'web_submenu', 'slug', self.gf('django.db.models.fields.CharField')(default='test', max_length=200))

        # Changing field 'Submenu.order'
        db.alter_column(u'web_submenu', 'order', self.gf('django.db.models.fields.IntegerField')(max_length=10))

        # Changing field 'Submenu.title'
        db.alter_column(u'web_submenu', 'title', self.gf('django.db.models.fields.CharField')(default='test', max_length=200))

        # Changing field 'Menu.title'
        db.alter_column(u'web_menu', 'title', self.gf('django.db.models.fields.CharField')(default='test', max_length=50))

        # Changing field 'Menu.order'
        db.alter_column(u'web_menu', 'order', self.gf('django.db.models.fields.IntegerField')(max_length=10))

        # Changing field 'Menu.slug'
        db.alter_column(u'web_menu', 'slug', self.gf('django.db.models.fields.CharField')(default='test', max_length=100))

        # Changing field 'Vacancy.closing_date'
        db.alter_column(u'web_vacancy', 'closing_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Vacancy.opening_date'
        db.alter_column(u'web_vacancy', 'opening_date', self.gf('django.db.models.fields.DateField')(null=True))
    def backwards(self, orm):
        # Adding model 'Freshers'
        db.create_table(u'web_freshers', (
            (u'candidate_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Candidate'], unique=True, primary_key=True)),
            ('Qualification', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'web', ['Freshers'])

        # Adding model 'Experienced'
        db.create_table(u'web_experienced', (
            ('candidate_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'candidate_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Candidate'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'web', ['Experienced'])

        # Deleting field 'Candidate.name'
        db.delete_column(u'web_candidate', 'name')

        # Deleting field 'Candidate.candidate_type'
        db.delete_column(u'web_candidate', 'candidate_type')

        # Deleting field 'Candidate.email'
        db.delete_column(u'web_candidate', 'email')

        # Deleting field 'Candidate.phone'
        db.delete_column(u'web_candidate', 'phone')

        # Deleting field 'Candidate.address'
        db.delete_column(u'web_candidate', 'address')

        # Deleting field 'Candidate.qualification'
        db.delete_column(u'web_candidate', 'qualification')


        # Changing field 'Candidate.resume'
        db.alter_column(u'web_candidate', 'resume', self.gf('django.db.models.fields.files.FileField')(max_length=20000))

        # Changing field 'Submenu.slug'
        db.alter_column(u'web_submenu', 'slug', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Submenu.order'
        db.alter_column(u'web_submenu', 'order', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True))

        # Changing field 'Submenu.title'
        db.alter_column(u'web_submenu', 'title', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Menu.title'
        db.alter_column(u'web_menu', 'title', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Menu.order'
        db.alter_column(u'web_menu', 'order', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True))

        # Changing field 'Menu.slug'
        db.alter_column(u'web_menu', 'slug', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Vacancy.closing_date'
        db.alter_column(u'web_vacancy', 'closing_date', self.gf('django.db.models.fields.DateField')(default='1-02-2013'))

        # User chose to not deal with backwards NULL issues for 'Vacancy.opening_date'
        raise RuntimeError("Cannot reverse this migration. 'Vacancy.opening_date' and its values cannot be restored.")
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
        u'web.candidate': {
            'Meta': {'object_name': 'Candidate', '_ormbases': [u'web.Dates']},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'candidate_type': ('django.db.models.fields.CharField', [], {'default': "'FRESHER'", 'max_length': '50'}),
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'qualification': ('django.db.models.fields.CharField', [], {'default': "'BSC'", 'max_length': '50'}),
            'resume': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
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
        u'web.testimonials': {
            'Meta': {'object_name': 'Testimonials', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'web.vacancy': {
            'Meta': {'object_name': 'Vacancy', '_ormbases': [u'web.Dates']},
            'closing_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'no_of_vacancy': ('django.db.models.fields.IntegerField', [], {'default': "'0'", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'opening_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['web']