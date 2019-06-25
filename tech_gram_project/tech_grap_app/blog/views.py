from django.shortcuts import render, get_object_or_404
from blog.models import Blog

def blog_home(request):
	blogs = Blog.objects.all()
	return render(request, "blog/all_blog.html" , {'blogs':blogs})

def one_blog_detail(request, blog_id):
	blog_detail = get_object_or_404(Blog,pk=blog_id)
	return render(request, "blog/blog_detail.html",{"blog_detail":blog_detail})
