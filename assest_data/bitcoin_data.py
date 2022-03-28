from bs4 import BeautifulSoup
import requests
import json


def get_bitcoin_price():
    ##Set the url for which we will be scraping data from
    url = "https://www.marketwatch.com/investing/cryptocurrency/btcusd"

    ##use the requests module to access the information at the URL
    result = requests.get(url)

    ##Use BeautifulSoup to parse the information using the HTML parser; 
    ##Extract only the text using .text on the result 
    doc = BeautifulSoup(result.text, 'html.parser')

    scripts = doc.find_all('script')

    ##Our data is kept at script index 13
    data = scripts[13].text.strip()

    bitcoin_data = json.loads(data)
    bitcoin_price = bitcoin_data["price"]

    return(bitcoin_price)