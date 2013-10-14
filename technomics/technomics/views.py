# Create your views here.

import os
import re
import os.path
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.db import models
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from web.models import Contactus, Dates, Homepage, Feature, Newsevents, Aboutus, Blog, Comment, Slideshow, Services, Services_section, \
Testimonials, Candidate, Vacancy, Menu
from web.forms import BlogCommentForm, CandidateFreshersForm, CandidateExperiencedForm, BlogForm
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

# def services(request):
#     services_page = Services.objects.latest('id')
#     services_section = Services_section.objects.all()
#     services_left = services_section[0]
#     services_right = services_section[1]
#     context = {'services_page': services_page,
#                'services_left': services_left,
#                'services_right': services_right
#     }
#     return render(request, 'services.html', context)
    
def rendermenu(request, menuslug):
    if menuslug:
        services_page = Services.objects.latest('id')
        template = "%s.html" % menuslug
        services_left = ''
        services_right = ''
        aboutus = ''
        menu = Menu.objects.get(slug=menuslug)
        sub_menus = menu.submenu_set.all()
        if sub_menus.count():
            return rendersubmenu(request, menuslug, sub_menus[0].slug)
        
        elif menuslug == 'about_us':            
            aboutus = Aboutus.objects.latest('id')
        context = {
            'aboutus': aboutus,
            'services_page': services_page,
            'services_left': services_left,
            'services_right': services_right
        }
            

        return render(request, template, context)


def rendersubmenu(request, menu_slug, submenuslug):
    if menu_slug:
        if submenuslug:
            template = "%s.html" % submenuslug
            freshersform = ''
            vacancies = ''
            services_page = Services.objects.latest('id')
            
            if submenuslug == 'freshers':
                freshersform = CandidateFreshersForm()

            elif submenuslug == 'experienced':
                vacancies = Vacancy.objects.all().exclude(name = 'Freshers')
            context = {
                'services_page': services_page,
                'form': freshersform,
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
        data_dict_form = CandidateExperiencedForm(request.POST,request.FILES)
        data = request.POST
        if request.method == 'POST':
            if data_dict_form.is_valid():
                candidate = Candidate()
                vacancy = Vacancy.objects.get(id = int(vacancy_id))
                vacancy_name = re.sub(r"\s+", '_', vacancy.name.lower())
                candidate_name = re.sub(r"\s+", '_', data['name'].lower())
                fileobj = request.FILES['resume']
                file_extension = fileobj.name.split(".")[-1]
                path = os.path.dirname(__file__)
                resume_file_name = 'experienced_%s_%s'%(candidate_name, str(vacancy_id))+"."+file_extension
                resume_name = path+'/media/uploads/resumes/%s'%(resume_file_name)
                file_name = '%s'%(resume_name)
                candidate.name = data['name']
                candidate.candidate_type = CANDIDATE_TYPE_EXPERIENCED
                candidate.email = data['email']
                candidate.phone = data['phone']
                candidate.address = data['address']
                candidate.qualification = data['qualification']
                candidate.vacancy = vacancy
                with open(file_name, 'w') as destination:
                    for chunk in fileobj.chunks():
                        destination.write(chunk)
                candidate.resume.name = "uploads/resumes/"+resume_file_name
                candidate.save()
                candidate.send_career_notification_mail_to_admins()
        return HttpResponse('You have successfully registered')

def freshers_detail(request):
    context = {}
    data_dict_form = CandidateFreshersForm(request.POST,request.FILES)
    data = request.POST
    if request.method == 'POST':
        if data_dict_form.is_valid():
            candidate = Candidate()
            vacancy = Vacancy.objects.get(name = 'Freshers')
            vacancy_name = re.sub(r"\s+", '_', vacancy.name.lower())
            candidate_name = re.sub(r"\s+", '_', data['name'].lower())
            fileobj = request.FILES['resume']
            file_extension = fileobj.name.split(".")[-1]
            path = os.path.dirname(__file__)
            resume_file_name = '%s_%s_%s'%(candidate_name, str(vacancy.id), str(candidate.id))+"."+file_extension
            resume_name = path+'/media/uploads/resumes/%s'%(resume_file_name)
            file_name = '%s'%(resume_name)
            candidate.name = data['name']
            candidate.candidate_type = CANDIDATE_TYPE_FRESHER
            candidate.email = data['email']
            candidate.phone = data['phone']
            candidate.address = data['address']
            candidate.qualification = data['qualification']
            candidate.vacancy = vacancy
            with open(file_name, 'wb+') as destination:
                for chunk in fileobj.chunks():
                    destination.write(chunk)
            candidate.resume.name = "uploads/resumes/"+resume_file_name
            candidate.save()
            candidate.send_career_notification_mail_to_admins()
    return HttpResponse('You have successfully sent the Message')


class BlogView(View):
    def get(self, request):
        template_name = 'add_blog.html'
        blog_form = BlogForm()
        context = {}
        context ['blog_form'] = blog_form
        return render(request, template_name, context)

    def post(self, request):
        context = {}
        data_dict_form = BlogForm(request.POST)
        data = request.POST
        name = request.user.username
        if request.method == 'POST':
            if data_dict_form.is_valid():
                blog = Blog()
                blog.title = data['title']
                blog.description = data['description']
                blog.author = name
                blog.save()
        return HttpResponse('You have successfully added the blog')


class BlogCommentView(View):
    def get(self, request, blog_id):
        context = listing(request)
        template_name = 'blog.html'
        comment_form = BlogCommentForm()
        context['comment_form'] = comment_form
        context['blog_id'] = int(blog_id)
        return render(request, template_name, context)

    def post(self, request, blog_id):
        context = {}
        data_dict_form = BlogCommentForm(request.POST)
        data = request.POST
        if request.method == 'POST':
            if data_dict_form.is_valid():
                blog = Blog.objects.get(id=int(blog_id))
                comment = Comment()
                comment.blog_id = blog
                comment.description = data['description']
                comment.author = request.user.username
                comment.save()
        return HttpResponse('You have successfully added the comment')


def blog_listing(request):
    context = listing(request)
    return render(request, 'blog.html',context)


def listing(request):
    blogs_list = Blog.objects.all()
    services_page = Services.objects.latest('id')
    paginator = Paginator(blogs_list, 5)

    page = request.GET.get('page')
    print 'page', page
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {
    'services_page': services_page,
    'blogs': blogs,
    'is_staff': request.user.is_staff
    }
    return context
