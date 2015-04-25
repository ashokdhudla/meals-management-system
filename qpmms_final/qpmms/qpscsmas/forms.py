from django import forms
from django.forms import ModelForm,PasswordInput
from models import *
		
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = qpusers
		fields = '__all__'
class RoleForm(forms.ModelForm):
    class Meta:
        model = role
        fields = '__all__'
class associative_companyForm(forms.ModelForm):
	class Meta:
		model = associative_company
		fields = '__all__'
# class QpadminForm(forms.ModelForm):
# 	class Meta:
# 		model = Qpadmin
# 		fields = '__all__'
class employee_detailsForm(forms.ModelForm):
	class Meta:
		model = employee_details
		fields = '__all__'
class meal_timingForm(forms.ModelForm):
	class Meta:
		model = meal_timing
		fields = '__all__'
class device_infoForm(forms.ModelForm):
	class Meta:
		model = device_info
		fields = '__all__'
class qpusersForm(forms.ModelForm):
	class Meta:
		model = qpusers
		fields = '__all__'

class emp_accommodationForm(forms.ModelForm):
 class Meta:
  model = emp_accommodation
  fields = '__all__'

class emp_detailaccomodationForm(forms.ModelForm):
 class Meta:
  model = emp_accommodation
  fields = '__all__'