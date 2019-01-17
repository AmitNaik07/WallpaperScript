import requests, json, os
import datetime, sys


# Enter your API key here 
api_key = "f7b4d81dcf39308ed2732e89dac45f6c"

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + "Pune" 

response = requests.get(complete_url) 

x = response.json() 

#Check if the city exists. 404 signifies that the city could not be found
if x["cod"] != "404": 

	z = x["weather"] 

	weather_description = z[0]["main"] 
 
	print("description = " + str(weather_description))
	now = datetime.datetime.now()
	'''
	weather description: 'Clear', 'Mist', 'Drizzle', 'Snow', 'Thunderstorm'
	'''
	if str(weather_description) == 'Drizzle':
		os.system("""osascript -e 'tell application "Finder" to set desktop picture to POSIX file "/Users/amitnaik/Pictures/Camera Roll/Weather/rainy.jpg"'""")
	
	elif str(weather_description) == 'Thunderstorm':
		os.system("""osascript -e 'tell application "Finder" to set desktop picture to POSIX file "/Users/amitnaik/Pictures/Camera Roll/Weather/thunderstorm.jpg"'""")

	elif str(weather_description) == 'Snow':
		if now.hour >= 0 and now.hour <=18:
			os.system("""osascript -e 'tell application "Finder" to set desktop picture to POSIX file "/Users/amitnaik/Pictures/Camera Roll/Weather/snow_morning.jpg"'""")
		elif now.hour > 18 and now.hour <=23:
			os.system("""osascript -e 'tell application "Finder" to set desktop picture to POSIX file "/Users/amitnaik/Pictures/Camera Roll/Weather/snow_night.jpg"'""")

	elif str(weather_description) == 'Clear': 
		if now.hour > 18 and now.hour <=23:
			os.system("""osascript -e 'tell application "Finder" to set desktop picture to POSIX file "/Users/amitnaik/Pictures/Camera Roll/Weather/clear_night.jpg"'""")
		elif now.hour > 15 and now.hour <=18:
			os.system("""osascript -e 'tell application "Finder" to set desktop picture to POSIX file "/Users/amitnaik/Pictures/Camera Roll/Weather/clear_evening.jpg"'""")
		elif now.hour >= 0 and now.hour <=15:
			os.system("""osascript -e 'tell application "Finder" to set desktop picture to POSIX file "/Users/amitnaik/Pictures/Camera Roll/Weather/clear_morning.jpg"'""")

else: 
	print(" City Not Found ") 
