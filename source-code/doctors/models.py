import datetime

from django.db import models
from django.contrib.auth.models import (AbstractBaseUser)
from django.utils import timezone
from doctors.managers import *

class Specialization(models.Model):
	"Specialization model stores the data about the types of specialization"
	type = models.CharField(max_length=30)

	def __str__(self):
		"specified which field of the table will be seen in the admin page"
		return self.type

class Hospital(models.Model):
	"Stores data about each Hospital such that every one of them has an addres, zip_code and name"
	zip_code = models.CharField(max_length=7)
	address  = models.CharField(max_length=50)
	name     = models.CharField(max_length=30)

	def __str__(self):
		return self.zip_code

class Doctor(AbstractBaseUser):
	"Stores the data about each Doctor. Each doctor is defined by name, rating, speciality, zip_code, photo, gender and education. The field password is automatically added from the DoctorManager class"
	name = models.CharField(max_length=50)
	specialization = models.ForeignKey(Specialization)
	#avaiable_date = models.DateTimeField('date free')
	zip_code = models.ForeignKey(Hospital)
	photo = models.ImageField(default = 'image')
	rating = models.CharField(max_length=50)
	gender = models.CharField(max_length=10)
	education = models.TextField(default = 'education')

	objects = DoctorManager()

	def get_name(self):
		return self.name


	def __str__(self):
		return self.name
		

class Patient(AbstractBaseUser):
	"Stores the data about each Patient. Each doctor is defined by name, surname, insurance number, date of birth, email. The field password is automatically added from the DoctorManager class"
	name = models.CharField(max_length=100)
	date_of_birth = models.CharField(max_length=25)
	#symptoms = models.TextField()

	objects = PatientManager()

	def get_name(self):
		return self.name

	def __str__(self):
		return self.name


class Appointment(models.Model):
	"Stores the data about each Appointment. Each Appointment has the filds: patient which created the appointment, doctor at whom, date of creation and validation status"
	patient = models.ForeignKey(Patient)
	doctor = models.ForeignKey(Doctor)
	date   = models.DateTimeField('created at:', default=timezone.now())
	validate = models.BooleanField(default=False)

	def __str__(self):           
		buffer = "date: " + str(self.date)
		return str(buffer)
		