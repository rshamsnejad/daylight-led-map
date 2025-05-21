from secrets.apiverve import *
from rude_http import get


def get_suntime(lat: float, lon: float, date: str):

	url = "https://api.apiverve.com/v1/sunrisesunset"

	querystring = {'lat': lat, 'lon': lon, 'date': date}

	headers = {
		"x-api-key": apiverve_key
	}

	response = get(url, headers=headers, params=querystring)

	return response.json()
	