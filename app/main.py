
from datetime import datetime, timezone
from configparser import ConfigParser
import requests
import json
import sys
import logging
from pprint import pprint 

def loadConfig( configFileName):
    """
    reads config file and returns outputPath, latitude and longitude
    """
    #TODO check if config file exists
    logging.info("loading config file")
    config  = ConfigParser()
    config.read(configFileName)
    logging.info(f"loaded config file \"{configFileName}\".")

    outputPath = config["OUTPUT"]["path"]
    longitude = config["LOCATION"]["longitude"]
    latitude = config["LOCATION"]["latitude"]

    logging.info(f"output path {outputPath} , latitude {latitude}, longitude {longitude}")
    return outputPath , latitude, longitude


def writeJsonToFile( outputPath, filename, data):
    logging.info(f"writing forecast data to {outputPath}/{filename}.json")
    with open( f"{outputPath}/{filename}.json" , "w") as file :
        json.dump(data, file )

def getJsonResponse( url ):
    try : 
        logging.info(f"fetching forecast from {url}")
        response = requests.get(url)
        data = json.loads(response.text)
        # TODO check response.status
        return data
    except Error: 
        sys.exit(1)

def reteriveforecastHourlyURL(latitude, longitude):
    try:
        url = f"https://api.weather.gov/points/{latitude},{longitude}"
        response = requests.get(url)
        data = json.loads(response.text)
        forecastHourlyURL = data['properties']['forecastHourly']
        logging.info(f"grid point url {forecastHourlyURL}")
        return forecastHourlyURL
        
    except Error:
        pass


if __name__ ==  "__main__" :
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    outputPath, latitude, longitude = loadConfig("config.ini")

    hourlyForecastURL = reteriveforecastHourlyURL(latitude, longitude)
    
    hourlyForecast = getJsonResponse(hourlyForecastURL)

    now = datetime.now(timezone.utc)
    dateNowString  = now.strftime("%Y-%m-%d_%H%M%S")
    writeJsonToFile(outputPath, dateNowString, hourlyForecast)
