from django.db import models
from django.utils import timezone
# Create your models here.
class Contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	message=models.TextField()
	subject=models.CharField(max_length=100)

	def __str__(self):
		return self.name
class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	address=models.TextField()
	password=models.CharField(max_length=100)
	usertype=models.CharField(max_length=100,default="patient")

	def __str__(self):
		return self.fname +" - "+ self.lname

class Doctor_profile(models.Model):
	doctor=models.ForeignKey(User,on_delete=models.CASCADE)
	doctor_degree=models.CharField(max_length=100)
	doctor_speciality=models.CharField(max_length=100)
	doctor_starttime=models.CharField(max_length=100)
	doctor_endtime=models.CharField(max_length=100)
	doctor_fees=models.PositiveIntegerField()
	doctor_picture=models.ImageField(upload_to="doctor_picture/")

	def __str__(self):
		return self.doctor.fname+" - "+ self.doctor_degree




class Appointment(models.Model):
	patient=models.ForeignKey(User,on_delete=models.CASCADE,related_name="patient")
	doctor=models.ForeignKey(Doctor_profile,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)
	time=models.CharField(max_length=100)
	health_issue=models.TextField()
	status=models.CharField(max_length=100,default="pending")
	prescription=models.TextField(default="not given yet")

	def __str__(self):
		return self.patient.fname

class cancelappointment(models.Model):
	appointment=models.ForeignKey(Appointment,on_delete=models.CASCADE)
	reason=models.CharField(max_length=100)

	def __str__(self):
		return self.appointment.patient.fname+" = "+self.appointment.doctor.doctor.fname

class Healthprofile(models.Model):
	patient=models.ForeignKey(User,on_delete=models.CASCADE)
	bloodgroup=models.CharField(max_length=100)
	weight=models.CharField(max_length=100)
	diabetes=models.BooleanField(default=False)
	bloodpressure=models.BooleanField(default=False)

	def __str__(self):
		return self.patient.fname