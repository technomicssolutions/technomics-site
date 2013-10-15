from django.contrib.sites.models import Site
from django.db import models
from web.models import Contactus, Dates, Homepage, Feature, Newsevents, Aboutus, Blog, Comment, Slideshow, Services, Services_section,  Menu

def site_variables(request):
    current_site = Site.objects.get_current()

    header_objs = Homepage.objects.all()
    if ( header_objs ):
        header_obj = header_objs[0]
    else:
        header_obj = ''

    menu_obj = Menu.objects.all().order_by('order');
    return {
        'SITE_ROOT_URL_S': 'http://%s/'%(current_site.domain),
        'SITE_ROOT_URL': 'http://%s'%(current_site.domain),
        'context_header': header_obj,
        'context_menu': menu_obj,
    }
 
