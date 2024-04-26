
from datetime import datetime, timezone
import requests
import json
import sys

# TODO read from config file
OUTPUT_PATH="/mnt/pv"

def writeJsonToFile( jsonData, filename) :
    with open( f"{OUTPUT_PATH}/{filename}.json" , "w") as file :
        json.dump(data, file )

def getJsonResponse( url ):
    try :
        response = requests.get(url)
        data = json.loads(response.text)
        # TODO check response.status
        return data
    except Error: 
        sys.exit(1)


reqUrl = "https://api.weather.gov/gridpoints/TOP/32,81/forecast/hourly"
response = requests.get(reqUrl)
data = json.loads(response.text)
print("writing file")
now = datetime.now(timezone.utc)
dateNowString  = now.strftime("%Y-%m-%d_%H%M%S")
writeJsonToFile(data , dateNowString)
