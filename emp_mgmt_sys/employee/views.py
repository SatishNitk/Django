from django.shortcuts import render, get_object_or_404
from employee.forms import UserForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from emp_mgmt_sys.decorator import *
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView

# Create your views here.

@login_required(login_url='/login')
def employee_list(request):
	context = {}
	print(request.role)
	context['users'] = User.objects.all()
	context['title'] = 'Employee'
	return render(request, "employee/index.html", context)

@login_required(login_url='/login')
@admin_only  # this is decorator defind in decorator .py file  this method will be executed by only admin now due to decorator 
def employee_add(request):
	context = {}
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			user_form.save()
			return HttpResponseRedirect(reverse('employee_list'))
		else:
			return render(request, "employee/add.html", {"user_form": user_form})
	else:
		user_form = UserForm()
		context['user_form'] = user_form
		return render(request, 'employee/add.html', context)



@login_required(login_url='/login')
def employee_delete(request, id=None):
	user = get_object_or_404(User, id=id)
	if request.method == 'POST':
		print(type(user))
		print("coming....................................")
		user.delete()
		return HttpResponseRedirect(reverse('employee_list'))
	else:
		context = {}
		context['user'] = user
		return render(request, 'employee/delete.html', context)		

@login_required(login_url='/login')
def employee_edit(request, id=None):
	context = {}
	user1 = get_object_or_404(User, id=id)
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance = user1)
		if user_form.is_valid():
			user_form.save()
			return HttpResponseRedirect(reverse('employee_list'))
		else:
			return render(request, "employee/edit.html", {"user_form": user_form})
	else:
		user_form = UserForm(instance=user1)
		context['user_form'] = user_form
		return render(request, 'employee/edit.html', context)		

@login_required(login_url='/login')
def employee_detail(request, id=None):
    context = {}
    context['user'] = get_object_or_404(User, id=id)
    return render(request, 'employee/details.html', context)


def user_login(request):
	context = {}
	if request.method == 'POST':
		username = request.POST['username']
		password =  request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user:
			login(request,user)
			if request.GET.get('next',None):
				return HttpResponseRedirect(request.GET['next']) # check the url how it change if u try to visit without login... from there i am getting next
			return HttpResponseRedirect(reverse("user_success"))
		else:
			context['error'] = "provide valid credentials!!"	
			return render(request, "auth/login.html",context)
	else:
		return render(request,"auth/login.html", context)		

def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('user_login'))

@login_required(login_url='/login')
def success(request):
	context = {}
	context['user'] = request.user
	return render(request, "auth/success.html",context)


class ProfileUpdate(UpdateView):
    fields = ['designation', 'salary']
    template_name = 'auth/profile_update.html'
    success_url = reverse_lazy('my_profile')  # check the difference between reverse and reverse_lazy

    def get_object(self):
        return self.request.user.profile  # it automatically return form  ... google it for more



class MyProfile(DetailView):
    template_name = 'auth/profile.html'

    def get_object(self):
        return self.request.user.profile  #if it is a single object then it will return objects  for multiple it will return queryset... google it