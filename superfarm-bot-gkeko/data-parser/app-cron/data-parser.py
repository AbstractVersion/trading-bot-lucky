from pycoingecko import CoinGeckoAPI
from influxdb import InfluxDBClient
import time 

cg = CoinGeckoAPI()
print ('Initializint...')
coinlist = ['superfarm', 'bitcoin', 'ethereum' ,'terrausd', 'akash-network', 'cardano', 'spookyswap', 'thor', 'olympus', 'fantom']

def connectToInflux():
    try:
        client = InfluxDBClient(    host= "192.168.1.8", 
                                    port=8086, 
                                    username="admin", 
                                    password="sexmeup44"
                                )
        client.create_database("crypto-curency-raw")
        client.switch_database("crypto-curency-raw")
        print("connected to influx")
        return client
    except:
        print('ERROR during connection with INFLUX DB')
        return None

def writeMeasurement(value=None,coin=None, against=None, timestamp=None, client = None):

    print( 'coin : {} & price : {}'.format( coin,value))
    json_measurment = [{
        "measurement" : "coin_per_minute",
        "tags" : {
                "coin": coin,
                "against": against
            },
            "time": timestamp ,
            "fields": {
                "price": float(value)
            }
        }]
    response = client.write_points(json_measurment , time_precision='ms')
    if response == True:
        return True
    else: print('something went wrong during storage of measurment : ')


def getCurrentCoinPrices(currency='usd'):
    client = connectToInflux()
    for d in coinlist:
        data = (cg.get_price(ids=d, vs_currencies=currency))
        price = data[d][currency]
        print( 'coin : {} & price : {}'.format( d,price))
        writeMeasurement(value=price,coin=d, against=currency, timestamp= int(time.time()), client=client) 
        print ('appended')   

getCurrentCoinPrices()
# print('succesfull operation -> price : ' + str(usdPrice) + '    time : '+str(int(time.time())))
# time.sleep(15)
