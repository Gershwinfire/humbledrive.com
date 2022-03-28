from bs4 import BeautifulSoup
import requests
import json



def get_nasdaq_price():
    ##Set the url for which we will be scraping data from
    url = "https://www.cnbc.com/quotes/NDAQ?qsearchterm=nasdaq"

    ##use the requests module to access the information at the URL
    result = requests.get(url)

    ##Use BeautifulSoup to parse the information using the HTML parser; 
    ##Extract only the text using .text on the result 
    doc = BeautifulSoup(result.text, 'html.parser')

    ##Search through the html text for scripts
    scripts = doc.find_all("script")

    ##Here I manually searched the scripts individually to find the correct index that will be used
    ##Strip the data of white space and only return the text
    data = scripts[4].text.strip()

    ##Now That the data is cleaned and in a json format we can properly use the json module to 
    ##return the data we wish to extract
    nasdaq_data = json.loads(data)
    nasdaq_price = nasdaq_data["price"]
    ##for this we want to return the price
    
    return nasdaq_price


