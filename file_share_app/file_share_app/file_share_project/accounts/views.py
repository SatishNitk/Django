from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.forms import StudentForm
from accounts.models import *
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



def upload_view(request):
	if request.method == 'POST':
		if request.POST.get('title') and request.POST.get('author') and request.POST.get('file'):
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

def book_list_view(request):
    books = Filedb.objects.all()
    return render(request, 'accounts/book_list.html', {
        'books': books
    })

def book_list_view_by_other(request):
    books = Filedb.objects.exclude(user = request.user)
    return render(request, 'accounts/book_list.html', {
        'books': books
    })

def book_list_view_by_u(request):
    books = Filedb.objects.filter(user = request.user)
    return render(request, 'accounts/book_list.html', {
        'books': books
    })



def delete_view(request, pk):
	if request.method == 'POST':
		book = Filedb.objects.get(pk=pk)
		book.delete()
		return redirect('book_list_view')
