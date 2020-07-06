# https://openweathermap.org/forecast5
# cnt Number of lines returned by this API call

class City:
    # city
    # city.id City ID
    # city.name City name
    # city.coord
    # city.coord.lat City geo location, latitude
    # city.coord.lon City geo location, longitude
    # city.country Country code (GB, JP etc.)
    # city.timezone Shift in seconds from UTC    
    # "sunrise": 1593945177,
    # "sunset": 1594000882    
    def __init__(self, cid, name, lat, lon, country, timezone, sunrise, sunset):
        self.cid = cid
        self.name = name
        self.coord = {
            "lat": lat, 
            "lon": lon
        }
        self.country = country
        self.timezone = timezone
        self.sunrise = sunrise
        self.sunset = sunset

    def __str__(self):
        return "Name: {0} | Country: {1} | Lat: {2} | Lon: {3}"\
        .format(self.name, 
                self.country,
                self.coord["lat"], 
                self.coord["lon"])


class ForecastRecord:
    # list
    # list.dt Time of data forecasted, unix, UTC
    # list.main
    # list.main.temp Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
    # list.main.feels_like Temperature. This temperature parameter accounts for the human perception of weather. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
    # list.main.temp_min Minimum temperature at the moment of calculation. This is minimal forecasted temperature (within large megalopolises and urban areas), use this parameter optionally. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
    # list.main.temp_max Maximum temperature at the moment of calculation. This is maximal forecasted temperature (within large megalopolises and urban areas), use this parameter optionally. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
    # list.main.pressure Atmospheric pressure on the sea level by default, hPa
    # list.main.sea_level Atmospheric pressure on the sea level, hPa
    # list.main.grnd_level Atmospheric pressure on the ground level, hPa
    # list.main.humidity Humidity, %
    # list.main.temp_kf Internal parameter
    # list.weather (more info Weather condition codes)
    # list.weather.id Weather condition id
    # list.weather.main Group of weather parameters (Rain, Snow, Extreme etc.)
    # list.weather.description Weather condition within the group. You can get the output in your language. Learn more.
    # list.weather.icon Weather icon id
    # list.clouds
    # list.clouds.all Cloudiness, %
    # list.wind
    # list.wind.speed Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour.
    # list.wind.deg Wind direction, degrees (meteorological)
    # list.rain
    # list.rain.3h Rain volume for last 3 hours, mm (SKIPPED)
    # list.snow
    # list.snow.3h Snow volume for last 3 hours (SKIPPED)
    # list.dt_txt Time of data forecasted, ISO, UTC            
    def __init__(self, dt, temp, feels_like, temp_min, temp_max, 
                 pressure, sea_level, grnd_level, humidity, temp_kf,
                 wid, main, description, icon, call, speed, deg, dt_txt):
        self.dt = dt
        self.main = {
            "temp" : temp, 
            "feels_like" : feels_like, 
            "temp_min" : temp_min, 
            "temp_max" : temp_max, 
            "pressure" : pressure, 
            "sea_level" : sea_level, 
            "grnd_level" : grnd_level, 
            "humidity" : humidity, 
            "temp_kf" : temp_kf
        }
        self.weather = {
            "wid" : wid, 
            "main" : main, 
            "description" : description, 
            "icon" : icon
        }
        self.clouds = {
            "call" : call
        }
        self.wind = {
            "speed" : speed, 
            "deg" : deg
        }
        self.dt_txt = dt_txt

    def __str__(self):
        return "Date: {0}\nTemp: {1}F\nWeather: {2}\n"\
        .format(self.dt_txt, 
                self.main["temp"],
                self.weather["description"])        

