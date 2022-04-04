import requests

api_key = 'UC58CHR7KEMO6OHI'

ticker = "NYA"


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=NYA&interval=5min&apikey={api_key}'
r = requests.get(url)
data = r.json()

print(data)

api_key = 'UC58CHR7KEMO6OHI'
