# Angi hourly weather forecast

This a Python script downloads hourly weather forecast from National weather service. The api is located at `api.weather.gov`. It takes cordinates (latitude and longitude) as inputs to determine location. API documentation can be found [here](https://www.weather.gov/documentation/services-web-api).

Script uses `/points/{lat},{lon}` endpoint  to retrive metadata associated with the goegraphic coordinates. Then from retrived metadata uses `/gridpoints/{wfo}/{x},{y}/forecast/hourly` endpoint to download hourly forecast for the location. Return data is in JSON format.

## installation 
Create and activate virtual environment
```bash
python3 -m pip venv ~/.venv/angi
source ~/.venv/angi/source/activate
```

install required modules 
```bash
python3 -m pip install -r requirments
```

## configuration 
Script reads configuration file in `./config.ini`. 

## build container image
```bash
REGISTRY="gitea.gc.home.arpa"
REPOSITORY="black_sage/angi-data-platform-infrastructure-engineer/angi-forecast"
TAG="0.0.1"
IMAGE="${REGISTRY}/${REPOSITORY}:${TAG}"

podman build -t "$IMAGE" .

podman push "$IMAGE"
```