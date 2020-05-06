import requests
import json

akResponse = requests.get("https://covidtracking.com/api/v1/states/current.json")

def alaskaRecovered(obj):
    # createa  formatted string of the Python JSON Object
    text = json.dumps(obj, sort_keys=True, indent=4)
    x = json.loads(text)
    x = x[0]['recovered']
    #print(text)
    print(str(x))
    
    
alaskaRecovered(requests.get("https://covidtracking.com/api/v1/states/current.json").json())
#jprint(akResponse.json())