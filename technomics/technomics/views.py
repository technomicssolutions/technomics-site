import os

from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.db import models

from models import Contactus, Dates, Homepage, Feature, Newsevents, Aboutus, Blog, Comment, Slideshow, Services, Services_section, Testimonials

# def home(request):
    
#     return TemplateView.as_view(template_name='home.html')

class Homepage_view():




