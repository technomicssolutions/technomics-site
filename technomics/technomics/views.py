# Create your views here.

import os
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db import models
from web.models import Contactus, Dates, Homepage, Feature, Newsevents, Aboutus, Blog, Comment, Slideshow, Services, Services_section, Testimonials

def home(request):
    latest_content = Feature.objects.latest('id')
    latest_events = Newsevents.objects.latest('id')
    testimonials = Testimonials.objects.latest('id')
    slideshow = Slideshow.objects.latest('id')
    context = { 
        'latest_content': latest_content,
        'latest_events': latest_events,
        'testimonials' : testimonials,
        'slideshow' : slideshow
    }
    return render(request, 'home.html',context)

def services(request):
    services_page = Services.objects.latest('id')
    services_section = Services_section.objects.all()
    services_left = services_section[1]
    services_right = services_section[0]
    context = {'services_page': services_page,
               'services_left': services_left,
               'services_right': services_right
    }
    return render(request, 'services.html', context)





