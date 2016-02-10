from django import forms

class SearchDoc(forms.Form):
	"SearchDoc Class represents a form which allows user to fill it with desired doctor's specialization and zip_code. The form uses GET method and returns a list of Doctor objects from database results that fulfill the required search criteria"
	specialization = forms.CharField(max_length=20)
	zip_code  = forms.CharField(max_length=20)


class BookDoc(forms.Form):
	"SearchDoc Class represents a form which allows user to fill it with required details about reservation. The form uses POST method and save the introduced data as a new Appointment Object in database"
	lastName  = forms.CharField(max_length=50)
	phone     = forms.CharField(max_length=50)
	email     = forms.CharField(max_length=50)
