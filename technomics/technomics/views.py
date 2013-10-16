# Create your views here.

import os
import re
import os.path
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.db import models
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.utils import simplejson

from web.models import Contactus, Dates, Homepage, Feature, Newsevents, Aboutus, Blog, Comment, Slideshow, Services, Services_section, \
    Candidate, Vacancy, Menu
from web.forms import BlogCommentForm, CandidateFreshersForm, CandidateExperiencedForm, BlogForm, ContactUsForm
from web import CANDIDATE_TYPE_FRESHER, CANDIDATE_TYPE_EXPERIENCED

def home(request):
    try:
        latest_content = Feature.objects.latest('id')
        latest_events = Newsevents.objects.latest('id')
        slideshow = Slideshow.objects.latest('id')
        context = { 
            'latest_content': latest_content,
            'latest_events': latest_events,
            'slideshow' : slideshow,
        }
    except:
        context = {}
    
    return render(request, 'home.html',context)

@csrf_exempt
def contact_us(request):
    form = ContactUsForm(request.POST)
    data_dict_form = request.POST
    context = {}
    if request.method == 'POST':
        if form.is_valid():
            contact_us = Contactus()
            contact_us.name = data_dict_form['name']
            contact_us.email_id = data_dict_form['email_id']
            contact_us.message = data_dict_form['message']
            contact_us.subject = data_dict_form['subject']
            contact_us.save();
            contact_us.send_contact_notification_mail_to_admins()
            form = ContactUsForm()
            context ={
                'form': form,
                'message': 'Your message sent successfully',
            }
        else:
            context ={
                'form': form,
            }
    return render(request, 'contact_us.html', context)
    
def rendermenu(request, menuslug):
    if menuslug:
        template = "%s.html" % menuslug
        aboutus = ''
        form = ''
        menu = Menu.objects.get(slug=menuslug)
        sub_menus = menu.submenu_set.all()
        if sub_menus.count():
            return rendersubmenu(request, menuslug, sub_menus[0].slug)
        
        if menuslug == 'about_us':            
            aboutus = Aboutus.objects.latest('id')
        elif menuslug == 'contact_us':
            form = ContactUsForm()
        context = {
            'aboutus': aboutus,
            'form': form,
        }
        return render(request, template, context)


def rendersubmenu(request, menu_slug, submenuslug):
    if menu_slug:
        if submenuslug:
            template = "%s.html" % submenuslug
            freshersform = ''
            vacancies = ''
            
            if submenuslug == 'freshers':
                freshersform = CandidateFreshersForm()

            elif submenuslug == 'experienced':
                vacancies = Vacancy.objects.all().exclude(name = 'Freshers')
            context = {
                'form': freshersform,
                'vacancies': vacancies,
            }
            return render(request, template, context)


class CareersView(View):
    def get(self, request, vacancy_id):
        template_name = 'experienced.html'
        context = {}
        experienced_form = CandidateExperiencedForm()
        context = {
            'form':experienced_form,
            'vacancy_id': vacancy_id,
        }
        return render(request, template_name, context)

    def post(self, request, vacancy_id):
        context = {}
        form = ''
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
                candidate.send_career_notification_mail_to_managers()
                vacancies = Vacancy.objects.all().exclude(name = 'Freshers')
                experienced_form = CandidateExperiencedForm()
                context = {
                    'vacancies': vacancies,
                    'message':'Your application sent successfully.'
                }
            else:
                context ={
                    'form': data_dict_form,
                    'vacancy_id': vacancy_id,
                }
        return HttpResponseRedirect(reverse('render_submenupage', kwargs={'menu_slug' :'careers', 'submenuslug' :'experienced'}))

def freshers_detail(request):
    context = {}
    data_dict_form = CandidateFreshersForm(request.POST,request.FILES)
    form = ''
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
            candidate.send_career_notification_mail_to_managers()
            form = CandidateFreshersForm()
            context = {
                'form': form,
                'message':'Your application sent successfully.'
            }
        else:
            form = CandidateFreshersForm()
            context ={
                'form': data_dict_form,
            }
    return HttpResponseRedirect(reverse('render_submenupage', kwargs={'menu_slug' :'careers', 'submenuslug' :'freshers'}))


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
        name = request.user
        if request.method == 'POST':
            if data_dict_form.is_valid():
                blog = Blog()
                blog.title = data['title']
                blog.description = data['description']
                blog.author = name
                blog.save()
        template_name = 'blog.html'
        context = listing(request)
        return render(request, template_name, context)


class BlogCommentView(View):
    def get(self, request, blog_id):
        template_name = 'blog.html'
        context = listing(request)
        comment_form = BlogCommentForm()
        context['comment_form'] = comment_form
        context['blog_id'] = int(blog_id)
        return render(request, template_name, context)

    def post(self, request, blog_id):
        context = {}
        context_new = {}
        data_dict_form = BlogCommentForm(request.POST)
        data = request.POST
        if request.method == 'POST':
            if data_dict_form.is_valid():
                blog = Blog.objects.get(id=int(blog_id))
                comment = Comment()
                comment.blog_id = blog
                comment.description = data['description']
                comment.author = request.user
                comment.save()               
                comment_obj = render_to_string('comment.html', {'comment': comment})
                return HttpResponse(comment_obj)

def blog_listing(request):
    context = listing(request)
    return render(request, 'blog.html',context)


def listing(request):
    blogs_list = Blog.objects.all()
    paginator = Paginator(blogs_list, 5)

    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    comment_form = BlogCommentForm()
    context = {
        'blogs': blogs,
        'is_staff': request.user.is_staff,
        'blog_id': '',
        'comment_form': comment_form,
    }
    return context
