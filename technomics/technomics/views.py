# Create your views here.

import os
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.db import models
from web.models import Contactus, Dates, Homepage, Feature, Newsevents, Aboutus, Blog, Comment, Slideshow, Services, Services_section, Testimonials, Candidate
from web.forms import CommentForm, FresherForm

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
    
def rendermenu(request, menuslug):
    if menuslug:
        template = "%s.html" % menuslug
        slideshow = Slideshow.objects.latest('id')
        if menuslug == 'services':
            services_page = Services.objects.latest('id')
            services_section = Services_section.objects.all()
            services_left = services_section[0]
            services_right = services_section[1]
            context = {'services_page': services_page,
                       'services_left': services_left,
                       'services_right': services_right
            }
        elif menuslug == 'about_us':
            aboutus = Aboutus.objects.latest('id')
            context = { 
                'aboutus': aboutus,
                'slideshow' : slideshow,
            }
        elif menuslug == 'contact_us':
            context = {
                'slideshow' : slideshow,
            }
        elif menuslug == 'blog':
            blogs = Blog.objects.all()
            #                comments = Comment.objects.filter(blog_id=blog.id)
            from django.forms.formsets import formset_factory
            CommentFormSet = formset_factory(CommentForm, max_num=len(blogs))
            formset = CommentFormSet()
            print formset
            context = {
            'slideshow': slideshow,
            'blogs_formset': zip(blogs,formset),
            #                    'comments': comments
            }

        return render(request, template, context)
def rendersubmenu(request, menuslug, submenuslug):
    if menuslug:
        if submenuslug:
            print "submenu", submenuslug
            template = "%s.html" % submenuslug
            slideshow = Slideshow.objects.latest('id')
            if submenuslug == 'school_resource_planning':
                services_page = Services.objects.latest('id')
                context = {
                    'services_page': services_page,
                }
            elif submenuslug == 'smartbook':
                context = {
                    'slideshow' : slideshow,
                }
            elif submenuslug == 'education':
                context = {
                    'slideshow': slideshow,
                }
            elif submenuslug == 'e_business':
                context = {
                    'slideshow': slideshow,
                }
            elif submenuslug == 'banking_and_financial':
                context = {
                    'slideshow': slideshow,
                }
            elif submenuslug == 'retail_and_customer_products':
                context = {
                    'slideshow': slideshow,
                }
            elif submenuslug == 'industrial_manufacturing':
                context = {
                    'slideshow': slideshow,
                }
            elif submenuslug == 'hospitality':
                context = {
                    'slideshow': slideshow,
                }
            elif submenuslug == 'linux_managed_services':
                services_page = Services.objects.latest('id')
                context = {
                    'services_page': services_page,
                }
            elif submenuslug == 'cloud_services':
                services_page = Services.objects.latest('id')
                context = {
                    'services_page': services_page,
                }
            elif submenuslug == 'erp_consultation':
                services_page = Services.objects.latest('id')
                print "services", services_page
                context = {
                    'services_page': services_page,
                }
            elif submenuslug == 'customized_software_development':
                services_page = Services.objects.latest('id')
                context = {
                    'services_page': services_page,
                }
            elif submenuslug == 'offshore_dedicated_staffing':
                services_page = Services.objects.latest('id')
                context = {
                    'services_page': services_page,
                }
            elif submenuslug == 'web_application':
                services_page = Services.objects.latest('id')
                context = {
                    'services_page': services_page,
                }
            elif submenuslug == 'e_commerce':
                services_page = Services.objects.latest('id')
                context = {
                    'services_page': services_page,
                }
            elif submenuslug == 'open_source_solutions':
                services_page = Services.objects.latest('id')
                context = {
                    'services_page': services_page,
                }
            elif submenuslug == 'mobile_platform_development':
                services_page = Services.objects.latest('id')
                context = {
                    'services_page': services_page,
                }
            elif submenuslug == 'freshers':
                fresherform = FresherForm()
                print fresherform
                context = {
                'slideshow': slideshow,
                'fresherform': fresherform,
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

def freshers_detail(request):
    context = {}
    if request.method == 'POST':
        candidate = Candidate();
#        candidate.name = request.POST['name']
        print "name : ",request.POST['name']
#        candidate.degree = request.POST['degree']
        print "degree :",request.POST['degree']
        print "marks : ",request.POST['marks']
#        candidate.marks = request.POST['marks']
        print "percentage : ",request.POST['percentage']
#        candidate.marks = request.POST['percentage']
#        candidate.save();
#        candidate.send_contact_notification_mail_to_admins();
    return HttpResponse('You have successfully submited details')

