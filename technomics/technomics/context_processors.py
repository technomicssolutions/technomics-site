from django.contrib.sites.models import Site
from django.db import models
from web.models import Contactus, Dates, Homepage, Feature, Newsevents, Aboutus, Blog, Comment, Slideshow, Services, Services_section, Testimonials

def site_variables(request):
    current_site = Site.objects.get_current()

    header_objs = Homepage.objects.all()
    if ( header_objs ):
        header_obj = header_objs[0]
    else:
        header_obj = ''

    footer_abtus = Aboutus.objects.all()
    if (footer_abtus):
        aboutus = footer_abtus[0]
    else:
        aboutus = ''

    footer_blog = Blog.objects.all();
    if (footer_blog):
        first_blog = footer_blog[0];
        second_blog = footer_blog[1];
        third_blog = footer_blog[2];
    else :
        first_blog = '';
        second_blog = '';
        third_blog = '';

    return {
        'SITE_ROOT_URL_S': 'http://%s/'%(current_site.domain),
        'SITE_ROOT_URL': 'http://%s'%(current_site.domain),
        'context_header': header_obj,
        'context_abtus': aboutus,
        'context_fblog': first_blog,
        'context_sblog': second_blog,
        'context_tblog': third_blog
    }
 
