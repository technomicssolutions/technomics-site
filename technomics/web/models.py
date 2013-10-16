from django.db import models
from django.template.loader import render_to_string
from django.core.mail import BadHeaderError, mail_managers, send_mail, EmailMessage, mail_admins
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.conf import settings
from .utils import slug
from web import CANDIDATE_TYPE, CANDIDATE_TYPE_FRESHER, QUALIFICATION_TYPE, QUALIFICATION_TYPE_BSC
# Create your models here.


class Dates(models.Model):
    created_date = models.DateTimeField('Created Date', auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField('Modified Date', auto_now=True, null=True, blank=True)

class Homepage(Dates):
    logo = models.ImageField(upload_to='uploads/images/', help_text="Upload image to be displayed as the logo in the page")
    customer_care = models.CharField('Phone', max_length=50, blank=True, null=True, help_text='Phone number for the reference')

    class Meta:
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Page'
            
    # def __unicode__(self):
    #     return self.

    def image_thumb(self):
        return '<img height="50px" src="/site_media/%s"/>' % self.logo
    image_thumb.allow_tags = True

class Feature(Dates):
    title = models.CharField('Content head', max_length=100, null=True, blank=True, help_text='Heading of the content in the page')
    description = models.TextField('Content description', null=True, blank=True, help_text='Content description')
    image = models.ImageField(upload_to='uploads/images/', help_text="Upload image to be displayed in the content section")
    
    class Meta:
        verbose_name = 'Home Left Section'
        verbose_name_plural = 'Home Left Section'
            
    def __unicode__(self):
        return self.title

    def image_thumb(self):
        return '<img height="50px" src="/site_media/%s"/>' % self.image
    image_thumb.allow_tags = True

class Newsevents(Dates):
    title = models.CharField('Content head', max_length=100, null=True, blank=True, help_text='Heading of the content in the page')
    description = models.TextField('Content description', null=True, blank=True, help_text='Content description')
    event_date = models.DateTimeField('Event date')
    image = models.ImageField(upload_to='uploads/images/', help_text="Upload image to be displayed in the content section", null= True, blank= True)

    class Meta:
        verbose_name = 'Home Right Section'
        verbose_name_plural = 'Home Right Section'

    def __unicode__(self):
        return self.title

    def image_thumb(self):
        return '<img height="50px" src="/site_media/%s"/>' % self.image
    image_thumb.allow_tags = True


class Aboutus(Dates):
    title = models.CharField('Content head', max_length=100, null=True, blank=True, help_text='Heading of the content in the page')
    description = models.TextField('Content description', null=True, blank=True, help_text='Content description')
    # left_content = models.TextField('Left content description', null=True, blank=True, help_text='Left content description')
    # right_content = models.TextField('Right content description', null=True, blank=True, help_text='Right content description')
    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

    def __unicode__(self):
        return self.title

class Contactus(Dates):
    name = models.CharField('Name', max_length=80)
    email_id = models.EmailField('Email', max_length = 120)
    subject = models.CharField('Subject', max_length = 100)
    message = models.TextField('Message', blank=True, null=True)
    
    def __unicode__(self):
        return self.name

    def send_contact_notification_mail_to_admins(self):
        root_url = 'http://%s'%(Site.objects.get_current().domain)
        subject = self.subject
        # contact_us/subject = 'Contact me'. self.name
        message = render_to_string('contactus_notification.html', {
            'name': self.name,
            'email': self.email_id,
            'content': self.message,
            'subject': self.subject,
            'root_url': root_url,
        }) 
        try:
            mail_admins(subject, message, fail_silently=False, connection=None, html_message=None)
        except BadHeaderError:
            return HttpResponse('Invalid Header Found')

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

class Blog(Dates):
    title = models.CharField('Content Subhead', max_length=500)
    description = models.TextField('Content Description')
    author = models.CharField(max_length=80, help_text='Name of the author')

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
        ordering = ['-created_date']

    def __unicode__(self):
        return self.title


class Comment(Dates):
    blog_id = models.ForeignKey(Blog, help_text="Corresponding Blog")
    author = models.CharField(max_length=80, help_text='Name of the user')
    description = models.TextField('Comment', null=True, blank=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_date']
            

class Services(Dates):
    content_subhead = models.CharField('Content Subhead', max_length=100, null=True, blank=True, help_text='Sub heading of the content in the page')
    description = models.TextField('Content description', null=True, blank=True, help_text='Content description')
    banner_image = models.ImageField(upload_to='uploads/images/', help_text="Upload banner to be displayed in the corresponding page")
    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Services'

    def banner_thumb(self):
        return '<img height="50px" src="/site_media/%s"/>' % self.banner_image
    banner_thumb.allow_tags = True

class Services_section(Dates):
    section_head = models.CharField('Content Subhead', max_length=100, null=True, blank=True, help_text='Heading of the content in the page')
    section_image = models.ImageField(upload_to='uploads/images/', help_text="Upload section image to be displayed in services section page")
    description = models.TextField('Content description', null=True, blank=True, help_text='Content description')
    
    class Meta:
        verbose_name = 'Services Sections'
        verbose_name_plural = 'Services Sections'

    def image_thumb(self):
        return '<img height="50px" src="/site_media/%s"/>' % self.section_image
    image_thumb.allow_tags = True

class Slideshow(Dates):
    left_arrow = models.ImageField(upload_to='uploads/images/', help_text="Upload image to be displayed in the banner" )
    right_arrow = models.ImageField(upload_to='uploads/images', help_text="Upload image to be displayed in the banner" )
    max_slide_count = models.IntegerField('Slide Count', help_text='Maximum number of slides to be appear in the banner', default=3)
    bullet_active = models.ImageField(upload_to='uploads/images/', help_text="Upload image to be displayed as the active bullet in the banner" )
    bullet_inactive = models.ImageField(upload_to='uploads/images/', help_text="Upload image to be displayed as the inactive bullet in the banner" )
    class Meta:
        verbose_name = 'Slideshow'
        verbose_name_plural = 'Slideshow'
            

    def left_arrow_thumb(self):
        return '<img height="50px" src="/site_media/%s"/>' % self.left_arrow
    left_arrow_thumb.allow_tags = True 

    def right_arrow_thumb(self):
        return '<img height="50px" src="/site_media/%s"/>' % self.right_arrow
    right_arrow_thumb.allow_tags = True

    def bullet_active_thumb(self):
        return '<img height="19px" src="/site_media/%s"/>' % self.bullet_active
    bullet_active.allow_tags = True

    def bullet_inactive_thumb(self):
        return '<img height="19px" src="/site_media/%s"/>' % self.bullet_inactive
    bullet_inactive.allow_tags = True

class Slide(Dates):
    text = models.CharField('Slogan', max_length = 200, null=True, blank=True, help_text='Slogan to be displayed in the banner')
    image = models.ImageField(upload_to='uploads/images/', help_text='Upload image to be displayed as slideshow')
    slideshow_id = models.ForeignKey(Slideshow, help_text='Corresponding Slideshow image')
    
    class Meta:
        verbose_name = 'Slides'
        verbose_name_plural = 'Slides'

    def image_thumb(self):
        return '<img height="50px" src="/site_media/%s"/>' % self.image
    image_thumb.allow_tags = True 

class Menu(Dates):
    title = models.CharField('Menu', max_length = 50, help_text = 'Name of the menu')
    slug = models.CharField('Slug', max_length = 100, help_text = 'Slug of the menu')
    order = models.IntegerField('Order', max_length = 10, default = '1', help_text = 'Order of the menus')
    # banner_image = models.ImageField(upload_to='uploads/images/', help_text="Upload banner to be displayed in the corresponding page")
    
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def save(self, *args, **kwargs):
        self.slug = slug(self.title)
        super(Menu, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

class Submenu(Dates):
    menu = models.ForeignKey(Menu, help_text = 'Corresponding menu')
    title = models.CharField('Submenu', max_length = 200 , help_text = 'Name of the submenu')
    slug = models.CharField('Slug', max_length = 200, help_text = 'Slug of the submenu')
    order = models.IntegerField('Order', max_length = 10, default = '1', help_text = 'Order of the submenu')
    # banner_image = models.ImageField(upload_to='uploads/images/', help_text="Upload banner to be displayed in the corresponding page")

    def save(self, *args, **kwargs):
        self.slug = slug(self.title)
        super(Submenu, self).save(*args, **kwargs) 

    def __unicode__(self):
        return self.title                     
        


class Vacancy(Dates):
    name = models.CharField('Name', max_length = 200, null=True, blank=True, help_text='Name of the Post')
    no_of_vacancy = models.IntegerField('No of Vacancy', max_length = 10, null = True, blank = True, default = '0', help_text = 'No of vacancies')
    description = models.TextField('Description', null = True, blank = True)
    opening_date = models.DateField('Opening Date', null = True, blank = True, help_text = 'Opening date')
    closing_date = models.DateField('Closing Date', null = True, blank = True, help_text = 'Closing date')

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __unicode__(self):
        return self.name
            

class  Candidate(Dates):
    name = models.CharField('Name', max_length = 150)
    candidate_type = models.CharField('Candidate type', max_length = 50, choices = CANDIDATE_TYPE, default = CANDIDATE_TYPE_FRESHER)
    email = models.EmailField('Email', max_length = 120)
    phone = models.CharField('Phone', max_length = 15)
    address = models.TextField('Address', max_length = 500)
    qualification = models.CharField('Qualification', max_length = 50, choices = QUALIFICATION_TYPE, default = QUALIFICATION_TYPE_BSC)
    resume = models.FileField(upload_to='uploads/resumes/')
    vacancy = models.ForeignKey('Vacancy')

    class Meta:
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'

    def __unicode__(self):
        return self.name

    def send_career_notification_mail_to_managers(self):
        root_url = 'http://%s'%(Site.objects.get_current().domain)
        subject = 'Contact me %s_%s'%(self.candidate_type, self.name)
        message = render_to_string('careers_notification.html', {
        'name': self.name,
        'email': self.email,
        'type': self.candidate_type
        }) 
#        body = 'name :'+self.name+'\n'
#        body += 'candidate_type :'+self.candidate_type+'\n'
#        body += 'email :'+self.email+'\n'
#        body += 'phone :'+self.phone+'\n'
#        body += 'address :'+self.address+'\n'
#        body += 'qualification :'+self.qualification+'\n'
#        body += 'for vacancy :'+self.vacancy.name+'\n'
#        email = EmailMessage(subject, body)
#        print dir(email)
        
        try:
            mail_managers(subject, message, fail_silently=False, connection=None, html_message=None)
        except BadHeaderError:
            return HttpResponse('Invalid Header Found')

