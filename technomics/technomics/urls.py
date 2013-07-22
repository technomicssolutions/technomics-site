from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name="home"),
    url(r'^services$', TemplateView.as_view(template_name='services.html'), name="services"),
    # url(r'^technomics/', include('technomics.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
   url(r'^static1/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.GENERATED_MEDIA_ROOT, 'show_indexes': True}),
)
