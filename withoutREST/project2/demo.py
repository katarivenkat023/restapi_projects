


import requests

BASE_URL='http://127.0.0.1:8000/'
END_POINT='json1/'
response=requests.get(BASE_URL+END_POINT)
print(response)
print(type(response))
print(response.text)


dict_response=response.json()
print(dict_response)
print(type(dict_response))


print('Employee Number: ',dict_response['eid'])
print('Employee Name: ',dict_response['ename'])
print('Employee Age: ',dict_response['eage'])
print('Employee Address: ',dict_response['eaddress'])