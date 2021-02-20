from binance.client import Client
from binance.enums import *
import config

SOCKET = "wss://stream.binance.com:9443/ws/adausdt@kline_1m"

RSI_PERIOD = 14
RSI_OVERBOUGHT = 68
RSI_OVERSOLD = 39
TRADE_SYMBOL = 'ADAUSDT'
TRADE_QUANTITY = 20
SIDE_BUY = Client.SIDE_BUY
SIDE_SELL = Client.SIDE_SELL
closes = []
in_position = False

client = Client(config.API_KEY, config.API_SECRET)

def order(side, quantity, symbol,order_type=ORDER_TYPE_MARKET):
    try:
        print("sending order")
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(order)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False

    return True

order_succeeded = order(SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)

    
print(order)