from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from technomics import views

admin.autodiscover()


urlpatterns = patterns('',
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.home, name="home"),
    url(r'^contactus$',views.contact_us),
    url(r'^(?P<slug>[-\w]+)/$', views.renderpage, name = "render_page"),
    url(r'^contact_notification$', TemplateView.as_view(template_name='contactus_notification.html')),
	url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
   url(r'^static1/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.GENERATED_MEDIA_ROOT, 'show_indexes': True}),
)
