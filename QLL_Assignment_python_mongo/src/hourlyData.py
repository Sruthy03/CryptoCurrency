

from datetime import datetime
import pymongo
import requests
import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["crypto"]
mycol = mydb["dataHourly"]

# Defining Binance API URL
key = "https://min-api.cryptocompare.com/data/v2/histohour?fsym="
params ="{}&tsym={}&limit=24&aggregate=1&e=CCCAGG"

#To Store data From Api to MongoDb
def storeHourlyData(crypto,values):
    data = requests.get(key + (params.format(crypto,values)))
    data =data.json()
    data['crypto'] = crypto
    data['values'] = values
    mycol.insert_one(data)

#To Store Get Data From DB
def getvaluesFromDB():
    result = mycol.find().sort('_id',-1)
    count =0;
    for x in result:
        if(x['Response'] != 'Error'):
            if count == 0:
                print(x)
                count += count + 1
                print("Hourly values of {} in {}".format(x['crypto'], x['values']))
                list = x['Data']['Data']
                print('Date \t\tTime \t\t High \t\t Low \t\t open \t\t close')
                for x in list:
                    date_time = datetime.datetime.fromtimestamp(x['time'])
                    print("{}\t{}\t{}\t{}\t{}".format(date_time, x['high'], x['low'], x['open'], x['close']))





