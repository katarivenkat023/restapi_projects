from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from testapp.serializers import NameSerializers

# Create your views here.
class TestViewSet(ViewSet):
	def list(self,request,*args,**kwargs):

		colours=['Red','Black','Blue','Green','Orange']
		my_dict={'msg':'Happy Depawali','colours':colours}

		# convert Python Dictionary into JSON
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

	def patch(self,request,*args,**kwargs):
		return Response({'msg':'This is from patch() of API View Class'})

	def delete(self,request,*args,**kwargs):
		return Response({'msg':'This is from delete() of API View Class'})