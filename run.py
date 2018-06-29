# Alpha Vantage API key is: 5VSS7HHPZKB1DXK9
import requests, json, urllib.request
from flask import Flask, render_template, request
from urllib.parse import urljoin

app = Flask(__name__)


@app.route("/")

def currency():
    # sets currency variables and default values
    currency1 = request.args.get("currency1", "EUR")
    currency2 = request.args.get("currency2", "USD")
    json_url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=" + currency1 + "&to_currency=" + currency2 + "&apikey=5VSS7HHPZKB1DXK9"

    curr_dict = {}
    
    result1 = {}
    result2 = {}

    print(json_url)

    # pick the currency list from csv file and store the currencies and  description in a dictionary 
    with open("files/currency_list.csv", "r") as file:
        for line in file:
            # putting the csv elements in a list, remove linebreaks
            curr_set = line.strip().split(",") 
            curr = curr_set[0]
            curr_name = curr_set[1]
            curr_dict[curr] = curr_name

    # open the API URl and load the response
    with urllib.request.urlopen(json_url) as url:
        api_response = json.load(url)

    # extract the currency rate value from the APi response
    rate = api_response["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
 
    # calculate the requested currency pair values for both directions
    for item in range(1, 51):
        result1[item] = round(item * float(rate), 2)

    for item in range(1, 51):
        result2[item] = round(item / float(rate), 2)

    # pass the variables to the template file
    return render_template ("currency.html",
                            currency1=currency1,
                            currency2=currency2, 
                            rate=rate, 
                            result1=result1, 
                            result2=result2, 
                            curr_dict=curr_dict
                            )