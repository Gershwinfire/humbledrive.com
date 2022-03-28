from bs4 import BeautifulSoup
import requests
import json
import time



def get_shanghai_price():
    ##Set the url for which we will be scraping data from
    url = "https://www.marketwatch.com/investing/index/shcomp?countrycode=cn"

    ##use the requests module to access the information at the URL
    result = requests.get(url)

    ##Use BeautifulSoup to parse the information using the HTML parser; 
    ##Extract only the text using .text on the result 
    doc = BeautifulSoup(result.text, 'html.parser')


    ##This data is kept in the form of table data, so we search throught the data for table rows
    trs = doc.find_all("tr")

    ##I manually used this step to clean the data and extact only the information I was aiming to find
    ##The data was kept in row 34, and in table data 3.
    ##I set those indices using two variables and used a third variable to set the beginning shanghai price to 0

    counter = 0
    index = 0
    shanghai_price = 0
    for tr in trs:
        if counter == 34:
            #print(counter, td)
            for td in tr:
                #print(index, td)
                if index == 3:
                    ##The Data was found, and using the .text we set the new shanghai price to the text at 
                    #previously discussed indices
                    shanghai_price = td.text
                index += 1
        counter += 1

    return(shanghai_price)