from django.shortcuts import render
from django.http import HttpResponse
from blog_app.models import Project
# Create your views here.

def index(request):
	return render(request, 'blog_app/hello.html',{})

def project_index(request):
    projects = Project.objects.all()
    return render(request, 'blog_app/project_index.html', {'projects':projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'blog_app/project_detail.html', {'context':context})
