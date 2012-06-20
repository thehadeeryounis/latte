from django import template
from taggit.models import *
from django.core.urlresolvers import reverse
from web.models import *
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag
def all_tags():
	return fix(Tag.objects.all())

@register.simple_tag
def all_users():
	return fix(User.objects.all())

@register.filter
def fix(obj):
	csv = ''
	for el in obj:
		try:
			csv += '"'+el.name+'",'
		except:
			csv += '"'+el.username+'",'
	return csv

@register.filter
def split(obj, str):
	data = obj.split("-")
	if data[0].capitalize() == str.capitalize():
		return data[1].capitalize()
	else:
		return ''

@register.filter
def as_tags(obj):
	csv = ''
	for el in obj:
		csv += '<a class="btn btn-small btn-info" href="'+el.slug+'"/><i class="icon-tag icon-white"></i>'+el.name+"</a>"
	return csv

@register.filter
def index(value):
	return reverse(value.__class__.__name__.lower()+"-index")

@register.filter
def model(value):
	value.__class__.__name__


@register.filter
def get_range( value ):
  return range( value )

@register.inclusion_tag('helpers/lang.html',takes_context=True)
def draw_lang(context):
	return context

@register.inclusion_tag('helpers/nav.html',takes_context=True)
def draw_nav(context):
	return context

@register.inclusion_tag('helpers/project-nav.html',takes_context=True)
def draw_projects(context):
	context['projects'] = Project.objects.filter(owner = context['user'].id)
	return context

@register.inclusion_tag('backlog/issue.html')
def draw_issue(issue):
	return {'issue' : issue}

@register.inclusion_tag('backlog/user.html',takes_context=True)
def draw_user_row(context):
	return context

@register.inclusion_tag('backlog/columns.html')
def draw_columns(project, header):
	return {'project': project, 'tags' : project.tags.filter(name__startswith="status"), 'header':header}

@register.filter
def issues(project, tag):
	issues = Issue.objects.filter(project = project, tags = tag)
	print tag
	print project
	print issues
	return issues