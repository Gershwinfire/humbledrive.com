from bs4 import BeautifulSoup
import requests


url = "https://www.coingecko.com/en/coins/bitcoin"


result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")


for line in doc:
    print(line)