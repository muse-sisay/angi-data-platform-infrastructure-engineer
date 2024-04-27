# Angi hourly weather forecast

This Python script downloads hourly weather forecast from the National weather service. The API is located at `api.weather.gov`. It takes coordinates (latitude and longitude) as inputs to determine which forecast office to use. API documentation can be found [here](https://www.weather.gov/documentation/services-web-api).

Script uses `/points/{lat},{lon}` endpoint  to retrieve metadata associated with the geographic coordinates. Then from the retrieved metadata uses `/gridpoints/{wfo}/{x},{y}/forecast/hourly` endpoint to download hourly forecast for the location. This returns a JSON response contains hourly weather predictions for the given location. Parameters included in the forecast data include temperature, wind speed, precipitation chances and more.

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

```bash
python3 main.py
```

## build container image
```bash
REGISTRY="gitea.gc.home.arpa"
REPOSITORY="black_sage/angi-data-platform-infrastructure-engineer/angi-forecast"
TAG="0.0.1"
IMAGE="${REGISTRY}/${REPOSITORY}:${TAG}"

podman build -t "$IMAGE" .

podman push "$IMAGE"
```