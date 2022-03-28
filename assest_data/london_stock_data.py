from bs4 import BeautifulSoup
import requests
import json
import time


def get_london_exchange_price():
    ##Set the url for which we will be scraping data from
    url = "https://www.marketwatch.com/investing/index/ukx?countrycode=uk"

    ##use the requests module to access the information at the URL
    result = requests.get(url)

    ##Use BeautifulSoup to parse the information using the HTML parser; 
    ##Extract only the text using .text on the result 
    doc = BeautifulSoup(result.text, 'html.parser')

    scripts = doc.find_all('script')

    ##Our data is kept at script index 13
    data = scripts[13].text.strip()

    london_data = json.loads(data)
    london_price = london_data["price"]
    
    return london_price