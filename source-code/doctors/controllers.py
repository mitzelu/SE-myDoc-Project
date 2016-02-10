from django.shortcuts import get_object_or_404
from doctors.dao import *

class PatientController(object):
	"PatientController class deals with implementing the methods specified in PatientDAO class"

	__patientDAO__ = PatientDAO()
	__appointmnentDAO__ = AppointmentDAO()
	__patient__ = object()

	def createAppointment(self, doctor, date, patient):
		self.__appointmnentDAO__.create(null, patient, doctor, date, False)
		return 


class SpecializationController(object):
	"SpecializationController class deals with implementing the methods specified in SpecializationDAO class"
	__specializationDAO__ = SpecializationDAO()

	def getAll(self):
		"method that retrieves all specializations types from database "
		return self.__specializationDAO__.getAll()

	def getById(self, ID):
		"method that retrieves specializations types from database by specified ID"
		return self.__specializationDAO__.getById(ID)

class HospitalController(object):
	"HospitalController class deals with implementing the methods specified in HospitalDAO class"
	__hospitalDAO__ = HospitalDAO()

	def getAll(self):
		"method that retrieves all Hospital objects from database "
		return self.__hospitalDAO__.getAll()

	def getById(self, ID):
		"method that retrieves Hospital objects from database by specified ID"
		return self.__hospitalDAO__.getById(ID)
		
		
class DoctorController(object):
	"DoctorController class deals with implementing the methods specified in DoctorDAO class"
	__doctorDAO__ = DoctorDAO()
	__specializationDAO__ = SpecializationDAO()

	def getById(self, doc_id):
		"method that retrieves  Doctor objects from database by specified ID"
		return self.__doctorDAO__.getById(doc_id)

	def getBySpecHospId(self, spec_id, hosp_id):
		"method that retrieves  Doctor objects from database by specified specialization ID and Hospital ID"
		return self.__doctorDAO__.getByCriteria(SpecializationController().getById(spec_id), HospitalController().getById(hosp_id)) 
		

class AppointmentController(object):
	"AppointmentController class deals with implementing the methods specified in AppointmentDAO class"
	__appointmentDAO__ = AppointmentDAO()

	def getTakenDays(self, doctor, date):
		return self.__appointmentDAO__.getTakenDays(doctor, date)
	
	
		
