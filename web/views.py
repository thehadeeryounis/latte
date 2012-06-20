from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import *
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from smarter.views import GenericViews
from web.models import *
import taggit
from git import *

def home(request):
    return render_to_response( "base.html", context_instance = RequestContext( request ), mimetype = "text/html" )

def welcome(request):
    return render_to_response( "base.html", context_instance = RequestContext( request ), mimetype = "text/html" )
