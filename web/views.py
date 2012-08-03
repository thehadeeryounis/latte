from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import *
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User, UserManager
from actstream.actions import follow, unfollow

def home(request):
    return render_to_response( "base.html", context_instance = RequestContext( request ), mimetype = "text/html" )

def welcome(request):
    follow(request.user, User.objects.get(username='admin'), actor_only=False)
    return render_to_response( "base.html", context_instance = RequestContext( request ), mimetype = "text/html" )
