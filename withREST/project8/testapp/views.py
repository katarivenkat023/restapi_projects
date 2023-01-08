from django.shortcuts import render
from rest_framework.views import APIView
from testapp.models import Employee
from testapp.serializers import EmployeeSerializers
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
# Create your views here.
class EmployeeListAPIView(ListAPIView):
		queryset=Employee.objects.all()
		serializer_class=EmployeeSerializers
		#to implememnt search operation
		def get_queryset(self):
			query_set=Employee.objects.all()
			name=self.request.GET.get('ename')
			if name is not None:
				query_set=query_set.filter(ename__icontains=name)
			return query_set

class EmployeeCreateAPIView(CreateAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializers


class EmployeeDetailAPIView(RetrieveAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializers
	lookup_field='id'

class EmployeeUpdateAPIView(UpdateAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializers

class EmployeeDeleteAPIView(DestroyAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializers