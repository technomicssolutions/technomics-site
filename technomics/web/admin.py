from django.contrib import admin
from django.db import models
from models import Contactus, Dates, Homepage, Feature, Newsevents, Aboutus, Blog, Comment, Slideshow, Services, Services_section, Testimonials
from adminthumbnail import AdminImageWidget

class HomepageAdmin(admin.ModelAdmin):
	list_display = ('image_thumb', 'customer_care')
	list_display_links = ('image_thumb', 'customer_care')
	formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget()},
    }

class FeatureAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'image_thumb')
	formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget()},
    }

class NewseventsAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'event_date', 'image_thumb')
	formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget()},
    }

class AboutusAdmin(admin.ModelAdmin):
	list_display = ('title', 'description')

class ContactusAdmin(admin.ModelAdmin):
	list_display = ('name', 'email_id', 'message')

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'author')

class CommentAdmin(admin.ModelAdmin):
	list_display = ('author', 'description')

class ServicesAdmin(admin.ModelAdmin):
	list_display = ('title', 'banner_thumb', 'content_subhead', 'description')
	formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget()},
    }
		
class Services_sectionAdmin(admin.ModelAdmin):
	list_display = ('section_head','image_thumb', 'description')
	formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget()},
    }

class TestimonialsAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'image_thumb')
	formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget()},
    }

class SlideshowAdmin(admin.ModelAdmin):
	list_display = ('image_thumb', 'slogan', 'description')
	formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget()},
    }
		
		
admin.site.register(Homepage, HomepageAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Newsevents, NewseventsAdmin)
admin.site.register(Aboutus, AboutusAdmin)
admin.site.register(Contactus, ContactusAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Services_section, Services_sectionAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
admin.site.register(Slideshow)