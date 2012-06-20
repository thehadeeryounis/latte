from django.conf.urls import patterns, include, url
from django.contrib import admin
from smarter import SmarterSite
from web.models import *
from web.views import *

admin.autodiscover()
site = SmarterSite()
site.register(MyCustomModel)

urlpatterns = patterns('',
    url(r'^', include(site.urls)),
    url(r'^$', 'web.views.home', name="home"),
    url(r'^welcome/$', 'web.views.welcome', name="welcome"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('social_auth.urls')),
    url(r'^messages/', include('accounts.contrib.umessages.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
 )
