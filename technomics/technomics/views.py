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
        slideshow = Slideshow.objects.latest('id')
        if slug == 'services':
            services_page = Services.objects.latest('id')
            services_section = Services_section.objects.all()
            services_left = services_section[0]
            services_right = services_section[1]
            context = {'services_page': services_page,
                       'services_left': services_left,
                       'services_right': services_right
            }
        elif slug == 'about_us':
            aboutus = Aboutus.objects.latest('id')
            context = { 
                'aboutus': aboutus,
                'slideshow' : slideshow,
            }
        elif slug == 'contact_us':
            context = {
                'slideshow' : slideshow,
            }
        elif slug == 'school_resource_planning':
            services_page = Services.objects.latest('id')
            context = {
                'services_page': services_page,
            }
        elif slug == 'smartbook':
            context = {
                'slideshow' : slideshow,
            }
        elif slug == 'education':
            context = {
                'slideshow': slideshow,
            }
        elif slug == 'e_business':
            context = {
                'slideshow': slideshow,
            }
        elif slug == 'banking_and_financial':
            context = {
                'slideshow': slideshow,
            }
        elif slug == 'retail_and_customer_products':
            context = {
                'slideshow': slideshow,
            }
        elif slug == 'industrial_manufacturing':
            context = {
                'slideshow': slideshow,
            }
        elif slug == 'hospitality':
            context = {
                'slideshow': slideshow,
            }
        elif slug == 'linux_managed_services':
            services_page = Services.objects.latest('id')
            context = {
                'services_page': services_page,
            }
        elif slug == 'cloud_services':
            services_page = Services.objects.latest('id')
            context = {
                'services_page': services_page,
            }
        elif slug == 'erp_consultation':
            services_page = Services.objects.latest('id')
            print "services", services_page
            context = {
                'services_page': services_page,
            }
        elif slug == 'customized_software_development':
            services_page = Services.objects.latest('id')
            context = {
                'services_page': services_page,
            }
        elif slug == 'offshore_dedicated_staffing':
            services_page = Services.objects.latest('id')
            context = {
                'services_page': services_page,
            }
        elif slug == 'web_application':
            services_page = Services.objects.latest('id')
            context = {
                'services_page': services_page,
            }
        elif slug == 'e_commerce':
            services_page = Services.objects.latest('id')
            context = {
                'services_page': services_page,
            }
        elif slug == 'open_source_solutions':
            services_page = Services.objects.latest('id')
            context = {
                'services_page': services_page,
            }
        elif slug == 'mobile_platform_development':
            services_page = Services.objects.latest('id')
            context = {
                'services_page': services_page,
            }

        return render(request, template, context)


@csrf_exempt
def contact_us(request):
    context = {}
    if request.method == 'POST':
        contact_us = Contactus();
        contact_us.name = request.POST['name']
        print "name : ",request.POST['name']
        contact_us.email_id = request.POST['email']
        print "email : ",request.POST['email']
        contact_us.message = request.POST['message']
        print "message :",request.POST['message']
        contact_us.subject = request.POST['subject']
        print "subject :",request.POST['subject']
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



