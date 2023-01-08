from rest_framework import serializers
from testapp.models import Employee

#by using validators
def multiple_of_1000(value):
	if value%1000!=0:
		raise serializers.ValidationError("EMplpoyee salary shoud be multiples of 1000")

class EmployeeSerializers(serializers.Serializer):
	eno = serializers.IntegerField() 
	ename = serializers.CharField(max_length=50)
	esalary = serializers.IntegerField(validators=[multiple_of_1000])
	eaddress = serializers.CharField(max_length=50)

	#Feild level validatrion
	def validate_esalary(self,value):
		if value < 5000:
			raise serializers.ValidationError("Employee salary shoud be more tham 5000")

	#object level validation
	def validate(self,value):
		ename=data.get('ename')
		esalary=data.get('esalary')

		if ename.lower()=='reddy':
			if value < 5000:
				raise serializers.ValidationError("Emplpoyee salary shoud be more than 5000")
		return data


	def create(self,validated_data):
		return Employee.objects.create(**validated_data)


	def update(self,instance,validated_data):
		instance.eno = validated_data.get('eno',instance.eno)
		instance.ename = validated_data.get('ename',instance.ename)
		instance.esalary = validated_data.get('esalary',instance.esalary)
		instance.eaddress = validated_data.get('eaddress',instance.eaddress)
		instance.save()
		return instance
