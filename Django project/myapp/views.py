from django.shortcuts import render
from .models import Contact, User

# Create your views here.
def index(request):
	return render(request, 'index.html') 

def contact(request):
	if request.method == "POST":
		Contact.objects.create(
			name = request.POST['name'],
			email = request.POST['email'],
			mobile = request.POST['mobile'],	
			remarks = request.POST['remarks']
			)
		msg = "Contact Saved Successfully"
		contacts = Contact.objects.all().order_by("-id")[:3]
		return render(request, 'contact.html', {'msg':msg, 'contacts':contacts} )
	else:
		contacts = Contact.objects.all().order_by("-id")[:3]
		return render(request, 'contact.html', {'contacts':contacts}) 

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
					password = request.POST['password']
					)
				msg = "User Signup Successfully"
				return render(request,  'signup.html', {'msg':msg})
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
				return render(request, 'index.html')
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
		msg = "user logged out successfully"
		return render (request, 'login.html', {'msg':msg})
	except:
		msg = "user looged out successfully"
		return render (request, 'login.html', {'msg':msg})

def change_password(request):
	if request.method == 'POST':
		user = User.objects.get(email = request.session['email'])
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
				return render (request, 'change-password.html', {'msg':msg})
		else:
			msg = "Old Password Is Incorrect"
			return render(request, 'change-password.html', {'msg':msg})
	else:
		return render(request, 'change-password.html')

def forgot_password(request):
	if request.method == 'POST':
	return render(request, 'forgot-password.html')