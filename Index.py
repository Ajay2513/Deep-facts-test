import sys
import requests

sys.stdout.reconfigure(encoding='utf-8')

url = "https://api.geonames.org/searchJSON?country=IN&featureClass=P&maxRows=100&username=srirampalika23"
result = requests.get(url, verify=False)

if result.status_code == 200:
        data = result.json()
        for re in data['geonames']:
            print(re['toponymName'], " ", re['population'])
else:
    print(f"Request failed with status code: {result.status_code}")
