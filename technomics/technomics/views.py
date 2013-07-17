import os

from django.views.generic import TemplateView
from django.conf import settings


def home(request):
    
    return TemplateView.as_view(template_name='home.html')
