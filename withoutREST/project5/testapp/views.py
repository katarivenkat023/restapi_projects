from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def get(request):
	data={'msg':'This is from get method'}
	return JsonResponse(data)
def post(request):
	data={'msg':'This is from post method'}
	return JsonResponse(data)

def put(request):
	data={'msg':'This is from put method'}
	return JsonResponse(data)

def delete(request):
	data={'msg':'This is from delete method'}
	return JsonResponse(data)