from pycoingecko import CoinGeckoAPI
from influxdb import InfluxDBClient
import time 

cg = CoinGeckoAPI()
print ('Initializint...')

def writeMeasurement(value=None):
    try:
        client = InfluxDBClient(    host= "influxDB", 
                                    port=8086, 
                                    username="admin", 
                                    password="admin"
                                )
        client.create_database("superfarm")
        client.switch_database("superfarm")
        print("connected to influx")
    except:
        print('ERROR during connection with INFLUX DB')

    json_measurment = [{
        "measurement" : "superfarm_usd",
        "tags" : {
                "project": "crypto-spy",
                "content": "crypto-market-monitoring"
            },
            "time": int(time.time()) ,
            "fields": {
                "value": value
            }
        }]
    response = client.write_points(json_measurment , time_precision='ms')
    if response == True:
        return True
    else: print('something went wrong during storage of measurment : ')


# btc = (cg.get_price(ids='bitcoin', vs_currencies='usd'))
superFarm = (cg.get_price(ids='SuperFarm', vs_currencies='usd'))
# {'superfarm': {'usd': 1.18}}
usdPrice = superFarm["superfarm"]["usd"]
print(usdPrice)
writeMeasurement(value=usdPrice)
print('succesfull operation -> price : ' + str(usdPrice) + '    time : '+str(int(time.time())))
# time.sleep(15)
