from django.db import models

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
        verbose_name = 'Feature'
        verbose_name_plural = 'Feature'
            
    def __unicode__(self):
        return self.title

    def image_thumb(self):
        return '<img height="50px" src="/site_media/%s"/>' % self.image
    image_thumb.allow_tags = True

class Newsevents(Dates):
    title = models.CharField('Content head', max_length=100, null=True, blank=True, help_text='Heading of the content in the page')
    description = models.TextField('Content description', null=True, blank=True, help_text='Content description')
    event_date = models.DateTimeField('Event date')
    image = models.ImageField(upload_to='uploads/images/', help_text="Upload image to be displayed in the content section")

    class Meta:
        verbose_name = 'News & Events'
        verbose_name_plural = 'News & Events'

    def __unicode__(self):
        return self.title

    def image_thumb(self):
        return '<img height="50px" src="/site_media/%s"/>' % self.image
    image_thumb.allow_tags = True


class Aboutus(Dates):
    title = models.CharField('Content head', max_length=100, null=True, blank=True, help_text='Heading of the content in the page')
    description = models.TextField('Content description', null=True, blank=True, help_text='Content description')
    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

    def __unicode__(self):
        return self.title

class Contactus(Dates):
    name = models.CharField(max_length=80, help_text='Name of the user')
    email_id = models.EmailField(help_text='Email id of the user')
    message = models.TextField(blank=True, null=True, help_text='The message sent by the user')
    # send button

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

class Blog(Dates):
    title = models.CharField('Content Subhead', max_length=500, null=True, blank=True, help_text='Sub heading of the content in the page')
    description = models.TextField('Content description', null=True, blank=True, help_text='Content description')
    author = models.CharField(max_length=80, help_text='Name of the author')

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'

    def __unicode__(self):
        return self.title
            

class Comment(Dates):
    blog_id = models.ForeignKey(Blog, help_text="Corresponding Blog")
    author = models.CharField(max_length=80, help_text='Name of the user')
    description = models.TextField('Content description', null=True, blank=True, help_text='Content description')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
            

class Services(Dates):
    title = models.CharField('Content Subhead', max_length=100, null=True, blank=True, help_text='Heading of the content in the page')
    banner_image = banner = models.ImageField(upload_to='uploads/images/', help_text="Upload banner to be displayed in home page")
    content_subhead = models.CharField('Content Subhead', max_length=100, null=True, blank=True, help_text='Sub heading of the content in the page')
    description = models.TextField('Content description', null=True, blank=True, help_text='Content description')

    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Services'

    def __unicode__(self):
        return self.title

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

class Testimonials(Dates):
    title = models.CharField('Content Subhead', max_length=100, null=True, blank=True, help_text='Heading of the content in the page')
    description = models.TextField('Content description', null=True, blank=True, help_text='Content description')
    image = models.ImageField(upload_to='uploads/images/', help_text="Upload image to be displayed in Testimonials section page")
    
    class Meta:
        verbose_name = 'Testimonials'
        verbose_name_plural = 'Testimonials'

    def __unicode__(self):
        return self.title

    def image_thumb(self):
        return '<img height="50px" src="/site_media/%s"/>' % self.image
    image_thumb.allow_tags = True

class Slideshow(Dates):
    image = models.ImageField(upload_to='uploads/images/', help_text="Upload image to be displayed as slideshow in the page")
    slogan = models.ImageField(upload_to='uploads/images/', help_text="Upload slogan to be displayed as a text in the slideshow")
    description = models.TextField('Content description', null=True, blank=True, help_text='Content description')       
    
    class Meta:
        verbose_name = 'Slideshow'
        verbose_name_plural = 'Slideshow'
            

    def image_thumb(self):
        return '<img height="50px" src="/site_media/%s"/>' % self.image
    image_thumb.allow_tags = True                   
        
                        
        
        
        
        
        