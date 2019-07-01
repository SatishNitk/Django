from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.forms import StudentForm
from accounts.models import *
from django.contrib.auth.decorators import login_required
from accounts.models import Filedb
import requests 
import os


import io
from django.http import FileResponse
from reportlab.pdfgen import canvas



# Create your views here.

def home_view(request):
	return render(request, 'accounts/home.html')


def login_view(request):
	if request.method == 'POST':
		user = auth.authenticate(username = request.POST['username'], password= request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('book_list_view')
		else:
			return render(request, 'accounts/login.html', {'error':'usrname or password is incorrect'})

	else:

		return render(request, "accounts/login.html")


def signup_view(request):
	if request.method == 'POST':
		if request.POST['password'] == request.POST['confirm_password']:
			try:
				User.objects.get(username=request.POST['username'])  # id user not exists it will raise exception
				return render(request,'accounts/signup.html', {'error':'user already exists'})
			except User.DoesNotExist:
				user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
				auth.login(request, user)
				return redirect('book_list_view')
		else:
			return render(request,'accounts/signup.html', {'error' : 'password does not match'})	

	else:
		return render(request, "accounts/signup.html")

def logout_view(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home_view')


@login_required(login_url='/login')
def upload_view(request):
	if request.method == 'POST':
		if request.POST.get('title') and request.POST.get('author') and len(request.FILES)!=0:
			user_form = StudentForm(request.POST, request.FILES)
			if user_form.is_valid():
				user_form_instance = user_form.save(commit=False)
				user_form_instance.user = request.user
				user_form_instance.save()
				form = StudentForm()
				msg1 = {
				"form":form,
				"msg":"file upload successfully",}
				return render(request, 'accounts/upload.html',msg1)  
		else:
			form = StudentForm()
			msg1 = {
			    "form":form,
				"msg":"please fill the title and author and file   are mendetory",}
			return render(request,"accounts/upload.html",msg1)
	else:
		form = StudentForm()
		return render(request,"accounts/upload.html",{"form":form})

# def demo_view(request):
# 	context1 = Filedb.objects.filter(user=request.user)
# 	context = {
# 	'context' : context1
# 	}
# 	return render(request, "accounts/login_success.html",context)
@login_required(login_url='/login')
def book_list_view(request):
    books = Filedb.objects.all()
    return render(request, 'accounts/book_list.html', {
        'books': books
    })

@login_required(login_url='/login')
def book_list_view_by_other(request):
    books = Filedb.objects.exclude(user = request.user)
    return render(request, 'accounts/book_list.html', {
        'books': books
    })

@login_required(login_url='/login')
def book_list_view_by_u(request):
    books = Filedb.objects.filter(user = request.user)
    return render(request, 'accounts/book_list.html', {
        'books': books
    })


@login_required(login_url='/login')
def delete_view(request, pk):
	if request.method == 'POST':
		book = Filedb.objects.get(pk=pk)
		book.delete()
		return redirect('book_list_view')

def pdfdownloader_view(request, file_name):
	print("file",file_name)
	# response = HttpResponse(content_type='application/pdf')
	# response['content_type'] = 'application/pdf'
	# response['Content-Disposition'] = 'attachment;filename={}'.format(file_name)
	# path = "/home/satish/satish_education/django/file_share_app/file_share_app/file_share_project/media/books/pdfs/" + file_name
	# print(path)
	# with open(path, 'rb') as pdf:
	# 	response = HttpResponse(pdf.read())
	# 	response['content_type'] = 'application/pdf'
	# 	response['Content-Disposition'] = 'attachment;filename={}'.format(file_name)
	# 	return response
	return HttpResponse("kjh")

def mp3downloader_view(request):
    fname='/home/satish/ime/mp3_folder/j.mp3'
    f = open(fname,"rb") 
    response = HttpResponse()
    response.write(f.read())
    response['Content-Type'] ='audio/mpeg'
    response['Content-Length'] =os.path.getsize(fname)
    response['Content-Disposition'] = 'attachment; filename=filename.mp3'
    return response


def mp4downloader_view(request):
    fname='/home/satish/Desktop/sa.mp4'
    f = open(fname,"rb") 
    response = HttpResponse()
    response.write(f.read())
    response['Content-Type'] ='video/mp4'
    response['Content-Length'] =os.path.getsize(fname)
    response['Content-Disposition'] = 'attachment; filename=filename.mp4'
    return response



def my_image(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="WishList.pdf"'
	buffer = io.BytesIO()
	p = canvas.Canvas(buffer)
	p.drawString(100, 100, "Helldddddo world.")
	p.showPage()
	p.save()
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response
