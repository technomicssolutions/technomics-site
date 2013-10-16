from django.contrib import admin
from django.db import models
from models import Contactus, Dates, Homepage, Feature, Newsevents, Aboutus, Blog, \
 Comment, Slideshow, Services, Services_section, Slide, Menu, Submenu, Vacancy, Candidate
from adminthumbnail import AdminImageWidget
from django.views.generic.list import ListView

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
    list_display = ('name', 'email_id', 'subject', 'message')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'description')

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('banner_thumb', 'content_subhead', 'description')
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget()},
    }
        
class Services_sectionAdmin(admin.ModelAdmin):
    list_display = ('section_head','image_thumb', 'description')
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget()},
    }


class SlideInline(admin.TabularInline):
    model = Slide
    initial_forms = 3
    max_num = 3
    extra = 0

    fk_name = 'slideshow_id'
    list_display = ('text', 'image_thumb')
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget()},
    }

class SlideshowAdmin(admin.ModelAdmin):
    inlines = [SlideInline]
    list_display = ('right_arrow_thumb', 'left_arrow_thumb', 'max_slide_count','bullet_active_thumb', 'bullet_inactive_thumb')
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget()},
    }

class SubmenuInline(admin.TabularInline):
    model = Submenu

    fk_name = 'menu'
    list_display = ('sub_title', 'slug', 'order')
    exclude = ('slug',)

class MenuAdmin(admin.ModelAdmin):
    inlines = [SubmenuInline]
    list_display = ('title', 'slug', 'order')
    exclude = ('slug',)

class  CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'candidate_type', 'email', 'phone', 'address', 'qualification', 'experience', 'resume')
    
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'no_of_vacancy', 'description', 'opening_date', 'closing_date')
        
        
        
        
admin.site.register(Homepage, HomepageAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Newsevents, NewseventsAdmin)
admin.site.register(Aboutus, AboutusAdmin)
admin.site.register(Contactus, ContactusAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Services_section, Services_sectionAdmin)
admin.site.register(Slideshow, SlideshowAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Vacancy, VacancyAdmin)