from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from accounts import views as accounts_views
from accounts import settings as accounts_settings

urlpatterns = patterns('',
    # Signup, signin and signout
    url(r'^register/$',
       accounts_views.signup,
       name='accounts_register'),
    url(r'^login/$',
       accounts_views.signin,
       name='accounts_login'),
    url(r'^logout/$',
       auth_views.logout,
       {'next_page': accounts_settings.ACCOUNTS_REDIRECT_ON_SIGNOUT,
        'template_name': 'accounts/signout.html'},
       name='accounts_logout'),

    # Reset password
    url(r'^password/reset/$',
       auth_views.password_reset,
       {'template_name': 'accounts/password_reset_form.html',
        'email_template_name': 'accounts/emails/password_reset_message.txt'},
       name='accounts_password_reset'),
    url(r'^password/reset/done/$',
       auth_views.password_reset_done,
       {'template_name': 'accounts/password_reset_done.html'},
       name='accounts_password_reset_done'),
    url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
       auth_views.password_reset_confirm,
       {'template_name': 'accounts/password_reset_confirm_form.html'},
       name='accounts_password_reset_confirm'),
    url(r'^password/reset/confirm/complete/$',
       auth_views.password_reset_complete,
       {'template_name': 'accounts/password_reset_complete.html'}),

    # Signup
    url(r'^(?P<username>[\.\w]+)/signup/complete/$',
       accounts_views.direct_to_user_template,
       {'template_name': 'accounts/signup_complete.html',
        'extra_context': {'accounts_activation_required': accounts_settings.ACCOUNTS_ACTIVATION_REQUIRED,
                          'accounts_activation_days': accounts_settings.ACCOUNTS_ACTIVATION_DAYS}},
       name='accounts_signup_complete'),

    # Activate
    url(r'^(?P<username>[\.\w]+)/activate/(?P<activation_key>\w+)/$',
       accounts_views.activate,
       name='accounts_activate'),

    # Change email and confirm it
    url(r'^(?P<username>[\.\w]+)/email/$',
       accounts_views.email_change,
       name='accounts_email_change'),
    url(r'^(?P<username>[\.\w]+)/email/complete/$',
       accounts_views.direct_to_user_template,
       {'template_name': 'accounts/email_change_complete.html'},
       name='accounts_email_change_complete'),
    url(r'^(?P<username>[\.\w]+)/confirm-email/complete/$',
       accounts_views.direct_to_user_template,
       {'template_name': 'accounts/email_confirm_complete.html'},
       name='accounts_email_confirm_complete'),
    url(r'^(?P<username>[\.\w]+)/confirm-email/(?P<confirmation_key>\w+)/$',
       accounts_views.email_confirm,
       name='accounts_email_confirm'),

    # Disabled account
    url(r'^(?P<username>[\.\w]+)/disabled/$',
       accounts_views.direct_to_user_template,
       {'template_name': 'accounts/disabled.html'},
       name='accounts_disabled'),

    # Change password
    url(r'^(?P<username>[\.\w]+)/password/$',
       accounts_views.password_change,
       name='accounts_password_change'),
    url(r'^(?P<username>[\.\w]+)/password/complete/$',
       accounts_views.direct_to_user_template,
       {'template_name': 'accounts/password_complete.html'},
       name='accounts_password_change_complete'),

    # Edit profile
    url(r'^(?P<username>[\.\w]+)/edit/$',
       accounts_views.profile_edit,
       name='accounts_profile_edit'),

    # View profiles
    url(r'^(?P<username>(?!signout|signup|signin)[\.\w]+)/$',
       accounts_views.profile_detail,
       name='accounts_profile_detail'),
    url(r'^page/(?P<page>[0-9]+)/$',
       accounts_views.profile_list,
       name='accounts_profile_list_paginated'),
    url(r'^$',
       accounts_views.profile_list,
       name='accounts_profile_list'),
)
