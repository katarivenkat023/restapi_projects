import requests

BASE_URL='http://127.0.0.1:8000/'
END_POINT='api/'
response=requests.get(BASE_URL+END_POINT)
print(response)
print(type(response))
print(response.text)
