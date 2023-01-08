from django import forms
from testapp.models import Employee
class EmployeeForm(forms.ModelForm):
	#form validation
	def clean_esalary(self):
		input_salary = self.cleaned_data['esalary']
		if input_salary<10000:
			raise forms.ValidationError('The minimum salary should be 10000')
		return input_salary	

	class Meta:
		model = Employee
		fields = '__all__'
    