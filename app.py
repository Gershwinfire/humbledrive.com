from flask import Flask, render_template, request
from assest_data.bitcoin_data import get_bitcoin_price
from assest_data.bombay_stock_exchange import get_bombay_price
from assest_data.hang_seng_data import get_hangseng_price
from assest_data.japan_exchange_data import get_japan_exchange_price
from assest_data.london_stock_data import get_london_exchange_price
from assest_data.nasdaq_data import get_nasdaq_price
from assest_data.national_stock_exchange import get_national_price
from assest_data.nyse_data import get_nyse_composite_price
from assest_data.shanghai_data import get_shanghai_price
from assest_data.shenzhen_data import get_shenzhen_price
from get_time import get_time




app = Flask(__name__)

@app.route("/", methods=["get"])
def welcome():
    return render_template("welcome.html")


@app.route("/index", methods=["get"])
def index():
    return render_template("index.html")

@app.route("/bobbygfitness", methods=["get"])
def bobbygfitness():
    return render_template("bgfhomepage.html")

@app.route("/crypto", methods=["get"])
def crypto():

        ##Assign the times/zone for each market along with Market Prices
        ##These are the Manually Scraped DATA for Stock Market Prices
        bitcoin_price = get_bitcoin_price()
        
        bom_price = get_bombay_price()
        bombaytime = get_time('Asia/Kolkata')

        hang_seng_price = get_hangseng_price()
        hong_kong_time = get_time('Asia/Hong_Kong')

        japan_exchange_price = get_japan_exchange_price()
        japan_time = get_time("Japan")

        london_stock_price = get_london_exchange_price()
        london_time = get_time("Europe/Dublin")

        nasdaq_price = get_nasdaq_price()
        east_coast_time = get_time("US/Eastern")

        national_stock_price = get_national_price()
        ##This is the same as bombay_time

        nyse_composite_price = get_nyse_composite_price()
        #This is the same as east_coast_time from U=S

        shanghai_price = get_shanghai_price()
        shanghai_time = get_time("Asia/Shanghai")

        shenzhen_price = get_shenzhen_price()
        ##This is the same as Hong_kong Time

        return render_template("crypto_test.html", nasdaq_price=nasdaq_price, nyse_composite_price=nyse_composite_price, bom_price=bom_price, hang_seng_price=hang_seng_price, japan_exchange_price=japan_exchange_price, national_stock_price=national_stock_price, london_stock_price=london_stock_price, shanghai_price=shanghai_price, shenzhen_price=shenzhen_price,
            shanghai_time=shanghai_time,east_coast_time=east_coast_time, hong_kong_time=hong_kong_time,london_time=london_time, japan_time=japan_time, bombaytime=bombaytime)
        ##return render_template("crypto_homepage.html", nasdaq_price=nasdaq_price, national_stock_price=national_stock_price, nyse_composite_price=nyse_composite_price, shanghai_price=shanghai_price, shenzhen_price=shenzhen_price, london_stock_price=london_stock_price, japan_exchange_price=japan_exchange_price, bitcoin_price=bitcoin_price, bom_price=bom_price, hang_seng_price=hang_seng_price)