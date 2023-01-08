from django.shortcuts import render 
import io
from rest_framework.parsers import JSONParser
from testapp.serializers import EmployeeSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from testapp.models import Employee
from django.views.generic import View 
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCROperation(View):
	def put(self,request,*args,**kwargs):
		json_data = request.body

		#Converting Json data into Python Dictionary
		stream = io.BytesIO(json_data)
		python_data = JSONParser().parse(stream)

		id = python_data.get('id')
		emp = Employee.objects.get(id=id)

		# perform Deserialization
		#convert Python Dictionary into Database code
		employee_serializer = EmployeeSerializers(emp,data=python_data,partial=True)
		if employee_serializer.is_valid():
			employee_serializer.save()
			msg={'msg':'Resource Updated successfully'}
			json_data = JSONRenderer().render(msg)
			return HttpResponse(json_data,content_type='application/json')

		json_data = JSONRenderer().render(employee_serializer.errors)
		return HttpResponse(json_data,content_type='application/json')
'''
	def delete(self,request,*args,**kwargs):
		json_data = request.body

		#Converting Json data into Python Dictionary
		stream = io.BytesIO(json_data)
		python_data = JSONParser().parse(stream)

		id = python_data.get('id')
		emp = Employee.objects.get(id=id)

		emp.delete()

		msg={'msg':'Resource Deleted successfully'}
		json_data = JSONRenderer().render(msg)
		return HttpResponse(json_data,content_type='application/json')'''














		