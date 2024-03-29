from django.shortcuts import render
from mauth.forms import UserForm, UserProfileForm, UserImageForm, ProfileUpdateForm
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .models import UserProfile

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def _login(request):
	title = "Login"
	redirect_url="/"
	if request.method == "GET":
		if request.GET.get('next') != None and len(request.GET.get('next')) != 0:
			redirect_url = request.GET['next']
			print redirect_url

	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				user.last_login=timezone.now()
				user.save()
				if not request.POST.get('remember', None):
					request.session.set_expiry(0)
				messages.info(request,'Welcome '+user.username)
				return HttpResponseRedirect(redirect_url)
			else:
				messages.info(request,'Your account is inactive, Contact webmaster.')
				return HttpResponseRedirect('/')
		else:
			messages.error(request,'Invalid Username or Password')
			return HttpResponseRedirect('/auth/login')
	return render(request, 'auth/login.html', {'title':title})

def _logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def _register(request):
	registered = False
	user_form = UserForm()
	profile_form = UserProfileForm()
	if request.method == "POST":
		password = request.POST.get('password')
	
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if len(password) < 6:
			messages.error(request, 'Password length must be greater than 6')
		elif user_form.is_valid() and profile_form.is_valid():
			user = user_form.save(commit=False)
			user.set_password(password)
			user.date_joined = timezone.now()
			user.is_active=True
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.ipAddress=get_client_ip(request)
			profile.save()
			registered = True
			messages.success(request, "Successfully Registered !!")
		else:
			messages.info(request, 'Error in form !')
	return render(request,'auth/register.html',{'title':'Sign Up', 'user_form':user_form,'profile_form':profile_form,'registered':registered})

@login_required(login_url='/auth/login')
def _changePassword(request):
	title='Change Password'
	if request.method == "POST":
		old_pass = request.POST.get('old')
		new = request.POST.get('new')
		new_confirm = request.POST.get('new_confirm')
		user = authenticate(username=request.user.username, password=old_pass)
		if new != new_confirm:
			messages.error(request, 'Password do not match !')
		elif user is not None:
			user.set_password(new)
			messages.success(request, 'Password Successfully Changed !')
			logout(request)
			return HttpResponseRedirect('/')
		else:
			messages.info(request, 'Please Enter correct password.')

	return render(request, 'auth/changePassword.html', {'title':title})

@login_required(login_url='/auth/login/')
def _upload(request):
	uploaded=False
	user_profile = UserProfile.objects.get(user=request.user)
	image_form = UserImageForm()
	if request.method == "POST":
		image_form = UserImageForm(request.POST, request.FILES)
		if(image_form.is_valid()):
			user_profile.picture = image_form.cleaned_data['picture']
			user_profile.save()
			uploaded=True
		else:
			print str(image_form.errors)
			messages.info(request, 'Image is not supported !')
	return render(request, 'auth/upload.html', {'title':'Upload Avatar','userprofile': user_profile, 'image_form':image_form, 'uploaded':uploaded})


@login_required(login_url='/auth/login')
def _profile(request):
	profile_update = ProfileUpdateForm()
	if request.method == 'POST':
		profile_update = ProfileUpdateForm(data=request.POST)
		if profile_update.is_valid():
			user = User.objects.get(username=request.user.username)
			user.first_name = profile_update.data['first_name']
			user.last_name = profile_update.data['last_name']
			user.email = profile_update.data['email']
			user.save()
			user_profile = UserProfile.objects.get(user=request.user)
			user_profile.gender = profile_update.data['gender']
			user_profile.birthdate = profile_update.data['birthdate']
			user_profile.phone = profile_update.data['phone']
			user_profile.save()
			#print requestuest.user.username, requestuest.user.password
			messages.success(request, 'profile updated Successfully')
		else:
			messages.error(request, 'form is not valid !')
			
	return render(request, 'auth/profile.html', {'title':'Profile', 'profile_update':profile_update})
