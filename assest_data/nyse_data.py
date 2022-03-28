from bs4 import BeautifulSoup
import requests
import json
import time



def get_nyse_composite_price():

    nyse_url = "https://www.cnbc.com/quotes/.NYA"

    nyse_result = requests.get(nyse_url)

    doc = BeautifulSoup(nyse_result.text, 'html.parser')

    scripts = doc.find_all("script")

    ##the data we need is located at script[1]

    data = scripts[4].text.strip()

    nya_info = json.loads(data)
    nya_price = nya_info["price"]

    return nya_price






