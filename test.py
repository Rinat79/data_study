import pandas as pd
import requests
import json
import sqlite3 

# 3) получаем данные из Historical Forecast API
url = "https://historical-forecast-api.open-meteo.com/v1/forecast"
params = {
	"latitude": 55.7522,
	"longitude": 37.6156,
	"start_date": "2023-11-01",
	"end_date": "2023-11-07",
	"daily": ["temperature_2m_max", "temperature_2m_min", "sunrise", "sunset", "snowfall_sum", "rain_sum"]
}

response = requests.get(url, params=params)
response.text