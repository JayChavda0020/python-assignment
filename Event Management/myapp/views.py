from django.shortcuts import render
from .models import Contact, User
from django.conf import settings
from django.core.mail import send_mail
import random
# Create your views here.
def index(request):
	try:
		user = User.objects.get(email = request.session['email'])
		if user.usertype == "user":
			return render(request, 'index.html')
		else:
			return render(request, 'manager-index.html')
	except:
		return render (request, 'index.html')

def contact(request):
	if request.method == "POST":
		Contact.objects.create(
			name = request.POST['name'],
			email = request.POST['email'],
			mobile = request.POST['mobile'],	
			message = request.POST['message']
			
			)
		msg = "Contact Saved Successfully"
		return render(request, 'contact.html', {'msg':msg})
	else:
		return render(request, 'contact.html',)

def about(request):
	return render (request, 'about.html')

def speakers(request):
	return render (request, 'speakers.html')

def schedule(request):
	return render (request, 'schedule.html')

def blog(request):
	return render (request, 'blog.html')

def signup(request):
	if request.method == "POST":
		try:
			User.objects.get(email = request.POST['email'])
			msg = "Email Already Registered"
			return render(request,  'signup.html', {'msg':msg})
		except:
			if request.POST['password'] == request.POST['cpassword']:
				User.objects.create(
					fname = request.POST['fname'],
					lname = request.POST['lname'],
					email = request.POST['email'],
					mobile = request.POST['mobile'],
					password = request.POST['password'],
					usertype = request.POST['usertype']
					)
				msg = "User Signup Successfully"
				return render(request,  'login.html', {'msg':msg})
			else:
				msg = "Password Does Not Match"
				return render(request,  'signup.html', {'msg':msg})
	else:
		return render(request, 'signup.html')

def login(request):
	if request.method == "POST":
		try:
			user = User.objects.get(email = request.POST['email'])
			if user.password == request.POST['password']:
				request.session['email'] = user.email
				request.session['fname'] = user.fname
				request.session['profile_picture'] = user.profile_picture.url
				if user.usertype == "user":
					return render(request, 'index.html')
				else:
					return render(request, 'manager-index.html')
			else:
				msg = "Incorrect password"
				return render(request, 'login.html', {'msg':msg})
		except:
			msg = "Email Not Registered"
			return render(request, 'login.html', {'msg':msg})
	else:
		return render(request, 'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		del request.session['profile_picture']
		msg = "User Logged Out Successfully"
		return render(request, 'login.html', {'msg':msg})
	except:
		msg = "User Logged Out Successfully"
		return render(request, 'login.html', {'msg':msg})

def change_password(request):
	user = User.objects.get(email = request.session['email'])
	if request.method == 'POST':
		if user.password == request.POST['old_password']:
			if request.POST['new_password'] == request.POST['cnew_password']:
				user.password = request.POST['new_password']
				user.save()
				msg = "Password Changed Successfully"
				del request.session['email']
				del request.session['fname']
				return render(request, 'login.html', {'msg':msg})
			else:
				msg = "New Passwords Does Not Match"
				if user.usertype == "user":
					return render(request, 'change-password.html', {'msg':msg})
				else:
					return render(request, 'manager-change-password.html', {'msg':msg})

		else:
			msg = "Old Password Is Incoorect"
			if user.usertype == "user":
				return render(request, 'change-password.html', {'msg':msg})
			else:
				return render(request, 'manager-change-password.html', {'msg':msg})
	else:
		if user.usertype == "user":
			return render(request, 'change-password.html')
		else:
			return render(request, 'manager-change-password.html')

def forgot_password(request):
	if request.method == 'POST':
		try:
			user = User.objects.get(email=request.POST['email'])
			otp = random.randint(1000,9999)
			subject = 'OTP For Forgot Password'
			message = 'Hello ' + user.fname + ' ,Your OTP Is ' + str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email, ]
			send_mail( subject, message, email_from, recipient_list )
			return render(request, 'otp.html', {'email':user.email, 'otp':otp})
		except:
			msg = "Email Is Not Registered"
			return render(request, 'forgot-password.html', {'msg':msg})
	else:
		return render(request, 'forgot-password.html')

def verify_otp(request):
	email = request.POST['email']
	otp = int(request.POST['otp'])
	uotp = int(request.POST['uotp'])

	if otp == uotp:
		return render(request, 'new-password.html', {'email':email})
	else:
		msg = "Invalid OTP"
		return render(request, 'otp.html', {'email':email, 'otp':otp, 'msg':msg})

def new_password(request):
	email = request.POST['email']
	np = request.POST['new_password']
	cnp = request.POST['cnew_password']

	if np == cnp:
		user = User.objects.get(email=email)
		user.password = np 
		user.save()
		msg = "Password Updated Successfully"
		return render(request, 'login.html', {'msg':msg})
	else:
		msg = "Passwords Does Not Match"
		return render(request, 'new-password.html', {'email':email, 'msg':msg})

def profile(request):
	user = User.objects.get(email = request.session['email'])
	if request.method == "POST":
		user.fname = request.POST['fname']
		user.lname = request.POST['lname']
		user.mobile = request.POST['mobile']
		try:
			user.profile_picture = request.FILES['profile_picture']
		except:
			pass
		user.save()
		request.session['profile_picture'] = user.profile_picture.url
		request.session['fname'] = user.fname
		msg = "Profile Updated Successfully"
		if user.usertype == "user":
			return render(request, 'profile.html', {'user':user, 'msg':msg})
		else:
			return render(request, 'manager-profile.html', {'user':user, 'msg':msg})
	else:
		if user.usertype == "user":
			return render(request, 'profile.html', {'user':user})
		else:
			return render(request, 'manager-profile.html', {'user':user})

def manager_add_event(request):
	return render(request, 'manager-add-event.html')