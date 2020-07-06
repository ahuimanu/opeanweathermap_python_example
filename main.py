from dotenv import load_dotenv, find_dotenv
import json
import mysql.connector
import os
import requests
from OpenWeatherMapForecastRecord import City, ForecastRecord

# this example requires that you obtain an open weather map API key
# https://openweathermap.org/api

# while this could use better organization into functions, this code
# reads from an API, fills values for City and ForecastRecord objects
# and suggests how inserts into MySQL, using mysql-connector-python,
# can be accomplished

# python dotenv documentation: https://pypi.org/project/python-dotenv/
# read dotenv file
load_dotenv(find_dotenv())

# setup

# python data structures review
# [] - means a list - https://www.w3schools.com/python/python_lists.asp (just like an array and list put together)
# () - means a tuple - https://www.w3schools.com/python/python_tuples.asp
# {} - means a dictionary - https://www.w3schools.com/python/python_dictionaries.asp
#    - or a set - https://www.w3schools.com/python/python_sets.asp

# let's use Minneapolis–Saint Paul International Airport as an example location
kmsp = (44.881944, -93.221667)

# don't forget that this requires that you've read the dotenv documentation
# and that you have created a .env file in the same directory as this script
api_key = os.getenv("OPEN_WEATHER_MAP_API_KEY")
url = "http://api.openweathermap.org/data/2.5/forecast?lat={0}&lon={1}&appid={2}&units={3}"\
      .format(kmsp[0], kmsp[1], api_key,"imperial")


# call service
service = requests.get(url)
data = service.json()

# parse data
count = data["cnt"]

# CITY ########################################################################

 # id, name, lat, lon, country, tz, sunrise, sunset

city = City(data["city"]["id"],
            data["city"]["name"],
            data["city"]["country"],
            data["city"]["coord"]["lat"],
            data["city"]["coord"]["lat"],
            data["city"]["timezone"],
            data["city"]["sunrise"],
            data["city"]["sunset"])

print(city)

# db stuff
# don't run these without using actual db conneciton values - uncomment to use
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# MySQL Connector Code
sql_statement = "INSERT INTO TableName VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
val = (city.cid, city.name, city.country, city.coord["lat"],
       city.coord["lon"], city.timezone, city.sunrise, city.sunset)

# don't run these without using actual db conneciton values - uncomment to use
# mycursor.execute(sql_statement, val)
# mydb.commit()

forecasts = []

# FORECAST RECORDS ############################################################
for forecast in data["list"]:
    # datetime
    dt = forecast["dt"]

    #main
    main_temp = forecast["main"]["temp"]
    main_feels_like = forecast["main"]["feels_like"]
    main_temp_min = forecast["main"]["temp_min"]
    main_temp_max = forecast["main"]["temp_max"]
    main_pressure = forecast["main"]["pressure"]
    main_sea_level = forecast["main"]["sea_level"]
    main_grnd_level = forecast["main"]["grnd_level"]
    main_humidity = forecast["main"]["humidity"]
    main_temp_kf = forecast["main"]["temp_kf"]

    #weather
    weather_id = forecast["weather"][0]["id"]
    weather_main = forecast["weather"][0]["main"]
    weather_description = forecast["weather"][0]["description"]
    weather_icon = forecast["weather"][0]["icon"]

    # clouds
    clouds_all = forecast["clouds"]["all"]

    # wind
    wind_speed = forecast["wind"]["speed"]
    wind_deg = forecast["wind"]["deg"]

    #datetime text
    dt_txt = forecast["dt_txt"]

    # build ForecastRecord object
    rec = ForecastRecord(dt, main_temp, main_feels_like, main_temp_min, main_temp_max, 
                         main_pressure, main_sea_level, main_grnd_level, main_humidity, 
                         main_temp_kf, weather_id, weather_main, weather_description, 
                         weather_icon, clouds_all, wind_speed, wind_deg, dt_txt)
    forecasts.append(rec)
    print(rec)

    # todo: write to database here

