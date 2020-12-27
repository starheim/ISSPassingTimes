import requests
import json
from datetime import datetime

astronauts = "http://api.open-notify.org/astros.json"
issPass = "http://api.open-notify.org/iss-pass.json"

issPassParams = {
	"lat":62,
	"lon":7
}

astronautsResponse = requests.get(astronauts)
issPassResponse = requests.get(issPass, params=issPassParams)

passes = issPassResponse.json()['response']

for p in passes:
	risetime = datetime.fromtimestamp(p['risetime'])
	duration = p['duration']
	m, s = divmod(duration, 60)
	print(f"ISS will pass over Molde: {risetime} for {m}m {s}s")
