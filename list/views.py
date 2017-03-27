from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
	template = loader.get_template('base.html')
	context = {site : 'site'}
	return HttpResponse(template.render(context, request));

def list(request):
	context = {site: 'list'}
	render(request,'list.html',context);

def admin(request):
	context = {site: 'admin'}
	render(request,'admin.html',context);
