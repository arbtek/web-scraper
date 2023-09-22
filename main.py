import requests 
from bs4 import BeautifulSoup

### Build query - pick website to scrape data from 
URL = "https://weather.com/weather/today/l/54f9d8baac32496f6b5497b4bf7a277c3e2e6cc5625de69680e6169e7e38e9a8"
htmlPage = requests.get(URL)
BeautifulSoup = BeautifulSoup(htmlPage.content, "html.parser")

### Parse the results 
results = BeautifulSoup.find(id="WxuCurrentConditions-main-eb4b02cb-917b-45ec-97ec-d4eb947f6b6a")
###print(results)
currentTemp = results.find("span", class_="CurrentConditions--tempValue--MHmYY")
###print(currentTemp)
###print(currentTemp.txt)
description = results.find("div", class_="CurrentConditions--phraseValue--mZC_p")

location = results.find("h1", class_="CurrentConditions--location--1YWj_")
timeOfDay = results.find("span", class_="CurrentConditions--timestamp--1ybTk")

### Print results to user 
print("Current temperature:", currentTemp.text)
print("Weather description:", description.text)
print("Location:", location.text)
print("Local time:", timeOfDay.text)