import requests

BASE_URL='http://127.0.0.1:8000/'
END_POINT='api/'

import json
def update_resource(id):
	update_data={'esalary':20000,'eaddress':'Mandya'}
	
	response = requests.put(BASE_URL+END_POINT+str(id)+'/',data=json.dumps(update_data))
	print(response.json())
	print(response.status_code)

id = int(input('Enter the id:\t'))
update_resource(id)

