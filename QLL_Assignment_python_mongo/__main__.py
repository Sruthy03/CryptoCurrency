from src import cryptoprices,hourlyData

user_input=4
while user_input!='3':

    user_input = input(" 1.Current  prices of BTC, BSC, Ethereum in USD and GBP \n 2.Hourly Values of crypto \n 3.Quit From the App \n")
    if user_input == '1':
        cryptoprices.storeValuesIntoDB()
        cryptoprices.getValuesFromDB()
    elif user_input == '2':
        x = input("Enter the crypto 1.BTC 2.BSC 3.ETD(Ethereum)\n")
        if x == '1':
            x = "BTC"
        elif x == '2':
            x = "BSC"
        else:
            x = "ETH"
        y = input("Eneter the currency value to get the hourly high low opening and closing price 1.USD 2.GBP\n")
        if y == '1':
            y = 'USD'
        else:
            y = 'GBP'
        hourlyData.storeHourlyData(x, y)
        hourlyData.getvaluesFromDB()

    else:
        if user_input not in ('1','2','3'):
            print("Please Enter the valid input 1 /2 /3 ")
        else:
            print("Existing the App!!!")
            break





# output = hourlyData.getvaluesFromDB()
