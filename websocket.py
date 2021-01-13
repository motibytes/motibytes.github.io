import websocket, numpy, json
SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1h"
closes = []

def on_open(ws):
    print('Opening Connection')

def on_close(ws):
    print('Closed Connection')

def on_message(ws, message):
    global closes
    json_message = json.loads(message)
    candle = json_message['k']
    is_candle_closed = candle['c']
    close = candle['c']
    closes.append(float(close))
    np_closes = numpy.array(closes)
    print(np_closes)

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()
