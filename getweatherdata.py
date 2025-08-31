import openmeteo_requests
import json as js
import pandas as pd
import requests_cache

from retry_requests import retry
from pdb import set_trace as B

def test():
    
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)
    
    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
	"latitude": 52.52,
	"longitude": 13.41,
	"hourly": "temperature_2m",
    }
    responses = openmeteo.weather_api(url, params=params)
    
    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation: {response.Elevation()} m asl")
    print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")
    
    # Process hourly data. The order of variables needs to be the same as requested.
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    
    hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
    )}
    
    hourly_data["temperature_2m"] = hourly_temperature_2m
    
    hourly_dataframe = pd.DataFrame(data = hourly_data)
    print("\nHourly data\n", hourly_dataframe)

def getCityd():
    openmeteo = openmeteo_requests.Client()

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
	"latitude": 52.52,
	"longitude": 13.41,
	"hourly": ["temperature_2m", "precipitation", "wind_speed_10m"],
	"current": ["temperature_2m", "relative_humidity_2m"],
    }
    responses = openmeteo.weather_api(url, params=params)
    
    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation: {response.Elevation()} m asl")
    print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")
    
    # Process current data. The order of variables needs to be the same as requested.
    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()
    current_relative_humidity_2m = current.Variables(1).Value()
    
    print(f"Current time: {current.Time()}")
    print(f"Current temperature_2m: {current_temperature_2m}")
    print(f"Current relative_humidity_2m: {current_relative_humidity_2m}")

def histdata():

    cities = [
        {"city": "Tokyo", "country": "Japan", "lat": 35.6828, "lon": 139.7595, "population_millions": 37.04},
        {"city": "Delhi", "country": "India", "lat": 28.6139, "lon": 77.2090, "population_millions": 34.67},
        {"city": "Shanghai", "country": "China", "lat": 31.2304, "lon": 121.4737, "population_millions": 30.48},
        {"city": "Dhaka", "country": "Bangladesh", "lat": 23.8103, "lon": 90.4125, "population_millions": 24.65},
        {"city": "Cairo", "country": "Egypt", "lat": 30.0444, "lon": 31.2357, "population_millions": 23.07},
        {"city": "São Paulo", "country": "Brazil", "lat": -23.5505, "lon": -46.6333, "population_millions": 22.99},
        {"city": "Mexico City", "country": "Mexico", "lat": 19.4326, "lon": -99.1332, "population_millions": 22.75},
        {"city": "Beijing", "country": "China", "lat": 39.9042, "lon": 116.4074, "population_millions": 22.60},
        {"city": "Mumbai", "country": "India", "lat": 19.0760, "lon": 72.8777, "population_millions": 22.09},
        {"city": "Osaka", "country": "Japan", "lat": 34.6937, "lon": 135.5023, "population_millions": 18.92},
        {"city": "Chongqing", "country": "China", "lat": 29.4316, "lon": 106.9123, "population_millions": 18.17},
        {"city": "Karachi", "country": "Pakistan", "lat": 24.8607, "lon": 67.0011, "population_millions": 18.08},
        {"city": "Kinshasa", "country": "DR Congo", "lat": -4.4419, "lon": 15.2663, "population_millions": 17.78},
        {"city": "Lagos", "country": "Nigeria", "lat": 6.5244, "lon": 3.3792, "population_millions": 17.16},
        {"city": "Istanbul", "country": "Turkey", "lat": 41.0082, "lon": 28.9784, "population_millions": 16.24},
        {"city": "Kolkata", "country": "India", "lat": 22.5726, "lon": 88.3639, "population_millions": 15.85},
        {"city": "Buenos Aires", "country": "Argentina", "lat": -34.6037, "lon": -58.3816, "population_millions": 15.75},
        {"city": "Manila", "country": "Philippines", "lat": 14.5995, "lon": 120.9842, "population_millions": 15.23},
        {"city": "Guangzhou", "country": "China", "lat": 23.1291, "lon": 113.2644, "population_millions": 14.88},
        {"city": "Lahore", "country": "Pakistan", "lat": 31.5546, "lon": 74.3572, "population_millions": 14.83},
        {"city": "Tianjin", "country": "China", "lat": 39.3434, "lon": 117.3616, "population_millions": 14.70},
        {"city": "Bangalore", "country": "India", "lat": 12.9716, "lon": 77.5946, "population_millions": 14.40},
        {"city": "Rio de Janeiro", "country": "Brazil", "lat": -22.9068, "lon": -43.1729, "population_millions": 13.92},
        {"city": "Shenzhen", "country": "China", "lat": 22.5431, "lon": 114.0579, "population_millions": 13.55},
    ]
    
    cities2 = [
        {"city": "Tokyo", "country": "Japan", "lat": 35.6828, "lon": 139.7595},
        {"city": "Delhi", "country": "India", "lat": 28.6139, "lon": 77.2090},
        {"city": "Shanghai", "country": "China", "lat": 31.2304, "lon": 121.4737},
        {"city": "São Paulo", "country": "Brazil", "lat": -23.5505, "lon": -46.6333},
        {"city": "Mexico City", "country": "Mexico", "lat": 19.4326, "lon": -99.1332},
        {"city": "Cairo", "country": "Egypt", "lat": 30.0444, "lon": 31.2357},
        {"city": "Dhaka", "country": "Bangladesh", "lat": 23.8103, "lon": 90.4125},
        {"city": "Beijing", "country": "China", "lat": 39.9042, "lon": 116.4074},
        {"city": "Mumbai", "country": "India", "lat": 19.0760, "lon": 72.8777},
        {"city": "Osaka", "country": "Japan", "lat": 34.6937, "lon": 135.5023}]
    
    cities3 ={'Tokyo':['Japan',35.6828,139.7595],
            'Dehli':['India',28.6139,77.2090],
            'Shanghai':['China',31.2304,121.4737],
            'São Paulo':['Brazil',-23.5505,-46.6333],
            'Mexico City':['Mexico',19.4326,-99.1332],
            'Cairo':['Egypt',30.0444,31.2357],
	    'Dhaka':['Bangladesh',23.8103,90.4125],
            'Beijing':['China',39.9042,116.4074],
            'Mumbai':['India',19.0760,72.8777],
	    'Osaka':['Japan',34.6937,135.5023]}
    
    # Initialize client
    client = openmeteo_requests.Client()

    # Correct archive endpoint
    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": 59.3293,         # Example: Stockholm
        "longitude": 18.0686,
        "start_date": "1940-01-01",
        "end_date": "1940-01-07",
        "hourly": ["temperature_2m", "precipitation"]
    }
    
    # Fetch data
    responses = client.weather_api(url, params=params)
    response = responses[0]
    
    # Access hourly data
    hourly = response.Hourly()
    temp = hourly.Variables(0).ValuesAsNumpy()   # temperature_2m
    precip = hourly.Variables(1).ValuesAsNumpy() # precipitation

    print("First 10 temperatures:", temp[:100])
    print("First 10 precip values:", precip[:100])

    ct=[l['city'] for l in cities]
    
    with open("cities.json","w") as f:
        js.dump(ct,f)
        
