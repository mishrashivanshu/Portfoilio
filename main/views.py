from django.shortcuts import render
from django.conf import settings
# Create your views here.
def index(request):
    context={}
    return render(request,'main/index.html',context)

def projects(request):
    context={}
    return render(request,'main/projects.html',context)

def skills(request):
    context={}
    return render(request,'main/skills.html',context)

def contact(request):
    context={}
    return render(request,'main/contact.html')

def education(request):
    context={}
    return render(request,'main/education.html')

def achievements(request):
    context={}
    return render(request,'main/achievements.html')
