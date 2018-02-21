#! /usr/local/bin/python3
from flask import Flask
from flask import request
from flask import render_template

import requests
import csv
import json

# Function to retrieve the stock prices from the API
BASE_URL = 'https://www.quandl.com/api/v3/datasets/EOD'
API_KEY = 'zC992yeEkw5VTye5PFJY'

def retrieve_stock_price(stock_name):
	# Make the request to receive the CSV data
	api_url = '%s/%s.csv?api_key=%s' % (BASE_URL, stock_name, API_KEY)
	result = requests.get(api_url).content
	csv_as_text = result.decode('utf-8').splitlines()
	
	# Now, use the csv module to interpret all this data
	return list(csv.reader(csv_as_text, delimiter=','))

# Declare the Flask application
app = Flask("BigSmoke")

# index route, the page that displays the stock prices
@app.route('/', methods=['GET'])
def index_page():
	# Get the stock name from the GET parameters, or just pick Apple if none are provided
	stock_name = request.args.get('stock', 'AAPL')
	
	# Fetch the price data and serve a page containing it.
	stock_prices = retrieve_stock_price(stock_name)
	
	return render_template('index.html', 
		stock_prices=stock_prices
	)

# Run the server
app.run(host='localhost', port=7777)

