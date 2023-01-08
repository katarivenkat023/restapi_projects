
from rest_framework import serializers

# Create your serializers here.
class EmployeeSerializers(serializers.Serializer):
	eno = serializers.IntegerField()
	ename=serializers.CharField(max_length=20)
	esalary=serializers.IntegerField()
	eaddress=serializers.CharField(max_length=50)