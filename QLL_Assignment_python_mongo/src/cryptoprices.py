# Import libraries

import requests
from datetime import datetime
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["crypto"]
mycol = mydb["cryptoprices"]
key = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BSC,BTC,ETH&tsyms=USD,GBP"


now = datetime.now()
current_date = now.date()
current_time = now.time()


def getValuesFromDB():
    result = mycol.find().sort('_id',-1)
    count =0;
    for x in result:
        if(count==0):

            print("BTC \n USD :{}\tGBP\t:{}".format(x['BTC']['USD'],x['BTC']['GBP']))
            print("BSC \n USD :{}\tGBP\t:{}".format(x['BSC']['USD'],x['BSC']['GBP']))
            print("Ethereum  \n USD :{}\tGBP\t:{}".format(x['ETH']['USD'],x['ETH']['GBP']))



            count+=count+1


def storeValuesIntoDB():
    # Defining Binance API URL
    data = requests.get(key)
    data = data.json()
    data['date'] = current_date.strftime('%Y-%m-%d')
    data['time'] = current_time.strftime("%H:%M:%S")

    # Adding the data to DB collection in Mongo
    mycol.insert_one(data)






