from django.shortcuts import render,redirect
from .models import Contact,User,Doctor_profile,Appointment,cancelappointment,Healthprofile


# Create your views here.
def index(request):
	return render(request,'index.html')

def doctor_home(request):
	return render(request,'doctor_index.html')

def signup(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.post['email'])
			msg="email alredy registerd"
			return render(request,'signup.html',{'msg':msg})

		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					password=request.POST['password'],
					address=request.POST['address']
			)

				msg="user signup successfully"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="password and confirm password does not mtched"
				return render(request,'signup.html',{'msg':msg})		
	else:
		return render(request,'signup.html')

	

def gallery(request):
	return render(request,'gallery.html')

def login(request):
	if request.method=="POST":
		try:

			user=User.objects.get(email=request.POST['email'],
				password=request.POST['password'])

			if user.usertype=="patient":
				request.session['email']=user.email
				request.session['fname']=user.fname
				appointments1=Appointment.objects.filter(patient=user,status="pending")
				request.session['appointment_count']=len(appointments1)				
				return render(request,'index.html')
			else:
				doctor_profile=Doctor_profile.objects.get(doctor=user)
				request.session['email']=user.email
				request.session['fname']=user.fname
				request.session['doctor_picture']=doctor_profile.doctor_picture.url
				return render(request,'doctor_index.html')
		except Exception as e:
			print(e)
			msg="email and password is incorrect"
			return render(request,'login.html',{'msg':msg})


	else:
		return render(request,'login.html')

def about(request): 
	return render(request,'about-us.html')

def contact(request):
	if request.method=="POST":
		Contact.objects.create(
				name=request.POST['name'],
				email=request.POST['email'],
				subject=request.POST['subject'],
				message=request.POST['message']
			)
		msg="contact saved successfully"
		contacts=Contact.objects.all().order_by("-id")[:5]
		return render(request,'contact.html',{'msg':msg,'contacts':contacts})

	else:
		contacts=Contact.objects.all().order_by("-id")[:5]
		return render(request,'contact.html',{'contacts':contacts})
def logout(request): 
	try:
		del request.session['email']
		del request.session['fname']	
		return render(request,'login.html')
	except:
		return render(request,'login.html')
	

def doctor_profile(request):
	doctor_profile=Doctor_profile()
	doctor=User.objects.get(email=request.session['email'])
	try:
		doctor_profile=Doctor_profile.objects.get(doctor=doctor)
	except: 
		pass
	if request.method=="POST":
		doctor=Doctor_profile.objects.create(
			doctor=doctor,
			doctor_degree=request.POST['doctor_degree'],
			doctor_speciality=request.POST['doctor_speciality'],
			doctor_starttime=request.POST['doctor_starttime'],
			doctor_endtime=request.POST['doctor_endtime'],
			doctor_fees=request.POST['doctor_fees'],
			doctor_picture=request.FILES['doctor_picture'],
		)
		msg="Doctor Profile updated successfully"
		return render(request,'doctor_profile.html',{'msg':msg,'doctor':doctor})
	else:
		return render(request,'doctor_profile.html',{'doctor_profile':doctor_profile})

def change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		
		if request.POST['old_password']==user.password:
			if request.POST['new_password']==request.POST['cnew_password']:
				user.password=request.POST['new_password']
				user.save()
				return redirect('logout') 
			else:
				msg="new password and confirm new password does not match"
				return render(request,'change_password.html',{'msg':msg})
		else:
			msg="old password  does not match"
			return render(request,'change_password.html',{'msg':msg})
	else:
		return render(request,'change_password.html')

def forgot_password(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			subject = 'OTP for forgot_password'
			otp=random.randint(1000,9999)
			message =	'Hello' +user.fname+',your OTP for fogot password is' +str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email, ] 
			send_mail( subject, message, email_from, recipient_list )
			return render(request,'otp.html',{'otp':otp,'email':user.email})		
		except Exception as e:
			print(e)
			msg="email not registered"
			return render(request,'forgot_password.html',{'msg':msg})
	else:
		return render(request,'forgot_password.html')
	return render(request,'forgot_password.html')

def verifyotp(request):
	otp=request.POST['otp']
	uotp=request.POST['uotp']
	email=request.POST['email']

	if otp==uotp:
		return render(request,'new_password.html',{'email':email})
	else:
		msg="invalid OTP"
		return render(request,'new_password.html',{'otp':otp,'email':email,'msg':msg})
	
