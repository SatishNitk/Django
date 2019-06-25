from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from products.models import Product

# Create your views here.

def account_home_page(request):
	return render(request, 'products/home.html')

def account_home_page(request):
	product = Product.objects.all()
	return render(request, 'products/home.html',{'products':product})


def account_login_page(request):
	if request.method == 'POST':
		user = auth.authenticate(username = request.POST['username'], password= request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('account_home')
		else:
			return render(request, 'accounts/login.html', {'error':'usrname or password is incorrect'})

	else:
		return render(request, "accounts/login.html")
	
def account_logout_page(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('account_home')
	return render(request, "accounts/logout.html")

def account_signup_page(request):
	if request.method == 'POST':
		if request.POST['password'] == request.POST['confirm_password']:
			try:
				User.objects.get(username=request.POST['username'])  # id user not exists it will raise exception
				return render(request,'accounts/signup.html', {'error':'user already exists'})
			except User.DoesNotExist:
				user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
				auth.login(request, user)
				return redirect('account_home')
		else:
			return render(request,'accounts/signup.html', {'error' : 'password does not match'})	

	else:
		return render(request, "accounts/signup.html")
