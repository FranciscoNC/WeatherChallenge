# WeatherChallenge

Show weather and forecsast for multiple cities.

## Instructions

You have to return information at:

/api/cities/weather/

/api/cities/\<id\>/forecast/

> **_PATH:_** _weather_api/locations/views.py_.

# Commands
## Install dependencies
```
pip install -r requirements.txt
```
## Migrate
```
python3 manage.py migrate
```
## Create default locations
```
python3 manage.py create_locations
```
## Resources
https://www.weatherapi.com/

https://docs.djangoproject.com/en/4.1/intro/tutorial01/