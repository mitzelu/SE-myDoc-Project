from django.contrib.auth.models import (BaseUserManager)
from django.db import models 

class PatientManager(BaseUserManager):
	"PatientManager class"
	def create_patient(self, name, password=None):
		"method for careting new users with the role Patient in the System"
		user = self.model(name=name)

		user.set_password(password)
		user.save(using=self._db)

		return user


class DoctorManager(BaseUserManager):
	"DoctorManager class"
	def create_patient(self, name, password=None):
		"method for careting new users with the role Doctor in the System"
		user = self.model(name=name)

		user.set_password(password)
		user.save(using=self._db)

		return user
	
		
