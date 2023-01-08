from rest_framework import serializers
from testapp.models import Employee

# By using Validators(User defined)
def multiple_of_1000(value):
	if value%1000!=0:
		raise serializers.ValidationError('Employee salary should be multiple of 1000')

#MODEL SERIALIZER
class EmployeeSerializers(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields= '__all__'

	# Field Level validation
	def validate_esalary(self,value):
		if value < 5000:
			raise serializers.ValidationError('Employee salary should be more than 5000')
		return value

	# Object Level Validation
	def validate(self,data):
		ename=data.get('ename')
		esalary=data.get('esalary')

		if ename.lower()=='kiran':
			if esalary>60000:
				raise serializers.ValidationError('Employee salary should be less than 60000')
		return data				
