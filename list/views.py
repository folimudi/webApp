from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
	template = loader.get_template('index.html')
	context = {'site' : 'index'}
	return HttpResponse(template.render(context, request));

def list(request):
	context = {'site': 'list'}
	return render(request,'list.html',context);

def admin(request):
	context = {'site': 'admin'}
	return render(request,'admin.html',context);
