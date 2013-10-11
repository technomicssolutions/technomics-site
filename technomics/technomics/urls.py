from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from technomics import views

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^static1/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.GENERATED_MEDIA_ROOT, 'show_indexes': True}),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.home, name="home"),
    url(r'^contactus$',views.contact_us),
    url(r'^careers/freshers/apply/$',views.freshers_detail, name = "freshers_apply"),
    url(r'^careers/experienced/apply/(?P<vacancy_id>[-\w]+)/$',views.CareersView.as_view(), name = "experienced_apply"),
#    url(r'^add_blog$', views.add_blog),
    url(r'^(?P<menuslug>[-\w]+)/$', views.rendermenu, name = "render_menupage"),
    url(r'^(?P<menu_slug>[-\w]+)/(?P<submenuslug>[-\w]+)/$', views.rendersubmenu, name = "render_submenupage"),
    url(r'^contact_notification/$', TemplateView.as_view(template_name='contactus_notification.html')),
	url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^static1/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.GENERATED_MEDIA_ROOT, 'show_indexes': True}),
)
