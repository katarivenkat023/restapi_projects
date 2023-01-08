import requests

BASE_URL='http://127.0.0.1:8000/'
END_POINT='api/'



def get_resource():
	response=requests.get(BASE_URL+END_POINT)
	print(response)
	print(response.status_code)
	print(response.json())
	

get_resource()