def new_password(request):
	email=request.POST['email']
	new_password=request.POST['new_password']
	cnew_password=request.POST['cnew_password']
	print(new_password)
	print(cnew_password)
	if new_password==cnew_password:
		user=User.objects.get(email=email)
		user.password=new_password
		user.save()
		return redirect('login')
	else:
		msg="New password and confirm new password does not  matched"
		return render(request,'new_password.html',{'email':email,'msg':msg})
def edit_profile(request):
		return render(request,'edit_profile.html')

def doctors(request):
	doctors=Doctor_profile.objects.all()
	for i in doctors:
	 	print(i.id)
	return render(request,'doctors.html',{'doctors':doctors})

def doctor_detail(request,pk):
	doctor=Doctor_profile.objects.get(pk=pk)
	return render(request,'doctor_detail.html',{'doctor':doctor})

def book_appointment(request,pk):
	doctor=Doctor_profile.objects.get(pk=pk)
	patient=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		Appointment.objects.create(
				patient=patient,
				doctor=doctor,
				date=request.POST['date'],
				time=request.POST['time'],
				health_issue=request.POST['health_issue']
			)
		msg="Appointment Booked Successfully"
		appointments=Appointment.objects.filter(patient=patient)
		appointments1=Appointment.objects.filter(patient=patient,status="pending")
		request.session['appointment_count']=len(appointments1)	
		return render(request,'myappointment.html',{'msg':msg,'appointments':appointments})
	else:
		return render(request,'book_appointment.html',{'doctor':doctor,'patient':patient})	

def myappointment(request):
	patient=User.objects.get(email=request.session['email'])
	appointments=Appointment.objects.filter(patient=patient)
	appointments1=Appointment.objects.filter(patient=patient,status="pending")
	request.session['appointment_count']=len(appointments1)	
	return render(request,'myappointment.html',{'appointments':appointments})

def patient_cancel_appointment(request,pk):
	appointment=Appointment.objects.get(pk=pk)
	if request.method=="POST":
		cancelappointment.objects.create(
				appointment=appointment,
				reason=request.POST['reason']
			)
		appointment.status="cancelled by patient"
		appointment.save()
		return redirect("myappointment")
	else:
		return render(request,'patient_cancel_appointment.html',{'appointment':appointment})
   	

def health_profile(request):
	health_profile=Healthprofile()
	patient=User.objects.get(email=request.session['email'])
	try:
		health_profile=Healthprofile.objects.get(patient=patient)
	except:
		pass	
	if request.method=="POST":
		patient=User.objects.get(email=request.session['email'])
		diabetes=request.POST['diabetes']
		if diabetes=="yes":
			flag1=True
		else:
			flag1=False

		bloodpressure=request.POST['bloodpressure']
		if bloodpressure=="yes":
			flag2=True
		else:
			flag2=False
		
		health_profile=Healthprofile.objects.create(
			patient=patient,
			bloodgroup=request.POST['bloodgroup'],
			weight=request.POST['weight'],
			diabetes=flag1,
			bloodpressure=flag2,

			)
		msg="health profile update successfully"
		return render(request,'health_profile.html',{'msg':msg,'health_profile':health_profile})
	else:
		return render(request,'health_profile.html',{'health_profile':health_profile})

def doctor_appointment(request):
	doctor=User.objects.get(email=request.session['email'])
	doctor_profile=Doctor_profile.objects.get(doctor=doctor)
	doctor_appointments=Appointment.objects.filter(doctor=doctor_profile)
	return render(request,'doctor_appointment.html',{'doctor_appointments':doctor_appointments})



def doctor_approve_appointment(request,pk):
	appointment=Appointment.objects.get(pk=pk)
	appointment.status="approved"
	appointment.save()
	return redirect('doctor_appointment')

def doctor_complete_appointment(request,pk):
	appointment=Appointment.objects.get(pk=pk)
	if request.method=="POST":
		appointment.prescription=request.POST['prescription']
		appointment.status="completed"
		appointment.save()
		return redirect('doctor_appointment')

	else:	
		return render(request,'doctor_complete_appointment.html',{'appointment':appointment})
	#appointment.status="completed"
	#appointment.save()
	
def doctor_cancel_appointment(request,pk):
	appointment=Appointment.objects.get(pk=pk)
	appointment.status="cancelled by doctor"
	appointment.save()
	return redirect('doctor_appointment')
