from django.shortcuts import render
from app.models import *

def index(request):
    cour =  Courses.objects.all()
    context = {'cour':cour}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')  

def contact(request):
    return render(request, 'contact.html')  

def courses(request):
    return render(request, 'courses.html')         
