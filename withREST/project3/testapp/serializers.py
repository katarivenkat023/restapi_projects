from rest_framework import serializers
from testapp.models import Employee

class EmployeeSerializers(serializers.Serializer):
	eno = serializers.IntegerField()
	ename = serializers.CharField(max_length=50)
	esalary = serializers.IntegerField()
	eaddress=serializers.CharField(max_length=50)


	
	def create(self,validated_data):
		return Employee.objects.create(**validated_data)