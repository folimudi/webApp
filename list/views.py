from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from list.models import Brother, Guest
from rest_framework import generics
from list.serializers import BrotherSerializer, GuestSerializer

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

#API views

class BrothersList(generics.ListCreateAPIView):
	"""docstring for BrothersList."""
	queryset = Brother.objects.all()
	serializer_class = BrotherSerializer

class BrotherDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Brother.objects.all()
	serializer_class = BrotherSerializer

class GuestList(generics.ListCreateAPIView):
	queryset = Guest.objects.all()
	serializer_class = GuestSerializer

class GuestDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Guest.objects.all()
	serializer_class = GuestSerializer
