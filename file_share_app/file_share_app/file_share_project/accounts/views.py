from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.forms import StudentForm
# Create your views here.

def home_view(request):
	return render(request, 'accounts/home.html')


def login_view(request):
	if request.method == 'POST':
		user = auth.authenticate(username = request.POST['username'], password= request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('upload_view')
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
				return redirect('home_view')
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
		if request.POST.get('title') and request.POST.get('description'):
			user_form = StudentForm(request.POST, request.FILES)
			if user_form.is_valid():
				user_form_instance = user_form.save(commit=False)
				user_form_instance.user = request.user
				user_form_instance.save()
				return render(request, 'accounts/main_home.html',{"msg": "File uploaded successfully"})  
			else:
				print("djhdh")
		else:
			return render(request,"accounts/main_home.html",{"msg":"please fill the title and file both are mendetory"})
	else:
		form = StudentForm()
		return render(request,"accounts/main_home.html",{"form":form})

