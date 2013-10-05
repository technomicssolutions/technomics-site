# Create your views here.

import os
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
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
        'slideshow' : slideshow,
    }
    return render(request, 'home.html',context)
    
def renderpage(request, slug):
    if slug:
        template = "%s.html" % slug
        services_page = Services.objects.latest('id')
        services_section = Services_section.objects.all()
        services_left = services_section[0]
        services_right = services_section[1]
        context = {'services_page': services_page,
                   'services_left': services_left,
                   'services_right': services_right
        }
        return render(request, template, context)


@csrf_exempt
def contact_us(request):
    context = {}
    if request.method == 'POST':
        contact_us = Contactus();
        contact_us.name = request.POST['name']
        contact_us.email_id = request.POST['email']
        contact_us.message = request.POST['msg']
        contact_us.save();
        contact_us.send_contact_notification_mail_to_admins();
    return HttpResponse('You have successfully sent the Message')

def services(request):
    services_page = Services.objects.latest('id')
    services_section = Services_section.objects.all()
    services_left = services_section[0]
    services_right = services_section[1]
    context = {'services_page': services_page,
               'services_left': services_left,
               'services_right': services_right
    }
    return render(request, 'services.html', context)



