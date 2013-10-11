# Create your views here.

import os
import re
import os.path
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.db import models
from django.views.generic.base import View

from web.models import Contactus, Dates, Homepage, Feature, Newsevents, Aboutus, Blog, Comment, Slideshow, Services, Services_section, \
Testimonials, Candidate, Vacancy
from web.forms import CommentForm, CandidateFreshersForm, CandidateExperiencedForm
from web import CANDIDATE_TYPE_FRESHER, CANDIDATE_TYPE_EXPERIENCED

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
        services_page = Services.objects.latest('id')
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
                'services_page': services_page,
            }
        elif menuslug == 'contact_us':
            context = {
                'services_page': services_page,
            }
        elif menuslug == 'blog':
            blogs = Blog.objects.all()
            #                comments = Comment.objects.filter(blog_id=blog.id)
            from django.forms.formsets import formset_factory
            CommentFormSet = formset_factory(CommentForm, max_num=len(blogs))
            formset = CommentFormSet()
            context = {
            'services_page': services_page,
            'blogs_formset': zip(blogs,formset),
            #                    'comments': comments
            }

        return render(request, template, context)

def rendersubmenu(request, menu_slug, submenuslug):
    if menu_slug:
        if submenuslug:
            template = "%s.html" % submenuslug
            services_page = Services.objects.latest('id')
            slideshow = Slideshow.objects.latest('id')
            if submenuslug == 'school_resource_planning':
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
                freshersform = CandidateFreshersForm()
                context = {
                'slideshow': slideshow,
                'freshersform': freshersform,
                }
            elif submenuslug == 'experienced':
                vacancies = Vacancy.objects.all()
                # experienced_form = CandidateExperiencedForm()
                context = {
                    'services_page': services_page,
                    'vacancies': vacancies,
                }
            return render(request, template, context)

class CareersView(View):
    def get(self, request, vacancy_id):
        template_name = 'experienced.html'
        services_page = Services.objects.latest('id')
        context = {}
        experienced_form = CandidateExperiencedForm()
        context = {
            'form':experienced_form,
            'services_page': services_page,
            'vacancy_id': vacancy_id,
        }
        return render(request, template_name, context)

    def post(self, request, vacancy_id):
        context = {}
        data_dict_form = CandidateFreshersForm(request.POST,request.FILES)
        data = request.POST
        vacancy = Vacancy.objects.get(id = vacancy_id)
        vacancy_name = re.sub(r"\s+", '_', vacancy.name.lower())
        candidate_name = re.sub(r"\s+", '_', data['name'].lower())
        resume_name = 'experienced_%s_%s'%(vacancy_name,candidate_name)
        fileobj = request.FILES['resume']
        file_extension = fileobj.name.split(".")[-1]
        file_name = '%s.%s'%(resume_name, file_extension)
        if request.method == 'POST':
            if data_dict_form.is_valid():
                candidate = Candidate()
                candidate.name = data['name']
                candidate.candidate_type = CANDIDATE_TYPE_EXPERIENCED
                candidate.email = data['email']
                candidate.phone = data['phone']
                candidate.address = data['address']
                candidate.qualification = data['qualification']
                candidate.vacancy = vacancy
                with open(file_name, 'wb+') as destination:
                    for chunk in fileobj.chunks():
                        destination.write(chunk)
                candidate.resume = file_name
                candidate.save()
                # candidate.send_contact_notification_mail_to_admins()
        return HttpResponse('You have successfully registered')
        
# def careers_experienced(request):
#     print "in views"
#     context = {}
#     data_dict = CandidateFreshersForm(request.POST, request.FILES)
#     print "data_dict", data_dict
#     # print "file", request.FILES['resume']
#     if request.method == 'POST':
#         candidate = Candidate()
#         candidate.name = data_dict['name']
#         candidate.candidate_type = CANDIDATE_TYPE_EXPERIENCED
#         candidate.email = data_dict['email']
#         candidate.phone = data_dict['phone']
#         candidate.address = data_dict['address']
#         candidate.qualification = data_dict['qualification']
#         # candidate.resume = 
#         # candidate.save()
#     return HttpResponse('You have successfully registered')

@csrf_exempt
def contact_us(request):
    context = {}
    if request.method == 'POST':
        contact_us = Contactus()
        contact_us.name = request.POST['name']
        contact_us.email_id = request.POST['email']
        contact_us.message = request.POST['message']
        contact_us.subject = request.POST['subject']
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
        print "name : ",request.POST['name']
        candidate.name = request.POST['name']
        print "email :",request.POST['email']
        candidate.email = request.POST['email']
        print "phone : ",request.POST['phone']
        candidate.phone = request.POST['phone']
        print "address : ",request.POST['address']
        candidate.address = request.POST['address']
        print "qualification : ",request.POST['qualification']
        candidate.qualification = request.POST['qualification']
        print "resume : ",request.POST['resume']
        candidate.resume = request.POST['resume']
        candidate.save();
        candidate.send_contact_notification_mail_to_admins();
    return HttpResponse('You have successfully submited details')

