from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	return render(request,'home.html')

def home(request):
	return render(request,'home.html')

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	a = int(a)
	b = int(b)
	return HttpResponse(str(a+b))
