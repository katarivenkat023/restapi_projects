import requests

BASE_URL='http://127.0.0.1:8000/'
END_POINT='api/'

import json
def delete_resource(id):
	response = requests.delete(BASE_URL+END_POINT+str(id)+'/')
	print(response.json())
	print(response.status_code)

id = int(input('Enter the id:\t'))
delete_resource(id)

