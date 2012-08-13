from django.conf.urls import patterns, include, url
from django.contrib import admin
from smarter import SmarterSite
from web.models import *
from web.views import *

admin.autodiscover()
site = SmarterSite()
site.register(Item)

urlpatterns = patterns('',
    url(r'^', include(site.urls)),
    url(r'^$', 'web.views.home', name="home"),
    url(r'^welcome/$', 'web.views.welcome', name="welcome"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('social_auth.urls')),
    url(r'^accounts/', include('userprofiles.urls')),
    url(r'^accounts/profile/(?P<username>[-\w]+)/$', 'web.views.profile', name="public_profile"),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^activity/', include('actstream.urls')),
    url(r'^messages/', include('django_messages.urls'))
 )
