from bs4 import BeautifulSoup
import requests
import json
import time


##Set the url for which we will be scraping data from
url = "https://www.marketwatch.com/investing/index/n100?countrycode=xx"

##use the requests module to access the information at the URL
result = requests.get(url)

##Use BeautifulSoup to parse the information using the HTML parser; 
##Extract only the text using .text on the result 
doc = BeautifulSoup(result.text, 'html.parser')

scripts = doc.find_all('script')

##Our data is kept at script index 13
data = scripts[13].text.strip()

euronext_data = json.loads(data)

print(euronext_data['price'])