import requests

BASE_URL='http://127.0.0.1:8000/'
END_POINT='api/'



def get_resource(id):
	response=requests.get(BASE_URL+END_POINT+id+'/')
	data=response.json()
	print(data)
	
id=input("Enter the id : \t")
get_resource(id)
