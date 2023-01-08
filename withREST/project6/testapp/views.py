from django.shortcuts import render
from testapp.serializers import NameSerializers
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.
class APIViewclass(APIView):

	def get(self,request,*args,**kwargs):
		colors=['Red','Blue','Green','Yeloow']
		my_dict={'msg':"Happy Diwali",'colors':colors}

		#converting python dictinary into JSON
		return Response(my_dict)


	def post(self,request,*args,**kwargs):
		serializer=NameSerializers(data=request.data)
		if serializer.is_valid():
			name=serializer.data.get('name')
			msg='Hello {} welcome to Study Online'.format(name)
			my_dict={'msg':msg}
			return Response(my_dict)
		else: 
			return Response(serializer.errors,status=400)


	def put(self,request,*args,**kwargs):
		return Response({'msg':'This is from put() of API View Class'})

	def delete(self,request,*args,**kwargs):
		return Response({'msg':'This is from delete() of API View Class'})


