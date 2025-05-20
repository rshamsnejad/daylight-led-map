import requests
from pprint import pprint
from apikeys.apiverve import *

url = "https://api.apiverve.com/v1/sunrisesunset"

querystring = {'lat': '36.7201600', 'lon': '-4.4203400', 'date': '05-20-2025'}

headers = {
	"x-api-key": apiverve_key
}

response = requests.get(url, headers=headers, params=querystring)

pprint(response.json())
	
							