
from datetime import datetime, timezone
from configparser import ConfigParser
import requests
import json
import sys

def writeJsonToFile( outputPath, filename, data) :
    with open( f"{outputPath}/{filename}.json" , "w") as file :
        json.dump(data, file )

def getJsonResponse( url ):
    try :
        response = requests.get(url)
        data = json.loads(response.text)
        # TODO check response.status
        return data
    except Error: 
        sys.exit(1)



#TODO write log to STDOUT

if __name__ ==  "__main__" :
    #TODO check if config file exists
    config  = ConfigParser()
    config.read('config.ini')

    outputPath = config["OUTPUT"]["path"]
    forecastOfficeID = config["LOCATION"]["forecase_office_id"]
    longitude = config["LOCATION"]["x_coordinate"]
    latitude = config["LOCATION"]["y_coordinate"]

    reqUrl = f"https://api.weather.gov/gridpoints/{forecastOfficeID}/{latitude},{longitude}/forecast/hourly"

    data = getJsonResponse(reqUrl)

    now = datetime.now(timezone.utc)
    dateNowString  = now.strftime("%Y-%m-%d_%H%M%S")
    writeJsonToFile(outputPath, dateNowString, data)
