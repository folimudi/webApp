from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
	template = loader.get_template('base.html')
	return HttpResponse(template.render(context, request));

def list(request):
	return HttpResponse(template.render(context, request))

def admin(request):
	return HttpResponse();
