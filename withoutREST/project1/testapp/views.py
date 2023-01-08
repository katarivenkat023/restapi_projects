from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student_data(request):
	data={'sid':123,'name':"venky","age":23,"address":"Bangalore"}
	response="<h1>Student id : {} <br> Student Name : {} <br> Student Age : {} <br>Student address: {} </h1>".format(data['sid'],data['name'],data['age'],data['address'])
	return HttpResponse(response)